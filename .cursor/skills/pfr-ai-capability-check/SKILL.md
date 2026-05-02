---
name: pfr-ai-capability-check
description: >-
  Runs an AI-assisted standard capability check on Public 360° Product First
  Request (PFR) Features in Azure DevOps: fetches the work item, grounds findings
  in wiki/MediaWiki and product repo (code as T1 evidence) where possible, and emits a structured
  capability outcome plus a paste-ready Description block. Use when the user
  asks for a PFR capability check, AI screening of a PFR, pre-triage before PM,
  or “do we already support this” for a DevOps Feature under Product First Requests.
---

# PFR — AI-assisted standard capability check

## Purpose

Support **problem 2** from the PFR initiative: Public 360° is large; consultants and customers often request something that is **already supported or achievable without new core code**, but phrased as a product gap. This skill defines how the agent **uses AI (and tools) to pre-check** that gap and produce the **Standard capability check** content intended to live on the **Azure DevOps Feature** (see `pfr-ai-capability-check/references/pfr_problem2_capability_knowledge_gap.md`).

This skill is **not** a substitute for PM or architecture sign-off. It **accelerates** the gate and **documents evidence** for humans.

## Normative output (always use this)

**Read and follow** `pfr-ai-capability-check/references/pfr_ai_capability_check_output_format.md` on every run, **`pfr-ai-capability-check/references/pfr_evidence_sources_credibility.md`** for **T1–T4**, **`pfr-ai-capability-check/references/pfr_evidence_retrieval_cost_strategy.md`** for **PFR stage 0** (ingestion), and **`shared/evidence/`** for **shared staged retrieval** — profile **`profile:cost-aware-doc-first`** in [`shared/evidence/profiles/cost-aware-doc-first.md`](../shared/evidence/profiles/cost-aware-doc-first.md) plus [`shared/evidence/README.md`](../shared/evidence/README.md), [`shared/evidence/budgets.md`](../shared/evidence/budgets.md), [`shared/evidence/ratatoskr-preflight.md`](../shared/evidence/ratatoskr-preflight.md), [`shared/evidence/sources-and-tools.md`](../shared/evidence/sources-and-tools.md), [`shared/evidence/verification-and-leads.md`](../shared/evidence/verification-and-leads.md), [`shared/evidence/evidence-playbook.md`](../shared/evidence/evidence-playbook.md) — for **stages 1–4, search budgets, and shared claim/evidence/confidence vocabulary** (do **not** run unbounded whole-repo code search by default). **T1 is canonical product *source code*** (ground truth); official wiki and release notes are **T2** unless the credibility doc specifies otherwise. Prefer **`kind`: `source_code`** with path and commit or tag in `title`, `url`, or `excerpt` when citing implementation. Do not invent an alternate JSON shape or a free-form-only answer. Use **`schema_version` `1.2.2`** in emitted JSON.

Deliverables, in order:

1. **One JSON object** that conforms to the schema in that file (`schema_version` through `model_and_tools`, including every **required** top-level key, including **`documentation_status`**).  
2. **One Markdown block** for pasting into Azure DevOps Description, **generated only from** that JSON (table + sections as in the format doc), including **Documentation coverage**, **Capability analysis** (with **Key implementation finding** when T1 exists — one plain-language line for non-developers), **Decision framing** (after Capability analysis; see format doc), **Outcome and confidence (rationale)**, **Recommended next steps** (Markdown-only bullets; see format doc), and tightened doc-gap wording when **`documentation_status`** is not **`well_documented`**.  
3. Apply the **human review rules** from `pfr_ai_capability_check_output_format.md` **and** `pfr_evidence_sources_credibility.md` (unchanged triggers): set `human_review_required` to `true` when confidence is `medium` or `low`, when `outcome` is `insufficient_information`, when `evidence` is empty, when **no T1 code and no T2** sources exist, when `outcome` is `already_supported` or `achievable_without_new_core` but **no T1** and **fewer than two** independent **T2** (strict gate), when **every** claim has `support` ∈ {`inferred`, `uncited` only}, when any `documented_in_source` claim violates the **T1 code or dual-T2** rule, or when partial/gap outcomes lack defensible sources — and set **`human_review_reason`** whenever `human_review_required` is `true`. **`high` confidence does not waive** other triggers (for example the “all claims inferred/uncited” rule).

**Outcome enum (JSON, exactly one):** `already_supported` | `achievable_without_new_core` | `partially_supported` | `not_supported_product_gap` | `insufficient_information` — map prose from the gate doc to these snake_case values.

