"""Generate detailed NAV endringsønsker assessment report (Markdown + PDF)."""
from __future__ import annotations

import csv
import html
from collections import Counter, defaultdict
from datetime import date
from io import BytesIO
from pathlib import Path

import markdown
from xhtml2pdf import pisa

REPO = Path(__file__).resolve().parents[2]
CSV_PATH = REPO / "outputs/pfr/nav_endringonsker_assessment_2026-09-09.csv"
MD_PATH = REPO / "outputs/pfr/nav_endringonsker_assessment_2026-09-09.md"
PDF_PATH = REPO / "outputs/pfr/nav_endringonsker_assessment_2026-09-09.pdf"

TIER_ORDER = [
    "Fully implemented",
    "Partially implemented",
    "Already supported (configuration)",
    "Resolved (customer/integration)",
    "Resolved (customer)",
    "Planned / in development",
    "Not yet implemented",
    "Not implemented (closed out of scope)",
    "Not implemented (duplicate)",
    "Not implemented (by design)",
]

TIER_INTRO = {
    "Fully implemented": (
        "Delivered in product with release notes, closed core work, and/or CIM confirmation."
    ),
    "Partially implemented": (
        "Material product improvements shipped, but NAV-specific refinements or related scope remains open."
    ),
    "Already supported (configuration)": (
        "Available today through configuration — not a product code gap."
    ),
    "Resolved (customer/integration)": (
        "Marked resolved in CIM; verify scope with NAV/integration team before customer meeting."
    ),
    "Resolved (customer)": (
        "Closed in CIM; confirm whether resolution was product, process, or integration."
    ),
    "Planned / in development": (
        "Committed on roadmap or active in core development — frame as planned, not delivered."
    ),
    "Not yet implemented": (
        "No matching release or closed core implementation found in cross-reference."
    ),
    "Not implemented (closed out of scope)": (
        "Explicitly closed without generic product delivery."
    ),
    "Not implemented (duplicate)": (
        "Duplicate of another request — not a separate delivery."
    ),
    "Not implemented (by design)": (
        "Rejected as intentional product design."
    ),
}


def load_rows() -> list[dict[str, str]]:
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def esc(text: str) -> str:
    return html.escape(text or "")


def row_table(rows: list[dict[str, str]]) -> str:
    lines = [
        "| CS / Source | DevOps | Description | Contact | Status | When | Evidence | Talking point |",
        "|-------------|--------|-------------|---------|--------|------|----------|---------------|",
    ]
    for r in rows:
        cs = r["CS_Number"] if r["CS_Number"] != "N/A" else "Fra prosjekt"
        lines.append(
            "| {cs} | {devops} | {desc} | {contact} | {status} | {when} | {evidence} | {talk} |".format(
                cs=esc(cs),
                devops=esc(r["DevOps_IDs"]),
                desc=esc(r["Short_description"][:120]),
                contact=esc(r["Contact"]),
                status=esc(r["Implementation_Status"]),
                when=esc(r["When_Delivered_or_Target"]),
                evidence=esc(r["Evidence"][:160]),
                talk=esc(r["Customer_Talking_Point"][:160]),
            )
        )
    return "\n".join(lines)


