"""Extract PFR items related to search improvement, cross-entity, and meta fields."""

from __future__ import annotations

import csv
import json
import re
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = REPO_ROOT / "outputs/archive/_archive/large_inputs/pfrs (1).csv"
OUT_DIR = REPO_ROOT / "projects/search-experience/evidence/ado"

PATTERNS = {
    "cross_entity": re.compile(
        r"cross[\s-]?entity|tværs af entit|tværs af objekt|across entit|across object|"
        r"multiple entit|kombineret søg|combined search|søgning på tværs|search across|"
        r"case/document|case and document|document and case|relations between|relationships between|"
        r"included in.*search|search.*contact info|from advanced search case/document",
        re.I,
    ),
    "meta_fields_all": re.compile(
        r"all (customer|custom|standard)?\s*(specific )?metadata|all fields|alle felter|"
        r"add search field|searchable field|search field|metadatafield|meta data field|"
        r"customer-specific metadata|additional data.*search|configured fields|custom field.*search|"
        r"include.*field.*search|mark that the field should appear",
        re.I,
    ),
    "search_core": re.compile(
        r"advanced search|global search|saved search|search result|search assist|query builder|"
        r"avanceret søg|global søg|gemte søgninger",
        re.I,
    ),
}


def strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text or "")
    return re.sub(r"\s+", " ", text).strip()


def classify(text: str) -> list[str]:
    return [key for key, pattern in PATTERNS.items() if pattern.search(text)]


def tier(themes: list[str], text: str) -> str | None:
    if "cross_entity" in themes and "search_core" in themes:
        return "A"
    if "meta_fields_all" in themes and "search_core" in themes:
        if re.search(r"all customer|all metadata|alle felter|all fields", text, re.I):
            return "A"
        return "B"
    if "cross_entity" in themes:
        return "B"
    if "meta_fields_all" in themes and "search_core" in themes:
        return "B"
    return None


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rows: list[dict] = []

    with CSV_PATH.open(encoding="utf-8-sig", errors="replace", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            wid = (row.get("ID") or "").strip()
            if not wid.isdigit():
                continue

            title = (row.get("Title") or "").strip()
            state = (row.get("State") or "").strip()
            assigned = (row.get("Assigned To") or "").strip()
            tags = (row.get("Tags") or "").strip()
            desc = row.get("Description") or ""
            text = f"{title} {desc} {tags}"
            themes = classify(text)
            rel = tier(themes, text)
            if not rel:
                continue

            rows.append(
                {
                    "id": int(wid),
                    "title": title,
                    "state": state,
                    "assigned": assigned,
                    "tags": tags,
                    "tier": rel,
                    "themes": themes,
                    "excerpt": strip_html(desc)[:600],
                    "url": f"https://dev.azure.com/tieto-si/360/_workitems/edit/{wid}",
                }
            )

    rows.sort(key=lambda item: ({"A": 0, "B": 1}[item["tier"]], item["id"]))

    tier_a = [r for r in rows if r["tier"] == "A"]
    tier_b = [r for r in rows if r["tier"] == "B"]

    summary = {
        "generated": datetime.now().strftime("%Y-%m-%d"),
        "source": str(CSV_PATH.relative_to(REPO_ROOT)).replace("\\", "/"),
        "query_scope": "PFR Feature export snapshot (CSV); relevance filter for search + cross-entity/meta-field themes",
        "counts": {
            "total_matched": len(rows),
            "tier_A": len(tier_a),
            "tier_B": len(tier_b),
            "with_meta_fields_theme": sum(1 for r in rows if "meta_fields_all" in r["themes"]),
            "with_cross_entity_theme": sum(1 for r in rows if "cross_entity" in r["themes"]),
        },
        "tier_A": tier_a,
        "tier_B": tier_b,
        "all_items": rows,
    }

    json_path = OUT_DIR / "pfr-search-demand.json"
    json_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {json_path} ({len(rows)} items; A={len(tier_a)}, B={len(tier_b)})")


if __name__ == "__main__":
    main()
