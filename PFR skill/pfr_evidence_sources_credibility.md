# PFR capability check — evidence sources and credibility tiers

**Purpose:** Define **which sources count as evidence** for an AI-assisted standard capability check, and **how trustworthy each class is**, so `claims[].support`, `confidence`, and `human_review_required` stay consistent.

**Normative for:** `pfr_ai_capability_check_output_format.md`, `.cursor/skills/pfr-ai-capability-check/SKILL.md`

---

## 1. Credibility tiers (T1 = highest)

| Tier | Meaning | Typical use in PFR checks |
|------|---------|---------------------------|
| **T1** | **Authoritative product truth** for Public 360° as currently documented by the product organization. | Official **MediaWiki** product/process pages (module overviews, configuration possibilities, supported integration patterns, release information for a **stated** version when the page is current). |
| **T2** | **Strong engineering / delivery record** tied to the product codebase or formal backlog. | **Release note** URLs aligned with shipped product; **official product Git** README, ADO wiki in project, specs checked into the canonical repo; **Azure DevOps** Epic/Feature/User Story **Done/Resolved** with description/AC that directly proves behaviour **in the shipped product** (not another customer’s PFR text alone). |
| **T3** | **Context and intent** — useful for triage, **not** sufficient alone to prove standard capability. | **This or another PFR Feature** text; **ServiceNow / CIM** ticket; customer email pasted into Description; **consultant notes**; screenshots without doc link; **{{Expired}}** wiki pages (still cite, but **downgrade** to T3 unless cross-checked to a T1/T2 current source). |
| **T4** | **Non-evidence for product facts.** | **Model recollection** without retrieval; **generic web** or vendor blogs not owned by the product org; **other customers’** unsubstantiated assertions; **chat** transcripts; **“I think”** from the PFR body with no doc. Do **not** attach T4 to a claim as proof; use only in `limitations` if mentioned. |

**Principle:** *Structured validity ≠ factual accuracy.* Tiers make explicit **how much to trust** each `source_ref` when scoring a claim.

---

## 2. Source kinds (`source_ref.kind`) — default tier mapping

When emitting JSON, set **`credibility_tier`** on every `source_ref` (see schema in `pfr_ai_capability_check_output_format.md`). If a source is borderline, pick the **more conservative** tier and explain in `limitations`.

| `kind` value | Default tier | Notes |
|--------------|----------------|------|
| `mediawiki` | **T1** if page is current process/product doc; **T3** if page has `{{Expired}}` or is talk/essay namespace | Agent must note expiry in `excerpt` or `limitations`. |
| `release_note_url` | **T2** when URL is official release information for Public 360° / named product line | Downgrade to **T3** if version not matched to customer environment. |
| `repo_file` | **T2** for canonical product repo paths and committed docs | **T3** for draft branches or forks unless policy says otherwise. |
| `ado_work_item` | **T2** if work item type is product backlog item and state shows **delivered** behaviour relevant to claim; **T3** if it is another **PFR** or proposal in **New** | Another open PFR is **peer intent**, not proof of shipping. |
| `github` | **T2** official org/repo; **T3** fork or issue without merge | Use `github` when not using `repo_file` for the same URL. |
| `service_now` | **T3** | Intent, SLA, GDPR pointer — not proof of standard product behaviour. |
| `other` | **T3** unless you document why it is T1/T2 in `excerpt`** | e.g. licensed third-party spec = case-by-case in `limitations`. |

Add new `kind` values only after updating the JSON Schema enum in `pfr_ai_capability_check_output_format.md`.

---

## 3. Rules: tiers ↔ `claims[].support`

| `support` value | Requirement on sources attached to that claim |
|-----------------|--------------------------------------------------|
| **`documented_in_source`** | At least **one T1** source **or** at least **two independent T2** sources that together substantiate the same concrete behaviour (not two links to the same page). **T3/T4 alone is never enough.** |
| **`inferred`** | Only **T3** sources, or mixed T2+T3 where inference bridges a gap — state the inference in `limitations`. |
| **`uncited`** | No `source_ref` attached, or only T4 — use rarely; triggers **`human_review_required`** per format rules. |

---

## 4. Rules: tiers ↔ `confidence` (whole assessment)

Heuristics for the **overall** `confidence` field (agent judgment, human can override):

| Condition | Suggested max `confidence` |
|-----------|---------------------------|
| Any dispositive claim for `already_supported` or `achievable_without_new_core` backed only by **T3** | **`low`**; set `human_review_required` **true**. |
| Outcome is `already_supported` / `achievable_without_new_core` and **≥1 T1** directly addresses the claim | **`high`** allowed if `limitations` are empty or minor. |
| Outcome is `already_supported` / `achievable_without_new_core` and only **T2** (no T1) | **`medium`** unless two independent T2 lines agree. |
| `partially_supported` or `not_supported_product_gap` with mixed T1/T2 and clear gap analysis | **`medium`** or **`high`** depending on gap clarity; document negation risk in `limitations`. |
| Any **{{Expired}}** wiki used without T1/T2 current cross-check | Cap at **`medium`**; prefer **`low`** for customer-facing “close as standard”. |

---

## 5. Ordering evidence in the JSON

In the `evidence` array, prefer order: **T1 first**, then **T2**, then **T3**. Omit **T4** from `evidence` (use `limitations` only).

---

## 6. Governance

| Action | Owner (suggested) |
|--------|-------------------|
| Reclassify a wiki page between T1 default and T3 (expired) | Product / wiki steward |
| Add a new `kind` or change tier defaults | Update this file + JSON Schema + skill in one PR |
| Dispute “this should be T1” | Principal PM / Tech lead decision; document in wiki or here |

---

## 7. Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-04-29 | Initial tiers T1–T4, kind mapping, claim/confidence rules |

---

**File:** `PFR skill/pfr_evidence_sources_credibility.md`
