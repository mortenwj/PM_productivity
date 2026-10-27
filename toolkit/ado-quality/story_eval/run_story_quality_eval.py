"""One-off helper: merge ADO batch JSON files and score user stories (heuristic)."""
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from html import unescape
from pathlib import Path

STORY_EVAL = Path(__file__).resolve().parent

# Fields aligned with MCP `wit_get_work_items_batch_by_ids` / policy in `copilot-instructions.md`.
ADO_STORY_BATCH_FIELDS = [
    "System.Id",
    "System.Title",
    "System.WorkItemType",
    "System.State",
    "System.Description",
    "Microsoft.VSTS.Common.AcceptanceCriteria",
    "System.Parent",
    "Microsoft.VSTS.Common.Risk",
    "Custom.Riskdescription",
    "System.IterationPath",
]

ADO_WORKITEMSBATCH_API = "7.1-preview.1"
ADO_BATCH_CHUNK = 200


def strip_html(html: str | None) -> str:
    if not html:
        return ""
    t = re.sub(r"<[^>]+>", " ", html)
    return unescape(re.sub(r"\s+", " ", t)).strip()


def _parse_risk_value(risk_raw) -> int | None:
    """ADO may return 1–3, or strings like '3 - Low' / '1 - High'."""
    if risk_raw is None or risk_raw == "":
        return None
    if isinstance(risk_raw, (int, float)):
        v = int(risk_raw)
        return v if v in (1, 2, 3) else None
    s = str(risk_raw).strip()
    m = re.match(r"^([1-3])\b", s)
    if m:
        return int(m.group(1))
    try:
        v = int(float(s))
        return v if v in (1, 2, 3) else None
    except (TypeError, ValueError):
        return None


def _load_work_items() -> list:
    """Prefer latest PP22 merge (includes Risk fields), then generic merge, then legacy agent-tools batches."""
    pp22 = STORY_EVAL / "_merged_pp22_batches.json"
    if pp22.exists():
        return json.loads(pp22.read_text(encoding="utf-8"))
    merged = STORY_EVAL / "_merged_story_batches.json"
    if merged.exists():
        return json.loads(merged.read_text(encoding="utf-8"))
    base = Path(
        r"C:\Users\jensemor\.cursor\projects\c-Users-jensemor-cursor-projects-PM-productivity-PM-productivity\agent-tools"
    )
    batches = [
        base / "607f1164-a36e-4ad7-98ea-95f8f215bda5.txt",
        base / "57b9a675-1dd7-48b3-94f1-7b306ffd06a7.txt",
    ]
    items = []
    for p in batches:
        if p.exists():
            items.extend(json.loads(p.read_text(encoding="utf-8")))
    return items


def _ado_basic_auth_header() -> str:
    pat = os.environ.get("AZURE_DEVOPS_PAT") or os.environ.get("ADO_PAT")
    if not pat:
        raise SystemExit(
            "Live fetch needs a Personal Access Token. Set environment variable AZURE_DEVOPS_PAT or ADO_PAT "
            "(Azure DevOps: User settings, Personal access tokens; scope Work Items Read)."
        )
    token = base64.b64encode(f":{pat}".encode()).decode()
    return f"Basic {token}"