**Confidence enum (JSON):** `high` | `medium` | `low` (lowercase strings only). **Calibration (PFR, aligns with `pfr_evidence_sources_credibility.md` §4 and `evidence-playbook.md` §5):** use **`high`** when **verified T1** directly establishes the dispositive implementation behaviour (for example optional filter vs no enforcement path), **independent T2** aligns with that reading, and **no verified conflict** exists — state residual integration/toggle/tenant uncertainty only in **`limitations`** (for example: “High confidence due to direct T1 implementation evidence confirming optional filtering rather than enforced visibility; residual uncertainty limited to integration-specific overrides not observed.”). Use **`medium`** when **T1 is missing** for the critical path, when the **enforcement** path is **not visible** in retrieved code, when T2–T1 conflict is unresolved, or when build/branch mismatch is material. Use **`low`** per existing thin-evidence rules.

**Documentation status enum (JSON):** `well_documented` | `partially_documented` | `missing_documentation` — calibrate from **verified** wiki/help and other **T2** official prose that *explains* the need (**not** from code alone, not from search snippets). Definitions and relationship to **confidence** / strict gates: **`../shared/evidence/evidence-playbook.md`** §8. When status is not **`well_documented`**, add concise doc-gap wording to **`limitations`** (**documented / not documented / why it matters for the decision**) and mirror it in the Markdown **Documentation coverage** subsection (cite **SRC-**\* where relevant).

**Claims:** use ids `C-1`, `C-2`, …; each claim must include `statement`, `support`, and `sources` when `support` is `documented_in_source` (**T1 code** or **two independent T2** per credibility doc). **Evidence** array: deduplicated `source_ref` entries with stable `source_id` values (`SRC-1`, …); order **T1 → T2 → T3**.

**`recommended_next_action`:** set per the **unchanged** enum in the format doc. The **Markdown** block must still add **2–4 concrete next-step bullets** under **Recommended next steps** (e.g. validate Responsible Unit usage, verify import-archive permission model, check related ADO ids, clarify expected behaviour with the reporter) so PMs get actions, not only the enum token.

Optional: attach the JSON file to the work item for audit, as described in the format doc.

## When to apply

- User references a **PFR Feature ID** or paste of title/description, or asks to screen the Product First board item.
- User asks: “Is this already in the product?”, “Capability check”, “pre-flight PFR”, “AI triage for PFR”.

## Primary references (read as needed)

| Artifact | Path |
|----------|------|
| Gate definition and DevOps enforcement | `pfr-ai-capability-check/references/pfr_problem2_capability_knowledge_gap.md` |
| **Output format (JSON Schema + Markdown)** | `pfr-ai-capability-check/references/pfr_ai_capability_check_output_format.md` |
| **Evidence sources + tier rules (T1–T4)** | `pfr-ai-capability-check/references/pfr_evidence_sources_credibility.md` |
| **Retrieval order + token / search budget** | `pfr-ai-capability-check/references/pfr_evidence_retrieval_cost_strategy.md` (stage 0); **`../shared/evidence/`** — profile **`profile:cost-aware-doc-first`** |
| Wiki process summary | `pfr-ai-capability-check/references/wiki_investigation_product_first_request.md` |
| PFR field patterns (sample) | `pfr-ai-capability-check/references/ado_pfr_sample_40_analysis.md` |
| Longer wiki extract (if present) | `../shared/evidence/mediawiki_extract.md` |
| **Shared evidence retrieval (mechanics)** | `../shared/evidence/README.md` |
| **Shared evidence vocabulary (claims, confidence, conflicts)** | `../shared/evidence/evidence-playbook.md` |

## Capability comparison (required reasoning — not new JSON fields)

Before locking **`outcome`** and **`confidence`**, structure the assessment for PMs:

1. **Observed capability** — What the product **actually** does today per **verified** evidence (**T1** code when read; **T2** wiki/help/release when read as full pages/topics, not snippets alone). Be specific (e.g. “web part offers filters X/Y”, “administrator setting Z”).  
2. **Required capability** — What the **PFR / underlying need** asks for, in neutral capability language (not only the customer’s frustration prose).  
3. **Gap analysis** — State whether observed and required are **equivalent**, **not equivalent**, or **unclear** given evidence. When you compare, **explicitly separate**  
   - **Filtering / configuration** (user or admin narrows lists, optional views, import rules that limit sources) from  
   - **Access control / enforced visibility** (who may see an item at all, server-side enforcement, tenant-wide guarantees).  
   Non-equivalence here often drives **`partially_supported`** vs **`not_supported_product_gap`**; do **not** soften **T1–T4** rules or **`human_review_required`** gates.

