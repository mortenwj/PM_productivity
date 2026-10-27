# Day 1 — BRE session plan (90 min)

**Title:** Business Rules Engine — status, commitments and role in the platform  
**When:** Day 1, 13:20–14:50  
**Owners:** Morten (lead) · Bjørn (technical status)  
**Audience:** Process Platform team (internal)  
**India:** Required hybrid session — same content, IST times per main workshop schedule

---

## Session goal

Align the team on **what BRE is for**, **why it matters to customers**, and **where we actually are** — so we share one story when process, automation, and rules come up elsewhere in the workshop (including Day 2 customer dialog on process support — BRE is not the headline there).

**Outputs:** Shared understanding · agreed pilot slice · clarity on commitment timeline · owners for next steps

---

## Timing

| Block | Duration | Focus |
|-------|----------|--------|
| **A — What & why** | 30 min | BRE in platform context, customer problems, rule model, 3 example cases |
| **B — Status & next steps** | 55 min | Code/dev reality, DevOps, commitments, role in Process Framework, decisions |
| **Close** | 5 min | Capture actions |

---

## Block A — What BRE is and why it matters (~30 min)

### Slide 1 — Title & goal (2 min)

**Business Rules Engine — status, commitments and role in the platform**

Today we align internally on BRE. Not a customer session; not a sales pitch.

---

### Slide 2 — Where BRE sits in the platform (3 min)

**Process Framework — three questions**

| Component | Question |
|-----------|----------|
| Process models | **What** the process looks like |
| Process Engine / Flow | **How** it runs |
| **Business Rules Engine** | **When** actions are allowed or required |

BRE is the **governance layer** — validations, constraints, and (eventually) automation — without bespoke code per customer.

*Speaker note:* Link to Flow inventory from earlier Day 1; BRE is a sibling pillar, not a replacement for Flow or Process Engine.

---

### Slide 3 — The customer problem (5 min)

**Why customers care**

Public-sector organisations need **standardisation and compliance** *and* **local adaptation**. Today much of that lives in:

- Custom event code and consultant one-offs  
- Opaque configuration that breaks on upgrade  
- Repeated patterns (close-case checks, auto-close, field rules) rebuilt per customer  

**BRE aims to:** make operational rules **explicit, configurable, versionable, and auditable** — DMN-based, inside the product.

*Speaker note:* Avoid “no-code magic”; be honest that consultant/admin skill is still needed early on.

---

### Slide 4 — Rule model (5 min)

**Every rule: Trigger → Condition → Action**

| Part | Meaning | Examples |
|------|---------|----------|
| **Trigger (WHEN)** | What starts evaluation | Case updated, document created, schedule (future) |
| **Condition (IF)** | When the rule applies | Case type, status, field values, document state |
| **Action (WHAT)** | What happens | Block with message · update data · notify · trigger process |

*Reuse:* Oslo deck slide 12 (or equivalent visual).

---

### Slides 5–7 — Three example cases (15 min, ~5 min each)

Pick **concrete, named patterns** the team already knows from scope sheet and customers. Keep one slide per example: **problem → rule pattern → customers**.

#### Example 1 — Close-case validation (First wave)

**Problem:** Cases closed with working documents, missing mandatory fields, or cancelled while documents still active.

**Pattern:** Event · Case status change · **Raise error** (validation message)

