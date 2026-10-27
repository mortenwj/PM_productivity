# 360° Flow — Commercial Specification v1

**Status:** DRAFT — pending management approval of Hybrid architecture  
**Owner:** Product (Flow / Process Framework) · **Consumers:** Enablement, Sales, Finance, Delivery  
**Effective:** Pilot → GA catalogue freeze (date TBD)

This document is the **operational source of truth** for Flow commercialization after architecture is approved. It is derived from the decision analysis; it does not replace Enablement list prices or the Sales Playbook deck.

---

## 1. Document map

| Document | Role | When to use |
|----------|------|-------------|
| **This spec (`360_Flow_Commercial_Spec_v1.md`)** | Definitions, SKU shape, guardrails, open items | Catalogue build, CRM, contracts, delivery scoping |
| [`360_Flow_Pricing_Options_Management_Deck.md`](360_Flow_Pricing_Options_Management_Deck.md) | Decision record (options, scores, rationale) | Management approval meeting only |
| [`360_Flow_Pricing_Management_Deck_8slides.md`](360_Flow_Pricing_Management_Deck_8slides.md) | Executive summary of decision deck | Same meeting |
| Commercial Playbook (source deck; extract: [`commercial_playbook_extract.txt`](commercial_playbook_extract.txt)) | Customer-facing levels, journey, sales guardrails | Sales conversations, training |
| [`360_Flow_PRD_Reconstruction_Unredacted_v4.md`](360_Flow_PRD_Reconstruction_Unredacted_v4.md) | Product capabilities, boundaries, GA reality | Feature ↔ tier alignment; Hosted Process product boundary |
| [`360_Flow_Implementation_Package_2Process_SalesKit_DRAFT.md`](360_Flow_Implementation_Package_2Process_SalesKit_DRAFT.md) | 2-process delivery package, contract appendix, sales-facing detail | Quotes, SOW, customer product sheet source |
| [`360_Flow_Implementation_Delivery_Project_Description_DRAFT.md`](360_Flow_Implementation_Delivery_Project_Description_DRAFT.md) | How first delivery project is run; time estimate; conditions | Delivery, SOW, service sheet |
| [`360_Flow_Playbook_Pilot_Footnote_DRAFT.md`](360_Flow_Playbook_Pilot_Footnote_DRAFT.md) | Playbook pilot callout + speaker notes | Sales training; deck update |
| [`360_Flow_Entitlement_and_Metering_Contract_Addendum_DRAFT.md`](360_Flow_Entitlement_and_Metering_Contract_Addendum_DRAFT.md) | Customer contract appendix — entitlement & metering | Attach to `FLOW-IMPL-2PROC` SOW |
| [`360_Flow_Implementation_Package_Product_Sheet_ENG.md`](360_Flow_Implementation_Package_Product_Sheet_ENG.md) | Customer product sheet (ENG, one page) | Sales / Enablement PDF |
| Enablement price model / CRM catalogue | **List prices, product numbers, bands** | Quotes and invoicing (not in this repo) |

**Rule:** If Playbook narrative, PRD capability, and this spec disagree after approval, **this spec + PRD** win for entitlement; **Playbook** wins for sales wording; **Enablement** wins for price.

---

## 2. Management decision (to record)

| # | Decision | Proposed default | Approved (Y/N) | Date | Notes |
|---|----------|------------------|----------------|------|-------|
| D1 | Commercial architecture = **Hybrid (Option 3)** | Yes | | | |
| D2 | Customer-facing packaging = **Playbook levels 1–3** on Hybrid meters | Yes | | | |
| D3 | Overage / expansion bands = **Process Engine per-process** where catalogue exists | Yes | | | |
| D4 | Included capacity — **pilot:** **2 active process models** per customer (all segments) | **Locked (pilot)** | | 2026-05-26 | **Conditional** on signed delivery contract (D9); GA segment model still TBD |
| D5 | **Hosted Processes** = separate commercial line (not Flow capacity) | Yes | | | |
| D6 | Pilot: **2** processes + **shipped building blocks only** + fixed implementation | **Locked (pilot)** | | 2026-05-26 | Enterprise features monetized post-pilot |
| D7 | Publish catalogue SKUs + definitions **before GA** | Yes | | | |
| D8 | Metering unit = **active process model** (§5.1): published + ≥1 connected case | Yes | | 2026-09-10 | Built-in platform monitoring is authoritative for overage |
| D9 | Included **2-process capacity** only with **signed delivery contract** (`FLOW-IMPL-2PROC`) | Yes | | 2026-09-10 | No standalone platform entitlement |
| D10 | Limited introductory offer: delivery contracts **signed by 31 Dec 2026**; **subject to change** | Yes | | 2026-09-10 | Grandfathering for signed contracts; see §11.4 |
| D11 | Overage invoicing per **E.6 / sales kit** — capacity fee separate from implementation | Yes | | 2026-09-10 | Unit price and billing period: Enablement (O3) |
| D12 | External quotes for **implementation package** permitted when sales kit + prices approved | Yes | | 2026-09-10 | Supersedes §11.3 "no list-price quotes" for this package only |

