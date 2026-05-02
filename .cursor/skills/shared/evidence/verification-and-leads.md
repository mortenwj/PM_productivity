# Verification and leads

**Purpose:** Operational checklists and anti-patterns so **leads** are upgraded to **verified** evidence before claims ship.

**Authoritative definitions:** **[`evidence-playbook.md`](evidence-playbook.md)** — claim, evidence, **verified** vs **lead** vs **inferred**, **verification**, **confidence**, **when to stop**, **conflicting evidence**. Use the same meanings everywhere; do not redefine those terms in this file.

---

## Leads vs verification (operational)

Search hits (`gh search code`, `mediawiki_search`, ADO list rows, topic title matches) are **leads** until you complete **verification** per **`evidence-playbook.md`** §4. See also **`evidence-playbook.md`** §3.

---

## Neutral capture checklist (before mapping to skill output)

For each material finding, capture at least:

- **Stable locator:** URL (wiki, help topic, GitHub blob, ADO work item URL) or path + commit where applicable  
- **Title or label:** page title, topic title, file path, work item title  
- **Excerpt:** short quoted or paraphrased support (and section anchors if the source is long)  
- **Verified how:** per **`evidence-playbook.md`** §4 (e.g. read full file | read full help topic | read wiki section | traced code path | searched but found nothing)

---

## PFR runs

Map checklist fields into `source_ref` / `evidence` / `claims` per **`pfr-ai-capability-check/references/pfr_ai_capability_check_output_format.md`** and assign **`credibility_tier`** per **`pfr-ai-capability-check/references/pfr_evidence_sources_credibility.md`**. **Support** values (`documented_in_source`, `inferred`, `uncited`) align with the playbook → PFR quick map in **`evidence-playbook.md`**.

When code or topic budget is hit without T1: stop further code search, document in **`limitations`**, set **`human_review_required`** as appropriate, and prefer **`recommended_next_action`**: `escalate_to_pm_or_tc` or `request_more_detail_from_reporter` rather than silent guessing (per PFR format doc).

---

## lmwtfy runs

Present an **evidence ledger** before writing the answer file. For each factual **claim** (see **`evidence-playbook.md`** §1):

**Claim:** [the specific statement you will write]  
**Source:** [GitHub file:line URL / help center topic URL / DevOps work item / wiki URL / "UNVERIFIED"]  
**Verified how:** [values per **`evidence-playbook.md`** §4]

**UNVERIFIED** = not yet **verified** (still a **lead** or missing source per **`evidence-playbook.md`** §3). Downgrade **confidence** per **`evidence-playbook.md`** §6, verify, or remove the claim.

---

## Rationalizations to reject (process)

| Rationalization | Why it is wrong |
|-----------------|-----------------|
| "I already found this in a search snippet, no need to read the full file" | Violates **`evidence-playbook.md`** §3–§4; use `gh api` / full read. |
| "The wiki page title confirms this" | Violates **`evidence-playbook.md`** §4; open `mediawiki_get_page` and read the section. |

---

**File:** `shared/evidence/verification-and-leads.md`
