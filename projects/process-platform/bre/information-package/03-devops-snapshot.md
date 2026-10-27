# BRE — Azure DevOps snapshot

**Refreshed:** 2026-06-16 via Azure DevOps MCP (`wit_get_work_items_batch_by_ids`)  
**Project:** 360 · **Area:** Core-Process-platform  
**Full tree:** [`../sources/ado-work-items.md`](../sources/ado-work-items.md)

---

## Epic

### #11122 — DMN - Business Rules Engine

| Field | Value |
|-------|-------|
| State | New |
| Assigned | Bjørn Kristiansen |
| Start | 2025-02-20 |
| Target | **2026-12-30** |
| Changed | 2026-03-16 |
| Link | https://dev.azure.com/tieto-si/360/_workitems/edit/11122 |

**Description (summary):**

- Configurable no/low-code business rules in 360
- InRule evaluation insufficient → internal engine
- **DMN standard required** ([omg.org/dmn](https://www.omg.org/dmn/))
- Use cases: validations; IFTTT flows with processes; import/export of rules

**Attachments on epic:** Risk assessment xlsx, BRE_Actions.docx, Massejournalisering regler docx

---

## Platform features under epic (sample — live states)

| ID | Title | State | Assigned | Changed |
|----|-------|-------|----------|---------|
| [301056](https://dev.azure.com/tieto-si/360/_workitems/edit/301056) | BRE - Data model | **Active** | Bjørn | 2026-06-08 |
| [301062](https://dev.azure.com/tieto-si/360/_workitems/edit/301062) | BRE - Executing RuleSets from Meta Events | New | Bjørn | 2026-06-08 |
| [362499](https://dev.azure.com/tieto-si/360/_workitems/edit/362499) | BRE - Validations on RuleSets | Active | Bjørn | — |
| [364464](https://dev.azure.com/tieto-si/360/_workitems/edit/364464) | BRE - Standard (BuiltIn) Queries and Actions | Active | Bjørn | — |
| [371193](https://dev.azure.com/tieto-si/360/_workitems/edit/371193) | BRE - DMN - Input Resolution Service | Active | Bjørn | — |
| [392248](https://dev.azure.com/tieto-si/360/_workitems/edit/392248) | BRE - Admin Design | New | Bjørn | — |

---

## Customer-linked features (pilot drivers)

### #219865 — Close-case validation requirements

| Field | Value |
|-------|-------|
| Type | Feature |
| State | New |
| Assigned | **Morten Jensen** |
| Changed | 2026-03-16 |

**Ask:** Mandatory fields on close; no working documents on close; prevent cancel if docs not cancelled. Market: yes, multiple customers (upgrade/prestudy).

### #345523 — Same theme (epic child)

Duplicate close-case validation feature under epic #11122; assigned Morten; New.

---

## Commitment pressure (from inventory — not re-fetched)

Epic target **2026-12-30** may be **ahead** of customer Commitment-tagged items clustering **H2 2027** (IVO tender, Danish tender K). See `06-pilot-readiness-and-gaps.md`.

---

## Closed / historical

| ID | Title |
|----|-------|
| [90638](https://dev.azure.com/tieto-si/360/_workitems/edit/90638) | evaluate InRule engine (Closed) |
| [351872](https://dev.azure.com/tieto-si/360/_workitems/edit/351872) | BRE - PM - Common Project Infrastructure (Closed) |
