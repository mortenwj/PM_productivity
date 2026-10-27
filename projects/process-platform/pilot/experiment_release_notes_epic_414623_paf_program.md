# PAF program overview — Process Automation Framework (user-level draft)

> **Disclaimer:** This is an **internal draft** built from Azure DevOps epic text. It is **not** a signed-off customer brochure. It avoids implementation detail on purpose.

**Anchor epic:** [414623 – PAF – Process Automation Framework](https://dev.azure.com/tieto-si/360/_workitems/edit/414623) (project **360**).

**Scope of this document:** All **child epics** of 414623 **except** [**PAF – Discovery**](https://dev.azure.com/tieto-si/360/_workitems/edit/410862) (intake for ideas; excluded by request).

**Generated:** 17 April 2026 — sourced from live work item **titles** and **descriptions** in Azure DevOps.

---

## What the program is for (reader level)

**PAF** is the umbrella for turning **process automation** into something your organisation can **design, reuse, and run** in the product: cases move through **stages**, **processes**, and **milestones** in a predictable way, with shared building blocks so you do not reinvent the same automation for every customer.

The child epics below split that story into **platform**, **reusable content**, **experience**, **packaging**, and a **named pilot**—each described in everyday terms.

---

## Child epics (excluding Discovery)

### [PAF – Core Platform](https://dev.azure.com/tieto-si/360/_workitems/edit/411614) (411614) — *Active*

**What it does:** Provides the **foundation** the rest of PAF stands on: the machinery that **stores**, **versions**, and **runs** process definitions and automation so case workers see stable behaviour in production. Other epics add **libraries of ready-made flows** or **screens**; Core Platform is what keeps those definitions **trustworthy and executable** over time.

*Note:* The work item has **no long description** in DevOps at the time of export; wording above reflects its **title** and its relationship to the other epics.

---

### [PAF – Standard Artifacts](https://dev.azure.com/tieto-si/360/_workitems/edit/414328) (414328)

**What it does:** Builds a **shared library** of ready-to-use automation pieces—things like **process templates**, **stage templates**, **process definitions**, **rules**, and **shared configuration**—that consultants and customers can **pick up and combine** when they design a customer-specific process model. The emphasis is on **generic, reusable content** that many deployments can share, while still allowing local tailoring when a case needs it.

**In practice for users:** When someone configures a case type or phase, they can draw from a **catalog** of proven patterns instead of modelling every document flow, milestone, or decision from scratch.

---

### [PAF – User Experience (UX)](https://dev.azure.com/tieto-si/360/_workitems/edit/414727) (414727)

**What it does:** Improves **how people see and use** process automation in day-to-day work—both **administrators** who set up process models and **case workers** who run them. That includes clearer **screens for stages, processes, and milestones**, better **navigation** around process-related information, and smoother interaction when **configuring or using** process artefacts across the solution.

**Explicitly elsewhere (per DevOps):** The **data model**, **execution engine**, **trigger system**, **artifact repositories**, and **rule engines** stay under other epics; UX focuses on **presentation and interaction**.

---

### [PAF – Productization](https://dev.azure.com/tieto-si/360/_workitems/edit/411613) (411613)

**What it does:** Covers the work needed to treat PAF as a **repeatable product line**—how capabilities are **scoped, packaged, and delivered** so customers and partners know what they are buying and how it evolves. (The epic had **no detailed description** in DevOps at export; treat this sentence as a **placeholder** until Product fills the field.)

---

### [PAF – NVE Pilot](https://dev.azure.com/tieto-si/360/_workitems/edit/411612) (411612)

**What it does:** Tracks **pilot delivery** of PAF in the **NVE** customer context—rolling out the framework in a real programme, learning what works in production, and feeding that back into the broader PAF backlog. The work item is tagged **6.10** in DevOps (release alignment); it had **no long description** at export, so scope detail lives in linked **features and stories** under this epic.

---

## Full backlog tree (Feature → children)

The structure below mirrors **parent / child** links in Azure DevOps under each **child epic** of [414623](https://dev.azure.com/tieto-si/360/_workitems/edit/414623), still **excluding** [PAF – Discovery](https://dev.azure.com/tieto-si/360/_workitems/edit/410862). **Features** link to DevOps; bullets are **direct children** (user stories, bugs, or a nested **feature** where the backlog uses an extra level). Each line gives **work item type**, **title**, and **state** at export (**17 April 2026**).

### Under [PAF – Core Platform](https://dev.azure.com/tieto-si/360/_workitems/edit/411614) (411614)

#### [PAF – Export and import of Process models](https://dev.azure.com/tieto-si/360/_workitems/edit/252292) (252292) — New
- User story — UI: Import/Export of process models (New)
- User story — BL: Import/Export of process models (New)

#### [PAF – Quality initiatives](https://dev.azure.com/tieto-si/360/_workitems/edit/344868) (344868) — New
- User story — PM – Integration tests after feature toggle removal (New)
- User story — Move CreateMilestoneOnStage logic to MilestoneMetaHandlers (Closed)

#### [PAF – Process Models Performance Initiative (Backend, SQL)](https://dev.azure.com/tieto-si/360/_workitems/edit/397370) (397370) — Active
- User story — BEFORE ASYNC – PM – Performance – Analyse of ProcessModel cloning flow during case creation (New)
- User story — Started – PM – Performance – Identify instance-specific fields in cloned ProcessModel sub-entities (New)
- User story — PM – Performance – Investigate abnormal MilestoneConfig & StageProcessConfig row counts (New)
- User story — PM – Performance – Analyse of legacy StageTemplate behaviour and requirements for redesign – UseLatestVersion (Active)
- User story — PM – Milestone Performance – ValidateMilestoneUID (Closed)
- User story — PM – Performance – Analyze StageApi/GetAllStagesConnectedToCase for overfetching and unnecessary data (Closed)
- User story — TO FIX – PM – Performance – ProcessModelApi/GetProcessModelProperties for data reduction (Closed)
- User story — TO FIX Cache – PM – Performance – Analyze StageApi/CalculateDeadLine for unnecessary data loading (New)
- User story — PM – P360 – UI – Analyze all API calls executed during case UI load (New)
- User story — PM – Performance – Analyze StageApi/GetAllStagesWithAllowManualAdd for unnecessary data volume (Closed)
- User story — PM – Performance – Analyze ChecklistDefinitionView/GetChecklistByCasetype (Closed)
- User story — OK – PM – Performance – Analyze ChecklistInstanceView/GetChecklistThemeList (New)
- User story — TO FIX – PM – Performance – Analyze ChecklistInstanceView/GetMilestoneListByChecklist (New)
- User story — OK – PM – Performance – Analyze StageApi/SetStageWinterBreakErrorMsg (Closed)
- User story — PM – Performance – Analyze StageApi/GetAllStagesConnectedToCase (duplicate invocation) (Closed)
- User story — Frontend – PM – Performance – Analyze ProcessModelApi/GetProcessModelProperties (duplicate invocation check) (Closed)
- User story — PM – Performance – Analyze StageApi/GetAllStagesWithAllowManualAdd (duplicate check) (Closed)
- User story — PM – Performance – Analyze - Could we wait with creating the instances of the stac/milc/stapc until instantiation and get those from the templates (New)
- User story — PM –Performance – StageCalculations on MilestoneUpdates (Closed)

#### [PAF – Process Model Templates](https://dev.azure.com/tieto-si/360/_workitems/edit/402354) (402354) — New
- User story — Prevent customers from creating new versions of vendor supplied models/stage templates (New)
- User story — Implement auto scroll and highlight process model item in sidebar as per recno (Closed)
- User story — PMC – StageTemplate – TemplateState Validations and Logic (Closed)
- User story — Process Model templates interface (New)

#### [PAF – DB and Version Backed WorkUnit Framework](https://dev.azure.com/tieto-si/360/_workitems/edit/412681) (412681) — New
- User story — Implement initial DB (Closed)

#### [PAF – Localization Framework and Administration](https://dev.azure.com/tieto-si/360/_workitems/edit/414468) (414468) — New
- User story — WorkUnit – feature toggles should be configurable using the Management portal (Resolved)
- User story — WorkUnit Schema – Optional localized name, description, and categories (Closed)
- User story — WorkUnit Schema – Loading work units for specific customers (Closed)

#### [PAF – Core Platform – Trigger Data Model and Automation Relationships](https://dev.azure.com/tieto-si/360/_workitems/edit/414600) (414600) — New
- User story — PM – Trigger – BL – AutomationID validations (Closed)
- Bug — Milestone Automation ID should be unique message is not shown to user when given the same ID (Resolved)
- User story — PM – DB & Meta – Change to multi trigger system (New)
- User story — PM – Admin – React – New dialog for choosing (Parent) Trigger Automation ID (Pending)
- User story — PM – BL – Make sure AutomationIDs are uniqe across entities (Active)
- User story — PM – BL – Uncomment commented code (New)
- User story — PM – BL – Trigger all entities connected to triggering (parent) (New)
- User story — PM – Admin – BL – API for searching Automation IDs (Closed)
- User story — PM – Trigger – DB & Meta – Add AutomationID on MilestoneConfig (Closed)
- User story — PM – BL – Comment out code using TriggerAutomationId (Closed)
- User story — PM – Trigger – UI – Enable Automation ID on Milestone (Closed)

#### [PAF – Core Platform – Trigger Execution and Runtime Policies](https://dev.azure.com/tieto-si/360/_workitems/edit/414604) (414604) — New
- User story — Analysis Required: Manual stage Which is also trigger does not change the status from upcoming to in progress, instead is triggered again (New)
- User story — Analyze: Parent stage when added manually again and it has some trigger then Closing the Parent stage should again trigger the child stage. (New)
- User story — Triggers Should work according to Concurrency settings in admin (New)
- User story — Analysis: IsTriggered for StageConfig and StageProcessConfig is currently not supporting more than 1 instance (New)
- User story — Concurrency setting should be thought of when trigger functionality is invoked (New)
- Bug — Stage Process should be in Planned status if initiate as planned is checked in admin stage process config (New)
- User story — Keep Process Trigger Configuration when Creating Copy of Models, Stages, StageTemplates (New)
- Bug — Duplicate Process and milestones are created on the stage which is triggered by closure of the parent stage (New)

#### [PAF – Process Model Capabilities](https://dev.azure.com/tieto-si/360/_workitems/edit/414750) (414750) — New
- User story — UX – Design Process Model Capabilities Configuration UI (New)
- User story — React : Add process model capabilites tab with all configurable capabilites as a tile (Closed)
- User story — DB – Create data model for Process Model Capabilities (New)

#### [PAF – trigger milestone on document dispatch](https://dev.azure.com/tieto-si/360/_workitems/edit/417484) (417484) — New
- User story — Add document trigger on milestone config (Active)
- User story — Trigger milestone update on document dispatch or receive (New)

---

### Under [PAF – Standard Artifacts](https://dev.azure.com/tieto-si/360/_workitems/edit/414328) (414328)

#### [PAF – Artifacts – Process Definitions](https://dev.azure.com/tieto-si/360/_workitems/edit/400794) (400794) — New
- User story — Stage defined process – NOR "Mottak" – ENU "Received- Process" (New)
- User story — Stage defined process – "Saksbehandling" (New)
- User story — Stage defined process- "Vedtak" (New)
- User story — Stage defined process- "Sluttbehandling" (New)
- User story — Automation Activity when a application is received with document category " Application"- Create case with the correct process model and stage (New)
- User story — Major deficiency letter (New)
- User story — Minor Deficiency letter (New)
- User story — Minor defeciency – write notification (New)
- User story — Standard Process: Reject application (Active)
- User story — Autoreceipt (Active)
- User story — Create documment with review and approval (Resolved)
- User story — Process Withdrawn (Resolved)
- User story — Plan handling (New)
- User story — Register or update milestone (New)
- User story — Open URL with arguments (New)
- User story — Create process task (New)
- User story — Invoke subprocess as server action (Closed)
- User story — Add Application Master as an example in ProcessEngineToolkit (Closed)
- Bug — Adding a New Document Wizard on Xaml files, gives error on UI (New)
- Bug — Adding new workflow on a xaml file , gives error on UI (New)
- Bug — Spelling mistake in Default document title (Active)
- Bug — Error message should be user friendly if user forgets creating the contact role while creating case with process model (Active)
- Bug — Dispatch dialogue should show Print as the default option if Dispatch channel is selected as Print in work unit (New)
- Bug — Process is initiated even if it is marked as Upcoming (New)
- Bug — After the dispatch of the Receipt the process should be closed automatically (New)
- Bug — Document should be connected to stage entity and shown in the third column for the selected stage (New)

#### [PAF – Artifacts – Deadline Calculation Types](https://dev.azure.com/tieto-si/360/_workitems/edit/411623) (411623) — New
- Bug — Milestones do not control time logging correctly on deadline calculation type "Calculate from Start/Finish milestones" (New)
- User story — MilestoneConfig – Default Calculation type – Update (New)

#### [PAF – Artifacts – Process Model Templates](https://dev.azure.com/tieto-si/360/_workitems/edit/414342) (414342) — New
- *(No child items on the hierarchy link; this feature is cross-related to sibling artifact features in DevOps.)*

#### [PAF – Artifacts – Stage Templates](https://dev.azure.com/tieto-si/360/_workitems/edit/414343) (414343) — New
- *(No hierarchy children; cross-related to other artifact features.)*

#### [PAF – Artifacts – Rule Sets (Yes, it might be needed)](https://dev.azure.com/tieto-si/360/_workitems/edit/414344) (414344) — New
- *(No hierarchy children; cross-related to other artifact features.)*

#### [PAF – Artifacts – Shared Supporting Artifacts](https://dev.azure.com/tieto-si/360/_workitems/edit/414345) (414345) — New
- User story — Invoke subprocess (New)

#### [PAF – Artifacts – Standard Checklist](https://dev.azure.com/tieto-si/360/_workitems/edit/414351) (414351) — New
- User story — Add default outcome types (Closed)

#### [PAF – Artifacts – ProcessEngine – Designer Components](https://dev.azure.com/tieto-si/360/_workitems/edit/414353) (414353) — Active
- User story — Dispatch dialogue (New)
- User story — PE Designer Component – Create a Stage (Closed)
- User story — PE deigner create designer action for notification (Active)
- User story — PE designer: Create appointment (New)
- User story — Support Stage pre-selection in New Document Wizard and Dialog when opened from Process Engine client action (Closed)
- User story — PE designer component – email dialogue (New)
- Feature — PE Designer Component – Create new process (230801) — Closed
  - User story — PE Designer Component – Extend server action to support params (New)
  - User story — Create method for creating a new process instance from a stageConfig (Closed)
  - User story — Create "one-liner" for creating a new process instance from a process (Closed)

#### [PAF – Artifacts – HOW TO](https://dev.azure.com/tieto-si/360/_workitems/edit/414386) (414386) — New
- *(No hierarchy children; related to Process Definitions work in DevOps.)*

#### [PAF – Artifacts – Standard Milestones](https://dev.azure.com/tieto-si/360/_workitems/edit/414516) (414516) — New
- Bug — Milestone recno 201- "Tilleggsdokumentasjon etterspurt – vesentlig mangel" – description appears 2 times (New)
- User story — PMC – DB – Add standard milestones (Closed)
- User story — PMC – DB – Expire required Case Type on MilestoneTypes (Closed)
- Bug — Missing standard milestone- Nor-"Trukket søknad" ENU-"Withdrawn application" (New)

#### [PAF – Artifacts – Milestone status](https://dev.azure.com/tieto-si/360/_workitems/edit/415983) (415983) — New
- User story — Add standard milestone status (Closed)

#### [PAF – Artifacts – Contact – Case roles](https://dev.azure.com/tieto-si/360/_workitems/edit/415986) (415986) — New
- User story — Add standard contact – case roles (Closed)

#### [PAF – Artifacts – Shortcoming status](https://dev.azure.com/tieto-si/360/_workitems/edit/415991) (415991) — New
- User story — add shorcmong statuses (Closed)

#### [PAF – Artifacts – Condition status values](https://dev.azure.com/tieto-si/360/_workitems/edit/415993) (415993) — New
- User story — add condition statuses (Closed)

#### [PAF – Artifacts – Document Categories](https://dev.azure.com/tieto-si/360/_workitems/edit/415996) (415996) — New
- User story — Add document categories (Resolved)

#### [PAF artifacts : create email](https://dev.azure.com/tieto-si/360/_workitems/edit/418321) (418321) — New
- User story — new email dialogue (New)
- User story — email creation dialogue (New)
- User story — Email client action (New)

#### [PAF artifacts : create Appontment](https://dev.azure.com/tieto-si/360/_workitems/edit/418326) (418326) — New
- User story — appointment creation dialogue (New)
- User story — Outlook invite client action (New)

---

### Under [PAF – User Experience (UX)](https://dev.azure.com/tieto-si/360/_workitems/edit/414727) (414727)

#### [PM – P360 – Support for editing- and add new milestones on closed stages](https://dev.azure.com/tieto-si/360/_workitems/edit/399007) (399007) — New
- User story — PM360 – Urestricted Milestones – Edit Milestones on a Closed Stage (Closed)
- User story — PM360 – Urestricted Milestones – Add Milestones on a Closed Stage (New)
- Bug — Edit milestones dialog on a close stage – Localization Text should be Corrected. (Closed)

#### [PAF – UI/UX – Minor improvements](https://dev.azure.com/tieto-si/360/_workitems/edit/403959) (403959) — New
- User story — PM360 – UI – Align labels mentioning process models (New)
- User story — PAF – CaseView – Consistent Button Design on Case Views (New)
- User story — PMC – Entity Order – Design | UX (New)
- User story — Show em dash (—) for unpublished versions in Published field (New)
- User story — Display version number next to process model titles (New)
- User story — PMC – Admin – Visual Ordering of Autogenerated Entities in the ProcessModelAdmin Treeview (Active)
- User story — Edit icon is shown in historical (archived) view + Calculation days field is still interactive (New)
- User story — Change floppy "Save" icon to new icon from BP DS (Closed)
- User story — Remove leading asterisk (*) from texts in Stage Templates view (New)

#### [PMC – Admin – Stage defined Process – Select Workflow definition](https://dev.azure.com/tieto-si/360/_workitems/edit/410828) (410828) — New
- User story — Compose new design (New)
- User story — UI – Admin panel – Create Extended Search Dialog for Workflow Definition Dropdown in Process Property (Closed)
- Bug — Sorting for the Name and Category field is not working in Search Workflow definition table (New)

#### [Worklists — Case processing phases & deadlines (Caseworker + Department desktops)](https://dev.azure.com/tieto-si/360/_workitems/edit/411634) (411634) — New
- *(No hierarchy children in DevOps at export; scope is described on the feature itself.)*

---

### Under [PAF – Productization](https://dev.azure.com/tieto-si/360/_workitems/edit/411613) (411613)

#### [PM – Documentation](https://dev.azure.com/tieto-si/360/_workitems/edit/272200) (272200) — New
- User story — Update main doc (New)
- User story — Wiki content update (Active)

#### [PMC – Admin – 12 – Process Model Statistics Tab](https://dev.azure.com/tieto-si/360/_workitems/edit/380663) (380663) — New
- User story — Design for Process Models Monitoring (New)
- User story — Implement SQL-script for invoicing (Closed)

---

### Under [PAF – NVE Pilot](https://dev.azure.com/tieto-si/360/_workitems/edit/411612) (411612)

#### [Send e-mail and outlook invitations from prosess in Plan and Build.](https://dev.azure.com/tieto-si/360/_workitems/edit/390288) (390288) — New
- *(No hierarchy children; DevOps links this feature as a duplicate of work item 279724.)*

#### [In a process model, customers want to be able to change what is set up in a case processing phase](https://dev.azure.com/tieto-si/360/_workitems/edit/400798) (400798) — New
- *(No child backlog items linked under hierarchy.)*

#### [Varsel når oppgave er utført eller kommentert](https://dev.azure.com/tieto-si/360/_workitems/edit/412778) (412778) — New
- *(No child backlog items linked under hierarchy.)*

#### [NVE Specific process definitions before go-live](https://dev.azure.com/tieto-si/360/_workitems/edit/413948) (413948) — New
- User story — NVE Process: Announcement (Active)
- User story — NVE Process: Final processing (New)
- User story — NVE Process: Consultation and inspection (New)
- User story — NVE Process: Processing of objections (New)
- User story — NVE Process: Hearing (Active)
- User story — NVE Process: Make decision (New)

---

## Traceability

| Epic | ID | State (at export) |
|------|-----|-------------------|
| PAF – Core Platform | [411614](https://dev.azure.com/tieto-si/360/_workitems/edit/411614) | Active |
| PAF – Standard Artifacts | [414328](https://dev.azure.com/tieto-si/360/_workitems/edit/414328) | New |
| PAF – User Experience (UX) | [414727](https://dev.azure.com/tieto-si/360/_workitems/edit/414727) | New |
| PAF – Productization | [411613](https://dev.azure.com/tieto-si/360/_workitems/edit/411613) | New |
| PAF – NVE Pilot | [411612](https://dev.azure.com/tieto-si/360/_workitems/edit/411612) | New |
| *Excluded: PAF – Discovery* | [410862](https://dev.azure.com/tieto-si/360/_workitems/edit/410862) | New |

---

## Suggested next steps (if you extend this experiment)

- Pull **ADO Test Plans / test cases** linked to the stories above for **expected behaviour** in reviewer language.
- Optionally add **GitHub** only where **Development** links are clean, to confirm wording against shipped examples.
- For artifact features **414342–414344** that only use **Related** links today, add hierarchy children when backlog decomposition is ready so the tree stays navigable from the epic alone.

---

_End of program-level experiment — epic 414623, Discovery omitted; includes Feature → child backlog tree from live DevOps parent links._
