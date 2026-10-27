# Current state — Public 360° search

**Status:** Draft (desk research)  
**Last updated:** 2026-07-08  
**Refresh:** Product owner demo + help center before PRD

---

## Surfaces today

| Surface | Role | Notes |
|---------|------|-------|
| **Global Search** | Fast cross-type overview | Filters by entity type; operators per KUM bid text |
| **Advanced Search** | Structured multi-criteria | Form-based; cross-entity combinations; saved searches |
| **Saved searches** | Reuse + share | Toggle for sharing (MK-69) |
| **360° Search Assistant** | NL + statistics module | Built on Advanced Search; licensed; **public cloud only** (for now) |

---

## Search Assistant (documented)

Source: [New 360° Search Assistant module](https://help.360online.com/Release_information/Index.html#!Documents/newmodule2.htm)

- NL prompts → precise, **auditable** criteria.
- Entities: cases, documents, files, projects, employees, etc.
- Sorting, grouping, column selection; results → saved searches.
- Org-level search templates.
- Two menu entries at bottom of Advanced Search when enabled.
- Submodule: statistics / counting.

**Admin constraints** ([admin help](https://help.360online.com/6.8.0000/SIAdminHelp/1033/HH_Start.htm#!Documents/360searchassistant.htm)):

- Searchable metadata = configured subset (`CaseSearchAI`, `DocumentSearchAI`, … in Meta administrator).
- Default date filters to limit DB load (user can override).

**Visual query builder (observed, not fully in public help):**

- Screenshot: `../evidence/screenshots/sa-query-builder-case-document.png`
- Case root → **+ Relation** → Document; filter e.g. "Document title begins with test"
- Default 6-month result window; "No time limit" override
- Internal roadmap reference: query builder GA ~6.12 (verify with product)

---

## Platform / licensing

From `docs/product/Module_platform_support_overview.md`:

- **360° Search Assistant:** No on-prem; Yes public cloud; No domestic/private (for now).
- Separate module license.

---

## Gaps vs tender "search block" (UIM)

| ID | Title | Tool | Issue |
|----|-------|------|-------|
| MK-66 | Søgning på flere felter på samme tid | Partly met | Cross-entity / "all fields at once" interpretation |
| MK-74/75 | Søgebilleder | Partly met | Customer-configurable search forms |
| MK-77 | Visning af store mængder | Not met | Unbounded result lists |

---

## T1 evidence still needed

- [ ] Full entity/relation/operator matrix for visual query builder
- [ ] Custom field coverage via SearchAI meta config
- [ ] ADO epic/feature IDs for Search Assistant + query builder
- [ ] On-prem / domestic cloud roadmap
