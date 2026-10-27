"""
Process batch JSON files from wit_get_work_items_batch_by_ids to extract
Svenska kyrkan PFRs.

Usage:
  python process_svenska_kyrkan_batches.py batch_1.json batch_2.json ...
  python process_svenska_kyrkan_batches.py batch_*.json
  python process_svenska_kyrkan_batches.py  # uses batch_*.json in current dir

Input: Batch JSON files (output of Azure DevOps wit_get_work_items_batch_by_ids).
       Each file may have {"value": [...]} or a raw array of work items.

Output: svenska_kyrkan_full_query_result.json
        JSON array: id, title, state, assignedTo (displayName), customername
        Sorted by ID ascending.
"""

import argparse
import glob
import json
import re
import sys
from pathlib import Path

OUTPUT_FILE = "svenska_kyrkan_full_query_result.json"
EXCLUDE_ID_SVENSKA_INSTITUTET = 262489


def matches_svenska_kyrkan(customername: str) -> bool:
    """Check if Customername field contains Svenska kyrkan (any casing)."""
    if not customername or not isinstance(customername, str):
        return False
    return bool(re.search(r"svenska\s*kyrkan", customername, re.IGNORECASE))


def is_svenska_institutet_only(customername: str) -> bool:
    """Exclude if only Svenska institutet (different org, no Svenska kyrkan)."""
    if not customername or not isinstance(customername, str):
        return False
    c = customername.lower()
    return "svenska kyrkan" not in c and "svenska institutet" in c


def extract_work_items_from_batch(data) -> list:
    """Extract work item list from batch JSON (handles various formats)."""
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        if "value" in data:
            return data["value"]
        if "workItems" in data:
            return data["workItems"]
    return []


def to_output_item(wi: dict) -> dict:
    """Convert work item to output format: id, title, state, assignedTo, customername."""
    fields = wi.get("fields", {})
    wid = wi.get("id") or fields.get("System.Id")
    title = fields.get("System.Title") or ""
    state = fields.get("System.State") or ""
    assigned_to = fields.get("System.AssignedTo")
    if isinstance(assigned_to, dict):
        assigned_to = assigned_to.get("displayName") or ""
    elif assigned_to is None:
        assigned_to = ""
    else:
        assigned_to = str(assigned_to)
    customername = (
        fields.get("Custom.Customername")
        or fields.get("Custom.CustomerName")
        or ""
    )
    if customername is None:
        customername = ""
    return {
        "id": wid,
        "title": title,
        "state": state,
        "assignedTo": assigned_to,
        "customername": str(customername),
    }


def process_batch_files(paths: list[str]) -> list[dict]:
    """Process batch files and return filtered output items."""
    seen_ids = set()
    results = []

    for path in sorted(paths):
        p = Path(path)
        if not p.exists():
            print(f"Warning: {path} not found, skipping", file=sys.stderr)
            continue
        try:
            with open(p, encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Warning: {path} invalid JSON: {e}", file=sys.stderr)
            continue

        items = extract_work_items_from_batch(data)
        for wi in items:
            fields = wi.get("fields", {})
            customername = (
                fields.get("Custom.Customername")
                or fields.get("Custom.CustomerName")
                or ""
            )
            customername_str = str(customername or "")

            if not matches_svenska_kyrkan(customername_str):
                continue

            wid = wi.get("id") or fields.get("System.Id")
            if wid == EXCLUDE_ID_SVENSKA_INSTITUTET and is_svenska_institutet_only(
                customername_str
            ):
                continue

            if wid in seen_ids:
                continue
            seen_ids.add(wid)

            results.append(to_output_item(wi))

    return sorted(results, key=lambda x: x["id"])


def main():
    parser = argparse.ArgumentParser(
        description="Process batch JSON files to extract Svenska kyrkan PFRs"
    )
    parser.add_argument(
        "batches",
        nargs="*",
        help="Batch JSON files (e.g. batch_1.json batch_2.json). If none, uses batch_*.json",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=OUTPUT_FILE,
        help=f"Output file (default: {OUTPUT_FILE})",
    )
    args = parser.parse_args()

    if args.batches:
        paths = args.batches
    else:
        paths = sorted(glob.glob("batch_*.json"))
        if not paths:
            print(
                "No batch files found. Provide paths: python process_svenska_kyrkan_batches.py batch_1.json batch_2.json ...",
                file=sys.stderr,
            )
            sys.exit(1)

    print(f"Processing {len(paths)} batch file(s)...")
    results = process_batch_files(paths)
    print(f"Found {len(results)} Svenska kyrkan PFR(s)")

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"Saved to {args.output}")


if __name__ == "__main__":
    main()
