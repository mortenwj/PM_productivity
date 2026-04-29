# PFR capability check — evidence retrieval cost (tokens / compute)

**Purpose:** Keep AI-assisted capability checks **affordable and predictable**. **T1 source code is ground truth**, but **unbounded code search** burns context fast and is usually unnecessary if **T2** docs already answer the question.

**Normative for:** `.cursor/skills/pfr-ai-capability-check/SKILL.md` (retrieval order and stop rules), alongside `pfr_evidence_sources_credibility.md`.

---

## 1. Relative cost (qualitative)

Higher = more tokens, latency, or tool volume. Use this to **order retrieval**, not to change **T1–T4 truth** once evidence is in hand.

| Source / action | Typical relative cost | Notes |
|-----------------|------------------------|--------|
| PFR fields already on the Feature (`wit_get_work_item`) | **Lowest** | Always first; no extra search. |
| **Internal MediaWiki** — targeted `mediawiki_search` / `mediawiki_get_page` for a few pages | **Low–medium** | Bounded by **query count** and **page cap** (see §3). |
| **Ratatoskr** — `search_topics`, `read_topic` for a small set of help topics | **Medium** | Help HTML can be large; cap **topics read** per run. |
| **Azure DevOps** — WIQL / get related / batch by id for a handful of items | **Low–medium** | Cheap if **top N** and **specific fields**; expensive if huge descriptions in batch. |
| **Repo / code** — `grep` / semantic search over **wide** paths, or many large files | **High** | Dominates token use if unconstrained. |
| **Deep code exploration** — many files, cross-service tracing | **Very high** | Reserve for **ambiguous** outcomes or **high-stakes** PFRs when user explicitly asks. |

**Rule:** **Credibility tier** answers “how much we trust this evidence.” **Cost** answers “**in what order** we try to find it and **when we stop**.” Cheap T2 that settles the question beats expensive T1 trawling.

---

## 2. Staged retrieval (default waterfall)

Execute **in order**; **stop early** when an outcome is already defensible under `pfr_evidence_sources_credibility.md` and `pfr_ai_capability_check_output_format.md` (including `human_review_required` / `limitations`).

| Stage | Action | Stop if |
|-------|--------|--------|
| **0** | Parse PFR **title, description, tags, Impacted Module, Source** | Empty body → outcome `insufficient_information`, list `unknowns`; still cheap. |
| **1** | **MediaWiki:** 1–3 focused searches → fetch **≤5** high-value pages (prefer Release Information / module overview per §2.1) | Strong T2 answers “already documented standard” or proves gap is doc-only. |
| **2** | **Ratatoskr:** `search_topics` (and `read_topic` only for **≤3** hits) | Help confirms/denies user-visible behaviour for same need. |
| **3** | **ADO:** query **≤10** related IDs or one WIQL with small `top`; prefer **closed** items for shipped claims | Closed item + wiki/help already support dual-T2 narrative. |
| **4** | **Code (T1):** only if stages 1–3 **do not** support a confident classification **or** user asks for code proof | **Scoped only** (§3); never “read the whole repo.” |

If stage 4 is skipped, state in **`limitations`**: e.g. “No source code retrieved; assessment based on T2 documentation and ADO metadata.” Apply the **strict gate** (no T1 → human review for `already_supported` / `achievable_without_new_core`) per credibility doc.

---

## 3. Code exploration budget (hard caps for autonomous runs)

Unless the user explicitly expands the budget:

| Cap | Suggested default |
|-----|-------------------|
| **Broad repo searches** (e.g. whole-workspace ripgrep with tiny pattern) | **≤2** distinct search queries per PFR check, each with a **path scope** (directory or known module root) when possible. |
| **Files read in full** (or large chunks) for T1 | **≤5** files, prioritizing paths **hinted by wiki**, **help**, **ADO**, or **stack traces** in the PFR. |
| **Lines / characters** pulled into the model from code | Keep each file read **bounded** (e.g. relevant symbol region); if file is huge, read **headers + search within file** instead of whole file. |

When the budget is hit without a T1 cite: stop code search, document in **`limitations`**, set **`human_review_required`** as appropriate, and prefer **`recommended_next_action`**: `escalate_to_pm_or_tc` or `request_more_detail_from_reporter` rather than silent guessing.

---

## 4. When to pay for T1 early

Worth **earlier** code spend (small scoped read) when:

- PFR alleges a **specific bug or regression** (narrow file likely).  
- **Impacted Module** + keywords map to a **known subsystem path** in the repo.  
- Wiki/help **contradict** each other — T1 resolves.

Defer code when:

- Wiki + help + closed ADO already give a **clear** `already_supported` with two T2 lines.  
- Question is **purely process** (“how do I register a PFR?”).

---

## 5. Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-04-29 | Initial staged retrieval, cost table, code caps |

---

**File:** `PFR skill/pfr_evidence_retrieval_cost_strategy.md`
