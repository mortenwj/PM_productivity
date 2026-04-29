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

4. **Classify outcome (exactly one)**  
   Map to the four outcomes in `pfr_problem2_capability_knowledge_gap.md`:

   - **Already supported** — cite *where* (wiki page title, section concept, or release note if known).  
   - **Achievable without new core code** — configuration, case model, integration, supported extension; cite evidence or mark “hypothesis — TC/PM must confirm”.  
   - **Partially supported** — what exists + what is still missing.  
   - **Not supported (product gap)** — why standard paths do not cover it.

5. **Confidence**  
   Assign **High / Medium / Low** with one sentence. **Low** must default to recommending **human** (solution consultant, TC, or PM from Product teams) before any “close as duplicate of standard” recommendation.

6. **Output (always)**  
   Follow **`PFR skill/pfr_ai_capability_check_output_format.md`**: emit **(B) JSON** validating against the documented schema (enums, `claims`, `evidence`, `unknowns`, `limitations`, `human_review_required`), then **(A) Markdown** for the DevOps Description generated **from that JSON** so the human view and machine artifact stay aligned.

7. **Safety and honesty**  
   - Do **not** fabricate version numbers, toggles, or undocumented APIs.  
   - If the description is empty or GDPR-referenced only, set outcome to **insufficient information**, confidence **Low**, and list **exact questions** for the reporter.  
   - Do **not** use wiki MCP **edit** tools to change process pages unless the user explicitly asks and follows preview/consent rules.

## Handoff to humans

- **High confidence + Already supported or Config-only:** suggest closing or redirecting with a **clear customer-facing explanation** path (per wiki); still recommend a named human signs off.  
- **Medium/Low or Partial/Gap:** assign or @mention the appropriate role per wiki RACI; keep the Feature in **New** until a person validates the AI block.

## Relation to other skills

- **`pm-ado-work-item-authoring`**: authoring and story quality for Epics/Features/User Stories; use that when **creating** or **rewriting** backlog text, not for capability grounding alone.  
- **`ado-user-story-quality`**: rubric for User Stories, not PFR Features.

## Maintenance

When wiki URLs, PFR fields, or the Feature template change, update **`PFR skill/`** specs first, then adjust this skill in one pass.
