"""Extract slide text from a .pptx file."""
from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile

NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}


def extract(pptx: Path) -> list[tuple[int, list[str]]]:
    with ZipFile(pptx) as z:
        slides = sorted(
            [n for n in z.namelist() if n.startswith("ppt/slides/slide") and n.endswith(".xml")],
            key=lambda s: int(re.search(r"slide(\d+)", s).group(1)),
        )
        out: list[tuple[int, list[str]]] = []
        for slide_path in slides:
            num = int(re.search(r"slide(\d+)", slide_path).group(1))
            root = ET.fromstring(z.read(slide_path))
            texts = [t.text.strip() for t in root.findall(".//a:t", NS) if t.text and t.text.strip()]
            out.append((num, texts))
        return out


def main() -> int:
    pptx = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(r"C:\Users\MortenJensen\Downloads\roadmap_tech_added.pptx")
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    if not pptx.is_file():
        print(f"Missing file: {pptx}", file=sys.stderr)
        return 1
    slides = extract(pptx)
    lines: list[str] = [f"Slides: {len(slides)}\n"]
    for num, texts in slides:
        lines.append(f"=== Slide {num} ===")
        lines.extend(texts)
        lines.append("")
    body = "\n".join(lines)
    if out_path:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(body, encoding="utf-8")
    else:
        sys.stdout.buffer.write(body.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
