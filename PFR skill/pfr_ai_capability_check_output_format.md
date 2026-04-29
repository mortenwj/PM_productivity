# PFR AI capability check — recommended output format

**Purpose:** Machine- and human-consumable results for the **Standard capability check**, aligned with common **production LLM** and **RAG** guidance: **schema-first** outputs, **enums** for controlled vocabulary, **explicit evidence**, **confidence separate from outcome**, and **human review** flags when evidence is thin.

**Related:** `.cursor/skills/pfr-ai-capability-check/SKILL.md` (binds this document as **normative** for agent runs), `pfr_problem2_capability_knowledge_gap.md`

---

## 1. Practices to align with (short rationale)

| Practice | Why it matters for PFR | Further reading |
|----------|-------------------------|-----------------|
| **Schema-first / strict structured output** | Lets you validate parses, build dashboards, and version the contract without regex on free text. Industry write-ups emphasize **defining the JSON contract before prompts** and using **validator-constrained** APIs where available. | [LLM structured output: schema-first development](https://webcite.co/blog/llm-structured-output-schema-first-development/), [Structured outputs in production](https://tianpan.co/blog/2025-10-29-structured-outputs-llm-production) |
| **Structural validity ≠ factual correctness** | A valid JSON row can still be wrong about the product. Pipeline should be: **parse → validate schema → human or second source verifies claims**. | Same sources as above; OWASP LLM guidance on untrusted model output in applications |
| **Citations as first-class data** | Claims (“already supported in module X”) should carry **stable source IDs** and titles/URLs so humans can verify. RAG documentation stresses **citable units**, **consistent citation format**, and avoiding **only** post-hoc attribution where possible. | [OpenAI API: citation formatting](https://developers.openai.com/api/docs/guides/citation-formatting), [Cohere: RAG citations](https://docs.cohere.com/docs/rag-citations) |
| **Explicit uncertainty** | Risk-style frameworks use **confidence / evidence quality** and **assumptions** in the open. For PFR, map that to **`human_review_required`** and **`unknowns`**. | [PRA for AI workbook](https://pra-for-ai.github.io/pra/workbook.html) (structured assessment patterns) |

This document gives you a **single JSON object** (primary) plus an optional **Markdown summary** generated from the same fields (no drift).

---

## 2. Primary artifact: JSON (recommended)

### 2.1 Design rules

- **`schema_version`**: bump when you change fields (e.g. `"1.0.0"`).
- **Enums** for `outcome` and `confidence` — avoids ambiguous strings in WIQL exports later.
- **`claims`**: atomic statements the triager can verify; each claim lists `sources` (wiki, release note, ADO link).
- **`human_review_required`**: `true` if confidence is not high, or evidence is empty, or outcome is partial/gap with weak sources.
- **`model_and_tools`**: provenance for audit (model id if known, “MediaWiki MCP”, “ADO MCP”).

### 2.2 JSON Schema (Draft 2020-12 compatible)

Use this with validators (Pydantic, Zod, AJV) or with APIs that accept **JSON Schema** for structured output.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://local.dev/schemas/pfr-capability-check-v1.json",
  "title": "PFR capability check (AI-assisted)",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "work_item_project",
    "work_item_id",
    "assessed_at",
    "outcome",
    "confidence",
    "human_review_required",
    "claims",
    "evidence",
    "unknowns",
    "limitations",
    "model_and_tools"
  ],
  "properties": {
    "schema_version": {
      "type": "string",
      "const": "1.0.0"
    },
    "work_item_project": {
      "type": "string",
      "description": "Azure DevOps project name, e.g. 360"
    },
    "work_item_id": {
      "type": "integer",
      "minimum": 1
    },
    "assessed_at": {
      "type": "string",
      "format": "date-time",
      "description": "UTC ISO-8601 when the assessment was produced"
    },
    "outcome": {
      "type": "string",
      "enum": [
        "already_supported",
        "achievable_without_new_core",
        "partially_supported",
        "not_supported_product_gap",
        "insufficient_information"
      ]
    },
    "confidence": {
      "type": "string",
      "enum": ["high", "medium", "low"]
    },
    "human_review_required": {
      "type": "boolean"
    },
    "human_review_reason": {
      "type": "string",
      "description": "Required when human_review_required is true"
    },
    "underlying_need_summary": {
      "type": "string",
      "maxLength": 2000,
      "description": "Neutral restatement of the job-to-be-done"
    },
    "impacted_module_inferred": {
      "type": ["string", "null"],
      "description": "Echo or infer from PFR fields; null if unknown"
    },
    "claims": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["id", "statement", "support"],
        "properties": {
          "id": { "type": "string", "pattern": "^C-[0-9]+$" },
          "statement": { "type": "string", "maxLength": 500 },
          "support": {
            "type": "string",
            "enum": ["documented_in_source", "inferred", "uncited"]
          },
          "sources": {
            "type": "array",
            "items": { "$ref": "#/$defs/source_ref" }
          }
        }
      }
    },
    "evidence": {
      "type": "array",
      "description": "Distinct sources consulted (dedupe)",
      "items": { "$ref": "#/$defs/source_ref" }
    },
    "unknowns": {
      "type": "array",
      "items": { "type": "string", "maxLength": 500 }
    },
    "limitations": {
      "type": "string",
      "maxLength": 2000,
      "description": "What was not verified (versions, toggles, tenant config)"
    },
    "recommended_next_action": {
      "type": "string",
      "enum": [
        "paste_into_devops_description",
        "request_more_detail_from_reporter",
        "escalate_to_pm_or_tc",
        "candidate_close_as_standard",
        "no_change_pending_human"
      ]
    },
    "model_and_tools": {
      "type": "object",
      "additionalProperties": false,
      "required": ["components"],
      "properties": {
        "components": {
          "type": "array",
          "items": { "type": "string" },
          "description": "e.g. cursor-agent, ado-mcp, mediawiki-mcp"
        },
        "model_label": { "type": ["string", "null"] }
      }
    }
  },
  "$defs": {
    "source_ref": {
      "type": "object",
      "additionalProperties": false,
      "required": ["source_id", "kind", "title"],
      "properties": {
        "source_id": {
          "type": "string",
          "description": "Stable within this JSON doc, e.g. SRC-1"
        },
        "kind": {
          "type": "string",
          "enum": ["mediawiki", "ado_work_item", "release_note_url", "repo_file", "other"]
        },
        "title": { "type": "string" },
        "url": { "type": ["string", "null"], "format": "uri" },
        "wiki_page_title": { "type": ["string", "null"] },
        "excerpt": { "type": ["string", "null"], "maxLength": 800 }
      }
    }
  }
}
```

**Validation rule (business logic, not in JSON Schema):** set `human_review_required` to `true` when any of:

- `confidence` ∈ {`medium`, `low`}  
- `outcome` = `insufficient_information`  
- every `claims[].support` is `uncited` or `inferred`  
- `evidence` is empty

---

## 3. Secondary artifact: Markdown (for Azure DevOps Description)

Generate Markdown **from the JSON** so humans never edit two divergent truths.

Suggested section:

```markdown
## Standard capability check (AI-assisted)

| Field | Value |
|-------|--------|
| **Outcome** | already_supported \| achievable_without_new_core \| partially_supported \| not_supported_product_gap \| insufficient_information |
| **Confidence** | high \| medium \| low |
| **Human review required** | yes / no |
| **Assessed at** | 2026-04-29T12:00:00Z |

### Underlying need
…

### Claims (verify before closing)
1. [C-1] … — *support:* documented_in_source — *sources:* SRC-1, SRC-2  
2. [C-2] …

### Evidence consulted
- **SRC-1** (mediawiki): [[Page title]] — …  
- **SRC-2** (ado_work_item): Feature 12345 — …

### Unknowns / questions for reporter
- …

### Limitations (what AI did not verify)
- …
```

---

## 4. Optional: store JSON on the work item

- **Attachment** (`.json`) on the Feature — preserves audit without stuffing Description.  
- Or a **single-line** `System.Tags` token only for filtering (e.g. `AICapCheck-v1`) plus full JSON in attachment.

---

## 5. Versioning

- Bump **`schema_version`** / `$id` when fields change.  
- Keep **older schema files** in git for replaying historical attachments.

---

**File:** `PFR skill/pfr_ai_capability_check_output_format.md`  
**Last updated:** 2026-04-29
