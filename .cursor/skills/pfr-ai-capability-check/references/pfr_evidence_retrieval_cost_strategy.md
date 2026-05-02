# PFR capability check — evidence retrieval cost (tokens / compute)

**Purpose:** Keep AI-assisted capability checks **affordable and predictable**. **T1 source code is ground truth**, but **unbounded code search** burns context fast and is usually unnecessary if **T2** docs already answer the question.

**Normative for:** `.cursor/skills/pfr-ai-capability-check/SKILL.md` (**stage 0** below; **stages 1–4** and numeric budgets via **`shared/evidence/`**), alongside **`pfr_evidence_sources_credibility.md`**.

**Shared mechanics (stages 1–4, relative cost ordering, code exploration caps, when to pay for T1 early):**  
[`shared/evidence/README.md`](../../shared/evidence/README.md), profile **`profile:cost-aware-doc-first`** in [`shared/evidence/profiles/cost-aware-doc-first.md`](../../shared/evidence/profiles/cost-aware-doc-first.md), and [`shared/evidence/budgets.md`](../../shared/evidence/budgets.md). Ratatoskr preflight and tool hygiene: [`shared/evidence/ratatoskr-preflight.md`](../../shared/evidence/ratatoskr-preflight.md), [`shared/evidence/sources-and-tools.md`](../../shared/evidence/sources-and-tools.md); leads vs verification: [`shared/evidence/verification-and-leads.md`](../../shared/evidence/verification-and-leads.md).

**Stop early** when an outcome is already defensible under **`pfr_evidence_sources_credibility.md`** and **`pfr_ai_capability_check_output_format.md`** (including **`human_review_required`** / **`limitations`**).

---

## Stage 0 (PFR only, before shared profile stages 1–4)

| Stage | Action | Stop if |
|-------|--------|--------|
| **0** | Parse PFR **title, description, tags, Impacted Module, Source** | Empty body → outcome `insufficient_information`, list `unknowns`; still cheap. |

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-04-29 | Initial staged retrieval, cost table, code caps |
| 1.1 | 2026-05-02 | Stages 1–4 and shared budgets relocated to **`shared/evidence/`**; this file retains **PFR-specific stage 0** and pointers to the shared profile |

---

**File:** `pfr-ai-capability-check/references/pfr_evidence_retrieval_cost_strategy.md`
