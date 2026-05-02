---
name: ado-bug-report-quality
description: Evaluates Azure DevOps Bug work items against Public 360° wiki bug procedures plus industry bug-reporting practice. Emits pass/fail gates, a 1–10 quality score from a defined rubric, and structured JSON. Use when reviewing bug quality, Definition of Ready for bugs, triage hygiene, or coaching reporters on repro/content before the skill is applied at scale.
---

# Azure DevOps bug report quality (Public 360° + best practice)

## Canonical wiki sources (primary)

Use these as **normative** for process language and field expectations:

- [Routine for customer bugs and assistance from R&D](https://wiki.software-innovation.com/wiki/Routine_for_customer_bugs_and_assistance_from_R%26D) — board usage, **English** title, **no customer names / personal data in title** (build log), **Area** `360\Support`, **Iteration** `360\Core` for the **customer bugs** board, **Repro Steps** detail, **Customer** section fields, **Customer_Severity**, optional **Impacted module**, **SLA**, hotfix pointer.
- [Handling of Customer Bugs](https://wiki.software-innovation.com/wiki/Handling_of_Customer_Bugs) — **Repro steps**: English, screenshots/logs; **Planning**: severity/priority; **Customer information** section.
- [Support Troubleshooting Guide](https://wiki.software-innovation.com/wiki/Support_Troubleshooting_Guide) — gather **exact repro**, **screenshots**, **errors**, **server logs** (on-prem); reproduce on standard/latest build before filing where applicable.
- [Registering Work Items in Azure DevOps](https://wiki.software-innovation.com/wiki/Registering_Work_Items_in_Azure_DevOps) — **Description/Repro**: steps + **expected vs actual**; **Area** from **Product teams** where that page applies; **Impacted module**; clarity (“no one is a brain-reader”).
- [Core-testing process](https://wiki.software-innovation.com/wiki/Core-testing_process) — **How to create a bug**: Repro Steps template (environment, credentials/role, preconditions, how to reproduce, expected, actual).
- [Release Management Process (Overview)](https://wiki.software-innovation.com/wiki/Release_Management_Process_%28Overview%29) — build log driven by **bug title**; title must stay **safe for external build log**.

**Scope note:** Some teams use **PnB** (or other) **Iteration** paths and **`360\support\Hotfix Request`** (or similar) **Area** children. Treat those as **compliant with local board policy** if the user states that; still evaluate **content quality** the same way. Call out **mismatches** only when the user asked for strict **customer bugs board** compliance.

## Secondary: product-development best practice

Apply when wiki is silent:

- **One problem per bug** (or explicitly scoped set of tightly related symptoms).
- **Minimal reproducible case** (smallest steps/data), not only narrative.
- **Observable actual** vs **expected** (even short bullets).
- **Environment identity** (tenant URL, farm, on-prem server role, or “standard test env X”) + **product version/build** when known.
- **Intermittency** called out if relevant (always vs sometimes; triggers).
- **Regressions**: “worked in version X, fails in Y” when known.
- **Privacy**: no unnecessary personal data in **title** or **public-facing** fields; keep customer identifiers in designated customer fields where your template provides them.

## MCP and safety

- Server: **`user-azure-devops`**. Read tool descriptors under `mcps/user-azure-devops/tools/` before calling.
- **Read-only** unless the user explicitly asks to update work items.
- **Never** call `wit_update_work_item` / batch update without explicit approval.
- Prefer **`wit_get_work_items_batch_by_ids`** with explicit **`fields`**; chunk IDs (e.g. **200** per batch) if large.
- If a **custom field** returns **TF51535**, drop it and continue; note **unknown** in output.

### Recommended fields (adjust if TF51535)

`System.Id`, `System.WorkItemType`, `System.State`, `System.Title`, `System.AreaPath`, `System.IterationPath`, `Microsoft.VSTS.Common.Priority`, `Microsoft.VSTS.Common.Severity`, `Microsoft.VSTS.TCM.ReproSteps`, `System.Description`, `Custom.Customername`, `Custom.ImpactedModule`, `Custom.CustomerVersion`

Add other org fields only after resolving reference names (e.g. via `wit_get_work_item_type` for `Bug`).

### Plain text for checks

Strip HTML tags when measuring length or searching phrases in **Repro Steps** / **Description**.

---

## Part A — Pass / fail gates

Emit **`gates`** with **`id`**, **`name`**, **`result`**: `pass` | `fail` | `na` | `unknown`, **`evidence`** (short quote or field name), **`remediation`** (one line).

### A1. Critical gates (wiki-aligned “minimum bar” for an actionable bug)

| ID | Rule | Fail when |
|----|------|-----------|
| `CG-TYPE` | Work item is a **Bug** | Type ≠ Bug (if user asked to evaluate bugs) |
| `CG-TITLE-NONEMPTY` | **Title** present and not placeholder | Title missing or trivial (“bug”, “fix”, “issue”) |
| `CG-TITLE-ENGLISH` | **Title** in **English** (wiki) | Clear non-English dominant title (heuristic; flag `unknown` if unsure) |
| `CG-TITLE-NO-CUSTOMER-PII` | **Title** has **no customer names** and no obvious **personal data** (build log rule) | Known municipality/customer strings or PII patterns in title (heuristic; prefer `unknown` over false pass) |
| `CG-REPRO-SUBSTANCE` | **Repro Steps** (+ **Description** if used) has enough substance to attempt reproduction | Stripped text **&lt; 200 characters** with no images that plausibly carry repro |
| `CG-NO-UNRESOLVED-NOT-REPRO` | Does **not** claim **cannot reproduce / not reproduced / no repro steps** as the **final** state without a clear **next action** (wiki: reproduce on latest build before board) | Phrases like “not reproduced”, “no repro steps”, “cannot reproduce” **and** no structured workaround (e.g. “blocked on: access to X”, “pending logs from customer”) — use judgment: **fail** if it reads as “closed content” |

### A2. Advisory checks (should fix; do not flip a separate “compliant” bit unless the user wants strict mode)

| ID | Rule | Advisory fail when |
|----|------|---------------------|
| `AD-AREA-SUPPORT` | **Area** under `360\support` (wiki default) | Area path does not start with intended support root |
| `AD-CUSTOMER-NAME` | **Customer name** custom field populated | Empty |
| `AD-CUSTOMER-VERSION` | **Customer version** populated when customer-specific | Empty and bug is clearly customer-specific |
| `AD-IMPACTED-MODULE` | **Impacted module** set when template exists | Empty |
| `AD-SEV-PRI` | **Severity** and **Priority** set | Either missing |
| `AD-EXPECTED-ACTUAL` | **Expected** and **actual** explicit (wiki + best practice) | Neither clearly present in repro/description |
| `AD-ENV-VERSION` | **Environment** + **product version** identifiable | Neither URL/tenant/farm/on-prem hint nor version/build string |
| `AD-EVIDENCE` | **Screenshot**, **log snippet**, or **exact error text** | None |

**`overall_critical`**: `pass` only if **all** A1 gates are `pass` or `na`.  
**`overall_advisory`**: counts of advisory passes/fails for coaching.

---

## Part B — Quality score (1–10)

### B1. Rubric matrix (weighted: repro + expected + actual matter most)

**Weighted points** (max **13**), then **normalize to 0–10** (round):  
`quality_score_raw = round(10 × weighted_sum / 13)`.

| # | Criterion | Max pts | Scoring |
|---|-----------|---------|---------|
| **Q2** | **Structured repro** | **2** | **2** = ordered/numbered repro (`<ol>`, multiple `<li>`, or explicit step list). **1** = some structure (bullets / step refs) or long clear sequence. **0** = weak / missing. |
| **Q6** | **Expected behavior** | **2** | **2** = explicit *expected* / *forventet* / normative *should* / *supposed to*. **1** = contrast implies expectation (e.g. correct vs incorrect, works vs does not). **0** = not discernible. |
| **Q7** | **Actual behavior** | **2** | **2** = explicit *actual* / *observed* / `BUG:` / *does not work*. **1** = clear failure description (*incorrect*, *cannot*, *not received*, *fails*, …). **0** = vague. |
| **Q1** | Title specificity | 1 | As before. |
| **Q3** | Preconditions / data | 1 | As before. |
| **Q4** | Environment | 1 | As before. |
| **Q5** | Version / build | 1 | As before. |
| **Q8** | Evidence | 1 | As before. |
| **Q9** | Classification | 1 | As before. |
| **Q10** | Single-focus clarity | 1 | As before. |

**Rationale:** Wiki and good practice treat **repro steps** and **expected vs actual** as the core of an actionable bug; they carry **~46%** of weighted points (6/13) vs **~30%** under flat 10×1.

Always list per-criterion results with **`points`** and **`max_points`** for auditability.

### B2. Score caps (honesty rules)

Apply **after** normalizing to **0–10**:

- If **`CG-NO-UNRESOLVED-NOT-REPRO`** is **fail** → **`quality_score_final`** = **`min(normalized_score, 3)`**, **`cap_reason`** = `unresolved_not_repro_content`.
- If **`CG-REPRO-SUBSTANCE`** is **fail** → **`quality_score_final`** = **`min(normalized_score, 2)`**, **`cap_reason`** = `insufficient_repro`; if both caps apply, use the **lower** score and concatenate reasons.

Report:

- **`quality_weighted_points`** / **`quality_weighted_max`** (13)
- **`quality_score_raw`** (0–10, normalized from weighted sum)
- **`quality_score_final`** (capped 0–10)
- **`scoring_model`**: e.g. `weighted_core_v2` (batch script)
- **`criteria`**: `{ "id", "points", "max_points", "note" }`

### B3. Optional labels (for dashboards)

Map **`quality_score_final`** to bands:

| Score | Label |
|-------|--------|
| 9–10 | **Strong** |
| 7–8 | **Good** |
| 5–6 | **Adequate** |
| 3–4 | **Weak** |
| 0–2 | **Insufficient** |

---

## Required JSON output shape

Emit **one** JSON object:

```json
{
  "evaluatedAt": "ISO-8601",
  "policy": {
    "wikiSources": ["urls..."],
    "notes": ["scope: customer-bugs board vs PnB if applicable"]
  },
  "workItems": [
    {
      "id": 0,
      "url": "https://tieto-si.visualstudio.com/360/_workitems/edit/0",
      "gates": {
        "critical": [{ "id": "CG-TYPE", "result": "pass|fail|na|unknown", "evidence": "", "remediation": "" }],
        "advisory": [{ "id": "AD-AREA-SUPPORT", "result": "pass|fail|na|unknown", "evidence": "", "remediation": "" }],
        "overall_critical": "pass|fail",
        "advisory_pass_count": 0,
        "advisory_fail_count": 0
      },
      "quality": {
        "scoring_model": "weighted_core_v2",
        "criteria": [{ "id": "Q2", "points": 0, "max_points": 2, "note": "" }],
        "quality_weighted_points": 0,
        "quality_weighted_max": 13,
        "quality_score_raw": 0,
        "quality_score_final": 0,
        "quality_label": "Strong|Good|Adequate|Weak|Insufficient",
        "cap_reason": null
      },
      "summary": "One paragraph coaching summary."
    }
  ]
}
```

---

## Evaluation steps

1. Confirm **project** (e.g. `360`) and **which bugs** (IDs, query, or backlog).
2. Fetch fields via MCP; build **stripped_text** from HTML fields.
3. Evaluate **Part A** gates with evidence quotes (short).
4. Score **Part B** criteria (0/1 each); compute **raw** and **capped** scores.
5. Write **`summary`**: top 2 fixes that would raise score fastest.
6. Do **not** modify Azure DevOps unless the user explicitly requests it.

---

## Markdown report builder

Repo script (stdlib only) turns evaluation JSON into a short **overview table** plus **per-item breakdown** (gates, advisory, Q1–Q10 notes, summary):

```bash
python build_bug_quality_report.py -i path/to/eval.json -o path/to/report.md
```

- Default output path: **`<input_stem>_report.md`** next to the JSON if `-o` is omitted.
- **Stdin:** `python build_bug_quality_report.py -i - < eval.json` writes to **stdout** unless `-o` is set.

Example inputs:

- `.cursor/skills/ado-bug-report-quality/examples/sample_eval.json` (minimal smoke test)
- `bug_quality_eval_2026-04-07.json` (repo root — full five-bug sample evaluation; regenerate report with `-o bug_quality_report_2026-04-07.md`)

### Saved query workflow (Azure DevOps)

1. Confirm **saved query id** (GUID from the query URL) and project **`360`**.
2. **`wit_get_query_results_by_id`** — `id`: query GUID, `project`: `360`, optional `top`, `responseType`: `ids` then hydrate with **`wit_get_work_items_batch_by_ids`** (chunk ≤ **200** ids), **or** one batch call if the set is small.
3. Save the batch JSON array (e.g. **`bug_quality_query_<guid>_wi.json`**) for audit/re-run.
4. **`evaluate_bug_quality_batch.py`** — heuristic evaluation matching this skill’s gates and Q1–Q10:

```bash
py -3 evaluate_bug_quality_batch.py -i bug_quality_query_<guid>_wi.json -o bug_quality_eval_query_<guid>.json \
  --query-id "<guid>" --query-url "https://tieto-si.visualstudio.com/360/_queries/query/<guid>/"
```

5. **`build_bug_quality_report.py`** — `-i` the eval JSON, `-o` the Markdown report.

**Note:** Automated scoring uses **heuristics** (HTML strip, keywords). Spot-check **`overall_critical`: `fail`** items and high-impact bugs manually.

## Related skills

- **`ado-user-story-quality`** — user stories, not bugs.
- **`ado-user-story-quality`** `story_eval/copilot-instructions.md` — parallel pattern for JSON-first evaluation.
