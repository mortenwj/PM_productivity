import json
from collections import Counter
from pathlib import Path

p = Path(
    r"C:\Users\MortenJensen\.cursor\projects\c-Users-MortenJensen-source-repos-te-industry-public360-core-bl\agent-tools\e170cc56-c79a-4648-9ccc-9b69e4ed0b61.txt"
)
data = json.loads(p.read_text(encoding="utf-8"))
items = data.get("workItems", data)
states = Counter()
types = Counter()
for wi in items:
    f = wi.get("fields", wi)
    states[f.get("System.State", "Unknown")] += 1
    types[f.get("System.WorkItemType", "Unknown")] += 1

print("Total items:", len(items))
print("By state:", dict(states))
print("By type:", dict(types))
print("\nNVE-related:")
for wi in items:
    f = wi.get("fields", wi)
    title = f.get("System.Title", "")
    if "NVE" in title:
        print(f"{f.get('System.Id')} | {f.get('System.State')} | {title[:90]}")
