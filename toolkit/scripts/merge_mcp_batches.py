"""Auto-build MCP evidence cache by searching Ratatoskr + MediaWiki per target.

Uses MCP servers via the mcp Python SDK is not available; this script reads
pre-fetched batch JSON files from docs/tender-reference/ai-drafts/mcp-batches/.

The agent populates batch files; this merges them into uim-mcp-evidence-cache.json.

For automated fetch, run from agent session:
  enrich_mcp_targets.py (creates batch stubs)
"""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
QUERIES_PATH = REPO_ROOT / "docs/tender-reference/ai-drafts/uim-mcp-queries.json"
CACHE_PATH = REPO_ROOT / "docs/tender-reference/ai-drafts/uim-mcp-evidence-cache.json"
BATCH_DIR = REPO_ROOT / "docs/tender-reference/ai-drafts/mcp-batches"


def confidence(rat: list, wiki: list) -> str:
    if rat and wiki:
        return "Verified"
    if rat or wiki:
        return "Lead"
    return "Lead"


def main() -> int:
    cache = {
        "run_id": f"uim-mcp-enrich-{date.today().isoformat()}",
        "generated": date.today().isoformat(),
        "entries": {},
    }
    if CACHE_PATH.exists():
        existing = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
        cache["entries"] = existing.get("entries", {})

    merged = 0
    if BATCH_DIR.exists():
        for path in sorted(BATCH_DIR.glob("*.json")):
            batch = json.loads(path.read_text(encoding="utf-8"))
            cache["entries"].update(batch)
            merged += len(batch)

    entries = cache["entries"]
    rat_hits = sum(1 for e in entries.values() if e.get("ratatoskr"))
    wiki_hits = sum(1 for e in entries.values() if e.get("wiki"))

    CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Cache: {len(entries)} entries ({rat_hits} ratatoskr, {wiki_hits} wiki) -> {CACHE_PATH}")
    print(f"Merged {merged} from batches")
    return 0


if __name__ == "__main__":
    sys.exit(main())
