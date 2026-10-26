# Shared evidence retrieval (Public 360°)

**Purpose:** Single place for **how** agents search bounded corpora (wiki, help, ADO, code) and apply **call budgets**. This is **mechanics documentation**, not a runtime library.

**Authoritative semantics:** **[`evidence-playbook.md`](evidence-playbook.md)** defines **claim**, **evidence**, **verified** vs **lead** vs **inferred**, **verification**, **confidence** (high / medium / low), **when to stop searching**, and **conflicting evidence**. Read it before interpreting any other file in this folder that mentions those words.

**Normative precedence:**

- **Vocabulary** (verified, lead, confidence, claim, evidence, conflicts): **`evidence-playbook.md`**.
- **Numbers, stage order, tool hygiene:** this folder (`budgets.md`, `sources-and-tools.md`, `profiles/`, …). If a skill doc disagrees on **order or caps**, fix this folder.
- **PFR JSON, T1–T4 tiers, `human_review_required`, outcome enums:** **[`quality-gates/pfr-evidence-tiers.md`](../../quality-gates/pfr-evidence-tiers.md)** and **[`quality-gates/pfr-output-format.md`](../../quality-gates/pfr-output-format.md)** (retrieval order here does **not** override tier rules).

## Which skills use which profile

| Skill | Profile | Also read |
|-------|---------|-----------|
| **`pfr-capability-gate`** | [`profiles/cost-aware-doc-first.md`](profiles/cost-aware-doc-first.md) | [`evidence-playbook.md`](evidence-playbook.md); [`quality-gates/pfr-retrieval-strategy.md`](../../quality-gates/pfr-retrieval-strategy.md); [`quality-gates/pfr-evidence-tiers.md`](../../quality-gates/pfr-evidence-tiers.md); [`quality-gates/pfr-output-format.md`](../../quality-gates/pfr-output-format.md). |
| **`lmwtfy`** | [`profiles/code-first-research.md`](profiles/code-first-research.md) | [`evidence-playbook.md`](evidence-playbook.md), [`budgets.md`](budgets.md), [`ratatoskr-preflight.md`](ratatoskr-preflight.md); output in `skills/claude-code/lmwtfy/rules/lmwtfy-format.md`. |
| **`tender-response`** | [`profiles/tender-evidence.md`](profiles/tender-evidence.md) | [`evidence-playbook.md`](evidence-playbook.md), [`budgets.md`](budgets.md), [`ratatoskr-preflight.md`](ratatoskr-preflight.md); ledger and workflow in `tender-response/references/evidence-retrieval.md`. |

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
| [`profiles/tender-evidence.md`](profiles/tender-evidence.md) | Doc-first waterfall for tender/RFP answers (prior art → wiki → help → ADO → code) |

## Changelog (this folder)

| Version | Date | Change |
|---------|------|--------|
| 1.3 | 2026-07-07 | Added `profile:tender-evidence` for `tender-response` skill |
| 1.2 | 2026-05-02 | README: `evidence-playbook.md` as authoritative semantics; file index order; profile table links |
| 1.1 | 2026-05-02 | Added `evidence-playbook.md` |
| 1.0 | 2026-05-02 | Initial shared extraction from PFR retrieval strategy + lmwtfy context-assembly / SKILL |
