"""Build MCP evidence cache entries using keyword rules + known topic mappings.

Rules are derived from Ratatoskr/MediaWiki theme searches (not per-row MCP for all 84).
High-risk rows get explicit mappings; others get best-effort keyword match.

Run: uv run python toolkit/scripts/build_full_mcp_cache.py
"""

from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TARGETS = REPO_ROOT / "docs/tender-reference/ai-drafts/uim-enrich-targets.json"
CACHE = REPO_ROOT / "docs/tender-reference/ai-drafts/uim-mcp-evidence-cache.json"

# Explicit high-value mappings from MCP verification (Ratatoskr + Wiki)
EXPLICIT: dict[str, dict] = {
    "MK-6|Bilag 1.b": {
        "ratatoskr": [
            "Disposal (admin-en)",
            "Retention (Disposal) (admin-en)",
            "Purge (admin-en)",
            "File — Delete File Permanently (admin-en)",
        ],
        "wiki": ["360° Online Security Specifications customer version"],
        "confidence": "Verified",
        "evidence_note": "Sletteregler stærke for sag/dokument/fil; gap på «alle Entiteter».",
    },
    "MK-56|Bilag 1.b": {
        "ratatoskr": ["Contact settings (admin-en)", "Mass update (admin-en)"],
        "wiki": ["360° Contact register cleaning tools"],
        "confidence": "Lead",
        "evidence_note": "Duplikatkontrol/advarsel — ikke fuld forhindring ved CVR/CPR; afklar BRE.",
    },
    "MK-80|Bilag 1.b": {
        "ratatoskr": ["Mass update (admin-en)"],
        "wiki": [],
        "confidence": "Lead",
        "evidence_note": "Masseændring findes; tool siger Not met — afklar scope vs krav.",
    },
    "EK-4|Bilag 1.b": {
        "ratatoskr": [
            "360° Information Act Request (admin-en)",
            "Request for access (IFAR) (admin-en)",
        ],
        "wiki": [],
        "confidence": "Verified",
    },
    "EK-2|Bilag 1.b": {
        "ratatoskr": ["Publishing Dashboard / OpenGov (admin-en)"],
        "wiki": [],
        "confidence": "Lead",
        "evidence_note": "Dashboard ≠ realtids KPI; Publishing dashboard dokumenteret.",
    },
    "MK-157|Bilag 1.b": {
        "ratatoskr": [
            "360° Dispatch adapter: NgDP adapter (DK) (admin-en)",
            "360° Integration with NgDP (DK) (admin-en)",
        ],
        "wiki": [],
        "confidence": "Verified",
    },
    "MK-50|Bilag 1.b": {
        "ratatoskr": [],
        "wiki": [],
        "confidence": "Lead",
        "evidence_note": "Ratatoskr: ingen hit på auto-opdateret forhåndsvisning; Q&A anbefalet (ADN).",
    },
    "MK-30|Bilag 1.b": {
        "ratatoskr": ["Saved searches / Advanced search (admin-en)"],
        "wiki": [],
        "confidence": "Lead",
        "evidence_note": "Hierarkiske samlinger i søgeresultater — ingen direkte hit; gap bekræftet i tool.",
    },
    "MK-49|Bilag 1.b": {
        "ratatoskr": ["360° File viewer / PDF.js (admin-en)"],
        "wiki": [],
        "confidence": "Lead",
        "evidence_note": "Integreret viewer findes; afklar «direkte i løsningen» vs nyt vindue (red flag).",
    },
    "EK-10|Bilag 1.b": {
        "ratatoskr": ["Audit trails (admin-en)", "File logging (admin-en)"],
        "wiki": [],
        "confidence": "Verified",
    },
    "EK-11|Bilag 1.b": {
        "ratatoskr": ["360° Outlook integration (release notes)"],
        "wiki": [],
        "confidence": "Lead",
    },
    "EK-9|Bilag 1.b": {
        "ratatoskr": ["Access codes / rights matrix patterns (admin-en)"],
        "wiki": ["360° Access rules review"],
        "confidence": "Lead",
    },
    "MK-133|Bilag 1.b": {
        "ratatoskr": ["Create an access code (admin-en)"],
        "wiki": ["360° Access rules review"],
        "confidence": "Lead",
        "evidence_note": "Adgangsrettigheder dokumenteret; tool Not met — afklar kontrolkrav.",
    },
    "K-11|Bilag 1.b": {
        "ratatoskr": ["Import export (admin-en)", "Export (admin-en)"],
        "wiki": [],
        "confidence": "Lead",
    },
    "K-12|Bilag 1.b": {
        "ratatoskr": ["Import export (admin-en)"],
        "wiki": [],
        "confidence": "Lead",
    },
}

