# Competitive landscape — search

**Status:** Draft  
**Last updated:** 2026-07-08

---

## KMD WorkZone (primary comparator for Danish ESDH tenders)

### WorkZone Client search

Source: [Perform a search](https://docs.workzone.kmd.net/2023_2/en-us/Content/WZClient_UserGuide/Search/Perform_search.htm)

- Entity-specific search pages (Case, Document, Contact, Meeting).
- Multiple criteria on one page; multi-value fields default to **OR** (toggle to AND).
- **Cross-register search** — documents filtered by case criteria (structured, not flat).
- Configurable search pages (add/remove/reorder fields, incl. custom types).
- Saved, shareable searches.

### WorkZone QueryBuilder (WZQB)

Sources:

- [About WorkZone QueryBuilder](https://docs.workzone.kmd.net/2026_0/da-dk/Content/WZQB/WZQB_AboutWZQB.htm)
- [The QueryBuilder page](https://docs.workzone.kmd.net/2022_1/da-dk/Content/WZQB/WZQB_QueryBuilder%20page.htm)

| Aspect | Behaviour |
|--------|-----------|
| Model | OData graphical UI |
| Base entity | **One** per query; related via **Expand** |
| Multi-field | Multiple filters, **AND** combined |
| Operators | Equals, Contains, Starts/Ends with, date ranges, numeric compares |
| Custom fields | "Just Custom Properties" endpoint |
| Output | Grid, OData URI, Excel export |
| Reuse | Saved queries → lists, dashboards, tab filters, mobile filters |
| Limits | Read-only; not for create/update/delete |

### OData Summary / autocomplete

- `*_Summary` fields combine elaboration text for freetext-style search on some entities.

---

## Implication for Public 360°

KMD does **not** offer literal "all fields, all entities, no model" search. They split:

1. **Everyday** structured client search  
2. **Power** QueryBuilder (entity + expand + AND filters)

Our **Search Assistant visual query builder** is structurally similar to WZQB but with NL entry and a tree UI (+ Relation vs Expand clauses).

---

## Other references

- Prior bid language: KUM-SLKS Bilag 3 §Søgning (Global + Avanceret, combined criteria) — see `04-tender-and-market-pull.md`
