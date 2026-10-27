# 360 Flow — PRD Reconstruction Consolidated v3

## Status

This is the consolidated reconstruction of the 360 Flow PRD after iterative review, runtime refreshes, governance analysis, UX analysis, and scenario validation.

It is intentionally written as an operational product document, not a short strategy note.

---

## 0. Canonical Product Model & Terminology

360 Flow is a governed operational execution environment for public-sector administration.

### Canonical terminology

| Term | Meaning |
|---|---|
| **360 Flow** | Product and customer-facing capability umbrella |
| **Flow Runtime** | Execution and orchestration infrastructure |
| **Process Model** | Structural administrative lifecycle |
| **Process / Progress Plan** | Executable operational Flow |
| **Activity** | Operational execution primitive |
| **Dialog** | Structured operational interaction |
| **Work Unit** | Runtime execution definition |
| **Rules** | Operational governance semantics |
| **Flow Workspace** | Operational execution surface |
| **Portfolio Management** | Operational overview and control |
| **Governed Flow Building Blocks** | Reusable operational building blocks |
| **Hosted Process** | Commercial / service delivery layer |

### Core product principle

Standardized operational semantics with governed configurability.

### Core product interpretation

360 Flow is not a generic BPM system. It is a Public 360-native operational layer for end-to-end administrative Flow execution, lifecycle progression, governance, overview, and reusable operational behavior.

---

## 1. Product Context

360 Flow extends Public 360 with:
- lifecycle-aware process execution,
- process-oriented operational work,
- reusable runtime patterns,
- configurable operational behavior,
- operational overview and control.

The current implementation is centered around:
- Process Models,
- Progress Plans,
- Activities,
- runtime orchestration,
- milestone and stage handling,
- ProcessView-driven execution.

### Current strategic direction

| Direction | Meaning |
|---|---|
| Current reality | ProcessView-centered runtime execution |
| Emerging | Worklists, desktops, webparts, broader overview surfaces |
| Future direction | Web-based modeling, functional operational modeling, AI-assisted composition |

---

## 2. Problem Space

### Domain reality

Public-sector organizations require:
- equal treatment,
- traceability,
- operational control,
- deadline governance,
- standardized handling,
- archival integrity,
- role-based workflows.

At the same time they require:
- local adaptation,
- configurable workflows,
- reusable operational patterns,
- efficient operational execution.

### Current operational problems

Current realities often include:
- fragmented workflows,
- weak overview,
- manual coordination,
- disconnected task handling,
- inconsistent operational progression,
- siloed management follow-up.

### Core tension

| Need | Counter-need |
|---|---|
| Standardization | Local adaptation |
| Compliance | Efficient handling |
| Auditability | Operational flexibility |
| Role control | Process variation |
| Reuse | Customer-specific needs |

### Product response

360 Flow addresses this through:
- process-aware execution,
- lifecycle visibility,
- operational workspaces,
- reusable Flow Building Blocks,
- governed configurability.

---

## 3. Product Vision

360 Flow aims to become the operational Flow layer for Public 360.

The long-term direction combines:
- lifecycle-aware execution,
- reusable operational patterns,
- process-oriented operational work,
- operational overview and control,
- future AI-assisted operational support,
- browser-based operational modeling,
- functional process ownership,
- reusable Flow composition.

### AI direction

AI is future direction, not current pilot capability.

| AI direction | Meaning |
|---|---|
| AI-assisted process definition | Future support for composing Flow models |
| AI-assisted operational guidance | Future support for next-step suggestions |
| AI-assisted completeness analysis | Future support for document / case checks |
| AI-assisted composition | Future support for Governed Flow Building Blocks |
| AI-assisted operational participation | Future support for agents inside structured Flows |

### Functional modeling direction

The intended future modeling direction is:
- functional process owners first,
- AI-assisted modeling first,
- technical modelers and delivery consultants second.

---

## 4. Product Definition & Boundaries

360 Flow combines:
- Process Models,
- executable Processes,
- Activities,
- runtime orchestration,
- lifecycle handling,
- dialogs,
- notifications,
- worklists,
- operational overview surfaces,
- reusable Flow Building Blocks.

Hosted Processes are treated as a commercial/service layer built on top of 360 Flow.

### Not the product

360 Flow is not:
- a generic BPM suite,
- unrestricted low-code workflow tooling,
- a free-form scripting platform,
- a generic task manager.

### Boundary principle

The product provides governed configurability within runtime-controlled boundaries.

---

## 5. Personas & Roles

Primary personas:
- Case Worker / Case Handler
- Registrar / Administrative Staff
- Process Owner / Flow Administrator
- Operational Leadership
- External Applicants / Citizens
- Product & Engineering Governance Roles

### Role model

The platform is role-governed rather than person-governed.

### Current operational roles

| Role | Primary use of Flow |
|---|---|
| Case worker | Execute activities, complete steps, progress cases |
| Registrar / archivist | Intake, registration quality, metadata handling |
| Manager | Monitor progress, bottlenecks, deadlines, workloads |
| Process owner | Govern lifecycle structure and operational rules |
| Applicant / external user | Submit material, respond, receive notifications |

---

## 6. Core Process Areas

Core operational areas:
1. Information Intake / Registration
2. Case Management
3. Quality Assurance
4. Publishing & External Interaction
5. Collaboration & Operational Overview

### Cross-cutting capabilities

- rules,
- notifications,
- lifecycle visibility,
- reusable Flow Building Blocks,
- runtime orchestration.

---

## 7. Capability Model

### Current capability areas

| Capability area | Current state | Notes |
|---|---|---|
| Process Models | Shipped | PMC binding, activation, lifecycle structure |
| Progress Plans | Shipped | Core process execution model |
| Activities | Shipped | Activity-driven execution semantics |
| Milestones | Shipped | Runtime + React integration |
| Stages | Shipped | Runtime + React integration |
| Dialogs | Shipped | Milestone, stage, process dialogs |
| Rules | Shipped | DMN-based runtime rules |
| Notifications | Shipped | Email and related runtime behavior |
| Runtime orchestration | Shipped | WorkUnit scheduling and execution |
| ProcessView execution | Shipped | Main operational UI surface |
| Worklists | Emerging | ADO-driven direction |
| Desktops / webparts | Emerging | ADO-driven direction |
| PMC admin UX | Emerging | APIs exist, routed UI limited in current slice |

### Capability layers

| Layer | Responsibility |
|---|---|
| Process Structure Capabilities | Structural lifecycle |
| Flow Execution Capabilities | Operational progression |
| Runtime & Orchestration Capabilities | Execution coordination |
| Rules & Governance Capabilities | Constraints and validation |
| User Interaction Capabilities | Operational UX |
| Portfolio Management Capabilities | Overview and control |
| Reusable Flow Building Blocks | Reusable operational semantics |
| Integration & Communication | External interaction |
| AI-Assisted Capabilities | Future direction |

---

## 8. Operational Workspace Model

Current UX is ProcessView-centered and lifecycle-aware.

### Current operational surfaces

| Surface | Current state | Notes |
|---|---|---|
| ProcessView | Shipped | Main operational execution surface |
| Activity lists | Shipped | Phase-based activity execution |
| Activity actions | Shipped | Execute, edit, cancel, reactivate |
| Milestone views | Shipped | Case/project milestone visibility |
| Stage views | Shipped | Lifecycle-oriented visibility |
| Dialogs | Shipped | Milestone, stage, process |
| Worklists | Emerging | Not yet first-class in current slice |
| Desktops / webparts | Emerging | Management overview/control direction |

### Current UX pattern

Operational work today is:
- process-progress-centered,
- lifecycle-aware,
- activity-driven,
- case-centered.

---

## 9. Runtime & Execution Model

### Current runtime capabilities

| Runtime area | Current state | Notes |
|---|---|---|
| Process Models | Operational | PMC binding, lifecycle prep |
| Progress Plans | Operational | Execution backbone |
| Activities | Operational | Core execution primitive |
| Milestones | Operational | Handlers, dialogs, views |
| Stages | Operational | Handlers, dialogs, views |
| Document Flow | Partially transitional | Runtime present, routing mixed |
| Send Email | Runtime-ready | UX integration transitional |
| Meeting Invite | Runtime-ready | UX integration transitional |
| ShareWith | Emerging | New runtime capability |
| Rules Engine | Operational | DMN runtime |
| Worklists | Emerging | Backlog-led |
| Desktops / webparts | Emerging | Backlog-led |

### Runtime characteristics

The current runtime supports:
- lifecycle orchestration,
- activity execution,
- Progress Plan execution,
- Work Unit scheduling,
- DMN rules,
- milestone/stage orchestration,
- notifications,
- subprocesses,
- deferred execution.

### Transitional runtime reality

The current runtime still includes:
- legacy coexistence,
- mixed routing patterns,
- transitional orchestration behavior.

---

## 10. Configuration & Governance

### Current governance model

| Area | Current state | Configurability | Notes |
|---|---|---|---|
| Process Models | Shipped | High | PMC structure configurable |
| Stages / Milestones | Shipped | High | Admin / registrar governed |
| Activities | Shipped | Medium | Runtime-controlled semantics |
| Work Units | Shipped | Medium | XML/XAML-centric authoring |
| Rules (DMN) | Shipped | Medium | Runtime-oriented today |
| Runtime orchestration | Shipped | Low | Centrally governed |
| Feature toggles | Shipped | Medium | Product/runtime controlled |
| ProcessView | Shipped | Low | Operational UX surface |
| Worklists | Emerging | Low | Backlog-led |
| Desktops / webparts | Emerging | Low | Limited evidence |
| Web-based modeling | Future direction | Low | Not current maturity |
| AI-assisted modeling | Future direction | Low | Strategic direction only |

### Governance boundaries

- Process Models are configurable.
- Runtime semantics remain centrally governed.
- New activity types remain developer-dependent.
- Functional modeling is still emerging.

### Governance principle

Configurable operational behavior within controlled runtime boundaries.

---

## 11. Lifecycle & Operational Semantics

360 Flow treats administrative work as lifecycle progression rather than isolated tasks.

### Lifecycle model

| Layer | Meaning |
|---|---|
| Structural lifecycle | Process Model |
| Executable progression | Process / Progress Plan |
| Runtime execution | Activities / Work Units |
| Governance semantics | Rules and constraints |
| Oversight | Portfolio overview and control |

### Current interpretation

Lifecycle progression is the core organizing principle for operational work.

---

## 12. Reusable Flow Building Blocks

### Current reusable assets

