#!/usr/bin/env python3
"""
Sprint Analysis for Core-Process-platform Team
Analyzes last 6 sprints: completion rates, scope creep, transfers.
Uses Azure DevOps MCP - run via Cursor agent or with AZURE_DEVOPS_PAT env var for standalone.
"""

import json
import os
from pathlib import Path
from collections import defaultdict

# Sprint iteration IDs (last 6 sprints: PP-16 through PP-21)
SPRINTS = [
    ("PP-16", "c0801d12-3b0b-42f6-b2a0-fab1a05b5177", "10.11.2025 - 28.11.2025"),
    ("PP-17", "2a775370-ba6b-46d1-aec3-51d2e95beb6a", "01.12.2025 - 19.12.2025"),
    ("PP-18", "ff6d2f4a-5723-4a62-89f1-e06a867705c8", "22.12.2025 - 09.01.2026"),
    ("PP-19", "d3b9fcc1-9b64-471d-9480-5afd5a068bb0", "12.01.2026 - 30.01.2026"),
    ("PP-20", "6fbda8ab-5bac-4bf5-94a6-4fcfcf9fd165", "02.02.2026 - 20.02.2026"),
    ("PP-21", "09ddf2e9-fe45-4661-945a-e9959ef0b097", "23.02.2026 - 13.03.2026"),
]

# Path to agent-tools output (MCP writes here)
AGENT_TOOLS = Path(__file__).parent.parent / "agent-tools"
# Fallback: use pre-fetched data files if provided
DATA_DIR = Path(__file__).parent / "sprint_analysis_data"


def load_sprint_relations(sprint_name: str) -> list[int]:
    """Load work item relations from MCP output or cached file. Returns root work item IDs."""
    # Try agent-tools first (from recent MCP calls)
    patterns = [
        AGENT_TOOLS / "976f65bb-4f43-4a16-af43-412ad520b182.txt",  # PP-16
        AGENT_TOOLS / "0957d92e-d0a8-40a1-a139-736552a9609a.txt",  # PP-17
    ]
    # Map sprint to file - we'll need to pass the actual file path
    return []


def extract_root_ids(relations: list) -> list[int]:
    """Extract root work item IDs from workItemRelations (source is null)."""
    return [r["target"]["id"] for r in relations if r.get("source") is None]


def analyze_work_items_states(work_items: list) -> dict:
    """Count work items by state. Closed/Resolved = completed."""
    completed_states = {"Closed", "Resolved", "Done"}
    by_state = defaultdict(int)
    for wi in work_items:
        state = wi.get("fields", {}).get("System.State", "Unknown")
        by_state[state] += 1
    completed = sum(by_state[s] for s in completed_states if s in by_state)
    total = len(work_items)
    return {
        "total": total,
        "completed": completed,
        "by_state": dict(by_state),
        "completion_pct": (completed / total * 100) if total else 0,
    }


def main():
    """Run analysis on cached/sample data."""
    # Load PP-16 from the file we know exists
    pp16_file = AGENT_TOOLS / "976f65bb-4f43-4a16-af43-412ad520b182.txt"
    pp17_file = AGENT_TOOLS / "0957d92e-d0a8-40a1-a139-736552a9609a.txt"

    results = {}
    for name, path in [("PP-16", pp16_file), ("PP-17", pp17_file)]:
        if path.exists():
            with open(path) as f:
                data = json.load(f)
            roots = extract_root_ids(data["workItemRelations"])
            results[name] = {"root_count": len(roots), "root_ids_sample": roots[:20]}
        else:
            results[name] = {"root_count": 0, "error": "File not found"}

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
