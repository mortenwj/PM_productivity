#!/usr/bin/env python3
"""
Build Module Health Scorecard from ADO JSON snapshots (bugs + open PFRs).

Revenue is optional (--with-revenue) for when financial data is available again.

  uv run python toolkit/module-health/build_scorecard.py --dry-run
  uv run python toolkit/module-health/build_scorecard.py \\
    --bugs outputs/scratch/module_health_bugs.json \\
    --pfrs outputs/scratch/module_health_pfrs.json \\
    --team "Process Platform"
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

_PKG = Path(__file__).resolve().parent
if str(_PKG) not in sys.path:
    sys.path.insert(0, str(_PKG))

from ado_aggregator import (  # noqa: E402
    aggregate_bugs,
    aggregate_pfrs,
    load_json_file,
    merge_module_stats,
)
from report import render_scorecard  # noqa: E402
from revenue_loader import build_module_revenue  # noqa: E402
from scoring import score_modules  # noqa: E402


def _repo_root() -> Path:
    return _PKG.parent.parent


def _default_excel() -> Path:
    return _repo_root() / "External Revenue, EUR.xlsx"


def _dry_run_payload() -> tuple[list[dict], list[dict]]:
    bugs = [
        {"id": 1, "fields": {"Custom.ImpactedModule": "Dispatch", "Microsoft.VSTS.Common.Priority": 2}},
        {"id": 2, "fields": {"Custom.ImpactedModule": "Dispatch", "Microsoft.VSTS.Common.Priority": 1}},
        {"id": 3, "fields": {"Custom.ImpactedModule": "Process Engine", "Microsoft.VSTS.Common.Priority": 3}},
        {"id": 4, "fields": {"Custom.ImpactedModule": "Search", "Microsoft.VSTS.Common.Priority": 2}},
        {"id": 5, "fields": {"Custom.ImpactedModule": "Workflow", "Microsoft.VSTS.Common.Priority": 1}},
    ]
    pfrs = [
        {"id": 10, "fields": {"Custom.ImpactedModule": "Process Engine", "Custom.Customername": "Oslo Kommune"}},
        {"id": 11, "fields": {"Custom.ImpactedModule": "Process Engine", "Custom.Customername": "Bergen"}},
        {"id": 12, "fields": {"Custom.ImpactedModule": "Search", "Custom.Customername": "Trondheim"}},
        {"id": 13, "fields": {"Custom.ImpactedModule": "Workflow", "Custom.Customername": "Oslo Kommune"}},
        {"id": 14, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "Customer A"}},
    ]
    return bugs, pfrs


def build(
    *,
    excel_path: Path | None,
    bugs_path: Path | None,
    pfrs_path: Path | None,
    team_filter: str | None,
    module_filter: str | None,
    output_path: Path,
    include_revenue: bool = False,
    dry_run: bool = False,
) -> dict:
    ado_notes: list[str] = []
    unmapped_count = 0

    if dry_run:
        bugs_items, pfr_items = _dry_run_payload()
        revenue_data = {"by_module": {}, "unmapped_products": []}
        ado_notes.append("Dry-run mode — sample ADO data only.")
    else:
        if not bugs_path or not pfrs_path:
            raise SystemExit("Provide --bugs and --pfrs JSON paths, or use --dry-run.")
        bugs_items = load_json_file(bugs_path)
        pfr_items = load_json_file(pfrs_path)

    revenue_by_module: dict = {}
    revenue_source = ""

    if include_revenue:
        excel = excel_path or _default_excel()
        if excel.exists():
            revenue_data = build_module_revenue(excel)
            revenue_by_module = revenue_data["by_module"]
            unmapped_count = len(revenue_data.get("unmapped_products", []))
            revenue_source = str(excel)
        else:
            ado_notes.append(
                f"`--with-revenue` set but Excel not found at `{excel}` — scoring ADO signals only."
            )
            include_revenue = False
    else:
        ado_notes.append("Revenue excluded — scoring from ADO bugs and open PFRs only.")

    bug_stats = aggregate_bugs(bugs_items)
    pfr_stats = aggregate_pfrs(pfr_items)
    rows = merge_module_stats(
        revenue_by_module,
        bug_stats,
        pfr_stats,
        team_filter=team_filter,
        module_filter=module_filter,
    )

    if not rows:
        raise SystemExit("No modules matched the filters. Check team/module names and ADO payloads.")

    scored = score_modules(rows, include_revenue=include_revenue)
    markdown = render_scorecard(
        scored,
        report_date=date.today().isoformat(),
        team_filter=team_filter,
        module_filter=module_filter,
        include_revenue=include_revenue,
        revenue_source=revenue_source,
        ado_notes=ado_notes,
        unmapped_count=unmapped_count,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")

    return {
        "output": str(output_path),
        "module_count": len(scored),
        "scoring_mode": scored[0].get("scoring_mode") if scored else "ado_only",
        "top_module": scored[0]["module"] if scored else None,
        "top_score": scored[0]["health_score"] if scored else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Build Module Health Scorecard")
    parser.add_argument("--bugs", type=Path, help="JSON file with Bug work items from ADO MCP")
    parser.add_argument("--pfrs", type=Path, help="JSON file with open PFR work items from ADO MCP")
    parser.add_argument("--revenue-excel", type=Path, help="Path to External Revenue, EUR.xlsx")
    parser.add_argument("--with-revenue", action="store_true", help="Include revenue in scoring (optional)")
    parser.add_argument("--team", help="Filter to one product team (e.g. 'Process Platform')")
    parser.add_argument("--module", help="Filter to one module (e.g. 'Dispatch')")
    parser.add_argument(
        "--output",
        type=Path,
        default=_repo_root() / "outputs" / "portfolio" / "module_health.md",
    )
    parser.add_argument("--dry-run", action="store_true", help="Use sample ADO data for smoke test")
    parser.add_argument("--json-summary", action="store_true", help="Print JSON summary to stdout")
    args = parser.parse_args()

    result = build(
        excel_path=args.revenue_excel,
        bugs_path=args.bugs,
        pfrs_path=args.pfrs,
        team_filter=args.team,
        module_filter=args.module,
        output_path=args.output,
        include_revenue=args.with_revenue,
        dry_run=args.dry_run,
    )

    if args.json_summary:
        print(json.dumps(result, indent=2))
    else:
        print(f"Wrote {result['output']} ({result['module_count']} modules, {result['scoring_mode']})")


if __name__ == "__main__":
    main()
