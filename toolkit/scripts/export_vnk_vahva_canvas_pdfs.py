"""Export VNK-Vahva canvas content to print-ready PDF via Edge headless.

Usage (from repo root):

    uv run python toolkit/scripts/export_vnk_vahva_canvas_pdfs.py
"""
from __future__ import annotations

import html
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
EXPORT_DIR = REPO_ROOT / "docs" / "tender-reference" / "export"
BRIEF_MD = REPO_ROOT / "docs" / "tender-reference" / "VNK-Vahva-management-gate-brief.md"

EDGE_CANDIDATES = [
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
]

PRINT_CSS = """
@page { size: A4 landscape; margin: 12mm; }
body { font-family: Segoe UI, DejaVu Sans, Arial, sans-serif; font-size: 9pt; line-height: 1.35; color: #111; }
h1 { font-size: 18pt; margin: 0 0 8pt; }
h2 { font-size: 12pt; margin: 14pt 0 6pt; page-break-after: avoid; }
h3 { font-size: 10.5pt; margin: 10pt 0 4pt; page-break-after: avoid; }
p, li { margin: 0 0 4pt; }
.meta { color: #444; font-size: 8.5pt; margin-bottom: 10pt; }
.callout { border: 1px solid #ccc; border-left: 4px solid #c0392b; padding: 8pt 10pt; margin: 10pt 0; background: #fdf6f6; }
.callout.info { border-left-color: #2980b9; background: #f4f8fc; }
.callout.warn { border-left-color: #d68910; background: #fef9f0; }
table { border-collapse: collapse; width: 100%; margin: 8pt 0; font-size: 8pt; }
th, td { border: 1px solid #bbb; padding: 3px 5px; vertical-align: top; text-align: left; }
th { background: #eef2f7; font-weight: 600; }
tr:nth-child(even) td { background: #fafafa; }
.gap-partial { color: #8a6d00; font-weight: 600; }
.roadmap-a { background: #eefaf0; }
.roadmap-b { background: #fff8e6; }
.roadmap-c { background: #fdecea; }
.stats { display: grid; grid-template-columns: repeat(5, 1fr); gap: 8pt; margin: 10pt 0; }
.stat { border: 1px solid #ccc; padding: 8pt; border-radius: 4px; }
.stat .val { font-size: 14pt; font-weight: 700; }
.stat .lbl { font-size: 8pt; color: #555; }
"""


def roadmap_row_class(roadmap: str) -> str:
    if roadmap.startswith("A"):
        return "roadmap-a"
    if roadmap.startswith("B"):
        return "roadmap-b"
    if roadmap.startswith("C"):
        return "roadmap-c"
    return "roadmap-d"


