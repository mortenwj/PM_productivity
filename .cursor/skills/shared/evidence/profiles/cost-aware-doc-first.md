# Profile: cost-aware-doc-first

**Id:** `profile:cost-aware-doc-first`  
**Used by:** `pfr-ai-capability-check` (after PFR-specific **stage 0** ingestion — see [`pfr-ai-capability-check/references/pfr_evidence_retrieval_cost_strategy.md`](../../../pfr-ai-capability-check/references/pfr_evidence_retrieval_cost_strategy.md)).

**Evidence semantics:** **[`../evidence-playbook.md`](../evidence-playbook.md)** is authoritative for **verified**, **lead**, **inferred**, **confidence**, **when to stop**, **conflicts**, and **documentation coverage** (§8). **T1–T4** tier meanings and JSON rules: **`pfr-ai-capability-check/references/pfr_evidence_sources_credibility.md`** and **`pfr-ai-capability-check/references/pfr_ai_capability_check_output_format.md`**.

**Related files:** [`../budgets.md`](../budgets.md), [`../ratatoskr-preflight.md`](../ratatoskr-preflight.md), [`../sources-and-tools.md`](../sources-and-tools.md), [`../verification-and-leads.md`](../verification-and-leads.md).

---

## 1. Relative cost (qualitative)

Higher = more tokens, latency, or tool volume. Use this to **order retrieval** only, not to redefine **credibility tiers** (see PFR credibility doc).

| Source / action | Typical relative cost | Notes |
|-----------------|------------------------|--------|
| Work item / request fields already retrieved (`wit_get_work_item`, batch) | **Lowest** | PFR: always complete stage 0 before external search; no extra search for that body. |
| **Internal MediaWiki** — targeted `mediawiki_search` / `mediawiki_get_page` for a few pages | **Low–medium** | Bounded by [`../budgets.md`](../budgets.md). |
| **Ratatoskr** — `search_topics`, `read_topic` for a small set of help topics | **Medium** | Cap **topics read** per [`../budgets.md`](../budgets.md). |
| **Azure DevOps** — WIQL / get related / batch by id for a handful of items | **Low–medium** | Cheap if **top N** and **specific fields**; expensive if huge descriptions in batch. |
| **Repo / code** — `grep` / semantic search over **wide** paths, or many large files | **High** | Dominates token use if unconstrained. |
| **Deep code exploration** — many files, cross-service tracing | **Very high** | Reserve for **ambiguous** outcomes or **high-stakes** items when user explicitly asks. |

**Cost vs trust:** **Cost** (this table) = **in what order** to try sources and **when to stop** for budget. **Trust** (T1–T4, **verified** material, **confidence**) = **`evidence-playbook.md`** + PFR skill docs.

---

## 2. Staged retrieval (default waterfall)

Execute **in order** (after PFR **stage 0** when applicable). **Stop early** when both are true: (1) [`../budgets.md`](../budgets.md) and this §2, (2) **sufficiency / defensibility** per **`evidence-playbook.md`** §6 **and** `pfr_evidence_sources_credibility.md` / `pfr_ai_capability_check_output_format.md` (including `human_review_required` / `limitations`).

| Stage | Action | Stop if |
|-------|--------|--------|
| **1** | **MediaWiki:** 1–3 focused searches → fetch **≤5** high-value pages (prefer Release Information / module overview per `pfr_evidence_sources_credibility.md` §2.1) | Strong T2 answers “already documented standard” or proves gap is doc-only. |
| **2** | **Ratatoskr:** `search_topics` (and `read_topic` only for **≤3** hits) | Help confirms/denies user-visible behaviour for same need. |
| **3** | **ADO:** query **≤10** related IDs or one WIQL with small `top`; prefer **closed** items for shipped claims | Closed item + wiki/help already support dual-T2 narrative. |
| **4** | **Code (T1):** only if stages 1–3 **do not** support a confident classification **or** user asks for code proof | **Scoped only** ([`../budgets.md`](../budgets.md)); never “read the whole repo.” |

If stage 4 is skipped, state in **`limitations`** (e.g. no source code retrieved). Apply the **strict gate** for `already_supported` / `achievable_without_new_core` per PFR credibility doc.

---

## 3. When to pay for T1 early

Worth **earlier** code spend (small scoped read) when:

- PFR alleges a **specific bug or regression** (narrow file likely).  
- **Impacted Module** + keywords map to a **known subsystem path** in the repo.  
- Wiki/help **contradict** each other — resolve per **`evidence-playbook.md`** §7 and PFR credibility doc.

Defer code when:

- Wiki + help + closed ADO already give a **clear** `already_supported` with two T2 lines.  
- Question is **purely process** (“how do I register a PFR?”).

---

**File:** `shared/evidence/profiles/cost-aware-doc-first.md`
