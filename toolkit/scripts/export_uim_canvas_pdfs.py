"""Export UIM canvas content to print-ready PDF via Edge headless.

Generates HTML snapshots aligned with uim-management-gate, uim-commitment-heatmap,
and uim-delivery-roadmap canvases, then prints to PDF. Usage (from repo root):

    uv run python toolkit/scripts/export_uim_canvas_pdfs.py
    uv run python toolkit/scripts/export_uim_canvas_pdfs.py --only uim-delivery-roadmap
"""
from __future__ import annotations

import argparse
import html
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
EXPORT_DIR = REPO_ROOT / "docs" / "tender-reference" / "export"
BRIEF_MD = REPO_ROOT / "docs" / "tender-reference" / "UIM-management-gate-brief.md"

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
    {"id": "433895", "ref": "EK-6 / EK-1", "title": "Customer entities platform + Udlændingeoverblik", "cluster": "Platform spine", "size": "XL", "gap": "Draft needed", "risk": "High", "owner": "Claus", "roadmap": "B — Accelerate", "roadmap_ref": "Full Flex UI cont.", "note": "Hub program; scope exceeds FFUI waves"},
    {"id": "433881", "ref": "MK-6", "title": "Retention/deletion on all entities", "cluster": "Platform spine", "size": "XL", "gap": "Partial", "risk": "High", "owner": "Morten", "roadmap": "B — Accelerate", "roadmap_ref": "Full Flex UI cont. (433895 satellite)", "note": ""},
    {"id": "433883", "ref": "MK-80", "title": "Mass update on contacts & custom entities", "cluster": "Platform spine", "size": "XL", "gap": "Not met", "risk": "High", "owner": "Torben", "roadmap": "B — Accelerate", "roadmap_ref": "Full Flex UI cont.", "note": ""},
    {"id": "433887", "ref": "K-11 / K-12", "title": "Configuration import/export module", "cluster": "Platform admin", "size": "XL", "gap": "Not met", "risk": "High", "owner": "Anton", "roadmap": "B — Accelerate", "roadmap_ref": "Config migration tool", "note": "Export breadth may exceed migration tool"},
    {"id": "435597", "ref": "EK-5", "title": "Configurable rules and validations", "cluster": "Platform spine", "size": "L", "gap": "TBD", "risk": "High", "owner": "Torben / Claus", "roadmap": "A — Aligns", "roadmap_ref": "Business Rules Engine", "note": "Evaluation criterion; partial fit"},
    {"id": "435603", "ref": "EK-6", "title": "Configurable icons", "cluster": "Platform spine", "size": "M", "gap": "TBD", "risk": "Medium", "owner": "Torben", "roadmap": "D — Low priority", "roadmap_ref": "—", "note": "Low market potential"},
    {"id": "433882", "ref": "MK-66+", "title": "Full Flex advanced search", "cluster": "Search / FFUI", "size": "XL", "gap": "Partial", "risk": "High", "owner": "Jarle", "roadmap": "B — Accelerate", "roadmap_ref": "360° Søkeassistent + Refactor search experience", "note": ""},
    {"id": "433884", "ref": "MK-84+", "title": "Full Flex detail webparts / columns", "cluster": "Search / FFUI", "size": "XL", "gap": "Not met", "risk": "High", "owner": "Torben", "roadmap": "B — Accelerate", "roadmap_ref": "Full Flex UI cont.", "note": ""},
    {"id": "435253", "ref": "EK-3", "title": "UI personalization (search, lists, detail views)", "cluster": "Search / FFUI", "size": "XL", "gap": "Draft needed", "risk": "High", "owner": "Claus / Jarle", "roadmap": "B — Accelerate", "roadmap_ref": "Full Flex UI cont. + search refactor", "note": "Overlaps 433882/433884"},
    {"id": "435606", "ref": "MK-66+ / EK-3", "title": "All listviews configurable with all first-level metadata", "cluster": "Search / FFUI", "size": "XL", "gap": "TBD", "risk": "High", "owner": "Jarle / Torben", "roadmap": "B — Accelerate", "roadmap_ref": "Full Flex UI cont. + search refactor", "note": "Universal listviews not on roadmap"},
    {"id": "435257", "ref": "MK-77", "title": "No limit on list/search result counts", "cluster": "Search / UI", "size": "M", "gap": "Not met", "risk": "High", "owner": "Willy / Jarle", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": "Bid blocker; architecture change"},
    {"id": "433877", "ref": "MK-30", "title": "Hierarchical case collections in search lists", "cluster": "Search / UI", "size": "M", "gap": "Not met", "risk": "Medium", "owner": "Eva", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": ""},
    {"id": "435258", "ref": "EK-12", "title": "Create/update Activities via API", "cluster": "API / integration", "size": "M", "gap": "In flight", "risk": "Medium", "owner": "Nikita", "roadmap": "A — Aligns", "roadmap_ref": "NG Integration API / 360° API Gateway", "note": "Linked to WI 377061"},
    {"id": "433889", "ref": "K-16", "title": "LibreOffice support", "cluster": "Integrations", "size": "L", "gap": "Not met", "risk": "Medium", "owner": "Anton", "roadmap": "A — Aligns", "roadmap_ref": "Office alternatives", "note": ""},
    {"id": "433891", "ref": "K-17", "title": "Evolution mail client integration", "cluster": "Integrations", "size": "L", "gap": "Not met", "risk": "Medium", "owner": "Anton", "roadmap": "B — Accelerate", "roadmap_ref": "Office alternatives", "note": ""},
    {"id": "435203", "ref": "K-17", "title": "Alternative email clients (duplicate scope)", "cluster": "Integrations", "size": "L", "gap": "TBD", "risk": "Medium", "owner": "Hans", "roadmap": "D — Low priority", "roadmap_ref": "—", "note": "Dedupe with 433891"},
    {"id": "433894", "ref": "MK-20 (UUID)", "title": "UUID across all logging", "cluster": "Logging / audit", "size": "L", "gap": "TBD", "risk": "Medium", "owner": "Willy", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": "Overlap with 435333"},
    {"id": "435333", "ref": "MK-20", "title": "Log separation & transaction traceability", "cluster": "Logging / audit", "size": "L", "gap": "TBD", "risk": "Medium", "owner": "Hans", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": "Broader than 433894"},
    {"id": "433885", "ref": "MK-99", "title": "Workflow history report on completion", "cluster": "Workflow", "size": "M", "gap": "Not met", "risk": "Medium", "owner": "Torben", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": ""},
    {"id": "433886", "ref": "MK-120", "title": "Mask definition through web-admin", "cluster": "Admin / security", "size": "M", "gap": "TBD", "risk": "Medium", "owner": "Anton", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": ""},
    {"id": "433888", "ref": "MK-133", "title": "Report: entities no user can access", "cluster": "Admin / security", "size": "M", "gap": "Not met", "risk": "Medium", "owner": "Eva", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": ""},
    {"id": "433892", "ref": "MK-169", "title": "Failed document dispatch notification", "cluster": "Dispatch", "size": "M", "gap": "Not met", "risk": "Medium", "owner": "Hans", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": ""},
    {"id": "433893", "ref": "K-18", "title": "Split large document dispatches", "cluster": "Dispatch", "size": "M", "gap": "Not met", "risk": "Medium", "owner": "Hans", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": ""},
    {"id": "435336", "ref": "MK-165", "title": "Remote Print configuration", "cluster": "Dispatch", "size": "M", "gap": "TBD", "risk": "Medium", "owner": "Hans", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": ""},
    {"id": "435338", "ref": "MK-167", "title": "Dispatch channel (physical mail)", "cluster": "Dispatch", "size": "M", "gap": "TBD", "risk": "Medium", "owner": "Hans", "roadmap": "C — Strategic", "roadmap_ref": "—", "note": ""},
    {"id": "433880", "ref": "MK-56", "title": "Duplicate contact prevention", "cluster": "Point fix", "size": "S", "gap": "Partial", "risk": "Low", "owner": "Panu", "roadmap": "D — Low priority", "roadmap_ref": "—", "note": "~40h ballpark"},
    {"id": "433890", "ref": "MK-145", "title": "Archiving datetime in Outlook", "cluster": "Integrations", "size": "S", "gap": "Partial", "risk": "Low", "owner": "Anton", "roadmap": "A — Aligns", "roadmap_ref": "New Outlook Support cont.", "note": ""},
]


ROADMAP_INITIATIVES: list[dict[str, str | bool]] = [
    {"team": "Core UI + Core BL", "title": "Unified search surface (Search Assistant + query builder)", "problem": "Users expect combined multi-field, cross-entity search in one place — not three parallel mental models (Global / Advanced / Assistant).", "tender_refs": "MK-66, MK-73, MK-74, MK-75, K-4", "pfr_ids": "433882", "gap": "Partial", "start": "Now", "end": "Q4 2026", "start_now": True, "dependency": "MVP for bid narrative by Nov 2026; hardening in Q1 2027 only"},
    {"team": "Core UI + Core BL", "title": "Unbounded search & list results (MK-77)", "problem": "Tender requires displaying large result sets without hard caps. Current architecture limits list/search counts — bid blocker.", "tender_refs": "MK-77", "pfr_ids": "435257", "gap": "Not met", "start": "Now", "end": "Q4 2026", "start_now": True, "dependency": "Architecture decision by mid-Sep 2026; blocks all list work"},
    {"team": "Core UI + Core BL", "title": "Listviews & personalization — alt UI layer (not FIB)", "problem": "435606 / EK-3 / MK-84+ via FIB+FFUI is 25–40 months net effort — too slow. Explore thin React shell, Search Assistant host, or generated views on existing APIs.", "tender_refs": "MK-66+, EK-3, MK-84+", "pfr_ids": "435606, 435253, 433884", "gap": "TBD", "start": "Now", "end": "Q2 2027", "start_now": True, "dependency": "UI layer spike (Sep 2026) gates scope: alt shell vs FIB/FFUI vs hybrid"},
    {"team": "Core UI + Core BL", "title": "Hierarchical case collections in search lists", "problem": "Search result lists must support hierarchical case collection structures (parent/child cases).", "tender_refs": "MK-30", "pfr_ids": "433877", "gap": "Not met", "start": "Q2 2027", "end": "Q2 2027", "start_now": False, "dependency": "Q&A narrow to evaluation-only or defer post go-live"},
    {"team": "Core Integration", "title": "Activities create/update via API (EK-12)", "problem": "External systems must create and update Activities through a documented REST API — not UI-only flows.", "tender_refs": "EK-12", "pfr_ids": "435258", "gap": "In flight", "start": "Now", "end": "Q4 2026", "start_now": True, "dependency": "Linked to WI 377061 — lowest gate risk if closed before bid lock"},
    {"team": "Core Integration", "title": "Mass update API & bulk operations (MK-80)", "problem": "Bulk update of contacts and customer-created entities is not supported today. Requires API orchestration, audit trail, and async job patterns.", "tender_refs": "MK-80", "pfr_ids": "433883", "gap": "Not met", "start": "Now", "end": "Q1 2027", "start_now": True, "dependency": "Entity model breadth from 433895; UI may use alt layer not FIB Massupdate"},
    {"team": "Process Platform", "title": "Business Rules Engine — platform MVP", "problem": "Platform needs a rules execution layer for workflow-adjacent automation. Existing roadmap targets MVP in 6.11 stretch (eDoc caseclose).", "tender_refs": "— (platform)", "pfr_ids": "—", "gap": "Aligns", "start": "Now", "end": "Q4 2026", "start_now": True, "dependency": ""},
    {"team": "Process Platform", "title": "Configurable rules & validations on entities (EK-5)", "problem": "Customer-configurable validation rules on standard and custom fields — evaluation criterion, not just minimum requirement.", "tender_refs": "EK-5", "pfr_ids": "435597", "gap": "TBD", "start": "Q1 2027", "end": "Q2 2027", "start_now": False, "dependency": "Extends BRE MVP; ties to custom fields / 433895 platform spine"},
]

ROADMAP_EXPERIMENTS: list[dict[str, str]] = [
    {"tool": "BMAD (spec-driven)", "track": "Search", "purpose": "bmad-investigate → brief → spec → architecture on search-experience information-package", "timebox": "Sep 2026 (2 weeks)", "success": "Architecture + UI layer recommendation for Sep gate"},
    {"tool": "BMAD (spec-driven)", "track": "Integration + PP", "purpose": "BRE-style information package for EK-12 closure and mass-update API contract", "timebox": "Sep–Oct 2026", "success": "OpenAPI + acceptance criteria signed"},
    {"tool": "Paperclip", "track": "Search + Integration", "purpose": "Orchestrate Cursor/Claude agents on ADO backlog — spikes, tests, API boilerplate", "timebox": "Sep spike · Oct decision", "success": "≥1 vertical slice with measured human-review ratio"},
    {"tool": "AI-generated code", "track": "All tracks", "purpose": "BMAD spec + ADO story → agent generates handlers/views; human owns architecture and merge", "timebox": "Ongoing from Sep 2026", "success": "Green/yellow/red zones agreed per team"},
    {"tool": "Alt UI layer spike", "track": "Search", "purpose": "FIB/FFUI vs thin React host vs generated list components on search API", "timebox": "Sep 2026 (1 week)", "success": "Go/no-go on FIB dependency for search MVP"},
]

ROADMAP_DECISIONS: list[dict[str, str]] = [
    {"id": "D1", "cat": "Strategy", "question": "Can we deliver full UIM portfolio on current FFUI/FIB path?", "options": "Compress + alt UI + AI · Partial bid · Full commit (9–14 FTE peak)", "deadline": "Sep 2026", "owner": "Program / DG"},
    {"id": "D2", "cat": "Architecture", "question": "Search UI layer: extend FIB/FFUI or separate React shell?", "options": "Search Assistant host · FIB/FFUI full · Hybrid", "deadline": "Mid-Sep 2026", "owner": "Core UI + Search"},
    {"id": "D3", "cat": "Architecture", "question": "MK-77: unbounded results without breaking performance?", "options": "Cursor/streaming · virtual scroll + paging · async export · Q&A cap", "deadline": "Mid-Sep 2026", "owner": "Core BL + Search"},
    {"id": "D4", "cat": "Delivery", "question": "Search MVP for Nov 2026 award vs Sep 2027 build complete?", "options": "MK-66 partial + MK-77 plan · include MK-74/75 · defer 435606", "deadline": "Sep 2026", "owner": "Morten / tender"},
    {"id": "D5", "cat": "Delivery", "question": "Where is AI-generated code allowed?", "options": "Green: API/UI from spec · Yellow: BL query · Red: auth, pagination, audit", "deadline": "Sep 2026", "owner": "Tech leads"},
    {"id": "D6", "cat": "Delivery", "question": "Paperclip pilot: adopt or stay Cursor-only?", "options": "Search spike · Integration API · No", "deadline": "Oct 2026", "owner": "Program + leads"},
    {"id": "D7", "cat": "Strategy", "question": "433895 customer entities — in, partial, or out?", "options": "Full hub · Phased · Q&A narrow · Out", "deadline": "Sep 2026", "owner": "Claus / program"},
    {"id": "D8", "cat": "Tender", "question": "435606 universal listviews — minimum or evaluation?", "options": "Q&A clarify · Partial (search lists) · Alt UI columns · Defer", "deadline": "Oct 2026", "owner": "Tender owner"},
    {"id": "D9", "cat": "Strategy", "question": "Search Assistant: replace or coexist with Advanced Search?", "options": "Replace · Unified entry · Coexist", "deadline": "Sep 2026", "owner": "Search PM"},
    {"id": "D10", "cat": "Tender", "question": "MK-30 hierarchical collections — in scope for Oct 2027?", "options": "Commit · Evaluation only · Q&A out", "deadline": "Oct 2026", "owner": "Tender owner"},
]

ROADMAP_DEFERRED: list[dict[str, str]] = [
    {"cluster": "Platform spine", "refs": "EK-6, MK-6, K-11/K-12", "pfrs": "433895, 433881, 433887, 435603", "note": "Hub decision gate — 433895 blocks mass update & validations breadth"},
    {"cluster": "Office / mail integrations", "refs": "K-16, K-17, MK-145", "pfrs": "433889, 433891, 433890", "note": "LibreOffice, Evolution, Outlook datetime"},
    {"cluster": "Dispatch / Strålfors", "refs": "MK-169, K-18, MK-165, MK-167", "pfrs": "433892, 433893, 435336, 435338", "note": "Physical mail channel assumptions"},
    {"cluster": "Logging / audit", "refs": "MK-20", "pfrs": "433894, 435333", "note": "Merge duplicate Features before commitment"},
    {"cluster": "Admin / workflow / security", "refs": "MK-99, MK-120, MK-133", "pfrs": "433885, 433886, 433888", "note": "Medium priority; Q&A on minimum vs evaluation"},
]

ROADMAP_PHASES: list[list[str]] = [
    ["Now (Aug–Sep 2026)", "MK-77 architecture decision; BMAD investigate+brief; alt UI layer spike; Search Assistant MVP scope lock", "Close EK-12 / WI 377061; mass update API design; Paperclip pilot", "BRE MVP scoping; BMAD spec for rule model", "D1–D5 decisions · acceleration experiments start"],
    ["Q4 2026", "Search MVP: MK-66 + query builder for bid; MK-77 implementation; alt-UI list prototype", "Mass update API alpha; async bulk job pattern", "BRE MVP delivery (6.11 stretch)", "Award gate ~Nov 2026 · search demo-ready"],
    ["Q1 2027", "Search hardening; MK-74/75; listviews on chosen UI layer (not full FIB if spike succeeds)", "Mass update API beta; integration testing", "EK-5 validations on custom entities", "Post-award acceleration"],
    ["Q2 2027", "Personalization (EK-3) to committed minimum; MK-30 only if in scope", "Mass update GA; API documentation & compliance evidence", "EK-5 GA", "Tender compliance hardening"],
    ["Sep 2027", "Search/list UAT sign-off", "API & bulk UAT sign-off", "BRE / validations UAT sign-off", "Build complete · Go-live Oct 2027"],
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
    """Minimal markdown converter for the management brief (headings, tables, lists)."""
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
            if stripped[0].isdigit() and ". " in stripped[:4]:
                out.append(f"<p>{inline_md(stripped)}</p>")
            else:
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


def risk_row_class(risk: str) -> str:
    if risk == "High":
        return "risk-high"
    if risk == "Medium":
        return "risk-med"
    if risk == "Low":
        return "risk-low"
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
    return wrap_html("UIM management go/no-go brief", body, landscape=False)


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
<h1>UIM 2026 tender — commitment heatmap</h1>
<p class="meta">Parent ADO #433876 · 27 related Features · Roadmap source: Public 360° PPT (Q1 2026–Q2 2027)</p>
<div class="stats">
  <div class="stat"><div class="val">27</div><div class="lbl">Features in portfolio</div></div>
  <div class="stat"><div class="val">{roadmap_counts['B — Accelerate']}</div><div class="lbl">B — Accelerate</div></div>
  <div class="stat"><div class="val">{roadmap_counts['C — Strategic']}</div><div class="lbl">C — Strategic</div></div>
  <div class="stat"><div class="val">{roadmap_counts['A — Aligns']}</div><div class="lbl">A — Aligns</div></div>
  <div class="stat"><div class="val">45–75 mo</div><div class="lbl">Net effort (conservative)</div></div>
</div>
<div class="callout info"><strong>Roadmap alignment:</strong> UIM is not mostly deliver planned roadmap on time.
A {roadmap_counts['A — Aligns']} · B {roadmap_counts['B — Accelerate']} · C {roadmap_counts['C — Strategic']} · D {roadmap_counts['D — Low priority']}.</div>
<p><strong>Gap profile:</strong>
Not met {gap_counts['Not met']} · Partial {gap_counts['Partial']} · Draft {gap_counts['Draft needed']} ·
In flight {gap_counts['In flight']} · TBD {gap_counts['TBD']}</p>
<h2>PFR portfolio detail</h2>
<table>
<thead><tr>
<th>ID</th><th>Ref</th><th>Title</th><th>Roadmap</th><th>Roadmap ref</th><th>Cluster</th><th>Size</th>
<th>Gap</th><th>Risk</th><th>Owner</th><th>Notes</th>
</tr></thead>
<tbody>{''.join(rows_html)}</tbody>
</table>
<p class="small">Roadmap mapped against UIM build complete 1 Sep 2027. Cluster-owner validation pending.</p>
"""
    return wrap_html("UIM commitment heatmap", body, landscape=True)


def team_short(team: str) -> str:
    return (
        team.replace("Core UI + Core BL", "Search")
        .replace("Core Integration", "Integration")
        .replace("Process Platform", "PP")
    )


def build_initiative_html(item: dict[str, str | bool], *, compact: bool = False) -> str:
    gap = str(item["gap"])
    start_now = bool(item["start_now"])
    dep = str(item.get("dependency") or "")
    pfr_ids = str(item["pfr_ids"])
    problem_html = "" if compact else f"<p class='small'>{html.escape(str(item['problem']))}</p>"
    start_now_badge = "<span class='badge warn'>Start now</span> " if start_now else ""
    pfr_html = "" if pfr_ids == "—" else f" · PFR {html.escape(pfr_ids)}"
    dep_html = f"<p class='small'><em>{html.escape(dep)}</em></p>" if dep else ""
    return (
        f"<div class='initiative'>"
        f"<p><strong>{html.escape(str(item['title']))}</strong> "
        f"<span class='{gap_class(gap) or 'gap-tbd'}'>{html.escape(gap)}</span> {start_now_badge}</p>"
        f"{problem_html}"
        f"<p class='small'>{html.escape(str(item['tender_refs']))}{pfr_html} · {html.escape(str(item['start']))} → {html.escape(str(item['end']))}</p>"
        f"{dep_html}"
        f"</div>"
    )


def build_delivery_roadmap_html() -> str:
    start_now_count = sum(1 for i in ROADMAP_INITIATIVES if i["start_now"])
    not_met_count = sum(1 for i in ROADMAP_INITIATIVES if i["gap"] == "Not met")
    teams = ["Core UI + Core BL", "Core Integration", "Process Platform"]

    swimlanes = []
    for team in teams:
        items = [i for i in ROADMAP_INITIATIVES if i["team"] == team]
        now_items = [i for i in items if i["start_now"]]
        follow_items = [i for i in items if not i["start_now"]]
        now_html = "".join(build_initiative_html(i) for i in now_items)
        follow_html = "".join(build_initiative_html(i, compact=True) for i in follow_items)
        swimlanes.append(
            f"<h3>{html.escape(team)} ({len(items)} initiatives)</h3>"
            f"<h4>Start now ({len(now_items)})</h4>{now_html}"
            f"<h4>Follow-on</h4>{follow_html}"
        )

    problem_rows = []
    for item in ROADMAP_INITIATIVES:
        gap = str(item["gap"])
        row_cls = risk_row_class("High" if gap == "Not met" else "Medium" if gap in {"Partial", "TBD"} else "Low")
        problem_rows.append(
            f"<tr class='{row_cls}'>"
            f"<td>{html.escape(team_short(str(item['team'])))}</td>"
            f"<td>{html.escape(str(item['tender_refs']))}</td>"
            f"<td>{html.escape(str(item['problem']))}</td>"
            f"<td class='{gap_class(gap) or 'gap-tbd'}'>{html.escape(gap)}</td>"
            f"<td>{'Yes' if item['start_now'] else '—'}</td>"
            f"</tr>"
        )

    phase_rows = []
    for row in ROADMAP_PHASES:
        phase_rows.append("<tr>" + "".join(f"<td>{html.escape(c)}</td>" for c in row) + "</tr>")

    deferred_rows = []
    for row in ROADMAP_DEFERRED:
        deferred_rows.append(
            "<tr>"
            f"<td>{html.escape(row['cluster'])}</td>"
            f"<td>{html.escape(row['refs'])}</td>"
            f"<td>{html.escape(row['pfrs'])}</td>"
            f"<td>{html.escape(row['note'])}</td>"
            "</tr>"
        )

    experiment_rows = []
    for row in ROADMAP_EXPERIMENTS:
        experiment_rows.append(
            "<tr>"
            f"<td>{html.escape(row['tool'])}</td>"
            f"<td>{html.escape(row['track'])}</td>"
            f"<td>{html.escape(row['purpose'])}</td>"
            f"<td>{html.escape(row['timebox'])}</td>"
            f"<td>{html.escape(row['success'])}</td>"
            "</tr>"
        )

    decision_rows = []
    for row in ROADMAP_DECISIONS:
        decision_rows.append(
            "<tr>"
            f"<td>{html.escape(row['id'])}</td>"
            f"<td>{html.escape(row['cat'])}</td>"
            f"<td>{html.escape(row['question'])}</td>"
            f"<td>{html.escape(row['options'])}</td>"
            f"<td>{html.escape(row['deadline'])}</td>"
            f"<td>{html.escape(row['owner'])}</td>"
            "</tr>"
        )

    body = f"""
<h1>UIM ESDH — delivery roadmap (draft)</h1>
<p class="meta">High-level plan to start work before award · Three parallel tracks · ADO parent #433876<br/>
UIM ESDH tender tool · 27 commitment Features · Aug 2026 · Build complete 1 Sep 2027 · Search MVP Q4 2026 (compressed)</p>
<div class="stats">
  <div class="stat"><div class="val">3</div><div class="lbl">Parallel tracks</div></div>
  <div class="stat"><div class="val">{start_now_count}</div><div class="lbl">Start now</div></div>
  <div class="stat"><div class="val">{not_met_count}</div><div class="lbl">Gap: Not met</div></div>
  <div class="stat"><div class="val">~10 mo</div><div class="lbl">Build window</div></div>
</div>
<div class="callout warn"><strong>Timeline compression — search is on the critical path:</strong> Original plan (search through Q2 2027 on FIB/FFUI) cannot deliver the full UIM portfolio by Sep 2027. Search MVP must land Q4 2026; MK-77 decided by mid-Sep. Listviews require alt UI layer decision — FIB extension is the slow path.</div>
<div class="callout warn"><strong>Critical path outside these three tracks:</strong> Customer entities platform (433895 / EK-6) is the hub for mass update breadth, configurable validations, and FFUI scope. Go/no-go on 433895 affects Integration and Process Platform follow-ons.</div>
<h2>Team tracks</h2>
{''.join(swimlanes)}
<div class="page-break"></div>
<h2>Acceleration experiments (BMAD · Paperclip · AI codegen)</h2>
<table>
<thead><tr><th>Tool</th><th>Track</th><th>Purpose</th><th>Timebox</th><th>Success criteria</th></tr></thead>
<tbody>{''.join(experiment_rows)}</tbody>
</table>
<h2>Decisions to make · questions to answer</h2>
<table>
<thead><tr><th>ID</th><th>Category</th><th>Question</th><th>Options</th><th>Deadline</th><th>Owner</th></tr></thead>
<tbody>{''.join(decision_rows)}</tbody>
</table>
<h2>Problems to solve · requirements map</h2>
<table>
<thead><tr><th>Track</th><th>Tender refs</th><th>Problem / requirement</th><th>Gap today</th><th>Start now</th></tr></thead>
<tbody>{''.join(problem_rows)}</tbody>
</table>
<h2>Phased timeline (compressed)</h2>
<table>
<thead><tr><th>Phase</th><th>Search (Core UI + BL)</th><th>Integration</th><th>Process Platform</th><th>Program milestone</th></tr></thead>
<tbody>{''.join(phase_rows)}</tbody>
</table>
<h2>Cross-track dependencies</h2>
<ul>
<li><strong>Search ↔ Integration:</strong> Mass update UI may use alt layer (not FIB Massupdate) consuming Integration bulk API. Avoid duplicate FIB/FFUI work with 433882.</li>
<li><strong>Integration ↔ Process Platform:</strong> EK-5 validations may invoke BRE; mass update may need rule checks before bulk apply. Define API contracts in Q4 2026.</li>
<li><strong>All tracks ↔ Platform spine:</strong> 433895 unlocks full MK-80 and EK-5 scope. Bid narrative must clarify phased delivery if 433895 is partial.</li>
<li><strong>Search internal:</strong> Core BL owns query engine + MK-77 pagination. Core UI owns Search Assistant + chosen UI layer. AI codegen highest value on UI + API boilerplate after BMAD spec lock.</li>
</ul>
<h2>Deferred clusters (not in initial three tracks)</h2>
<table>
<thead><tr><th>Cluster</th><th>Tender refs</th><th>PFR IDs</th><th>Note</th></tr></thead>
<tbody>{''.join(deferred_rows)}</tbody>
</table>
<h3>Next steps (Sep 2026)</h3>
<ol>
<li>Run BMAD investigate + brief on search-experience (2 weeks) → D2, D4, D9.</li>
<li>MK-77 architecture review by mid-Sep → D3.</li>
<li>Alt UI layer spike: FIB/FFUI vs Search Assistant React shell → D2 within 1 week.</li>
<li>Paperclip pilot: one Search slice + one Integration API handler → D6 by Oct.</li>
<li>Define AI codegen green/yellow/red zones → D5.</li>
<li>Integration: close WI 377061 before Nov 2026 award gate.</li>
<li>Program: resolve 433895 in/out → D7.</li>
<li>Tender: Q&A strategy for 435606 and MK-30 → D8, D10.</li>
</ol>
"""
    css_extra = """
.initiative { border-left: 3px solid #7BAFE9; padding-left: 8pt; margin: 6pt 0 10pt; }
.badge { font-size: 7.5pt; padding: 1pt 4pt; border-radius: 3px; background: #eee; }
.badge.warn { background: #fff3cd; color: #856404; }
.gap-tbd { color: #555; font-weight: 600; }
"""
    page = "@page { size: A4 landscape; margin: 12mm; }"
    css = PRINT_CSS.replace("@page { size: A4 landscape; margin: 12mm; }", page) + css_extra
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"/><title>UIM delivery roadmap</title>
<style>{css}</style></head><body>{body}</body></html>"""


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
    parser = argparse.ArgumentParser(description="Export UIM canvas snapshots to PDF")
    parser.add_argument(
        "--only",
        choices=["uim-management-gate", "uim-commitment-heatmap", "uim-delivery-roadmap"],
        help="Export a single canvas (default: all)",
    )
    args = parser.parse_args()

    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    edge = find_edge()

    all_exports = [
        ("uim-management-gate", build_management_html(), False),
        ("uim-commitment-heatmap", build_heatmap_html(), True),
        ("uim-delivery-roadmap", build_delivery_roadmap_html(), True),
    ]
    exports = [e for e in all_exports if args.only is None or e[0] == args.only]

    outputs: list[Path] = []
    for stem, html_content, _ in exports:
        html_path = EXPORT_DIR / f"{stem}.html"
        pdf_path = EXPORT_DIR / f"{stem}.pdf"
        html_path.write_text(html_content, encoding="utf-8")
        print_pdf(edge, html_path, pdf_path)
        outputs.append(pdf_path)
        print(pdf_path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