**PM-facing wording (Markdown + rationale strings):** Prefer precise language over vague “not equivalent” alone. When **T1 confirms** there is **no** server-side enforcement of the required access rule (or the implementation is **only** optional filters/configuration), say the product **does not enforce required behaviour** or **does not implement required behaviour** for that requirement — still grounded in cited lines. When T1 is **absent** for the enforcement question, keep softer language (“not shown equivalent”, “unclear”) and cap confidence per rules.

**`human_review_reason`** and **`limitations`** (JSON strings) should, when relevant, **one sentence** tie **`outcome`** / **`confidence`** to this comparison (e.g. “T1 shows org-unit narrowing **only when filters are applied**; PFR requires **recipient-only enforced visibility** — product **does not enforce** that behaviour → gap; **high** confidence with residual integration caveats in limitations.”).

**`claims[].support` (JSON schema unchanged):** Only **`documented_in_source`**, **`inferred`**, **`uncited`**. For claims resting on **PFR / ADO Feature text alone**, JSON remains **`inferred`** with **`ado_work_item` (T3)** sources when attached. For claims about **retrieval environment** (e.g. no product files in workspace), JSON remains **`inferred`**. In the **Markdown** “Claims” section, append a **visible prose label** after the JSON support value so PMs scan faster: **`(Markdown label: reported in PFR request)`** for PFR-sourced inferred claims, and **`(Markdown label: observed in environment)`** for environment/retrieval inferred claims — see **`evidence-playbook.md`** quick map.

## Decision framing (Markdown — required section)

Immediately after **Capability analysis**, include **Decision framing** (see `pfr_ai_capability_check_output_format.md` §3 template): branch on whether the interpreted PFR requirement is **enforced access control** vs **achievable via filtering/configuration only**, then give **one final interpretation sentence** tied to the chosen **`outcome`**.

## Related / duplicate work items (lightweight)

When WIQL or related queries return **other work item ids**, use **`wit_get_work_items_batch_by_ids`** (or equivalent) within **`budgets.md`** caps to fetch **titles (and states) for at least 2–3** ids. Summarize in **Markdown** (*Related ADO items*) and add a short line to **`unknowns`** or **`limitations`** if duplicates may exist. Do **not** expand into a full duplicate analysis unless the user asks.

## Workflow

1. **Ingest the PFR**  
   Use the **Azure DevOps** MCP: read tool schemas, then fetch the work item (`wit_get_work_item` or `wit_get_work_items_batch_by_ids`) for project **`360`**. Collect at least: `System.Title`, `System.Description`, `System.Tags`, `Custom.ImpactedModule`, `Custom.Source`, `Custom.Customername`, `Microsoft.VSTS.Common.Priority`, `System.State`, `System.Id`.

2. **Extract the underlying need**  
   From title + description, state in plain language: **user goal**, **constraints**, **product area** (guess allowed; mark uncertainty).

3. **Ground in sources (cost-aware, required attempt)**  
   Complete **stage 0** (parse PFR body) per **`pfr-ai-capability-check/references/pfr_evidence_retrieval_cost_strategy.md`**, then run **`profile:cost-aware-doc-first`** per **`shared/evidence/profiles/cost-aware-doc-first.md`** with caps in **`shared/evidence/budgets.md`**: cheap/bounded sources **first**, **T1 code last** unless already needed to resolve ambiguity (see **when to pay for T1 early** in that profile). Use **`shared/evidence/ratatoskr-preflight.md`** before relying on help text; use **`shared/evidence/sources-and-tools.md`**, **`shared/evidence/verification-and-leads.md`**, and **`shared/evidence/evidence-playbook.md`** for MCP hygiene, leads vs verified reads, and shared claim/evidence/confidence language (map to JSON per PFR docs). **Stop early** when T2 evidence already supports a defensible outcome under **`pfr-ai-capability-check/references/pfr_evidence_sources_credibility.md`** and **`pfr-ai-capability-check/references/pfr_ai_capability_check_output_format.md`**; record skipped T1 in **`limitations`** and apply strict-gate / `human_review_required` per credibility doc. If budget is exhausted without T1, document that and escalate via `recommended_next_action` rather than guessing.

