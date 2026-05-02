# Evidence playbook (shared)

**Purpose:** One **PM-friendly** vocabulary for **claims**, **evidence**, **verification**, **confidence**, and **documentation coverage** (§8), shared by **`pfr-ai-capability-check`** and **`lmwtfy`**.  
**Scope:** *What good evidence looks like* and *how to think about it*. **Not** a duplicate of: which MCP tool to call ([`sources-and-tools.md`](sources-and-tools.md)), numeric caps ([`budgets.md`](budgets.md)), search order ([`profiles/`](profiles/)), or snippet discipline ([`verification-and-leads.md`](verification-and-leads.md)).

**Alignment with PFR:** Product-truth strength still maps to **T1–T4** and JSON fields in **`pfr-ai-capability-check/references/pfr_evidence_sources_credibility.md`** and **`pfr-ai-capability-check/references/pfr_ai_capability_check_output_format.md`**. This playbook gives **plain-language labels**; PFR JSON remains the legal contract where the two differ in wording.

---

## 1. What is a claim?

A **claim** is a **single, checkable statement** you are asking others to believe, for example:

- “Feature X exists in the product today.”
- “The customer can achieve outcome Y with configuration only.”
- “This PFR describes a bug, not a missing feature.”

**Good claims are small.** If you need “and” three times, split into several claims.

**Per skill:**

- **PFR:** Each JSON `claims[]` row is one claim (`C-1`, `C-2`, …) with `statement`, `support`, and optional `sources`.
- **lmwtfy:** Each **evidence ledger** row states one claim you plan to put in the written answer.

---

## 2. What is evidence?

**Evidence** is **retrieved material** (or an explicit “we looked and found nothing”) that lets a **human** re-check your reasoning.

It always includes:

- **Where** you looked (link, file path + repo, work item id, help topic).
- **What** you saw (short excerpt or paraphrase tied to that locator).
- **How** you know it (see §4 Verification).

**Per skill:**

- **PFR:** The `evidence[]` list: deduplicated `source_ref` entries with tiers **T1–T3** (see PFR credibility doc; do not put T4 in `evidence`).
- **lmwtfy:** The **Source** and **Verified how** columns in the ledger, plus links in the final answer.

---

## 3. Evidence types (simple labels)

Use these three labels when **talking about** a finding before or beside skill-specific enums:

| Label | Meaning | Typical strength |
|--------|---------|------------------|
| **Verified (strong)** | You opened the **primary source** (full file, full help page, full wiki section, or traced code path) and the claim is **directly supported** by what that source says or does. | Maps to **strong** PFR paths (`support`: `documented_in_source` with required tiers per PFR rules). For **lmwtfy**, this is what backs **High** confidence together with §6. |
| **Lead** | A **pointer only**: search hit, title match, snippet, ADO preview line, “someone said in chat.” **Not** enough on its own. | Treat as **unverified** until you complete §4. PFR: do not treat as `documented_in_source` until upgraded. |
| **Inferred (low confidence)** | A **reasonable step** from verified items, but **not** spelled out in a single source (gap-filling, “usually,” architecture judgment). | PFR: `support`: `inferred` and explain gaps in `limitations`. **lmwtfy:** flag in prose; usually caps confidence at **Medium** or **Low** unless a second source agrees. |

**Important:** “Inferred” here names **how the claim is supported**. **Confidence** (§6) names **how sure you are overall**; they are related but not the same field.

---

## 4. What counts as verification?

**Verification** means you did the **boring work** so another person does not have to guess.

**Counts as verified**

- **Code:** Read the **relevant region** of the implementation (not only a search hit). Prefer a stable link (for example GitHub blob with line) when you cite it in the deliverable.
- **Help (Ratatoskr):** Read the **topic** (or the section you rely on), not only `search_topics` snippets.
- **Wiki:** Open the **page** and read the section you cite; not only the search snippet.
- **ADO:** Read the **work item** fields you rely on (state, description, AC); not only a query title list.
- **Nothing found:** You ran a **bounded** search per [`budgets.md`](budgets.md) and profile, and you say **clearly** that nothing usable turned up.

**Does not count as verified**

- Search-only hits, unread attachments, “I remember from last year,” model guessing.

**Details and anti-patterns:** [`verification-and-leads.md`](verification-and-leads.md).

---

## 5. Confidence levels (High / Medium / Low)

Use **one** overall confidence for the **assessment** (PFR JSON) or the **answer** (lmwtfy prose). Calibrate from **verified** material, not from hope.

| Level | When to use |
|--------|----------------|
| **High** | At least **one verified implementation or authoritative product fact** (T1-style for behaviour), **and** at least **one independent** corroborating line (for example help, wiki, or closed delivery record as defined in PFR tier rules). **lmwtfy:** same idea: **code verified** plus **one other** verified source. |
| **Medium** | **One** strong line only (for example only wiki, or only help, or only code without a second check). Or: verified core plus **inferred** edges only. |
| **Low** | Mostly **leads** or **inferred** content, or important **unknowns** (version, tenant, toggles) not resolved. |

**PFR (extra nuance):** **`high`** is appropriate when **verified T1** pins a dispositive implementation fact (for example “enforcement is absent; filtering is optional”), **independent T2** (help/wiki) **agrees** on how the feature is presented, and there is **no verified conflict** — state any residual integration-only uncertainty in **`limitations`**, not by downgrading to **`medium`** unless a format-rule trigger still forces review.

**PFR-only rules** (strict gates, `human_review_required`, caps on `confidence` by tier mix): **`pfr-ai-capability-check/references/pfr_evidence_sources_credibility.md`** §3–§4 and the JSON format doc. This playbook does not relax those rules.

