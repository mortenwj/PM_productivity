# Tender and market pull

**Status:** Draft  
**Last updated:** 2026-07-08

---

## UIM ESDH — search requirements (Bilag 1.b)

Full list: 17 rows in **Søgning** section + MK-30, MK-77. Tool: `docs/tender-reference/source/UIM ESDH Tender tool.xlsx`

### Priority rows for this project

| ID | Title | Tool (O) | AI | Notes |
|----|-------|----------|-----|-------|
| **MK-66** | Søgning på flere felter på samme tid | Partly met | Partial | *Alle standard- og kundeoprettede felter på samme tid* — ADN: no entity boundaries |
| MK-65 | Søgning | Fully met | Met | "All fields" risk |
| MK-74 | Søgebilleder - Entiteter | Partly met | Partial | Customer-configurable search forms |
| MK-75 | Søgebilleder - Felter | Partly met | Partial | Customer-defined field sets |
| MK-73 | Søgning på tværs af Entiteter | Fully met | Met | Cross-entity |
| K-4 | Søgeoperatorer | Fully met | Met | AND/OR/NOT, comparisons |
| MK-77 | Visning af store mængder | Not met | Not met | Unbounded lists |

### MK-66 requirement text

> ESDH-løsningen skal understøtte, at der kan søges på alle standard- og Kundeoprettede felter på samme tid i ESDH-løsningen.

**Reasonable reading (KUM precedent):** Combined criteria across objects in **one search form** — not unconstrained flat search across every field.

**Recommended bid stance:** Partial → Met with clarification, citing Advanced Search + Search Assistant visual builder.

---

## KUM-SLKS — prior bid language (reuse)

Source: `docs/tender-reference/extracted/KUM-SLKS/Bilag 3 - Kravspecifikation.txt`

Key claims already made:

- Combined search across objects via **Global Søg** + **Avanceret Søgning**.
- One advanced search form with fields from multiple object types; criteria visible and auditable.
- Operators: AND, OR, NOT, Contains, Equals, Greater/Less than.
- Examples: case + document + workflow criteria in one query.

Search Assistant should be positioned as **evolution** of this story, not a contradiction.

---

## Timeline pressure (UIM PFR context)

- Tender decision: **Nov 2026**
- Build deadline: **Oct 2027**
- Search Assistant query builder maturity: verify GA date vs tender commitments