def build_markdown(rows: list[dict[str, str]]) -> str:
    today = date.today().isoformat()
    counts = Counter(r["Implementation_Status"] for r in rows)
    arguable = sum(1 for r in rows if r["Arguable_for_NAV"] == "Yes")

    by_tier: dict[str, list[dict[str, str]]] = defaultdict(list)
    for r in rows:
        by_tier[r["Implementation_Status"]].append(r)

    parts = [
        "# NAV Endringsønsker — Implementation Assessment",
        "",
        f"**Report date:** {today}  ",
        "**Source:** Nav endringsønsker.xlsx (updated 2026-09-09)  ",
        "**Cross-reference:** Azure DevOps PFR/core backlog, CIM comments, release notes",
        "",
        "---",
        "",
        "## Executive summary",
        "",
        f"- **Total change requests assessed:** {len(rows)}",
        f"- **Arguable for customer narrative:** {arguable}",
        f"- **Fully implemented:** {counts.get('Fully implemented', 0)}",
        f"- **Partially implemented:** {counts.get('Partially implemented', 0)}",
        f"- **Resolved or already supported:** "
        f"{counts.get('Already supported (configuration)', 0) + counts.get('Resolved (customer/integration)', 0) + counts.get('Resolved (customer)', 0)}",
        f"- **Planned / in development:** {counts.get('Planned / in development', 0)}",
        f"- **Not yet implemented:** {counts.get('Not yet implemented', 0)}",
        "",
        "**Recommended customer framing:** Of 63 registered change requests, we can document "
        "**3 fully delivered in 2025**, **4 areas with substantial partial delivery** "
        "(stand-in, webparts, accessibility), **4 resolved or already supported**, and "
        "**~7 actively committed** on the roadmap (especially 6.11). Several rows are duplicates "
        "of the same theme — count unique themes (~14–15), not every row.",
        "",
        "**Verify before customer meeting:** CS0057279, CS0011998, CS0005990, and the scope of "
        "354222 \"Fixed\" (partial coverage only).",
        "",
        "---",
        "",
        "## Status overview",
        "",
        "| Implementation status | Count |",
        "|-----------------------|------:|",
    ]
    for tier in TIER_ORDER:
        if counts.get(tier):
            parts.append(f"| {tier} | {counts[tier]} |")

    parts.extend(["", "---", ""])

    for tier in TIER_ORDER:
        tier_rows = by_tier.get(tier)
        if not tier_rows:
            continue
        parts.extend(
            [
                f"## {tier} ({len(tier_rows)})",
                "",
                TIER_INTRO.get(tier, ""),
                "",
                row_table(tier_rows),
                "",
                "---",
                "",
            ]
        )

    parts.extend(
        [
            "## Deduplication notes (same theme, count once)",
            "",
            "| Theme | Related items |",
            "|-------|---------------|",
            "| Folkeregister / Infotorg parity | CS0038567, 347815, 373813 |",
            "| Register-based recipient lookup | 350615, 352215 |",
            "| Stand-in improvements | 350612, CS0021019 / 400608 |",
            "| Webpart type-in search | 354222, 335602 (distribution units overlap) |",
            "",
            "---",
            "",
            "## Methodology",
            "",
            "1. Parsed customer spreadsheet `Nav endringsønsker.xlsx` (63 data rows).",
            "2. Linked DevOps IDs cross-referenced against NAV PFRs and core backlog.",
            "3. Matched against release notes, closed core work items, and CIM comments.",
            "4. Classified each item as fully implemented, partially implemented, resolved, "
            "planned, or not yet implemented.",
            "",
            "**Evidence sources:** Azure DevOps (project 360), CIM ticket comments, "
            "360° Online release notes (Ratatoskr/help center), prior PFR cross-reference analysis.",
            "",
            "---",
            "",
            "*Generated by toolkit/pfr/generate_nav_assessment_report.py*",
        ]
    )
    return "\n".join(parts)


def markdown_to_pdf(md_text: str, pdf_path: Path) -> None:
    body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "nl2br", "sane_lists"],
    )
    html_doc = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"/>
<style>
@page {{ size: A4 landscape; margin: 12mm; }}
body {{ font-family: DejaVu Sans, Helvetica, Arial, sans-serif; font-size: 7.5pt; line-height: 1.3; }}
h1 {{ font-size: 15pt; page-break-after: avoid; }}
h2 {{ font-size: 11pt; page-break-after: avoid; margin-top: 10pt; color: #1a1a1a; }}
p, li {{ margin: 3pt 0; }}
table {{ border-collapse: collapse; width: 100%; margin: 6pt 0; font-size: 6.5pt; }}
th, td {{ border: 1px solid #999; padding: 3px 4px; vertical-align: top; word-wrap: break-word; }}
th {{ background: #e8e8e8; font-weight: bold; }}
tr:nth-child(even) td {{ background: #fafafa; }}
hr {{ border: none; border-top: 1px solid #ccc; margin: 8pt 0; }}
strong {{ font-weight: bold; }}
</style></head><body>{body}</body></html>"""

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    with pdf_path.open("wb") as f:
        status = pisa.CreatePDF(html_doc.encode("utf-8"), dest=f, encoding="utf-8")
    if status.err:
        raise RuntimeError(f"PDF generation failed with {status.err} error(s)")


def main() -> None:
    if not CSV_PATH.is_file():
        raise FileNotFoundError(f"Assessment CSV not found: {CSV_PATH}")

    rows = load_rows()
    md_text = build_markdown(rows)
    MD_PATH.write_text(md_text, encoding="utf-8")
    markdown_to_pdf(md_text, PDF_PATH)

    print(f"Rows: {len(rows)}")
    print(f"Markdown: {MD_PATH}")
    print(f"PDF: {PDF_PATH}")


if __name__ == "__main__":
    main()
