"""Fix em-dash mojibake (â€") in Process Platform check-in pptx files."""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path

# UTF-8 mojibake when em dash was double-encoded / mis-handled via PowerPoint COM
MOJIBAKE_REPLACEMENTS: list[tuple[bytes, bytes]] = [
    (b"\xc3\xa2\xe2\x82\xac\xe2\x80\x9d", b" - "),  # â€"
    (b"\xc3\xa2\xe2\x82\xac\xe2\x80\x94", b" - "),  # â€— variant
    (b"\xc3\xa2\xe2\x82\xac\"", b" - "),
]

TEXT_REPLACEMENTS: list[tuple[str, str]] = [
    ("\u2014", " - "),  # em dash
    ("\u2013", " - "),  # en dash
    ("\u00e2\u20ac\u201d", " - "),  # mojibake â€"
    ("\u00e2\u20ac\u201c", " - "),  # mojibake â€"
    ("\u00e2\u20ac\u2014", " - "),  # mojibake â€—
]


def fix_bytes(data: bytes) -> tuple[bytes, int]:
    count = 0
    for bad, good in MOJIBAKE_REPLACEMENTS:
        n = data.count(bad)
        if n:
            count += n
            data = data.replace(bad, good)
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return data, count
    original = text
    for bad, good in TEXT_REPLACEMENTS:
        if bad in text:
            count += text.count(bad)
            text = text.replace(bad, good)
    if text != original:
        data = text.encode("utf-8")
    return data, count


def fix_pptx(path: Path, output: Path | None = None) -> int:
    out = output or path
    total = 0
    tmp = path.with_suffix(".pptx.tmp")
    with zipfile.ZipFile(path, "r") as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename.endswith(".xml") or item.filename.endswith(".rels"):
                data, n = fix_bytes(data)
                total += n
            zout.writestr(item, data)
    tmp.replace(out)
    return total


def main() -> None:
    paths = [
        Path(r"C:\Users\MortenJensen\Downloads\Process Platform check-in 2026_updated.pptx"),
        Path(r"C:\Users\MortenJensen\Downloads\Process Platform check-in 2026_updated_regen.pptx"),
    ]
    if len(sys.argv) > 1:
        paths = [Path(p) for p in sys.argv[1:]]
    for p in paths:
        if not p.exists():
            print(f"skip (missing): {p}")
            continue
        n = fix_pptx(p)
        print(f"fixed {n} occurrence(s): {p}")


if __name__ == "__main__":
    main()
