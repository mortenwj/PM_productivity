# PM / Azure DevOps work items — MediaWiki extract

**Purpose:** Consolidated norms from Public 360° MediaWiki (via `user-mediawiki` MCP) for **Epics**, **Features**, and **User Stories** in Azure DevOps, plus related **development process** pages. Use when authoring or applying the `pm-ado-work-item-authoring` skill.

**Fetched:** 2026-04-22 — wikitext from live wiki; verify current revision if policy changes.

**Wiki base URL:** `https://wiki.software-innovation.com/wiki/` + MediaWiki page title (URL-encoded).

---

## 1. Canonical page index (prioritized)

| Topic | Wiki page |
|--------|-----------|
| **Epic / Feature / User Story / Task / Bug definitions, sprint ceremonies, Area/Iteration, acceptance criteria, DoD, risk in ADO** | [Sprints and Work Planning](https://wiki.software-innovation.com/wiki/Sprints_and_Work_Planning) |
| **Product intake → roadmap / Feature (PFR board)** | [Product first - Request new functionality](https://wiki.software-innovation.com/wiki/Product_first_-_Request_new_functionality) |
| **Support: registering User Story / Bug (Area, Iteration, Impacted module)** | [Registering Work Items in Azure DevOps](https://wiki.software-innovation.com/wiki/Registering_Work_Items_in_Azure_DevOps) |
| **Overall product + delivery process (being merged into PDP)** | [Development and Delivery Process](https://wiki.software-innovation.com/wiki/Development_and_Delivery_Process) |
| **Product Development Process hub (diamonds, sub-process links)** | [Product Development Process](https://wiki.software-innovation.com/wiki/Product_Development_Process) |
| **Test strategy, DoD for closing stories, bugs from test cases** | [Core-testing process](https://wiki.software-innovation.com/wiki/Core-testing_process) |
| **Customer team boards: Epic → Feature → sprint US → tasks** | [How to use Azure DevOps in Customer teams](https://wiki.software-innovation.com/wiki/How_to_use_Azure_DevOps_in_Customer_teams) |
| **Plan & Build product teams (PM creates Epic/Feature only; US on backlog not sprint)** | [Plan & Build 360° - Common way of work in product teams](https://wiki.software-innovation.com/wiki/Plan_%26_Build_360%C2%B0_-_Common_way_of_work_in_product_teams) |
| **Sales usage of Epic / User Story / Feature (different semantics than R&D)** | [Sales](https://wiki.software-innovation.com/wiki/Sales) |
| **Roll-up columns Epic/Feature/US** | [Azure DevOps tip: How to show Progress of Epic / Feature / User Story](https://wiki.software-innovation.com/wiki/Azure_DevOps_tip:_How_to_show_Progress_of_Epic_/_Feature_/_User_Story) |

**Related (search hits / PDP sidebar):** Product Development Process Set Up; 1st/2nd/3rd Diamond pages; Product Governance; Release Management Process (Overview); Routine for customer bugs and assistance from R&D; Commitments; Product teams; Module overview.

---

## 2. Work item types — **Sprints and Work Planning** (normative table)

### Epic

- **Product & R&D:** ambitious, linked to company mission / product vision (ideas from customers, tech leads, etc.).
- **Customer team:** contracted project (matches invoicing category): implementation / upgrade / orders (ServiceNow RITM), annual fee S&M, ASM, etc.
- **RACI:** Product Manager (product) / Project Manager (customer).
- **DoD:** all child types closed before closing Epic.

### Feature

- Backlog item breaking down an Epic — still high-level but more detail toward the Epic.
- **Customer team:** project phase or delivery (e.g. group of orders).
- **RACI:** Product Manager / Project Manager.
- **Acceptance criteria:** mandatory for **User Story**; **favourable** also on Features. Goals: clarify before work; shared understanding; know when story is complete; support automated tests. May include: negative scenarios; impact on other features; UX; functional/NFR; performance; roles affected; what system must not do; end-to-end flow; **concrete** criteria.
- **Definition of Done (shared for Feature and User Story):** team checklist before release each sprint (or continuously). Examples: feature complete; code complete; no known defects; regression done; user doc updated; seen/approved by PM or customer; production ready. **Public 360° concrete DoD:** all PRs reviewed; final testing on Test/QA before Close; bugs under story fixed; **functionality accepted by Product Manager**.

### User Story (US)

- Items in the **backlog “pick list”** for sprint planning.
- Often: story about **what the user is doing and why**; define together as a team; story maps help remote collaboration.
- **Sizing:** aim to close in **one sprint**; if not, create new US for next sprint, link, close the old one at sprint end. **Recommended max 2–3 days** per US.
- **ServiceNow / Robocop:** auto-created US; if **> 40h** effort, convert to appropriate work item type.
- **RACI:** any team member (creation).

### Task

- All activities to implement a US or bug (analysis, RCA, dev, test, auto-test, acceptance, deploy, doc, …). **US/bug cannot close until all tasks done**; use **NA** if activity not applicable.
- **Recommended estimate:** ~±4 h, **max 8–12 h** per task.

### Process notes (same page)

- Create **Feature** work item type for new features/enhancements; break into **small US** (max **3–4 days** each for analysis/design/dev/test).
- Create **child tasks** after US/bug; add estimates before setting Active; ensure analysis complete and no PM/TL/architect dependency surprises.
- **Traceability:** use **Related** links to parent Epic/Feature/US/Bug.
- **Design review (UI):** optional process with dedicated **User Story** on Core-UX board; English; tags; area `360\core\Core-UX-Design-Review`; etc.

### Risk (Azure DevOps fields)

- **Risk level** 1 = High, 2 = Medium, 3 = Low; **Risk description** when relevant.
- Consider on **Features, User Stories, and Bugs**; high risk needs mitigation documented before implementation.

---

## 3. **Registering Work Items in Azure DevOps** (support-focused)

- Audience: **support** (consistent registration of US and bugs).
- **Area path:** must align with **[Product teams](https://wiki.software-innovation.com/wiki/Product_teams)** (table in wiki for Bugs vs User Story / Request for Assistance per product team).
- **Iteration:** align with Area for reporters; teams adjust for sprint.
- **Title:** clear and descriptive.
- **Description — User story:** situation and concrete ask; be clear (“no one is brain-reader”).
- **Description — Bug:** repro steps; expected vs actual.
- **Planning:** Impacted module; priority; severity; link back to support ticket where applicable.

---

## 4. **Product first - Request new functionality** (PM / anyone)

- Create a **Feature** on [Product First Request board](https://dev.azure.com/tieto-si/360/_boards/board/t/Product%20First%20Requests/Features) using [template work item 86204](https://tieto-si.visualstudio.com/360/_boards/board/t/Product%20First%20Requests/Features/?workitem=86204).
- Template sections: specification (need, roles, functionality, history vs workarounds); consequences of not delivering; market potential; co-funding; source of request; critical priority needs explanation.
- Outcomes: bug path; roadmap Feature (no date); commitment (tag + commitments query); discovery; idea bank; no — with rationale.
- PM updates state/conclusion; may close PFR and create **related** core backlog item.

---

## 5. **Plan & Build 360° — Common way of work** (product-team variant)

- **PM/PDM creates Epics and Features only — not User Stories.**
- Features: focus on use cases (“As a case handler I want …”); **not** full UX (designer); **not** implementation how-to.
- Feature ready for dev: team meeting → **US with Feature as parent**; US **≤ ~3 days**; rough effort on feature; **all US linked to Feature**; **US stay on backlog, not placed on a sprint** until planning; US status **New**; keep backlog **1–2 sprints** ahead.
- Before sprint planning: PM prioritized backlog; no US on backlog that are not ready; all US have Feature parent (bugs may omit parent).
- Sprint planning: pull US/bugs from top; assign sprint + dev; **tasks on people**; estimates; keep New until work starts; **never create US on bugs** — use tasks.

*This differs from generic “Sprints and Work Planning” text (which allows PM-defined acceptance tasks on US). Reconcile by **team** (PnB vs Core) in the skill.*

---

## 6. **Core-testing process** (testing / DoD alignment)

- No code until **acceptance criteria / tests** defined; story not complete until acceptance tests pass; TDD where valuable.
- **DoD (testing):** final testing on **QA** before Close; **test tasks mandatory** on US; test cases documented in tasks; bugs linked under US must be fixed before close.

---

## 7. **Sales** (warning: different meanings)

| ADO type | Sales usage |
|----------|----------------|
| Epic | Sales case (RFP, upgrade SaaS, …) |
| User Story | Appendix / contract document |
| Task | RFP paragraph or concrete bid task |
| Feature (optional) | Evaluation criteria (price, quality, SLA, …) |

Minimum: maintain **Epic** task board per sales team. **Do not** mix this vocabulary into R&D product backlog skills without explicit context.

---

## 8. **Development and Delivery Process** (highlights)

- **Product** detail lives under **[Product Development Process](https://wiki.software-innovation.com/wiki/Product_Development_Process)**; this page is gradually merging/phasing.
- **Customer PM** responsibilities include: capacity in MyProject; **3-week sprints** aligned to calendar weeks; **area path per customer**; Epics/Features per templates; parent/child integrity (**stories** at minimum under Epic or area); ServiceNow/Robocop imports; planning US into sprints with hour budgets; sprint forums.
- Links: **Sprints and Work Planning**, pull requests, coding standards, deliveries, release management.

---

## 9. Further MediaWiki search (for maintenance)

Use MCP `mediawiki_search` with queries such as: `Azure DevOps`, `user story`, `Product Development Process`, `work item`, `backlog`, `sprint planning`. **Total hits vary**; filter out pages that only mention DevOps in passing (e.g. giant release notes).

---

## 10. Repo policy not duplicated on wiki

For **User Story** format scoring (As a / I want / so that, Gherkin AC, Risk field refs), the repository policy remains:

- `story_eval/copilot-instructions.md`
- Skill: `.cursor/skills/ado-user-story-quality/SKILL.md`

**Align the new PM skill:** wiki = process / hierarchy / fields / boards; `story_eval` = story text quality and JSON evaluation when needed.
