"""
Fetch all 23 batches via Azure DevOps REST API and save to batch_1.json through batch_23.json.
Then runs save_batches_and_build.py to create all_batches_combined.json and build_svenska_kyrkan_result.py.

Requires: AZURE_DEVOPS_PAT or ADO_PAT environment variable.
Org: tieto-si, Project: 360.
"""
import base64
import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

IDS_FILE = Path(__file__).parent / "pfr_ids_1120.json"
BATCH_SIZE = 50
ORG = "tieto-si"
PROJECT = "360"


def fetch_batch(ids: list) -> list:
    """Fetch work items via Azure DevOps REST API. Returns list of work items."""
    pat = os.environ.get("AZURE_DEVOPS_PAT") or os.environ.get("ADO_PAT")
    if not pat:
        return None
    auth = base64.b64encode(f":{pat}".encode()).decode()
    ids_param = ",".join(str(i) for i in ids)
    url = f"https://dev.azure.com/{ORG}/{PROJECT}/_apis/wit/workitems?ids={ids_param}&api-version=7.0"
    req = urllib.request.Request(url, headers={"Authorization": f"Basic {auth}"})
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read().decode())
    return data.get("value", [])


def main():
    if not os.environ.get("AZURE_DEVOPS_PAT") and not os.environ.get("ADO_PAT"):
        print("PAT not set. Set AZURE_DEVOPS_PAT or ADO_PAT environment variable.")
        print("Example: $env:AZURE_DEVOPS_PAT = \"your_pat_here\"  (PowerShell)")
        print("         export AZURE_DEVOPS_PAT=\"your_pat_here\"  (bash)")
        sys.exit(1)

    with open(IDS_FILE) as f:
        all_ids = json.load(f)
    batches = [all_ids[i:i + BATCH_SIZE] for i in range(0, len(all_ids), BATCH_SIZE)]
    print(f"Total {len(all_ids)} IDs in {len(batches)} batches")

    root = Path(__file__).parent
    for i, batch_ids in enumerate(batches):
        out = root / f"batch_{i+1}.json"
        items = fetch_batch(batch_ids)
        if items is None:
            print("Fetch failed - PAT may be invalid")
            sys.exit(1)
        with open(out, "w", encoding="utf-8") as f:
            json.dump(items, f, indent=2, ensure_ascii=False)
        print(f"  Batch {i+1}: saved {len(items)} items")

    print("Running save_batches_and_build.py...")
    r = subprocess.run([sys.executable, str(root / "save_batches_and_build.py")], cwd=root)
    sys.exit(r.returncode)


if __name__ == "__main__":
    main()
