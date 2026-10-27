"""Generate markdown report from story-eval.json (user story quality evaluation)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser(description="Markdown report from story quality eval JSON.")
    base = Path(__file__).resolve().parent
    ap.add_argument(
        "-i",
        "--input",
        type=Path,
        default=base / "story-eval.json",
        help="Eval JSON (default: story-eval.json next to this script).",
    )
    ap.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Report .md path (default: story-quality-report.md, or story-quality-report-<id>.md for single-item eval files).",
    )
    args = ap.parse_args()
    data_path = args.input
    if args.output is not None:
        out_path = args.output
    else:
        name = data_path.name
        if name.startswith("story-eval-") and name.endswith(".json") and name != "story-eval.json":
            stem = name.removeprefix("story-eval-").removesuffix(".json")
            out_path = base / f"story-quality-report-{stem}.md"
        else:
            out_path = base / "story-quality-report.md"
    data = json.loads(data_path.read_text(encoding="utf-8"))

    scope = data.get("scope", {})
    agg = data.get("aggregateSummary", {})
    notes = data.get("evaluationNotes", [])
    stories = data.get("stories", [])

    lines: list[str] = []
    lines.append("# User story quality report")
    lines.append("")
    lines.append(f"**Evaluated (UTC):** `{data.get('evaluatedAt', '')}`")
    lines.append("")
    lines.append("## Scope")
    lines.append("")
    lines.append(f"| | |")
    lines.append(f"|---|---|")
    lines.append(f"| Team | {scope.get('team', '')} |")
    lines.append(f"| Iteration | {scope.get('iterationName', '')} |")
    lines.append(f"| Work item types | {', '.join(scope.get('workItemTypes', []))} |")
    lines.append(f"| Stories evaluated | {scope.get('storyCount', len(stories))} |")
    if scope.get("filterWorkItemIds"):
        lines.append(f"| Filter (work item IDs) | {', '.join(str(x) for x in scope['filterWorkItemIds'])} |")
    lines.append("")
    if notes:
        lines.append("## Evaluation notes")
        lines.append("")
        for n in notes:
            lines.append(f"- {n}")
        lines.append("")
    lines.append("## Aggregate summary")
    lines.append("")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Count | {agg.get('count', '')} |")
    lines.append(f"| Avg final score | {agg.get('avgFinalScore', '')} |")
    lines.append(f"| Non-compliant | {agg.get('nonCompliantCount', '')} |")
    lines.append("")
    if agg.get("topSystemicIssues"):
        lines.append("### Top systemic issues")
        lines.append("")
        for i in agg["topSystemicIssues"]:
            lines.append(f"- {i}")
        lines.append("")
    if agg.get("quickWins"):
        lines.append("### Quick wins")
        lines.append("")
        for q in agg["quickWins"]:
            lines.append(f"- {q}")
        lines.append("")
    lines.append("## Story summary")
    lines.append("")
    lines.append(
        "| ID | Title | Score | Status | Parent Feature/Epic | Format | AC | Risk | Parent |"
    )
    lines.append("|---:|---|---:|:---|:---:|:---:|:---:|:---:|:---:|")
    for s in sorted(stories, key=lambda x: x.get("id", 0)):
        d = s.get("dimensions", {})
        title = (s.get("title") or "").replace("|", "\\|")
        if len(title) > 70:
            title = title[:67] + "…"
        lines.append(
            "| [{id}](https://dev.azure.com/tieto-si/360/_workitems/edit/{id}) | {title} | {score} | {st} | {ph} | {sf} | {ac} | {rk} | {pl} |".format(
                id=s.get("id"),
                title=title,
                score=s.get("finalScore"),
                st=s.get("complianceStatus", ""),
                ph="Yes" if s.get("hasParentFeatureOrEpic") else "No",
                sf=d.get("storyFormat"),
                ac=d.get("acFormat"),
                rk=d.get("riskClassification"),
                pl=d.get("parentLink"),
            )
        )
    lines.append("")
    lines.append("## Non-compliant detail (issues)")
    lines.append("")
    for s in sorted(stories, key=lambda x: x.get("id", 0)):
        if s.get("complianceStatus") != "Non-Compliant":
            continue
        sid = s.get("id")
        lines.append(f"### #{sid} — {s.get('title', '')}")
        lines.append("")
        for issue in s.get("issues") or []:
            lines.append(f"- {issue}")
        lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(out_path)


if __name__ == "__main__":
    main()