PFR_ROWS: list[dict[str, str]] = [
    {"id": "437273", "ref": "A12–A14 / API", "title": "360° API requirements (API-first / new SIF)", "cluster": "API / integration platform", "size": "XL", "gap": "Partial", "risk": "High", "owner": "Mika / Tero", "roadmap": "C — Strategic", "roadmap_ref": "NG Integration API / 360° API Gateway", "note": "Post–Innovation Board"},
    {"id": "430281", "ref": "F-section", "title": "Metadata — language, length, inheritance, infosec", "cluster": "Metadata / TOS", "size": "L", "gap": "Partial", "risk": "High", "owner": "Willy Koch", "roadmap": "B — Accelerate", "roadmap_ref": "Custom fields / metadata model", "note": "111 Liite 2.3 reqs in F"},
    {"id": "433271", "ref": "B7–B10, E48", "title": "Mass functions", "cluster": "Mass operations", "size": "L", "gap": "Partial", "risk": "Medium", "owner": "—", "roadmap": "B — Accelerate", "roadmap_ref": "Mass update", "note": ""},
    {"id": "434693", "ref": "I-section", "title": "Search — wildcard, saved-search sharing", "cluster": "Search / FFUI", "size": "L", "gap": "Partial", "risk": "Medium", "owner": "Willy Koch", "roadmap": "B — Accelerate", "roadmap_ref": "Refactor search experience", "note": ""},
    {"id": "430271", "ref": "E-dispatch", "title": "Enhanced dispatch", "cluster": "Dispatch / notifications", "size": "L", "gap": "Partial", "risk": "Medium", "owner": "Olga Safonova", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": "Commitment; Conditional"},
    {"id": "432904", "ref": "E21–E26", "title": "Enhanced email notifications", "cluster": "Dispatch / notifications", "size": "M", "gap": "Partial", "risk": "Medium", "owner": "—", "roadmap": "A — Aligns", "roadmap_ref": "New Outlook Support", "note": ""},
    {"id": "430291", "ref": "E-notify", "title": "Email configurability (ORPHAN)", "cluster": "Dispatch / notifications", "size": "M", "gap": "Partial", "risk": "Medium", "owner": "Jarle Steira", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": "Not on epic #436815"},
    {"id": "433354", "ref": "B58", "title": "Template filtering FI/SV", "cluster": "Templates / document UX", "size": "M", "gap": "Partial", "risk": "Low", "owner": "—", "roadmap": "B — Accelerate", "roadmap_ref": "Full Flex UI / templates", "note": "Only child of epic"},
    {"id": "433356", "ref": "B66, H", "title": "Draft file version disposal", "cluster": "Archiving / disposal", "size": "M", "gap": "Partial", "risk": "Medium", "owner": "—", "roadmap": "C — Strategic", "roadmap_ref": "Retention / disposal", "note": ""},
]


def find_edge() -> Path:
    for candidate in EDGE_CANDIDATES:
        if candidate.is_file():
            return candidate
    raise FileNotFoundError("Microsoft Edge not found")


def is_table_separator(line: str) -> bool:
    stripped = line.strip()
    if not stripped.startswith("|"):
        return False
    inner = stripped.strip("|")
    return bool(inner) and all(ch in "-:| " for ch in inner)


def inline_md(text: str) -> str:
    escaped = html.escape(text)
    parts = escaped.split("**")
    for idx in range(1, len(parts), 2):
        parts[idx] = f"<strong>{parts[idx]}</strong>"
    return "".join(parts)


def md_to_simple_html(md_text: str) -> str:
    lines = md_text.splitlines()
    out: list[str] = []
    in_table = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("# "):
            out.append(f"<h1>{html.escape(line[2:])}</h1>")
        elif line.startswith("## "):
            out.append(f"<h2>{html.escape(line[3:])}</h2>")
        elif line.startswith("### "):
            out.append(f"<h3>{html.escape(line[4:])}</h3>")
        elif line.strip() == "---":
            out.append("<hr/>")
        elif line.startswith("|") and "|" in line[1:]:
            if is_table_separator(line):
                i += 1
                continue
            if not in_table:
                in_table = True
                out.append("<table>")
            cells = [c.strip() for c in line.strip("|").split("|")]
            tag = "th" if out[-1] == "<table>" else "td"
            row = "".join(f"<{tag}>{inline_md(c)}</{tag}>" for c in cells)
            out.append(f"<tr>{row}</tr>")
        else:
            if in_table:
                out.append("</table>")
                in_table = False
            stripped = line.strip()
            if not stripped:
                i += 1
                continue
            if stripped.startswith("- "):
                items = []
                while i < len(lines) and lines[i].strip().startswith("- "):
                    items.append(f"<li>{inline_md(lines[i].strip()[2:])}</li>")
                    i += 1
                out.append("<ul>" + "".join(items) + "</ul>")
                continue
            out.append(f"<p>{inline_md(stripped)}</p>")
        i += 1
    if in_table:
        out.append("</table>")
    return "\n".join(out)


def wrap_html(title: str, body: str, landscape: bool = False) -> str:
    page = "@page { size: A4 landscape; margin: 12mm; }" if landscape else "@page { size: A4; margin: 18mm; }"
    css = PRINT_CSS.replace("@page { size: A4 landscape; margin: 12mm; }", page)
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"/><title>{html.escape(title)}</title>
<style>{css}</style></head><body>{body}</body></html>"""


def build_management_html() -> str:
    md = BRIEF_MD.read_text(encoding="utf-8")
    return wrap_html("VNK-Vahva management go/no-go brief", md_to_simple_html(md), landscape=False)


def build_heatmap_html() -> str:
    gap_counts = {"Partial": len(PFR_ROWS)}
    roadmap_counts = {"A — Aligns": 0, "B — Accelerate": 0, "C — Strategic": 0, "D — Low priority": 0}
    for row in PFR_ROWS:
        roadmap_counts[row["roadmap"]] = roadmap_counts.get(row["roadmap"], 0) + 1

    rows_html = []
    for row in PFR_ROWS:
        cls = roadmap_row_class(row["roadmap"])
        rows_html.append(
            f"<tr class='{cls}'>"
            f"<td>{row['id']}</td><td>{html.escape(row['ref'])}</td>"
            f"<td>{html.escape(row['title'])}</td>"
            f"<td>{html.escape(row['roadmap'])}</td>"
            f"<td>{html.escape(row['roadmap_ref'])}</td>"
            f"<td>{html.escape(row['cluster'])}</td><td>{row['size']}</td>"
            f"<td class='gap-partial'>{html.escape(row['gap'])}</td>"
            f"<td>{row['risk']}</td><td>{html.escape(row['owner'])}</td>"
            f"<td>{html.escape(row['note'])}</td>"
            f"</tr>"
        )

    body = f"""
<h1>VNK-Vahva — commitment heatmap</h1>
<p class="meta">VN Asia (Valtioneuvoston kanslia / Valtori) · Epic #436815 · 9 PFRs · Liite 2.3: 487 reqs (416 Pakollinen) · verified 4 Sep 2026</p>
<div class="callout warn"><strong>Coverage warning:</strong> 9 registered PFRs vs 487 functional requirements (~2%). Unregistered: Suomi.fi (A15), eIDAS (C21), multi-org (A2–A7), Liite 2.6 security.</div>
<div class="stats">
  <div class="stat"><div class="val">487</div><div class="lbl">Liite 2.3 reqs</div></div>
  <div class="stat"><div class="val">9</div><div class="lbl">Registered PFRs</div></div>
  <div class="stat"><div class="val">{gap_counts['Partial']}</div><div class="lbl">Partial (RFI evidence)</div></div>
  <div class="stat"><div class="val">55–90 mo</div><div class="lbl">PFR portfolio effort</div></div>
  <div class="stat"><div class="val">1 XL</div><div class="lbl">#437273 API</div></div>
</div>
<div class="callout info"><strong>Roadmap alignment:</strong>
A {roadmap_counts['A — Aligns']} · B {roadmap_counts['B — Accelerate']} · C {roadmap_counts['C — Strategic']} · D {roadmap_counts['D — Low priority']}.</div>
<h2>PFR portfolio detail</h2>
<table>
<thead><tr>
<th>ID</th><th>Ref</th><th>Title</th><th>Roadmap</th><th>Roadmap ref</th><th>Cluster</th><th>Size</th>
<th>Gap</th><th>Risk</th><th>Owner</th><th>Notes</th>
</tr></thead>
<tbody>{''.join(rows_html)}</tbody>
</table>
"""
    return wrap_html("VNK-Vahva commitment heatmap", body, landscape=True)


def print_pdf(edge: Path, html_path: Path, pdf_path: Path) -> None:
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    uri = html_path.resolve().as_uri()
    cmd = [
        str(edge),
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=10000",
        f"--print-to-pdf={pdf_path.resolve()}",
        uri,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0 or not pdf_path.is_file():
        raise RuntimeError(f"Edge PDF export failed: {result.stderr}")


def main() -> int:
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    edge = find_edge()
    exports = [
        ("vnk-vahva-management-gate", build_management_html(), False),
        ("vnk-vahva-commitment-heatmap", build_heatmap_html(), True),
    ]
    for stem, html_content, _ in exports:
        html_path = EXPORT_DIR / f"{stem}.html"
        pdf_path = EXPORT_DIR / f"{stem}.pdf"
        html_path.write_text(html_content, encoding="utf-8")
        print_pdf(edge, html_path, pdf_path)
        print(pdf_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
