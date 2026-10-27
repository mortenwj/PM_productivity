"""
Build svenska_kyrkan_full_query_result.json from batch data.
First looks for all_batches_combined.json (single array of all work items).
Else uses batch_1.json, batch_2.json, etc.
"""
import json
import re
import sys
from pathlib import Path

EXCLUDE_ID = 262489  # Svenska institutet only


def matches(cn):
    if not cn or not isinstance(cn, str):
        return False
    return bool(re.search(r"svenska\s*kyrkan", cn, re.IGNORECASE))


def exclude_institut_only(cn):
    if not cn or not isinstance(cn, str):
        return False
    c = cn.lower()
    return "svenska kyrkan" not in c and "svenska institutet" in c


def to_item(wi):
    f = wi.get("fields", {})
    aid = wi.get("id") or f.get("System.Id")
    at = f.get("System.AssignedTo")
    if isinstance(at, dict):
        at = at.get("displayName", "")
    else:
        at = str(at) if at else ""
    cn = f.get("Custom.Customername") or f.get("Custom.CustomerName") or ""
    return {
        "id": aid,
        "title": f.get("System.Title", ""),
        "state": f.get("System.State", ""),
        "assignedTo": at,
        "customername": str(cn),
    }


def main():
    root = Path(__file__).parent
    all_items = []

    combined_path = root / "all_batches_combined.json"
    if combined_path.exists():
        with open(combined_path) as f:
            data = json.load(f)
        all_items = data if isinstance(data, list) else data.get("value", [])
    else:
        for p in sorted(root.glob("batch_*.json")):
            if "batch_ids" in p.name:
                continue  # skip batch_ids_N.json (ID lists, not work items)
            with open(p) as f:
                data = json.load(f)
            items = data if isinstance(data, list) else data.get("value", [])
            # Only include items that look like work items (have id/fields)
            items = [x for x in items if isinstance(x, dict) and ("fields" in x or "id" in x)]
            all_items.extend(items)

    seen = set()
    out = []
    for wi in all_items:
        f = wi.get("fields", {})
        cn = str(f.get("Custom.Customername") or f.get("Custom.CustomerName") or "")
        if not matches(cn):
            continue
        aid = wi.get("id") or f.get("System.Id")
        if aid == EXCLUDE_ID and exclude_institut_only(cn):
            continue
        if aid in seen:
            continue
        seen.add(aid)
        out.append(to_item(wi))

    out.sort(key=lambda x: x["id"])
    out_path = root / "svenska_kyrkan_full_query_result.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(out)} Svenska kyrkan PFRs to {out_path}")


if __name__ == "__main__":
    main()
