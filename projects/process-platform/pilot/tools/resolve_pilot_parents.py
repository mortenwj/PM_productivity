"""Resolve epic root for items from pilot weekly WIQL JSON exports (offline helper)."""
import json
import pathlib
import sys

ROOTS = frozenset({414328, 414727, 411612})


def main() -> int:
    paths = [pathlib.Path(p) for p in sys.argv[1:]]
    if not paths:
        print("Usage: py -3 tools/resolve_pilot_parents.py <batch1.json> [batch2.json ...]")
        return 2
    parent_by_id: dict[int, int | None] = {}
    meta_by_id: dict[int, dict] = {}
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        for w in data:
            f = w.get("fields") or {}
            i = f.get("System.Id")
            if i is None:
                continue
            parent_by_id[int(i)] = f.get("System.Parent")
            meta_by_id[int(i)] = {
                "title": f.get("System.Title", ""),
                "type": f.get("System.WorkItemType", ""),
                "state": f.get("System.State", ""),
                "changed": f.get("System.ChangedDate"),
                "resolved": f.get("Microsoft.VSTS.Common.ResolvedDate"),
                "closed": f.get("Microsoft.VSTS.Common.ClosedDate"),
            }
    # Placeholder: without live ADO, epic resolution needs parent chain loaded into parent_by_id
    missing = {p for p in parent_by_id.values() if p and p not in parent_by_id}
    print("items", len(parent_by_id), "missing_one_parent_level", len(missing))
    print("first_missing", sorted(missing)[:50])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
