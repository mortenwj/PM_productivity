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

Support **problem 2** from the PFR initiative: Public 360° is large; consultants and customers often request something that is **already supported or achievable without new core code**, but phrased as a product gap. This skill defines how the agent **uses AI (and tools) to pre-check** that gap and produce the **Standard capability check** content intended to live on the **Azure DevOps Feature** (see `PFR skill/pfr_problem2_capability_knowledge_gap.md`).

This skill is **not** a substitute for PM or architecture sign-off. It **accelerates** the gate and **documents evidence** for humans.

## Normative output (always use this)

**Read and follow** `PFR skill/pfr_ai_capability_check_output_format.md` on every run, and **`PFR skill/pfr_evidence_sources_credibility.md`** when assigning **`credibility_tier`** (T1–T4) to each `source_ref` and when mapping tiers to `claims[].support` and overall `confidence`. **T1 is canonical product *source code*** (ground truth); official wiki and release notes are **T2** unless the credibility doc specifies otherwise. Prefer **`kind`: `source_code`** with path and commit or tag in `title`, `url`, or `excerpt` when citing implementation. Do not invent an alternate JSON shape or a free-form-only answer. Use **`schema_version` `1.2.1`** in emitted JSON.

Deliverables, in order:

1. **One JSON object** that conforms to the schema in that file (`schema_version` through `model_and_tools`, including every **required** top-level key).  
2. **One Markdown block** for pasting into Azure DevOps Description, **generated only from** that JSON (table + sections as in the format doc).  
3. Apply the **human review rules** from `pfr_ai_capability_check_output_format.md` **and** `pfr_evidence_sources_credibility.md`: set `human_review_required` to `true` when confidence is `medium` or `low`, when `outcome` is `insufficient_information`, when `evidence` is empty, when **no T1 code and no T2** sources exist, when `outcome` is `already_supported` or `achievable_without_new_core` but **no T1** and **fewer than two** independent **T2** (strict gate), when every claim has `support` ∈ {`inferred`, `uncited` only}, when any `documented_in_source` claim violates the **T1 code or dual-T2** rule, or when partial/gap outcomes lack defensible sources — and set **`human_review_reason`** whenever `human_review_required` is `true`.

**Outcome enum (JSON, exactly one):** `already_supported` | `achievable_without_new_core` | `partially_supported` | `not_supported_product_gap` | `insufficient_information` — map prose from the gate doc to these snake_case values.

**Confidence enum (JSON):** `high` | `medium` | `low` (lowercase strings only).

**Claims:** use ids `C-1`, `C-2`, …; each claim must include `statement`, `support`, and `sources` when `support` is `documented_in_source` (**T1 code** or **two independent T2** per credibility doc). **Evidence** array: deduplicated `source_ref` entries with stable `source_id` values (`SRC-1`, …); order **T1 → T2 → T3**.

**`recommended_next_action`:** set per the enum in the format doc (e.g. `paste_into_devops_description`, `escalate_to_pm_or_tc`, `request_more_detail_from_reporter`).

Optional: attach the JSON file to the work item for audit, as described in the format doc.

## When to apply

- User references a **PFR Feature ID** or paste of title/description, or asks to screen the Product First board item.
- User asks: “Is this already in the product?”, “Capability check”, “pre-flight PFR”, “AI triage for PFR”.

## Primary references (read as needed)

| Artifact | Path |
|----------|------|
| Gate definition and DevOps enforcement | `PFR skill/pfr_problem2_capability_knowledge_gap.md` |
| **Output format (JSON Schema + Markdown)** | `PFR skill/pfr_ai_capability_check_output_format.md` |
| **Evidence sources + tier rules (T1–T4)** | `PFR skill/pfr_evidence_sources_credibility.md` |
| Wiki process summary | `PFR skill/wiki_investigation_product_first_request.md` |
| PFR field patterns (sample) | `PFR skill/ado_pfr_sample_40_analysis.md` |
| Longer wiki extract (if present) | `reference/mediawiki_extract.md` |

## Workflow

