---
name: pfr-ai-capability-check
description: >-
  Runs an AI-assisted standard capability check on Public 360° Product First
  Request (PFR) Features in Azure DevOps: fetches the work item, grounds findings
  in wiki/MediaWiki and repo references where possible, and emits a structured
  capability outcome plus a paste-ready Description block. Use when the user
  asks for a PFR capability check, AI screening of a PFR, pre-triage before PM,
  or “do we already support this” for a DevOps Feature under Product First Requests.
---

# PFR — AI-assisted standard capability check

## Purpose

Support **problem 2** from the PFR initiative: Public 360° is large; consultants and customers often request something that is **already supported or achievable without new core code**, but phrased as a product gap. This skill defines how the agent **uses AI (and tools) to pre-check** that gap and produce the **Standard capability check** content intended to live on the **Azure DevOps Feature** (see `PFR skill/pfr_problem2_capability_knowledge_gap.md`).

This skill is **not** a substitute for PM or architecture sign-off. It **accelerates** the gate and **documents evidence** for humans.

## Normative output (always use this)

**Read and follow** `PFR skill/pfr_ai_capability_check_output_format.md` on every run. Do not invent an alternate JSON shape or a free-form-only answer.

Deliverables, in order:

1. **One JSON object** that conforms to the schema in that file (`schema_version` through `model_and_tools`, including every **required** top-level key).  
2. **One Markdown block** for pasting into Azure DevOps Description, **generated only from** that JSON (table + sections as in the format doc).  
3. Apply the **human review rule** from the format doc: set `human_review_required` to `true` when confidence is `medium` or `low`, when `outcome` is `insufficient_information`, when `evidence` is empty, when every claim has `support` ∈ {`inferred`, `uncited` only}, or when partial/gap outcomes lack `documented_in_source` claims — and set **`human_review_reason`** whenever `human_review_required` is `true`.

**Outcome enum (JSON, exactly one):** `already_supported` | `achievable_without_new_core` | `partially_supported` | `not_supported_product_gap` | `insufficient_information` — map prose from the gate doc to these snake_case values.

**Confidence enum (JSON):** `high` | `medium` | `low` (lowercase strings only).

**Claims:** use ids `C-1`, `C-2`, …; each claim must include `statement`, `support`, and `sources` when `support` is `documented_in_source`. **Evidence** array: deduplicated `source_ref` entries with stable `source_id` values (`SRC-1`, …).

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
| Wiki process summary | `PFR skill/wiki_investigation_product_first_request.md` |
| PFR field patterns (sample) | `PFR skill/ado_pfr_sample_40_analysis.md` |
| Longer wiki extract (if present) | `reference/mediawiki_extract.md` |

## Workflow

1. **Ingest the PFR**  
   Use the **Azure DevOps** MCP: read tool schemas, then fetch the work item (`wit_get_work_item` or `wit_get_work_items_batch_by_ids`) for project **`360`**. Collect at least: `System.Title`, `System.Description`, `System.Tags`, `Custom.ImpactedModule`, `Custom.Source`, `Custom.Customername`, `Microsoft.VSTS.Common.Priority`, `System.State`, `System.Id`.

2. **Extract the underlying need**  
   From title + description, state in plain language: **user goal**, **constraints**, **product area** (guess allowed; mark uncertainty).

3. **Ground in sources (required attempt)**  
   - Use **MediaWiki** MCP: search the wiki for distinctive terms (module names, IFAR, eArchive, Plan&Build, feature names). Prefer official process and module pages over guesswork.  
   - Optionally grep this repo for ADO/wiki snippets that disambiguate the same topic.  
   If no relevant pages are found, say so explicitly.

4. **Classify outcome**  
   Choose exactly one JSON `outcome` (see enums above), aligned with `pfr_problem2_capability_knowledge_gap.md`: already supported; achievable without new core; partial gap; true product gap; or insufficient information when the PFR body cannot be interpreted.

5. **Build `claims`, `evidence`, `unknowns`, `limitations`**  
   Per `pfr_ai_capability_check_output_format.md`: atomic verifiable claims with `support` and `sources`; deduplicated evidence list; explicit unknowns and limitations (versions, toggles, tenant-specific config not verified).

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
