"""Compute module health scores and insight tags."""

from __future__ import annotations

from typing import Any

from revenue_loader import load_scoring_config


def _percentile_ranks(values: list[float]) -> list[float]:
    if not values:
        return []
    if len(values) == 1:
        return [50.0]
    sorted_vals = sorted(values)
    ranks: list[float] = []
    for v in values:
        below = sum(1 for x in sorted_vals if x < v)
        ranks.append(round(100 * below / (len(sorted_vals) - 1), 1))
    return ranks


def _bug_score(row: dict[str, Any], penalties: dict[str, Any]) -> float:
    bugs = row.get("bugs_90d", 0)
    p1 = row.get("p1_bugs_90d", 0)
    per = penalties.get("bugs_per_point", 2)
    mult = penalties.get("p1_bug_multiplier", 10)
    penalty = bugs * per + p1 * mult
    return max(0.0, 100.0 - min(100.0, penalty))


def _pfr_score(row: dict[str, Any], penalties: dict[str, Any]) -> float:
    open_pfrs = row.get("open_pfrs", 0)
    per = penalties.get("open_pfr_per_point", 3)
    return max(0.0, 100.0 - min(100.0, open_pfrs * per))


def _growth_score(row: dict[str, Any], growth_values: list[float]) -> float:
    growth = row.get("growth_eur", 0.0)
    if not any(g != 0 for g in growth_values):
        return 50.0
    if growth > 0:
        return min(100.0, 50.0 + growth / max(max(growth_values), 1) * 50)
    if growth < 0:
        return max(0.0, 50.0 + growth / min(min(growth_values), -1) * 50)
    return 50.0


def _band(score: float, bands: dict[str, Any]) -> tuple[str, str]:
    if score >= bands.get("healthy", 75):
        return "Healthy", "✅"
    if score >= bands.get("watch", 55):
        return "Watch", "⚠️"
    if score >= bands.get("at_risk", 35):
        return "At Risk", "🔴"
    return "Review", "⬜"


def _eval_insight(rule: dict[str, Any], scored: dict[str, Any]) -> bool:
    expr = rule.get("when", "")
    ctx = {
        "revenue_rank": scored.get("revenue_rank", 0),
        "revenue_eur": scored.get("revenue_eur", 0),
        "open_pfrs": scored.get("open_pfrs", 0),
        "pfr_customers": scored.get("pfr_customers", 0),
        "bugs_90d": scored.get("bugs_90d", 0),
        "p1_bugs_90d": scored.get("p1_bugs_90d", 0),
        "bug_score": scored.get("bug_score", 100),
    }
    try:
        return bool(eval(expr, {"__builtins__": {}}, ctx))
    except Exception:
        return False


def _has_revenue_data(rows: list[dict[str, Any]]) -> bool:
    return any(r.get("revenue_eur", 0) > 0 for r in rows)


def score_modules(rows: list[dict[str, Any]], *, include_revenue: bool = False) -> list[dict[str, Any]]:
    config = load_scoring_config()
    penalties = config.get("penalties", {})
    bands_cfg = config.get("bands", {})

    use_revenue = include_revenue and _has_revenue_data(rows)
    if use_revenue:
        weights = config.get("weights", {})
        insights_cfg = config.get("insights", [])
    else:
        weights = config.get("weights_ado_only", {"bug_burden": 0.55, "pfr_backlog": 0.45})
        insights_cfg = config.get("insights_ado_only", config.get("insights", []))

    revenues = [r.get("revenue_eur", 0.0) for r in rows]
    revenue_ranks = _percentile_ranks(revenues) if use_revenue else [0.0] * len(rows)
    growth_values = [r.get("growth_eur", 0.0) for r in rows]

    scored_rows: list[dict[str, Any]] = []
    for row, revenue_rank in zip(rows, revenue_ranks):
        bug_score = _bug_score(row, penalties)
        pfr_score = _pfr_score(row, penalties)
        growth_score = _growth_score(row, growth_values) if use_revenue else None

        if use_revenue:
            health = round(
                weights.get("revenue_rank", 0.35) * revenue_rank
                + weights.get("revenue_growth", 0.15) * (growth_score or 50.0)
                + weights.get("bug_burden", 0.25) * bug_score
                + weights.get("pfr_backlog", 0.25) * pfr_score,
                1,
            )
        else:
            health = round(
                weights.get("bug_burden", 0.55) * bug_score
                + weights.get("pfr_backlog", 0.45) * pfr_score,
                1,
            )

        band_label, band_icon = _band(health, bands_cfg)

        scored = {
            **row,
            "scoring_mode": "full" if use_revenue else "ado_only",
            "revenue_rank": revenue_rank if use_revenue else None,
            "bug_score": round(bug_score, 1),
            "pfr_score": round(pfr_score, 1),
            "growth_score": round(growth_score, 1) if growth_score is not None else None,
            "health_score": health,
            "band": band_label,
            "band_icon": band_icon,
            "insights": [],
        }

        for rule in insights_cfg:
            if _eval_insight(rule, scored):
                scored["insights"].append(rule.get("text", rule.get("id", "")))

        scored_rows.append(scored)

    scored_rows.sort(key=lambda r: r["health_score"], reverse=True)
    return scored_rows
