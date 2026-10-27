"""Merge MCP evidence cache into tender AI draft overrides.

Reads uim-enrich-targets.json + mcp-evidence-cache.json, updates evidence/confidence
fields, writes enriched overrides for generate_tender_ai_drafts.py.

Example:
    uv run python toolkit/scripts/merge_mcp_enrichment.py
    uv run python toolkit/scripts/generate_tender_ai_drafts.py \\
        --overrides docs/tender-reference/ai-drafts/uim-MK-6.json \\
        --overrides docs/tender-reference/ai-drafts/uim-mcp-enriched.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TARGETS_PATH = REPO_ROOT / "docs/tender-reference/ai-drafts/uim-enrich-targets.json"
CACHE_PATH = REPO_ROOT / "docs/tender-reference/ai-drafts/uim-mcp-evidence-cache.json"
FULL_PATH = REPO_ROOT / "docs/tender-reference/ai-drafts/uim-full.json"
OUTPUT_PATH = REPO_ROOT / "docs/tender-reference/ai-drafts/uim-mcp-enriched.json"


def cache_key(req_id: str, document: str) -> str:
    return f"{req_id}|{document}"


def format_evidence(entry: dict) -> str:
    parts: list[str] = []
    rat = entry.get("ratatoskr") or []
    wiki = entry.get("wiki") or []
    local = entry.get("local") or []

    if rat:
        parts.append("Ratatoskr: " + "; ".join(rat[:3]))
    if wiki:
        parts.append("Wiki: " + "; ".join(wiki[:2]))
    if local:
        parts.append("Local: " + "; ".join(local[:2]))
    if not parts:
        return entry.get("evidence_note", "Ingen MCP-træffere; manuel verify påkrævet.")
    return " | ".join(parts)


def confidence_from_entry(entry: dict, base: str) -> str:
    if entry.get("confidence"):
        return str(entry["confidence"])
    has_rat = bool(entry.get("ratatoskr"))
    has_wiki = bool(entry.get("wiki"))
    if has_rat and has_wiki:
        return "Verified"
    if has_rat or has_wiki:
        return "Lead"
    return base


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--targets", type=Path, default=TARGETS_PATH)
    parser.add_argument("--cache", type=Path, default=CACHE_PATH)
    parser.add_argument("--full", type=Path, default=FULL_PATH)
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.targets.exists():
        raise SystemExit(f"Targets not found: {args.targets}")
    if not args.cache.exists():
        raise SystemExit(f"MCP cache not found: {args.cache}")

    targets = json.loads(args.targets.read_text(encoding="utf-8"))["targets"]
    cache = json.loads(args.cache.read_text(encoding="utf-8"))
    full_map = {
        (d["req_id"], d["document"]): d
        for d in json.loads(args.full.read_text(encoding="utf-8"))["drafts"]
    }

    drafts: list[dict] = []
    hit = miss = 0

    for target in targets:
        key = cache_key(target["req_id"], target["document"])
        base = full_map.get((target["req_id"], target["document"]), {})
        entry = cache.get("entries", {}).get(key) or cache.get(key)

        if not entry:
            miss += 1
            continue
        hit += 1

        draft = dict(base)
        draft["req_id"] = target["req_id"]
        draft["document"] = target["document"]
        draft["evidence"] = format_evidence(entry)
        draft["confidence"] = confidence_from_entry(entry, base.get("confidence", "Lead"))
        if entry.get("summary"):
            draft["summary"] = entry["summary"]
        if entry.get("gaps"):
            draft["gaps"] = entry["gaps"]
        if entry.get("compliance"):
            draft["compliance"] = entry["compliance"]
        draft["source"] = "Cursor / tender-response (MCP-enriched)"
        draft["run_id"] = cache.get("run_id", "uim-mcp-enrich")
        drafts.append(draft)

    payload = {
        "tender": "UIM ESDH",
        "enrichment": "ratatoskr+mediawiki",
        "drafts": drafts,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Wrote {len(drafts)} enriched overrides -> {args.output}")
    print(f"Cache hits: {hit}, misses: {miss} / {len(targets)} targets")
    return 0


if __name__ == "__main__":
    sys.exit(main())
