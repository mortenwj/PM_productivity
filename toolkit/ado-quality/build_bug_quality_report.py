#!/usr/bin/env python3
"""
Build a Markdown report from ado-bug-report-quality evaluation JSON.

  python build_bug_quality_report.py -i eval.json -o report.md

Input schema matches .cursor/skills/ado-bug-report-quality/SKILL.md (workItems[]).
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _esc(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ")


def _gate_rows(gates: list[dict[str, Any]]) -> list[str]:
    lines = ["| Gate | Result | Evidence | Remediation |", "|------|--------|----------|-------------|"]
    for g in gates:
        rid = g.get("id", "")
        res = g.get("result", "")
        ev = _esc(str(g.get("evidence", "") or ""))
        rem = g.get("remediation")
        rem_s = "" if rem is None else _esc(str(rem))
        lines.append(f"| `{rid}` | {res} | {ev} | {rem_s} |")
    return lines


def _criteria_rows(criteria: list[dict[str, Any]]) -> list[str]:
    lines = ["| Criterion | Pts | Max | Note |", "|-----------|-----|-----|------|"]
    for c in criteria:
        cid = c.get("id", "")
        pts = c.get("points", 0)
        mx = c.get("max_points")
        if mx is None:
            mx_s = "1"
            pts_cell = str(pts)
        else:
            mx_s = str(mx)
            pts_cell = str(pts)
        note = _esc(str(c.get("note", "") or ""))
        lines.append(f"| `{cid}` | {pts_cell} | {mx_s} | {note} |")
    return lines


def build_markdown(data: dict[str, Any]) -> str:
    evaluated = data.get("evaluatedAt") or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    policy = data.get("policy") or {}
    notes = policy.get("notes") or []
    sources = policy.get("wikiSources") or []

    items = data.get("workItems") or []
    lines: list[str] = [
        "# Bug quality report",
        "",
        f"Generated from evaluation JSON (`evaluatedAt`: **{evaluated}**).",
        "",
    ]
    if notes:
        lines.append("## Policy notes")
        for n in notes:
            lines.append(f"- {n}")
        lines.append("")
    if sources:
        lines.append("## Wiki sources")
        for u in sources:
            lines.append(f"- {u}")
        lines.append("")

    lines.extend(
        [
            "## Overview",
            "",
            "| Work item | Critical | Score | Weighted | Label | Cap reason |",
            "|-----------|----------|-------|----------|-------|------------|",
        ]
    )

    for wi in sorted(items, key=lambda x: int(x.get("id", 0))):
        wid = wi.get("id", "")
        url = wi.get("url") or f"https://tieto-si.visualstudio.com/360/_workitems/edit/{wid}"
        gates = wi.get("gates") or {}
        oc = gates.get("overall_critical", "")
        q = wi.get("quality") or {}
        final = q.get("quality_score_final", "")
        raw = q.get("quality_score_raw", "")
        wpts = q.get("quality_weighted_points")
        wmax = q.get("quality_weighted_max")
        if wpts is not None and wmax is not None:
            wcell = f"{wpts}/{wmax}"
        else:
            wcell = str(raw) if raw != "" else "—"
        label = q.get("quality_label", "")
        cap = q.get("cap_reason")
        cap_s = "" if cap is None else str(cap)
        link = f"[#{wid}]({url})"
        lines.append(f"| {link} | **{oc}** | **{final}/10** | {wcell} | {label} | {cap_s} |")

    lines.extend(["", "---", "", "## Detailed breakdown", ""])

    for wi in sorted(items, key=lambda x: int(x.get("id", 0))):
        wid = wi.get("id", "")
        url = wi.get("url") or f"https://tieto-si.visualstudio.com/360/_workitems/edit/{wid}"
        gates = wi.get("gates") or {}
        q = wi.get("quality") or {}
        summary = wi.get("summary", "")

        lines.extend(
            [
                f"### #{wid}",
                "",
                f"**Work item:** [{url}]({url})",
                "",
                f"**Summary:** {summary}",
                "",
                "**Quality**",
                "",
                f"- **Final score:** {q.get('quality_score_final', '—')}/10 ({q.get('quality_label', '—')})",
                f"- **Normalized (0–10):** {q.get('quality_score_raw', '—')} (from weighted rubric)",
            ]
        )
        wpts = q.get("quality_weighted_points")
        wmax = q.get("quality_weighted_max")
        if wpts is not None and wmax is not None:
            lines.append(f"- **Weighted points:** {wpts}/{wmax} (Q2, Q6, Q7 up to 2 pts each; others up to 1)")
        cap = q.get("cap_reason")
        if cap:
            lines.append(f"- **Cap reason:** `{cap}`")
        lines.append("")

        crit = q.get("criteria") or []
        if crit:
            lines.append("**Scoring criteria** (repro / expected / actual weighted higher)")
            lines.append("")
            lines.extend(_criteria_rows(crit))
            lines.append("")

        lines.append("**Critical gates**")
        lines.append("")
        lines.extend(_gate_rows(gates.get("critical") or []))
        lines.append("")
        ap = gates.get("advisory_pass_count")
        af = gates.get("advisory_fail_count")
        if ap is not None or af is not None:
            lines.append(f"*Advisory pass/fail count:* {ap} / {af}")
            lines.append("")

        lines.append("**Advisory checks**")
        lines.append("")
        lines.extend(_gate_rows(gates.get("advisory") or []))
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    p = argparse.ArgumentParser(description="Build Markdown from bug quality evaluation JSON.")
    p.add_argument(
        "-i",
        "--input",
        required=True,
        help="Path to evaluation JSON (or '-' for stdin)",
    )
    p.add_argument(
        "-o",
        "--output",
        default="",
        help="Output Markdown path (default: <input stem>_report.md, or stdout if input is '-')",
    )
    args = p.parse_args()

    if args.input == "-":
        raw = sys.stdin.read()
        data = json.loads(raw)
        out_path = None
        if args.output:
            out_path = Path(args.output)
    else:
        in_path = Path(args.input)
        if not in_path.is_file():
            print(f"Error: file not found: {in_path}", file=sys.stderr)
            return 1
        data = json.loads(in_path.read_text(encoding="utf-8"))
        out_path = Path(args.output) if args.output else in_path.with_name(f"{in_path.stem}_report.md")

    md = build_markdown(data)

    if args.input == "-" and not args.output:
        sys.stdout.write(md)
        return 0

    assert out_path is not None
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(md, encoding="utf-8")
    print(f"Wrote {out_path.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
