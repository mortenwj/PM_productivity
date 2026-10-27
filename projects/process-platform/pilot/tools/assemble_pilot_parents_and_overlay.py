"""Build pilot_weekly_parents_level1.json + overlay from batch1/bugs on disk."""
from __future__ import annotations

import json
import pathlib

TOOLS = pathlib.Path(__file__).resolve().parent

# wit_get (project 360), fields Id Title Type State Parent — parent closure only (not in WIQL batches)
PARENT_CLOSURE_RAW: list[dict] = [
    {"id": 143647, "fields": {"System.Id": 143647, "System.WorkItemType": "Feature", "System.State": "New", "System.Parent": 136166, "System.Title": "Role Based Workflows"}},
    {"id": 179509, "fields": {"System.Id": 179509, "System.WorkItemType": "Feature", "System.State": "New", "System.Parent": 90705, "System.Title": "IFAR - Access request reports"}},
    {"id": 228634, "fields": {"System.Id": 228634, "System.WorkItemType": "Feature", "System.State": "Active", "System.Parent": 90705, "System.Title": "Migrate emailscanner to GEMI"}},
    {"id": 296041, "fields": {"System.Id": 296041, "System.WorkItemType": "Feature", "System.State": "New", "System.Parent": 272636, "System.Title": "RV"}},
    {"id": 368549, "fields": {"System.Id": 368549, "System.WorkItemType": "Feature", "System.State": "Pending", "System.Title": "Tender requirement: Assign Processplan activities to multiple users and groups"}},
    {"id": 399190, "fields": {"System.Id": 399190, "System.WorkItemType": "Feature", "System.State": "New", "System.Parent": 90705, "System.Title": "IFAR - Redaction"}},
    {"id": 400794, "fields": {"System.Id": 400794, "System.WorkItemType": "Feature", "System.State": "New", "System.Parent": 414328, "System.Title": "PAF - Artifacts - Process Definitions"}},
    {"id": 410862, "fields": {"System.Id": 410862, "System.WorkItemType": "Epic", "System.State": "New", "System.Parent": 414623, "System.Title": "PAF - Discovery"}},
    {"id": 411061, "fields": {"System.Id": 411061, "System.WorkItemType": "User Story", "System.State": "Closed", "System.Parent": 276815, "System.Title": "IFAR processing should exclude file references"}},
    {"id": 411614, "fields": {"System.Id": 411614, "System.WorkItemType": "Epic", "System.State": "Active", "System.Parent": 414623, "System.Title": "PAF - Core Platform"}},
    {"id": 411623, "fields": {"System.Id": 411623, "System.WorkItemType": "Feature", "System.State": "New", "System.Parent": 414328, "System.Title": "PAF - Artifacts - Deadline Calculation Types"}},
    {"id": 413948, "fields": {"System.Id": 413948, "System.WorkItemType": "Feature", "System.State": "New", "System.Parent": 411612, "System.Title": "NVE Specific process definitions before go-live"}},
    {"id": 414353, "fields": {"System.Id": 414353, "System.WorkItemType": "Feature", "System.State": "Active", "System.Parent": 414328, "System.Title": "PAF - Artifacts - ProcessEngine - Designer Components"}},
    {"id": 414516, "fields": {"System.Id": 414516, "System.WorkItemType": "Feature", "System.State": "New", "System.Parent": 414328, "System.Title": "PAF - Artifacts - Standard Milestones"}},
    {"id": 414600, "fields": {"System.Id": 414600, "System.WorkItemType": "Feature", "System.State": "New", "System.Parent": 411614, "System.Title": "PAF - Core Platform - Trigger Data Model and Automation Relationships"}},
    {"id": 414622, "fields": {"System.Id": 414622, "System.WorkItemType": "Feature", "System.State": "New", "System.Parent": 410862, "System.Title": "Up For Discussions"}},
    {"id": 415996, "fields": {"System.Id": 415996, "System.WorkItemType": "Feature", "System.State": "New", "System.Parent": 414328, "System.Title": "PAF - Artifacts - Document Categories"}},
    {"id": 417484, "fields": {"System.Id": 417484, "System.WorkItemType": "Feature", "System.State": "New", "System.Parent": 411614, "System.Title": "PAF - trigger milestone on document dispatch"}},
    {"id": 418321, "fields": {"System.Id": 418321, "System.WorkItemType": "Feature", "System.State": "New", "System.Parent": 414328, "System.Title": "PAF artifacts : create email"}},
    {"id": 90705, "fields": {"System.Id": 90705, "System.WorkItemType": "Epic", "System.State": "Active", "System.Parent": 414659, "System.Title": "IFAR MLP"}},
    {"id": 136166, "fields": {"System.Id": 136166, "System.WorkItemType": "Epic", "System.State": "New", "System.Title": "SIT - Ministerial Services"}},
    {"id": 272636, "fields": {"System.Id": 272636, "System.WorkItemType": "Epic", "System.State": "Active", "System.Title": "Team Stuff"}},
    {"id": 276815, "fields": {"System.Id": 276815, "System.WorkItemType": "Feature", "System.State": "New", "System.Parent": 90705, "System.Title": "IFAR - handling file references"}},
    {"id": 414659, "fields": {"System.Id": 414659, "System.WorkItemType": "Epic", "System.State": "New", "System.Title": "IFAR - Freedom of Information request (FOI request)"}},
]


def load_batch(path: pathlib.Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    b1 = load_batch(TOOLS / "pilot_weekly_batch1.json")
    bugs = load_batch(TOOLS / "pilot_weekly_bugs_batch.json")
    seed_ids = set()
    for w in b1 + bugs:
        i = (w.get("fields") or {}).get("System.Id")
        if i is not None:
            seed_ids.add(int(i))

    parents_out = [
        row for row in PARENT_CLOSURE_RAW if int(row["fields"]["System.Id"]) not in seed_ids
    ]
    (TOOLS / "pilot_weekly_parents_level1.json").write_text(
        json.dumps(parents_out, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    keys_overlay = (
        "System.Description",
        "Microsoft.VSTS.Common.AcceptanceCriteria",
        "Microsoft.VSTS.Common.StateChangeDate",
        "System.Title",
        "System.WorkItemType",
    )
    overlay: list[dict] = []
    for w in b1 + bugs:
        f = w.get("fields") or {}
        i = f.get("System.Id")
        if i is None:
            continue
        slim = {"System.Id": i}
        for k in keys_overlay:
            if f.get(k) not in (None, ""):
                slim[k] = f[k]
        overlay.append({"id": int(i), "fields": slim})
    (TOOLS / "pilot_weekly_descriptions_overlay.json").write_text(
        json.dumps(overlay, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    meta = {
        "as_of_utc": "2026-04-21T20:31:38.820Z",
        "wiql_nonbug_as_of": "2026-04-21T20:31:38.820Z",
        "wiql_bug_as_of": "2026-04-21T20:31:46.653Z",
        "nonbug_ids": 50,
        "bug_ids": 28,
        "parent_closure_rows": len(parents_out),
    }
    (TOOLS / "pilot_weekly_query_meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    (TOOLS / "pilot_weekly_batch2.json").write_text("[\n]\n", encoding="utf-8")

    print("parents", len(parents_out), "overlay", len(overlay))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
