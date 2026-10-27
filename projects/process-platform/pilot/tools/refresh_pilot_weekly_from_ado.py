"""
Refresh pilot weekly JSON batches from Azure DevOps (WIQL + workitemsbatch).

Uses WIQL files:
  projects/process-platform/pilot/tools/pilot_weekly_nonbug_wiql_asof_*.txt
  projects/process-platform/pilot/tools/pilot_weekly_bug_wiql_asof_*.txt

Requires: AZURE_DEVOPS_PAT or ADO_PAT (Work Items Read).

Writes:
  pilot_weekly_batch1.json, pilot_weekly_batch2.json (empty array),
  pilot_weekly_bugs_batch.json, pilot_weekly_parents_level1.json,
  pilot_weekly_descriptions_overlay.json

Then run: py -3 projects/process-platform/pilot/tools/generate_pilot_weekly_report.py
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ADO_BATCH_CHUNK = 200
WIQL_API = "7.1"
WORKITEMSBATCH_API = "7.1-preview.1"

DEFAULT_NONBUG = TOOLS / "pilot_weekly_nonbug_wiql_asof_2026-04-21.txt"
DEFAULT_BUG = TOOLS / "pilot_weekly_bug_wiql_asof_2026-04-21.txt"

BATCH_FIELDS = [
    "System.Id",
    "System.Title",
    "System.WorkItemType",
    "System.State",
    "System.Parent",
    "System.ChangedDate",
    "Microsoft.VSTS.Common.ResolvedDate",
    "Microsoft.VSTS.Common.ClosedDate",
    "Microsoft.VSTS.Common.StateChangeDate",
]

PARENT_FIELDS = [
    "System.Id",
    "System.Title",
    "System.WorkItemType",
    "System.State",
    "System.Parent",
]

OVERLAY_FIELDS = [
    "System.Id",
    "System.Title",
    "System.WorkItemType",
    "System.Description",
    "Microsoft.VSTS.Common.AcceptanceCriteria",
    "Microsoft.VSTS.Common.StateChangeDate",
]

TARGET_EPICS = frozenset({411612, 414727, 414328})
PROGRAM = 414623


def _auth_header() -> str:
    pat = os.environ.get("AZURE_DEVOPS_PAT") or os.environ.get("ADO_PAT")
    if not pat:
        raise SystemExit(
            "Set AZURE_DEVOPS_PAT or ADO_PAT (Work Items Read) for live WIQL/batch fetch."
        )
    token = base64.b64encode(f":{pat}".encode()).decode()
    return f"Basic {token}"


def _wiql_ids(query: str, organization: str, project: str) -> list[int]:
    org_q = urllib.parse.quote(organization, safe="")
    proj_q = urllib.parse.quote(project, safe="")
    url = (
        f"https://dev.azure.com/{org_q}/{proj_q}/_apis/wit/wiql"
        f"?api-version={WIQL_API}"
    )
    auth = _auth_header()
    body = json.dumps({"query": query}).encode()
    req = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={"Content-Type": "application/json", "Authorization": auth},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            payload = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")
        raise SystemExit(f"WIQL failed HTTP {e.code}: {detail[:1200]}") from e
    except urllib.error.URLError as e:
        raise SystemExit(f"WIQL request failed: {e.reason!r}") from e
    out: list[int] = []
    for row in payload.get("workItems") or []:
        wid = row.get("id")
        if wid is not None:
            out.append(int(wid))
    return out


def _workitemsbatch(
    ids: list[int],
    *,
    organization: str,
    project: str,
    fields: list[str],
) -> list[dict]:
    if not ids:
        return []
    org_q = urllib.parse.quote(organization, safe="")
    proj_q = urllib.parse.quote(project, safe="")
    url = (
        f"https://dev.azure.com/{org_q}/{proj_q}/_apis/wit/workitemsbatch"
        f"?api-version={WORKITEMSBATCH_API}"
    )
    auth = _auth_header()
    result: list[dict] = []
    unique = sorted(set(ids))
    for i in range(0, len(unique), ADO_BATCH_CHUNK):
        chunk = unique[i : i + ADO_BATCH_CHUNK]
        body = json.dumps({"ids": chunk, "fields": fields}).encode()
        req = urllib.request.Request(
            url,
            data=body,
            method="POST",
            headers={"Content-Type": "application/json", "Authorization": auth},
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                payload = json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            detail = e.read().decode(errors="replace")
            raise SystemExit(f"workitemsbatch failed HTTP {e.code}: {detail[:1200]}") from e
        for row in payload.get("value", []):
            result.append(
                {
                    "id": row["id"],
                    "rev": row.get("rev"),
                    "fields": row.get("fields", {}),
                    "multilineFieldsFormat": row.get("multilineFieldsFormat") or {},
                    "url": row.get("url", ""),
                }
            )
    return result


def _fields_map(items: list[dict]) -> dict[int, dict]:
    out: dict[int, dict] = {}
    for w in items:
        f = w.get("fields") or {}
        i = f.get("System.Id")
        if i is not None:
            out[int(i)] = f
    return out


def _parent_closure(
    seed_items: list[dict],
    *,
    organization: str,
    project: str,
) -> list[dict]:
    """Fetch ancestors not in `seed_items`, until parent is epic root / program / unknown."""
    by_id = _fields_map(seed_items)
    seed_ids = set(by_id.keys())

    def parent_int(f: dict) -> int | None:
        p = f.get("System.Parent")
        if p is None:
            return None
        try:
            return int(p)
        except (TypeError, ValueError):
            return None

    to_fetch: set[int] = set()
    for f in by_id.values():
        pid = parent_int(f)
        if pid is None:
            continue
        if pid in seed_ids or pid in TARGET_EPICS or pid == PROGRAM:
            continue
        if pid not in by_id:
            to_fetch.add(pid)

    rounds = 0
    while to_fetch and rounds < 60:
        rounds += 1
        batch = _workitemsbatch(
            sorted(to_fetch), organization=organization, project=project, fields=PARENT_FIELDS
        )
        to_fetch.clear()
        for w in batch:
            f = w.get("fields") or {}
            i = f.get("System.Id")
            if i is None:
                continue
            by_id[int(i)] = f
        for f in batch:
            fl = f.get("fields") or {}
            i = fl.get("System.Id")
            if i is None:
                continue
            pid = parent_int(fl)
            if pid is None:
                continue
            if pid in TARGET_EPICS or pid == PROGRAM:
                continue
            if pid not in by_id:
                to_fetch.add(pid)

    extra: list[dict] = []
    for i, f in sorted(by_id.items()):
        if i in seed_ids:
            continue
        extra.append(
            {
                "id": i,
                "fields": {k: v for k, v in f.items() if k in PARENT_FIELDS},
            }
        )
    return extra


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--org", default="tieto-si")
    ap.add_argument("--project", default="360")
    ap.add_argument("--nonbug-wiql", type=Path, default=DEFAULT_NONBUG)
    ap.add_argument("--bug-wiql", type=Path, default=DEFAULT_BUG)
    args = ap.parse_args()

    nonbug_q = args.nonbug_wiql.read_text(encoding="utf-8").strip()
    bug_q = args.bug_wiql.read_text(encoding="utf-8").strip()

    as_of = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print("Query time (UTC):", as_of)

    ids_nonbug = _wiql_ids(nonbug_q, args.org, args.project)
    ids_bug = _wiql_ids(bug_q, args.org, args.project)
    print("Non-Bug WIQL count:", len(ids_nonbug))
    print("Bug WIQL count:", len(ids_bug))

    batch_main = _workitemsbatch(
        ids_nonbug, organization=args.org, project=args.project, fields=BATCH_FIELDS
    )
    batch_bugs = _workitemsbatch(
        ids_bug, organization=args.org, project=args.project, fields=BATCH_FIELDS
    )

    seed = batch_main + batch_bugs
    parents_extra = _parent_closure(seed, organization=args.org, project=args.project)
    print("Parent closure rows (not in WIQL batches):", len(parents_extra))

    scope_ids = sorted(
        set(ids_nonbug) | set(ids_bug) | {int(w["fields"]["System.Id"]) for w in parents_extra}
    )
    overlay = _workitemsbatch(
        scope_ids, organization=args.org, project=args.project, fields=OVERLAY_FIELDS
    )

    (TOOLS / "pilot_weekly_batch1.json").write_text(
        json.dumps(batch_main, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (TOOLS / "pilot_weekly_batch2.json").write_text("[\n]\n", encoding="utf-8")
    (TOOLS / "pilot_weekly_bugs_batch.json").write_text(
        json.dumps(batch_bugs, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (TOOLS / "pilot_weekly_parents_level1.json").write_text(
        json.dumps(parents_extra, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (TOOLS / "pilot_weekly_descriptions_overlay.json").write_text(
        json.dumps(overlay, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    meta = {
        "as_of_utc": as_of,
        "nonbug_count": len(ids_nonbug),
        "bug_count": len(ids_bug),
        "parent_closure_count": len(parents_extra),
    }
    (TOOLS / "pilot_weekly_query_meta.json").write_text(
        json.dumps(meta, indent=2) + "\n", encoding="utf-8"
    )
    print("Wrote projects/process-platform/pilot/tools/pilot_weekly_*.json and pilot_weekly_query_meta.json")
    print("Suggested report header line: **ADO query as-of (UTC):** " + as_of + " (Azure DevOps REST).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
