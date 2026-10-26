---
name: tender-response
description: >-
  Drafts, reviews, and structures tender/RFP requirement responses for Public 360°
  and Nordic public-sector procurements. Builds compliance matrices, applies win themes,
  writes evidence-backed answers in Norwegian or English, and flags gaps honestly.
  Retrieves evidence via prior bid library (docs/tender-reference), MediaWiki, Ratatoskr,
  using shared/evidence profile:tender-evidence. Use when the user mentions tender, anbud, RFP, RFQ, kravbesvarelse, compliance matrix,
  leverandørens besvarelse, requirement response, or bid/proposal writing.
allowed-tools: Read Write Grep Glob
category:
  - writing
  - productivity
---

# Tender requirement response

Guide drafting and review of **individual requirement answers** and **full bid packages** for Nordic public-sector tenders, aligned with market best practice and Tietoevry / Public 360° conventions in this repo.

## Core principles (market best practice)

1. **Compliance first** — Every mandatory requirement gets an owner, a response location, and a traceable answer. Missing a buried "shall" disqualifies more bids than weak prose.
2. **Win themes before words** — Agree 3–5 differentiators tied to evaluation criteria; thread them through every section so the bid reads as one argument.
3. **Evidence over assertion** — Claims must be supportable from product truth, help, wiki, certifications, or prior approved answers. Never invent capabilities.
4. **Mirror the buyer** — Use the customer's requirement ID, terminology, and section order. Lead with direct compliance, then proof.
5. **Honest gaps** — Flag partial compliance, alternatives, or customer responsibilities explicitly. Silence on a gap reads as dishonesty.
6. **Evaluator-friendly** — Scannable structure, explicit cross-references to attachments, consistent facts across all answers.

## Mode detection

| Mode | Indicators | Output |
|------|------------|--------|
| **Respond** | New requirement text, "draft answer for krav X" | Single or batch requirement response(s) |
| **Matrix** | Full RFP, "build compliance matrix", many requirements | Compliance matrix + draft plan |
| **Review** | Existing draft pasted or file path | Structured review checklist |
| **Gap analysis** | "Can we meet…", bid/no-bid, capability check | Compliance assessment per requirement |

If ambiguous, ask which mode. Default to **Respond** for a single requirement.

## Before writing (always)

### 1. Gather context (minimum)

Ask or infer:

- **Tender language** (Norwegian Bokmål default for NO public sector; English when RFP is EN)
- **Requirement ID(s)** and exact requirement text (verbatim)
- **Response format** mandated by buyer (table cell, free text, max length, attachment refs)
- **Deployment context** if relevant: SaaS (U), platform B, platform K, on-prem
- **Evaluation weight** if known (technical, security, price, etc.)

### 2. Shared evidence retrieval (Ratatoskr, wiki, code)

**Default:** Treat **`shared/evidence/`** plus **`profile:tender-evidence`** as the baseline retrieval path for any factual product, security, or process claim. **Do not** invent a parallel verification standard; **verified / lead / inferred / confidence** stay in **`shared/evidence/evidence-playbook.md`**.

**Load once per run (before MCP or GitHub):**

1. [`shared/evidence/README.md`](../shared/evidence/README.md) — confirms **`tender-response`** → **`profile:tender-evidence`**
2. [`shared/evidence/evidence-playbook.md`](../shared/evidence/evidence-playbook.md) — claim, evidence, confidence, conflicts
3. [`shared/evidence/budgets.md`](../shared/evidence/budgets.md) — caps (wiki pages, help topics, ADO, code)
4. [`shared/evidence/sources-and-tools.md`](../shared/evidence/sources-and-tools.md) — MCP servers, `gh`, repos
5. [`shared/evidence/verification-and-leads.md`](../shared/evidence/verification-and-leads.md) — ledger hygiene
6. [`shared/evidence/ratatoskr-preflight.md`](../shared/evidence/ratatoskr-preflight.md) — before Ratatoskr body text
7. [`shared/evidence/profiles/tender-evidence.md`](../shared/evidence/profiles/tender-evidence.md) — **normative load order**

**Default execution path (`profile:tender-evidence`):**

| Stage | Source | Purpose |
|-------|--------|---------|
| **0a** | **`docs/tender-reference/extracted/`** | **Prior bid answers (mandatory grep + read)** |
| **0b** | `docs/product/` + context files | Drafts, partial extracts, master context |
| **1** | **MediaWiki** (`user-mediawiki`) | Process, security, release, certifications |
| **2** | **Ratatoskr** (`user-ratatoskr`) | Customer-facing product/admin capabilities |
| **3** | **ADO** (`user-azure-devops`) | Shipped vs planned; commitment dates |
| **4** | **GitHub / code** (`gh`, Grep) | Verify behaviour when docs insufficient |