4. **Classify outcome**  
   Choose exactly one JSON `outcome` (see enums above), aligned with `pfr_problem2_capability_knowledge_gap.md`: already supported; achievable without new core; partial gap; true product gap; or insufficient information when the PFR body cannot be interpreted. **Justify** the choice by referencing the **capability comparison** (observed vs required vs equivalent or not); see **Capability comparison** above.

5. **Build `claims`, `evidence`, `unknowns`, `limitations`, and `documentation_status`**  
   Per `pfr_ai_capability_check_output_format.md` and **`pfr_evidence_sources_credibility.md`**: cite **implementation** with **`source_code`** (or `repo_file`/`github` at **T1**) when claiming shipped behaviour **and** code was within retrieval budget; cite wiki/help/release/ADO at **T2**. Every `source_ref` includes **`credibility_tier`**; order `evidence` T1→T2→T3; do not list T4 as evidence. In **`limitations`**, note **retrieval budget** or **early stop** (e.g. no code read) when relevant; apply the **no-T1 strict gate** for “already standard” outcomes. Atomic claims with `support` and `sources` consistent with tier rules; deduplicated evidence list; explicit unknowns and limitations (branch, toggles, tenant config). Set **`documentation_status`** from **evidence-playbook** §8 using only **verified** reads (**§3–§4**) of **T2**-style sources (`mediawiki`, `help_360`, release notes as used); **do not** set **`well_documented`** from **leads** or code-only. **`documentation_status`** must stay **consistent** with what you put in **`limitations`** for doc gaps; it does **not** replace or relax **`human_review_required`** rules in the format doc.

6. **Set `confidence`, `human_review_required`, `human_review_reason`, `recommended_next_action`**  
   Apply the format doc rules and **§Confidence enum** calibration above; **`confidence`** rationale must reference the **same** observed-vs-required assessment and whether T1 **does or does not** show enforcement for access-style requirements. Fill `underlying_need_summary` and `impacted_module_inferred` when possible. Set `assessed_at` to UTC ISO-8601. Set `model_and_tools.components` (e.g. `ado-mcp`, `mediawiki-mcp`, `cursor-agent`).

7. **Emit deliverables**  
   Output the **JSON** first (single fenced code block), then the **Markdown** Description block (second fenced block), both consistent with the same assessment.

8. **Safety and honesty**  
   - Do **not** fabricate version numbers, toggles, or undocumented APIs.  
   - If the description is empty or GDPR-referenced only, set `outcome` to **`insufficient_information`**, `confidence` to **`low`**, populate **`unknowns`** with exact questions for the reporter, and set **`human_review_required`** true with a clear **`human_review_reason`**.  
   - Do **not** use wiki MCP **edit** tools to change process pages unless the user explicitly asks and follows preview/consent rules.

## Product source code — read-only (non-negotiable)

This skill **reads** canonical product **T1** repositories (for example **`te-industry-public360/core-bl`** and siblings) **only** for evidence: **local** `Read` / `Grep` / scoped search, or **`gh`** **read** operations (e.g. `gh search code`, `gh api repos/.../contents/...`, `gh api search/code`).  

**Under no circumstances** may runs of this skill **modify** product source code: **no** `Write` / `StrReplace` / `EditNotebook` on product trees, **no** commits, **no** pushes, **no** branches, **no** PRs, **no** `gh` mutating APIs (issues, PR create, repo edit, workflow dispatch, etc.). If the user asks to change product code during a capability check, **stop** and respond that implementation changes are **out of scope**; record intent in **`limitations`** or hand off to humans. **`PM_productivity`** own files (skills, scripts) are **not** “product T1” for this rule — the rule targets **Public 360° product** repositories cited as **T1**.

## Handoff to humans

- **High confidence + Already supported or Config-only:** suggest closing or redirecting with a **clear customer-facing explanation** path (per wiki); still recommend a named human signs off.  
- **Medium/Low or Partial/Gap:** assign or @mention the appropriate role per wiki RACI; keep the Feature in **New** until a person validates the AI block.

## Relation to other skills

- **`pm-ado-work-item-authoring`**: authoring and story quality for Epics/Features/User Stories; use that when **creating** or **rewriting** backlog text, not for capability grounding alone.  
- **`ado-user-story-quality`**: rubric for User Stories, not PFR Features.

## Maintenance

When wiki URLs, PFR fields, or the Feature template change, update **`pfr-ai-capability-check/references/`** specs first, then adjust this skill in one pass.
