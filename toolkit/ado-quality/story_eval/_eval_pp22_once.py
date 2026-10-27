"""One-off: merge two MCP batch files + parent batch, score User Stories (policy heuristic)."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from html import unescape
from pathlib import Path

STORY_EVAL = Path(__file__).resolve().parent

# MCP output may land under a sibling Cursor project folder; try several roots.
def _find_agent_batches() -> list[Path]:
    names = (
        "563fde59-90a4-4c9d-87f3-bc197bd6b458.txt",
        "0a4a10d6-31bf-4f7e-ae3b-e1d4a916ba3c.txt",
    )
    roots = [
        STORY_EVAL.parent.parent / "agent-tools",
        Path(r"C:\Users\jensemor\.cursor\projects\c-Users-jensemor-cursor-projects-PM-productivity-PM-productivity\agent-tools"),
    ]
    out = []
    for n in names:
        for r in roots:
            p = r / n
            if p.exists():
                out.append(p)
                break
    return out


def strip_html(html: str | None) -> str:
    if not html:
        return ""
    t = re.sub(r"<[^>]+>", " ", html)
    return unescape(re.sub(r"\s+", " ", t)).strip()


def main() -> None:
    paths = _find_agent_batches()
    items: list = []
    for p in paths:
        items.extend(json.loads(p.read_text(encoding="utf-8")))
    if not items:
        raise SystemExit("No batch files found")

    parents_raw = [
        {"id": 228634, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 230801, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 273420, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 276815, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 344868, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 348439, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 373512, "fields": {"System.WorkItemType": "Epic"}},
        {"id": 381967, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 391561, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 397370, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 399007, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 399190, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 400785, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 400794, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 402354, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 406819, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 410828, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 412681, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 414351, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 414353, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 414516, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 414600, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 414750, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 414994, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 415983, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 415986, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 415991, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 415993, "fields": {"System.WorkItemType": "Feature"}},
        {"id": 415996, "fields": {"System.WorkItemType": "Feature"}},
    ]
    parent_types: dict[int, str] = {
        x["id"]: x["fields"]["System.WorkItemType"] for x in parents_raw
    }

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
        # Batches must request: Microsoft.VSTS.Common.Risk, Custom.Riskdescription

        plain_d = strip_html(desc_raw).lower()
        plain_ac = strip_html(ac_raw).lower()
        combined = plain_d + " " + plain_ac

        is_tech = title.strip().lower().startswith("[tech]") or title.strip().lower().startswith(
            "[enabler]"
        )
        story_type = (
            "Tech"
            if title.strip().lower().startswith("[tech]")
            else (
                "Enabler"
                if title.strip().lower().startswith("[enabler]")
                else "User Story"
            )
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

        risk_raw = f.get("Microsoft.VSTS.Common.Risk")
        try:
            risk_val = int(risk_raw) if risk_raw is not None and risk_raw != "" else None
        except (TypeError, ValueError):
            risk_val = None
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
                "Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (re-fetch batch with Risk + Risk description fields)."
            )
        elif risk_val in (1, 2) and risk_d == 0:
            issues.append(
                "Risk is 1 or 2: populate Custom.Riskdescription with clear risk/impact text."
            )
        if parent and not parent_ok:
            issues.append(f"Parent {parent} is not typed Feature/Epic.")
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
                "rewriteSuggestions": {"story": "", "acceptanceCriteria": ""},
            }
        )

    stories_out.sort(key=lambda s: s["id"])
    non_compliant = [s for s in stories_out if s["complianceStatus"] == "Non-Compliant"]
    avg = sum(s["finalScore"] for s in stories_out) / len(stories_out) if stories_out else 0

    out = {
        "evaluatedAt": datetime.now(timezone.utc).isoformat(),
        "scope": {
            "team": "Core-Process-platform",
            "iterationName": "PP - 22 - 16.03.2026 - 03.04.2026",
            "iterationId": "24c69368-31d8-4ecd-9316-2f6c46253853",
            "project": "360",
            "workItemTypes": ["User Story"],
            "storyCount": len(stories_out),
        },
        "evaluationNotes": [
            "Heuristic scoring from Description, AcceptanceCriteria, Parent, Microsoft.VSTS.Common.Risk, Custom.Riskdescription.",
            "Parent Feature/Epic types confirmed via wit_get_work_items_batch_by_ids on 29 parent IDs.",
            "Re-run MCP batch with fields including Microsoft.VSTS.Common.Risk and Custom.Riskdescription for accurate risk scoring.",
        ],
        "stories": stories_out,
        "aggregateSummary": {
            "count": len(stories_out),
            "avgFinalScore": round(avg, 1),
            "nonCompliantCount": len(non_compliant),
            "topSystemicIssues": [
                "Populate Microsoft.VSTS.Common.Risk (1–3) and Risk description when risk is 1–2.",
                "Many standard stories lack strict As a / I want / so that and Gherkin AC.",
            ],
            "quickWins": [
                "Add Given/When/Then in Acceptance Criteria field.",
                "Set Risk field and Custom.Riskdescription where required.",
            ],
        },
    }

    outp = STORY_EVAL / "story-eval-pp22.json"
    outp.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(outp)
    print("stories", len(stories_out), "non_compliant", len(non_compliant), "avg", round(avg, 1))


if __name__ == "__main__":
    main()
