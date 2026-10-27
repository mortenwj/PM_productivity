"""Merge Azure DevOps get_batch JSON export into nve_behov_ado_cache.json."""
from __future__ import annotations

import json
import sys
from pathlib import Path

CACHE = Path(__file__).resolve().parent / "nve_behov_ado_cache.json"


def load_batch_array(path: Path) -> list[dict]:
    lines = [
        ln
        for ln in path.read_text(encoding="utf-8").splitlines()
        if not ln.startswith("<<") and not ln.startswith("<</")
    ]
    text = "\n".join(lines)
    start = text.find("[")
    end = text.rfind("]") + 1
    if start < 0 or end <= start:
        raise ValueError(f"No JSON array in {path}")
    return json.loads(text[start:end])


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: merge_ado_batch_into_cache.py <batch.json.txt>", file=sys.stderr)
        return 1
    batch_path = Path(sys.argv[1])
    items = load_batch_array(batch_path)
    ado = json.loads(CACHE.read_text(encoding="utf-8"))
    for item in items:
        fields = item.get("fields") or {}
        wid = str(fields.get("System.Id") or item.get("id"))
        entry = ado.setdefault(wid, {})
        entry["type"] = fields.get("System.WorkItemType", entry.get("type", ""))
        entry["state"] = fields.get("System.State", entry.get("state", ""))
        entry["title"] = fields.get("System.Title", entry.get("title", ""))
        entry["iteration_path"] = fields.get("System.IterationPath") or ""
        entry["tags"] = fields.get("System.Tags") or ""
        if fields.get("System.CreatedDate"):
            entry["created"] = fields.get("System.CreatedDate")
        if fields.get("System.ChangedDate"):
            entry["changed"] = fields.get("System.ChangedDate")
    CACHE.write_text(json.dumps(ado, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Updated {len(items)} items in {CACHE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