**Customers:** Tullverket, Regeringskansliet, IMR, Svenska kyrkan · DevOps [#219865](https://dev.azure.com/tieto-si/360/_workitems/edit/219865)

*Reuse:* Oslo slide 13.

#### Example 2 — Auto-close ready cases (First / Second wave)

**Problem:** Large share of cases sit in “ready from case handler” but never close; manual follow-up cost.

**Pattern:** Scheduled job · status + document conditions · **Update data** (close case)

**Customers:** Aurskog-Høland · DevOps [#311335](https://dev.azure.com/tieto-si/360/_workitems/edit/311335)

*Reuse:* Oslo slide 14. **Flag in talk:** update/automation actions not in runtime yet — sets up Block B honestly.

#### Example 3 — Empty cases → void only (First wave)

**Problem:** Cases without documents should not be closed normally — only voided.

**Pattern:** Event · Case close attempt · **Raise error**

**Customers:** Regeringskansliet Klaradia · DevOps [#239187](https://dev.azure.com/tieto-si/360/_workitems/edit/239187)

*Optional backup:* Helsedirektoratet due date on incoming doc ([#312153](https://dev.azure.com/tieto-si/360/_workitems/edit/312153)) — shows **Commitment** pressure and Update-data pattern.

---

## Block B — Status, commitments, next steps (~55 min)

### Slide 8 — What we have built (10 min) · *Bjørn*

**Backend (core-bl) — substantial framework**

| Area | Status |
|------|--------|
| DMN meta model + publish lifecycle | Strong |
| Admin APIs (list, save, publish) | Ready |
| Event runtime (Case/Document CRUD) | Partial — wired, gaps remain |
| ValidationMessage (block with message) | **Works** |
| RunProcess / data updates / jobs | **Not implemented** |
| Admin UI | Separate repo; feature flag gated |
| Feature flag `BusinessRuleEngineEnabled` | **Off by default** (6.6+) |

*Detail:* [BRE_Pilot_Readiness_Assessment.md](./BRE_Pilot_Readiness_Assessment.md) · [BRE_Architecture.md](./BRE_Architecture.md)

**Key runtime gaps to mention (not slide-heavy — whiteboard OK):**

- ContextEntity not filtered at runtime  
- IsEnabled not enforced  
- RunProcess is empty stub  
- Job/Manual triggers — meta only  

---

### Slide 9 — DevOps structure (5 min) · *Morten*

**Epic [#11122](https://dev.azure.com/tieto-si/360/_workitems/edit/11122)** — DMN Business Rules Engine · Bjørn · Target **2026-12-30**

**Active now:** Data model · Input resolution · Validations · Built-in queries/actions  

**Backlog:** Meta events · Admin UX · Publishing · Rules library · Statistics  

*Detail:* [sources/ado-work-items.md](./sources/ado-work-items.md)

---

### Slide 10 — Commitments drive the real timeline (10 min) · *Morten*

**Planning assumption:** Customer **Commitment** items matter more than epic target date alone.

| When | Item | Needs from BRE |
|------|------|----------------|
| Overdue | #312153 Helsedirektoratet | Event + update due date |
| Feb 2026 (desc.) | #231319 Svenska Kyrkan | Cleanup on case close |
| **Jun 2027** | #422713 Danish tender K | Auto-close docs on case close |
| **Sep 2027** | #420587, #420590, #420282 IVO tender | Mandatory fields, dependencies, cleanup |

**Anchor for full scenario coverage: mid–late 2027** — not Dec 2026.

Epic #11122 can still frame **pilot / foundation** in 2026; commitments define **automation and tender-grade** delivery.

---

### Slide 11 — Role in platform & relation to AI (5 min) · *Morten*

**BRE in the Process Platform stack**

- **Flow / Process Engine** — structure and execution of work  
- **BRE** — when things are allowed, required, or blocked  
- **FFUI** — field-level UI rules (related, not same engine today)  
- **AI / agentic** — needs **rules and structure** as guardrails (hypothesis; Day 2 dialog explores customer view — we don't lead with BRE there)

*Speaker note:* This connects to Day 1 AI/rules session later; don't pre-empt Day 2 customer agenda.

---

### Slide 12 — Proposed pilot & next steps (10 min) · *Morten + Bjørn*

**Pilot v1 (realistic with code today + small fixes)**

- Event trigger · **Case OnUpdate** · **ValidationMessage** only  
- First-wave scenarios: close-case validation, void-only empty cases  
- 1 tenant · flag on · 1–2 rule sets · single-decision models  
- **Engineering first:** ContextEntity + IsEnabled filtering · e2e test  

**Not in pilot v1:** Auto-close jobs, RunProcess, plugin actions, FFUI rules

**Discussion (15 min)** — capture on flip / DevOps:

1. Agree pilot slice?  
2. Who owns runtime blocker fixes?  
3. Admin UX — where is webadmin? Demo lovable.app?  
4. Reconcile epic Dec 2026 vs commitment Jun–Sep 2027  
5. ProductPlan bar — unpark/update?  

---

### Slide 13 — Close (5 min)

**Actions:** owner · date · link to DevOps / memo  

Point team to [`projects/process-platform/bre/`](./) inventory for reference after the session.

---

## Deck build notes

| Source | Use |
|--------|-----|
| **New slides** | 1–3, 8–13 (problem, status, commitments, next steps) |
| **Oslo deck** | Slide 12 (rule model), 13–14 (examples 1–2), optionally 15 trimmed as backup table |
| **Skip from Oslo** | Feature laundry list (Rule Designer, sync/async, explainability) — oversells current code |
| **Appendix (optional)** | Capability matrix from [BRE_Pilot_Readiness_Assessment.md](./BRE_Pilot_Readiness_Assessment.md) — for Bjørn deep-dive if asked |

---

## Facilitation

| Role | Who |
|------|-----|
| Part A — value, examples | Morten |
| Part B — technical status | Bjørn |
| Part B — DevOps, commitments, pilot proposal | Morten |
| Discussion scribe | Assign in room |

**Hybrid (India):** Same deck; pause after Slide 12 for async questions if needed.

---

## Related docs

| Doc | Use in session |
|-----|----------------|
| [BRE_Inventory.md](./BRE_Inventory.md) | Pre-read / reference |
| [BRE_Pilot_Readiness_Assessment.md](./BRE_Pilot_Readiness_Assessment.md) | Slide 8 detail |
| [sources/scenarios-register.md](./sources/scenarios-register.md) | Example cases |
| [sources/ado-work-items.md](./sources/ado-work-items.md) | Commitments table |
| [sources/oslo-workshop-deck.md](./sources/oslo-workshop-deck.md) | Reuse mapping |
