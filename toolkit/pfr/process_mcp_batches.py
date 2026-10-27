"""Process MCP batch output files and build Svenska kyrkan result."""
import json
import re
from pathlib import Path

# agent-tools can be in different locations
for candidate in [
    Path(__file__).parent.parent / "agent-tools",  # sibling of PM_productivity
    Path(r"C:\Users\jensemor\.cursor\projects\c-Users-jensemor-cursor-projects-PM-productivity-PM-productivity\agent-tools"),
    Path(__file__).parent / "agent-tools",
]:
    if candidate.exists():
        AGENT_TOOLS = candidate
        break
else:
    AGENT_TOOLS = Path(__file__).parent

BATCH_FILES = [
    "fb0adabf-b03b-479a-af60-598cf588c0fa.txt",
    "9f757a45-c67c-4c33-8b8e-c756ee397c16.txt",
    "984ef787-3b6e-457a-b760-dc1fd8cd5bf9.txt",
    "ba45e97e-9827-4ad7-97ce-7c3f04e60409.txt",
    "cced6c04-c93c-4c08-9e6f-c642d492bf97.txt",
    "cd88121d-23ff-4979-9fb7-5615c73bf988.txt",
]

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


def main():
    all_items = []
    for fname in BATCH_FILES:
        p = AGENT_TOOLS / fname
        if not p.exists():
            # Try glob
            matches_list = list(Path(__file__).parent.rglob(fname))
            if matches_list:
                p = matches_list[0]
            else:
                print(f"Skip {fname} (not found)")
                continue
        with open(p, encoding="utf-8") as f:
            data = json.load(f)
        items = data if isinstance(data, list) else data.get("value", [])
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
        at = f.get("System.AssignedTo")
        if isinstance(at, dict):
            at = at.get("displayName", "")
        else:
            at = str(at) if at else ""
        out.append({
            "id": aid,
            "title": f.get("System.Title", ""),
            "state": f.get("System.State", ""),
            "assignedTo": at,
            "customername": cn,
        })

    out.sort(key=lambda x: x["id"])
    out_path = Path(__file__).parent / "svenska_kyrkan_full_query_result.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(out)} Svenska kyrkan PFRs to {out_path}")
    for item in out:
        print(f"  {item['id']}: {item['title'][:60]}...")


if __name__ == "__main__":
    main()