**Tender reference library:** [references/tender-reference-library.md](references/tender-reference-library.md) — always run **Stage 0a** before drafting.

**Unlike `lmwtfy`:** tender uses **doc-first** (wiki → help → code), not code-first. Use `lmwtfy` only for deep technical investigation; import verified facts into the tender ledger — do not paste colleague-answer prose into bid text.

**Ratatoskr tool order:** [references/ratatoskr-mcp-tools.md](references/ratatoskr-mcp-tools.md). **Full workflow + ledger:** [references/evidence-retrieval.md](references/evidence-retrieval.md).

If an MCP server is not configured, skip that source, record in the tender evidence ledger, and continue. Do not invent tool names — use `GetMcpTools` to discover schemas.

**Controlled extensions** (same bar as lmwtfy): declare in ledger what you did beyond the profile, why, and **Verified how** per playbook §4.

### 3. Local product context

| Source | Path |
|--------|------|
| Master product context | `docs/product/context/master-context.md` |
| AI governance (if AI/security krav) | `docs/product/context/ai-governance-principles.md` |
| Prior tender drafts | `docs/product/` (grep for requirement ID or topic) |

### 4. Win themes (batch or full bid only)

Before drafting multiple sections, propose **3–5 win themes**. Each theme must be:

- One memorable sentence
- Differentiating (not generic "quality" or "innovation")
- Aligned to stated evaluation criteria
- Supportable with evidence

Record themes and reference them in relevant answers. Skip for isolated single-krav drafts unless the user asks.

## Respond mode — single requirement workflow

### Step A: Parse the requirement

Extract and list:

- **Mandatory vs desirable** ("skal"/"må"/"shall"/"must" vs "bør"/"should"/"kan")
- **Sub-parts** (numbered bullets, scenarios, graded/ungraded splits)
- **Implicit asks** (evidence, attachments, competence level, process description)
- **Compliance level** target: Full | Partial | Alternative | Customer responsibility | Not applicable

### Step B: Decompose and retrieve evidence

1. List **verifiable claims** per sub-requirement (see [evidence-retrieval.md](references/evidence-retrieval.md)).
2. **Stage 0a (mandatory):** Grep and read `docs/tender-reference/extracted/` for this krav (see [tender-reference-library.md](references/tender-reference-library.md)).
3. Classify **krav type** (product / security / process / certification / roadmap).
4. Run **`profile:tender-evidence`** stages 0b–4 unless reusing confirmed prior art (spot-check still required).
5. Build **tender evidence ledger**; present to user: **"Evidence checks out? OK to draft final answer?"**

Skip MCP stages only when: matching text exists in **tender-reference** or `docs/product/` + user confirms reuse + spot-check passes.

### Step C: Build a mini compliance row

```
| Krav ID | Type | Compliance | Owner | Evidence needed | Response section |
```

### Step D: Draft the answer

Use the template that matches the buyer format. See [references/response-templates.md](references/response-templates.md).

**Default Norwegian structure** (when format is free text):

1. **Direct compliance statement** — First sentence answers yes/no/how, using buyer terms.
2. **How the requirement is met** — Product capability, process, or architecture; concrete not marketing.
3. **Evidence** — Certifications, help topics, attachment IDs, metrics (RTO, retention, etc.).
4. **Customer/Oppdragsgiver angle** — Benefits only when the RFP template asks for "fordeler"; otherwise keep brief.
5. **Gaps or conditions** — Partial compliance, roadmap, or split responsibility (especially B/K vs SaaS).

**English structure** — Same logic; use "Customer" / "Contracting Authority" per RFP.

### Step E: Self-check before presenting

