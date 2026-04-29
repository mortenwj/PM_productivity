# Pilot list: 10 most recently **created** PFR Features (DevOps)

**As of:** 2026-04-29 (query time in MCP)  
**Project:** `360`  
**WIQL:** `Feature` under `360\Product First Requests`, `ORDER BY [System.CreatedDate] DESC`, `top` = 10.

| # | ID | Created (UTC) | State | P | Title (short) | Customer | Impacted module | Source |
|---|-----|-----------------|-------|---|-----------------|----------|-----------------|--------|
| 1 | [421450](https://dev.azure.com/tieto-si/360/_workitems/edit/421450) | 2026-04-29 13:10 | New | 2 | PB360: Innsyn og filer — ikke mulighet til å hente alle filer … | Hamar kommune / Indigo IKT | Document | Change requests from Customer |
| 2 | [421448](https://dev.azure.com/tieto-si/360/_workitems/edit/421448) | 2026-04-29 13:05 | New | 3 | Suggestion (P&B): moving multiple files at once during registration | Oslo Kommune | File Operations | *(empty)* |
| 3 | [421428](https://dev.azure.com/tieto-si/360/_workitems/edit/421428) | 2026-04-29 12:08 | New | 4 | Suggestion (P&B): link new documents to case processing phases | Bergen kommune | Case Handling Model | *(empty)* |
| 4 | [421370](https://dev.azure.com/tieto-si/360/_workitems/edit/421370) | 2026-04-29 10:28 | New | 3 | Suggestion (P&B): flexibility in case handling models | Bergen kommune | Case Handling Model | *(empty)* |
| 5 | [421353](https://dev.azure.com/tieto-si/360/_workitems/edit/421353) | 2026-04-29 09:26 | New | 2 | Suggestion (P&B): close stage before complaint deadline | Bergen kommune | Case Handling Model | *(empty)* |
| 6 | [420968](https://dev.azure.com/tieto-si/360/_workitems/edit/420968) | 2026-04-27 13:40 | New | 2 | NAV: eArchive edit imported document number | *(empty)* | eArchive | *(empty)* |
| 7 | [420902](https://dev.azure.com/tieto-si/360/_workitems/edit/420902) | 2026-04-27 11:14 | New | 3 | Suggestion: prosesser seksjoneringsak | Bergen kommune | Case Handling Model | *(empty)* |
| 8 | [420839](https://dev.azure.com/tieto-si/360/_workitems/edit/420839) | 2026-04-27 07:46 | New | 2 | PB360: activities in diagrams | KRISTIANSAND KOMMUNE | Plan&Build | Change requests from Customer |
| 9 | [420762](https://dev.azure.com/tieto-si/360/_workitems/edit/420762) | 2026-04-24 12:43 | New | 2 | SIF: generic activity services + custom fields | SCC Skiljedomsinstitut | SIF | Upgrade Project |
| 10 | [420624](https://dev.azure.com/tieto-si/360/_workitems/edit/420624) | 2026-04-24 06:39 | New | 2 | Tender requirement: preliminary cases + conversion function | IVO | Case | New Bid/Tender |

**P** = `Microsoft.VSTS.Common.Priority`.

## Notes for testing

- **Mix:** Mostly **Bergen/Oslo/Hamar** P&B suggestions + **NAV eArchive** + **SIF upgrade** + **IVO tender** — good spread for staged retrieval (wiki/help vs tender text vs upgrade).
- **Field gaps:** Several rows have **`Custom.Source` empty** (pilot will surface whether the AI capability block + review rules behave as intended).
- **Board:** [Product First Requests — Features](https://dev.azure.com/tieto-si/360/_boards/board/t/Product%20First%20Requests/Features)

## Next step

Run the **`pfr-ai-capability-check`** skill per item (or batch 2–3 at a time to control tokens), paste JSON + Markdown into a scratch doc or DevOps **Description** append, and have a human score outcome vs tier rules.
