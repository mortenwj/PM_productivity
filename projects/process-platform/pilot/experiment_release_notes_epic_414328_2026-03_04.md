# Draft release overview — Standard process artifacts (PAF)

> **Disclaimer:** This document is an **automated draft** generated from Azure DevOps work items (English, customer-facing wording). It is **not** a signed-off release communication. Internal fields, attachment links, and assignee identities from the work tracking system are intentionally omitted.

**Scope:** Deliveries under the **PAF – Standard Artifacts** initiative ([Azure DevOps epic 414328](https://dev.azure.com/tieto-si/360/_workitems/edit/414328)) with work items in **Resolved** or **Closed** state whose **release timestamp** falls in **March 2026 or April 2026** (using `ResolvedDate` for Resolved items and `ClosedDate` for Closed items, per your rules).

**Program context:** This initiative is part of the broader **Process Automation Framework (PAF)** program ([parent epic 414623](https://dev.azure.com/tieto-si/360/_workitems/edit/414623)). Standard artifacts are reusable building blocks—definitions, templates, and configuration data—that help organizations deploy consistent process automation on top of the PAF platform.

---

## Data access note (GitHub)

The **GitHub MCP** token is **authorized for `te-industry-public360`** (SAML). For repository **[`te-industry-public360/core-bl`](https://github.com/te-industry-public360/core-bl)**, file contents and pull requests were reviewed **17 April 2026**.

**Caveats for release owners:** Azure DevOps **Development** links are not always aligned with the story title. Where GitHub shows **open** or **closed without merge**, that is the repository state at review time.

**Repository mapping:** Unless a story says otherwise, PR links below use `core-bl`.

---

## Evidence and methodology (including tests)

**Goal:** Describe **observable behaviour** for release readers, not implementation detail. Prefer sources in this order, and **merge** them when they agree; when they disagree, say so explicitly.

1. **Azure DevOps — work item**  
   Title, description, acceptance criteria, and **parent** links set the intended scope.

2. **Azure DevOps — test cases** *(you asked to add this explicitly)*  
   Link or embed **Test Case** work items (and suites / plans if your process uses them) that are **linked to the story or feature**. Their **title and steps** often spell out **given / when / then** behaviour in language close to what testers and customers care about.  
   *Tip:* In ADO, use **Links** (e.g. *Tested By*, *Related*, or test-plan associations) from the user story outward, not only **Development** → GitHub.

3. **GitHub — merged change**  
   Use the **Development** link to resolve **repo + PR**, then read the **merge commit** (or equivalent release branch). Process models (e.g. **`.wu`** argument `comment` text) remain the best **in-repo** product hints for PAF artefacts.

4. **GitHub — automated tests** *(same priority as “nearby product code” for behaviour)*  
   For each PR, scan **added or modified test files** (common patterns: `*Test.cs`, `*.spec.ts`, `Tests/`). **Test method names**, **`[TestMethod]` / `[Fact]` descriptions**, and **Arrange / Act / Assert** blocks encode **expected behaviour** and edge cases (e.g. “clears org unit when zero”, “throws when neither id set”).  
   *Concrete examples in `core-bl` for this epic’s neighbourhood:* tests around **`NewDocumentDialogClientAction`** ([`NewDocumentDialogClientActionTest.cs`](https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessPlatform.UnitTest/ProcessEngine/Runtime/ProgressPlan/NewDocumentDialogClientActionTest.cs) and sibling projects), **`NewDocumentActionDataAdapterTest.cs`**, and [`ProgressPlanHandlerTest.cs`](https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessPlatform.UnitTest/ProcessEngine/Support/ProgressPlanHandlerTest.cs) (e.g. responsibility / org-unit update rules shipped with subprocess work).  
   Use tests to **validate** and **extend** “What it does”; strip type names and assertion API noise when writing for non-developers.

5. **Gap handling**  
   Where ADO titles, test cases, and GitHub disagree—or GitHub has **no** tests for the linked PR—call that out as **traceability or coverage debt** instead of smoothing it over.

**What this draft actually used:** Work-item wording, **`.wu`** configuration comments, a small amount of **production** C# summary text, and **PR-level** GitHub metadata. It did **not** yet systematically pull **ADO Test Case** steps or full **test class** narratives into each bullet; that is the recommended next enrichment pass before you treat the document as complete.

---

## Deliveries by feature area

### PAF – Artifacts – Process Definitions

- **Create document with review and approval** (Resolved; April 2026)

  **What it does:** The updated **standard document-creation** process model is a reusable **progress-plan / stage** automation. A case worker or automated step drives the case through **creating an outgoing document** and, only where you turn the switches on, through **review**, **approval**, **dispatch**, and **milestone registration**.

  In more detail (wording taken from the embedded configuration comments on the shipped model): you choose **which contact–case role** the document is anchored to (defaulting to applicant-style usage), whether a **public access** group applies, which **archive** stores the document, which **outgoing document category** applies, what users should see as the **header** and the **public title**, and which **template** shapes the document body.

  Optional **review** asks whether the document should be sent for review, supplies a **default title** when it is sent for review, and sets **how many calendar days** reviewers have. Optional **approval** does the same pattern for an approval round (yes/no, default title, **calendar-day** horizon). Optional **dispatch** asks whether the document should be sent out through a channel chosen from your **dispatch-channel** catalog. Optional **milestone handling** asks whether a milestone should be created, lets you pick the **milestone type** from the standard list, and sets the **action title** that should appear on that milestone.

  **Linked engineering:** [`core-bl`](https://github.com/te-industry-public360/core-bl) PRs [#19591](https://github.com/te-industry-public360/core-bl/pull/19591), [#19753](https://github.com/te-industry-public360/core-bl/pull/19753) (plus related commits as linked on the work item in Azure DevOps).

- **Add Application Master as an example in ProcessEngineToolkit** (Closed; March 2026)

  **What it does:** In **`core-bl`**, pull request **#19** only adds a **JSON library dependency** to an unrelated component area. It does **not**, in this repository snapshot, add an “Application Master” toolkit example. Treat the **Application Master** outcome as **not demonstrated by this link** until the Azure DevOps **Development** section points at the correct repository and pull request.

  **Linked engineering:** [`core-bl`](https://github.com/te-industry-public360/core-bl) PR [#19](https://github.com/te-industry-public360/core-bl/pull/19).

- **Process Withdrawn** (Resolved; April 2026)

  **What it does:** The **standard withdrawn-document** process model mirrors the same **document setup** ideas as creation—**contact role on the case**, **public access**, **archive**, **outgoing category**, **header text**, **public document title**, and **template**—and offers the same style of optional **review**, **approval**, and **dispatch** questions (each with titles and **calendar-day** horizons where relevant, and a **dispatch channel** when dispatch is used).

  For **milestones on withdrawal**, the shipped argument list exposes **which milestone type** to use and the **action title** for that milestone (the withdrawal model does not use the same separate “create milestone yes/no” switch text as the creation model; milestone behaviour is expressed through those fields instead).

  **Linked engineering:** [`core-bl`](https://github.com/te-industry-public360/core-bl) PRs [#19591](https://github.com/te-industry-public360/core-bl/pull/19591), [#19753](https://github.com/te-industry-public360/core-bl/pull/19753).

- **Invoke subprocess as server action** (Closed; March 2026)

  **What it does:** Adds a **server action** named **Create subprocess** so a running process can **start a child process** on the current case progression. The person configuring the action chooses **which automation** should run as the child, can give the child a **visible title**, and can **leave responsibility unchanged**, **copy it from the parent**, **set a specific person or organisational unit**, or **clear** responsibility according to the same semantics described beside each field in the shipped definition. The definition also reserves a **“deadline after N days”** idea for the child; the shipped workflow notes that this part is **not implemented yet**—so planners should not rely on automatic child deadlines from this action until a later delivery completes that behaviour.

  **Linked engineering:** [`core-bl`](https://github.com/te-industry-public360/core-bl) PR [#19476](https://github.com/te-industry-public360/core-bl/pull/19476).

---

### PAF – Artifacts – Standard Checklist

- **Add default outcome types** (Closed; March 2026)

  **What it does:** The linked pull request **does not** change checklist outcomes. It **removes an obsolete document-archive macro** from API code paths (the engineering description is about **document archive handling**, not checklists). The **“default outcome types”** intent of the story is **not reflected** in this GitHub change—correct the Azure DevOps link or supplement with the real delivery repository.

  **Linked engineering:** [`core-bl`](https://github.com/te-industry-public360/core-bl) PR [#9371](https://github.com/te-industry-public360/core-bl/pull/9371).

---

### PAF – Artifacts – ProcessEngine – Designer Components

- **PE Designer Component – Create a Stage** (Closed; March 2026)

  **What it does:** *(No pull request was linked on this user story in Azure DevOps at export; text unchanged from work-item summary.)* Strengthens **stage-based case handling** by enabling a first-class **“create stage”** building block in the Process Engine designer—reducing the need to spin up separate processes when advancing a case through multiple stages.

  *No GitHub pull request was linked on this user story in Azure DevOps at the time of export.*

- **Support Stage pre-selection in New Document Wizard and Dialog when opened from Process Engine client action** (Closed; April 2026)

  **What it does:** The runtime for the **New document** client action is documented in code as the handler that **builds the link and supporting data** for opening the new-document experience. The change under review extends the **XML payload** that is passed when a document-flow dialog or related invoker runs so it carries **which case stage** the new document belongs to—not only process identity, dialog title, and document title. Practically, that means when staff open the **new document wizard** from a Process Engine action, downstream steps can **respect the active stage** instead of losing stage context. At snapshot date the pull request was still **open** on GitHub; confirm merge and release branch with your engineering team.

  **Linked engineering:** [`core-bl`](https://github.com/te-industry-public360/core-bl) PR [#19718](https://github.com/te-industry-public360/core-bl/pull/19718).

- **PE Designer Component – Create a Milestone Dialog in Case Handling view** (Resolved; March 2026)

  **What it does:** The linked pull request in **`core-bl`** concerns **file-format blacklist checks** in a surface/API layer, not the milestone dialog described by the story. There are **no process-model comments** here that explain milestone dialog behaviour. Validate the **Development** link; until then, rely on the Azure DevOps story text: a **case-handler milestone creation** experience driven by the process definition (labels, descriptions, optional status and custom naming, required fields, and date rules).

  **Linked engineering:** [`core-bl`](https://github.com/te-industry-public360/core-bl) PR [#14132](https://github.com/te-industry-public360/core-bl/pull/14132).

---

### PAF – Artifacts – Standard Milestones

- **PMC – DB – Add standard milestones** (Closed; March 2026)

  **What it does:** The four linked changes do **different jobs**; none is solely “seed a milestone catalog” in GitHub’s own titles:

  - One adjusts **deadline behaviour on a phase** in an estate-style **sectioning** process (extra argument for deadline handling).
  - One is a **code hygiene** change (replacing a common string conversion pattern flagged by static analysis).
  - One fixes **how milestone types are ordered** when they appear beside **checklist** configuration: the list follows each type’s **administrator-defined sort order** instead of sorting alphabetically by description—so what staff see matches the order you configured in the milestone-type catalog.
  - One tightens **when a “signed” date may be applied** for documents created through an **IFAR-related** path (ignoring certain sign-off updates when the request is IFAR-specific).

  Treat the story as an **umbrella** and map each bullet above to the correct work item child if you need a customer-safe narrative per change.

  **Linked engineering:** [`core-bl`](https://github.com/te-industry-public360/core-bl) PRs [#9367](https://github.com/te-industry-public360/core-bl/pull/9367), [#9369](https://github.com/te-industry-public360/core-bl/pull/9369), [#9372](https://github.com/te-industry-public360/core-bl/pull/9372), [#9419](https://github.com/te-industry-public360/core-bl/pull/9419) (multiple PR links recorded on the work item).

- **PMC – DB – Expire required Case Type on MilestoneTypes** (Closed; April 2026)

  **What it does:** Combines the **milestone-type ordering** fix above (sort by configured **sort id** in checklist context), a **service-delivery / address-validation** change (return-address validation in the SDP v2 flow), and a **short pair of backend fixes** (“fix breaking method” then “refix method”) where the first attempt was **closed without merge** and the follow-up **merged**. Net effect for milestone administration: behaviour around **milestone types and related backend rules** was corrected after an initial incompatible change. For correspondence workflows, **address validation** behaviour in the SDP v2 path was touched. Use Azure DevOps for the exact business rule you marketed to customers.

  **Linked engineering:** [`core-bl`](https://github.com/te-industry-public360/core-bl) PRs [#9372](https://github.com/te-industry-public360/core-bl/pull/9372), [#9402](https://github.com/te-industry-public360/core-bl/pull/9402), [#19536](https://github.com/te-industry-public360/core-bl/pull/19536), [#19538](https://github.com/te-industry-public360/core-bl/pull/19538).

---

### PAF – Artifacts – Milestone status

- **Add standard milestone status** (Closed; March 2026)

  **What it does:** *(No pull request was linked on this user story in Azure DevOps at export; text unchanged from work-item summary.)* Adds a **standard set of milestone status** values across environments (reusing existing identifiers where applicable) for consistent milestone reporting.

  *No GitHub pull request was linked on this user story in Azure DevOps at the time of export.*

---

### PAF – Artifacts – Contact – Case roles

- **Add standard contact – case roles** (Closed; March 2026)

  **What it does:** The linked change **adds logging when a document is signed off during creation**—useful for audit trails of **sign-off at creation time**. It does **not**, in GitHub’s description, add or reorganise **contact–case role** catalog entries. Reconcile the story with the correct pull request before customer communication.

  **Linked engineering:** [`core-bl`](https://github.com/te-industry-public360/core-bl) PR [#9370](https://github.com/te-industry-public360/core-bl/pull/9370).

---

### PAF – Artifacts – Shortcoming status

- **Add shortcoming statuses** (Closed; March 2026)

  **What it does:** Same GitHub change as **Add standard contact – case roles** above (sign-off logging at document creation). The **shortcoming status** catalog work is **not described** by this pull request in GitHub.

  **Linked engineering:** [`core-bl`](https://github.com/te-industry-public360/core-bl) PR [#9370](https://github.com/te-industry-public360/core-bl/pull/9370).

---

### PAF – Artifacts – Condition status values

- **Add condition statuses** (Closed; March 2026)

  **What it does:** Same GitHub change as **Add standard contact – case roles** above (sign-off logging at document creation). The **condition status** catalog work is **not described** by this pull request in GitHub.

  **Linked engineering:** [`core-bl`](https://github.com/te-industry-public360/core-bl) PR [#9370](https://github.com/te-industry-public360/core-bl/pull/9370).

---

## Feature areas with no customer-visible deliveries in this period

The following **epic-level feature buckets** did not have **user stories** meeting the March/April 2026 Resolved/Closed date rule under strict **parent/child** hierarchy during this export:

- **PAF – Artifacts – Process Model Templates**
- **PAF – Artifacts – Stage Templates**
- **PAF – Artifacts – Rule Sets (Yes, it might be needed)**
- **PAF – Artifacts – Shared Supporting Artifacts** *(child story work remained outside the date/state filter)*
- **PAF – Artifacts – HOW TO**
- **PAF – Artifacts – Deadline Calculation Types**
- **PAF – Artifacts – Document Categories** *(active child work did not meet the Resolved/Closed + date filter)*
- **PAF artifacts : create email**
- **PAF artifacts : create Appontment**

---

## Appendix — GitHub PR verification (`core-bl`)

Snapshot **17 April 2026**. **Merged** is taken from GitHub’s merge indicator on each pull request.

| PR | State | Merged | Title (GitHub) |
|----|--------|--------|----------------|
| [19](https://github.com/te-industry-public360/core-bl/pull/19) | closed | Yes | Fixed Newtonsoftversion issue |
| [9367](https://github.com/te-industry-public360/core-bl/pull/9367) | closed | Yes | eEstate - sectioningprocess - New argument for deadline on phase |
| [9369](https://github.com/te-industry-public360/core-bl/pull/9369) | closed | Yes | Sonar issue :- Convert.ToString method replaced |
| [9370](https://github.com/te-industry-public360/core-bl/pull/9370) | closed | Yes | Added log for signing off document while document creation |
| [9371](https://github.com/te-industry-public360/core-bl/pull/9371) | closed | Yes | Removed [(DocumentArchive)] macro from API code which is not required |
| [9372](https://github.com/te-industry-public360/core-bl/pull/9372) | closed | Yes | Bug:224452 BL - Sorting updation for Milestone type list |
| [9402](https://github.com/te-industry-public360/core-bl/pull/9402) | closed | Yes | SDPv2 - Return Address Validation |
| [9419](https://github.com/te-industry-public360/core-bl/pull/9419) | closed | Yes | Changes to check and ignore the set to signed of date in case it's a request for IFAR |
| [14132](https://github.com/te-industry-public360/core-bl/pull/14132) | closed | Yes | Add Surface callable method for IsFileFormatBlacklisted |
| [19476](https://github.com/te-industry-public360/core-bl/pull/19476) | closed | Yes | Server Action for CreateSubProcess and dorrect SetResponsibe method |
| [19536](https://github.com/te-industry-public360/core-bl/pull/19536) | closed | **No** | Fix breaking method |
| [19538](https://github.com/te-industry-public360/core-bl/pull/19538) | closed | Yes | Refix method |
| [19591](https://github.com/te-industry-public360/core-bl/pull/19591) | closed | Yes | First Draft Version Of Document Process Handling Including Creation and Withdrawn |
| [19718](https://github.com/te-industry-public360/core-bl/pull/19718) | open | **No** | BL Document Dialog, the ProcessDataOnInvoker is missing the stage Rec… |
| [19753](https://github.com/te-industry-public360/core-bl/pull/19753) | closed | Yes | Added updated version for the Creation and withdrawal process along with shared component. |

---

## Traceability

- **Primary epic:** [414328 – PAF – Standard Artifacts](https://dev.azure.com/tieto-si/360/_workitems/edit/414328)
- **Parent program epic:** [414623 – PAF – Process Automation Framework](https://dev.azure.com/tieto-si/360/_workitems/edit/414623)
- **GitHub baseline repo for this draft:** [`te-industry-public360/core-bl`](https://github.com/te-industry-public360/core-bl) — PR metadata and file comments reviewed **17 April 2026** (see appendix).

---

_End of experiment run — generated for internal evaluation of auto-generated customer release notes._
