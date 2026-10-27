"""Aggregate Azure DevOps work items into per-module bug and PFR statistics."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from revenue_loader import load_taxonomy


def _normalize_module(raw: str | None, aliases: dict[str, str]) -> str | None:
    if not raw or raw.strip() in ("", "0 - Not applicable"):
        return None
    name = raw.strip()
    return aliases.get(name, name)


def _field(item: dict[str, Any], key: str, default: Any = None) -> Any:
    fields = item.get("fields") or {}
    return fields.get(key, default)


def _items_from_payload(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        if "workItems" in payload:
            return payload["workItems"]
        if "value" in payload and isinstance(payload["value"], list):
            # wit_query wiql full response
            ids = [w.get("id") for w in payload["value"] if w.get("id")]
            if ids and all(isinstance(i, int) for i in ids):
                return [{"id": i, "fields": {}} for i in ids]
        if "items" in payload:
            return payload["items"]
    return []


def aggregate_bugs(bugs_payload: Any) -> dict[str, dict[str, int]]:
    taxonomy = load_taxonomy()
    aliases = taxonomy.get("aliases", {})
    stats: dict[str, dict[str, int]] = defaultdict(lambda: {"bugs_90d": 0, "p1_bugs_90d": 0})

    for item in _items_from_payload(bugs_payload):
        module = _normalize_module(_field(item, "Custom.ImpactedModule"), aliases)
        if not module:
            continue
        stats[module]["bugs_90d"] += 1
        priority = _field(item, "Microsoft.VSTS.Common.Priority")
        try:
            if priority is not None and int(priority) == 1:
                stats[module]["p1_bugs_90d"] += 1
        except (TypeError, ValueError):
            pass

    return dict(stats)


def aggregate_pfrs(pfr_payload: Any) -> dict[str, dict[str, int]]:
    taxonomy = load_taxonomy()
    aliases = taxonomy.get("aliases", {})
    stats: dict[str, dict[str, Any]] = defaultdict(
        lambda: {"open_pfrs": 0, "pfr_customers": set()}
    )

    for item in _items_from_payload(pfr_payload):
        module = _normalize_module(_field(item, "Custom.ImpactedModule"), aliases)
        if not module:
            continue
        stats[module]["open_pfrs"] += 1
        customer = (
            _field(item, "Custom.Customername")
            or _field(item, "Custom.CustomerName")
            or _field(item, "System.Title")
        )
        if customer and isinstance(customer, str) and customer.strip():
            stats[module]["pfr_customers"].add(customer.strip().lower())

    result: dict[str, dict[str, int]] = {}
    for module, data in stats.items():
        result[module] = {
            "open_pfrs": data["open_pfrs"],
            "pfr_customers": len(data["pfr_customers"]),
        }
    return result


def merge_module_stats(
    revenue_by_module: dict[str, dict[str, Any]],
    bug_stats: dict[str, dict[str, int]],
    pfr_stats: dict[str, dict[str, int]],
    *,
    team_filter: str | None = None,
    module_filter: str | None = None,
) -> list[dict[str, Any]]:
    """Union modules from all sources into rows for scoring."""
    taxonomy = load_taxonomy()
    module_to_team = taxonomy.get("module_to_team", {})
    modules: set[str] = set(revenue_by_module) | set(bug_stats) | set(pfr_stats)

    rows: list[dict[str, Any]] = []
    for module in sorted(modules):
        team = module_to_team.get(module, "Other")
        if team_filter and team != team_filter:
            continue
        if module_filter and module != module_filter:
            continue

        rev = revenue_by_module.get(module, {})
        bugs = bug_stats.get(module, {})
        pfrs = pfr_stats.get(module, {})

        rows.append(
            {
                "module": module,
                "team": rev.get("team") or team,
                "revenue_eur": rev.get("revenue_eur", 0.0),
                "growth_eur": rev.get("growth_eur", 0.0),
                "bugs_90d": bugs.get("bugs_90d", 0),
                "p1_bugs_90d": bugs.get("p1_bugs_90d", 0),
                "open_pfrs": pfrs.get("open_pfrs", 0),
                "pfr_customers": pfrs.get("pfr_customers", 0),
            }
        )
    return rows


def load_json_file(path: str | Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))
