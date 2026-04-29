# PFR capability check — evidence sources and credibility tiers

**Purpose:** Define **which sources count as evidence** for an AI-assisted standard capability check, and **how trustworthy each class is**, so `claims[].support`, `confidence`, and `human_review_required` stay consistent.

**Normative for:** `pfr_ai_capability_check_output_format.md`, `.cursor/skills/pfr-ai-capability-check/SKILL.md`

---

## 1. Credibility tiers (**T1 = actual product code, absolute truth**)

| Tier | Meaning | Typical use in PFR checks |
|------|---------|---------------------------|
| **T1** | **Canonical product source code** — the shipped implementation in the **official product repository** (correct branch, tag, or commit). This is **ground truth**: behaviour exists iff the code path exists for that build (subject to configuration and data, which must be stated in `limitations`). | Cite **`source_code`** (preferred) or **`repo_file`** / **`github`** when the reference points at **implementation** files (e.g. services, UI, rules, SQL migrations), with **path** and ideally **commit or tag** in `title`, `url`, or `excerpt`. |
| **T2** | **Authoritative description of the product** or **delivery record**, not the executing code itself. Can lag, be incomplete, or be misinterpreted — but still org-sanctioned. | Official **MediaWiki** (current product/process/module pages, release information), **release_note_url**, **Azure DevOps** work items that prove **delivered** behaviour, **committed design/spec .md** in the canonical repo (documentation, not the code path under test). |
| **T3** | **Context and intent** — useful for triage, **not** sufficient alone to prove standard capability. | **This or another PFR Feature** text; **ServiceNow / CIM**; customer email in Description; screenshots without code/doc link; **{{Expired}}** wiki (cite as T3 unless cross-checked to **T1** or current **T2**). |
| **T4** | **Non-evidence for product facts.** | **Model recollection** without retrieval; **generic web**; chat; “we need a button here” with no code/doc. Do **not** list T4 in `evidence`; use `limitations` only. |

**Principle:** *Documentation describes; code decides.* Tiers encode that **T1 code outranks** T2 docs when they conflict — note the conflict in `limitations` and prefer the **T1** reading unless a human architect resolves otherwise.

**Caveat:** Reading code still requires the **right branch/build**, feature toggles, and tenant configuration. If those are unknown, **lower `confidence`** and expand `limitations` even when T1 is present.

---

## 2. Source kinds (`source_ref.kind`) — default tier mapping

When emitting JSON, set **`credibility_tier`** on every `source_ref`. If a source is borderline, pick the **more conservative** tier and explain in `limitations`.

| `kind` value | Default tier | Notes |
|--------------|----------------|------|
| **`source_code`** | **T1** | **Preferred** for implementation evidence: canonical repo, file path, optional commit/tag in `excerpt` or `url`. |
| `repo_file` | **T1** if the path is **implementation** under the product tree on a **release** branch/tag/commit; **T2** if the path is **only** documentation (e.g. root `README.md`, design markdown) | Same repo, different epistemic weight. |
| `github` | **T1** for **blob** / **tree** links to implementation on canonical repo+ref; **T3** for forks, random issues | Prefer **`source_code`** when the agent is citing Git explicitly. |
| `mediawiki` | **T2** when the page is current product/process documentation; **T3** if `{{Expired}}`, draft, or talk namespace | Wiki is **not** T1: it can be wrong or stale relative to code. |
| `release_note_url` | **T2** | Official release communication. |
| `ado_work_item` | **T2** if delivered backlog item proves shipped behaviour; **T3** if another **PFR** or item in **New** | Not code. |
| `service_now` | **T3** | |
| `other` | **T3** unless justified as **T2** (e.g. signed external standard) in `limitations` | |

Add new `kind` values only after updating the JSON Schema enum in `pfr_ai_capability_check_output_format.md`.

---

## 3. Rules: tiers ↔ `claims[].support`

| `support` value | Requirement on sources attached to that claim |
|-----------------|--------------------------------------------------|
| **`documented_in_source`** | **Either** at least **one T1** (code) source **directly** supporting the claim **or** at least **two independent T2** sources that together substantiate the same concrete behaviour. **T3/T4 alone is never enough.** |
| **`inferred`** | Only **T3**, or **T2+T3** / **T1+T3** where the jump is explained (e.g. code exists but product doc does not mention the UI entry point) — state the gap in `limitations`. |
| **`uncited`** | No usable `source_ref`, or only T4 — triggers **`human_review_required`** per format rules. |

---

## 4. Rules: tiers ↔ `confidence` (whole assessment)

| Condition | Suggested max `confidence` |
|-----------|---------------------------|
| Dispositive claim for `already_supported` / `achievable_without_new_core` backed only by **T3** | **`low`**; `human_review_required` **true**. |
| Same outcomes with **≥1 relevant T1** code reference and build/branch context matches | **`high`** allowed if `limitations` are minor. |
| Same outcomes with **only T2** (wiki + release note, no T1) | **`medium`** at most unless **two** independent T2 lines agree; prefer **`human_review_required`** until a tech role confirms code path. |
| `partially_supported` / `not_supported_product_gap` with **T1** showing partial implementation | **`medium`**–**high** for the “partial” aspect; document what is missing vs code. |
| **{{Expired}}** wiki without T1/T2 current cross-check | Cap at **`medium`**; prefer **`low`** for customer-facing “close as standard”. |

**Strict gate (recommended):** If `outcome` ∈ {`already_supported`, `achievable_without_new_core`} and **`evidence` contains no T1**, set **`human_review_required`** to **true** unless **two** independent **T2** sources are present *and* `limitations` explicitly state that code was not retrieved but documentation is aligned.

---

## 5. Ordering evidence in the JSON

In the `evidence` array, prefer order: **T1 first**, then **T2**, then **T3**. Omit **T4** from `evidence`.

---

## 6. Governance

| Action | Owner (suggested) |
|--------|-------------------|
| Define “canonical product repo” and default branches/tags for T1 | Tech lead / release engineering |
| Resolve **doc vs code** conflict | Principal PM + tech lead; update **T2** wiki after resolution |
| Add a new `kind` or change tier defaults | Update this file + JSON Schema + skill in one PR |

---

## 7. Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-04-29 | Initial tiers T1–T4, kind mapping, claim/confidence rules |
| 1.1 | 2026-04-29 | **T1 = product source code (absolute truth)**; wiki and similar docs → **T2**; add `source_code` kind; strict gate when no T1 for “already standard” outcomes |

---

**File:** `PFR skill/pfr_evidence_sources_credibility.md`
