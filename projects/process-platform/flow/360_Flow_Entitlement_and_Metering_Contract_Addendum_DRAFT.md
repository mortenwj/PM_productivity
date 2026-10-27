# 360° Flow — Entitlement and metering (contract addendum)

**Status:** DRAFT — for Legal review before customer use  
**Version:** 0.1  
**Date:** 2026-09-11  
**Owner:** Product (Flow / Process Framework)  
**Attach to:** Delivery contract / SOW for `FLOW-IMPL-2PROC` and underlying Public 360° subscription agreement  
**Source:** [`360_Flow_Commercial_Spec_v1.md`](360_Flow_Commercial_Spec_v1.md) §5, §11.4

> **Instructions:** Legal to adapt governing law, defined terms, and cross-references to the customer's master agreement. Replace `[TBD]` and `●` placeholders before execution.

---

## Contract appendix text (customer-facing)

*Suggested title: **Appendix [X] — 360° Flow process entitlement and metering***

---

### 1. Purpose

This Appendix sets out how **360° Flow** process **capacity** is entitled, measured, and invoiced for the Customer. It supplements the Delivery Contract dated `[DATE]` and the Customer's Public 360° agreement.

**Capacity fees** under this Appendix are separate from **implementation fees** for designing, configuring, and delivering processes.

---

### 2. Definitions

| Term | Meaning |
|------|---------|
| **360° Flow** | The Process Framework process-modelling and execution capability in Public 360° (process models, phases, checklists, milestones, ProcessView), as enabled for the Customer. |
| **Active process model** | A process model that is **(a)** **published** (available for operational use, not draft-only) and **(b)** has **at least one Case** connected to it in the **production environment**. |
| **Process entitlement** | The maximum number of Active process models the Customer may operate without additional capacity fees under this Appendix. |
| **Production environment** | The Customer's live operational Public 360° environment designated for case handling in production. Test, training, and other non-production environments are **excluded** from capacity metering. |
| **Monitoring** | Tieto's built-in platform capability that reports the count of Active process models in the Production environment. |

**Excluded from the Active process model count:** process models built and operated solely on **360° Process Engine** or legacy Workflow-only flows outside 360° Flow / Process Framework (if any remain in the Customer's environment).

---

### 3. Contracted entitlement (introductory pilot offer)

| Item | Value |
|------|-------|
| **Included process entitlement** | **2** Active process models |
| **Condition** | Applies because the Customer has signed the Delivery Contract for the **360° Flow Implementation Package (2 Processes)** (`FLOW-IMPL-2PROC` or equivalent) |
| **Capacity fee for included entitlement** | **None** (included for the contracted term) |
| **Introductory offer** | Available where the Delivery Contract was **signed on or before 31 December 2026**; offer terms are fixed at signature for this Customer |

If the Delivery Contract was signed after 31 December 2026, or no qualifying Delivery Contract exists, process entitlement and capacity fees follow the catalogue in effect at the time of order (**TBD** — Enablement to insert GA terms or remove this sentence).

---

### 4. How active process models are counted

An Active process model is counted when **both** are true:

1. The process model is **published**; and  
2. At least **one Case** is connected to that process model in the **Production environment**.

The following **do not** count:

- Published process models with **no** connected Cases  
- Unpublished (draft) process models, even if Cases exist elsewhere  
- Process models in non-production environments  
- 360° Process Engine-only or legacy Workflow-only flows (Section 2)

**Additional rules:**

- **Each** published process model with at least one connected Case counts as **one** Active process model, even if multiple models support the same type of work.  
- A process model remains Active while at least one connected Case **exists**, regardless of Case status (including closed or archived), unless the process model is **unpublished**.

---

### 5. Monitoring and measurement

1. Tieto measures the number of Active process models using **Monitoring** in the Production environment.  
2. For billing purposes, the count used is the **monthly peak** number of Active process models during each billing period.  
3. The Monitoring count is the **primary basis** for capacity billing under this Appendix, subject to the dispute process in the master agreement.  
4. **TBD** — Tieto will provide the Customer with `[quarterly statement / admin report / other]` showing Active process model count.

---

### 6. Fees for additional active process models

When the monthly peak count of Active process models **exceeds** the Process entitlement in Section 3:

| Element | Terms |
|---------|-------|
| **Charge** | **TBD NOK** per Active process model **above** entitlement, per **TBD** billing period (month / quarter / year) |
| **SKU** | `FLOW-CAP-OVG-1` or catalogue equivalent — **TBD** Enablement |
| **Duration** | Charged for each billing period in which the additional process model qualifies as Active |
| **Implementation** | Configuring and go-living an additional process requires a **separate implementation order** (e.g. `FLOW-IMPL-L2-PROC`) unless already covered by an agreed change order |

**Example (illustrative only):**

| Monthly peak — Active process models | Process entitlement | Additional (billable) |
|--------------------------------------|---------------------|------------------------|
| 2 | 2 | 0 |
| 3 | 2 | 1 |
| 4 | 2 | 2 |

---

### 7. Customer obligations

The Customer shall:

1. **Order capacity** before go-live when adding processes that will exceed Process entitlement.  
2. **Notify** Tieto **TBD** `[e.g. 14 days]` before go-live of a new Active process model that will exceed entitlement.  
3. **Unpublish** process models no longer in use if the Customer does not wish them to count toward Active process models (subject to Section 4).  
4. Not rely on test or training environments to avoid Production metering.

---

### 8. No technical capacity enforcement (pilot)

During the pilot phase, the platform may **not** technically prevent publication of process models beyond Process entitlement. The Customer remains liable for capacity fees under this Appendix. Tieto may invoice for excess Active process models identified through Monitoring.

---

### 9. Relationship to other agreements

| Topic | Rule |
|-------|------|
| **Implementation services** | Scoped in the Delivery Contract; not repeated here |
| **360° Process Engine** | Licensed and metered under separate terms; **not** included in Active process model count |
| **Hosted Processes** | If purchased, governed by separate subscription terms |
| **Platform support** | Standard Public 360° support applies to platform defects; process configuration changes are **consultancy** unless otherwise agreed |

---

### 10. Changes

Changes to Process entitlement or capacity fees require a **written amendment** or new order reference, except where introductory offer terms were fixed at Delivery Contract signature (Section 3).

---

### 11. Signatures

| | Customer | Tieto |
|---|----------|-------|
| **Name** | | |
| **Title** | | |
| **Date** | | |
| **Signature** | | |

---

## Legal / Enablement checklist (internal — remove before customer PDF)

| # | Item | Status |
|---|------|--------|
| 1 | Insert overage unit price and billing period (Section 6) | ☐ TBD |
| 2 | Insert customer notification period (Section 7) | ☐ TBD |
| 3 | Insert customer reporting mechanism (Section 5.4) | ☐ TBD |
| 4 | Cross-reference master agreement dispute and invoicing clauses | ☐ Legal |
| 5 | Confirm GA fallback text (Section 3) for post–2026 contracts | ☐ Legal |
| 6 | Norwegian translation if required for customer | ☐ Enablement |

---

## Revision history

| Version | Date | Changes |
|---------|------|---------|
| 0.1 DRAFT | 2026-09-11 | Initial addendum; O1d PE exclusion; locked metering rules |

---

*Internal use until Legal approval. Attach to delivery contract for `FLOW-IMPL-2PROC` deals.*
