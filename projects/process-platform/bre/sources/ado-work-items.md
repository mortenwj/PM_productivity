# Azure DevOps — BRE work items

**Project:** 360  
**Query date:** 2026-06-08 (refreshed)  
**Query:** Epic #11122 children + title/tag search for BRE/DMN

---

## Epic

### #11122 — DMN - Business Rules Engine

| Field | Value |
|-------|-------|
| **Type** | Epic |
| **State** | New |
| **Area** | 360\Core-Process-platform |
| **Iteration** | 360\core\Process-platform |
| **Assigned to** | Bjørn Kristiansen |
| **Created by** | Morten Jensen (2019-03-05) |
| **Start** | 2025-02-20 |
| **Target** | 2026-12-30 |
| **Link** | https://dev.azure.com/tieto-si/360/_workitems/edit/11122 |

**Description summary:**

- Need configurable no/low-code business rules in 360
- InRule evaluation did not yield desired results → internal engine
- Must support **DMN standard** (https://www.omg.org/dmn/)
- Use cases: configurable validations; IFTTT flows combined with processes
- DMN enables import/export and sharing of rules

**Attachments on epic:** `Risk assesment Business_Rules.xlsx`, `BRE_Actions.docx`, `Massejournalisering - Regler.docx`

---

## Platform features (children of #11122)

### Active (in progress)

| ID | Title | Assigned |
|----|-------|----------|
| [301056](https://dev.azure.com/tieto-si/360/_workitems/edit/301056) | BRE - Data model | Bjørn |
| [362499](https://dev.azure.com/tieto-si/360/_workitems/edit/362499) | BRE - Validations on RuleSets | Bjørn |
| [364464](https://dev.azure.com/tieto-si/360/_workitems/edit/364464) | BRE - Standard (BuiltIn) Queries and Actions | Bjørn |
| [371193](https://dev.azure.com/tieto-si/360/_workitems/edit/371193) | BRE - DMN - Input Resolution Service | Bjørn |

### New (backlog)

| ID | Title | Assigned |
|----|-------|----------|
| [392248](https://dev.azure.com/tieto-si/360/_workitems/edit/392248) | BRE - Admin Design | Bjørn |
| [373120](https://dev.azure.com/tieto-si/360/_workitems/edit/373120) | BRE - BusinessRuleSet Version & Publishing Support | Bjørn |
| [364641](https://dev.azure.com/tieto-si/360/_workitems/edit/364641) | BRE - Business Rules Admin UX | Bjørn |
| [301062](https://dev.azure.com/tieto-si/360/_workitems/edit/301062) | BRE - Executing RuleSets from Meta Events | Bjørn |
| [369221](https://dev.azure.com/tieto-si/360/_workitems/edit/369221) | BRE - Admin - DMN ↔ Meta Model Synchronization | Bjørn |
| [370766](https://dev.azure.com/tieto-si/360/_workitems/edit/370766) | BRE - Runtime Engine Repository and CI/CD | Bjørn |
| [370784](https://dev.azure.com/tieto-si/360/_workitems/edit/370784) | BRE - InMemory Cache of Executable Rule Models | Bjørn |
| [364034](https://dev.azure.com/tieto-si/360/_workitems/edit/364034) | BRE - Statistics and monitoring | — |
| [301078](https://dev.azure.com/tieto-si/360/_workitems/edit/301078) | DMN - Query interface for 360 | — |
| [301068](https://dev.azure.com/tieto-si/360/_workitems/edit/301068) | DMN - rules library | — |
| [301063](https://dev.azure.com/tieto-si/360/_workitems/edit/301063) | BRE - standard rule-set for 360 | — |
| [374441](https://dev.azure.com/tieto-si/360/_workitems/edit/374441) | BRE - Misc | — |
| [345523](https://dev.azure.com/tieto-si/360/_workitems/edit/345523) | Make it possible to set more validation requirements when closing a case | Morten |

### Closed

| ID | Title | Assigned |
|----|-------|----------|
| [90638](https://dev.azure.com/tieto-si/360/_workitems/edit/90638) | evaluate InRule engine as an integration component | Andreas |
| [351872](https://dev.azure.com/tieto-si/360/_workitems/edit/351872) | BRE - PM - Common Project Infrastructure | Bjørn |

### User story under epic

| ID | Title | State |
|----|-------|-------|
| [345526](https://dev.azure.com/tieto-si/360/_workitems/edit/345526) | AURSKOG-HØLAND KOMMUNE PUBLIC360 - Automatisk avslutning av saker i P360 | New |

---

## Customer / scenario-linked items (tagged Business rules)

| ID | Title | State | Assigned | Tags / notes |
|----|-------|-------|----------|--------------|
| [219865](https://dev.azure.com/tieto-si/360/_workitems/edit/219865) | Make it possible to set more validation requirements when closing a case | New | Morten | Business rules; **Scope: First** |
| [239187](https://dev.azure.com/tieto-si/360/_workitems/edit/239187) | Cases without documents → void only | New | — | **Scope: First** (from scope sheet) |
| [283950](https://dev.azure.com/tieto-si/360/_workitems/edit/283950) | AST - Handling of business rules | New | Morten | ast; Business rules; FFUI scenarios |
| [311335](https://dev.azure.com/tieto-si/360/_workitems/edit/311335) | AURSKOG-HØLAND - Automatisk avslutning av saker | Pending | Elisabeth | Business rules; **Scope: First**; Discovery: Yes |
| [202616](https://dev.azure.com/tieto-si/360/_workitems/edit/202616) | Checked-out files / "Under arbete" validation | — | — | **Scope: Second** |
| [255097](https://dev.azure.com/tieto-si/360/_workitems/edit/255097) | 90-day auto-close (Arbetsmiljöverket) | — | — | **Scope: Second** |
| [256135](https://dev.azure.com/tieto-si/360/_workitems/edit/256135) | Sync responsible person case → documents | — | — | Event / Update |
| [297383](https://dev.azure.com/tieto-si/360/_workitems/edit/297383) | Document archive move restrictions (Tullverket) | — | — | Event / Raise Error |
| [299567](https://dev.azure.com/tieto-si/360/_workitems/edit/299567) | Document distribution on case distribute | — | — | Multiple customers |
| [312153](https://dev.azure.com/tieto-si/360/_workitems/edit/312153) | Auto due date on incoming document (Helsedirektoratet) | — | — | Event / Update |
| [329199](https://dev.azure.com/tieto-si/360/_workitems/edit/329199) | Default incoming doc status Registered (Kommerskollegium) | — | — | Event / Update |

---

## WIQL used

```sql
-- All children of epic
SELECT [System.Id], [System.Title], [System.State], [System.AssignedTo], [System.WorkItemType]
FROM WorkItems
WHERE [System.TeamProject] = '360' AND [System.Parent] = 11122
ORDER BY [System.State], [System.Title]

-- Broader search
SELECT [System.Id], [System.Title], [System.State], [System.WorkItemType],
       [System.AreaPath], [System.AssignedTo], [System.ChangedDate]
FROM WorkItems
WHERE [System.TeamProject] = '360'
  AND ( [System.Title] CONTAINS 'BRE'
     OR [System.Title] CONTAINS 'Business Rule'
     OR [System.Title] CONTAINS 'Rules Engine'
     OR [System.Title] CONTAINS 'DMN'
     OR [Tags] CONTAINS 'BRE' )
ORDER BY [System.ChangedDate] DESC
```

---

## Commitment-driven timeline

**Planning assumption:** Customer commitments in DevOps define delivery pressure more reliably than epic #11122 target date (2026-12-30).

| Tier | When | Items | What they need from BRE |
|------|------|-------|-------------------------|
| **Overdue** | Jun 2025 | #312153 | Event + Update data (due date on doc) — `Commitment`, `Pri 1` |
| **Near-term text deadline** | Feb 2026 | #231319 | Event + cleanup on close — `Commitment` (no target date field) |
| **Mid 2027** | Jun 2027 | #422713 | Auto-close documents on case close — `conditional commitment` |
| **Late 2027** | Sep 2027 | #420587, #420590, #420282 | Mandatory fields, field dependency, cleanup jobs — IVO tender |

**Anchor date for "BRE meets commitments": mid–late 2027** (Jun–Sep), not Dec 2026.

Epic #11122 remains the internal backlog root but should be reconciled with this external timeline at the Copenhagen roadmap session.

---

## Notes

- **4 Active features** indicate runtime foundation work (data model, input resolution, validations, built-in queries/actions)
- Admin UX, publishing, meta events remain **New** — aligns with immature authoring surface
- Filter by Area Path `Core-Process-platform` for platform work; many DMN-tagged items elsewhere are unrelated
- Parent epic #11122 is the canonical backlog root for BRE platform features
