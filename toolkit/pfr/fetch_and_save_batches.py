"""
Fetch all 23 batches via Azure DevOps REST API and save to batch_N.json.
Requires: AZURE_DEVOPS_ORG, AZURE_DEVOPS_PROJECT, AZURE_DEVOPS_PAT (or similar)
If not available, run MCP calls manually and save each batch to batch_1.json, etc.
"""
import json
import os
import sys
from pathlib import Path

IDS_FILE = Path(__file__).parent / "pfr_ids_1120.json"
BATCH_SIZE = 50
FIELDS = ["System.Id", "System.Title", "System.State", "System.AssignedTo", "Custom.Customername"]


def fetch_batch(ids: list) -> list:
    """Fetch work items via REST API. Returns list of work items."""
    org = os.environ.get("AZURE_DEVOPS_ORG", "tieto-si")
    project = os.environ.get("AZURE_DEVOPS_PROJECT", "360")
    pat = os.environ.get("AZURE_DEVOPS_PAT") or os.environ.get("ADO_PAT")
    if not pat:
        return None
    import base64
    import urllib.request
    auth = base64.b64encode(f":{pat}".encode()).decode()
    ids_param = ",".join(str(i) for i in ids)
    url = f"https://dev.azure.com/{org}/{project}/_apis/wit/workitems?ids={ids_param}&api-version=7.0"
    req = urllib.request.Request(url, headers={"Authorization": f"Basic {auth}"})
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read().decode())
    return data.get("value", [])


def main():
    with open(IDS_FILE) as f:
        all_ids = json.load(f)
    batches = [all_ids[i:i + BATCH_SIZE] for i in range(0, len(all_ids), BATCH_SIZE)]
    print(f"Total {len(all_ids)} IDs in {len(batches)} batches")
    for i, batch_ids in enumerate(batches):
        out = Path(__file__).parent / f"batch_{i+1}.json"
        if out.exists():
            print(f"  Batch {i+1}: exists, skip")
            continue
        items = fetch_batch(batch_ids)
        if items is None:
            print("No AZURE_DEVOPS_PAT - run MCP wit_get_work_items_batch_by_ids manually")
            sys.exit(1)
        with open(out, "w", encoding="utf-8") as f:
            json.dump(items, f, indent=2, ensure_ascii=False)
        print(f"  Batch {i+1}: saved {len(items)} items")


if __name__ == "__main__":
    main()
