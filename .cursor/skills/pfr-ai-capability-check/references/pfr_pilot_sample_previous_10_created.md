# Pilot sample B: **previous** 10 PFR Features (11th–20th by `CreatedDate` desc)

**As of:** 2026-04-29  
**Project:** `360` — same WIQL as pilot A, `top` = 20, then **rows 11–20** (next oldest after the 10 newest).

**Compared to pilot A** (`pfr_pilot_latest_10_created.md`): this slice is **mostly IVO tender requirements** plus **one Oslo P&B** change and **one NVE file-operations** change request — less Bergen P&B suggestion clustering.

| # | ID | Created (UTC) | State | P | Title (short) | Customer | Impacted module | Source |
|---|-----|-----------------|-------|---|-----------------|----------|-----------------|--------|
| 1 | [420623](https://dev.azure.com/tieto-si/360/_workitems/edit/420623) | 2026-04-24 06:31 | New | 2 | Tender requirement: marking on case for personal / sensitive PI | IVO | Case | New Bid/Tender |
| 2 | [420621](https://dev.azure.com/tieto-si/360/_workitems/edit/420621) | 2026-04-24 06:22 | New | 2 | Tender requirement: personal ID and samordningsnummer | IVO | Contact | New Bid/Tender |
| 3 | [420616](https://dev.azure.com/tieto-si/360/_workitems/edit/420616) | 2026-04-24 06:05 | New | 2 | Tender requirement: protection of personal information (internal/external) | IVO | Access Code | New Bid/Tender |
| 4 | [420614](https://dev.azure.com/tieto-si/360/_workitems/edit/420614) | 2026-04-24 05:40 | New | 2 | Change request: change access code on files (caseworker operation) | NORGES VASSDRAGS- OG ENERGIDIREKTORAT | File Operations | Change requests from Customer |
| 5 | [420590](https://dev.azure.com/tieto-si/360/_workitems/edit/420590) | 2026-04-23 15:17 | New | 2 | Tender requirement: multivalue fields depend on another multivalue field | IVO | Case | New Bid/Tender |
| 6 | [420587](https://dev.azure.com/tieto-si/360/_workitems/edit/420587) | 2026-04-23 14:57 | New | 2 | Tender requirement: actions make fields mandatory | IVO | Case | New Bid/Tender |
| 7 | [420558](https://dev.azure.com/tieto-si/360/_workitems/edit/420558) | 2026-04-23 14:12 | New | 2 | Tender requirement: case content report, internal and external | IVO | Case | New Bid/Tender |
| 8 | [420492](https://dev.azure.com/tieto-si/360/_workitems/edit/420492) | 2026-04-23 10:06 | New | 2 | PB360: option for contact person as case contact | Oslo kommune | Plan&Build | *(empty)* |
| 9 | [420282](https://dev.azure.com/tieto-si/360/_workitems/edit/420282) | 2026-04-22 11:23 | New | 2 | Tender requirement: cleaning job when closing case | IVO | Case | New Bid/Tender |
| 10 | [420281](https://dev.azure.com/tieto-si/360/_workitems/edit/420281) | 2026-04-22 11:15 | New | 2 | Tender requirement: save origin for case | IVO | Case | New Bid/Tender |

**P** = `Microsoft.VSTS.Common.Priority`.

## ID list (copy-paste)

`420623, 420621, 420616, 420614, 420590, 420587, 420558, 420492, 420282, 420281`
