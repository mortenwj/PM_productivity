# PFR AI capability check — recommended output format

**Purpose:** Machine- and human-consumable results for the **Standard capability check**, aligned with common **production LLM** and **RAG** guidance: **schema-first** outputs, **enums** for controlled vocabulary, **explicit evidence**, **confidence separate from outcome**, and **human review** flags when evidence is thin.

**Related:** `.cursor/skills/pfr-ai-capability-check/SKILL.md` (binds this document as **normative** for agent runs), `pfr_problem2_capability_knowledge_gap.md`, **`../../shared/evidence/evidence-playbook.md`** (§8 **`documentation_status`**)

**Evidence credibility:** Every `source_ref` must include a **`credibility_tier`** (T1–T4). Definitions, `kind` → tier defaults, and rules linking tiers to `claims[].support` and overall `confidence` are in **`pfr_evidence_sources_credibility.md`** (read it when building `evidence` and `claims`).

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

- **`schema_version`**: bump when you change fields. Current contract: **`1.2.2`** (`credibility_tier`; **T1 = product code**; `source_code`, **`help_360`** kinds per `pfr_evidence_sources_credibility.md`; **`documentation_status`** per **`../../shared/evidence/evidence-playbook.md`** §8).
- **Enums** for `outcome` and `confidence` — avoids ambiguous strings in WIQL exports later.
- **`claims`**: atomic statements the triager can verify; each claim lists `sources` (wiki, release note, ADO link).
- **`human_review_required`:** Apply **only** the explicit triggers in **§2.2 validation rules** below (do **not** invent new ones). Note: **`high` confidence** does **not** automatically set `human_review_required` to `false` if another trigger still applies (for example **every** claim remains `inferred` or `uncited`).
- **`model_and_tools`**: provenance for audit (model id if known, “MediaWiki MCP”, “ADO MCP”).
- **Capability comparison (reasoning only; no extra JSON keys):** Before finalizing **`outcome`** and **`confidence`**, compare **observed capability** (from **T1/T2** evidence) to **required capability** (from the PFR / **`underlying_need_summary`**). State whether they are **equivalent**, **not equivalent**, or **unclear**. Explicitly distinguish **filtering / configuration** from **access control / enforced visibility** when both appear in the thread. **`human_review_reason`** and **`limitations`** should, when material, reference this comparison in **one clear sentence** without changing gate rules. When **T1** shows the product **does not** apply a required enforcement path (for example optional UI filters only), use explicit wording in Markdown / rationale: **does not enforce required behaviour** or **does not implement required behaviour** — not vague “not equivalent” alone. If T1 is **missing** for the enforcement question, keep softer language (“not shown equivalent”, “unclear”).
- **`confidence` calibration (PFR):** Use **`high`** when **verified T1** establishes the dispositive implementation fact, **≥1 independent T2** aligns with that reading, and **no verified conflict**; put residual integration/toggle/tenant caveats in **`limitations`** (and optionally one clause in **`human_review_reason`** only if review is still required for another trigger). Use **`medium`** when T1 is missing for the critical enforcement path, when enforcement is not visible in retrieved code, or when doc–code conflict is unresolved. See **`pfr_evidence_sources_credibility.md`** §4 and **`../../shared/evidence/evidence-playbook.md`** §5.
- **Markdown-only claim labels (schema unchanged):** JSON `claims[].support` stays **`documented_in_source` \| `inferred` \| `uncited`**. In the **Markdown** Claims list, for rows where JSON uses **`inferred`**, append **`(Markdown label: reported in PFR request)`** when the claim is grounded in **PFR / Feature description** (sources typically **T3** `ado_work_item`), or **`(Markdown label: observed in environment)`** when the claim describes **retrieval / workspace** facts (still JSON **`inferred`**). See **`../../shared/evidence/evidence-playbook.md`** quick map.
- **`recommended_next_action`:** Values remain the **fixed enum** below. **PM-facing detail** belongs in the **Markdown** block under **Recommended next steps** (2–4 bullets), not by inventing new enum values.
- **WIQL follow-up:** If a query returns other work item ids, batch-fetch **at least 2–3 titles** within default caps; note possible duplicates in **`limitations`** or **`unknowns`** and in Markdown.
- **T1 retrieval is read-only:** Evidence from product repos (local clone or GitHub/`gh`) must be **read-only** — **never** edit, commit, push, or open PRs against canonical product source as part of this capability check. See **`SKILL.md`** section **Product source code — read-only** and **`../../shared/evidence/sources-and-tools.md`** § GitHub / local code.

### 2.2 JSON Schema (Draft 2020-12 compatible)