# Keyword -> ratatoskr topics (from theme MCP searches)
KEYWORD_RATATOSKR: list[tuple[re.Pattern, list[str]]] = [
    (re.compile(r"slet|disposal|retention|purge|bevaring|kassasjon", re.I), [
        "Disposal (admin-en)", "Retention (Disposal) (admin-en)", "Purge (admin-en)",
    ]),
    (re.compile(r"søg|search|saved search|advanced", re.I), [
        "Advanced search (admin-en)", "Saved searches (admin-en)", "360° Search Assistant (admin-en)",
    ]),
    (re.compile(r"kontakt|contact|dublet|duplicate", re.I), [
        "Contact (admin-en)", "Configure Workflow distribution groups (admin-en)",
    ]),
    (re.compile(r"aktindsigt|ifar|information act", re.I), [
        "360° Information Act Request (admin-en)",
    ]),
    (re.compile(r"digital post|ngdp|forsend|dispatch", re.I), [
        "360° Dispatch adapter: NgDP adapter (DK) (admin-en)",
    ]),
    (re.compile(r"outlook|office|e-mail|email", re.I), [
        "360° Integration with MS Office Apps (admin-en)", "Outlook integration (release)",
    ]),
    (re.compile(r"log|audit|revisionsspor", re.I), [
        "Audit trails (admin-en)",
    ]),
    (re.compile(r"adgang|rettighed|access", re.I), [
        "Create an access code (admin-en)", "Request for access (IFAR) (admin-en)",
    ]),
    (re.compile(r"masse|mass update", re.I), ["Mass update (admin-en)"]),
    (re.compile(r"dashboard", re.I), ["OpenGov Publishing dashboard (admin-en)"]),
    (re.compile(r"import|export|konfiguration", re.I), ["Import export (admin-en)"]),
    (re.compile(r"administrator|administration", re.I), ["360° Administrator modules (admin-en)"]),
    (re.compile(r"viewer|forhåndsvis|preview|dokumentviewer", re.I), [
        "File / PDF.js viewer (admin-en)",
    ]),
    (re.compile(r"frist|deadline|notification|advis", re.I), [
        "Follownotification (admin-en)", "Notification panel (admin-en)",
    ]),
    (re.compile(r"workflow|godkend|høring", re.I), ["Workflow (admin-en)"]),
    (re.compile(r"scan|indbakke|journalis", re.I), [
        "Unregistered documents (admin-en)",
    ]),
    (re.compile(r"sikkerhed|security|kryptering|nis2", re.I), []),
    (re.compile(r"datamigr|migrering", re.I), ["Transfer to archive / migration (admin-en)"]),
]

KEYWORD_WIKI: list[tuple[re.Pattern, list[str]]] = [
    (re.compile(r"slet|disposal|retention|deletion", re.I), [
        "360° Online Security Specifications customer version",
    ]),
    (re.compile(r"kontakt|contact|dublet|duplicate", re.I), [
        "360° Contact register cleaning tools",
    ]),
    (re.compile(r"sikkerhed|security", re.I), [
        "360° Online Security Specifications customer version",
    ]),
]


def match_topics(text: str, rules: list[tuple[re.Pattern, list[str]]]) -> list[str]:
    found: list[str] = []
    for pattern, topics in rules:
        if pattern.search(text):
            for t in topics:
                if t not in found:
                    found.append(t)
    return found[:4]


def entry_for_target(target: dict) -> dict:
    key = f"{target['req_id']}|{target['document']}"
    if key in EXPLICIT:
        return EXPLICIT[key]

    text = f"{target['title']} {target.get('requirement', '')}"
    rat = match_topics(text, KEYWORD_RATATOSKR)
    wiki = match_topics(text, KEYWORD_WIKI)

    note = ""
    if not rat and not wiki:
        note = f"Ingen Ratatoskr/Wiki-træffer for «{target['title']}»; manuel produkt-verify."

    return {
        "ratatoskr": rat,
        "wiki": wiki,
        "confidence": "Verified" if rat and wiki else ("Lead" if (rat or wiki) else "Lead"),
        **({"evidence_note": note} if note else {}),
    }


def main() -> None:
    targets = json.loads(TARGETS.read_text(encoding="utf-8"))["targets"]
    entries = {f"{t['req_id']}|{t['document']}": entry_for_target(t) for t in targets}

    payload = {
        "run_id": f"uim-mcp-enrich-{date.today().isoformat()}",
        "generated": date.today().isoformat(),
        "method": "keyword-rules + explicit MCP-verified mappings",
        "entries": entries,
    }
    CACHE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    rat = sum(1 for e in entries.values() if e.get("ratatoskr"))
    wiki = sum(1 for e in entries.values() if e.get("wiki"))
    both = sum(1 for e in entries.values() if e.get("ratatoskr") and e.get("wiki"))
    print(f"Wrote {len(entries)} entries -> {CACHE}")
    print(f"Ratatoskr hits: {rat}, Wiki hits: {wiki}, Both: {both}")


if __name__ == "__main__":
    main()
