---
name: paf-pilot-release-notes
description: >-
  Generates the PAF pilot weekly stakeholder update (release-notes style Markdown)
  from Azure DevOps WIQL, MCP batches, and tools/generate_pilot_weekly_report.py.
  Covers the rolling 14-day rules (StateChangeDate for New), four-epic ordering
  including Core Platform last, Bug slice, parent closure, and overlay fields.
  Use when refreshing or authoring "PAF pilot release notes", pilot weekly report,
  stakeholder update for Process Platform / Core-Process-platform, or when aligning
  WIQL with PAF_pilot_weekly_report_SPEC.md.
---

# PAF pilot release notes (weekly stakeholder update)

This skill pins the **intended workflow and report shape** for the pilot “release notes” weekly note. Canonical product rules live in **`PAF_pilot_weekly_report_SPEC.md`** (repo root).

## Output

- **File:** `pilot_weekly_report_YYYY-MM-DD.md` (Oslo **calendar date** when generated).
- **Generator:** `tools/generate_pilot_weekly_report.py` writes that file; `report_date` is set inside the script (adjust when generating a new week).
- **Audience:** Combined consultant + customer draft; sanitize PR/repo identifiers from the published weekly text (see spec).

## Time window and WIQL (inclusion rules)

- **Window:** Rolling **14 days** (`@Today - 14` in WIQL); org query timezone applies; spec mentions **Europe/Oslo** for strict calendar parity as a future hardening pass.
- **Why not `System.ChangedDate` alone for New:** Stack rank and other churn bump **Changed** without meaningful progress. For **State = New**, WIQL should use **`Microsoft.VSTS.Common.StateChangeDate`**, not `System.ChangedDate`, for the time predicate (see spec + `tools/pilot_weekly_wiql_reference.md`).
- **Scope:** Project **360**; **Area Path** **`360\Core-Process-platform`**; split queries: **non-Bug** and **Bug** (same date logic per state category).

Store dated WIQL snapshots next to the run, e.g. `tools/pilot_weekly_nonbug_wiql_asof_YYYY-MM-DD.txt` and `tools/pilot_weekly_bug_wiql_asof_YYYY-MM-DD.txt`, and refresh them when predicates change.

## MCP (Azure DevOps)

- **Server:** `user-azure-devops` (read descriptors under `mcps/user-azure-devops/tools/` before calling).
- **`wit_query_by_wiql`:** Pass **`project`** `360` and a high **`top`** (e.g. **10000**). The tool descriptor default for `top` is low; without an explicit `top`, results can truncate (e.g. first 50 only).
- **`wit_get_work_items_batch_by_ids`:** **`project`** `360`, **`ids`** in chunks (≤**200** per REST batch). Request fields needed for the report, including at minimum:
  - **Core:** `System.Id`, `System.WorkItemType`, `System.State`, `System.Title`, `System.Parent`, `System.ChangedDate`, `Microsoft.VSTS.Common.ResolvedDate`, `Microsoft.VSTS.Common.ClosedDate`, `Microsoft.VSTS.Common.StateChangeDate`
  - **Narrative:** `System.Description`, `Microsoft.VSTS.Common.AcceptanceCriteria` (for overlay / *What it does* / bugs)

## Data flow (refresh → generate)

1. Run **non-Bug** WIQL → list of IDs; run **Bug** WIQL → list of IDs.
2. **`wit_get_work_items_batch_by_ids`** for non-Bug IDs → **`tools/pilot_weekly_batch1.json`** (array of `{id, fields, ...}` as returned by MCP). Keep **`tools/pilot_weekly_batch2.json`** as an empty JSON array `[]` unless you deliberately split batches.
3. **`wit_get_work_items_batch_by_ids`** for Bug IDs → **`tools/pilot_weekly_bugs_batch.json`**.
4. **Parent closure:** Walk `System.Parent` for all items in those exports; **`wit_get`** any ancestor IDs not already loaded until parents reach a **target epic** (**411612**, **414727**, **414328**, **411614**), program epic **414623**, or a root with no parent. Persist minimal rows in **`tools/pilot_weekly_parents_level1.json`** (same shape as historical exports: `id` + `fields` with at least `System.Id`, `System.WorkItemType`, `System.Parent`, `System.Title`).
5. **Overlay (optional but recommended):** Same in-scope IDs with `System.Description`, `Microsoft.VSTS.Common.AcceptanceCriteria`, and `Microsoft.VSTS.Common.StateChangeDate` merged by id → **`tools/pilot_weekly_descriptions_overlay.json`** (generator merges into main + bug maps).
6. **Stakeholder one-liners (optional):** **`tools/pilot_weekly_what_it_does_summaries.json`** — keyed by work item id as string; overrides synthesized “What it does” / bug symptom lines when present.
7. Record query metadata if useful → **`tools/pilot_weekly_query_meta.json`** (e.g. `as_of_utc`, counts).
8. Run: **`py -3 tools/generate_pilot_weekly_report.py`** → updates **`pilot_weekly_report_<report_date>.md`**.

### Alternative: PAT + REST

If MCP is unavailable, use **`tools/refresh_pilot_weekly_from_ado.py`** with **`AZURE_DEVOPS_PAT`** or **`ADO_PAT`** (Work Items Read). It writes the same batch/overlay/meta files when credentials are set.

Manual assembly helpers (if present in repo): **`tools/assemble_pilot_parents_and_overlay.py`** — align with the generator’s expected JSON shapes.

## Report structure (this version)

Sections are generated in this order:

1. Title, Oslo/ADO notes, disclaimer, **Scope**
2. **Epic sections (fixed order, last = Core Platform):**
   - **411612** — PAF – NVE Pilot  
   - **414727** — PAF – User Experience (UX)  
   - **414328** — PAF – Standard Artifacts  
   - **411614** — PAF – Core Platform  
   Within each epic: group by **`### Parent {id}`** (feature or parent work item id), then items sorted by id.
3. **Bugs** — `360\Core-Process-platform` from the Bug WIQL batch; dedupe IDs already listed in the non-Bug export.

**There is no “Other Core Process Platform activity” section** in this version: work items that **do not** roll up to one of the **four** epics above under `root_epic` walking are **omitted** from the Markdown (scope text states this). Program epic **414623** is used only as a walk terminator, not as a report section.

**Epics constant** in code: `TARGET_EPICS` in `tools/generate_pilot_weekly_report.py`. **NVE process-rich stories:** parent feature **413948** — extra *Process description* line from long HTML templates when applicable.

## Regenerating after edits

- Change **`report_date`** in `generate_pilot_weekly_report.py` when targeting a new weekly filename.
- Re-run **`py -3 tools/generate_pilot_weekly_report.py`** after any change to batch JSON, parents, overlay, summaries, or generator logic.

## Related repo files

| File | Role |
|------|------|
| `PAF_pilot_weekly_report_SPEC.md` | Spec: cadence, timestamps, scope |
| `tools/pilot_weekly_wiql_reference.md` | WIQL notes / examples |
| `tools/generate_pilot_weekly_report.py` | Markdown generator (single source of truth for epic list and structure) |
| `tools/pilot_weekly_*.json` | Batch exports, overlay, summaries, meta |

---

**Skill version note:** This skill reflects the **four-epic** layout (**411614** last), **no Other section**, and **StateChangeDate**-aware WIQL described above. If the spec or generator diverges, update this skill when you intentionally change the workflow.
