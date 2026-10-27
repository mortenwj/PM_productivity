"""Concatenate product objectives strategy docs into a ChatGPT context export."""

from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
OUT_DIR = REPO / "outputs"

SECTIONS: list[tuple[str, str]] = [
    ("docs/product-strategy/team-objectives-strategy-brief-2026.md", "Strategy brief"),
    ("docs/product-strategy/agent-strategy-appendix-d7.md", "Agent strategy appendix D7/D8/D9"),
    ("docs/product-strategy/team-objectives-refresh-workbook-2026.md", "LPM workbook Phase A + B"),
    ("docs/product-strategy/team-objectives-proposal-2026.md", "QCLT proposal summary"),
    ("docs/product-strategy/qclt-objectives-alignment-pack-2026.md", "QCLT alignment pack"),
    ("docs/product-strategy/qclt-objectives-decision-sheet-2026.md", "QCLT decision sheet"),
    ("docs/product-strategy/quadcore-meeting-pack-2026.md", "QuadCore session guide"),
    ("docs/product-strategy/quadcore-meeting-one-pager-2026.md", "QuadCore one-pager"),
    ("docs/product-strategy/quadcore-meeting-decision-sheet-2026.md", "QuadCore decision sheet"),
    ("docs/product-strategy/quadcore-objectives-alignment-2026.md", "QuadCore alignment detail"),
    ("docs/tender-reference/UIM-management-gate-brief.md", "UIM management gate brief"),
    ("docs/tender-reference/KK-management-gate-brief.md", "KK management gate brief"),
    ("docs/tender-reference/VNK-Vahva-management-gate-brief.md", "VN Asia Vahva gate brief"),
    ("outputs/pfr/dss_uim_tender_overlap_analysis.md", "DSS vs UIM overlap analysis"),
]

HEADER = """# Public 360° — Product team objectives (2026–2027) — ChatGPT context export

**Generated:** {date}
**Purpose:** Single bundle for continuing objective/KR work in ChatGPT.

## Suggested ChatGPT opener

You are helping refine Public 360° product team objectives for 2026–27. Use this export as source of truth. Rules: max 2–3 objectives per team; CO1–CO3 company themes; AI Software Factory is a program overlay (not CO4); customer AI is CO3/AI1–AI2 separate from factory; UIM spine direction stands post-offer regardless of award (D1 = phasing only); PP2 BRE gates CU1. Produce workshop-ready KRs and ProductPlan Phase A actions.

---

"""


def build_full() -> str:
    from datetime import date

    parts = [HEADER.format(date=date.today().isoformat())]
    for rel, title in SECTIONS:
        path = REPO / rel
        parts.append(f"\n<!-- BEGIN: {rel} -->\n\n# [{title}]\n\n")
        if path.exists():
            parts.append(path.read_text(encoding="utf-8"))
        else:
            parts.append(f"<!-- MISSING: {rel} -->")
        parts.append(f"\n<!-- END: {rel} -->\n")
    return "".join(parts)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    full_path = OUT_DIR / "product-team-objectives-chatgpt-export-2026.md"
    text = build_full()
    full_path.write_text(text, encoding="utf-8")

    marker = "<!-- BEGIN: docs/tender-reference/UIM-management-gate-brief.md -->"
    idx = text.find(marker)
    if idx == -1:
        raise SystemExit("split marker not found")
    part1 = text[:idx].rstrip() + "\n"
    part2 = (
        "# Public 360° objectives export — Part 2 (tender background)\n\n"
        "Upload **after** Part 1 in the same ChatGPT project/thread.\n\n---\n\n"
        + text[idx:]
    )
    (OUT_DIR / "product-team-objectives-chatgpt-export-2026-part1-strategy.md").write_text(
        part1, encoding="utf-8"
    )
    (OUT_DIR / "product-team-objectives-chatgpt-export-2026-part2-tenders.md").write_text(
        part2, encoding="utf-8"
    )
    print(f"Wrote {full_path} ({full_path.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
