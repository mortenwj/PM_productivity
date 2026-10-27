# PAF pilot — weekly stakeholder report (spec)

Single reference for **how** we generate the combined consultant + customer update. This version runs **without** scanning Git for commits that lack Azure DevOps work items; that is a **planned separate experiment** using the stored repo map (`pilot_git_repo_mapping_from_ado.json`).

---

## Purpose

Under pilot time pressure, consultants and the customer still need a **predictable weekly view** of what changed in the solution: **what shipped**, **what moved**, and **what is in flight**.

---

## Cadence and time window

| Rule | Value |
|------|--------|
| Frequency | **Weekly** |
| Window | Rolling **last 14 days**, end = **when the report is generated** |
| Timezone | **Europe/Oslo** for interpreting calendar boundaries |

---

## Timestamps (inclusion in the 14-day window)

### Why not raw `System.ChangedDate` alone?

`System.ChangedDate` updates when **any** field changes—including **stack rank** (board ordering), bulk edits, or automation that do **not** reflect “real” product progress. That can flood the rolling window with **New** items that only moved on the backlog.

### Field rules (use in WIQL / queries)

| State category | Field | Rule |
|----------------|--------|------|
| **Closed** | `Microsoft.VSTS.Common.ClosedDate` | Include if Oslo-interpreted date falls in the window |
| **Resolved** (terminal “done” for your process, if distinct from Closed) | `Microsoft.VSTS.Common.ResolvedDate` | Same |
| **New** | `Microsoft.VSTS.Common.StateChangeDate` | Use **State change date**, not `System.ChangedDate`, for the window predicate. For items that stay **New**, rank and other non-state edits bump **ChangedDate** but typically **do not** change **StateChangeDate**, so the set better matches “state or meaningful backlog movement you care about.” (If the item was created as **New**, the initial transition still sets state-change history—align with how your process uses the field.) |
| **Active / In progress / other non-terminal (not New)** | `System.ChangedDate` *or* evaluate case-by-case | Default remains **Changed** for “touched this sprint,” knowing rank can still noise. If backlog hygiene is a problem for **Active** too, consider filtering on **StateChangeDate** when the question is “entered this state recently,” or combine with other signals in a later iteration. |

Use **one 14-day window**, but **split predicates by state** so **New** does not rely on `System.ChangedDate` for inclusion.

### Activity line in the generated Markdown

The report’s per-item “activity” line still prefers **Closed** → **Resolved** → **Changed** dates for display (see `projects/process-platform/pilot/tools/generate_pilot_weekly_report.py`). Optional hardening: when **`State` = New** and overlay batches include `Microsoft.VSTS.Common.StateChangeDate`, show that date instead of **ChangedDate** for readability consistent with the WIQL rule.

---

## Backlog scope

| Rule | Value |
|------|--------|
| Project | **360** |
| Epic roots (traverse `Hierarchy-Forward` only for discovery) | **414328**, **414727**, **411612** |
| Bugs off the hierarchy | Include **Bug** work items with **Area Path** = **`360\Core-Process-platform`** that pass the time rules |
| Related/Successor links | **Do not** traverse for expanding the set |
| Dedup | If an item appears both under an epic and via Area Path, **count once** |
| Audience filter | **None** — everything in scope |

---

## Report structure

1. **Top level:** group by **epic**, in this order: **411612** → **414727** → **414328**.
2. **Under each epic:** **Feature → User Story** (and Tasks only when they clarify delivery). No secondary Process/UI split **for now**.
3. **Orphan Bugs** (area path only, not under the three epics): section **Core-Process-platform** (or title: “Bugs — Core Process Platform”).
4. **One combined** document for consultants and customers.

---

## Content rules (per item)

| Topic | Rule |
|-------|------|
| Pattern | Keep **What it does** + short outcome-focused text (**hide** PR links, merge state, repo names from the **published** weekly note). |
| Bugs | **Symptom + fix** in plain language (or planned fix if not done). |
| Internals | Traceability gaps are **not** surfaced to the customer-facing weekly text (still resolve internally in ADO/Git). |
| Disclaimer | **Yes** — short “draft / not signed-off release communication” line at the top. |

Internal drafts used for authoring may still use Development links; the **weekly** file is sanitized per above.

---

## Delivery (format and storage)

| Topic | Rule |
|-------|------|
| Markdown | **Yes** — canonical source in repo: `pilot_weekly_report_YYYY-MM-DD.md` (Oslo **date** when generated) |
| PDF | **Optional** — generate from Markdown when needed (e.g. `export_md_to_pdf.py`) |
| Distribution | **Manual** for now (email / Teams); files **stay in repo** as history |

---

## Engineering support data (not part of the weekly narrative)

| Artifact | Purpose |
|----------|--------|
| `pilot_git_repo_mapping_from_ado.json` | Repos and PRs inferred from **Development** links on scoped work items. **Update** when you refresh the report from ADO. Used later to experiment with **commits without linked work items** (separate job; compare repo commit SHAs in the same window to AB# coverage). |

---

## Out of scope for this report run

- **No** Git-wide scan for commits missing AB# or missing DevOps links.
- **No** automatic enforcement that every PR has a user story (tracked as a **future** pipeline using the JSON map + Git API).

---

## Related files

- `projects/process-platform/pilot/tools/pilot_weekly_wiql_reference.md` — example **WIQL** split so **New** uses `Microsoft.VSTS.Common.StateChangeDate` instead of `System.ChangedDate` (stack rank / spurious updates).
- `experiment_release_notes_epics_414328_414727_411612_2026-03_04.md` — earlier experiment with full engineering appendix (different date rules).
- `export_md_to_pdf.py` — optional PDF export.