**lmwtfy:** If you would label **Low** for the answer, do **not** treat the wiki publication loop as mandatory truth transfer; see `rules/knowledge-loop.md`.

---

## 6. When to stop searching

Stop when **both** are true:

1. **Budget:** You respected [`budgets.md`](budgets.md) and the active **profile** ([`profiles/cost-aware-doc-first.md`](profiles/cost-aware-doc-first.md) or [`profiles/code-first-research.md`](profiles/code-first-research.md)), including any **early-stop** rules in those files.  
2. **Sufficiency for the job:** You can either **defend** your claims with **verified** material, or you can **honestly list** what is still unknown and why (PFR: `unknowns` / `limitations`; lmwtfy: ledger + answer caveats). For **PFR**, “defensible” also follows **`pfr-ai-capability-check/references/pfr_evidence_sources_credibility.md`** and **`pfr-ai-capability-check/references/pfr_ai_capability_check_output_format.md`** (outcome, strict gates, `human_review_required`).

**Do not** “just one more unbounded search.” If the next step does not change a human decision, skip it and document the skip.

**PFR stage 0** (parse the Feature body before external search): **`pfr-ai-capability-check/references/pfr_evidence_retrieval_cost_strategy.md`**.

---

## 7. Conflicting evidence

When two **verified** sources disagree:

- **Default rule (product behaviour):** **Implementation wins** over prose. In practice: **T1 (code)** outranks **T2 (docs/help)** for what the product **does** today. Say so explicitly and quote or cite both so a human can follow.

**Where each skill states this:**

- **lmwtfy:** Conflict rule in [`profiles/code-first-research.md`](profiles/code-first-research.md) (**code wins** vs help).
- **PFR:** Tier principle and doc-vs-code handling in **`pfr-ai-capability-check/references/pfr_evidence_sources_credibility.md`** §1 and related sections.

**If conflict is unresolved** (for example old wiki vs new code and you cannot confirm branch): lower **confidence**, widen **limitations** / caveats, and set **human review** where the skill requires it.

---

## 8. Documentation coverage (wiki / help)

Use this **only** for whether **official product documentation** (wiki, 360 help, release notes treated as **T2** in PFR) **explains** the capability well enough for a colleague or customer, **separate** from whether the **product implements** it (**T1** can still answer the latter).

Calibrate using **§3–§4**: count **verified** reads of wiki/help topics (not search snippets alone). **Leads** do **not** justify **well_documented**.

| Status | When to use |
|--------|----------------|
| **well_documented** | At least one **verified** wiki/help (or other **T2** doc you treat as official prose) **directly** covers the need with enough clarity to act or decide, without material gaps on the questions you assessed. |
| **partially_documented** | Some **verified** official doc exists but is thin, scoped wrong, missing steps, ambiguous, or **conflicts** with **verified** code (**§7**) without a clear “implementation wins” resolution in text. |
| **missing_documentation** | After **bounded** retrieval, no **verified** official doc addresses the need, or only **leads** / nothing usable (**§3**). |

**Relationship to confidence (§5):** Doc coverage is **orthogonal**. Example: **missing_documentation** can coexist with **high** `confidence` on behaviour if **T1** and tier rules support it; do **not** lower PFR gates or skip **`human_review_required`** solely because docs are good, or vice versa.

**Per skill:** PFR emits **`documentation_status`** in JSON (see **`pfr-ai-capability-check/references/pfr_ai_capability_check_output_format.md`**). **lmwtfy** includes a **Documentation assessment** section in the answer file (see **`rules/lmwtfy-format.md`**).

---

## Quick map: playbook label → PFR JSON (reminder only)

| Playbook | PFR `claims[].support` (when applicable) |
|----------|------------------------------------------|
| Verified (strong) | `documented_in_source` (with tier rules satisfied) |
| Lead (until upgraded) | Treat as **not yet** `documented_in_source`; do not ship as proven |
| Inferred | `inferred` |

For **`uncited`**, see PFR format doc; playbook shorthand: “still a **lead** or nothing usable.”

**Markdown-only (PFR Description block, schema unchanged):** When JSON uses **`inferred`**, the pasted Markdown **Claims** lines should add a visible prose tag after the enum value so PMs see intent without new JSON fields:

| Situation | Append after `*support:* inferred` |
|-----------|--------------------------------------|
| Claim rests on **PFR / Feature** description (typically **T3** `ado_work_item`) | `*(Markdown label: reported in PFR request)*` |
| Claim rests on **retrieval / workspace** facts (e.g. “no product files in this workspace”) | `*(Markdown label: observed in environment)*` |

Do **not** emit new JSON enum values for these phrases.

---

## File maintenance

| Change | Update |
|--------|--------|
| New corpus (new MCP, new repo family) | [`sources-and-tools.md`](sources-and-tools.md), relevant **profile**, [`README.md`](README.md) |
| New caps | [`budgets.md`](budgets.md) |
| New “do not trust snippets” examples | [`verification-and-leads.md`](verification-and-leads.md) |
| New **meaning** of claim / evidence / confidence / documentation coverage | **This file** |

---

**File:** `shared/evidence/evidence-playbook.md`

| Version | Date | Change |
|---------|------|--------|
| 1.2 | 2026-05-02 | §8: documentation coverage (wiki/help) shared with PFR + lmwtfy |
| 1.1 | 2026-05-02 | §6: explicit PFR defensibility alongside budgets/profiles |
| 1.0 | 2026-05-02 | Initial shared evidence definitions for PFR + lmwtfy |
