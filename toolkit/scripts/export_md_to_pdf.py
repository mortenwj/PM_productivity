"""One-off: Markdown -> HTML -> PDF via xhtml2pdf. Usage: py -3 export_md_to_pdf.py <file.md>"""
from __future__ import annotations

import sys
from pathlib import Path

import markdown
from xhtml2pdf import pisa


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: py -3 export_md_to_pdf.py <input.md>", file=sys.stderr)
        return 2
    md_path = Path(sys.argv[1]).resolve()
    if not md_path.is_file():
        print(f"Not found: {md_path}", file=sys.stderr)
        return 1
    out_path = md_path.with_suffix(".pdf")
    text = md_path.read_text(encoding="utf-8")
    body = markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "nl2br", "sane_lists"],
    )
    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"/>
<style>
@page {{ size: A4; margin: 18mm; }}
body {{ font-family: DejaVu Sans, Helvetica, Arial, sans-serif; font-size: 9pt; line-height: 1.35; }}
h1 {{ font-size: 16pt; page-break-after: avoid; }}
h2 {{ font-size: 12pt; page-break-after: avoid; margin-top: 12pt; }}
h3 {{ font-size: 10.5pt; page-break-after: avoid; margin-top: 10pt; }}
h4 {{ font-size: 10pt; page-break-after: avoid; }}
table {{ border-collapse: collapse; width: 100%; margin: 8pt 0; page-break-inside: avoid; }}
th, td {{ border: 1px solid #bbb; padding: 4px 6px; vertical-align: top; }}
th {{ background: #f0f0f0; font-weight: bold; }}
code, pre {{ font-family: DejaVu Sans Mono, Consolas, monospace; font-size: 8.5pt; }}
pre {{ background: #f6f8fa; padding: 8px; border: 1px solid #e1e4e8; white-space: pre-wrap; }}
a {{ color: #0969da; word-wrap: break-word; }}
blockquote {{ margin: 0 0 0 8px; padding-left: 8px; border-left: 3px solid #ddd; color: #444; }}
hr {{ border: none; border-top: 1px solid #ccc; margin: 12pt 0; }}
ul, ol {{ margin-top: 4pt; margin-bottom: 6pt; }}
</style></head><body>{body}</body></html>"""

    with out_path.open("wb") as f:
        status = pisa.CreatePDF(html.encode("utf-8"), dest=f, encoding="utf-8")
    if status.err:
        print(f"xhtml2pdf reported errors; output may be incomplete: {out_path}", file=sys.stderr)
        return 1
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
