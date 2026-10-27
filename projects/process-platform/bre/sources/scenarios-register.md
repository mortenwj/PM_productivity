# BRE customer scenarios register

**Source:** `BRE_scope_and_scenarios.xlsx` (Sheet 1)  
**Extracted:** 2026-06-08

Columns: Invoke Type · Rule Type · Description · Customer · DevOps · Scope

---

| # | Scope | Invoke | Rule type | Summary | Customers | DevOps |
|---|-------|--------|-----------|---------|-----------|--------|
| 1 | Second | Event | Update | Validation: checked-out files + docs in "Under arbete" only (not all unhandled incoming) | Kungälv, Riksrevisionen, IVO, MFD, Försäkringskassan, Bergen | [202616](https://dev.azure.com/tieto-si/360/_workitems/edit/202616) |
| 2 | **First** | Event | Raise Error | Close-case validation: no working docs; mandatory fields; prevent cancel if docs not cancelled | Tullverket, Strålsäkerhetsmyndigheten, IMR, Regeringskansliet, Svenska kyrkan | [219865](https://dev.azure.com/tieto-si/360/_workitems/edit/219865) |
| 3 | **First** | Event | Raise Error | Cases without documents → only Void status allowed | Regeringskansliet Klaradia | [239187](https://dev.azure.com/tieto-si/360/_workitems/edit/239187) |
| 4 | Second | Job | Update | Auto-close case: one doc type 6.1-42, 90+ days old, has responsible | Arbetsmiljöverket | [255097](https://dev.azure.com/tieto-si/360/_workitems/edit/255097) |
| 5 | — | Event | Update | Change case responsible → all documents same responsible | Försäkringskassan, MFD, SKR | [256135](https://dev.azure.com/tieto-si/360/_workitems/edit/256135) |
| 6 | — | Event | Raise Error | Meeting doc: only one allowed per meeting | AST | [283950](https://dev.azure.com/tieto-si/360/_workitems/edit/283950) |
| 7 | — | FFUI | Raise Error | Meeting doc: required file types must be connected | AST | [283950](https://dev.azure.com/tieto-si/360/_workitems/edit/283950) |
| 8 | — | FFUI | Raise Error | Meeting doc: unchecked files connected → error | AST | [283950](https://dev.azure.com/tieto-si/360/_workitems/edit/283950) |
| 9 | — | FFUI | FFUI | Document category → title field auto-filled | AST | [283950](https://dev.azure.com/tieto-si/360/_workitems/edit/283950) |
| 10 | — | FFUI | FFUI | Board handling dialogue field guidance message | AST | [283950](https://dev.azure.com/tieto-si/360/_workitems/edit/283950) |
| 11 | — | FFUI | Raise Error | Mandatory contact roles per document package | AST | [283950](https://dev.azure.com/tieto-si/360/_workitems/edit/283950) |
| 12 | — | FFUI | Raise Error | Block changes to closed case | AST | [283950](https://dev.azure.com/tieto-si/360/_workitems/edit/283950) |
| 13 | — | Event | Raise Error | Restrict move/save between document archives | Tullverket | [297383](https://dev.azure.com/tieto-si/360/_workitems/edit/297383) |
| 14 | — | Event | Raise Error | Case distribute → document distribute options (4 modes) | Tullverket, Regeringskansliet, SKR, Kemikalieinspektionen | [299567](https://dev.azure.com/tieto-si/360/_workitems/edit/299567) |
| 15 | **First** | Job | Update | Automatic closing of cases based on rules | Aurskog-Høland | [311335](https://dev.azure.com/tieto-si/360/_workitems/edit/311335) |
| 16 | — | Event | Update | Incoming doc due date 120 days (case category Ammehjelpen) | Helsedirektoratet | [312153](https://dev.azure.com/tieto-si/360/_workitems/edit/312153) |
| 17 | — | Event | Update | Incoming documents default status Registered | Kommerskollegium | [329199](https://dev.azure.com/tieto-si/360/_workitems/edit/329199) |
| 18 | — | Event | Raise Error | Close-case validation (duplicate theme) | Tullverket et al. | [345523](https://dev.azure.com/tieto-si/360/_workitems/edit/345523) |

---

## First-wave themes (for pilot / workshop)

1. **Governance on case close/cancel** — validation, mandatory fields, document state checks  
2. **Empty case handling** — void-only without documents  
3. **Scheduled auto-close** — rule-based case closure (Aurskog-Høland pattern)

## Second-wave themes

1. **Lighter validation on status change** — checked-out / under arbeid only  
2. **Time-based auto-close** — 90-day rule with record type filter

## AST / FFUI cluster

Single feature [#283950](https://dev.azure.com/tieto-si/360/_workitems/edit/283950) covers multiple FFUI + event rules for meeting/case handling — likely a **package deal** for one customer upgrade.

---

## Sheet 2 — Unscoped ideas (for backlog discussion)

- Notify when approved documents not dispatched
- Checklist: only close allowed at certain checkpoints
- Milestone deadline → auto-close or notify
- Per-milestone rule attachment