| Building block type | Current state | Notes |
|---|---|---|
| Milestone patterns | Shipped | Runtime + React integrated |
| Stage patterns | Shipped | Lifecycle aware |
| Process dialogs | Shipped | Subprocess handling |
| Approval flows | Shipped | Document Flow integrated |
| Review flows | Shipped | Runtime-driven |
| Dispatch flows | Shipped | Runtime-driven |
| Notification patterns | Shipped | Email / related runtime |
| Consultation patterns | Shipped | Reusable subprocess direction |
| ShareWith | Emerging | New reusable interaction pattern |
| Rules (DMN) | Shipped | Runtime-oriented reuse |
| Work Unit templates | Shipped | .wu / .xaml based |
| StandardProcesses | Shipped | Reference implementations |
| SharedComponents | Shipped | Reusable server actions |
| Worklists | Emerging | Operational overview direction |
| Web-based reusable composition | Future direction | Not current maturity |

### Reuse interpretation

Current reuse maturity is:
- runtime reuse is strong,
- governance standardization is still evolving.

---

## 13. AI-Assisted Direction

AI is currently future direction.

### Potential future areas

- AI-assisted process definition
- AI-assisted operational guidance
- AI-assisted completeness analysis
- AI-assisted recommendations
- AI-assisted composition of Governed Flow Building Blocks
- AI agents participating in structured Flows

### Important constraint

The intended direction is governed AI-assisted operational support, not unrestricted autonomous orchestration.

---

## 14. Portfolio Management & Operational Overview

Portfolio management currently focuses on:
- operational overview,
- workload awareness,
- lifecycle visibility,
- management follow-up,
- deadline awareness,
- operational control.

### Current surfaces

| Surface | Current state | Notes |
|---|---|---|
| Worklists | Emerging | Backlog-led |
| Milestone views | Shipped | Active operational visibility |
| ProcessView | Shipped | Case progress execution |
| Desktops / webparts | Emerging | Overview and control direction |

### Current meaning

Portfolio management is currently:
- operational visibility and control,
not advanced process intelligence.

---

## 15. Pilot Scope & Operational Reality

### Current maturity

Current pilot maturity demonstrates:
- strong runtime foundations,
- lifecycle-aware execution,
- milestone / stage maturity,
- reusable runtime primitives,
- ProcessView-centered operational execution.

### Current gaps

- worklists,
- desktops,
- UX unification,
- functional modeling,
- reusable governance operationalization.

### Pilot reality

AI and web-based modeling remain future direction.

---

## 16. Non-Functional Requirements

### Core operational requirements

- auditability
- predictable execution
- lifecycle traceability
- role accountability
- security
- compatibility
- runtime stability
- archival integrity
- scalability

### Core principle

Predictable and traceable operational execution.

---

## 17. Reference Scenario: Liquor Serving License Application

This is the reference operational scenario used to pressure-test the model.

### Why this scenario

A liquor serving license application is:
- standardized,
- document-heavy,
- deadline-aware,
- role-governed,
- operationally repetitive,
- a natural fit for Flow.

### Example lifecycle

| Stage | Purpose |
|---|---|
| Application received | Intake and registration |
| Validation & completeness | Verify required documentation |
| Internal review | Assess and coordinate |
| Consultation / hearing | External or internal review as needed |
| Decision preparation | Prepare recommendation |
| Approval & decision | Formal decision handling |
| Notification & closure | Communicate and archive outcome |

### What it demonstrates

- Process Model lifecycle
- Progress Plan execution
- lifecycle-aware progression
- milestone handling
- applicant interaction
- operational overview
- approvals
- notifications
- reusable Flow Building Blocks

---

## 18. Operational Modeling Direction

### Current reality

Current modeling is:
- runtime-oriented,
- XML/XAML-centric,
- admin-oriented.

### Future direction

- browser-based operational modeling,
- functional process ownership,
- reusable Flow Building Block composition,
- AI-assisted composition.

### Current maturity

Implementation-centric today, functional modeling later.

---

## 19. Current Runtime Capability Overview

| Capability | Current maturity |
|---|---|
| Process Models | Shipped |
| Progress Plans | Shipped |
| Activities | Shipped |
| Milestones | Shipped |
| Stages | Shipped |
| Document Flow | Partially transitional |
| Send Email | Runtime-ready |
| Meeting Invite | Runtime-ready |
| ShareWith | Emerging |
| Rules Engine | Shipped |
| Worklists | Emerging |
| Desktops / webparts | Emerging |

ProcessView is the operational center of gravity today.

---

## 20. Current UX & Workspace Overview

| UX area | Current state | Notes |
|---|---|---|
| ProcessView | Shipped | Main operational surface |
| Activity execution | Shipped | Core interaction pattern |
| Milestone / stage dialogs | Shipped | React-integrated |
| Process dialogs | Shipped | Subprocess support |
| Milestone views | Shipped | Strong lifecycle visibility |
| Worklists | Emerging | Backlog-led |
| Desktops / webparts | Emerging | Backlog-led |
| PMC admin UX | Emerging | API and types present, routed UX limited |

### UX maturity interpretation

Current UX is:
- lifecycle-aware,
- ProcessView-centered,
- partially transitional.

---

## 21. Current Governance & Configurability Boundaries

### Governance interpretation

360 Flow currently supports governed configurability within runtime-controlled boundaries.

### Current boundary matrix

| Area | Current state | Configurability | Operational notes |
|---|---|---|---|
| Process Models | Shipped | High | PMC structure configurable |
| Stages & Milestones | Shipped | High | Admin / registrar governed |
| Activities | Shipped | Medium | Runtime-controlled semantics |
| Work Units | Shipped | Medium | XML/XAML-centric authoring |
| Rules (DMN) | Shipped | Medium | Runtime-oriented today |
| Runtime orchestration | Shipped | Low | Centrally runtime-governed |
| Feature toggles | Shipped | Medium | Product/runtime controlled |
| ProcessView | Shipped | Low | Operational UX surface |
| Worklists | Emerging | Low | Backlog-led |
| Desktops / webparts | Emerging | Low | Limited evidence |
| Web-based modeling | Future direction | Low | Not current maturity |
| AI-assisted modeling | Future direction | Low | Strategic direction only |

### Governance maturity interpretation

Current governance is runtime-governed configurability, not yet broad functional operational modeling.

---

## 22. Current Runtime & UX Transition Areas

### Transitional areas

| Area | Current state | Operational impact |
|---|---|---|
| BIF vs React dialogs | Transitional | Mixed UX behavior |
| Document Flow routing | Transitional | Dual runtime paths |
| Workflow coexistence | Transitional | Separate product/runtime concepts |
| Worklists | Emerging | Limited operational maturity |
| Desktops / webparts | Emerging | Operational overview still evolving |
| PMC UX | Emerging | Runtime/admin-oriented today |
| Localization | Transitional | Active improvement area |
| Functional modeling | Emerging | Runtime-centric today |
| AI-assisted modeling | Future direction | Not operational today |

### Transition interpretation

Runtime foundations are stronger than UX and modeling maturity.

---

## 23. Current Governance & Configurability Boundaries

### Current governance matrix

| Area | Current state | Configurability | Operational notes |
|---|---|---|---|
| Process Models | Shipped | High | PMC structure configurable |
| Stages & Milestones | Shipped | High | Admin / registrar governed |
| Activities | Shipped | Medium | Runtime-controlled semantics |
| Work Units | Shipped | Medium | XML/XAML-centric authoring |
| Rules (DMN) | Shipped | Medium | Runtime-oriented today |
| Runtime orchestration | Shipped | Low | Centrally runtime-governed |
| Feature toggles | Shipped | Medium | Product/runtime controlled |
| ProcessView | Shipped | Low | Operational UX surface |
| Worklists | Emerging | Low | Backlog-led |
| Desktops / webparts | Emerging | Low | Limited evidence |
| Web-based modeling | Future direction | Low | Not current maturity |
| AI-assisted modeling | Future direction | Low | Strategic direction only |

### Governance summary

- Process Models are configurable.
- Runtime semantics are centrally governed.
- New activity types are still developer-dependent.
- Functional modeling is still emerging.
- Current configuration is strong, but still runtime-led.

---

## 24. Current Reusable Flow Building Blocks

### Current reusable building blocks

| Building block type | Current state | Notes |
|---|---|---|
| Milestone patterns | Shipped | Runtime + React integrated |
| Stage patterns | Shipped | Lifecycle aware |
| Process dialogs | Shipped | Subprocess handling |
| Approval flows | Shipped | Document Flow integrated |
| Review flows | Shipped | Runtime-driven |
| Dispatch flows | Shipped | Runtime-driven |
| Notification patterns | Shipped | Email / related runtime |
| Consultation patterns | Shipped | Reusable subprocess direction |
| ShareWith | Emerging | New reusable interaction pattern |
| Rules (DMN) | Shipped | Runtime-oriented reuse |
| Work Unit templates | Shipped | .wu / .xaml based |
| StandardProcesses | Shipped | Reference implementations |
| SharedComponents | Shipped | Reusable server actions |
| Worklists | Emerging | Operational overview direction |
| Web-based reusable composition | Future direction | Not current maturity |

### Reuse summary

Reuse today is strong at runtime and template level. Governance standardization is still evolving.

---

## 25. Current Runtime & UX Transition Areas

### Transitional areas

| Area | Current state | Operational impact |
|---|---|---|
| BIF vs React dialogs | Transitional | Mixed UX behavior |
| Document Flow routing | Transitional | Dual runtime paths |
| Workflow coexistence | Transitional | Separate product/runtime concepts |
| Worklists | Emerging | Limited operational maturity |
| Desktops / webparts | Emerging | Operational overview still evolving |
| PMC UX | Emerging | Runtime/admin-oriented today |
| Localization | Transitional | Active improvement area |
| Functional modeling | Emerging | Runtime-centric today |
| AI-assisted modeling | Future direction | Not operational today |

### Transition summary

The platform is runtime-mature but operationally transitional in UX, overview surfaces, and modeling maturity.

---

## Final current-state summary

360 Flow today is best understood as:

- a ProcessView-centered lifecycle execution environment,
- with configurable runtime orchestration,
- strong milestone and stage behavior,
- runtime-reusable operational patterns,
- emerging worklists and overview surfaces,
- transitional UX and routing in some areas,
- and future direction toward functional modeling and AI-assisted composition.

---

*Consolidated from the operational intelligence packs, governance/configurability review, UX/workspace review, runtime delta review, and scenario validation work.*


---

# FULL OPERATIONAL APPENDICES (UNREDACTED)

The sections below are preserved in substantially fuller operational detail from the working reconstruction process.

These appendices intentionally preserve:
- matrices,
- operational nuance,
- maturity distinctions,
- runtime caveats,
- governance boundaries,
- UX transition realities,
- and pilot-facing implementation detail.

They are intentionally NOT editorially compressed.

---