---

## 3. Product scope (what we sell)

**360° Flow** = governed **operational execution** on Public 360°: process models, progress plans, activities, rules, ProcessView — **not** generic BPM or standalone workflow SKU.

**Positioning:** Operational case progression inside Public 360°; monetize **scale and operating-model power**, not permission to run basic lifecycle/workflow.

| Commercial pillar | Product meaning |
|-------------------|-----------------|
| **Foundation** | Runtime + standard case execution surfaces (ProcessView, milestones/stages, standard dialogs, progression auditability, shipped building blocks) |
| **Capacity** | Entitlement to run **N active process models** in production (§5.1) |
| **Enterprise** | Portfolio/overview, advanced rules lifecycle, advanced integration patterns, cross-org governance **when GA** |
| **Services** | Fixed implementation packages (onboarding, process rollout) |
| **Hosted Processes** | Tieto-maintained, ready-to-use process **subscriptions** on top of Flow (separate line — §8) |

**Out of scope for this spec:** List prices, discount policy, contract legal text.

---

## 4. Approved commercial stack (Hybrid)

### 4.1 Layers

| Layer | ID | Customer receives | Charge model |
|-------|-----|-------------------|--------------|
| **A — Foundation** | `FLOW-FOUNDATION` | ProcessView execution, milestones/stages, standard dialogs, progression auditability, **shipped** governed building blocks only (pilot: §11) | **Included** in Public 360° / Basic — no compliance paywall |
| **B — Capacity** | `FLOW-CAPACITY` | Right to operate **N active process models** (§5.1) | **Included entitlement** (segment-based) + **per-process overage** / packs |
| **C — Enterprise** | `FLOW-ENTERPRISE` | Operating-model power (portfolio, advanced rules, advanced integrations, scale governance) | **Premium tier** — not required for basic traceability/compliance |
| **Services** | `FLOW-IMPL-*` | Fixed-scope implementation per Playbook | **One-time / project** packages |

### 4.2 Land vs return economics

| | Land | Return |
|--|------|--------|
| **Intent** | Adoption, pilot conversion, Nordic bundle norm | Fund Process Framework R&D and delivery standardization |
| **Mechanism** | Foundation included; included **N** processes (**pilot: 2** — §11) | Process packs · Enterprise · implementation services |

### 4.3 Optional add-ons (TBD with Enablement)

| Add-on | Use when |
|--------|----------|
| **Narrow user band** | Cross-case operational roles only — not every case worker |
| **Process pack (+5, +10, …)** | Entitlement exceeded |
| **Enterprise upgrade** | Customer needs GA Enterprise capabilities (§7) |

---

## 5. Definitions (catalogue-critical)

### 5.1 Active process model (metering unit)

**Terminology:** **Active process model** is the operational metering unit. The term **production process** in older docs maps to this definition unless context says otherwise.

An **active process model** counts toward capacity entitlement when **both** conditions are true:

| Criterion | Definition |
|-----------|------------|
| **Published** | The process model is published (available for operational use — not draft-only) |
| **In use** | At least **one case** is connected to the process model |

**Does not count:**

- Published process model with **no** connected cases  
- Draft / unpublished process model (even if cases exist in test)  
- Hosted Process SKUs billed on the hosted subscription line (§8) — **no double count**

**Measured by:** Built-in platform monitoring of active process model count per customer environment (§5.2).

**Resolved edge cases (2026-09-10):**

| ID | Rule | Decision |
|----|------|----------|
| O1b | Duplicate templates for same logical process | **Each** published model with ≥1 connected case counts **separately** (strict) |
| O1c | Non-production environments | **Excluded** — billing meter applies to **production environment only** |
| O1e | All connected cases closed/archived | **Still active** while ≥1 case **exists** (any status); customer may unpublish to stop count |
| O1d | Process Engine / legacy workflow flows | **Excluded** from Flow active-process meter; PE billed on PE terms (§9) |