Use this with validators (Pydantic, Zod, AJV) or with APIs that accept **JSON Schema** for structured output.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://local.dev/schemas/pfr-capability-check-v1.2.2.json",
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
    "documentation_status",
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
      "const": "1.2.2"
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
    "documentation_status": {
      "type": "string",
      "enum": [
        "well_documented",
        "partially_documented",
        "missing_documentation"
      ],
      "description": "Whether official wiki/help (T2-style) verified per evidence-playbook §3–§4 adequately explains the capability; orthogonal to outcome and confidence. See evidence-playbook §8."
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
      "required": ["source_id", "kind", "title", "credibility_tier"],
      "properties": {
        "source_id": {
          "type": "string",
          "description": "Stable within this JSON doc, e.g. SRC-1"
        },
        "kind": {
          "type": "string",
          "enum": [
            "source_code",
            "mediawiki",
            "help_360",
            "ado_work_item",
            "release_note_url",
            "repo_file",
            "github",
            "service_now",
            "other"
          ]
        },
        "credibility_tier": {
          "type": "string",
          "enum": ["T1", "T2", "T3", "T4"],
          "description": "See pfr_evidence_sources_credibility.md"
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
- **every** `evidence[].credibility_tier` is **`T3`** or **`T4`** (no **T1** code and no **T2** doc/delivery in the corpus)  
- any claim with `support` = `documented_in_source` violates the **T1 code or dual-T2** rule in `pfr_evidence_sources_credibility.md`  
- `outcome` ∈ {`already_supported`, `achievable_without_new_core`} and **no** evidence item has **`credibility_tier` `T1`**, and there are **fewer than two** independent **`T2`** sources — per strict gate in that file

**`documentation_status`:** Set from **verified** wiki/help (and other **T2** official prose you rely on for *explanation*), per **`../../shared/evidence/evidence-playbook.md`** §8. **Do not** use this field to bypass any rule above; **`well_documented`** does **not** imply `human_review_required` may be `false` when another trigger applies.

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
| **Documentation status** | well_documented \| partially_documented \| missing_documentation (per evidence-playbook §8; wiki/help T2 coverage for *explaining* the need, not product truth alone) |
| **Human review required** | yes / no |
| **Assessed at** | 2026-04-29T12:00:00Z |

### Documentation coverage
Short rationale tied to **verified** wiki/help (cite **SRC-**\*). If **`documentation_status`** is **`partially_documented`** or **`missing_documentation`**, use **three short sentences**: (1) **What is documented** (verified topics/pages). (2) **What is not documented** for this PFR decision (e.g. end-to-end behaviour, Swedish-specific flow, enforcement vs filter). (3) **Why that gap matters** for PM triage (e.g. cannot confirm equivalence to required capability from docs alone). Do not weaken strict gates on outcome.

### Capability analysis
- **Observed capability** — What the product **does** per **T1/T2** evidence (concise; cite **SRC-**\*).
- **Required capability** — What the PFR / underlying need **must** achieve (neutral capability wording).
- **Assessment** — One explicit line: **equivalent** → supports **`already_supported`** / **`achievable_without_new_core`** / **`partially_supported`** only when tier rules and gates allow; **not equivalent** → supports **`partially_supported`** or **`not_supported_product_gap`**; **unclear** → supports **`insufficient_information`** or lower **confidence**. Call out **filtering/configuration** vs **access control/enforced visibility** when both are in play. When **T1** confirms absence of enforcement (or only optional filters), prefer **does not enforce required behaviour** / **does not implement required behaviour** over vague “not equivalent” alone.
- **Key implementation finding** — If **T1** was read: one **non-developer** sentence summarising the decisive code fact (e.g. “Org-unit restriction applies only when the user has applied filters; the default query still returns every row the user may access under import-archive rules.”). Omit this bullet only if no T1 was retrieved.

### Decision framing
- **If the interpreted requirement is enforced access control** (only intended recipient unit may see the row, by default, for all users): state whether evidence shows a **product gap** — typically **`not_supported_product_gap`** when **T1** shows **no** such enforcement and **T2** does not contradict that reading.
- **If the interpreted requirement is achievable via filtering/configuration alone** (narrowing a shared list): state **`partially_supported`** or **`already_supported`** / **`achievable_without_new_core`** only when tier rules and strict gates allow — and if the **PFR still** asks for hard enforcement, state clearly that configuration **does not meet the stated need**.
- **Final interpretation** — One sentence: which branch applies **for this PFR** and how that maps to the JSON **`outcome`**.

### Underlying need
…

### Outcome and confidence (rationale)
One short paragraph: tie **`outcome`** and **`confidence`** to **Capability analysis** + **Decision framing**. When T1 supports it, say explicitly whether the product **does not enforce** / **does not implement** the required behaviour. For **`high`** confidence with strong T1+T2 alignment, you may add: *High confidence due to direct T1 implementation evidence …; residual uncertainty limited to …* (mirror **`limitations`**).

### Claims (verify before closing)
1. [C-1] … — *support:* documented_in_source — *sources:* SRC-1, SRC-2  
2. [C-2] … — *support:* inferred *(Markdown label: reported in PFR request)* — *sources:* SRC-4  
3. [C-3] … — *support:* inferred *(Markdown label: observed in environment)* — *sources:* (optional)

### Evidence consulted
- **SRC-1** (source_code, **T1**): `repo` / `path` @ `tag|commit` — …  
- **SRC-2** (mediawiki, **T2**): [[Page title]] — …

### Related ADO items (if queried)
If WIQL returned ids: list **2–3** `id — title — state` from batch fetch; one line whether they **look related** or **unclear**.

### Unknowns / questions for reporter
- …

### Limitations (what AI did not verify)
- …

### Recommended next steps
2–4 **actionable** bullets (configuration check, permission/import model, duplicate check with reporter, clarify expected behaviour, etc.). Maps to the JSON **`recommended_next_action`** enum but **expands** it for humans (do not add enum values).
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

**File:** `pfr-ai-capability-check/references/pfr_ai_capability_check_output_format.md`  
**Last updated:** 2026-05-02 (schema **1.2.2** unchanged; Markdown: **Key implementation finding**, **Decision framing**, **confidence** calibration note, T1-strong wording, **Markdown-only** inferred labels; JSON `claims[].support` enum unchanged)
