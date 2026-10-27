"""Split pfr_ids_1120.json into 6 batches of 200 for MCP wit_get_work_items_batch_by_ids."""
import json
from pathlib import Path

root = Path(__file__).parent
with open(root / "pfr_ids_1120.json") as f:
    ids = json.load(f)

for i in range(0, len(ids), 200):
    batch = ids[i:i+200]
    batch_num = i // 200 + 1
    with open(root / f"mcp_batch_{batch_num}_ids.json", "w") as f:
        json.dump(batch, f)
    print(f"Batch {batch_num}: {len(batch)} IDs, first={batch[0]}, last={batch[-1]}")
