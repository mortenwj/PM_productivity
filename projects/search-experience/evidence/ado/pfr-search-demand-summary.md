# PFR evidence — search improvement demand

**Captured:** 2026-07-08  
**Tier:** T3 (ADO / internal)  
**Status:** **Live ADO verified** 2026-07-08 via Azure DevOps MCP (Tier A enriched; WIQL open-search PFR query returned 100+ items)

---

## Sources

| Source | Location | Notes |
|--------|----------|-------|
| PFR Feature export (CSV) | `outputs/archive/_archive/large_inputs/pfrs (1).csv` | Full PFR board export snapshot |
| Structured extract | [`pfr-search-demand.json`](./pfr-search-demand.json) | 61 items after relevance filter (CSV-based) |
| **Live ADO — Tier A** | [`pfr-tier-a-ado-live.json`](./pfr-tier-a-ado-live.json) | Current state, customer, Impacted Module |
| Extraction script | `toolkit/pfr/extract_search_pfr_evidence.py` | Re-runnable CSV filter |
| PFR board (live) | [Product First Requests](https://dev.azure.com/tieto-si/360/_boards/board/t/Product%20First%20Requests/Features) | Query ID `bb65b39e-f496-4577-85d2-6211ec66c218` |
| Prior PFR analysis | `outputs/pfr/new_state_impacted_module_proposals.md` | Search module tagging |

### Live ADO refresh (recommended WIQL)

```wiql
SELECT [System.Id], [System.Title], [System.State], [System.AssignedTo], [System.CreatedDate]
FROM WorkItems
WHERE [System.TeamProject] = '360'
  AND [System.WorkItemType] = 'Feature'
  AND [System.IterationPath] UNDER '360\Product First Requests'
  AND [System.State] <> 'Closed'
  AND [System.State] <> 'Rejected'
  AND (
    [System.Title] CONTAINS 'search'
    OR [System.Description] CONTAINS 'Advanced Search'
    OR [System.Description] CONTAINS 'Global Search'
    OR [System.Description] CONTAINS 'cross-entity'
    OR [System.Description] CONTAINS 'Add search field'
    OR [System.Description] CONTAINS 'metadata'
  )
ORDER BY [System.ChangedDate] DESC
```

---

## Summary counts (filtered extract)

| Metric | Count |
|--------|------:|
| Total matched (search + cross-entity and/or meta-field themes) | 61 |
| **Tier A** — cross-entity + search, or explicit all-metadata-in-search | 11 |
| **Tier B** — related meta-field or cross-entity demand | 50 |
| Items with `meta_fields_all` theme | 21 |
| Items with `cross_entity` theme | 43 |

**Tier definitions (this extract):**

- **A:** Cross-entity + Advanced/Global search in same item, *or* explicit “all customer metadata / all fields” searchable behaviour.
- **B:** Meta-field discoverability (`Add search field`), result-view columns, entity-adjacent search, or cross-entity without full search context.

---

## Theme 1 — Cross-entity and combined-criteria search

Customer language consistently asks to **search across object types or via relations**, not run separate searches per entity.

| ID | State | Title | Why it matters |
|----|-------|-------|----------------|
| [181607](https://dev.azure.com/tieto-si/360/_workitems/edit/181607) | Active | Sundvall/Tullverket — search Case/**document** using contact personal/org number | Classic cross-entity: contact criterion → case + document hits |
| [231324](https://dev.azure.com/tieto-si/360/_workitems/edit/231324) | New | Field **"Included in"** added to search (Svenska kyrkan) | Estate ↔ object **relationship** search; result views |
| [203211](https://dev.azure.com/tieto-si/360/_workitems/edit/203211) | New | Add **contacts** to custom result views (case + document Advanced Search) | Cross-entity columns in one result set |
| [188808](https://dev.azure.com/tieto-si/360/_workitems/edit/188808) | New | Advanced Search to **eArchive** when adding access requests from P360 | Cross-system search entry; P360 ↔ archive |
| [377579](https://dev.azure.com/tieto-si/360/_workitems/edit/377579) | New | PB360: search responsible units **different from** PB units | Combined criteria on case/document |
| [156018](https://dev.azure.com/tieto-si/360/_workitems/edit/156018) | New | Ruter — **Activities** search field on documents + open activity in display | Document search enriched with activity state |
| [386446](https://dev.azure.com/tieto-si/360/_workitems/edit/386446) | **Closed** | NIPPON GASES — **Global Search filter views** as in Advanced Search | User expectation: one coherent “power search” model |

**Pattern:** Demands align with **MK-66 / KUM combined-criteria** narrative and with Search Assistant’s **relation tree** model — but PFRs are filed against **classic Advanced Search**, not SA.

---

## Theme 2 — Meta fields, “all fields”, and Add search field friction

### Explicit “all metadata searchable” (Tier A)

| ID | State | Title | Demand |
|----|-------|-------|--------|
| [386280](https://dev.azure.com/tieto-si/360/_workitems/edit/386280) | New | **Additional data — enhanced filtering** (NAV/Arbeids- og Velferdsetaten) | Today **all customer-specific metadata** appear under “Add Search Field” even when case type is selected; want **filtering** so only relevant metadata show — but confirms breadth of metadata exposure problem |

> **Tension with MK-66:** Tender asks for searching **all standard and customer fields at once**. PFR 386280 shows the opposite UX pain — **too many** metadata options without context filtering. Product must reconcile “combined power search” with “sensible field scoping per entity/case type”.

### Meta / custom fields hard to reach (Tier A / B)

| ID | State | Title | Demand |
|----|-------|-------|--------|
| [172703](https://dev.azure.com/tieto-si/360/_workitems/edit/172703) | Active | **Multiple value lookup** fields in Advanced Search (Havs- och vattenmyndigheten) | Custom meta field type not searchable seamlessly |
| [239645](https://dev.azure.com/tieto-si/360/_workitems/edit/239645) | New | **Estate — Property number** missing from standard Advanced Search form | Must use “Add search field” every time |
| [208230](https://dev.azure.com/tieto-si/360/_workitems/edit/208230) | New | Jordbruksverket — **more fields** in Case advanced search result views | Contacts, process plan, case references, keywords |
| [390501](https://dev.azure.com/tieto-si/360/_workitems/edit/390501) | New | More columns when configuring **search result view for Case** | Result configurability |
| [388885](https://dev.azure.com/tieto-si/360/_workitems/edit/388885) | New | More available columns — **Search** list views | Same cluster |
| [368463](https://dev.azure.com/tieto-si/360/_workitems/edit/368463) | New | NOKUT — columns in **Advanced Search contacts** | Entity-specific field gap |
| [300567](https://dev.azure.com/tieto-si/360/_workitems/edit/300567) | New | **Inserted date** on Unregistered contact Advanced Search results | Meta field on result list |
| [175807](https://dev.azure.com/tieto-si/360/_workitems/edit/175807) | New | Process status in **UCC** columns (case/document search) | Cross-entity display |
| [247404](https://dev.azure.com/tieto-si/360/_workitems/edit/247404) | New | Possibility to add field in **own search view for all object types** | Wants custom meta on standard form + result views — **søgebillede** adjacent |

**Pattern:** Customers expect **customer-created meta fields** to be first-class in search without “Add search field” archaeology. Maps to investigation **H6** (SearchAI meta parity vs classic Advanced Search) and **MK-74/75** (søgebilleder).

---

## Theme 3 — Global vs Advanced UX coherence (supports SA as primary)

| ID | State | Title | Demand |
|----|-------|-------|--------|
| [386446](https://dev.azure.com/tieto-si/360/_workitems/edit/386446) | **Closed** | Global Search **filter views** like Advanced Search | Split mental model |
| [398108](https://dev.azure.com/tieto-si/360/_workitems/edit/398108) | New | Global Search **remember last filters** | Persistence |
| [302489](https://dev.azure.com/tieto-si/360/_workitems/edit/302489) | New | Administration of **global search favorites** | Ops / sharing |
| [369753](https://dev.azure.com/tieto-si/360/_workitems/edit/369753) | New | Sort search results for Case by **Class** column | Result UX |
| [129543](https://dev.azure.com/tieto-si/360/_workitems/edit/129543) | New | **Enter key** behaviour inconsistent across Advanced Search entities | Polish / parity |

From `outputs/pfr/new_state_impacted_module_proposals.md` — additional Search-tagged PFRs: 369753, 398108, 388885, 390501, 302489.

---

## Implications for Search Assistant as primary advanced search

| Finding | Implication |
|---------|-------------|
| **43 PFRs** touch cross-entity themes | Market pull for **relation/combined queries** — SA visual QB + JsonQuery relations address this better than form patching |
| **21 PFRs** touch meta-field searchability | `*SearchAI` meta config must **expand** or customers keep filing “Add search field” PFRs |
| **386280** (all metadata visible) vs **MK-66** (all fields at once) | Product must define **scoped “all fields”** — entity + case-type aware, not flat infinite list |
| PFRs cite **Advanced/Global Search**, not SA | Position SA as **successor UX** that absorbs open demand; update Impacted Module tagging |
| No PFR in extract mentions **Search Assistant** by name | Discovery/positioning gap — customers still think in legacy surfaces |

---

## Tier A — full list (live ADO, 2026-07-08)

| ID | Title | State | Customer | Impacted Module |
|----|-------|-------|----------|-----------------|
| 181607 | Case/document search via contact PNR | **Active** | Sundsvall, Tullverket, Uppsala | Search |
| 172703 | Multiple value lookup in advanced search | **Active** | Havs- och vattenmyndigheten | Search |
| 386280 | Additional data — metadata filtering / cross-field search | New | **NAV** | *(unset)* |
| 231324 | "Included in" estate relation search | New | Svenska Kyrkan | Search |
| 203211 | Contacts in custom result views | New | SSM, Tullverket, Riksbank, … | Search |
| 208230 | More fields in Case result views (1:N) | New | Jordbruksverket | Search |
| 239645 | Estate property number on standard form | New | KUM Slots-/Kulturstyrelsen | Search |
| 129543 | Enter-key parity in Advanced Search | New | KFST | Search |
| 258728 | "All words" vs "begins with" on Responsible | New | DSS | Search |
| 377579 | PB360 wrong responsible unit search | New | Arendal/Grimstad P&B | Plan&Build |
| 188808 | Advanced search for eArchive access requests | New | DSS | eArchive |
| ~~388375~~ | Journal units in advanced search | **Closed** | Svenska Kyrkan | Configurations |

**State changes vs CSV snapshot:** #388375 Closed; #386446 (Tier B) Closed.

**Standout live quote — [#386280](https://dev.azure.com/tieto-si/360/_workitems/edit/386280) (NAV):**  
*"you cannot search across all fields; you must search one field at a time"* — direct customer evidence for MK-66 / multi-field gap, while same PFR also asks to filter irrelevant metadata out of Add Search Field.

Full machine-readable live record: [`pfr-tier-a-ado-live.json`](./pfr-tier-a-ado-live.json).  
CSV-filtered list (61 items): [`pfr-search-demand.json`](./pfr-search-demand.json).

---

## Gaps / next refresh

- [x] Live ADO WIQL — 100+ open search-related PFRs (2026-07-08)
- [x] Tier A live state + Customer + Impacted Module
- [ ] Batch-refresh all 61 CSV-filtered IDs (batch API timed out; use smaller batches)
- [ ] Link PFRs to ADO epic **402803** (AISearchBuilder toggles)
