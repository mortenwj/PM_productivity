#!/usr/bin/env python3
"""
Evaluate Azure DevOps Bug work items (batch JSON) per .cursor/skills/ado-bug-report-quality/SKILL.md.
Output: evaluation JSON for build_bug_quality_report.py.

Weighted rubric (weighted_core_v2): Q2 repro, Q6 expected, Q7 actual = 0–2 each;
Q1, Q3–Q5, Q8–Q10 = 0–1; max 13 points → normalized 0–10.

  py -3 evaluate_bug_quality_batch.py -i workitems.json -o eval.json
  py -3 evaluate_bug_quality_batch.py -i workitems.json --query-id UUID --query-url URL -o eval.json
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

WIKI_SOURCES = [
    "https://wiki.software-innovation.com/wiki/Routine_for_customer_bugs_and_assistance_from_R%26D",
    "https://wiki.software-innovation.com/wiki/Handling_of_Customer_Bugs",
    "https://wiki.software-innovation.com/wiki/Support_Troubleshooting_Guide",
    "https://wiki.software-innovation.com/wiki/Registering_Work_Items_in_Azure_DevOps",
    "https://wiki.software-innovation.com/wiki/Core-testing_process",
    "https://wiki.software-innovation.com/wiki/Release_Management_Process_%28Overview%29",
]

GENERIC_TITLES = frozenset({"bug", "issue", "fix", "error", "test", "problem"})


def strip_html(html: str | None) -> str:
    if not html:
        return ""
    t = re.sub(r"(?is)<script.*?>.*?</script>", " ", str(html))
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def fields_from_wi(wi: dict[str, Any]) -> dict[str, Any]:
    return wi.get("fields") or {}


def combined_text(f: dict[str, Any]) -> str:
    r = strip_html(f.get("Microsoft.VSTS.TCM.ReproSteps"))
    d = strip_html(f.get("System.Description"))
    return f"{r} {d}".strip()


WEIGHTED_MAX = 13  # Q2,Q6,Q7 max 2 each; Q1,Q3,Q4,Q5,Q8,Q9,Q10 max 1 each


def label_from_score(n: int) -> str:
    if n >= 9:
        return "Strong"
    if n >= 7:
        return "Good"
    if n >= 5:
        return "Adequate"
    if n >= 3:
        return "Weak"
    return "Insufficient"


def _score_q2(repro_l: str, text: str, text_l: str) -> tuple[int, str]:
    """Structured repro: 0–2 (core triad — highest weight with Q6/Q7)."""
    li_count = repro_l.count("<li")
    if "<ol" in repro_l or re.search(r"\brepro steps?:", text_l):
        if li_count >= 2 or re.search(r"\b1[\.)]\s", text_l):
            return 2, "Numbered/ordered repro (ol or explicit steps)."
    if li_count >= 4:
        return 2, "Many bullet steps in Repro Steps."
    if li_count >= 1 or re.search(r"\bstep\s*\d", text_l):
        return 1, "Some structure (bullets or step refs)."
    if len(text) > 500 and text.count(".") >= 4:
        return 1, "Long sequential narrative."
    return 0, "Add numbered/bulleted repro steps."


def _score_q6(text_l: str) -> tuple[int, str]:
    """Expected behavior: 0–2."""
    if re.search(r"\bexpected\b", text_l) or "forventet" in text_l:
        return 2, "Explicit expected / forventet."
    if re.search(r"\bshould\b", text_l) or "supposed to" in text_l:
        return 2, "Normative should / supposed to."
    if ("correct" in text_l and ("incorrect" in text_l or "wrong" in text_l)) or (
        "works" in text_l and "does not" in text_l
    ):
        return 1, "Contrast implies expected (correct vs incorrect / works vs not)."
    return 0, "State explicit expected result."


def _score_q7(text_l: str) -> tuple[int, str]:
    """Actual behavior: 0–2."""
    if re.search(r"\bactual\b", text_l) or "observed" in text_l or "bug:" in text_l:
        return 2, "Explicit actual / observed / BUG:."
    if "does not work" in text_l:
        return 2, "Clear failure wording."
    if (
        "incorrect" in text_l
        or "not working" in text_l
        or "fails" in text_l
        or "not received" in text_l
        or "unable to" in text_l
        or "cannot " in text_l
        or "not able" in text_l
    ):
        return 1, "Failure described (weaker than labeled Actual/BUG)."
    return 0, "State what actually happens vs expected."


def weighted_to_10(weighted: int) -> int:
    return int(round(10 * weighted / WEIGHTED_MAX))


def gate(
    gid: str,
    ok: bool,
    evidence: str,
    remediation: str | None = None,
) -> dict[str, Any]:
    return {
        "id": gid,
        "result": "pass" if ok else "fail",
        "evidence": evidence[:500],
        "remediation": remediation,
    }


def evaluate_item(wi: dict[str, Any]) -> dict[str, Any]:
    f = fields_from_wi(wi)
    wid = f.get("System.Id") or wi.get("id")
    url = wi.get("url") or f"https://tieto-si.visualstudio.com/360/_workitems/edit/{wid}"
    title = (f.get("System.Title") or "").strip()
    area = f.get("System.AreaPath") or ""
    repro_html = f.get("Microsoft.VSTS.TCM.ReproSteps") or ""
    text = combined_text(f)
    text_l = text.lower()
    repro_l = repro_html.lower()

    # --- Critical gates
    cg_type = f.get("System.WorkItemType") == "Bug"
    cg_nonempty = len(title) >= 8 and title.lower() not in GENERIC_TITLES
    non_ascii = sum(1 for c in title if ord(c) > 127 and not c.isdigit())
    cg_english = len(title) == 0 or (non_ascii / max(len(title), 1)) < 0.35
    tl = title.lower()
    cg_no_pii = not any(
        x in tl
        for x in (
            "kommune",
            "lillestrøm",
            "bergen kommune",
            "oslo kommune",
            "oslo,",
            "customer:",
        )
    )
    cg_substance = len(text) >= 200 or ("img src" in repro_l) or ("_apis/wit/attachments" in repro_l)

    not_repro_triggers = (
        "not reproduced",
        "no repro steps",
        "cannot reproduce",
        "can not reproduce",
        "unable to reproduce",
    )
    has_not_repro = any(t in text_l for t in not_repro_triggers)
    excuses = (
        "blocked",
        "waiting for",
        "pending",
        "need access",
        "customer to provide",
        "cannot access",
        "lack of",
        "awaiting",
    )
    cg_not_repro_ok = (not has_not_repro) or any(e in text_l for e in excuses)

    critical = [
        gate("CG-TYPE", cg_type, f.get("System.WorkItemType", ""), "Use Bug type."),
        gate("CG-TITLE-NONEMPTY", cg_nonempty, title[:80], "Add specific title."),
        gate("CG-TITLE-ENGLISH", cg_english, title[:80], "Use English title per wiki."),
        gate("CG-TITLE-NO-CUSTOMER-PII", cg_no_pii, title[:80], "Remove customer/PII from title."),
        gate("CG-REPRO-SUBSTANCE", cg_substance, f"stripped_len={len(text)}", "Add repro steps, screenshots, or logs."),
        gate(
            "CG-NO-UNRESOLVED-NOT-REPRO",
            cg_not_repro_ok,
            "not_repro_phrase" if has_not_repro else "ok",
            "Resolve not-repro vs reproducible contradiction per wiki.",
        ),
    ]
    overall_ok = all(g["result"] == "pass" for g in critical)

    cust = (f.get("Custom.Customername") or "").strip()
    cv = (f.get("Custom.CustomerVersion") or "").strip()
    im = (f.get("Custom.ImpactedModule") or "").strip()
    sev = f.get("Microsoft.VSTS.Common.Severity")
    pri = f.get("Microsoft.VSTS.Common.Priority")

    advisory = [
        gate("AD-AREA-SUPPORT", area.lower().startswith(r"360\support"), area, None),
        gate("AD-CUSTOMER-NAME", bool(cust), cust[:60] or "(empty)", "Fill customer name."),
        gate(
            "AD-CUSTOMER-VERSION",
            bool(cv),
            cv or "(empty)",
            "Set customer version / build.",
        ),
        gate("AD-IMPACTED-MODULE", bool(im), im or "(empty)", "Set Impacted module."),
        gate("AD-SEV-PRI", sev is not None and pri is not None, f"{sev!s} / {pri!s}", "Set severity and priority."),
        gate(
            "AD-EXPECTED-ACTUAL",
            (
                ("expected" in text_l or "should " in text_l or "forventet" in text_l)
                or ("actual" in text_l or "bug:" in text_l or "observed" in text_l)
                or ("does not" in text_l or "not working" in text_l or "incorrect" in text_l)
            ),
            "expected/actual heuristic",
            "Add explicit Expected vs Actual.",
        ),
        gate(
            "AD-ENV-VERSION",
            ("http" in text_l or ".public360" in text_l or "tenant" in text_l)
            or ("http" in cust.lower() if cust else False)
            or bool(cv),
            "env+version",
            "Add environment URL and version.",
        ),
        gate(
            "AD-EVIDENCE",
            ("img src" in repro_l)
            or ("attachment" in repro_l)
            or ("error" in text_l)
            or ("exception" in text_l),
            "screenshot/log",
            "Add screenshot, log, or exact error text.",
        ),
    ]
    ap = sum(1 for g in advisory if g["result"] == "pass")
    af = sum(1 for g in advisory if g["result"] == "fail")

    # --- Q1–Q10: Q2, Q6, Q7 are 0–2 (repro + expected + actual core); others 0–1
    q1 = 1 if len(title) > 20 or (len(title) > 12 and title.lower() not in GENERIC_TITLES) else 0
    q2, note2 = _score_q2(repro_l, text, text_l)
    q3 = 1 if any(k in text_l for k in ("prerequisite", "precondition", "configuration", "setup", "feature flag")) else 0
    q4 = 1 if ("http" in text_l or ".public360" in text_l or "tenant" in text_l or "environment" in text_l) else 0
    if cust and "http" in cust.lower():
        q4 = 1
    q5 = 1 if cv or re.search(r"\b[56]\.\d", text_l) or ("build" in text_l and re.search(r"\d", text_l)) else 0
    q6, note6 = _score_q6(text_l)
    q7, note7 = _score_q7(text_l)
    q8 = 1 if ("img src" in repro_l) or ("attachment" in repro_l) or ("error" in text_l) else 0
    q9 = 1 if sev and pri is not None and im else 0
    q10 = 1
    if re.search(r"\b(issue|problem)\s*[123]\b", text_l) or "innmeldt problemstilling 2" in text_l:
        q10 = 0

    criteria_defs: list[tuple[str, int, int, str]] = [
        ("Q1", q1, 1, "Title specificity"),
        ("Q2", q2, 2, note2),
        ("Q3", q3, 1, "Preconditions / data"),
        ("Q4", q4, 1, "Environment"),
        ("Q5", q5, 1, "Version / build"),
        ("Q6", q6, 2, note6),
        ("Q7", q7, 2, note7),
        ("Q8", q8, 1, "Evidence"),
        ("Q9", q9, 1, "Classification (sev/pri + module)"),
        ("Q10", q10, 1, "Single-focus clarity"),
    ]
    criteria = [
        {"id": cid, "points": min(pts, mx), "max_points": mx, "note": note} for cid, pts, mx, note in criteria_defs
    ]
    weighted = sum(c["points"] for c in criteria)
    raw_10 = weighted_to_10(weighted)
    cap_reason = None
    final = raw_10
    if not cg_not_repro_ok:
        final = min(final, 3)
        cap_reason = "unresolved_not_repro_content"
    if not cg_substance:
        final = min(final, 2)
        cap_reason = (
            "insufficient_repro"
            if cap_reason is None
            else f"{cap_reason}; insufficient_repro"
        )

    gaps = []
    if not cv:
        gaps.append("CustomerVersion")
    if not im:
        gaps.append("ImpactedModule")
    if q4 == 0:
        gaps.append("environment URL")
    if q6 < 2:
        gaps.append("clearer Expected")
    if q7 < 2:
        gaps.append("clearer Actual")
    if q2 < 2:
        gaps.append("stronger repro steps")
    summary = f"Critical: {'PASS' if overall_ok else 'FAIL'}. "
    if gaps:
        summary += "Improve: " + ", ".join(gaps) + "."
    else:
        summary += "Solid field hygiene; refine narrative if score < 9."

    return {
        "id": wid,
        "url": url,
        "gates": {
            "critical": critical,
            "advisory": advisory,
            "overall_critical": "pass" if overall_ok else "fail",
            "advisory_pass_count": ap,
            "advisory_fail_count": af,
        },
        "quality": {
            "criteria": criteria,
            "scoring_model": "weighted_core_v2",
            "quality_weighted_points": weighted,
            "quality_weighted_max": WEIGHTED_MAX,
            "quality_score_raw": raw_10,
            "quality_score_final": final,
            "quality_label": label_from_score(final),
            "cap_reason": cap_reason,
        },
        "summary": summary,
    }


def main() -> int:
    p = argparse.ArgumentParser(description="Evaluate bug quality from ADO batch JSON.")
    p.add_argument("-i", "--input", required=True, help="JSON array of work items (wit_get_work_items_batch_by_ids)")
    p.add_argument("-o", "--output", required=True, help="Output evaluation JSON path")
    p.add_argument("--query-id", default="", help="Saved query GUID for report metadata")
    p.add_argument("--query-url", default="", help="Saved query URL for report metadata")
    args = p.parse_args()

    raw = Path(args.input).read_text(encoding="utf-8")
    items = json.loads(raw)
    if not isinstance(items, list):
        raise SystemExit("Input must be a JSON array of work items")

    notes = [
        "Automated heuristic evaluation; spot-check critical items.",
        "PnB iterations and Hotfix Request area allowed per local board policy.",
        "Scoring weighted_core_v2: Q2 (repro), Q6 (expected), Q7 (actual) = 0–2 pts each; Q1, Q3–Q5, Q8–Q10 = 0–1; max 13 → normalized 0–10.",
    ]
    if args.query_id:
        notes.append(f"Source query id: {args.query_id}")
    if args.query_url:
        notes.append(f"Source query: {args.query_url}")

    out = {
        "evaluatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "policy": {"wikiSources": list(WIKI_SOURCES), "notes": notes},
        "workItems": [evaluate_item(wi) for wi in items],
    }

    outp = Path(args.output)
    outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(out['workItems'])} items -> {outp.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
