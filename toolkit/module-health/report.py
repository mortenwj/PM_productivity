"""Render Module Health Scorecard as Markdown."""

from __future__ import annotations

from datetime import date
from typing import Any


def format_eur(value: float) -> str:
    return f"€{value:,.0f}"


def render_scorecard(
    scored_rows: list[dict[str, Any]],
    *,
    report_date: str | None = None,
    team_filter: str | None = None,
    module_filter: str | None = None,
    include_revenue: bool = False,
    revenue_source: str = "",
    ado_notes: list[str] | None = None,
    unmapped_count: int = 0,
) -> str:
    report_date = report_date or date.today().isoformat()
    title_team = team_filter or "All product teams"
    scope = module_filter or "All modules"
    mode = scored_rows[0].get("scoring_mode", "ado_only") if scored_rows else "ado_only"
    show_revenue = include_revenue and mode == "full"

    lines: list[str] = [
        f"# Module Health Scorecard — {report_date}",
        "",
        f"**Scope:** {title_team} · {scope}",
        f"**Scoring mode:** {'bugs + PFRs + revenue' if show_revenue else 'bugs + PFRs (ADO only)'}",
        "**ADO windows:** Bugs = last 90 days · PFRs = open (New, Active, Pending)",
        "",
        "> Scores are indicative — weights in `toolkit/module-health/scoring_config.json`.",
        "> Higher score = lower bug/PFR pressure relative to peers in scope.",
        "",
        "---",
        "",
        "## Summary table",
        "",
    ]

    if show_revenue:
        lines.extend(
            [
                "| Rank | Module | Team | Revenue (YTD) | Bugs (90d) | P1 (90d) | Open PFRs | Customers | Score | Band |",
                "|------|--------|------|---------------|------------|----------|-----------|-----------|-------|------|",
            ]
        )
        for rank, row in enumerate(scored_rows, 1):
            lines.append(
                "| {rank} | {module} | {team} | {rev} | {bugs} | {p1} | {pfr} | {cust} | {score} | {icon} {band} |".format(
                    rank=rank,
                    module=row["module"],
                    team=row.get("team", "Other"),
                    rev=format_eur(row.get("revenue_eur", 0)),
                    bugs=row.get("bugs_90d", 0),
                    p1=row.get("p1_bugs_90d", 0),
                    pfr=row.get("open_pfrs", 0),
                    cust=row.get("pfr_customers", 0),
                    score=row.get("health_score", 0),
                    icon=row.get("band_icon", ""),
                    band=row.get("band", ""),
                )
            )
    else:
        lines.extend(
            [
                "| Rank | Module | Team | Bugs (90d) | P1 (90d) | Open PFRs | Customers | Score | Band |",
                "|------|--------|------|------------|----------|-----------|-----------|-------|------|",
            ]
        )
        for rank, row in enumerate(scored_rows, 1):
            lines.append(
                "| {rank} | {module} | {team} | {bugs} | {p1} | {pfr} | {cust} | {score} | {icon} {band} |".format(
                    rank=rank,
                    module=row["module"],
                    team=row.get("team", "Other"),
                    bugs=row.get("bugs_90d", 0),
                    p1=row.get("p1_bugs_90d", 0),
                    pfr=row.get("open_pfrs", 0),
                    cust=row.get("pfr_customers", 0),
                    score=row.get("health_score", 0),
                    icon=row.get("band_icon", ""),
                    band=row.get("band", ""),
                )
            )

    insight_rows = [r for r in scored_rows if r.get("insights")]
    if insight_rows:
        lines.extend(["", "---", "", "## Insights", ""])
        for row in insight_rows:
            lines.append(f"### {row['module']} ({row.get('band', '')})")
            for insight in row["insights"]:
                lines.append(f"- {insight}")
            lines.append("")

    lines.extend(["---", "", "## Dimension scores (detail)", ""])
    if show_revenue:
        lines.append("| Module | Revenue rank | Growth | Bug burden | PFR backlog | Health |")
        lines.append("|--------|--------------|--------|------------|-------------|--------|")
        for row in scored_rows:
            lines.append(
                f"| {row['module']} | {row.get('revenue_rank', 0)} | "
                f"{row.get('growth_score', 0)} | {row.get('bug_score', 0)} | "
                f"{row.get('pfr_score', 0)} | **{row.get('health_score', 0)}** |"
            )
    else:
        lines.append("| Module | Bug burden | PFR backlog | Health |")
        lines.append("|--------|------------|-------------|--------|")
        for row in scored_rows:
            lines.append(
                f"| {row['module']} | {row.get('bug_score', 0)} | "
                f"{row.get('pfr_score', 0)} | **{row.get('health_score', 0)}** |"
            )

    if show_revenue and unmapped_count:
        lines.extend(
            [
                "",
                "---",
                "",
                f"**Note:** {unmapped_count} revenue product line(s) could not be mapped to a module.",
            ]
        )

    if show_revenue and revenue_source:
        lines.extend(["", f"**Revenue source:** {revenue_source}"])

    if ado_notes:
        lines.extend(["", "---", "", "## Data notes", ""])
        for note in ado_notes:
            lines.append(f"- {note}")

    lines.extend(
        [
            "",
            "---",
            "",
            "## How to regenerate",
            "",
            "Say **module health scorecard** in Cursor (skill: `module-health`), or run:",
            "",
            "```powershell",
            "uv run python toolkit/module-health/build_scorecard.py \\",
            "  --bugs outputs/scratch/module_health_bugs.json \\",
            "  --pfrs outputs/scratch/module_health_pfrs.json \\",
            "  --output outputs/portfolio/module_health.md",
            "```",
        ]
    )

    return "\n".join(lines)