def _fetch_work_items_batch(
    ids: list[int],
    *,
    organization: str,
    project: str,
    fields: list[str],
) -> list[dict]:
    """POST workitemsbatch; returns MCP-style list of {id, rev?, fields}."""
    if not ids:
        return []
    org_q = urllib.parse.quote(organization, safe="")
    proj_q = urllib.parse.quote(project, safe="")
    url = (
        f"https://dev.azure.com/{org_q}/{proj_q}/_apis/wit/workitemsbatch"
        f"?api-version={ADO_WORKITEMSBATCH_API}"
    )
    auth = _ado_basic_auth_header()
    out: list[dict] = []
    for i in range(0, len(ids), ADO_BATCH_CHUNK):
        chunk = ids[i : i + ADO_BATCH_CHUNK]
        body = json.dumps({"ids": chunk, "fields": fields}).encode()
        req = urllib.request.Request(
            url,
            data=body,
            method="POST",
            headers={
                "Content-Type": "application/json",
                "Authorization": auth,
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                payload = json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            detail = e.read().decode(errors="replace")
            raise SystemExit(
                f"Azure DevOps workitemsbatch failed (HTTP {e.code}) for {organization}/{project}: {detail[:800]}"
            ) from e
        except urllib.error.URLError as e:
            raise SystemExit(f"Azure DevOps request failed: {e.reason!r}") from e
        for row in payload.get("value", []):
            out.append({"id": row["id"], "rev": row.get("rev"), "fields": row.get("fields", {})})
    return out


def fetch_work_items_from_ado(
    ids: list[int],
    *,
    organization: str,
    project: str,
) -> list[dict]:
    """Latest work item revisions for `ids` (story evaluation fields)."""
    unique = sorted(set(ids))
    return _fetch_work_items_batch(
        unique,
        organization=organization,
        project=project,
        fields=ADO_STORY_BATCH_FIELDS,
    )


def _merge_parent_types_from_ado(
    base: dict[int, str],
    parent_ids: set[int],
    *,
    organization: str,
    project: str,
) -> dict[int, str]:
    missing = [pid for pid in parent_ids if pid and pid not in base]
    if not missing:
        return base
    merged = dict(base)
    for it in _fetch_work_items_batch(
        sorted(missing),
        organization=organization,
        project=project,
        fields=["System.Id", "System.WorkItemType"],
    ):
        f = it.get("fields", {})
        wid, wt = f.get("System.Id"), f.get("System.WorkItemType")
        if wid is not None and wt:
            merged[int(wid)] = str(wt)
    return merged


def _load_parent_types() -> dict[int, str]:
    p = STORY_EVAL / "_parent_types_pp22.json"
    if p.exists():
        return {int(k): v for k, v in json.loads(p.read_text(encoding="utf-8")).items()}
    return {
        228634: "Feature",
        230801: "Feature",
        273420: "Feature",
        276815: "Feature",
        344868: "Feature",
        348439: "Feature",
        373512: "Epic",
        381967: "Feature",
        391561: "Feature",
        397370: "Feature",
        399007: "Feature",
        399190: "Feature",
        400785: "Feature",
        400794: "Feature",
        402354: "Feature",
        406819: "Feature",
        410828: "Feature",
        412681: "Feature",
        414351: "Feature",
        414353: "Feature",
        414516: "Feature",
        414600: "Feature",
        414750: "Feature",
        414994: "Feature",
        415983: "Feature",
        415986: "Feature",
        415991: "Feature",
        415993: "Feature",
        415996: "Feature",
    }


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Score User Stories from cached ADO batch JSON or live Azure DevOps (--fetch)."
    )
    ap.add_argument(
        "--id",
        type=int,
        action="append",
        dest="ids",
        metavar="WORK_ITEM_ID",
        help="Only evaluate this work item ID (repeat for multiple). With --fetch, pulls live; else uses cached merge JSON.",
    )
    ap.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Write evaluation JSON here. Default: story-eval.json, or story-eval-<id>.json when a single --id is set.",
    )
    ap.add_argument(
        "--fetch",
        action="store_true",
        help="Load work items via Azure DevOps REST (workitemsbatch). Requires AZURE_DEVOPS_PAT or ADO_PAT and --id.",
    )
    ap.add_argument(
        "--organization",
        default="tieto-si",
        help="Azure DevOps organization name (default: tieto-si). Used with --fetch.",
    )
    ap.add_argument(
        "--project",
        default="360",
        help="Azure DevOps project (default: 360). Used with --fetch.",
    )
    ap.add_argument(
        "--batch-json",
        type=Path,
        default=None,
        help="JSON array of Azure DevOps batch work items ({id, fields, ...}). Skips default merge files.",
    )
    ap.add_argument(
        "--parent-types-json",
        type=Path,
        default=None,
        help='Optional JSON object mapping parent work item ID (string or int key) to WorkItemType, e.g. {"414994": "Feature"}. Merged over built-in parent map.',
    )
    ap.add_argument(
        "--scope-team",
        default=None,
        help="Optional team name written into output scope (e.g. Core-Process-platform).",
    )
    ap.add_argument(
        "--scope-iteration-name",
        default=None,
        help="Optional iteration display name for output scope.",
    )
    ap.add_argument(
        "--scope-iteration-id",
        default=None,
        help="Optional iteration GUID for output scope.",
    )
    args = ap.parse_args()

    if args.fetch and args.batch_json:
        raise SystemExit("Use either --fetch or --batch-json, not both.")

    if args.fetch and not args.ids:
        raise SystemExit("--fetch requires at least one --id (which items to pull live from Azure DevOps).")

    if args.batch_json:
        items = json.loads(args.batch_json.read_text(encoding="utf-8"))
        if not isinstance(items, list):
            raise SystemExit("--batch-json must contain a JSON array of work items.")
        parent_types = _load_parent_types()
        if args.parent_types_json:
            raw_pt = json.loads(args.parent_types_json.read_text(encoding="utf-8"))
            if not isinstance(raw_pt, dict):
                raise SystemExit("--parent-types-json must be a JSON object.")
            for k, v in raw_pt.items():
                parent_types[int(k)] = str(v)
        if args.ids:
            wanted = set(args.ids)
            items = [it for it in items if it.get("fields", {}).get("System.Id") in wanted]
            found = {it.get("fields", {}).get("System.Id") for it in items}
            missing = wanted - found
            if missing:
                raise SystemExit(
                    f"No work items in batch for ID(s): {sorted(missing)} (check --batch-json contents)."
                )
    elif args.fetch:
        unique_ids = sorted(set(args.ids))
        items = fetch_work_items_from_ado(unique_ids, organization=args.organization, project=args.project)
        if len(items) != len(unique_ids):
            got = {it.get("fields", {}).get("System.Id") for it in items}
            missing = set(unique_ids) - got
            if missing:
                raise SystemExit(f"ADO returned no data for ID(s): {sorted(missing)} (check project/org and token scope).")
        parent_types = _load_parent_types()
        parent_ids: set[int] = set()
        for it in items:
            f = it.get("fields", {})
            if f.get("System.WorkItemType") == "User Story" and f.get("System.Parent") is not None:
                parent_ids.add(int(f["System.Parent"]))
        parent_types = _merge_parent_types_from_ado(
            parent_types, parent_ids, organization=args.organization, project=args.project
        )
    else:
        items = _load_work_items()
        if not items:
            raise SystemExit("No work item batches found. Add _merged_pp22_batches.json or legacy batch files.")

        if args.ids:
            wanted = set(args.ids)
            items = [
                it
                for it in items
                if it.get("fields", {}).get("System.Id") in wanted
            ]
            found = {it.get("fields", {}).get("System.Id") for it in items}
            missing = wanted - found
            if missing:
                raise SystemExit(
                    f"No work items loaded for ID(s): {sorted(missing)} "
                    f"(refresh the merge file or run with --fetch --id …)."
                )

        parent_types = _load_parent_types()

    vague = re.compile(
        r"\b(optimize|improve|and/or|etc\.|as needed|user friendly|TBD)\b", re.I
    )
    nfr_kw = re.compile(
        r"\b(performance|security|availability|accessibilit|gdpr|encryption|latency|scalab)\b",
        re.I,
    )

    stories_out = []
    for it in items:
        f = it.get("fields", {})
        if f.get("System.WorkItemType") != "User Story":
            continue
        wid = f.get("System.Id")
        title = f.get("System.Title") or ""
        desc_raw = f.get("System.Description") or ""
        ac_raw = f.get("Microsoft.VSTS.Common.AcceptanceCriteria") or ""
        parent = f.get("System.Parent")

        plain_d = strip_html(desc_raw).lower()
        plain_ac = strip_html(ac_raw).lower()
        combined = plain_d + " " + plain_ac

        is_tech = title.strip().lower().startswith("[tech]") or title.strip().lower().startswith(
            "[enabler]"
        )
        story_type = "Tech" if title.strip().lower().startswith("[tech]") else (
            "Enabler" if title.strip().lower().startswith("[enabler]") else "User Story"
        )

        if is_tech:
            story_format = 85 if len(plain_d) > 80 else 40
        else:
            has_as = "as a" in plain_d
            has_want = "i want" in plain_d or "i need" in plain_d
            has_benefit = "so that" in plain_d
            if has_as and has_want and has_benefit:
                story_format = 100
            elif (has_as and has_want) or (has_want and has_benefit):
                story_format = 55
            else:
                story_format = 25

        if is_tech:
            ac_fmt = (
                100
                if re.search(r"the system must|this solution shall", plain_ac)
                else 50
                if len(plain_ac) > 40
                else 20
            )
        else:
            g, w, t = ("given" in plain_ac), ("when" in plain_ac), ("then" in plain_ac)
            if not plain_ac and "acceptance criteria" in plain_d:
                g = "given" in plain_d
                w = "when" in plain_d
                t = "then" in plain_d
            cnt = sum([g, w, t])
            if cnt >= 3:
                ac_fmt = 100
            elif cnt == 2:
                ac_fmt = 60
            elif cnt == 1:
                ac_fmt = 30
            else:
                ac_fmt = 15 if len(plain_ac) > 30 else 0

        ac_test = 85
        if vague.search(plain_ac) or vague.search(plain_d[:2000]):
            ac_test = 45
        if len(plain_ac) < 20 and "acceptance criteria" not in plain_d:
            ac_test = min(ac_test, 35)

        # Project 360: Risk field ref from wit_get_work_item_type ("User Story") —
        # Microsoft.VSTS.Common.Risk (label "Risk"); narrative: Custom.Riskdescription
        risk_raw = f.get("Microsoft.VSTS.Common.Risk")
        risk_val = _parse_risk_value(risk_raw)
        risk_c = 100 if risk_val in (1, 2, 3) else 0

        risk_desc_raw = f.get("Custom.Riskdescription") or ""
        plain_risk_desc = strip_html(risk_desc_raw)
        if risk_val in (1, 2):
            risk_d = (
                100
                if len(plain_risk_desc) >= 20
                else 50
                if len(plain_risk_desc) >= 8
                else 0
            )
        elif risk_val == 3:
            risk_d = 100
        else:
            risk_d = 0

        L = len(plain_d)
        if L > 12000 or plain_d.count("step ") > 8:
            story_size = 45
        elif L > 6000:
            story_size = 70
        else:
            story_size = 90

        if is_tech:
            business = 75 if len(plain_d) > 100 else 50
        else:
            m = re.search(r"so that\s+(.{15,})", plain_d)
            business = 100 if m else 35 if "so that" in plain_d else 20

        if nfr_kw.search(combined):
            nfr = 85 if nfr_kw.search(plain_ac) or "nfr" in plain_d else 50
        else:
            nfr = 100

        pt = parent_types.get(int(parent)) if parent else None
        parent_ok = pt in ("Feature", "Epic")
        parent_score = 100 if (parent and parent_ok) else 0
        deps_score = 70

        weights = {
            "storyFormat": 0.15,
            "acFormat": 0.125,
            "acTestability": 0.125,
            "riskClassification": 0.10,
            "riskDescription": 0.05,
            "storySize": 0.15,
            "businessValue": 0.15,
            "nfrConsideration": 0.05,
            "parentLink": 0.05,
        }
        dims = {
            "storyFormat": story_format,
            "acFormat": ac_fmt,
            "acTestability": ac_test,
            "riskClassification": risk_c,
            "riskDescription": risk_d,
            "storySize": story_size,
            "businessValue": business,
            "nfrConsideration": nfr,
            "parentLink": parent_score,
            "dependencies": deps_score,
        }
        final = sum(weights[k] * dims[k] for k in weights)

        mandatory_zero = parent_score == 0 or risk_c == 0
        if risk_val in (1, 2) and risk_d == 0:
            mandatory_zero = True
        if story_format == 0 or ac_fmt == 0:
            mandatory_zero = True
        if not is_tech and story_format < 50:
            mandatory_zero = True

        issues = []
        if risk_c == 0:
            issues.append(
                "Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story)."
            )
        elif risk_val in (1, 2) and risk_d == 0:
            issues.append(
                "Risk is 1 or 2: add a meaningful Custom.Riskdescription (Risk description field) "
                "or extend description with clear risk/impact text."
            )
        if parent and not parent_ok:
            issues.append(f"Parent {parent} is not typed Feature/Epic in snapshot.")
        if not parent:
            issues.append("No System.Parent; story must link to Feature or Epic.")
        if not is_tech and story_format < 100:
            issues.append("Standard user story should use classic As a / I want / so that format.")
        if not is_tech and ac_fmt < 80:
            issues.append("Acceptance criteria should use explicit Gherkin (Given / When / Then).")
        if ac_test < 60:
            issues.append("Acceptance criteria may be vague or insufficiently testable.")

        compliant = "Compliant" if not mandatory_zero and final >= 72 else "Non-Compliant"

        stories_out.append(
            {
                "id": wid,
                "title": title,
                "type": story_type,
                "hasParentFeatureOrEpic": bool(parent_ok),
                "riskClassification": risk_val,
                "riskDescriptionPresent": len(plain_risk_desc) >= 8,
                "dimensions": dims,
                "finalScore": round(final, 1),
                "complianceStatus": compliant,
                "issues": issues,
                "rewriteSuggestions": {
                    "story": "",
                    "acceptanceCriteria": "",
                },
            }
        )

    if not stories_out and items:
        types = sorted({it.get("fields", {}).get("System.WorkItemType") for it in items} - {None})
        raise SystemExit(
            "No User Stories to score. Loaded work item types: " + (", ".join(types) if types else "none")
        )

    stories_out.sort(key=lambda s: s["id"])
    non_compliant = [s for s in stories_out if s["complianceStatus"] == "Non-Compliant"]
    avg = sum(s["finalScore"] for s in stories_out) / len(stories_out) if stories_out else 0

    scope: dict = {
        "team": args.scope_team or "Core-Process-platform",
        "iterationName": args.scope_iteration_name or "PP - 22 - 16.03.2026 - 03.04.2026",
        "iterationId": args.scope_iteration_id or "24c69368-31d8-4ecd-9316-2f6c46253853",
        "workItemTypes": ["User Story"],
        "storyCount": len(stories_out),
    }
    if args.ids:
        scope["filterWorkItemIds"] = sorted(set(args.ids))

    eval_notes = [
        "Automated heuristic scoring from System.Description, Microsoft.VSTS.Common.AcceptanceCriteria, System.Parent, "
        "Microsoft.VSTS.Common.Risk, and Custom.Riskdescription.",
        "Risk classification uses Microsoft.VSTS.Common.Risk (1–3). Risk description uses Custom.Riskdescription when risk is 1 or 2.",
    ]
    if args.fetch:
        eval_notes.insert(
            0,
            f"Work item fields loaded live from Azure DevOps ({args.organization}/{args.project}) via "
            "workitemsbatch API (not from local merge JSON). Requires PAT in env; see --help.",
        )
    elif args.batch_json:
        eval_notes.insert(
            0,
            f"Work item batch loaded from local file: {args.batch_json.as_posix()}.",
        )

    out = {
        "evaluatedAt": datetime.now(timezone.utc).isoformat(),
        "scope": scope,
        "evaluationNotes": eval_notes,
        "stories": stories_out,
        "aggregateSummary": {
            "count": len(stories_out),
            "avgFinalScore": round(avg, 1),
            "nonCompliantCount": len(non_compliant),
            "topSystemicIssues": [
                "Unset or invalid Microsoft.VSTS.Common.Risk; populate Risk (1–3) and Risk description when risk is 1–2.",
                "Many standard stories deviate from strict As a / I want / so that and Gherkin AC; see per-item issues.",
            ],
            "quickWins": [
                "Add Given/When/Then to Acceptance Criteria field for stories with bullets-only AC.",
                "Shorten or split very large descriptions that look like multi-sprint specs.",
            ],
        },
    }

    if args.output is not None:
        outp = args.output
    elif args.ids and len(set(args.ids)) == 1:
        outp = STORY_EVAL / f"story-eval-{args.ids[0]}.json"
    else:
        outp = STORY_EVAL / "story-eval.json"
    outp.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(outp)


if __name__ == "__main__":
    main()
