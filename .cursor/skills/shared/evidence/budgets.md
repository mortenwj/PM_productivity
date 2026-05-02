# Retrieval budgets (numeric caps)

**Purpose:** Single table for **default caps** referenced by retrieval profiles. Unless the user explicitly expands the budget, stay within these limits.

---

## Corpus call caps (default)

| Cap | Suggested default |
|-----|-------------------|
| **MediaWiki** — focused searches then page reads | **1–3** searches → fetch **≤5** high-value pages per run (prefer Release Information / module overview when choosing pages). |
| **Ratatoskr** — topics read after `search_topics` | **`read_topic` for ≤3** hits per run unless the user expands budget. |
| **Azure DevOps** — related / WIQL | Query **≤10** related IDs or one WIQL with small `top`; prefer **closed** items when claiming shipped behaviour (encode state in excerpts per PFR credibility doc). |
| **Broad repo searches** (e.g. whole-workspace ripgrep with tiny pattern) | **≤2** distinct search queries per run, each with a **path scope** (directory or known module root) when possible. |
| **Files read in full** (or large chunks) for implementation evidence | **≤5** files, prioritizing paths **hinted by wiki**, **help**, **ADO**, or **stack traces** in the work item / question. |
| **Lines / characters** from code | Keep each file read **bounded** (e.g. relevant symbol region); if the file is huge, read **headers + search within file** instead of the whole file. |

---

## Code exploration budget (hard caps for autonomous runs)

Same as above, summarized for PFR-style checks:

| Cap | Suggested default |
|-----|-------------------|
| **Broad repo searches** | **≤2** distinct search queries per check, each with a **path scope** when possible. |
| **Files read in full** (or large chunks) for T1 | **≤5** files, prioritizing paths **hinted by wiki**, **help**, **ADO**, or **stack traces** in the PFR. |
| **Lines / characters** pulled into the model from code | Keep each file read **bounded**; if file is huge, read **headers + search within file** instead of whole file. |

---

**File:** `shared/evidence/budgets.md`
