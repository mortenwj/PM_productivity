# Core-Process-platform: Sprint Analysis (Last 6 Sprints)

**Team:** Core-Process-platform  
**Project:** 360  
**Sprints analyzed:** PP-16 through PP-21 (Nov 2025 – Mar 2026)  
**Generated:** 2026-03-20  

---

## Executive Summary

This report analyzes the last 6 sprints of the Core-Process-platform team using Azure DevOps data. It covers sprint completion, scope changes, and industry benchmark comparison. **Retrospectives** are stored in Azure DevOps under the Process Platform team via the [Retrospectives extension](https://marketplace.visualstudio.com/items?itemName=ms-devlabs.team-retrospectives) (Boards → Retrospectives).

---

## 1. Sprint Overview

| Sprint | Dates | Root Work Items | Notes |
|--------|-------|-----------------|-------|
| PP-16 | 10.11 – 28.11.2025 | 94 | Largest backlog |
| PP-17 | 01.12 – 19.12.2025 | 64 | Holiday period |
| PP-18 | 22.12 – 09.01.2026 | 40 | Year-end / New Year |
| PP-19 | 12.01 – 30.01.2026 | 54 | Post-holiday ramp-up |
| PP-20 | 02.02 – 20.02.2026 | 59 | — |
| PP-21 | 23.02 – 13.03.2026 | 54 | Most recent |

*Root work items = Features, User Stories, Bugs at the top level of the sprint backlog (excluding child tasks).*

---

## 2. Completion Rate Analysis

### PP-16 Sample (48 root items fetched)

| State | Count | % |
|-------|-------|---|
| **Closed** | 47 | **97.9%** |
| New | 1 | 2.1% |

**Finding:** PP-16 had a very high completion rate (~98% of sampled items closed). One item (402882 – Admin Historical view responsive) remained in New.

### Interpretation

- **Strong completion:** The team is closing most committed work.
- **Scope size:** 94 root items in PP-16 is large; industry guidance is typically 5–15 user stories per 2-week sprint for a team of 5–9.
- **Backlog mix:** Many items are Bugs and smaller User Stories, which can inflate counts compared to “story point”–based planning.

---

## 3. Scope Changes: Transferred & Added

### Data Limitation

Azure DevOps does not expose “transferred” or “added mid-sprint” as first-class metrics. To compute these accurately you would need:

1. **Iteration path change history** – when items moved from one sprint to another.
2. **Creation date vs sprint dates** – items created after sprint start = “added”.
3. **Work item revision history** – `wit_list_work_item_revisions` can provide this per item.

### What We Can Infer

- **Carry-over:** Items that appear in both PP-N and PP-N+1 (e.g. 399192, 402363, 401047, 403108, 402963, 402882, 399495, 397790) indicate work spanning multiple sprints.
- **High overlap:** Several items (e.g. 399192, 402363, 401047) appear in multiple sprints, suggesting either:
  - Large epics broken across sprints, or
  - Items carried over due to capacity or priority changes.

### Recommendation

To track “transferred” and “added” systematically:

1. Create a saved query: *Items in [Sprint N] where Iteration Path was changed during sprint*.
2. Use `wit_list_work_item_revisions` for key items to detect iteration path changes.
3. Add a custom field or tag (e.g. “Added mid-sprint”) if you want explicit tracking.

---

## 4. Industry Best Practice Comparison

| Metric | Industry Benchmark | Process Platform | Assessment |
|--------|--------------------|------------------|------------|
| **Sprint completion rate** | 80–95% | ~95–98% (PP-16 sample) | ✅ Above target |
| **Scope stability** | &lt;10% added mid-sprint | Not measured | ⚠️ Needs tracking |
| **Carry-over rate** | &lt;20% of sprint scope | Overlap observed | ⚠️ Review capacity |
| **Sprint length** | 2 weeks typical | ~3 weeks (19 days) | ℹ️ Longer cadence |
| **Backlog size** | 5–15 stories/sprint | 40–94 items | ⚠️ Very large scope |
| **Definition of Done** | Consistent | Implied by Closed state | ℹ️ Document explicitly |

### Observations

1. **Completion:** The team closes work effectively; completion rate is strong.
2. **Scope size:** 40–94 root items per sprint is high. Consider:
   - Focusing on fewer, higher-value items.
   - Using story points or capacity-based planning.
   - Splitting large epics into smaller, shippable increments.
3. **Sprint length:** ~3-week sprints are acceptable but differ from common 2-week practice.
4. **Carry-over:** Recurring items across sprints suggest either large epics or capacity/priority shifts. Worth reviewing in retro.

---

## 5. Retrospective Data

### Where Retros Are Stored

**Retrospectives are stored in Azure DevOps** under the Core-Process-platform team, using the Microsoft Retrospectives extension:

- **Location:** Boards → Retrospectives (select team: Core-Process-platform)
- **Direct link:** `https://tieto-si.visualstudio.com/360/_boards/board/t/Core-Process-platform/Retrospectives`
- **Extension:** [Team Retrospectives](https://marketplace.visualstudio.com/items?itemName=ms-devlabs.team-retrospectives)

The extension stores retro boards, feedback items, and team assessments in its own data store. Action items created from retros ("Add action item") become Azure DevOps work items (User Stories, Bugs, etc.) and are linked to the feedback.

### API Limitation

The retro board content (feedback cards, columns, votes) is **not exposed via the Work Item Tracking REST API**. The extension uses the Extension Management/Data API, which is separate from the standard work item APIs. To include retro summaries in this analysis:

1. **Manual export:** Use the extension's "Create summary" or "Copy retrospective link" to capture key points.
2. **Action items:** Work items created from retro feedback can be found via links; consider tagging them (e.g. `Retro-Action`) for querying.
3. **History view:** The extension's History tab shows past retros with feedback counts and linked work items.

### Recurring Issues to Look For

From sprint patterns and common agile issues, consider checking retros for:

- **Scope creep** – items added mid-sprint without capacity adjustment.
- **Interruptions** – production bugs, unplanned work.
- **Dependencies** – blocked by other teams or environments.
- **Estimation** – consistent over/under-estimation.
- **Technical debt** – time spent on refactoring vs new features.
- **Meetings** – too many or poorly timed.

---

## 6. Recommendations

### Immediate

1. **Track scope changes:** Add a simple process to record items added or removed mid-sprint (e.g. in sprint planning notes or a custom field).
2. **Review backlog size:** Aim for 10–20 well-defined items per sprint instead of 40–90.
3. **Document retros:** Retros are in Azure DevOps; use the extension's History view for trend analysis and recurring themes.

### Medium Term

1. **Use story points:** If not already, introduce points for better capacity and predictability.
2. **Analyze carry-over:** Use work item revisions to quantify how much work is moved between sprints.
3. **Create a “Retro” work item type:** Link retros to sprints in Azure DevOps for traceability.

### For Recurring Issues

1. **Retro action backlog:** Track action items from retros (in the extension's History view) and review in the next retro.
2. **Theme analysis:** Review past retro boards in Boards → Retrospectives → History; tag recurring themes for quarterly review.
3. **Repeating feedback:** Use the extension's History view to compare feedback across PP-16 through PP-21 and identify unresolved issues.

---

## 7. Data Sources & Methodology

- **Source:** Azure DevOps REST API via MCP (`wit_get_work_items_for_iteration`, `wit_get_work_items_batch_by_ids`).
- **Team:** Core-Process-platform.
- **Project:** 360.
- **Sprints:** PP-16 to PP-21 (iteration IDs from `work_list_team_iterations`).
- **Completion sample:** 48 root work items from PP-16 fetched for state distribution.
- **Limitation:** Transferred/added metrics require revision history analysis. Retro content is in Azure DevOps (Retrospectives extension) but not exposed via the Work Item Tracking API.

---

## Appendix: Sprint Iteration IDs

| Sprint | Iteration ID |
|--------|--------------|
| PP-16 | c0801d12-3b0b-42f6-b2a0-fab1a05b5177 |
| PP-17 | 2a775370-ba6b-46d1-aec3-51d2e95beb6a |
| PP-18 | ff6d2f4a-5723-4a62-89f1-e06a867705c8 |
| PP-19 | d3b9fcc1-9b64-471d-9480-5afd5a068bb0 |
| PP-20 | 6fbda8ab-5bac-4bf5-94a6-4fcfcf9fd165 |
| PP-21 | 09ddf2e9-fe45-4661-945a-e9959ef0b097 |
