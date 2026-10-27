# BRE — customer scenarios

**Source:** `sources/scenarios-register.md` (from `BRE_scope_and_scenarios.xlsx`, extracted 2026-06-08)

---

## First-wave (pilot / workshop priority)

| Theme | Invoke | Action | Customers | ADO |
|-------|--------|--------|-----------|-----|
| Close-case validation | Event | Raise Error | Tullverket, Strålsäkerhetsmyndigheten, IMR, Regeringskansliet, Svenska kyrkan | [#219865](https://dev.azure.com/tieto-si/360/_workitems/edit/219865) |
| Empty cases → Void only | Event | Raise Error | Regeringskansliet Klaradia | [#239187](https://dev.azure.com/tieto-si/360/_workitems/edit/239187) |
| Auto-close cases (scheduled) | Job | Update | Aurskog-Høland | [#311335](https://dev.azure.com/tieto-si/360/_workitems/edit/311335) |

---

## Second-wave

| Theme | Invoke | Summary | ADO |
|-------|--------|---------|-----|
| Checked-out / under arbeid validation | Event | Lighter validation on status change | [#202616](https://dev.azure.com/tieto-si/360/_workitems/edit/202616) |
| Time-based auto-close (90+ days) | Job | Record type filter | [#255097](https://dev.azure.com/tieto-si/360/_workitems/edit/255097) |

---

## AST / FFUI cluster (package)

Single feature [#283950](https://dev.azure.com/tieto-si/360/_workitems/edit/283950) — meeting docs, mandatory contact roles, block changes to closed case, etc. **Not feasible in narrow code pilot** (FFUI runtime not implemented).

---

## Full register (18 scoped scenarios)

See [`../sources/scenarios-register.md`](../sources/scenarios-register.md) for the complete table with all customers and DevOps links.

---

## PRD implication

**MVP candidate slice** (aligned with code reality): Event trigger → Case OnUpdate → ValidationMessage → EntityField/StatementField inputs.

**Out of MVP:** Job triggers, RunProcess/update actions, FFUI rules, multi-decision models without StartingPoint fix.
