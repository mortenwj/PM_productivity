# Shared evidence retrieval (Public 360°)

**Purpose:** Single place for **how** agents search bounded corpora (wiki, help, ADO, code) and apply **call budgets**. This is **mechanics documentation**, not a runtime library.

**Authoritative semantics:** **[`evidence-playbook.md`](evidence-playbook.md)** defines **claim**, **evidence**, **verified** vs **lead** vs **inferred**, **verification**, **confidence** (high / medium / low), **when to stop searching**, and **conflicting evidence**. Read it before interpreting any other file in this folder that mentions those words.

**Normative precedence:**

- **Vocabulary** (verified, lead, confidence, claim, evidence, conflicts): **`evidence-playbook.md`**.
- **Numbers, stage order, tool hygiene:** this folder (`budgets.md`, `sources-and-tools.md`, `profiles/`, …). If a skill doc disagrees on **order or caps**, fix this folder.
- **PFR JSON, T1–T4 tiers, `human_review_required`, outcome enums:** **`pfr-ai-capability-check/references/pfr_evidence_sources_credibility.md`** and **`pfr-ai-capability-check/references/pfr_ai_capability_check_output_format.md`** (retrieval order here does **not** override tier rules).

## Which skills use which profile

| Skill | Profile | Also read |
|-------|---------|-----------|
| **`pfr-ai-capability-check`** | [`profiles/cost-aware-doc-first.md`](profiles/cost-aware-doc-first.md) | [`evidence-playbook.md`](evidence-playbook.md); stage **0** in [`pfr-ai-capability-check/references/pfr_evidence_retrieval_cost_strategy.md`](../../pfr-ai-capability-check/references/pfr_evidence_retrieval_cost_strategy.md); PFR skill credibility + output format. |
| **`lmwtfy`** | [`profiles/code-first-research.md`](profiles/code-first-research.md) | [`evidence-playbook.md`](evidence-playbook.md), [`budgets.md`](budgets.md), [`ratatoskr-preflight.md`](ratatoskr-preflight.md); tool names in `.cursor/skills/lmwtfy/rules/ratatoskr-mcp-tools.md`; output in `rules/lmwtfy-format.md`. |

## File index

| File | Contents |
|------|----------|
| [`evidence-playbook.md`](evidence-playbook.md) | **Authoritative** shared vocabulary: claim, evidence, verified / lead / inferred, verification, confidence, stop rules, conflicts |
| [`sources-and-tools.md`](sources-and-tools.md) | MCP servers, descriptor rule, GitHub / Grep / WebFetch |
| [`mediawiki_extract.md`](mediawiki_extract.md) | mediawiki_extract.md — structure and conventions for extracting and interpreting MediaWiki content |
| [`verification-and-leads.md`](verification-and-leads.md) | Checklists and anti-patterns (points to playbook for definitions) |
| [`ratatoskr-preflight.md`](ratatoskr-preflight.md) | Help center preflight, DNS failures, fallbacks |
| [`budgets.md`](budgets.md) | Numeric caps (wiki, topics, ADO, code) in one table |
| [`profiles/cost-aware-doc-first.md`](profiles/cost-aware-doc-first.md) | Doc-first waterfall + relative cost + T1 timing (PFR-aligned) |
| [`profiles/code-first-research.md`](profiles/code-first-research.md) | Code-first load order + extract list (lmwtfy / product-context) |

## Changelog (this folder)

| Version | Date | Change |
|---------|------|--------|
| 1.2 | 2026-05-02 | README: `evidence-playbook.md` as authoritative semantics; file index order; profile table links |
| 1.1 | 2026-05-02 | Added `evidence-playbook.md` |
| 1.0 | 2026-05-02 | Initial shared extraction from PFR retrieval strategy + lmwtfy context-assembly / SKILL |
