"""Export KK canvas content to print-ready PDF via Edge headless.

Usage (from repo root):

    uv run python toolkit/scripts/export_kk_canvas_pdfs.py
"""
from __future__ import annotations

import html
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
EXPORT_DIR = REPO_ROOT / "docs" / "tender-reference" / "export"
BRIEF_MD = REPO_ROOT / "docs" / "tender-reference" / "KK-management-gate-brief.md"

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
.risk-high td { background: #fdecea; }
.risk-med td { background: #fff8e6; }
.risk-low td { background: #eefaf0; }
.gap-not-met { color: #a1260d; font-weight: 600; }
.gap-partial, .gap-in-flight { color: #8a6d00; font-weight: 600; }
.gap-draft { color: #1f4e79; font-weight: 600; }
.roadmap-a { background: #eefaf0; }
.roadmap-b { background: #fff8e6; }
.roadmap-c { background: #fdecea; }
.roadmap-d { background: #fafafa; }
.stats { display: grid; grid-template-columns: repeat(5, 1fr); gap: 8pt; margin: 10pt 0; }
.stat { border: 1px solid #ccc; padding: 8pt; border-radius: 4px; }
.stat .val { font-size: 14pt; font-weight: 700; }
.stat .lbl { font-size: 8pt; color: #555; }
.small { font-size: 8pt; color: #555; }
.page-break { page-break-before: always; }
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
    {"id": "435490", "ref": "B2-12+", "title": "Danish servicemål deadline model + dashboard + notifications", "cluster": "Servicemål / deadlines", "size": "XL", "gap": "Partial", "risk": "High", "owner": "Bjørn Henrik", "roadmap": "B — Accelerate", "roadmap_ref": "Plan & Build 360 / Flow", "note": "Consolidates 434878/434881"},
    {"id": "435495", "ref": "B2-18", "title": "Integration landscape", "cluster": "Integration spine", "size": "XL", "gap": "Partial", "risk": "High", "owner": "Olga", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": ""},
    {"id": "435489", "ref": "5.2.15.x", "title": "FilArkiv archive transfer from P&B", "cluster": "FilArkiv archive", "size": "L", "gap": "Partial", "risk": "Medium", "owner": "Bjørn Henrik", "roadmap": "C — Strategic", "roadmap_ref": "Archive automation", "note": ""},
    {"id": "435491", "ref": "B2-14", "title": "Time registration on cases", "cluster": "Time registration", "size": "L", "gap": "TBD", "risk": "Medium", "owner": "Morten", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": ""},
    {"id": "435486", "ref": "B2-03", "title": "BRE write-back to BOM", "cluster": "BOM + BRE", "size": "L", "gap": "Partial", "risk": "High", "owner": "Bjørn Henrik", "roadmap": "A — Aligns", "roadmap_ref": "Business Rules Engine", "note": "MK minimum"},
    {"id": "435480", "ref": "5.2.1.1", "title": "Tagging, structuring and sorting", "cluster": "Case UX / search", "size": "L", "gap": "Partial", "risk": "High", "owner": "Jarle", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": "Was Not met"},
    {"id": "435501", "ref": "B2-20", "title": "Log delivery to SIEM (LogPoint)", "cluster": "Security / SIEM", "size": "L", "gap": "Not met", "risk": "High", "owner": "—", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": "MK blocker"},
    {"id": "435493", "ref": "5.3.7.2.6", "title": "Log integrity manual deletion", "cluster": "Security / SIEM", "size": "M", "gap": "Not met", "risk": "High", "owner": "Jarle", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": "MK blocker"},
    {"id": "435499", "ref": "5.3.8.2.7.1.4", "title": "MeMo Digital Post actions", "cluster": "Integration spine", "size": "S", "gap": "Not met", "risk": "High", "owner": "—", "roadmap": "A — Aligns", "roadmap_ref": "Digital Post", "note": "Was In flight"},
    {"id": "435484", "ref": "5.2.8.4+", "title": "Case overview and process control", "cluster": "Process control", "size": "L", "gap": "Partial", "risk": "Medium", "owner": "Morten", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": ""},
    {"id": "435483", "ref": "5.2.4.3", "title": "Search, sorting, filtering, export", "cluster": "Case UX / search", "size": "M", "gap": "Partial", "risk": "Medium", "owner": "Jarle", "roadmap": "B — Accelerate", "roadmap_ref": "Refactor search experience", "note": ""},
    {"id": "435496", "ref": "5.3.8.2.2.1", "title": "Master data from registers", "cluster": "Integration spine", "size": "L", "gap": "Partial", "risk": "High", "owner": "—", "roadmap": "A — Aligns", "roadmap_ref": "NG Integration API", "note": ""},
    {"id": "435487", "ref": "5.2.9.x", "title": "BOM data as search criteria", "cluster": "BOM + BRE", "size": "M", "gap": "Partial", "risk": "Medium", "owner": "Bjørn Henrik", "roadmap": "B — Accelerate", "roadmap_ref": "Plan & Build / BOM", "note": ""},
    {"id": "435488", "ref": "5.2.13.1", "title": "Case templates", "cluster": "Process control", "size": "M", "gap": "In flight", "risk": "Medium", "owner": "Bjørn Henrik", "roadmap": "B — Accelerate", "roadmap_ref": "Hosted Processes / Flow", "note": ""},
    {"id": "435503", "ref": "5.4.2.1", "title": "AI Assist integration (option)", "cluster": "Integration spine", "size": "M", "gap": "Partial", "risk": "Medium", "owner": "—", "roadmap": "B — Accelerate", "roadmap_ref": "Agentic case management", "note": ""},
    {"id": "435502", "ref": "5.4.1.1", "title": "Debtor system (option)", "cluster": "Integration spine", "size": "M", "gap": "Partial", "risk": "Low", "owner": "—", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": ""},
    {"id": "435482", "ref": "5.2.1.3", "title": "Flexible journalisation", "cluster": "Case UX / search", "size": "M", "gap": "Partial", "risk": "Medium", "owner": "—", "roadmap": "B — Accelerate", "roadmap_ref": "Plan & Build / BOM", "note": ""},
    {"id": "435481", "ref": "5.2.1.2", "title": "Conflict resolution", "cluster": "Case UX / search", "size": "M", "gap": "Partial", "risk": "Medium", "owner": "Linn", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": ""},
    {"id": "435485", "ref": "5.2.8.5", "title": "Handling received information", "cluster": "Case UX / search", "size": "M", "gap": "Partial", "risk": "Medium", "owner": "Morten", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": ""},
    {"id": "435497", "ref": "5.3.8.2.3", "title": "Deep link integrations", "cluster": "Integration spine", "size": "M", "gap": "TBD", "risk": "Medium", "owner": "Jarle", "roadmap": "A — Aligns", "roadmap_ref": "NG Integration API", "note": ""},
    {"id": "435498", "ref": "5.3.8.2.7.1.2", "title": "Remote print SF1601", "cluster": "Integration spine", "size": "M", "gap": "Partial", "risk": "Medium", "owner": "—", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": ""},
    {"id": "434878", "ref": "5.2.11.2", "title": "Servicemålstid start/stop", "cluster": "Servicemål / deadlines", "size": "M", "gap": "Partial", "risk": "Medium", "owner": "Bjørn Henrik", "roadmap": "D — Low priority", "roadmap_ref": "—", "note": "Superseded by 435490"},
    {"id": "434881", "ref": "5.2.11.3", "title": "Sagsbehandlingstid ikke-BOM", "cluster": "Servicemål / deadlines", "size": "M", "gap": "Partial", "risk": "Medium", "owner": "Bjørn Henrik", "roadmap": "D — Low priority", "roadmap_ref": "—", "note": ""},
    {"id": "434352", "ref": "Data delimitation", "title": "Data delimitation of cases", "cluster": "Security / SIEM", "size": "M", "gap": "Partial", "risk": "Medium", "owner": "—", "roadmap": "A — Aligns", "roadmap_ref": "Access matrix", "note": ""},
    {"id": "435492", "ref": "5.3.4.2", "title": "Error texts and messages", "cluster": "Point fix", "size": "S", "gap": "Partial", "risk": "Low", "owner": "Jarle", "roadmap": "D — Low priority", "roadmap_ref": "—", "note": ""},
]


def find_edge() -> Path:
    for candidate in EDGE_CANDIDATES:
        if candidate.is_file():
            return candidate
    raise FileNotFoundError("Microsoft Edge not found; install Edge or adjust EDGE_CANDIDATES")


def is_table_separator(line: str) -> bool:
    stripped = line.strip()
    if not stripped.startswith("|"):
        return False
    inner = stripped.strip("|")
    return bool(inner) and all(ch in "-:| " for ch in inner)


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


def inline_md(text: str) -> str:
    escaped = html.escape(text)
    parts = escaped.split("**")
    for idx in range(1, len(parts), 2):
        parts[idx] = f"<strong>{parts[idx]}</strong>"
    return "".join(parts)


def gap_class(gap: str) -> str:
    if gap == "Not met":
        return "gap-not-met"
    if gap in {"Partial", "In flight"}:
        return "gap-partial"
    if gap == "Draft needed":
        return "gap-draft"
    return ""


def wrap_html(title: str, body: str, landscape: bool = False) -> str:
    page = "@page { size: A4 landscape; margin: 12mm; }" if landscape else "@page { size: A4; margin: 18mm; }"
    css = PRINT_CSS.replace("@page { size: A4 landscape; margin: 12mm; }", page)
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"/><title>{html.escape(title)}</title>
<style>{css}</style></head><body>{body}</body></html>"""


def build_management_html() -> str:
    md = BRIEF_MD.read_text(encoding="utf-8")
    body = md_to_simple_html(md)
    return wrap_html("KK management go/no-go brief", body, landscape=False)


def build_heatmap_html() -> str:
    gap_counts = {"Not met": 0, "Partial": 0, "Draft needed": 0, "In flight": 0, "TBD": 0}
    roadmap_counts = {"A — Aligns": 0, "B — Accelerate": 0, "C — Strategic": 0, "D — Low priority": 0}
    for row in PFR_ROWS:
        gap_counts[row["gap"]] = gap_counts.get(row["gap"], 0) + 1
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
            f"<td class='{gap_class(row['gap'])}'>{html.escape(row['gap'])}</td>"
            f"<td>{row['risk']}</td><td>{html.escape(row['owner'])}</td>"
            f"<td>{html.escape(row['note'])}</td>"
            f"</tr>"
        )

    body = f"""
<h1>KK tender — commitment heatmap</h1>
<p class="meta">Københavns Kommune · Foundation epic #434005 (200 days) + 25 tender PFR delta · ADO verified 18 Aug 2026 · Go-live ukendt</p>
<div class="callout info"><strong>Timeline:</strong> No fixed Overtagelsesdag in tender. Supplier proposes implementation plan (4.1.1, 15% weight).</div>
<div class="callout info"><strong>Gap profile (tender tool, 18 Aug):</strong>
Not met {gap_counts['Not met']} · Partial {gap_counts['Partial']} · In flight {gap_counts['In flight']} · TBD {gap_counts['TBD']}</div>
<div class="stats">
  <div class="stat"><div class="val">200 d</div><div class="lbl">Foundation epic #434005</div></div>
  <div class="stat"><div class="val">25</div><div class="lbl">Tender PFR delta</div></div>
  <div class="stat"><div class="val">{gap_counts['Not met']}</div><div class="lbl">Not met blockers</div></div>
  <div class="stat"><div class="val">{gap_counts['Partial']}</div><div class="lbl">Partial</div></div>
  <div class="stat"><div class="val">30–55 mo</div><div class="lbl">PFR delta only (excl. foundation)</div></div>
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
    return wrap_html("KK commitment heatmap", body, landscape=True)


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
        raise RuntimeError(
            f"Edge PDF export failed for {html_path.name}\n"
            f"stdout: {result.stdout}\nstderr: {result.stderr}"
        )


def main() -> int:
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    edge = find_edge()

    exports = [
        ("kk-management-gate", build_management_html(), False),
        ("kk-commitment-heatmap", build_heatmap_html(), True),
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
