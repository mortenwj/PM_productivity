"""
Run full Svenska kyrkan PFR query.

1. Fetches PFR IDs via wit_get_query_results_by_id (id=bb65b39e-f496-4577-85d2-6211ec66c218)
2. Batch-fetches work items (50 per batch due to MCP/API limits)
3. Filters Custom.Customername contains "svenska kyrkan" (case insensitive)
4. Excludes 262489 if only "Svenska institutet"
5. Saves to svenska_kyrkan_full_query_result.json

Run via: Call MCP wit_get_query_results_by_id, then wit_get_work_items_batch_by_ids
in batches of 50. Save each batch to batch_1.json, batch_2.json, etc.
Then: python process_svenska_kyrkan_batches.py
"""

import json
from pathlib import Path

# IDs from query bb65b39e-f496-4577-85d2-6211ec66c218 (1120 total)
IDS_FILE = Path(__file__).parent / "pfr_ids_1120.json"
BATCH_SIZE = 50

def get_batches():
    with open(IDS_FILE) as f:
        ids = json.load(f)
    for i in range(0, len(ids), BATCH_SIZE):
        yield ids[i:i + BATCH_SIZE]

if __name__ == "__main__":
    batches = list(get_batches())
    print(f"Total IDs: {len(IDS_FILE.read_text())}")  # placeholder
    print(f"Batches of {BATCH_SIZE}: {len(batches)}")
    for i, b in enumerate(batches):
        print(f"  Batch {i+1}: {b[0]}..{b[-1]} ({len(b)} IDs)")