### 5.2 Process entitlement and monitoring

Maximum number of **active process models** the customer may operate concurrently under contract without additional capacity fees.

| Element | Policy |
|---------|--------|
| **CRM field** | `flow_process_entitlement` — contracted count (default **2** under pilot limited offer) |
| **Monitoring** | Platform reports active process model count; authoritative for **overage detection and invoicing** unless contract dispute process applies |
| **Contract** | Must specify included count, unit price above entitlement, billing period, and measurement basis — see sales kit Part E.6 |
| **Environments** | **Production only** for billing meter (O1c locked) |
| **Billing basis** | **Monthly peak** active process model count in production (O2b locked) |
| **Enforcement** | **Contract + invoice only** in pilot — no technical block on exceeding entitlement (R5) |

### 5.3 Capability level (Playbook)

Sales-facing package level; maps to foundation + capacity + optional Enterprise:

| Playbook level | Name | Typical entitlement | Enterprise | Implementation |
|----------------|------|---------------------|------------|----------------|
| **1** | Single Process Access | Foundation + **1** production process | No | Fixed package — Level 1 |
| **2** | Managed Multi-Process | Foundation + **included multi** (align with D4: e.g. up to 5) | No | Fixed package per process rollout |
| **3** | Full Platform Access | Foundation + capacity per deal + **Enterprise** | **Yes** | Premium implementation / governance package |

**Horizontal growth:** Add processes via structured implementation + packs; platform fee does not replace pack/overage logic above included N.

**Vertical growth:** Upgrade to Level 3 / Enterprise for modeling autonomy, governance, advanced automation (only for **GA** features — §7).

### 5.4 Implementation package

Fixed-scope delivery envelope (oppsett, standard config, test, handover). **Not** open-ended consulting. Levels and SKU IDs: **Enablement to publish**.

**Pilot package:** `FLOW-IMPL-2PROC` — implementation of **2** processes; **required** for included 2-process capacity under limited offer (§11.4). Detail: sales kit.

### 5.5 Capacity overage invoicing

When active process model count **exceeds** `flow_process_entitlement`:

| Element | Policy |
|---------|--------|
| **Trigger** | Monitored count > contracted entitlement in billing period |
| **Charge** | Per additional active process model — **TBD** unit price and period (Enablement O3) |
| **SKU** | `FLOW-CAP-PACK-*` and/or Process Engine per-process band — **one** mechanism per deal |
| **Implementation** | Adding a new process typically requires **both** delivery services (`FLOW-IMPL-L2-PROC` or equivalent) **and** capacity fee unless pre-purchased pack covers it |
| **Billing basis** | **Monthly peak** count of active process models in production |
| **Notice** | **TBD** — customer notification before / when exceeding entitlement; no technical enforcement in pilot |

---

## 6. SKU and CRM shape (placeholders)

Enablement to replace `TBD` with catalogue IDs and price bands.

### 6.1 Recurring (subscription / annual)

| SKU placeholder | Description | Meter |
|-----------------|-------------|-------|
| `FLOW-CAP-INCL-2` | Included capacity — **pilot limited offer** (requires `FLOW-IMPL-2PROC`) | 2 active process models |
| `FLOW-CAP-INCL-5` | Included capacity — GA small segment (TBD) | 5 active process models |
| `FLOW-CAP-INCL-10` | Included capacity — GA default (TBD) | 10 active process models |
| `FLOW-CAP-PACK-5` | Expansion pack | +5 active process models |
| `FLOW-CAP-OVG-1` | Overage — single additional active process model | Per active process model per period (TBD) |
| `FLOW-ENTERPRISE` | Enterprise tier | Per org / tier band |
| `FLOW-HOSTED-*` | Hosted Process subscriptions | Per §8 |

### 6.2 One-time / services

| SKU placeholder | Description |
|-----------------|-------------|
| `FLOW-IMPL-2PROC` | **Pilot:** 2-process implementation package (unlocks limited 2-process capacity offer) |
| `FLOW-IMPL-L1` | Single Process Access implementation |
| `FLOW-IMPL-L2-PROC` | Per-process implementation (Managed Multi-Process) |
| `FLOW-IMPL-L3` | Full Platform / Enterprise onboarding |

### 6.3 CRM fields (minimum)

