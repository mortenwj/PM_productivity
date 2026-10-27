"""Extract searchable plain text from docs/tender-reference/source/ into extracted/.



Walks subfolders (e.g. NND/, KUM-SLKS/, Nationalbanken/). Writes INDEX.md.

"""

from __future__ import annotations



import json

import re

import zipfile

import xml.etree.ElementTree as ET

from dataclasses import dataclass, asdict

from datetime import datetime, timezone

from pathlib import Path



REPO_ROOT = Path(__file__).resolve().parents[2]

SOURCE_DIR = REPO_ROOT / "docs" / "tender-reference" / "source"

OUT_DIR = REPO_ROOT / "docs" / "tender-reference" / "extracted"

INDEX_PATH = REPO_ROOT / "docs" / "tender-reference" / "INDEX.md"



W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

X_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"



SUPPORTED = {".docx", ".xlsx", ".pdf"}





@dataclass

class FileIndexEntry:

    rel_source: str

    rel_extracted: str | None

    ext: str

    size_bytes: int

    tender: str

    extract_chars: int

    extract_status: str  # ok | skipped | failed

    notes: str = ""





def tender_from_path(rel: Path) -> str:

    parts = rel.parts

    if len(parts) > 1:

        return parts[0]

    return "(root)"





def extract_docx(filepath: Path) -> str:

    lines: list[str] = []

    with zipfile.ZipFile(filepath, "r") as z:

        with z.open("word/document.xml") as f:

            root = ET.parse(f).getroot()

    for body in root.findall(f".//{{{W_NS}}}body"):

        for p in body.findall(f"{{{W_NS}}}p"):

            texts: list[str] = []

            for node in p.iter():

                if node.tag.endswith("}t") and node.text is not None:

                    texts.append(node.text)

                if node.tag.endswith("}tab"):

                    texts.append("\t")

            if texts:

                line = "".join(texts).strip()

                if line:

                    lines.append(line)

    text = "\n".join(lines)

    return re.sub(r"\n{3,}", "\n\n", text)





def _xlsx_shared_strings(z: zipfile.ZipFile) -> list[str]:

    if "xl/sharedStrings.xml" not in z.namelist():

        return []

    with z.open("xl/sharedStrings.xml") as f:

        root = ET.parse(f).getroot()

    strings: list[str] = []

    for si in root.findall(f".//{{{X_NS}}}si"):

        parts: list[str] = []

        for t in si.iter(f"{{{X_NS}}}t"):

            if t.text:

                parts.append(t.text)

        strings.append("".join(parts))

    return strings





def extract_xlsx(filepath: Path) -> str:

    rows: list[str] = []

    with zipfile.ZipFile(filepath, "r") as z:

        shared = _xlsx_shared_strings(z)

        sheet_names = sorted(

            n for n in z.namelist() if n.startswith("xl/worksheets/sheet") and n.endswith(".xml")

        )

        for sheet_path in sheet_names:

            with z.open(sheet_path) as f:

                root = ET.parse(f).getroot()

            sheet_label = sheet_path.rsplit("/", 1)[-1]

            rows.append(f"## {sheet_label}")

            for row in root.findall(f".//{{{X_NS}}}row"):

                cells: list[str] = []

                for cell in row.findall(f"{{{X_NS}}}c"):

                    value = cell.find(f"{{{X_NS}}}v")

                    if value is None or value.text is None:

                        continue

                    raw = value.text

                    if cell.get("t") == "s" and shared:

                        try:

                            raw = shared[int(raw)]

                        except (ValueError, IndexError):

                            pass

                    cells.append(raw.strip())

                if cells:

                    rows.append("\t".join(cells))

    text = "\n".join(rows)

    return re.sub(r"\n{3,}", "\n\n", text)





def extract_pdf(filepath: Path) -> str:

    try:

        from pypdf import PdfReader

    except ImportError as e:

        raise RuntimeError("pypdf not installed; run: uv add pypdf && uv sync") from e



    reader = PdfReader(str(filepath))

    parts: list[str] = []

    for i, page in enumerate(reader.pages, start=1):

        text = page.extract_text() or ""

        text = text.strip()

        if text:

            parts.append(f"## Page {i}\n{text}")

    return re.sub(r"\n{3,}", "\n\n", "\n\n".join(parts))





def extract_file(filepath: Path) -> str:

    suffix = filepath.suffix.lower()

    if suffix == ".docx":

        return extract_docx(filepath)

    if suffix == ".xlsx":

        return extract_xlsx(filepath)

    if suffix == ".pdf":

        return extract_pdf(filepath)

    raise ValueError(f"Unsupported: {suffix}")





def rel_posix(path: Path, base: Path) -> str:

    return path.relative_to(base).as_posix()





def clean_stale_extracts(valid_extracted: set[Path]) -> int:

    removed = 0

    if not OUT_DIR.is_dir():

        return 0

    for txt in OUT_DIR.rglob("*.txt"):

        if txt not in valid_extracted:

            txt.unlink()

            removed += 1

    for empty in sorted(OUT_DIR.rglob("*"), reverse=True):

        if empty.is_dir() and not any(empty.iterdir()):

            empty.rmdir()

    return removed





