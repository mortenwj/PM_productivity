"""Build MCP evidence cache for UIM enrich targets (agent-assisted).

Reads uim-enrich-targets.json, derives search queries per target, merges
agent-supplied MCP hit batches into uim-mcp-evidence-cache.json.

The agent calls Ratatoskr + MediaWiki externally and passes hits via --batch JSON.

Example batch file (hits.json):
{
  "MK-56|Bilag 1.b": {
    "ratatoskr": ["Mass update (admin-en)"],
    "wiki": ["360° Contact register cleaning tools"],
    "confidence": "Lead"
  }
}
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TARGETS_PATH = REPO_ROOT / "docs/tender-reference/ai-drafts/uim-enrich-targets.json"
CACHE_PATH = REPO_ROOT / "docs/tender-reference/ai-drafts/uim-mcp-evidence-cache.json"


def cache_key(req_id: str, document: str) -> str:
    return f"{req_id}|{document}"


def search_query(title: str, requirement: str = "") -> str:
    text = f"{title} {requirement[:120]}"
    text = re.sub(r"[^\w\sæøåÆØÅ-]", " ", text)
    words = [w for w in text.split() if len(w) > 3][:6]
    return " ".join(words) if words else title[:40]


def load_cache(path: Path) -> dict:
    if not path.exists():
        return {
            "run_id": f"uim-mcp-enrich-{date.today().isoformat()}",
            "generated": date.today().isoformat(),
            "entries": {},
        }
    return json.loads(path.read_text(encoding="utf-8"))


def save_cache(path: Path, cache: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--targets", type=Path, default=TARGETS_PATH)
    parser.add_argument("--cache", type=Path, default=CACHE_PATH)
    parser.add_argument("--batch", type=Path, help="JSON object of cache entries to merge")
    parser.add_argument("--list-missing", action="store_true", help="Print targets without cache entries")
    parser.add_argument("--export-queries", type=Path, help="Export search queries JSON for batch MCP")
    parser.add_argument("--seed-mk6", action="store_true", help="Seed MK-6 known evidence")
    return parser.parse_args()


def seed_mk6(entries: dict) -> None:
    entries["MK-6|Bilag 1.b"] = {
        "ratatoskr": [
            "Disposal (admin-en)",
            "Retention (Disposal) (admin-en)",
            "Purge (admin-en)",
            "File — Delete File Permanently (admin-en)",
            "Perform disposal (admin-en)",
        ],
        "wiki": [
            "360° Online Security Specifications customer version",
            "Build log hotfix packages",
        ],
        "confidence": "Verified",
        "evidence_note": "Sletteregler for sag/dokument/fil; gap på «alle Entiteter».",
    }


def main() -> int:
    args = parse_args()
    targets = json.loads(args.targets.read_text(encoding="utf-8"))["targets"]
    cache = load_cache(args.cache)
    entries: dict = cache.setdefault("entries", {})

    if args.seed_mk6:
        seed_mk6(entries)
        save_cache(args.cache, cache)
        print("Seeded MK-6")

    if args.batch:
        batch = json.loads(args.batch.read_text(encoding="utf-8"))
        entries.update(batch)
        save_cache(args.cache, cache)
        print(f"Merged {len(batch)} entries -> {args.cache}")

    if args.export_queries:
        queries = [
            {
                "key": cache_key(t["req_id"], t["document"]),
                "req_id": t["req_id"],
                "title": t["title"],
                "query": search_query(t["title"], t.get("requirement", "")),
            }
            for t in targets
        ]
        args.export_queries.write_text(
            json.dumps({"queries": queries}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"Exported {len(queries)} queries -> {args.export_queries}")

    if args.list_missing:
        missing = [
            t for t in targets if cache_key(t["req_id"], t["document"]) not in entries
        ]
        print(f"Missing: {len(missing)} / {len(targets)}")
        for t in missing:
            print(f"  {t['req_id']}|{t['document']} :: {search_query(t['title'])}")

    if not any([args.batch, args.list_missing, args.export_queries, args.seed_mk6]):
        print("No action. Use --seed-mk6, --batch, --list-missing, or --export-queries")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
