# Evidence retrieval for tender responses

Implements **`profile:tender-evidence`** for the `tender-response` skill. Normative retrieval order: [`../../shared/evidence/profiles/tender-evidence.md`](../../shared/evidence/profiles/tender-evidence.md).

---

## When to run full retrieval

| Situation | Retrieval |
|-----------|-----------|
| Any Respond / Gap / Review with claims | **Stage 0a:** `docs/tender-reference/extracted/` (mandatory) |
| Reusing verbatim prior answer user confirmed | Spot-check changed facts; still grep 0a for the krav |
| Process krav with strong tender-reference hit | Stage 0a + wiki spot-check |
| Product capability, security, certification | Full waterfall (stages 0–4 as needed) |
| Gap analysis / bid-no-bid | Full waterfall mandatory |
| Review mode on existing draft | Verify sampled claims against sources |

---

## Step-by-step (Respond / Gap analysis)

### 1. Decompose the krav into verifiable claims

Before MCP calls, list checkpoints:

```
Krav [ID] decomposition:
- [ ] [Sub-requirement or claim to verify]
- [ ] [...]
```

Map each to **krav type** (product / security / process / certification / roadmap) per profile routing table.

### 2. Load shared evidence layer

Read once per run:

1. [`../../shared/evidence/evidence-playbook.md`](../../shared/evidence/evidence-playbook.md)
2. [`../../shared/evidence/budgets.md`](../../shared/evidence/budgets.md)
3. [`../../shared/evidence/sources-and-tools.md`](../../shared/evidence/sources-and-tools.md)
4. [`../../shared/evidence/verification-and-leads.md`](../../shared/evidence/verification-and-leads.md)
5. [`../../shared/evidence/profiles/tender-evidence.md`](../../shared/evidence/profiles/tender-evidence.md)

### 3. Execute `profile:tender-evidence`

**Stage 0a (mandatory):** Grep + read `docs/tender-reference/extracted/` — see [tender-reference-library.md](tender-reference-library.md).

Stage 0b → Wiki → Ratatoskr → ADO (if relevant) → Code (if needed).

**MCP servers:**

| Server | Tools |
|--------|-------|
| `user-mediawiki` | `mediawiki_search`, `mediawiki_get_page`, `mediawiki_search_in_page` |
| `user-ratatoskr` | See [ratatoskr-mcp-tools.md](ratatoskr-mcp-tools.md) |
| `user-azure-devops` | `wit_get_work_item`, `wit_query_by_wiql`, … per descriptors |
| GitHub | `gh search code`, `gh api repos/.../contents/...` per sources-and-tools |

If a server is not configured, skip and record in ledger.

### 4. Build tender evidence ledger

Present **before** final tender prose:

```markdown
## Tender evidence ledger — Krav [ID]

| Claim | Compliance | Source | Verified how | Cite in tender | Confidence |
|-------|------------|--------|--------------|---------------|------------|
| [statement for answer] | Met/Partial/Supporting | [URL or path] | [read full topic / wiki section / file region] | Inline / Bilag / internal | High/Med/Low |

### Profile extensions (if any)
[What you did beyond default waterfall and why]

### Conflicts noted
[Source A vs B → resolution per tender-evidence profile]

### Compliance summary
- **Planned compliance level:** Met | Partial | Gap
- **Gaps requiring frank disclosure:** [...]
```

Ask: **"Evidence checks out? OK to draft final answer?"**

### 5. Draft tender text

- Translate verified claims into buyer language (no URLs unless RFP allows).
- Map strong sources to **Bilag** references when buyer uses attachment numbering.
- Keep code citations in ledger unless RFP requests technical evidence.
- Apply [response-templates.md](response-templates.md).

### 6. Matrix mode integration

For each matrix row with Compliance ≠ Unknown, populate **Evidence** column from ledger sources. Batch ledgers by requirement group to avoid redundant `read_topic` calls.

---

## Citation strategy (evaluator-facing)

| Source type | In tender prose | In ledger |
|-------------|-----------------|-----------|
| Certification PDF | Bilag ID + document title | `read_pdf` URL or file path |
| Help topic | Paraphrase product fact; optional "se dokumentasjon" if allowed | Full help URL |
| Wiki | Internal process name; Bilag if published externally | Wiki URL |
| Code | Only if RFP asks; else internal verification | GitHub blob URL |
| ADO | "Planlagt leveranse [date]" for Partial only | Work item URL + state |
| Prior tender (canonical) | Reuse tone; verify facts | `docs/tender-reference/extracted/…` |
| Prior tender (drafts) | Reuse tone; verify facts | `docs/product/…` path |

---

## Confidence → compliance mapping

| Confidence | Allowed compliance in answer |
|------------|------------------------------|
| **High** | Met (if claim covers full sub-requirement) |
| **Medium** | Met with caveat, or Partial if sub-part unverified |
| **Low** | Partial or Gap only; flag for human review |

Never mark matrix **Met** on Low confidence.

---

## Controlled extensions

Same rules as lmwtfy shared layer:

- Complete default waterfall first unless justified skip (document why).
- Declare extensions in ledger before final draft.
- Same verification bar; extensions do not relax lead vs verified rules.
- Exceeding `budgets.md` → note in ledger and temper confidence.

---

## Integration with other skills

| Need | Route |
|------|-------|
| Shipped vs roadmap (PFR-style) | `pfr-ai-capability-check` for ambiguous features |
| Colleague-style deep technical proof | `lmwtfy` for investigation only — **not** for final tender prose; import verified facts into tender ledger |
| ADO work item authoring for gaps | `pm-ado-work-item-authoring` after bid decision |

**lmwtfy is not a substitute for tender-response.** Use lmwtfy to research; use this skill to draft compliant bid text from the ledger.
