#!/usr/bin/env python3
"""
Analyze .wu (Work Unit) files in the workunit analysis folder.
Produces:
1. Summary of workunits and categories
2. Workunits using xscript (require special attention)
3. Executables with no file names or entry points

Excludes workunits that exist in standardworkunits (delta analysis only).
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from collections import defaultdict

WU_DIR = Path(__file__).parent / "workunit analysis" / "ROK wu files"
STANDARD_WU_DIR = Path(__file__).parent / "workunit analysis" / "standardworkunits"
XAML_DIR = Path(__file__).parent / "workunit analysis" / "ROK xaml files"


def get_standard_workunit_names() -> set[str]:
    """Get set of .wu filenames in standardworkunits (used for exclusion)."""
    names = set()
    if STANDARD_WU_DIR.exists():
        for fp in STANDARD_WU_DIR.rglob("*.wu"):
            names.add(fp.name)
    return names


def get_xaml_basenames() -> set[str]:
    """Get set of .xaml basenames (stem) for matching. e.g. test.xaml -> test."""
    names = set()
    if XAML_DIR.exists():
        for fp in XAML_DIR.glob("*.xaml"):
            names.add(fp.stem)
    return names


def parse_wu_file(filepath: Path) -> dict | None:
    """Parse a .wu file and extract relevant info. Returns None on parse error."""
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
    except ET.ParseError:
        return None

    # Handle both workUnit and workunit (case may vary)
    if root.tag not in ("workUnit", "WorkUnit"):
        return None

    result = {
        "file": filepath.name,
        "displayName": root.get("displayName", ""),
        "id": root.get("id", ""),
        "categories": [],
        "executable": {},
        "raw_executable": "",
    }

    # Extract categories
    categories_el = root.find("categories")
    if categories_el is not None:
        for cat in categories_el.findall("category"):
            if cat.text and cat.text.strip():
                result["categories"].append(cat.text.strip())

    # Extract executable section
    exec_el = root.find("executable")
    if exec_el is not None:
        result["executable"]["file"] = exec_el.get("file")
        result["executable"]["assemblyType"] = exec_el.get("assemblyType")

        # Check for xscript
        xscript = exec_el.find("xscript")
        if xscript is not None:
            result["executable"]["has_xscript"] = True
            result["executable"]["xscript_entryPoint"] = xscript.get("entryPoint")
            result["executable"]["xscript_language"] = xscript.get("language")
        else:
            result["executable"]["has_xscript"] = False

        # Check for invoke (empty or not)
        invoke = exec_el.find("invoke")
        wf = exec_el.find("wf")

        result["executable"]["has_invoke"] = invoke is not None
        result["executable"]["has_wf"] = wf is not None

        # Determine if executable has no file/entry point
        has_file = bool(result["executable"]["file"])
        has_assembly = bool(result["executable"]["assemblyType"])
        has_entry = bool(result["executable"].get("xscript_entryPoint"))

        result["executable"]["has_reference"] = has_file or has_assembly or has_entry

    return result


def main():
    standard_names = get_standard_workunit_names()
    wu_files = sorted(WU_DIR.glob("*.wu"))
    # Exclude workunits that exist in standardworkunits (delta only)
    wu_files = [fp for fp in wu_files if fp.name not in standard_names]
    excluded_count = len(list(WU_DIR.glob("*.wu"))) - len(wu_files)

    if not wu_files:
        print(f"No .wu files to analyze (all excluded by standardworkunits)")
        return

    all_data = []
    for fp in wu_files:
        data = parse_wu_file(fp)
        if data:
            all_data.append(data)

    print("=" * 70)
    print("DELTA ANALYSIS: ROK wu files NOT in standardworkunits")
    print("=" * 70)
    print(f"Analyzing {len(all_data)} workunits (excluded {excluded_count} found in standardworkunits)\n")

    # --- 1. Categories summary ---
    category_to_files = defaultdict(list)
    no_category = []
    for d in all_data:
        if d["categories"]:
            for cat in d["categories"]:
                category_to_files[cat].append(d["file"])
        else:
            no_category.append(d["file"])

    print("=" * 70)
    print("1. WORKUNITS BY CATEGORY")
    print("=" * 70)
    for cat in sorted(category_to_files.keys()):
        files = category_to_files[cat]
        print(f"\n  {cat} ({len(files)} workunits)")
        for f in sorted(files):
            print(f"    - {f}")

    print(f"\n  [No category] ({len(no_category)} workunits)")
    for f in sorted(no_category):
        print(f"    - {f}")

    # --- 2. xscript workunits (special attention) ---
    xscript_files = [d for d in all_data if d["executable"].get("has_xscript")]
    print("\n" + "=" * 70)
    print("2. WORKUNITS USING XSCRIPT (require special attention)")
    print("=" * 70)
    print(f"\nTotal: {len(xscript_files)} workunits\n")
    for d in xscript_files:
        ep = d["executable"].get("xscript_entryPoint", "(none)")
        lang = d["executable"].get("xscript_language", "")
        print(f"  {d['file']}")
        print(f"    entryPoint: {ep}")
        print(f"    language: {lang}")
        print()

    # --- 3. Executables with no file names or entry points ---
    empty_exec = []
    for d in all_data:
        ex = d["executable"]
        if not ex:
            continue
        has_ref = ex.get("has_reference", False)
        has_invoke = ex.get("has_invoke", False)
        has_wf = ex.get("has_wf", False)

        # Empty: has invoke but no file, assemblyType, or xscript entryPoint
        if has_invoke and not has_ref and not has_wf:
            empty_exec.append(d)

    # Exclude from empty_exec those that have a matching .xaml file (same basename)
    xaml_basenames = get_xaml_basenames()
    empty_exec_no_xaml = []
    empty_exec_with_xaml = []
    for d in empty_exec:
        wu_stem = Path(d["file"]).stem  # e.g. "test" from "test.wu"
        if wu_stem in xaml_basenames:
            empty_exec_with_xaml.append(d)
        else:
            empty_exec_no_xaml.append(d)

    # All delta workunits with matching xaml (regardless of executable type)
    all_with_matching_xaml = [d for d in all_data if Path(d["file"]).stem in xaml_basenames]

    print("=" * 70)
    print("3. EXECUTABLES WITH NO FILE NAMES OR ENTRY POINTS")
    print("=" * 70)
    print("\nThese workunits have <invoke> but no file=, assemblyType=, or xscript entryPoint.")
    print("Excludes those with a matching .xaml file (workflow defined elsewhere).")
    print("They may be placeholders, misconfigured, or require manual setup.\n")
    print(f"Total: {len(empty_exec_no_xaml)} workunits\n")
    for d in empty_exec_no_xaml:
        print(f"  - {d['file']}")
        if d.get("displayName"):
            print(f"    displayName: {d['displayName'][:60]}...")
        print()

    # --- 3b. All workunits with matching XAML ---
    print("=" * 70)
    print("3b. WORKUNITS WITH MATCHING XAML FILE")
    print("=" * 70)
    print("\nThese workunits have a corresponding .xaml file with the same name")
    print("(e.g. DigitalPost.wu <-> DigitalPost.xaml). Workflow may be defined in XAML.\n")
    print(f"Total: {len(all_with_matching_xaml)} workunits\n")
    for d in all_with_matching_xaml:
        print(f"  {d['file']} <-> {Path(d['file']).stem}.xaml")
        if d.get("displayName"):
            print(f"    displayName: {d['displayName'][:60]}...")
        print()

    # Summary stats
    print("=" * 70)
    print("SUMMARY (Delta: ROK wu files minus standardworkunits)")
    print("=" * 70)
    print(f"  Total .wu files analyzed (delta): {len(all_data)}")
    print(f"  Excluded (in standardworkunits): {excluded_count}")
    print(f"  Unique categories: {len(category_to_files)}")
    print(f"  Workunits with xscript: {len(xscript_files)}")
    print(f"  Executables with no reference: {len(empty_exec_no_xaml)}")
    print(f"  Workunits with matching xaml: {len(all_with_matching_xaml)}")


if __name__ == "__main__":
    main()
