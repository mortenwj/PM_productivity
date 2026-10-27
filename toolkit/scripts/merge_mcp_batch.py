"""Process batched MCP search results into evidence cache.

Agent writes batch JSON files; this script merges them.

Example batch file (docs/tender-reference/ai-drafts/mcp-batches/batch-01.json):
{
  "MK-30|Bilag 1.b": {
    "ratatoskr": ["Saved search (admin-en)"],
    "wiki": ["Some page"],
    "confidence": "Lead",
    "evidence_note": "optional"
  }
}
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CACHE_PATH = REPO_ROOT / "docs/tender-reference/ai-drafts/uim-mcp-evidence-cache.json"


def load_cache(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {
        "run_id": f"uim-mcp-enrich-{date.today().isoformat()}",
        "generated": date.today().isoformat(),
        "entries": {},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("batch_files", nargs="+", type=Path)
    parser.add_argument("--cache", type=Path, default=CACHE_PATH)
    args = parser.parse_args()

    cache = load_cache(args.cache)
    entries = cache.setdefault("entries", {})
    merged = 0
    for bf in args.batch_files:
        data = json.loads(bf.read_text(encoding="utf-8"))
        entries.update(data)
        merged += len(data)

    args.cache.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Merged {merged} entries; cache now has {len(entries)} entries -> {args.cache}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