1. **Ingest the PFR**  
   Use the **Azure DevOps** MCP: read tool schemas, then fetch the work item (`wit_get_work_item` or `wit_get_work_items_batch_by_ids`) for project **`360`**. Collect at least: `System.Title`, `System.Description`, `System.Tags`, `Custom.ImpactedModule`, `Custom.Source`, `Custom.Customername`, `Microsoft.VSTS.Common.Priority`, `System.State`, `System.Id`.

2. **Extract the underlying need**  
   From title + description, state in plain language: **user goal**, **constraints**, **product area** (guess allowed; mark uncertainty).

3. **Ground in sources (required attempt)**  
   - Use **MediaWiki** MCP: search the wiki for distinctive terms (module names, IFAR, eArchive, Plan&Build, feature names). Prefer **Release Information** and **module overview** pages when relevant (see `pfr_evidence_sources_credibility.md` §2.1).  
   - Use **Ratatoskr** MCP (`user-ratatoskr`): search/read **360 Online help** (release topics, admin docs) for user-visible behaviour; cite as **`kind`: `help_360`**, tier **T2** (check tool schema before calling).  
   - Use **Azure DevOps** MCP for **related** work items: distinguish **closed/delivered** (**T2**) vs **open/planned** (**T3**); copy **State**, **Target Date**, **Tags** (e.g. Commitment) into `source_ref.excerpt` when citing.  
   - Optionally grep this repo for snippets that disambiguate the same topic.  
   If no relevant sources are found, say so explicitly.

4. **Classify outcome**  
   Choose exactly one JSON `outcome` (see enums above), aligned with `pfr_problem2_capability_knowledge_gap.md`: already supported; achievable without new core; partial gap; true product gap; or insufficient information when the PFR body cannot be interpreted.

5. **Build `claims`, `evidence`, `unknowns`, `limitations`**  
   Per `pfr_ai_capability_check_output_format.md` and **`pfr_evidence_sources_credibility.md`**: cite **implementation** with **`source_code`** (or `repo_file`/`github` at **T1**) when claiming shipped behaviour; cite wiki/release/ADO at **T2**. Every `source_ref` includes **`credibility_tier`**; order `evidence` T1→T2→T3; do not list T4 as evidence. If code was not retrieved, say so in `limitations` and apply the **no-T1 strict gate** for “already standard” outcomes. Atomic claims with `support` and `sources` consistent with tier rules; deduplicated evidence list; explicit unknowns and limitations (branch, toggles, tenant config).

6. **Set `confidence`, `human_review_required`, `human_review_reason`, `recommended_next_action`**  
   Apply the format doc rules; fill `underlying_need_summary` and `impacted_module_inferred` when possible. Set `assessed_at` to UTC ISO-8601. Set `model_and_tools.components` (e.g. `ado-mcp`, `mediawiki-mcp`, `cursor-agent`).

7. **Emit deliverables**  
   Output the **JSON** first (single fenced code block), then the **Markdown** Description block (second fenced block), both consistent with the same assessment.

8. **Safety and honesty**  
   - Do **not** fabricate version numbers, toggles, or undocumented APIs.  
   - If the description is empty or GDPR-referenced only, set `outcome` to **`insufficient_information`**, `confidence` to **`low`**, populate **`unknowns`** with exact questions for the reporter, and set **`human_review_required`** true with a clear **`human_review_reason`**.  
   - Do **not** use wiki MCP **edit** tools to change process pages unless the user explicitly asks and follows preview/consent rules.

## Handoff to humans

- **High confidence + Already supported or Config-only:** suggest closing or redirecting with a **clear customer-facing explanation** path (per wiki); still recommend a named human signs off.  
- **Medium/Low or Partial/Gap:** assign or @mention the appropriate role per wiki RACI; keep the Feature in **New** until a person validates the AI block.

## Relation to other skills

- **`pm-ado-work-item-authoring`**: authoring and story quality for Epics/Features/User Stories; use that when **creating** or **rewriting** backlog text, not for capability grounding alone.  
- **`ado-user-story-quality`**: rubric for User Stories, not PFR Features.

## Maintenance

When wiki URLs, PFR fields, or the Feature template change, update **`PFR skill/`** specs first, then adjust this skill in one pass.
