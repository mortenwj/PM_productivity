# Pilot sample C: **21st–30th** PFR Features by `CreatedDate` desc

**As of:** 2026-04-29 (query time in MCP)  
**Project:** `360` — same WIQL as pilot A (`Feature` under `360\Product First Requests`, `ORDER BY [System.CreatedDate] DESC`), **`top` = 30**, then **rows 21–30** (next oldest after sample B).

**Compared to pilot B** (`pfr_pilot_sample_previous_10_created.md`): this slice brings back **several Norwegian municipality P&B-style** items (Bergen search, Kristiansand map, Sarpsborg model change) alongside **Swedish HaV tender** cluster, **SIF**, **Teams**, **internal** detail-view improvement, and **WebAdmin** (Domstolsstyrelsen).

| # | ID | Created (UTC) | State | P | Title (short) | Customer | Impacted module | Source |
|---|-----|-----------------|-------|---|-----------------|----------|-----------------|--------|
| 1 | [420092](https://dev.azure.com/tieto-si/360/_workitems/edit/420092) | 2026-04-21 10:19 | New | 2 | Suggestion for improvement - search | BERGEN KOMMUNE | Search | *(empty)* |
| 2 | [419587](https://dev.azure.com/tieto-si/360/_workitems/edit/419587) | 2026-04-17 11:38 | New | 2 | PB360: Advanced Search — Case — Geographical Search — for Norkart map | Kristiansand kommune | Map Integration 360 | *(empty)* |
| 3 | [419267](https://dev.azure.com/tieto-si/360/_workitems/edit/419267) | 2026-04-15 11:03 | New | 2 | Improvements in Detail views setup | *(empty)* | Detail view | Internal suggestion for improvement |
| 4 | [419090](https://dev.azure.com/tieto-si/360/_workitems/edit/419090) | 2026-04-14 11:52 | New | 2 | Teams integration: registration screen/document card does not disappear on completion | *(empty)* | Teams Integration | *(empty)* |
| 5 | [418755](https://dev.azure.com/tieto-si/360/_workitems/edit/418755) | 2026-04-10 14:15 | New | 2 | Option to update multivalue lookup fields through SIF | Datatilsynet, Norges vassdrags- og energidirektorat | Simple Integration Framework (SIF) (126000) | Change requests from Customer |
| 6 | [418737](https://dev.azure.com/tieto-si/360/_workitems/edit/418737) | 2026-04-10 12:43 | New | 3 | Suggestion for improvment P&B — Bytting av modell | Sarpsborg-pb | Case Handling Model | *(empty)* |
| 7 | [418304](https://dev.azure.com/tieto-si/360/_workitems/edit/418304) | 2026-04-08 13:47 | New | 2 | Tender requirement: Dispose objects when cancelling | Havs- och vattenmyndigheten | Disposal and Retention | New Bid/Tender |
| 8 | [418294](https://dev.azure.com/tieto-si/360/_workitems/edit/418294) | 2026-04-08 13:19 | Closed | 2 | Tender requirement: All search fields available for search result | Havs- och vattenmyndigheten | Search | New Bid/Tender |
| 9 | [418254](https://dev.azure.com/tieto-si/360/_workitems/edit/418254) | 2026-04-08 11:12 | Closed | 2 | Tender requirement: Keep logs after retention | Havs- och vattenmyndigheten | Disposal and Retention | New Bid/Tender |
| 10 | [418224](https://dev.azure.com/tieto-si/360/_workitems/edit/418224) | 2026-04-08 08:25 | New | 2 | WebAdmin — Possibility to expand dialog boxes | Domstolsstyrelsen | Web admin | *(empty)* |

**P** = `Microsoft.VSTS.Common.Priority`.

## ID list (copy-paste)

`420092, 419587, 419267, 419090, 418755, 418737, 418304, 418294, 418254, 418224`

## Notes for testing

- **Closed in sample:** **418294**, **418254** — useful for piloting how the skill treats **State = Closed** PFRs vs open backlog (evidence / “already handled” narrative).
- **Field gaps:** **419090**, **420092**, **418737**, **419587**, **418224** have **`Custom.Source` empty** in the batch pull (same pattern as pilots A/B).