# Appendix A — Current-State Capability Matrix

# 360 Flow (PAF) — Current-state capability matrix

**Scope:** Operational reality in this workspace: `core-bl/Source/si-bl-process-platform-build`, `core-360-react-views/packages/process-components`, plus selected **Azure DevOps** items (project **360**, fetched **2026-05-10**) where code evidence for a surface was not found.  
**Legend:** Maturity is **code + tests present** unless ADO-only is explicitly stated. **(inferred)** = not spelled out in one line of source.

| Capability | Current maturity | Runtime evidence | UX evidence | Configurable? | Reusable? | Pilot usage | Limitations |
|------------|------------------|------------------|-------------|---------------|-----------|-------------|---------------|
| **Process models (bind PMC, insert, activate)** | **Shipped** (core BL + tests) | `ProcessModelMetaInsert` async vs sync branch on `AsyncProcessModelLoading` (`core-bl/.../ProcessPlatform.Meta/ProcessModel/ProcessModelMetaInsert.cs`); integration waits in `IntegrationTest.ProcessPlatform/ClientApi/ApiProcessModelTest.cs` | PMC admin flows via `StageProcessConfigApi`, `ProcessModelConfig` tree APIs (`SI.Client.Api.Process/StageProcessConfig/`, `ProcessModelConfig/`) | **High** (PMC + process model config in meta; feature toggle `AsyncProcessModelLoading`) | **Product** (platform meta) | **Primary** pilot surface | When async toggle on, stages or activities may appear after commit; clients must wait or poll (`ApiProcessModelTest` pattern). |
| **Progress plans (process instance)** | **Shipped** | `ProgressPlanApi`: terminate, cancel, passive or active, phases, activities, execute client or server actions (`SI.Client.Api.Process/ProgressPlan/ProgressPlanApi.cs`); `WorkUnitManager.Schedule` for work-unit driven work (`ProcessEngine.Runtime/WorkUnit/WorkUnitManager.cs`) | `ProcessView` + phase or activity UI (`process-components/src/ProcessView/*`); `useWaitTaskStatus.tsx` for wait-task polling | **Medium** (status transitions and PMC drive behavior; not all activity types fully handled in `ExecuteAction`) | **Product** | **Primary** | `ExecuteAction` throws for decision activity type **22** (“not implemented yet”, same file). Wait-task type **25** is a no-op branch. |
| **Activities (list, status, responsibilities)** | **Shipped** | `ProgressPlanApi.GetActivitiesForPhase`, `SetActivityStatus`, `GetActivityResponsibleInfo`, `CancelAction` (`ProgressPlanApi.cs`) | `ProcessViewActivitiesSection.tsx`, `ActivitiesForPhaseList.ts`, `ExecuteButtonComponent.tsx`, `ActionsComponent.tsx` | **Medium** (activity rows come from runtime or data; status rules in `ActivityManager`) | **Product** | **Primary** | Localization of list labels is under active ADO scope (**420545** Active, **420676** New); today APIs may still expose localization IDs in some fields **(inferred)** until those stories complete. |
| **Milestones (config + dialog + ops)** | **Shipped** | `MilestoneUserActionHandler`, `MilestoneOperations`, `MilestoneDialogApi` (`Runtime/UserActions/Milestone/`, `Client.Api.Process/UserActions/MilestoneDialog/`) | `CreateMilestoneDialog` under `ProcessView/ActivityDialogComponents/`; package exports `MilestoneDialog` from `process-components/src/index.ts` | **High** (milestone config on PMC or stage; dialog props from runtime data) | **Product** | **Primary** | Document milestone triggers were refactored recently (`Meta/Document/DocumentMilestoneOrchestrator*.cs`); pilot validation should include dispatch or receive paths tied to milestones. |
| **Stages (config + dialog + ops)** | **Shipped** | `StageUserActionHandler`, `StageOperations`, `StageDialogApi`, `StageApi` (includes `AsyncProcessModelLoading` guard in places, e.g. `StageApi.cs` around line 184 in repo snapshot) | `CreateStageDialog` in `ProcessView/`; `StageViewsList.ts`, `StageDetailsEntity.ts` | **High** | **Product** | **Primary** | `StageApi` permission change **#20002** (commit in process-platform history) affects who may add documents on public read; pilot ACL checks should be explicit. |
| **Subprocesses (create process dialog)** | **Shipped** | `ProcessUserActionHandler`, `ProcessOperations`, `ProcessDialogApi` | `CreateProcessDialog` in `ProcessView/` | **High** | **Product** | **Primary** | Same localization caveats as milestones or stages for dialog text **(inferred)**. |
| **Document flow (wizard, dialog, approval, review, dispatch)** | **Partial** (runtime handlers shipped; URL routing split) | `DocumentFlowUserActionHandler`, `ApprovalUserActionHandler`, `ReviewUserActionHandler`, `DispatchUserActionHandler`; `UserActionExecuter` resolves **only** document-flow client URLs among handled types (`Runtime/UserActions/UserActionExecuter.cs`) | Harness and flows in integration tests (`IntegrationTest.ProcessPlatform/Pandora/PandoraDocumentFlow*`, WWF harness work units under `WorkUnits/Platform-WWF-WorkUnits/TestWorkUnits/`); `ProcessView` drives generic client actions via `ProgressPlanApi.ExecuteAction` path | **High** (runtime data and designer payloads) | **Product** + **Harness** test assets | **High** | `UserActionExecuter` XML doc still requires fallback to `ActivityExecuter` for some legacy wizard or dialog routing; dual-path troubleshooting remains **(Fact)**. |
| **Send Email dialog** | **Shipped** (BL + tests) | `SendEmailUserActionHandler`, `SendEmailDialogApi`, `SendEmailDialogCaseFilesApi` | No dedicated `SendEmailDialog` export in `process-components/src/index.ts` in this snapshot; **(inferred)** host may open BIF or URL from `ExecuteClientAction` | **Medium** | **Product** | **Medium** (depends on host wiring) | ADO Feature **418321** remains **New** while code exists; pilot comms must not rely on Feature state alone **(Fact, ADO)**. |
| **Meeting Invite dialog** | **Shipped** (BL + tests) | `MeetingInviteUserActionHandler`, `MeetingInviteDialogApi` | Same pattern as send email: not exported from `process-components` index in this snapshot | **Medium** | **Product** | **Medium** | ADO Feature **418326** **New**; child-activity Feature **421477** **New** **(Fact, ADO)**. |
| **Share With dialog** | **Shipped** (BL + tests + toolbox activity) | `ShareWithDialog` toolbox activity (`ProcessEngine.Activities/ProgressPlan/ClientActions/ShareWithDialog.cs`); `ShareWithUserActionHandler`; `ShareWithDialogApi`; `PinAndShareItemsGateway` | No `ShareWith` symbol match under `process-components` in this scan | **Medium** | **Product** | **Medium** | Routed like other non-document-flow client actions through `ProgressPlanApi.ExecuteClientAction` path; **not** added to `UserActionExecuter` switch **(Fact)**. |
| **Approvals and reviews (document flow)** | **Shipped** | Same handlers as document flow row | `DecisionComponent.tsx`, decision types under `ProcessView/ProcessTypes/` | **High** (runtime configuration) | **Product** | **High** for case teams using approval or review activities | Due-date calculation hooks for approval or review touched in **#20032** (`ApprovalUserActionHandler`, `ReviewUserActionHandler`, `DueDateCalculationType.cs`) **(Fact, git)**. |
| **Dispatch (document flow)** | **Shipped** | `DispatchUserActionHandler` | Driven through client-action URL resolution plus engine | **High** | **Product** | **Medium** | Same routing caveats as document flow row. |
| **Rules (DMN rule sets)** | **Shipped** (engine internal) | `RuleSetExecuter` implements `IRuleSetExecuter` **internal** (`RulesEngine/Runtime/RuleSetExecuter.cs`); integration tests under `IntegrationTest.ProcessPlatform/RulesEngine/` | No dedicated rules authoring UX in `process-components` (rules are meta or designer elsewhere) | **Medium** (rule artifacts and registration) | **Product** | **Medium** (pilot if rules used) | `internal` executer limits extension from outside assembly **(Fact)**; authoring is not surfaced in this React package. |
| **Runtime orchestration (engine + platform)** | **Shipped** | `WorkUnitManager.Schedule`; `ProgressPlanApi.ExecuteAction` and `ExecuteClientAction` (see `ProgressPlanApi.cs`); meta insert or post-transaction background initiation (`ProcessModelMetaInsert.cs`) | `ProcessView` uses `ProgressPlanApi` procedures (`useWaitTaskStatus.tsx`, activity list) | **Medium** (feature toggles, engine selection) | **Product** | **Primary** | `ProgressPlanApi` documents `ActivityExecuterFactory` seam for engine fallback **(Fact)**. |
| **Reusable Flow building blocks** | **Shipped** (library + sector packs) | Toolbox activities under `ProcessEngine.Activities/ProgressPlan/` (including `ShareWithDialog`, email, meeting, document flow classes); `SharedComponents/Server Actions/CreateSubProcess.wu`; `StandardProcesses/*.wu` including `CreateSingleDocument.wu` | Examples under `WorkUnits/FlowWorkUnits/Examples/` exported from package for learning | **High** for `.wu` and XAML arguments; **Low** for new activity types (needs new activity classes) | **Product** (shared), **Reference** (`StandardProcesses/NVE Processes/*`, deficiency letters), **Harness** (`Platform-WWF-WorkUnits/TestWorkUnits/*`) | **High** for pilots using shipped templates; **Low** if expecting only empty `applicationmaster` folder **(Fact from prior pack)** | VB Flow work units use `OptionStrict Off` (`WorkUnits/FlowWorkUnits/FlowWorkUnits.vbproj`) **(Fact)**. |
| **Notifications or realtime entity sync** | **Partial** (toggle-driven backend) | `AsyncProcessModelLoading` path defers initiation (`ProcessModelMetaInsert.cs`); ADO **401108** “Entity Update Notifications and Real-time UI Synchronization” **Active**, tag `FT:AsyncProcessModelLoading` | `useWaitTaskStatus.tsx` and related wait-task UI for polling-style updates | **Medium** (feature toggles) | **Product** | **Medium** | Full “real-time” UX beyond wait-task polling is **not** evidenced solely in `process-components` **(inferred)**; align with **401108** scope before promising websocket-style behavior. |
| **Worklists (case phases and deadlines)** | **Backlog-led** | No `worklist` match under `process-components` in this scan | None found in `process-components` | **Unknown** (no code anchor here) | **N or A** | **Low until delivered** | ADO **411634** **New** (“Worklists — Case processing phases and deadlines…”) **(Fact, ADO)**. |
| **Desktops or webparts (process-model-centric)** | **Backlog-led** | No code hit for “Desktops for Process Models” in bounded search | `ProcessView` is the evidenced case-handling surface | **Unknown** without further host or webpart repo | **N or A** | **Medium planning** | ADO **414651** **Active** (“Desktops for Process Models”) **(Fact, ADO)**; implementation outside this package not verified in this pass **(inferred)**. |
| **Portfolio or cross-case management overview** | **Not evidenced** in PAF package | No portfolio or overview symbols under `process-components` in this scan | `EditProcessDialog.tsx` and process model info types (`ProcessModelInfoEntity.ts`) support **in-case** editing or views | **Low or N or A** here | **N or A** in this slice | **Low** | Cross-case portfolio would live in other modules or hosts **(inferred)**; not claimed from `process-components` alone. |