| Field | Purpose |
|-------|---------|
| `flow_module_product_id` | MDM module product number — **P00285** (360° Flow) |
| Organization tier | P360 segmentation |
| `flow_process_entitlement` | Contracted active process model count |
| `flow_active_process_count` | Monitored count (sync from platform or manual during pilot) |
| `flow_delivery_contract_signed` | Date — required for pilot included capacity |
| `flow_limited_offer` | Y/N — 2-process capacity bundle under §11.4 |
| `flow_capability_level` | Playbook level 1 / 2 / 3 |
| `flow_enterprise` | Y/N |
| `flow_implementation_package` | Services SKU (e.g. `FLOW-IMPL-2PROC`) |
| `flow_pilot` | Y/N + end date if pilot offer |
| `flow_hosted_skus` | Separate hosted subscriptions if any |

### 6.4 Playbook level → stack mapping

| Playbook | Foundation | Capacity | Enterprise | Services |
|----------|------------|----------|------------|----------|
| Level 1 | Included | 1 process | — | `FLOW-IMPL-L1` |
| Level 2 | Included | Included N (e.g. 5) + packs | — | `FLOW-IMPL-L2-PROC` per process |
| Level 3 | Included | Per deal + packs as needed | `FLOW-ENTERPRISE` | `FLOW-IMPL-L3` |

**Overage:** Above entitlement → `FLOW-CAP-PACK-*` and/or **360° Process Engine** per-process bands (§9) — **one** overage mechanism per deal; no double billing.

---

## 7. Enterprise boundary (must match GA)

Enterprise is sold as **operating-model power**, not basic compliance. Features **must** be GA (or qualified with date) before inclusion in Level 3 quotes.

| Capability area | In Enterprise (when GA) | **Not** Enterprise-only (stay in Foundation) |
|-----------------|-------------------------|-----------------------------------------------|
| Portfolio / cross-case overview (worklists, desktops) | Yes (when GA) | — |
| Advanced rules lifecycle | Yes (when GA) | — |
| Advanced integration patterns | Yes (when GA) | — |
| Cross-org governance / scale reporting | Yes (when GA) | — |
| ProcessView execution | — | Yes |
| Milestones, stages, standard dialogs | — | Yes |
| Progression auditability | — | Yes |
| Role enforcement (platform standard) | — | Yes |
| Basic lifecycle visibility on case | — | Yes |

**Backlog (do not sell at GA without date qualifier):** full PMC self-service modeling, portfolio features not shipped, deep BRE automation beyond Year 1 emphasis.

**PRD sync:** Update PRD § boundaries if Enterprise list changes.

---

## 8. Hosted / Managed Processes (separate commercial line)

**Product spec:** [`360_Hosted_Processes_spec.md`](360_Hosted_Processes_spec.md) (grill-me, 2026-05-26).

**Hosted Process** = standardized, Tieto-maintained process delivered as subscription; limited customer configuration. Product term per PRD; commercial line **separate from** Flow capacity packs.

### 8.1 Why separate

| | Configurable Flow (Hybrid) | Hosted Processes |
|--|---------------------------|------------------|
| Buyer wants | Ownership, adaptation, portfolio | Speed, low ops burden, predictability |
| Tieto role | Implementation packages; customer operates | **Maintains** standard process(es) |
| Meter | Active process model entitlement + Enterprise | **Subscription per process or pack** |
| Config | Governed configurability | **Limited** (standard template) |

### 8.2 Commercial shape (Enablement to price)

| Component | Model |
|-----------|--------|
| **Framework agreement** | Required to enter Hosted Processes program (assisted sale); unlocks catalog |
| **Per-process subscription** | **One annual line per activated process** (confirmed in product spec) |
| **Sector bundle** | Optional kommune/agency starter pack (TBD) |
| **Changes beyond standard** | Product change request → core expansion **or** T&M / change pack / Flow upgrade |

**Pilot catalog bar:** **≥5** templates at v1 launch (product spec AC1).

### 8.3 Rules

- Do **not** count hosted processes toward `FLOW-CAP-*` entitlement unless explicitly bundled in a combined offer (Finance approval required).
- Pilot hosted offers may use **manual annual contract** before subscription billing framework is GA.
- Delivery scope: oppsett, activation, documented standard processes, drift/maintenance by Tieto — per Forankring Alternativ 2.

**SKU placeholders:** `FLOW-HOSTED-BASE`, `FLOW-HOSTED-PROC-{name}`, `FLOW-HOSTED-BUNDLE-{sector}`.

---

## 9. Legacy 360° Process Engine

