# ProductPlan — BRE roadmap bars

**Queried:** 2026-06-08 via ProductPlan MCP

---

## Relevant roadmaps

| Roadmap | ID | URL | BRE relevance |
|---------|-----|-----|---------------|
| **Process Platform** | 592160 | https://app.productplan.com/ZFvmHNxV | Legacy BRE bar (parked, stale dates) |
| **PP now next latrer** | 1017261 | https://app.productplan.com/KrKfGUzh | Discovery projects BRE (Now lane) |
| **commitment roadmap** | 1017493 | https://app.productplan.com/R-8-z40r | No BRE-specific bars found |

---

## Process Platform roadmap — DMN bar

| Field | Value |
|-------|-------|
| **Bar** | [DMN - Business Rules Engine](https://app.productplan.com/bars/13933596) |
| **Lane** | Process Platform - general framework |
| **Legend** | Goal 3 |
| **Dates** | 2022-06-20 → 2022-09-18 *(stale)* |
| **Percent done** | 52% |
| **Parked** | **Yes** |
| **Last updated** | 2026-06-07 |

**Description** (matches DevOps Epic #11122):

- Configurable no/low-code business rules in 360
- InRule evaluation did not yield desired results → internal engine
- Must support **DMN standard** (https://www.omg.org/dmn/)
- Use cases: validations (dispatch with checked-out files, milestone prerequisites); IFTTT flows with processes
- DMN import/export for sharing rules across customers and systems

**Reconciliation note:** Bar is **parked** with 2022 dates while DevOps epic #11122 has **Start 2025-02-20 / Target 2026-12-30** and active child features. Treat ProductPlan bar as **out of date** — refresh or replace at Copenhagen workshop roadmap session.

---

## PP now next later — Discovery

| Bar | Dates | Lane | Parent | Notes |
|-----|-------|------|--------|-------|
| [Discovery projects BRE](https://app.productplan.com/bars/35503953) | 2025-02-04 → 2025-06-02 | Now / Goal 1 | — | Container |
| [3 customers for discovery](https://app.productplan.com/bars/35503954) | 2025-02-14 → 2025-05-14 | Now / Goal 1 | Discovery projects BRE | Child bar |

**Reconciliation note:** Discovery window ended May 2025. Align with scope sheet discovery column and customer-linked DevOps items (#311335 AURSKOG-HØLAND, #283950 AST, etc.) when updating roadmap.

---

## Commitment roadmap

Full bar list scanned (300+ bars). **No bars** named BRE, DMN, Business Rules Engine, or Discovery projects BRE.

Items matching "flexibility" are unrelated customer commitments (e.g. stand-in, progress plan transfer).

---

## Suggested workshop actions

1. **Unpark or replace** Process Platform BRE bar with 2025–2026 dates aligned to epic #11122
2. **Close out** "3 customers for discovery" — document which customers and outcomes
3. **Add Next/Later bars** for Admin UX (#364641), meta events (#301062), publishing (#373120), first-wave scenarios
4. Link ProductPlan bars to DevOps epic/features for single source of truth going forward
