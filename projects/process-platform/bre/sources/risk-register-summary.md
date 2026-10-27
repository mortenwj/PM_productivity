# BRE risk register — summary

**Source:** `Risk assesment Business_Rules.xlsx`  
**Extracted:** 2026-06-08

---

## Notable risks (from register tab)

| # | Category | Summary | Inherent score | Response | Residual | Owner | ADO link |
|---|----------|---------|----------------|----------|----------|-------|----------|
| — | Security | Business rules accessing data/BL — must be privileged | 16 | Mitigate: privileged authoring | 1 | Bjørn | [#364641](https://dev.azure.com/tieto-si/360/_workitems/edit/364641) |
| 3 | Business/Product | No formal price strategy yet | 15 | Mitigate: enablement meeting | 15 | Morten | — |
| 4 | Technical | Event system not designed for ad hoc runtime additions | 1 | Accept | 2 | — | — |
| 5 | Operational | Shortage of consultants for PE processes | 20 | Mitigate: education | 0 | — | In progress |
| 6 | Business/Product | Based on Camunda open-source component — license check | 10 | Mitigate: sourcing verify | 10 | Morten | — |
| 7 | Technical | Rules can run very long → bad UX | 8 | Mitigate | — | — | — |

---

## Risk category counts (summary sheet)

| Category | Count |
|----------|-------|
| Operations | 1 |
| Extreme inherent risks | 4 |
| Mitigate response | 6 |
| Accept response | 1 |
| States: New 1 · Assessed 4 · Mitigation in Progress 1 · Delayed 1 |

---

## Implications for product / workshop

1. **Security & governance** — Admin UX (#364641) is not just UX; it is a risk control  
2. **Commercial** — Pricing strategy gap must be closed before broad market message  
3. **Performance** — Long-running rules need architectural guardrails  
4. **Delivery capacity** — Consultant enablement is on critical path  
5. **License** — Confirm Camunda/DMN stack licensing with sourcing

---

## Full register

See original Excel in OneDrive for complete risk IDs, likelihood/impact matrix, and mitigation actions.