Run the [Review checklist](#review-checklist) silently. Flag any failed items in the output.

### Step F: Save (when user confirms)

Save under `docs/product/` with naming:

```
Tender Response - [Tender or customer short name] - Krav [ID].md
```

For multi-krav batches:

```
Tender Response - [Tender short name] - Krav [ID range].md
```

## Matrix mode — compliance matrix workflow

Use when the user supplies a full requirement set or asks for bid planning.

1. **Extract** every requirement with ID, source section, and mandatory flag.
2. **Build matrix** using [references/compliance-matrix.md](references/compliance-matrix.md).
3. **Assign** compliance status per row: Met | Partial | Alternative | Gap | N/A.
4. **Never delete** a row you cannot meet — flag and plan response strategy.
5. **Propose win themes** and map which requirements each theme supports.
6. **Prioritize** drafting order: pass/fail items first, then highest evaluation weight.
7. **Output** matrix (markdown table) + gap summary + recommended next actions.

Treat amendments as living updates: add rows, do not silently drop changed requirements.

## Review mode

Read the provided draft. **Sample-verify** factual claims via `profile:tender-evidence` when Review mode flags unsupported statements. Produce structured feedback:

```markdown
## Review: Krav [ID] — [short title]

### Compliance
- [ ] Requirement ID and all sub-parts explicitly addressed
- [ ] Mandatory language matched (skal/must answered directly)
- [ ] Compliance level stated where required

### Evidence and credibility
- [ ] Claims traceable to sources (no unsupported superlatives)
- [ ] Attachment references valid and consistent
- [ ] Numbers and product names consistent with other answers

### Structure and evaluator UX
- [ ] Direct answer in first 1–2 sentences
- [ ] Scannable headings mirror sub-requirements
- [ ] Within length limits / table constraints

### Risk flags
- [ ] Overclaim / future tense presented as today
- [ ] Custom code implied where only configuration applies
- [ ] SaaS facts copied to B/K without responsibility split
- [ ] Competitor-distinguishing claims without evidence

### Suggested edits
[Specific before/after for each issue]
```

## Gap analysis mode

For bid/no-bid or "can we comply":

**Portfolio / DG gate** (ADO PFR portfolio, effort months, roadmap A/B/C/D, management canvases): use skill **`tender-go-no-go-gate`** — not this per-requirement mode.

For individual requirements or tender-tool rows:

1. Parse requirement(s) and decompose claims.
2. Run **`profile:tender-evidence`** (mandatory full waterfall).
3. Present **tender evidence ledger** before compliance assessment.
4. Output per requirement:

| Field | Content |
|-------|---------|
| Compliance | Met / Partial / Gap / Unknown |
| Evidence | What supports the assessment |
| Risk | Disqualification vs score loss |
| Response strategy | Full answer / alternative / frank gap / question to buyer |
| Recommendation | Bid / clarify / no-bid signal |

Label confidence **High / Medium / Low** per evidence-playbook. Do not state Met without verified evidence.

## Writing rules

### Voice and tone

- **Confident, factual, public-sector appropriate** — No hype, no consumer SaaS tone.
- **Buyer terminology** — "Oppdragsgiver", "Skytjenesten", "Kunden" per tender glossary.
- **Active voice** — "Skytjenesten støtter…" not "Det er mulig å…" unless describing optional capability.

### Banned patterns

| Avoid | Use instead |
|-------|-------------|
| "Best-in-class", "innovative", "robust", "seamless" | Specific capability or metric |
| "We believe we can…" for existing features | Factual present tense |
| Vague "rutiner finnes" | Named process + frequency + tool |
| Copy-paste from old tenders without checking | Adapt + verify against current product |
| Hidden custom development | Configuration / standard product / low-code within product |

### Deployment splits (Norwegian tenders)

When krav covers **Ugradert** and **Gradert** (or SaaS vs B/K):

- **Ugradert/SaaS** — Supplier-operated controls, geo-redundancy, supplier ops routines.
- **Gradert/B/K** — Same product design; split **customer vs supplier** responsibility for infra, backup, admin access. Never claim supplier-operated guarantees that apply only to SaaS.

See `docs/product/Krav_2.24_Svar_Forslag.md` for the split pattern.

### Evidence tiers for tender claims

| Tier | Use in tender |
|------|----------------|
| **Strong** | Certification letter, help topic, wiki process page, shipped product behaviour verified in code |
| **Supporting** | Prior approved tender text, internal process doc in repo |
| **Weak / do not use alone** | Memory, search snippet, roadmap intent |

Mark `[Evidence: …]` inline when drafting for internal review; strip or convert to attachment refs for final submission unless the user wants markers kept.

## Review checklist

Use for self-check and Review mode:

1. Every sub-requirement has a visible answer.
2. First sentence is compliance-relevant (not background).
3. No contradictions with other known answers in the session.
4. Graded/ungraded or SaaS/on-prem split is correct.
5. Attachment references use buyer's naming convention.
6. No invented certifications, customer counts, or SLAs.
7. Partial compliance is explicit with mitigation or alternative.
8. Win theme present (batch bids only) where the section is strategic.

## Color-team gates (full bids)

When the user is preparing a full submission:

| Gate | Focus |
|------|--------|
| **Pink** | Outline mirrors evaluation criteria; matrix complete; themes defined; major gaps known |
| **Red** | Every requirement traceable; evidence for claims; consistent facts; risks documented |
| **Gold** | Format, page limits, signatures, portal packaging, final read-aloud for clarity |

Offer to run a gate when the user says "pink review", "red review", or "final QA".

## Integration with other skills

| Need | Skill / resource |
|------|------------------|
| Deep technical investigation | `lmwtfy` (import verified facts into tender ledger only) |
| Shipped vs roadmap (PFR) | `pfr-ai-capability-check` |
| Competitive positioning in themes | `competitive` |
| Risk management krav content | `docs/product/Risk_Management_Tender_Description.md` |
| Brand in slide decks | `tieto-brand` |
| ADO backlog links for roadmap gaps | `pm-ado-work-item-authoring` |

## MCP tools used

Per [`shared/evidence/sources-and-tools.md`](../shared/evidence/sources-and-tools.md) and **`profile:tender-evidence`**:

| Server | Typical use in tenders |
|--------|------------------------|
| `user-mediawiki` | Process, security, release notes, delivery |
| `user-ratatoskr` | Product capabilities, admin config, certifications PDFs |
| `user-azure-devops` | Commitment dates, shipped vs planned |
| GitHub (`gh`) | Verify implementation when help/wiki ambiguous |

## Additional resources

- Evidence retrieval workflow + ledger: [references/evidence-retrieval.md](references/evidence-retrieval.md)
- **Prior bid library (mandatory):** [references/tender-reference-library.md](references/tender-reference-library.md) → `docs/tender-reference/` + [`INDEX.md`](../../../docs/tender-reference/INDEX.md)
- Ratatoskr tool order: [references/ratatoskr-mcp-tools.md](references/ratatoskr-mcp-tools.md)
- Retrieval profile: [`shared/evidence/profiles/tender-evidence.md`](../shared/evidence/profiles/tender-evidence.md)
- Response templates (NO/EN): [references/response-templates.md](references/response-templates.md)
- Compliance matrix: [references/compliance-matrix.md](references/compliance-matrix.md)
- Repo examples: [references/examples.md](references/examples.md)

## Rules referenced

- `shared/evidence/README.md` — index; **`tender-response`** → **`profile:tender-evidence`**
- `shared/evidence/evidence-playbook.md` — claim / evidence / confidence vocabulary
- `shared/evidence/profiles/tender-evidence.md` — normative doc-first load order
- `shared/evidence/budgets.md` — default caps
- `shared/evidence/sources-and-tools.md` — MCP hygiene, GitHub repos
- `shared/evidence/ratatoskr-preflight.md` — help center preflight
- `shared/evidence/verification-and-leads.md` — tender ledger alignment

## DO / DON'T

**DO:**

- **Always** grep `docs/tender-reference/extracted/` first for the krav ID or topic.
- Run **`profile:tender-evidence`** before claiming product capabilities.
- Present tender evidence ledger before final draft (Respond / Gap analysis).
- Quote requirement IDs and sub-parts in headings.
- Search `docs/product/` for reusable prior art before MCP calls.
- State compliance level explicitly for partial gaps.
- Separate facts (product) from process (Tietoevry delivery) from customer responsibility (B/K).
- Ask for the mandated response template when unclear.

**DON'T:**

- Use lmwtfy answer files as tender prose without ledger verification.
- Cite search snippets without full topic/page read.
- Mark **Met** on Low confidence or UNVERIFIED claims.
- Draft without seeing the exact requirement text.
- Promise custom code when the RFP forbids it or only configuration applies.
- Copy SaaS operational answers to graded on-prem without rewriting responsibilities.
- Soften gaps with marketing language.
- Submit-style finalization without user confirmation on gap wording.

## Output contract

| Mode | Primary output | File |
|------|----------------|------|
| Respond | Requirement answer(s) ready to paste | Optional save to `docs/product/` |
| Matrix | Compliance matrix + gap summary + theme map | Optional save |
| Review | Checklist with pass/fail and edits | In conversation |
| Gap analysis | Per-requirement assessment table | In conversation |

Always show the draft in conversation. Save only after user confirms content (or when user explicitly says "save").