| Situation | Policy (proposed default — confirm Enablement) |
|-----------|-----------------------------------------------|
| **New Flow deals** | Process Engine per-process bands used for **overage above included entitlement** only; avoid parallel conflicting SKUs |
| **Existing Process Engine customers** | PE processes **do not** count toward Flow active-process meter (O1d); coexistence / migration memo still TBD |
| **Metering** | Flow meter = **360° Flow / Process Framework** active process models only (§5.1); **exclude** Process Engine-only and legacy Workflow-only flows |

---

## 10. Segment defaults (stress test)

**Pilot (locked):** **2** included active process models — **conditional** on signed delivery contract and limited offer (§11.4).

**GA hypothesis (still evaluating — not pilot):**

| Segment | Included N (GA proposal) | Land | Expand | Risk |
|---------|---------------------------|------|--------|------|
| Small kommune | **5** | Foundation + 5 | +5 packs | Over-metering blocks adoption |
| Large kommune | **10** | Foundation + 10 | Packs + Enterprise | Under-metering if unlimited |
| State agency | **10** | Foundation + governance story | Enterprise + capacity | Paywall on traceability fails procurement |

---

## 11. Pilot commercial policy (locked while evaluating)

While Flow is in **pilot**, the following overrides GA hypotheses in §4, §6, and §10.

### 11.1 Included capacity

| Rule | Pilot policy |
|------|----------------|
| **Active process model entitlement** | **2 per customer** — same for small kommune, large kommune, and state agency |
| **Condition** | **Only** with signed delivery contract for `FLOW-IMPL-2PROC` (or equivalent) — **no standalone entitlement** |
| **Third process and beyond** | Per active process model overage (§5.5) + implementation services — not included in pilot base |
| **Rationale** | Learn adoption and delivery cost with a **low, uniform floor**; tie capacity to delivered value |

### 11.2 Foundation scope — shipped building blocks only

Included (free) pilot use is limited to **existing shipped governed building blocks** — components delivered and maintained as part of the Flow product catalogue.

| In pilot Foundation (included) | Not in pilot Foundation (chargeable later) |
|--------------------------------|--------------------------------------------|
| ProcessView, milestones, stages, standard dialogs | Portfolio / cross-case overview (worklists, desktops) |
| Progression auditability, role enforcement (platform standard) | Advanced rules lifecycle beyond shipped blocks |
| **Shipped** Flow building blocks (activities, dialogs, patterns in product catalogue) | Custom work units / bespoke components outside catalogue |
| Standard process configuration within building-block boundaries | Self-service process modeling (Full Platform / Level 3) |
| | Advanced integration patterns beyond standard connectors |
| | Enterprise tier capabilities (§7) |

**Intent:** Pilot proves value on **standard, supportable patterns**; preserves monetization path for **Enterprise** and **capacity expansion** after evaluation.

**Delivery guardrail:** Pilot implementations compose processes from **shipped building blocks only** unless customer buys Enterprise, implementation add-on, or post-pilot expansion SKU.

### 11.3 Other pilot terms

| Element | Policy |
|---------|--------|
| **Goal** | Reference customers; **processes live**, not licences alone |
| **Services** | **Fixed implementation** scope per Playbook; primary pilot SKU: `FLOW-IMPL-2PROC` |
| **Exit** | Documented path to GA entitlement model + packs / Enterprise |
| **Messaging** | Structured flow, standardization, time-to-value; managed configuration before self-service modeling |
| **Pricing** | General Flow licensing remains unpublished in release notes; **implementation package** may be quoted when Enablement list price is published and sales kit is approved (D12) |

**Pilot success metrics (commercial):** # active process models live (≤2 without overage); signed delivery contract on every included-capacity deal; expansion path agreed in writing; no bespoke outside packages; building-block-only delivery unless explicitly upsold.

### 11.4 Limited introductory offer (2-process capacity)

| Element | Policy |
|---------|--------|
| **Offer** | **2 active process models** at no additional platform capacity fee |
| **Requires** | Signed **delivery contract** (`FLOW-IMPL-2PROC`) — capacity and implementation are a **bundle** |
| **Valid for** | Delivery contracts **signed on or before 31 December 2026** |
| **Subject to change** | Tieto may modify or withdraw before end date; Sales uses catalogue version at quote time |
| **Grandfathering** | Customers with signed delivery contract during offer period retain 2-process entitlement per contract term, even if go-live is after 31 December 2026 |
| **After expiry** | New deals follow GA catalogue (segment-based included N and/or packs — TBD) |
| **Sales kit** | Customer-facing detail: [`360_Flow_Implementation_Package_2Process_SalesKit_DRAFT.md`](360_Flow_Implementation_Package_2Process_SalesKit_DRAFT.md) |

