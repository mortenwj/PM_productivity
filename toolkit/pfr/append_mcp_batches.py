"""
Append MCP-fetched batch data to all_batches_combined.json.
Usage: Create batch_2.json, batch_3.json, etc. with work item data, then run:
  python append_mcp_batches.py

Or pass JSON files as arguments:
  python append_mcp_batches.py batch_2.json batch_3.json ...

Combines with existing batch_1.json and all_batches_combined.json, then runs build.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent


def main():
    all_items = []
    # Load existing batch_*.json (work item data, not batch_ids_*)
    for p in sorted(ROOT.glob("batch_*.json")):
        if "batch_ids" in p.name:
            continue
        try:
            with open(p) as f:
                data = json.load(f)
            items = data if isinstance(data, list) else data.get("value", [])
            items = [x for x in items if isinstance(x, dict) and ("fields" in x or "id" in x)]
            all_items.extend(items)
            print(f"  Loaded {p.name}: {len(items)} items")
        except Exception as e:
            print(f"  Skip {p}: {e}")

    # Also load any extra JSON files passed as args
    for arg in sys.argv[1:]:
        p = ROOT / arg if not Path(arg).is_absolute() else Path(arg)
        if p.exists():
            with open(p) as f:
                data = json.load(f)
            items = data if isinstance(data, list) else data.get("value", [])
            items = [x for x in items if isinstance(x, dict) and ("fields" in x or "id" in x)]
            all_items.extend(items)
            print(f"  Loaded {arg}: {len(items)} items")

    if not all_items:
        print("No batch data. Save MCP responses to batch_2.json, batch_3.json, etc.")
        sys.exit(1)

    # Dedupe by id
    seen = {}
    for wi in all_items:
        aid = wi.get("id") or wi.get("fields", {}).get("System.Id")
        if aid and aid not in seen:
            seen[aid] = wi
    all_items = list(seen.values())
    print(f"Total {len(all_items)} unique work items")

    combined = ROOT / "all_batches_combined.json"
    with open(combined, "w", encoding="utf-8") as f:
        json.dump(all_items, f, indent=2, ensure_ascii=False)
    print(f"Saved to {combined}")

    r = subprocess.run([sys.executable, str(ROOT / "build_svenska_kyrkan_result.py")], cwd=ROOT)
    sys.exit(r.returncode)


if __name__ == "__main__":
    main()