def write_index(entries: list[FileIndexEntry]) -> None:

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    by_tender: dict[str, list[FileIndexEntry]] = {}

    for e in entries:

        by_tender.setdefault(e.tender, []).append(e)



    lines = [

        "# Tender reference index",

        "",

        f"**Generated:** {now} by `toolkit/scripts/extract_tender_reference.py`",

        "",

        "Search **`extracted/`** (mirror of `source/` layout). Regenerate after source changes:",

        "",

        "```powershell",

        "uv run python toolkit/scripts/extract_tender_reference.py",

        "```",

        "",

        "## Summary",

        "",

        f"| Metric | Value |",

        f"|--------|-------|",

        f"| Source files | {len(entries)} |",

        f"| Extracted OK | {sum(1 for e in entries if e.extract_status == 'ok')} |",

        f"| Failed / skipped | {sum(1 for e in entries if e.extract_status != 'ok')} |",

        f"| Tenders / folders | {len(by_tender)} |",

        "",

    ]



    for tender in sorted(by_tender.keys(), key=lambda t: (t == "(root)", t)):

        lines.append(f"## {tender}")

        lines.append("")

        lines.append("| Source | Extracted | Size | Chars | Status | Notes |")

        lines.append("|--------|-----------|------|-------|--------|-------|")

        for e in sorted(by_tender[tender], key=lambda x: x.rel_source):

            size_kb = f"{e.size_bytes // 1024} KB"

            chars = str(e.extract_chars) if e.extract_chars else "—"

            ext_rel = e.rel_extracted or "—"

            notes = e.notes.replace("|", "\\|")

            lines.append(

                f"| `{e.rel_source}` | `{ext_rel}` | {size_kb} | {chars} | {e.extract_status} | {notes} |"

            )

        lines.append("")



    lines.extend(

        [

            "## Use when drafting",

            "",

            "| Tender | Primary files |",

            "|--------|----------------|",

            "| **(root)** | `KK Tender tool.xlsx` — KK compliance matrix; granskning krav map |",

            "| **FHM** | Forsvarshistorisk Museum — konkurransegrunnlag del III, ansvarsmatrise/kravsvar, tjenestebeskrivelse |",

            "| **NND** | `02.01-…kravtabell.docx` — full Norwegian kravtabell answers |",

            "| **HSØ** | `02.00-…beskrivelse av Tjenesten.docx` — service description |",

            "| **KUM-SLKS** | `Bilag 3 - Kravspecifikation.docx`, processtyring bilag — Danish KK cluster |",

            "| **Nationalbanken** | PDF bilag — solution descriptions, implementation, security questionnaire |",

            "",

        ]

    )



    INDEX_PATH.write_text("\n".join(lines), encoding="utf-8")





def main() -> None:

    if not SOURCE_DIR.is_dir():

        raise SystemExit(f"Source folder missing: {SOURCE_DIR}")



    OUT_DIR.mkdir(parents=True, exist_ok=True)

    entries: list[FileIndexEntry] = []

    valid_extracted: set[Path] = set()



    sources = sorted(

        p for p in SOURCE_DIR.rglob("*") if p.is_file() and p.suffix.lower() in SUPPORTED

    )



    for src in sources:

        rel = Path(rel_posix(src, SOURCE_DIR))

        out_path = OUT_DIR / rel.with_suffix(".txt")

        entry = FileIndexEntry(

            rel_source=rel_posix(src, SOURCE_DIR),

            rel_extracted=None,

            ext=src.suffix.lower(),

            size_bytes=src.stat().st_size,

            tender=tender_from_path(rel),

            extract_chars=0,

            extract_status="skipped",

        )



        if src.suffix.lower() not in SUPPORTED:

            entry.notes = "unsupported extension"

            entries.append(entry)

            continue



        try:

            text = extract_file(src)

            out_path.parent.mkdir(parents=True, exist_ok=True)

            out_path.write_text(text, encoding="utf-8")

            entry.rel_extracted = rel_posix(out_path, OUT_DIR)

            entry.extract_chars = len(text)

            entry.extract_status = "ok" if text.strip() else "ok-empty"

            print(f"Extracted: {entry.rel_source} -> {entry.rel_extracted} ({entry.extract_chars} chars)")

            valid_extracted.add(out_path)

        except Exception as exc:

            entry.extract_status = "failed"

            entry.notes = str(exc)[:120]

            print(f"FAILED: {entry.rel_source}: {exc}")



        entries.append(entry)



    removed = clean_stale_extracts(valid_extracted)

    write_index(entries)



    manifest = OUT_DIR / "_index.json"

    manifest.write_text(

        json.dumps([asdict(e) for e in entries], indent=2, ensure_ascii=False),

        encoding="utf-8",

    )



    print(f"Done. {len(sources)} source file(s), {removed} stale extract(s) removed.")

    print(f"Index: {INDEX_PATH}")





if __name__ == "__main__":

    main()