---

## 12. Guardrails (non-negotiable)

| # | Guardrail |
|---|-----------|
| G1 | No bespoke promises outside standard packages |
| G2 | No feature-based discounting |
| G3 | Do not gate auditability, role enforcement, or basic lifecycle visibility behind Enterprise |
| G4 | Do not position Flow as standalone BPM vs Public 360° case platform |
| G5 | Do not promise Enterprise or Level 3 capabilities not on GA roadmap without dates |
| G6 | Every deal documents: org tier · process entitlement · capability level · implementation package · expansion path |
| G7 | Do **not** grant included process capacity **without** signed delivery contract (`FLOW-IMPL-2PROC` or documented equivalent) |
| G8 | Do **not** quote overage / capacity without contract terms for metering and invoicing (§5.5, sales kit E.6) |
| G9 | Do **not** promise limited 2-process offer beyond **31 December 2026** for unsigned deals |

**Sales checklist:** Use Playbook guardrail table; CRM fields in §6.3 must be populated before order. Confirm `flow_delivery_contract_signed` and `flow_limited_offer` for pilot deals.

---

## 13. Customer journey (reference)

**Prove → Expand → Mature**

1. **Prove** — Level 1 or pilot; one end-to-end process; fixed implementation.  
2. **Expand** — Level 2; more processes; packs; structured implementation per process.  
3. **Mature** — Level 3 + Enterprise; governance and modeling autonomy (GA features only).

**30-second pitch (reuse):** Unified platform; start with one process; add processes; upgrade for governance and modeling control — **without changing architecture**.

---

## 14. Open items (pre-GA blockers)

| ID | Item | Owner | Target date |
|----|------|-------|-------------|
| O1 | **Active process model** definition (§5.1) — core locked; edge cases O1b–O1e | Product | |
| O1b | Dedup rule: duplicate templates / same logical process | Product | **Locked:** strict count per model |
| O1c | Non-prod environments excluded from billing meter? | Product | **Locked:** production only |
| O1d | Process Engine / legacy workflow in Flow meter? | Product | **Locked:** excluded from Flow meter |
| O1e | Closed/archived cases — does model stay "active"? | Product | **Locked:** yes while case exists |
| O2 | Pilot locked at **2**; confirm **GA** segment model (5/10?) and pack sizes | Enablement + Finance | |
| O2b | Overage **unit price** and billing period | Enablement + Finance | **Billing basis locked:** monthly peak |
| R5 | Technical enforcement when exceeding entitlement | Product | **Locked:** contract + invoice only (pilot) |
| O2c | Customer visibility of active process count (report / portal / quarterly) | Product + Enablement | |
| O3 | Publish SKU IDs and price bands | Enablement | |
| O4 | CRM field names and entitlement reporting | Enablement / CRM | |
| O5 | Enterprise feature list ↔ GA roadmap lock | Product | |
| O6 | Process Engine migration / coexistence | Enablement + Finance | |
| O7 | Hosted Process SKU list + subscription billing path | Product + Enablement | |
| O8 | Finance ARPA model (small / large / state) | Finance | |
| O9 | Sales training + Playbook deck sync | Sales Enablement | |
| O10 | Pilot offer: confirm **31 Dec 2026** end date and max # pilot customers (if capped) | Product + Sales | |
| O11 | Legal sign-off on metering + overage invoicing clause (sales kit E.6) | Legal | |
| O12 | `FLOW-IMPL-2PROC` list price and delivery hours envelope | Enablement + Delivery | |

---

## 15. Revision history

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 DRAFT | 2026-05-26 | — | Initial spec from approved Hybrid direction in pricing deck |
| 0.2 DRAFT | 2026-05-26 | — | Pilot locked: **2** processes all segments; Foundation = **shipped building blocks only** |
| 0.3 DRAFT | 2026-09-10 | — | **Active process model** metering; delivery-contract gate; limited offer to 31 Dec 2026; overage invoicing; `FLOW-IMPL-2PROC`; sales kit linked |
| 0.3.1 DRAFT | 2026-09-10 | — | Locked O1b, O1c, O1e, O2b (monthly peak), R5 (contract-only enforcement) |
| 0.3.2 DRAFT | 2026-09-11 | — | Locked O1d (PE excluded from Flow meter); Playbook footnote + contract addendum linked |

---

*Internal use. Align with Enablement before catalogue, quotes, or customer-facing commitments.*