---

## ADO references (pilot-facing)

- https://dev.azure.com/tieto-si/360/_workitems/edit/401108 — Async or entity-sync umbrella (**Active**).  
- https://dev.azure.com/tieto-si/360/_workitems/edit/414468 — Localization framework (**Active**).  
- https://dev.azure.com/tieto-si/360/_workitems/edit/414651 — Desktops for process models (**Active**).  
- https://dev.azure.com/tieto-si/360/_workitems/edit/411634 — Worklists (**New**).  
- https://dev.azure.com/tieto-si/360/_workitems/edit/418321 — Send email designer Feature (**New**).  
- https://dev.azure.com/tieto-si/360/_workitems/edit/418326 — Meeting invite designer Feature (**New**).  
- https://dev.azure.com/tieto-si/360/_workitems/edit/420545 — Localization for dialog APIs (**Active**).  
- https://dev.azure.com/tieto-si/360/_workitems/edit/420676 — Localization for lists and `GetActivitiesForPhase` (**New**).

---

*Matrix grounded in repo paths above and ADO batch read **2026-05-10**. Extend with host or webpart repos if desktops or worklists ship outside `process-components`.*


---

# Appendix B — Governance & Configurability Boundaries

# 360 Flow (PAF) — Governance and configurability boundaries (current state)

**Evidence base:** `core-bl/Source/si-bl-process-platform-build` (primary), `DEVELOPER_GUIDELINES.md`, internal Flow work unit skill `.cursor/skills/flowworkunit-new-process/SKILL.md`, and selected **Azure DevOps** items (project **360**, batch read **2026-05-10**).  
**Scope:** What is **operationally true today** in code and documented team rules. Anything labeled **(inferred)** is role mapping not spelled out in a single source line.

---

## 1. Governance boundary summary

**Centrally governed by product or runtime (facts from code and guidelines)**

- **Feature toggles:** Product defines toggle **types** and runtime checks them through `IMetaExecuter.IsFeatureEnabled<T>()`; toggle classes live in agreed namespaces (for example `SI.Biz.Core.ProcessPlatform.Shared.Types`). **Fact:** `DEVELOPER_GUIDELINES.md` §Feature toggles, §`IMetaExecuter` usage.
- **Entity update notifications:** After meta transactions, **core.bl** sends update notifications; Process Platform code must **not** call `SendMessage` or `SendEntityUpdateNotification` directly. **Fact:** `DEVELOPER_GUIDELINES.md` §`IMetaExecuter` (entity update bullet).
- **Process model insert lifecycle:** When `AsyncProcessModelLoading` is on and the row is not a switch scenario, stage or milestone preparation may run in a **fire-and-forget** background operation instead of inline with the insert statement. **Fact:** `ProcessModelMetaInsert.Prepare` and `PostTransactionOperation` (`SI.Biz.Core.ProcessPlatform.Meta/ProcessModel/ProcessModelMetaInsert.cs`).
- **PMC and harness separation:** Admin PMC APIs explicitly exclude Pandora harness categories from normal PMC editing contexts (`IsPandoraProcessModelConfig`, comments on `BaseUID` and `PandorasStageProcess`). **Fact:** `StageProcessConfigApi.cs` (comments and gate around lines 139–211 in the file snapshot read).
- **Process model configuration tree APIs:** Entry points call `ProcessModelUtility.ValidateAccessAdminOrRegistrar()` before serving data. **Fact:** `StageProcessConfigApi.cs` line 41; `ProcessModelConfigApiTreeView.cs` lines 50 and 135.
- **Plugin discovery:** Only assemblies under configured `ProcessPlatform.PluginPath` (default `bin`) whose file name contains `pluginengine` or `rulesetplugin`, with matching **strong name public key token**, are loaded. **Fact:** `MethodInspector.LoadSafeAssemblies` and `Initialize` (`SI.Biz.Core.ProcessPlatform.PluginEngine/Execution/MethodInspector.cs`). When `CLIBOOT` environment variable is true, **plugin method lists are not populated** during `Initialize`. **Fact:** same file, `Initialize` guard and `CLIBoot` property.
- **DMN rule execution class visibility:** `RuleSetExecuter` is **`internal`**. **Fact:** `SI.Biz.Core.ProcessPlatform.RulesEngine/Runtime/RuleSetExecuter.cs` class declaration.

**Delegated configuration (facts)**

- **Work unit definitions** resolve from persisted registry data by **work unit config GUID** (`stapc_workunitid` per interface XML doc). **Fact:** `IWorkUnitRegistry` (`SI.Biz.Core.ProcessPlatform.WorkUnitRegistry/Contracts/IWorkUnitRegistry.cs`).
- **Progress plan client actions:** URL resolution for platform-owned document-flow types is centralized in `UserActionExecuter`; other client action types return **false** and callers use the **engine** `ActivityExecuter` path. **Fact:** `UserActionExecuter.cs` XML documentation and `switch` body.

---

## 2. Configurability matrix

Rows list **who can change what** under typical RBAC (admin or registrar for PMC; case team for runtime). **(inferred)** marks role boundaries not defined in one code file.

| Area | Functional user (case handling) | Process owner (business) | Delivery consultant | Developer | Product or runtime gate |
|------|-----------------------------------|---------------------------|----------------------|-----------|-------------------------|
| **Process models on a case** | Activate or change PM when product UI allows; subject to case permissions **(inferred)** | Chooses which PMC applies; **cannot** bypass server validation | Implements PMC rows, stage or process links, tests in tenant | Changes insert rules, async behavior, validation | `ProcessModelMetaInsert`; `AsyncProcessModelLoading`; core.bl notification pipeline **(Fact)** |
| **PMC definition (stages, milestones, templates)** | No direct access unless also admin or registrar **(inferred)** | Defines desired model with consultant | Edits PMC via admin APIs (`ValidateAccessAdminOrRegistrar`) | Adds new meta statements or APIs | `StageProcessConfigApi`, `ProcessModelConfigApiTreeView` **(Fact)** |
| **Processes (progress plan instance)** | Execute or cancel allowed actions; close phases when UI allows **(inferred)** | Defines expectations; not file-level XAML **(inferred)** | Tunes PMC or work unit binding on stage | Changes `ProgressPlanApi` or `ActivityManager` integration | `ProgressPlanApi.ExecuteAction` supports only listed activity type branches; decision type **22** throws “not implemented” **(Fact)** `ProgressPlanApi.cs` |
| **Activities** | Operates within ACL and activity status rules **(inferred)** | Names or orders steps only through PMC or template design **(inferred)** | Configures runtime rows and templates | New `EnumActionType` or handler wiring | `EnumActionType` contract; `UserActionExecuter` routing **(Fact)** |
| **Work units (.wu and .xaml)** | Does not author XML **(inferred)** | Orders allowed toolbox steps with consultant per internal skill rules **(inferred)** | Authors or copies `.wu` and `.xaml`, arguments, optional `<featuretoggles>` only when product names exist **(Fact)** `flowworkunit-new-process/SKILL.md` | New toolbox activity types (`ProcessEngine.Activities`), new handlers, registry loaders | Work unit skill forbids inventing toggles or activity order **(Fact)**; VB project `OptionStrict Off` on `FlowWorkUnits.vbproj` **(Fact)** per prior operational pack |
| **Rules (DMN)** | No DMN editor in `process-components` **(Fact)** from package scan | Defines business outcomes with consultant | Deploys rule artifacts if product pipeline allows **(inferred)** | Implements input resolvers, rule sets, plugins | `internal` `RuleSetExecuter`; plugin DLL filter **(Fact)** |
| **Worklists** | Uses worklist product if present outside this slice **(inferred)** | Specifies need | Configures when feature ships | Implements | ADO **411634** **New** — not evidenced in `process-components` **(Fact, ADO)** |
| **Webparts or desktops** | Uses host shell features **(inferred)** | Specifies layout needs | Configures host | Implements host integration | ADO **414651** **Active** — implementation not verified under `process-components` **(Fact, ADO)** |
| **Reusable Flow building blocks** | Picks from shipped templates when exposed in UI **(inferred)** | Chooses standard versus sector packages with consultant | Adds `StandardProcesses` assets or copies `SharedComponents` | Adds new toolbox activities or server actions | Harness PMC exclusion in `StageProcessConfigApi` **(Fact)** |
| **Runtime extensions (plugins)** | None | None | Deploys signed DLLs to configured plugin path **(inferred)** | Writes `[Action]` or `[Query]` methods | Strong name token filter; `CLIBOOT` skips registration **(Fact)** `MethodInspector.cs` |
| **Notifications** | Sees results of standard core.bl notifications in clients **(inferred)** | None in Process Platform code path **(inferred)** | Enables toggles per environment policy **(inferred)** | Custom `PrepareEntityUpdateMessage` in meta managers **(Fact)** guideline | Process Platform must not send notifications directly **(Fact)** `DEVELOPER_GUIDELINES.md` |
| **Lifecycle structures (milestones, stages, subprocess)** | Completes dialogs when shown **(inferred)** | Configures on PMC with consultant | Same as PMC row | New lifecycle operations or APIs | `MilestoneOperations`, `StageOperations`, `ProcessOperations` **(Fact)** paths in operational pack |

**ADO references used above:** https://dev.azure.com/tieto-si/360/_workitems/edit/411634 — https://dev.azure.com/tieto-si/360/_workitems/edit/414651

---

## 3. Runtime-protected areas

These are **hard to override from configuration alone** because runtime or platform code enforces them.

