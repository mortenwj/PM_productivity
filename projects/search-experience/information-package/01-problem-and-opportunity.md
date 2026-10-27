# Problem and opportunity

**Status:** Draft  
**Last updated:** 2026-07-08

---

## Problem

Public 360° search is split across **Global Search**, **Advanced Search**, and (new) **360° Search Assistant**. Users and tenders expect **combined multi-field, cross-entity search in one place** — but the legacy Advanced Search UX feels dated and hard to extend without bolting on more complexity.

Patching Advanced Search alone is unlikely to feel optimal because:

- Cross-entity logic is awkward in classic form-based UIs.
- Tender language (e.g. UIM MK-66) pushes toward **one search surface** with multiple criteria — not repeated separate searches.
- Competitors (KMD WorkZone) expose **power search** via QueryBuilder + structured client search, not one infinite form.

---

## Opportunity

**360° Search Assistant** already:

- Converts natural language to **auditable structured queries** (built on Advanced Search).
- Shows a **visual query builder** (entity tree, relations, field operators) — see screenshot in evidence.
- Supports cross-entity insight, saved searches, org templates (per 6.8 release notes).

Hypothesis: SA could become the **primary advanced search experience** — NL for speed, visual builder for precision and audit — instead of maintaining two parallel mental models.

---

## Stakes (to confirm in product brief)

- [ ] Internal exploration / pilot only
- [ ] Tender compliance (UIM SKI, Nov 2026 decision)
- [ ] Customer-facing module positioning (licensed vs core)
- [ ] Replacement of Advanced Search UI vs additive module

---

## Open strategic questions

See [06-open-questions.md](./06-open-questions.md).
