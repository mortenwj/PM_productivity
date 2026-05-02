# Wiki investigation: Product First Request (PFR) and registering new functionality

**Source:** Public 360° wiki via MediaWiki MCP (read-only).  
**Date:** 2026-04-29

## Canonical process page

| Wiki page | Role |
|-----------|------|
| **[[Product first - Request new functionality]]** | End-to-end PFR process for *new functionality*: audience, flowchart, RACI table, DevOps registration, PM evaluation, customer communication, governance, change history. |
| **[[Product first - governance]]** | Redirects to the page above (same content). |

The **[[Product first]]** landing page is marked **{{Expired}}** (as of Dec 2023 per change history): *“Product First is now merged with Next Generation Public360, into Version 6.”* It still describes strategy, steering group, and Q&A, but **operational PFR steps live on** [[Product first - Request new functionality]].

## What the process is for

From the main page introduction:

- Handles **incoming client requests** and **internal ideas** related to **new functionality** (not standard configuration alone).
- Relates to **[[Product Development Process]]**, **[[Opportunity Management Process]]**, and **[[Upgrade process]]**.
- **Intended audience:** all Public 360° employees.

## High-level process (from the activity table)

1. **New requirement — understand request**  
   Confirm the need cannot be met by standard product + configuration (see [[Configuration Possibilities in 360°]], module overviews, existing board/dashboard history, **[[Product teams]]** for PM advice). **Output:** decision that reporting is justified.

2. **Report request new functionality** (including tenders)  
   Create a **Feature on the Azure DevOps Product First Requests board**, using the **work item template** linked from the wiki (example work item id **86204** referenced in wikitext).  
   **Bid rule:** one PFR **per bid/customer** even if requirement is similar; link as related.  
   **Fields / narrative expected** include: need and user scenarios, required functionality, history in prior versions / workarounds, consequences of not delivering, market potential, co-funding (**[[Customer financed product development]]**), **Source of Request** (upgrade, ServiceNow change order + order number, tender, internal SFI, etc.), priority `1` only with explanation.

3. **Evaluate request — decision (outcome)**  
   PM / BizDev / innovation boards / opportunity boards / innovation week. PM updates state and **Conclusion** (e.g. moved to roadmap → close PFR and create related core backlog item; idea bank → close and link to idea bank; tender path → **[[Opportunity Management Process]]**).

4. **Communicate decision to customer** (when request came via customer team)  
   PM/DM/solution consultant per RACI; no over-promising; strategic customer-plan discussion when heavily customized.

## How requests get “registered” (channels described on wiki)

| Channel | Wiki description |
|---------|------------------|
| **Azure DevOps — Product First Requests board** | Primary registration: create Feature from template; **Follow** the item for updates. |
| **ServiceNow (customer)** | Customers may report via ServiceNow; wiki states this **generates an automatic item** on the Product First board. |
| **Consultant / CIM path** | Change history **v2.0 (2025-02-19):** process updated so **customers register tickets processed by consultants** before items land on the internal Product First board. |
| **User association** | Customers can be referred to raise needs in their user association. |
| **Not PFR** | Actual defects → **[[Routine for customer bugs and assistance from R&D]]**. |

## SLAs and prioritization (guidelines)

- Expect **answer or preliminary answer within two weeks**; if urgent and no reply, escalate to area PM (**[[Product teams]]**) or Principal PM (Morten Jensen named in wikitext).
- **PM evaluation order:** (1) new bids/tenders, (2) upgrade projects, (3) change requests from existing customers.

## Documented outcomes

- Classified as **bug** → R&D bug routine.  
- **Yes, in product** (no fixed date) → roadmap feature in Azure DevOps.  
- **Yes, by a specific time** → tagged **Commitment**; visible in Commitments query (wiki: if not on list, not registered as commitment).  
- **Discovery** / **Idea bank** / **No** (with rationale).

## Related wiki pages worth cross-reading

| Page | Why |
|------|-----|
| **[[Commitments]]** | Defines commitments as **accepted PFRs** with dates; tagging (`Commitment`, `Conditional`), who may register, tender vs upgrade flows, links back to PFR creation. |
| **[[Innovation Process]]** | Customer requests transferred into innovation; references Product First Request Process. |
| **[[Technology&Development]]** | Lists PFR among T&D process library links. |
| **[[Consultancy]]** | “Create a Product First Request (new product functionality)”. |
| **[[Technical Consulting - architecture and development]]** | Mentions supporting **Product First Request Process**. |
| **[[Integration with 360°]]** | New outbound integration → follow PFR page. |
| **[[How to: Prestudy solution analysis]]** | If functionality need → create PFR per linked process. |
| **[[Upgrade process]]** | “Product first” strategy context + upgrade-related PFR linkage. |

## Artifacts on the wiki (not fetched as binary)

- Flowchart: `Pfr 20250219.png` (referenced 2025-02-19 process version).  
- PM evaluation guideline images: `PFR Guideline - PM evaluation.png`, `PFR Guideline - PM evaluation 2.png`.

## Gaps / consistency notes for your “broken process” exploration

- **Expired hub:** [[Product first]] still points to “[[Product first - governance|Product First Request Process]]” which redirects to the **live** PFR page — easy to confuse “expired” with “process retired.”
- **Version 6 merger** banner on [[Product first]] vs **active** procedure on [[Product first - Request new functionality]] (last touched **2026-01-16** in MCP revision timestamp) — clarify in org comms which narrative is authoritative for employees.
- **CIM / consultant triage (v2.0)** adds a step before the board; worth mapping to actual tooling (ServiceNow, CIM, DevOps) and where friction appears.

---

*Internal wiki link style in this doc uses MediaWiki titles for copy-paste into wiki search; live site is the Public 360° wiki host configured for the MCP.*