| Protected area | Why |
|----------------|-----|
| **Activity type numeric contract** | `EnumActionType` and activity type branches in `ProgressPlanApi.ExecuteAction` define what the server can execute today. **Fact:** `EnumActionType.cs`, `ProgressPlanApi.cs` (`ExecuteAction` switch, decision branch throws). |
| **Client URL routing for document flow** | Only listed document-flow types get URLs from `UserActionExecuter`. **Fact:** `UserActionExecuter.cs`. |
| **Async process model initiation** | Feature toggle and `isSwitchProcessModelScenario` gate whether stage or milestone prep runs inline or in background. **Fact:** `ProcessModelMetaInsert.cs`. |
| **Plugin assembly trust** | Public key token and file name filter. **Fact:** `MethodInspector.cs`. |
| **PMC versus Pandora harness visibility** | API filters harness work units from normal PMC contexts. **Fact:** `StageProcessConfigApi.cs`. |
| **Registrar or admin gate for PMC APIs** | `ProcessModelUtility.ValidateAccessAdminOrRegistrar()`. **Fact:** `StageProcessConfigApi.cs`, `ProcessModelConfigApiTreeView.cs`. |

---

## 4. Areas still heavily developer-dependent

| Area | Evidence |
|------|-----------|
| **New client or server activity types** | Requires new toolbox activities, `EnumActionType` values, handlers, and often tests. **Fact:** handler layout under `Runtime/UserActions/` and `ProcessEngine.Activities/ProgressPlan/ClientActions/`. |
| **Decision execution through `ProgressPlanApi.ExecuteAction`** | `case 22` throws not implemented. **Fact:** `ProgressPlanApi.cs`. |
| **New DMN integration surfaces** | `RuleSetExecuter` is `internal`; callers are inside the rules engine assembly boundary. **Fact:** `RuleSetExecuter.cs`. |
| **Changing entity notification transport** | Guidelines forbid Process Platform from calling send APIs directly; changes belong in core meta pipeline. **Fact:** `DEVELOPER_GUIDELINES.md`. |
| **Plugin discovery policy** | Changing token rules or folder conventions requires code change. **Fact:** `MethodInspector.cs`. |
| **Web-based modeling shell gaps** | BPMN modeler Feature **419789** is **New** in ADO **(Fact)** — not treated as shipped functional modeling in this repo slice. |

---

## 5. Current blockers for functional web-based modeling

**Operational honesty:** “Functional web-based modeling” is interpreted as **non-developer authoring or changing executable process definitions in a browser**. Evidence-based blockers:

| Blocker | Evidence |
|---------|-----------|
| **Work unit authoring is file and XML centric** | Internal skill requires explicit ordered activity list, `.wu` and `.xaml`, and controlled feature toggle declarations. **Fact:** `flowworkunit-new-process/SKILL.md`. That is **not** the same as a single web form for all tenants **(inferred)**. |
| **PMC editing is admin or registrar gated** | `ValidateAccessAdminOrRegistrar()` on tree and stage process config entry points. **Fact:** `StageProcessConfigApi.cs`, `ProcessModelConfigApiTreeView.cs`. Typical functional case users **do not** get this gate **(inferred)**. |
| **Designer Features still largely `New` in ADO** | Examples: **421813** Document Flow designer, **421812** Stage designer, **418321** Send Email, **418326** Meeting Invite — all **New** in the **2026-05-10** batch used for the capability matrix. **Fact:** ADO batch read referenced in `documents/work/360-flow-capability-matrix.md`. |
| **BPMN modeler not shipped in backlog state** | **419789** `PAF - BPMN modeler` **New**. **Fact:** ADO. |
| **Decision activities not executable via `ProgressPlanApi.ExecuteAction`** | Throws for type **22**. **Fact:** `ProgressPlanApi.cs`. |

---

## 6. Areas already suitable for functional process ownership

**“Process ownership” here means business-led definition of **what** happens (stages, milestones, document flows, ordering), with **consultant or admin** execution of configuration tools—not writing C#.**

| Area | Why it is suitable now |
|------|---------------------------|
| **PMC structure** | Stage and milestone configs, templates, and tree APIs exist and are intended for admin or registrar operators. **Fact:** `StageProcessConfigApi`, `ProcessModelConfigApiTreeView`, `MilestoneConfigQueries` patterns. |
| **Progress plan operation on a case** | End users can drive phases, decisions UI, and client or server actions that are implemented in `ProgressPlanApi` and `ProcessView`. **Fact:** `ProgressPlanApi.cs`; `process-components/src/ProcessView/`. |
| **Choosing among shipped Flow templates** | `StandardProcesses` and `Examples` provide reusable packages; consultants can bind the correct work unit GUID in configuration **(inferred)** once registry rows exist. **Fact:** paths under `WorkUnits/FlowWorkUnits/StandardProcesses` and `Examples` per operational inventory. |
| **Document flow configuration inside supported types** | Wizard, dialog, approval, review, dispatch handlers exist for runtime. **Fact:** `Runtime/UserActions/DocumentFlow`, `Approval`, `Review`, `Dispatch`. |
| **Operational toggles on known features** | Product-defined feature toggles are the supported way to branch behavior without forked code. **Fact:** `DEVELOPER_GUIDELINES.md` and `ProcessModelMetaInsert` toggle usage. |

---

## Source index (paths)

- `core-bl/Source/si-bl-process-platform-build/DEVELOPER_GUIDELINES.md`
- `core-bl/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessPlatform.Meta/ProcessModel/ProcessModelMetaInsert.cs`
- `core-bl/Source/si-bl-process-platform-build/SI.Client.Api.Process/StageProcessConfig/StageProcessConfigApi.cs`
- `core-bl/Source/si-bl-process-platform-build/SI.Client.Api.Process/ProcessModelConfig/ProcessModelConfigApiTreeView.cs`
- `core-bl/Source/si-bl-process-platform-build/SI.Client.Api.Process/ProgressPlan/ProgressPlanApi.cs`
- `core-bl/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessPlatform.Runtime/UserActions/UserActionExecuter.cs`
- `core-bl/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessPlatform.PluginEngine/Execution/MethodInspector.cs`
- `core-bl/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessPlatform.RulesEngine/Runtime/RuleSetExecuter.cs`
- `core-bl/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessPlatform.WorkUnitRegistry/Contracts/IWorkUnitRegistry.cs`
- `core-bl/Source/si-bl-process-platform-build/.cursor/skills/flowworkunit-new-process/SKILL.md`

---

*Current reality only. Roadmap language intentionally tied to explicit ADO states where cited.*


---

# Appendix C — Operational Reality Delta

# 360 Flow / PAF — Operational reality delta (since 2026-05-07 extraction)

**Baseline:** [documents/work/360-flow-operational-intelligence.md](360-flow-operational-intelligence.md) (*Generated 2026-05-07*).  
**As-of:** 2026-05-10 (ADO WIQL `asOf` + workspace read + **git log** under `core-bl`).  
**Legend:** **Fact** = cited path or work item. **(inferred)** = reasonable conclusion not printed verbatim in source.  
**Git layout (Fact):** The umbrella folder `te-industry-public360` has **no** `.git` at its root, but **`core-bl/.git` exists**. All history below is from `git -C core-bl` scoped to `Source/si-bl-process-platform-build`.

---

## 1. Executive delta summary — top 10 meaningful changes

