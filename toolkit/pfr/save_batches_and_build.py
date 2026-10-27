"""
Save batch JSON data to batch_N.json files, then run build_svenska_kyrkan_result.py.
Usage: python save_batches_and_build.py
Expects batch data in batches/ subfolder as batch_1.json, batch_2.json, etc.
Or pass --combine to merge all batch_*.json in cwd into all_batches_combined.json and build.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent


def main():
    # Combine existing batch_*.json into all_batches_combined.json
    all_items = []
    for p in sorted(ROOT.glob("batch_*.json")):
        if "batch_ids" in p.name:
            continue  # skip batch_ids_N.json (ID lists, not work items)
        try:
            with open(p) as f:
                data = json.load(f)
            items = data if isinstance(data, list) else data.get("value", [])
            items = [x for x in items if isinstance(x, dict) and ("fields" in x or "id" in x)]
            all_items.extend(items)
            print(f"  Loaded {p.name}: {len(items)} items")
        except Exception as e:
            print(f"  Skip {p}: {e}")

    if not all_items:
        print("No batch data found. Run MCP wit_get_work_items_batch_by_ids and save to batch_N.json")
        sys.exit(1)

    combined = ROOT / "all_batches_combined.json"
    with open(combined, "w", encoding="utf-8") as f:
        json.dump(all_items, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(all_items)} items to {combined}")

    # Run build
    import subprocess
    r = subprocess.run([sys.executable, str(ROOT / "build_svenska_kyrkan_result.py")], cwd=ROOT)
    sys.exit(r.returncode)


if __name__ == "__main__":
    main()