1. **`ShareWithDialog` (enum 17) vs baseline doc + May-8 execution PR** — **Fact:** [EnumActionType.cs](core-bl/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessPlatform.Shared/Types/EnumActionType.cs) defines `ShareWithDialog = 17`. **Fact (git):** `EnumActionType.cs` was last touched before this window in commit `83cb8b683d` “Adding designer component for Share component (#19989)”; the **full** Share With execute path, gateway, meta/post-execution, and tests landed **2026-05-08** in `18fbcdfe05` (#20034) (see §“Git history scan”).
2. **New toolbox / progress-plan activity `ShareWithDialog`** — **Fact:** [ShareWithDialog.cs](core-bl/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessEngine.Activities/ProgressPlan/ClientActions/ShareWithDialog.cs) (`[ToolBoxInfo("User: Share with", …)]`) documents the same child-activity composition model as Send Email / Document Flow dialog.
3. **New runtime handler `ShareWithUserActionHandler`** — **Fact:** [ShareWithUserActionHandler.cs](core-bl/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessPlatform.Runtime/UserActions/ShareWith/ShareWithUserActionHandler.cs) binds `EnumActionType.ShareWithDialog` and executes via `IShareItemsGateway`.
4. **New Client API surface `ShareWithDialogApi` (+ props/execute types)** — **Fact:** [SI.Client.Api.Process/UserActions/ShareWithDialog/](core-bl/Source/si-bl-process-platform-build/SI.Client.Api.Process/UserActions/ShareWithDialog/) (`ShareWithDialogApi.cs`, `ShareWithDialogProps.cs`, `ExecuteShareWithUserActionProps.cs`).
5. **New standard process asset `CreateSingleDocument.wu`** — **Fact:** present under [StandardProcesses](core-bl/Source/si-bl-process-platform-build/WorkUnits/FlowWorkUnits/StandardProcesses/CreateSingleDocument.wu); **not** listed in baseline pack §B1 table.
6. **`UserActionExecuter` URL routing remains document-flow-only** — **Fact:** [UserActionExecuter.cs](core-bl/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessPlatform.Runtime/UserActions/UserActionExecuter.cs) `switch` only covers `DocumentFlowApproval` … `DocumentFlowDispatch`; Share With follows the documented “return false → engine / legacy BIF” pattern **(inferred)** for client URL resolution.
7. **ADO: localization dialog story moved to Active** — **Fact:** [420545](https://dev.azure.com/tieto-si/360/_workitems/edit/420545) `System.State` = **Active**, `System.ChangedDate` = **2026-05-08**; baseline pack §E listed **420545** as **New**.
8. **ADO: new explicit backlog for Process View activity list + list localization** — **Fact:** [420676](https://dev.azure.com/tieto-si/360/_workitems/edit/420676) **New**, changed **2026-05-08**, description names `ProgressPlanApi.GetActivitiesForPhase` and `core-360-react-views/packages/process-components/src/ProcessView/ActivitiesForPhaseList.ts`.
9. **ADO hygiene churn on designer Features (same states)** — **Fact:** [414994](https://dev.azure.com/tieto-si/360/_workitems/edit/414994), [421477](https://dev.azure.com/tieto-si/360/_workitems/edit/421477), [421812](https://dev.azure.com/tieto-si/360/_workitems/edit/421812), [421813](https://dev.azure.com/tieto-si/360/_workitems/edit/421813) show `ChangedDate` on **2026-05-07**; states match baseline (**414994** Active, others **New**). Operational impact **(inferred):** low unless fields/comments changed beyond this pull.
10. **No additional PAF-tagged ADO motion after 2026-05-08** in the bounded WIQL used here — **Fact:** WIQL `ChangedDate >= 2026-05-08` with PAF/ProcessPlatform/title filters returned only **420676** and **420545** (query run **2026-05-10**).

---

## 2. Runtime delta

### New / expanded runtime surfaces

| Area | Delta vs 2026-05-07 pack | Evidence |
|------|---------------------------|----------|
| **New `EnumActionType`** | `ShareWithDialog = 17` not reflected in pack §C1 narrative | [EnumActionType.cs](core-bl/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessPlatform.Shared/Types/EnumActionType.cs) |
| **New progress-plan client activity** | Share With toolbox activity + child-activity model | [ShareWithDialog.cs](core-bl/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessEngine.Activities/ProgressPlan/ClientActions/ShareWithDialog.cs) |
| **New user-action handler** | `ShareWithUserActionHandler` not in pack §C2 table | [ShareWithUserActionHandler.cs](core-bl/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessPlatform.Runtime/UserActions/ShareWith/ShareWithUserActionHandler.cs) |
| **Client API** | `ShareWithDialogApi` not in pack §A / §C2 | [ShareWithDialogApi.cs](core-bl/Source/si-bl-process-platform-build/SI.Client.Api.Process/UserActions/ShareWithDialog/ShareWithDialogApi.cs) |
| **Tests** | New unit coverage signal | [ShareWithUserActionHandlerTests.cs](core-bl/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessPlatform.UnitTest/Runtime/UserActions/ShareWith/ShareWithUserActionHandlerTests.cs) |

### Orchestration / routing

- **Fact:** `UserActionExecuter.TryResolveUserActionUrl` still resolves **only** document-flow client URLs; default branch returns `false` for other `EnumActionType` values ([UserActionExecuter.cs](core-bl/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessPlatform.Runtime/UserActions/UserActionExecuter.cs)).
- **(inferred):** Share With remains on the **legacy BIF / engine** URL path unless a future change adds it to `UserActionExecuter` (same class-level contract described in baseline pack §H).

### Rules / DMN / plugins

- **No delta claimed:** no new `RuleSetExecuter` / DMN / `[Action]` evidence was gathered beyond baseline in this pass.

---

## 3. UX delta

- **Fact:** `ShareWithDialogApi` exists under `SI.Client.Api.Process` (see §2). **(inferred):** enables a React or host surface to drive Share With similarly to other dialog APIs once wired.
- **Fact:** `rg` under `core-360-react-views/packages/process-components` for `ShareWith` returned **no** matches in this workspace snapshot. **(inferred):** first-class **ProcessView** integration for Share With is **not** evidenced in `process-components` the way milestone/stage/process dialogs are in baseline §D1.
- **Fact:** ADO **420676** explicitly targets `ProgressPlanApi.GetActivitiesForPhase` and `ActivitiesForPhaseList.ts` for **resolved localization** on the phase activity list — backlog refinement for Process View, not verified shipped code in this pass.

---

## 4. Reuse delta

| Item | Delta | Evidence |
|------|-------|----------|
| **Toolbox building block** | “User: Share with” activity for modelers | [ShareWithDialog.cs](core-bl/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessEngine.Activities/ProgressPlan/ClientActions/ShareWithDialog.cs) attributes |
| **Standard process** | `CreateSingleDocument.wu` | [CreateSingleDocument.wu](core-bl/Source/si-bl-process-platform-build/WorkUnits/FlowWorkUnits/StandardProcesses/CreateSingleDocument.wu) |
| **SharedComponents** | No change claimed vs baseline | not re-counted |

---

## 5. ADO maturity delta

| Work item | Baseline (2026-05-07 pack) | Current (2026-05-10 pull) | Notes |
|-----------|----------------------------|---------------------------|--------|
| **420545** | New (§E) | **Active**, changed **2026-05-08** | **Fact:** state transition; scope text centers on resolving localization IDs in Stage/Milestone/Process dialog APIs. |
| **420676** | Not in baseline table | **New**, changed **2026-05-08** | **Fact:** expands localization work to lists, dropdowns, **GetActivitiesForPhase**, per WI description. |
| **414994, 421477, 421812, 421813** | Same states in pack | Same states; **ChangedDate** 2026-05-07 | **Fact:** metadata touch only in this snapshot. |
| **Other epics/features in pack §G** | e.g. **414328** New, **414727** New, **418321** New, … | Unchanged in batch fields pulled | **Fact:** `wit_get_work_items_batch_by_ids` for the baseline anchor set (no state deltas detected in that batch). |

**WIQL (bounded):** PAF/ProcessPlatform/title filters, `ChangedDate >= 2026-05-08`, returned **420676** and **420545** only (six items for `>= 2026-05-07` including the May-7 metadata touches above).

---

## 6. Pilot impact assessment

**What changes pilot scope / reality**

- **Share With in progress plans:** new user-facing branch (pin/share + optional child activities) once modelers adopt the toolbox activity — **Fact:** composition model in [ShareWithDialog.cs](core-bl/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessEngine.Activities/ProgressPlan/ClientActions/ShareWithDialog.cs). **(inferred):** expands pilot scenario catalog (permissions, contacts, notes, child milestones/stages/processes).
- **New shipped standard process asset** `CreateSingleDocument.wu` — **Fact:** file path above. **(inferred):** may change which reference progress plans exist in tenant packages if this asset is included in deployment scope.

**What reduces risk**

- **420545 → Active** and **420676** detailing `GetActivitiesForPhase` localization — **Fact:** ADO states/descriptions. **(inferred):** when implemented, reduces pilot risk for multilingual tenants and raw localization GUID leakage called out in baseline §H.

**What introduces risk**

- **Share With + child activities:** more post-dialog orchestration paths; aligns with email/document-flow complexity called out in baseline for child activities (**421477** still **New**). **(inferred):** pilot QA matrix should add Share With × child-activity combinations.
- **ProcessView / React gap signal:** no `ShareWith` usage under `process-components` in `rg` snapshot — **(inferred):** risk of “BL ready, UX incomplete” for pilots expecting parity inside Process View unless another package hosts the dialog.

---

## Git history scan (`core-bl` → `Source/si-bl-process-platform-build`)

**Command pattern (Fact):** `git -C <core-bl> log --since="2026-05-07 00:00:00" --until="2026-05-11 23:59:59" --pretty=format:"%h|%ci|%s" --name-status -- Source/si-bl-process-platform-build`

**Commit list (newest first, merges excluded in one-line summary; all below touch only `Source/si-bl-process-platform-build`):**

| Commit | Date (author) | Subject | Operational note |
|--------|---------------|---------|-------------------|
| `18fbcdfe05` | 2026-05-08 15:24 +0200 | Share With user action – gateway, execute DTO, and post-execution children (#20034) | **High:** runtime handler, `PinAndShareItemsGateway`, meta (`ActivityMetaUpdate`, `ActivityPostExecutionStatements`), Client API, Pandora harness + unit tests, WWF harness XAML. https://github.com/te-industry-public360/core-bl/commit/18fbcdfe05 |
| `8fec07213e` | 2026-05-08 12:27 +0200 | ProcessPlatform due dates - DueDateCalculationType and DbExecuter.SqlDateTimeFormat (#20032) | **Medium:** `ApprovalUserActionHandler`, `ReviewUserActionHandler`, new `DueDateCalculationType.cs`. https://github.com/te-industry-public360/core-bl/commit/8fec07213e |
| `da050b86f5` | 2026-05-08 15:25 +0530 | BL-Trigered milestone config entry (#20026) | **Medium:** refines document milestone orchestration; deletes `DocumentMilestoneTriggerRules.cs` (superseded path). https://github.com/te-industry-public360/core-bl/commit/da050b86f5 |
| `54d16fc0df` | 2026-05-08 12:06 +0530 | Making wu files shorter (#20021) | **Low for pilots:** test WU renames/moves under `Platform-WWF-WorkUnits/TestWorkUnits` (path length / fixture hygiene). https://github.com/te-industry-public360/core-bl/commit/54d16fc0df |
| `20bf834294` | 2026-05-08 11:50 +0530 | Jensemor/updateprocesseses (#20020) | **High:** adds `CreateSingleDocument.wu` + `.xaml`, touches many `StandardProcesses` `.wu`/`.xaml`, updates Flow work unit authoring skill docs. https://github.com/te-industry-public360/core-bl/commit/20bf834294 |
| `d539a0e541` | 2026-05-08 05:29 +0000 | Refactored - Trigger milestone update on document dispatch or receive (#20018) | **High:** document milestone orchestration refactor (`DocumentMilestoneOrchestrator` family), moves logic out of `Milestone/DocumentMilestoneTrigger.cs`. https://github.com/te-industry-public360/core-bl/commit/d539a0e541 |
| `c94f437f7e` | 2026-05-07 19:04 +0530 | BL - Trigger milestone - comments fix1 (#20015) | **Low:** follow-up on same milestone-on-document theme. https://github.com/te-industry-public360/core-bl/commit/c94f437f7e |
| `f4b265b21c` | 2026-05-07 17:06 +0530 | BL- Trigger milestone update on document dispatch or receive (#20004) | **High:** introduces `DocumentMetaInsert`/`DocumentMetaUpdate` under `Meta/Document`, `Milestone/DocumentMilestoneTrigger`, tests. https://github.com/te-industry-public360/core-bl/commit/f4b265b21c |
| `2478500380` | 2026-05-07 13:22 +0200 | Skip PluginEngine eventhander if BL is started from cliexec (#19992) | **Medium (governance/runtime):** `MethodInspector.cs` behavior for CLI-hosted BL. https://github.com/te-industry-public360/core-bl/commit/2478500380 |
| `f1a4de0035` | 2026-05-07 10:34 +0000 | Giving Permission to add document to public read as well. (#20002) | **Medium:** `StageApi.cs` permission surface. https://github.com/te-industry-public360/core-bl/commit/f1a4de0035 |
| `65cdb1ad5e` | 2026-05-07 11:33 +0200 | Kristbjo/api fix (#20000) | **Medium:** document-flow wizard/dialog/meeting harness + `FlowPhaseChildWaitTaskContainer`, milestone/process operations, harness WUs. https://github.com/te-industry-public360/core-bl/commit/65cdb1ad5e |

**Files with no commits in this window (Fact):** `git log --since=2026-05-07 -- Source/.../EnumActionType.cs` and same for `UserActionExecuter.cs` returned **empty** (enum / executer switch were not modified on or after 2026-05-07 in this branch snapshot).

**Related pre-window commit (Fact):** `git log -3 -- Source/.../EnumActionType.cs` shows `83cb8b683d` (#19989) as the latest touch for `EnumActionType` before the commits above.

---

## References

- Baseline: [documents/work/360-flow-operational-intelligence.md](360-flow-operational-intelligence.md)
- ADO: https://dev.azure.com/tieto-si/360/_workitems/edit/420545  
- ADO: https://dev.azure.com/tieto-si/360/_workitems/edit/420676  
- Code paths listed in §1–§4 above.


---

# Appendix D — Current Operational UX / Workspace Model

# 360 Flow — Current operational UX / workspace model

**Scope:** How operational work is surfaced **today** in this repo (React `process-views` + `process-components`, adjacent packages). **Fact** = file path or ADO work item. **(inferred)** = reasonable conclusion from absence of code hits in scoped paths, not verified end-to-end in product shell.

**Related packs:** [360-flow-operational-intelligence.md](360-flow-operational-intelligence.md) (§D UX inventory, §E pilot map), [360-flow-capability-matrix.md](360-flow-capability-matrix.md), [360-flow-governance-configurability.md](360-flow-governance-configurability.md).

---

## 1. UX surface inventory

| Surface | Where it lives (repo) | How it is reached / composed | Primary data / BL touchpoints |
|--------|------------------------|------------------------------|-------------------------------|
| **ProcessView (case progress plan)** | [process-components/src/ProcessView/ProcessViewComponent.tsx](core-360-react-views/packages/process-components/src/ProcessView/ProcessViewComponent.tsx) | Routed as `DMS/CaseDetails/ProcessView` from [apps/process-views/src/Routes.tsx](core-360-react-views/apps/process-views/src/Routes.tsx) (lazy `ProcessViewComponent`) | `ProgressPlanDetailsEntity`, `ProgressPlanPhaseList` procedures; URL `recno` / optional `ppRecno` **(Fact:** props + `URLSearchParams` in component) |
| **Phase + activity list (within ProcessView)** | [PhaseComponent.tsx](core-360-react-views/packages/process-components/src/ProcessView/PhaseComponent.tsx), [ActivitiesForPhaseList.ts](core-360-react-views/packages/process-components/src/ProcessView/ActivitiesForPhaseList.ts) | Nested under `CollapsibleList` when multiple phases; single-phase layout when one phase **(Fact:** `ProcessViewComponent.tsx`) | `GetActivitiesForPhaseProcedure` / `activityTableListName`; `ProgressPlanApi.ClosePhase` **(Fact:** `PhaseComponent.tsx`) |
| **Activity actions (execute, edit, cancel, reactivate, info)** | [Actions/ActionsComponent.tsx](core-360-react-views/packages/process-components/src/ProcessView/Actions/ActionsComponent.tsx), [ActionIconButtons.tsx](core-360-react-views/packages/process-components/src/ProcessView/Actions/ActionIconButtons.tsx), [ExecuteButtonComponent.tsx](core-360-react-views/packages/process-components/src/ProcessView/Actions/ExecuteButtonComponent.tsx) | Per activity row in `PhaseComponent` | `EnumActionType` (e.g. `MilestoneDialog`, `StageDialog`, `CreateProcessDialog`); client URLs / `BifOrFibDialog` routes **(Fact:** imports + `onClientActionExecution` in `ActionsComponent.tsx`) |
| **Activity dialogs (PAF-configured types)** | [ActivityDialogComponents/CreateMilestoneDialog](core-360-react-views/packages/process-components/src/ProcessView/ActivityDialogComponents/CreateMilestoneDialog), [CreateStageDialog](core-360-react-views/packages/process-components/src/ProcessView/ActivityDialogComponents/CreateStageDialog), [CreateProcessDialog](core-360-react-views/packages/process-components/src/ProcessView/ActivityDialogComponents/CreateProcessDialog) | Opened from `ActionIconButtons` when execute sets `isDialogVisible` and `actionType` matches **(Fact:** `ActionIconButtons.tsx`) | Aligned with BL handlers documented in [360-flow-operational-intelligence.md §A/C](360-flow-operational-intelligence.md) |
| **Edit progress plan / activity metadata** | [EditProcessDialog.tsx](core-360-react-views/packages/process-components/src/ProcessView/EditProcessDialog.tsx) | Triggered from `ActionsComponent` / edit button path **(Fact:** `ActionsComponent.tsx` imports) | Entity-driven form; deprecated string `methodName` prop noted in interface **(Fact:** `EditProcessDialog.tsx` lines 33–36) |
| **Milestone folder views (case + project)** | [FolderViews/Milestones/Milestones.tsx](core-360-react-views/apps/process-views/src/FolderViews/Milestones/Milestones.tsx) | Routes `DMS/Project/FolderViews/Milestones` and `…/Simple/Milestones` **(Fact:** [FolderViewRoutes.tsx](core-360-react-views/apps/process-views/src/Routes/FolderViewRoutes.tsx)) | `MilestoneDialog`, `enumMilestoneParentType`, `ProcessModelInfoEntity` from `@si/process-components` **(Fact:** `Milestones.tsx` imports) |
| **Case milestones + “by stage” toggle** | [CaseStageMilestones.tsx](core-360-react-views/apps/process-views/src/FolderViews/Case/CaseMilestones/CaseStageMilestones.tsx), [CaseMilestonesTable](core-360-react-views/apps/process-views/src/FolderViews/Case/CaseMilestones/CaseMilestonesTable.tsx), [StageMilestonesTable](core-360-react-views/apps/process-views/src/FolderViews/Case/CaseMilestones/StageMilestonesTable.tsx) | Routes `DMS/Case/FolderViews/Milestones` and `DMS/Case/FolderViews/Simple/Milestones` **(Fact:** `FolderViewRoutes.tsx`) | `getGetCaseProcessModelProcedure`; `StageViewsList` / `StageViewsListID` on stage table path **(Fact:** `CaseStageMilestones.tsx`, `StageMilestonesTable.tsx` per prior grep) |
| **MilestoneDialog (create/edit milestone record)** | [Milestone/MilestoneDialog.tsx](core-360-react-views/packages/process-components/src/Milestone/MilestoneDialog.tsx) | Used from milestone folder views and stage row actions **(Fact:** exports in [process-components/src/index.ts](core-360-react-views/packages/process-components/src/index.ts); app imports in `Milestones.tsx`, `OnRenderEditButton.tsx`) | `MilestoneApi` generated procedures **(Fact:** `MilestoneDialog.tsx` imports) |
| **Stage views list (typed list contract)** | [Types/StageViewsList.ts](core-360-react-views/packages/process-components/src/Types/StageViewsList.ts) | Consumed in case stage milestones UI and **PNB** case file viewer **(Fact:** grep: `StageMilestonesTable.tsx`, [PNBCaseFileViewer.tsx](core-360-react-views/apps/360-pnb-views/src/FullPageView/CaseDetails/PNBCaseFileViewer/PNBCaseFileViewer.tsx)) | List procedures bound in those components **(inferred)** per `fib-platform` list pattern |
| **Supporting dialogs (case / progress plan)** | [DialogViewRoutes.tsx](core-360-react-views/apps/process-views/src/Routes/DialogViewRoutes.tsx) | `DMS/Case/Dialog/AddStageDialogView`, `DMS/Dialog/EditResponsible`, deficiency dialogs | Mix of `process-components` and app-local `DialogViews` **(Fact:** route file) |
| **Checklist / deficiencies (adjacent case workspace)** | [FolderViewRoutes.tsx](core-360-react-views/apps/process-views/src/Routes/FolderViewRoutes.tsx) | `DMS/Case/FolderViews/Checklist`, `FolderViews/eBy/DeficienciesAndConditions` | Same case shell; not PAF runtime itself but shares `process-components` **(Fact:** routes) |
| **Business rules admin (governance of rules, not milestones)** | [AdminRulesRoutes.tsx](core-360-react-views/apps/process-views/src/Routes/AdminRulesRoutes.tsx) | `Admin/BusinessRules/*` | Rule set dashboard/editor/manager — **separate** from ProcessView **(Fact:** route file) |
| **Legacy workflow webpart** | [workflow-components/src/webpartRoutes.tsx](core-360-react-views/packages/workflow-components/src/webpartRoutes.tsx), `webparts/AllWorkflows/*` | Host route key `DMS/WebParts/AllWorkFlowView` **(Fact:** `webpartRoutes.tsx`) | `SI.Client.Api.Workflow` product line per [360-flow-operational-intelligence.md §D2](360-flow-operational-intelligence.md) — **not** `SI.Client.Api.Process` ProcessView |
| **Worklists** | No matches under [apps/process-views](core-360-react-views/apps/process-views) in scoped search | **(inferred)** Operational entry is not implemented as a first-class React route in this app slice | Tracked as product backlog: [411634](https://dev.azure.com/tieto-si/360/_workitems/edit/411634) (**Fact, ADO**) |
| **Desktops (process-model-centric)** | No `desktop` / `Desktop` string matches under `apps/process-views` in scoped search | **(inferred)** Not evidenced as named workspace primitive in this React app | Active feature: [414651](https://dev.azure.com/tieto-si/360/_workitems/edit/414651) under Epic [414727](https://dev.azure.com/tieto-si/360/_workitems/edit/414727) (**Fact, ADO** per prior packs) |
| **PMC / process model tree admin** | `StageProcessConfig` / `ProcessModelConfig` **TypeScript contracts** in [fib-bl-api/.../StageProcessConfig](core-360-react-views/packages/fib-bl-api/src/SI/Client/Api/Process/StageProcessConfig) | **No** `process-views` route referencing PMC UI found in grep | Backlog/admin intent: [410828](https://dev.azure.com/tieto-si/360/_workitems/edit/410828) “PMC - Admin…” under Epic **414727** (**Fact, ADO** per [360-flow-operational-intelligence.md §G6](360-flow-operational-intelligence.md)) |

---

## 2. Role-based workspace map

| Actor / intent | Primary surfaces today | Evidence |
|----------------|------------------------|----------|
| **Case handler (operational)** | ProcessView (`DMS/CaseDetails/ProcessView`); optional folder tabs Milestones / Checklist / deficiencies | [Routes.tsx](core-360-react-views/apps/process-views/src/Routes.tsx), [FolderViewRoutes.tsx](core-360-react-views/apps/process-views/src/Routes/FolderViewRoutes.tsx) |
| **Case handler (milestone overview)** | `CaseStageMilestones` — toggle “milestones in case” vs “milestones by stage” when `GetCaseProcessModel` returns non-zero | [CaseStageMilestones.tsx](core-360-react-views/apps/process-views/src/FolderViews/Case/CaseMilestones/CaseStageMilestones.tsx) |
| **Project user (milestone table)** | `Milestones` folder view with `enumMilestoneParentType.Project` | [FolderViewRoutes.tsx](core-360-react-views/apps/process-views/src/Routes/FolderViewRoutes.tsx) |
| **Sector / PNB host** | `StageViewsList` embedded in PNB case file viewer | [PNBCaseFileViewer.tsx](core-360-react-views/apps/360-pnb-views/src/FullPageView/CaseDetails/PNBCaseFileViewer/PNBCaseFileViewer.tsx) |
| **Rules administrator** | `Admin/BusinessRules/*` only in `process-views` | [AdminRulesRoutes.tsx](core-360-react-views/apps/process-views/src/Routes/AdminRulesRoutes.tsx) |
| **Process / PMC modeler (management)** | **Not** mapped to a `process-views` route in this scan; BL client types exist | `fib-bl-api` StageProcessConfig; ADO [410828](https://dev.azure.com/tieto-si/360/_workitems/edit/410828) |

---

## 3. Process-centered vs task-centered behavior

| Dimension | Current behavior | Evidence |
|-----------|------------------|----------|
| **Primary frame** | **Process-centered:** UI is anchored on a **progress plan** (`ppRecno` / URL) and **phases** rendered as collapsible sections | [ProcessViewComponent.tsx](core-360-react-views/packages/process-components/src/ProcessView/ProcessViewComponent.tsx) loads `progressPlanDetailsEntityName` + `progressPlanPhaseListName`, maps phases to `CollapsibleList` |
| **Work unit** | **Task-centered at the row:** each **activity** under a phase lists status icons, dates, wait-task handling, and an **action strip** | [PhaseComponent.tsx](core-360-react-views/packages/process-components/src/ProcessView/PhaseComponent.tsx) + `ActionsComponent` |
| **Execution** | **Task-triggered dialogs:** `EnumActionType` drives which Fib/React dialog mounts (`SetMilestoneConfigsDialog`, `SetStageConfigsDialog`, `SetProcessConfigsDialog`) | [ActionIconButtons.tsx](core-360-react-views/packages/process-components/src/ProcessView/Actions/ActionIconButtons.tsx) |
| **Cross-cutting** | Some actions still use **legacy BIF / window** patterns (`commonModalDialogClose`, `ProgressPlanActivity` window sizing) alongside Fib | [ActionsComponent.tsx](core-360-react-views/packages/process-components/src/ProcessView/Actions/ActionsComponent.tsx) (`onCloseActivityLegacyBifDialog`, `onClientActionExecution` opening `http` URLs) |

**Summary:** Operators navigate **by case progress plan and phase**; they complete work **per activity** via execute/edit/cancel flows.

---

## 4. Current operational overview capabilities

| Capability | Present? | Where |
|------------|----------|-------|
| **Single-case progress plan header (name, deadline when expanded)** | Yes | [ProcessViewComponent.tsx](core-360-react-views/packages/process-components/src/ProcessView/ProcessViewComponent.tsx) |
| **Multi-phase collapse / expand** | Yes | `CollapsibleList` + `defaultExpandedActivityRecno` from current phase **(Fact:** same file) |
| **Per-phase activity list with status visualization** | Yes | [PhaseComponent.tsx](core-360-react-views/packages/process-components/src/ProcessView/PhaseComponent.tsx) |
| **Close phase** | Yes (when BL enables button) | `ProgressPlanApi.ClosePhase` in `PhaseComponent` |
| **Wait-task status controls** | Yes | `WaittaskSetStatusComponent`, `useWaitTaskStatus` **(Fact:** `PhaseComponent.tsx` imports) |
| **Decision rows** | Yes | `DecisionComponent` **(Fact:** `PhaseComponent.tsx`) |
| **Milestone overview (case vs by-stage)** | Yes | [CaseStageMilestones.tsx](core-360-react-views/apps/process-views/src/FolderViews/Case/CaseMilestones/CaseStageMilestones.tsx) |
| **Cross-case work queue (“worklist”)** | Not in this React app slice | ADO [411634](https://dev.azure.com/tieto-si/360/_workitems/edit/411634) |
| **Process-model-specific desktop layout** | Not evidenced in `process-views` | ADO [414651](https://dev.azure.com/tieto-si/360/_workitems/edit/414651) |
| **Operator-visible localization completeness for activity list** | Gap tracked | ADO [420676](https://dev.azure.com/tieto-si/360/_workitems/edit/420676) names `ActivitiesForPhaseList.ts` and `GetActivitiesForPhase` **(Fact, ADO** per [360-flow-operational-delta-since-2026-05-07.md](360-flow-operational-delta-since-2026-05-07.md)) |

---

## 5. Current management visibility capabilities

| Capability | Present? | Where / note |
|------------|----------|----------------|
| **Edit milestone (dialog)** | Yes | `MilestoneDialog` + folder views **(Fact:** `MilestoneDialog.tsx`, `Milestones.tsx`) |
| **Stage / milestone tables in case folder** | Yes | `CaseMilestonesTable`, `StageMilestonesTable` under [FolderViews/Case/CaseMilestones](core-360-react-views/apps/process-views/src/FolderViews/Case/CaseMilestones) |
| **Edit progress plan properties (responsible, title, due)** | Yes | `EditProcessDialog` from activity actions **(Fact:** `EditProcessDialog.tsx`, `ActionsComponent.tsx`) |
| **DMN rule set lifecycle UI** | Yes (admin) | [AdminRulesRoutes.tsx](core-360-react-views/apps/process-views/src/Routes/AdminRulesRoutes.tsx) |
| **PMC tree / stage-process-config visual admin** | **Not** found as routed UI in `process-views` | Types in `fib-bl-api`; ADO [410828](https://dev.azure.com/tieto-si/360/_workitems/edit/410828) |
| **Designer Features (send email, meeting, document flow)** | Backlog states vs code — see pilot pack | [360-flow-operational-intelligence.md §E](360-flow-operational-intelligence.md); Features [418321](https://dev.azure.com/tieto-si/360/_workitems/edit/418321), [418326](https://dev.azure.com/tieto-si/360/_workitems/edit/418326), [421812](https://dev.azure.com/tieto-si/360/_workitems/edit/421812), [421813](https://dev.azure.com/tieto-si/360/_workitems/edit/421813) |

**Summary:** Management **visibility** today is **case- or project-scoped milestone tables**, **per-activity / progress-plan edits**, and **rules admin** — not a unified PMC cockpit in this package.

---

## 6. UX inconsistencies / transitional areas

| Topic | Observation | Evidence |
|-------|-------------|----------|
| **Dual dialog stacks** | Same activity strip supports Fib routes **and** legacy BIF / modal window flows | `onCloseActivityLegacyBifDialog`, `commonModalDialogClose`, `window.open(..., 'ProgressPlanActivity', ...)` in [ActionsComponent.tsx](core-360-react-views/packages/process-components/src/ProcessView/Actions/ActionsComponent.tsx) |
| **Styling debt** | Hardcoded class names `Multiple-Phases-Container` / `Single-Phase-Container` called out as non–Griffel pattern | Comment block in [ProcessViewComponent.tsx](core-360-react-views/packages/process-components/src/ProcessView/ProcessViewComponent.tsx) ~169–171 |
| **Type / status edge** | Comment notes `ActivityInfo` / `IsActive` mismatch | [PhaseComponent.tsx](core-360-react-views/packages/process-components/src/ProcessView/PhaseComponent.tsx) ~52–53 |
| **“Workflow” vs “Flow”** | Separate **AllWorkflows** webpart package vs **ProcessView** (`SI.Client.Api.Process`) | [webpartRoutes.tsx](core-360-react-views/packages/workflow-components/src/webpartRoutes.tsx) vs [Routes.tsx](core-360-react-views/apps/process-views/src/Routes.tsx) |
| **Backlog vs shell** | ADO tracks **worklists** and **desktops**; this React app does not expose them by those names | [411634](https://dev.azure.com/tieto-si/360/_workitems/edit/411634), [414651](https://dev.azure.com/tieto-si/360/_workitems/edit/414651) |
| **Async process model readiness** | ProcessView supports `isWaitingForProcessModel` / `showActivitiesLoading` overlays | [ProcessViewComponent.tsx](core-360-react-views/packages/process-components/src/ProcessView/ProcessViewComponent.tsx), [ProcessViewActivitiesSection.tsx](core-360-react-views/packages/process-components/src/ProcessView/ProcessViewActivitiesSection.tsx) |

---

## 7. Pilot-ready UX areas

These areas have **routed React surfaces** and **direct BL/procedure wiring** in-repo, suitable for **pilot hardening / QA** without assuming unshipped ADO scope.

| Area | Why pilot-ready | Pointers |
|------|-----------------|----------|
| **Case ProcessView** | Dedicated route; full phase → activity → action loop | [Routes.tsx](core-360-react-views/apps/process-views/src/Routes.tsx), [ProcessView/](core-360-react-views/packages/process-components/src/ProcessView/) |
| **PAF activity dialogs (milestone / stage / subprocess)** | Mounted from execute path with explicit `EnumActionType` | [ActionIconButtons.tsx](core-360-react-views/packages/process-components/src/ProcessView/Actions/ActionIconButtons.tsx) |
| **Case milestone folder (dual view)** | User-toggle between aggregate and stage-aligned tables | [CaseStageMilestones.tsx](core-360-react-views/apps/process-views/src/FolderViews/Case/CaseMilestones/CaseStageMilestones.tsx) |
| **Project milestones** | Routed folder view with `MilestoneDialog` | [FolderViewRoutes.tsx](core-360-react-views/apps/process-views/src/Routes/FolderViewRoutes.tsx), [Milestones.tsx](core-360-react-views/apps/process-views/src/FolderViews/Milestones/Milestones.tsx) |
| **Automated regression signal** | Tests exist around ProcessView and activities | e.g. [ProcessViewComponent.test.tsx](core-360-react-views/packages/process-components/src/ProcessView/Test/ProcessViewComponent.test.tsx), [ProcessViewActivitiesSection.test.tsx](core-360-react-views/packages/process-components/src/ProcessView/Test/ProcessViewActivitiesSection.test.tsx) |

**Explicitly outside “ready” for this document** (pending ADO / other host): worklists [411634](https://dev.azure.com/tieto-si/360/_workitems/edit/411634), desktops [414651](https://dev.azure.com/tieto-si/360/_workitems/edit/414651), PMC admin UI [410828](https://dev.azure.com/tieto-si/360/_workitems/edit/410828) — no matching routes found here.

---

## ADO index (used above)

- Epic **414727** — PAF User Experience: https://dev.azure.com/tieto-si/360/_workitems/edit/414727  
- **414651** — Desktops for Process Models: https://dev.azure.com/tieto-si/360/_workitems/edit/414651  
- **411634** — Worklists: https://dev.azure.com/tieto-si/360/_workitems/edit/411634  
- **410828** — PMC admin (stage-defined process): https://dev.azure.com/tieto-si/360/_workitems/edit/410828  
- **420676** — Process View activity list / localization: https://dev.azure.com/tieto-si/360/_workitems/edit/420676  

