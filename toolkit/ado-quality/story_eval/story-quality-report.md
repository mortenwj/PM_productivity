# User story quality report

**Evaluated (UTC):** `2026-03-31T13:13:03.138683+00:00`

## Scope

| | |
|---|---|
| Team | Core-Process-platform |
| Iteration | PP - 22 - 16.03.2026 - 03.04.2026 |
| Work item types | User Story |
| Stories evaluated | 71 |

## Evaluation notes

- Work item batch loaded from local file: story_eval/pp22_mcp_batch_current.json.
- Automated heuristic scoring from System.Description, Microsoft.VSTS.Common.AcceptanceCriteria, System.Parent, Microsoft.VSTS.Common.Risk, and Custom.Riskdescription.
- Risk classification uses Microsoft.VSTS.Common.Risk (1–3). Risk description uses Custom.Riskdescription when risk is 1 or 2.

## Aggregate summary

| Metric | Value |
|--------|-------|
| Count | 71 |
| Avg final score | 45.4 |
| Non-compliant | 68 |

### Top systemic issues

- Unset or invalid Microsoft.VSTS.Common.Risk; populate Risk (1–3) and Risk description when risk is 1–2.
- Many standard stories deviate from strict As a / I want / so that and Gherkin AC; see per-item issues.

### Quick wins

- Add Given/When/Then to Acceptance Criteria field for stories with bullets-only AC.
- Shorten or split very large descriptions that look like multi-sprint specs.

## Story summary

| ID | Title | Score | Status | Parent Feature/Epic | Format | AC | Risk | Parent |
|---:|---|---:|:---|:---:|:---:|:---:|:---:|:---:|
| [230794](https://dev.azure.com/tieto-si/360/_workitems/edit/230794) | PE Designer Component - Create a Milestone | 91.6 | Compliant | Yes | 100 | 100 | 100 | 100 |
| [230795](https://dev.azure.com/tieto-si/360/_workitems/edit/230795) | PE Designer Component - Create a Stage | 49.6 | Non-Compliant | Yes | 25 | 0 | 100 | 100 |
| [273412](https://dev.azure.com/tieto-si/360/_workitems/edit/273412) | PMC - Admin - Revert changes on the progressplan BIF page | 44.6 | Non-Compliant | Yes | 25 | 30 | 0 | 100 |
| [280267](https://dev.azure.com/tieto-si/360/_workitems/edit/280267) | Keep Process Trigger Configuration when Creating Copy of Models, St… | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [307028](https://dev.azure.com/tieto-si/360/_workitems/edit/307028) | PM - DB & Meta - Change to multi trigger system | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [307036](https://dev.azure.com/tieto-si/360/_workitems/edit/307036) | PM - Admin - React - New dialog for choosing (Parent) Trigger Autom… | 54.8 | Non-Compliant | Yes | 25 | 15 | 0 | 100 |
| [307040](https://dev.azure.com/tieto-si/360/_workitems/edit/307040) | PM - Admin - BL - API for searching Automation IDs | 57.9 | Non-Compliant | Yes | 100 | 0 | 0 | 100 |
| [307123](https://dev.azure.com/tieto-si/360/_workitems/edit/307123) | PM - BL - Make sure AutomationIDs are uniqe across entities | 66.0 | Non-Compliant | Yes | 100 | 15 | 0 | 100 |
| [307153](https://dev.azure.com/tieto-si/360/_workitems/edit/307153) | PM - BL - Trigger all entities connected to triggering (parent) | 66.0 | Non-Compliant | Yes | 100 | 15 | 0 | 100 |
| [307171](https://dev.azure.com/tieto-si/360/_workitems/edit/307171) | PM - BL - Comment out code using TriggerAutomationId | 57.9 | Non-Compliant | Yes | 100 | 0 | 0 | 100 |
| [307202](https://dev.azure.com/tieto-si/360/_workitems/edit/307202) | PM - BL - Uncomment commented code | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [349917](https://dev.azure.com/tieto-si/360/_workitems/edit/349917) | PM - Trigger - DB & Meta - Add AutomationID on MilestoneConfig | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [350217](https://dev.azure.com/tieto-si/360/_workitems/edit/350217) | PM - Trigger - BL - AutomationID validations | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [364011](https://dev.azure.com/tieto-si/360/_workitems/edit/364011) | Mailscanner migration - Register the unregistered document instead … | 86.6 | Compliant | Yes | 100 | 60 | 100 | 100 |
| [379584](https://dev.azure.com/tieto-si/360/_workitems/edit/379584) | DB Changes: Milestone and Case Connection Removal | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [381921](https://dev.azure.com/tieto-si/360/_workitems/edit/381921) | DB - Create data model for Process Model Capabilities | 44.6 | Non-Compliant | Yes | 25 | 30 | 0 | 100 |
| [382094](https://dev.azure.com/tieto-si/360/_workitems/edit/382094) | PMC - Admin - TreeView - Support for accessibility and keyboard nav… | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [391652](https://dev.azure.com/tieto-si/360/_workitems/edit/391652) | Stage defined process - NOR "Mottak" - ENU "Received- Process" | 54.9 | Non-Compliant | Yes | 100 | 0 | 0 | 100 |
| [394044](https://dev.azure.com/tieto-si/360/_workitems/edit/394044) | PMC - StageTemplate - TemplateState Validations and Logic | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [397393](https://dev.azure.com/tieto-si/360/_workitems/edit/397393) | BEFORE ASYNC - PM - Performance - Analyse of ProcessModel cloning f… | 42.8 | Non-Compliant | Yes | 25 | 15 | 0 | 100 |
| [397394](https://dev.azure.com/tieto-si/360/_workitems/edit/397394) | Started - PM - Performance - Identify instance-specific fields in c… | 42.8 | Non-Compliant | Yes | 25 | 15 | 0 | 100 |
| [397400](https://dev.azure.com/tieto-si/360/_workitems/edit/397400) | PM - Performance – Investigate abnormal MilestoneConfig & StageProc… | 35.2 | Non-Compliant | Yes | 25 | 15 | 0 | 100 |
| [397406](https://dev.azure.com/tieto-si/360/_workitems/edit/397406) | PM - Performance – Analyse of legacy StageTemplate behaviour and re… | 42.8 | Non-Compliant | Yes | 25 | 15 | 0 | 100 |
| [398964](https://dev.azure.com/tieto-si/360/_workitems/edit/398964) | PMC - Admin - HitoricView - Display what version we are looking at | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [399014](https://dev.azure.com/tieto-si/360/_workitems/edit/399014) | PM360 - Urestricted Milestones - Add Milestones on a Closed Stage | 76.6 | Non-Compliant | Yes | 100 | 100 | 0 | 100 |
| [399150](https://dev.azure.com/tieto-si/360/_workitems/edit/399150) | PM - P360 - UI - Analyze all API calls executed during case UI load | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [399156](https://dev.azure.com/tieto-si/360/_workitems/edit/399156) | TO FIX Cache - PM - Performance - Analyze StageApi/CalculateDeadLin… | 44.6 | Non-Compliant | Yes | 25 | 30 | 0 | 100 |
| [399167](https://dev.azure.com/tieto-si/360/_workitems/edit/399167) | OK - PM - Performance - Analyze ChecklistInstanceView/GetChecklistT… | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [399169](https://dev.azure.com/tieto-si/360/_workitems/edit/399169) | TO FIX - PM - Performance - Analyze ChecklistInstanceView/GetMilest… | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [401241](https://dev.azure.com/tieto-si/360/_workitems/edit/401241) | PM - Performance – Analyze - Could we wait with creating the instan… | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [405221](https://dev.azure.com/tieto-si/360/_workitems/edit/405221) | Stage Closure Blocked Message Is Misleading When Milestones Are Sti… | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [407075](https://dev.azure.com/tieto-si/360/_workitems/edit/407075) | Input Field Loses Cursor Focus After Exceeding 50 Characters in Des… | 44.6 | Non-Compliant | Yes | 25 | 30 | 0 | 100 |
| [407206](https://dev.azure.com/tieto-si/360/_workitems/edit/407206) | Follow up - Fix focus issue in Deadline Control Web Part (Progress … | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [409527](https://dev.azure.com/tieto-si/360/_workitems/edit/409527) | PMC - Admin - ArgumentsTab - FrontEnd - Show arguments for global s… | 42.8 | Non-Compliant | Yes | 25 | 15 | 0 | 100 |
| [411061](https://dev.azure.com/tieto-si/360/_workitems/edit/411061) | IFAR processing should exclude file references | 36.6 | Non-Compliant | Yes | 55 | 0 | 0 | 100 |
| [411642](https://dev.azure.com/tieto-si/360/_workitems/edit/411642) | PM - Fix all places using Milestone.ToCase & Milestone.ToCaseKey - … | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [412227](https://dev.azure.com/tieto-si/360/_workitems/edit/412227) | E-mail scanner should remove spaces surrounding the names in config… | 32.8 | Non-Compliant | No | 25 | 15 | 0 | 0 |
| [413628](https://dev.azure.com/tieto-si/360/_workitems/edit/413628) | IFAR - Redaction - Enable flattening for PDF forms and emails | 71.6 | Non-Compliant | Yes | 100 | 60 | 0 | 100 |
| [414030](https://dev.azure.com/tieto-si/360/_workitems/edit/414030) | Major deficiency letter | 71.6 | Non-Compliant | Yes | 100 | 60 | 0 | 100 |
| [414452](https://dev.azure.com/tieto-si/360/_workitems/edit/414452) | Autoreceipt | 39.1 | Non-Compliant | Yes | 55 | 0 | 0 | 100 |
| [414618](https://dev.azure.com/tieto-si/360/_workitems/edit/414618) | Create documment with review and approval | 32.4 | Non-Compliant | Yes | 55 | 0 | 0 | 100 |
| [414619](https://dev.azure.com/tieto-si/360/_workitems/edit/414619) | PMC - DB - Add standard milestones | 67.9 | Non-Compliant | Yes | 100 | 30 | 0 | 100 |
| [414620](https://dev.azure.com/tieto-si/360/_workitems/edit/414620) | Add default outcome types | 39.1 | Non-Compliant | Yes | 55 | 0 | 0 | 100 |
| [414671](https://dev.azure.com/tieto-si/360/_workitems/edit/414671) | Implement initial DB | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [414751](https://dev.azure.com/tieto-si/360/_workitems/edit/414751) | UX - Design Process Model Capabilities Configuration UI | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [414762](https://dev.azure.com/tieto-si/360/_workitems/edit/414762) | PE Designer Component - Extend server action to support params | 49.6 | Non-Compliant | Yes | 25 | 0 | 100 | 100 |
| [414763](https://dev.azure.com/tieto-si/360/_workitems/edit/414763) | PE designer Create client action for registering milestone date | 49.6 | Non-Compliant | Yes | 25 | 0 | 100 | 100 |
| [414799](https://dev.azure.com/tieto-si/360/_workitems/edit/414799) | Add Application Master as an example in ProcessEngineToolkit | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [414845](https://dev.azure.com/tieto-si/360/_workitems/edit/414845) | Plan handling | 39.1 | Non-Compliant | Yes | 55 | 0 | 0 | 100 |
| [414846](https://dev.azure.com/tieto-si/360/_workitems/edit/414846) | Implement auto scroll and highlight process model item in sidebar a… | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [414862](https://dev.azure.com/tieto-si/360/_workitems/edit/414862) | Process Withdrawn | 32.4 | Non-Compliant | Yes | 55 | 0 | 0 | 100 |
| [414875](https://dev.azure.com/tieto-si/360/_workitems/edit/414875) | PM - Trigger - UI - Enable Automation ID on Milestone | 44.6 | Non-Compliant | Yes | 25 | 30 | 0 | 100 |
| [414964](https://dev.azure.com/tieto-si/360/_workitems/edit/414964) | PMC - DB - Remove required Case Type on MilestoneTypes | 44.6 | Non-Compliant | Yes | 25 | 30 | 0 | 100 |
| [414997](https://dev.azure.com/tieto-si/360/_workitems/edit/414997) | PE Designer Component - Create a Milestone Dialog in Case Handling … | 59.6 | Non-Compliant | Yes | 25 | 30 | 100 | 100 |
| [415106](https://dev.azure.com/tieto-si/360/_workitems/edit/415106) | Move CreateMilestoneOnStage logic to MilestoneMetaHandlers | 67.9 | Non-Compliant | Yes | 100 | 30 | 0 | 100 |
| [415193](https://dev.azure.com/tieto-si/360/_workitems/edit/415193) | GEMI - Create Document for Mail-enabled Security Group for GEMI per… | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [415772](https://dev.azure.com/tieto-si/360/_workitems/edit/415772) | Support Stage pre-selection in New Document Wizard and Dialog when … | 60.4 | Non-Compliant | Yes | 25 | 60 | 0 | 100 |
| [415985](https://dev.azure.com/tieto-si/360/_workitems/edit/415985) | Add standard milestone status | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [415988](https://dev.azure.com/tieto-si/360/_workitems/edit/415988) | Add standard contact - case roles | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [415992](https://dev.azure.com/tieto-si/360/_workitems/edit/415992) | add shorcmong statuses | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [415994](https://dev.azure.com/tieto-si/360/_workitems/edit/415994) | add condition statuses | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [415997](https://dev.azure.com/tieto-si/360/_workitems/edit/415997) | Add document categories | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [416101](https://dev.azure.com/tieto-si/360/_workitems/edit/416101) | Register or update milestone | 39.1 | Non-Compliant | Yes | 55 | 0 | 0 | 100 |
| [416108](https://dev.azure.com/tieto-si/360/_workitems/edit/416108) | Invoke subprocess as server action | 39.1 | Non-Compliant | Yes | 55 | 0 | 0 | 100 |
| [416208](https://dev.azure.com/tieto-si/360/_workitems/edit/416208) | Translations - Fileviewer | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [416287](https://dev.azure.com/tieto-si/360/_workitems/edit/416287) | Open URL with arguments | 54.1 | Non-Compliant | Yes | 55 | 0 | 100 | 100 |
| [416534](https://dev.azure.com/tieto-si/360/_workitems/edit/416534) | IFAR - Redaction - Enable flattening for PDF forms and emails - 5.18 | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [416667](https://dev.azure.com/tieto-si/360/_workitems/edit/416667) | UI - Admin panel - Create Extended Search Dialog for Workflow Defin… | 34.6 | Non-Compliant | Yes | 25 | 0 | 0 | 100 |
| [416922](https://dev.azure.com/tieto-si/360/_workitems/edit/416922) | PE designer component - email dialogue | 72.9 | Non-Compliant | Yes | 100 | 0 | 100 | 100 |
| [416932](https://dev.azure.com/tieto-si/360/_workitems/edit/416932) | Create process task | 39.1 | Non-Compliant | Yes | 55 | 0 | 0 | 100 |
| [417345](https://dev.azure.com/tieto-si/360/_workitems/edit/417345) | Dispatch dialogue | 86.6 | Compliant | Yes | 100 | 60 | 100 | 100 |

## Non-compliant detail (issues)

### #230795 — PE Designer Component - Create a Stage

- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #273412 — PMC - Admin - Revert changes on the progressplan BIF page

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).

### #280267 — Keep Process Trigger Configuration when Creating Copy of Models, Stages, StageTemplates

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #307028 — PM - DB & Meta - Change to multi trigger system

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #307036 — PM - Admin - React - New dialog for choosing (Parent) Trigger Automation ID

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).

### #307040 — PM - Admin - BL - API for searching Automation IDs

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #307123 — PM - BL - Make sure AutomationIDs are uniqe across entities

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Acceptance criteria should use explicit Gherkin (Given / When / Then).

### #307153 — PM - BL - Trigger all entities connected to triggering (parent)

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Acceptance criteria should use explicit Gherkin (Given / When / Then).

### #307171 — PM - BL - Comment out code using TriggerAutomationId

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #307202 — PM - BL - Uncomment commented code

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #349917 — PM - Trigger - DB & Meta - Add AutomationID on MilestoneConfig

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #350217 — PM - Trigger - BL - AutomationID validations

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #379584 — DB Changes: Milestone and Case Connection Removal

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #381921 — DB - Create data model for Process Model Capabilities

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).

### #382094 — PMC - Admin - TreeView - Support for accessibility and keyboard navigation

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #391652 — Stage defined process - NOR "Mottak" - ENU "Received- Process"

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #394044 — PMC - StageTemplate - TemplateState Validations and Logic

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #397393 — BEFORE ASYNC - PM - Performance - Analyse of ProcessModel cloning flow during case creation

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).

### #397394 — Started - PM - Performance - Identify instance-specific fields in cloned ProcessModel sub-entities

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).

### #397400 — PM - Performance – Investigate abnormal MilestoneConfig & StageProcessConfig row counts

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #397406 — PM - Performance – Analyse of legacy StageTemplate behaviour and requirements for redesign - UseLatestVersion

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).

### #398964 — PMC - Admin - HitoricView - Display what version we are looking at

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #399014 — PM360 - Urestricted Milestones - Add Milestones on a Closed Stage

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).

### #399150 — PM - P360 - UI - Analyze all API calls executed during case UI load

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #399156 — TO FIX Cache - PM - Performance - Analyze StageApi/CalculateDeadLine for unnecessary data loading

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).

### #399167 — OK - PM - Performance - Analyze ChecklistInstanceView/GetChecklistThemeList

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #399169 — TO FIX - PM - Performance - Analyze ChecklistInstanceView/GetMilestoneListByChecklist

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #401241 — PM - Performance – Analyze - Could we wait with creating the instances of the stac/milc/stapc until instantiation and get those from the templates

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #405221 — Stage Closure Blocked Message Is Misleading When Milestones Are Still Active

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #407075 — Input Field Loses Cursor Focus After Exceeding 50 Characters in Description/Admin Notes fields

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).

### #407206 — Follow up - Fix focus issue in Deadline Control Web Part (Progress Plan Overview)

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #409527 — PMC - Admin - ArgumentsTab - FrontEnd - Show arguments for global stage processes read only

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).

### #411061 — IFAR processing should exclude file references

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #411642 — PM - Fix all places using Milestone.ToCase & Milestone.ToCaseKey - Copy

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #412227 — E-mail scanner should remove spaces surrounding the names in configuration

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- No System.Parent; story must link to Feature or Epic.
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #413628 — IFAR - Redaction - Enable flattening for PDF forms and emails

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Acceptance criteria should use explicit Gherkin (Given / When / Then).

### #414030 — Major deficiency letter

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Acceptance criteria should use explicit Gherkin (Given / When / Then).

### #414452 — Autoreceipt

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #414618 — Create documment with review and approval

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #414619 — PMC - DB - Add standard milestones

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Acceptance criteria should use explicit Gherkin (Given / When / Then).

### #414620 — Add default outcome types

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #414671 — Implement initial DB

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #414751 — UX - Design Process Model Capabilities Configuration UI

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #414762 — PE Designer Component - Extend server action to support params

- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #414763 — PE designer Create client action for registering milestone date

- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #414799 — Add Application Master as an example in ProcessEngineToolkit

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #414845 — Plan handling

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #414846 — Implement auto scroll and highlight process model item in sidebar as per recno

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #414862 — Process Withdrawn

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #414875 — PM - Trigger - UI - Enable Automation ID on Milestone

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).

### #414964 — PMC - DB - Remove required Case Type on MilestoneTypes

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).

### #414997 — PE Designer Component - Create a Milestone Dialog in Case Handling view

- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).

### #415106 — Move CreateMilestoneOnStage logic to MilestoneMetaHandlers

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Acceptance criteria should use explicit Gherkin (Given / When / Then).

### #415193 — GEMI - Create Document for Mail-enabled Security Group for GEMI permission.

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #415772 — Support Stage pre-selection in New Document Wizard and Dialog when opened from Process Engine client action

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).

### #415985 — Add standard milestone status

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #415988 — Add standard contact - case roles

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #415992 — add shorcmong statuses

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #415994 — add condition statuses

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #415997 — Add document categories

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #416101 — Register or update milestone

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #416108 — Invoke subprocess as server action

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #416208 — Translations - Fileviewer

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #416287 — Open URL with arguments

- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #416534 — IFAR - Redaction - Enable flattening for PDF forms and emails - 5.18

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #416667 — UI - Admin panel - Create Extended Search Dialog for Workflow Definition Dropdown in Process Property

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #416922 — PE designer component - email dialogue

- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.

### #416932 — Create process task

- Set Microsoft.VSTS.Common.Risk to 1, 2, or 3 (field label: Risk on User Story).
- Standard user story should use classic As a / I want / so that format.
- Acceptance criteria should use explicit Gherkin (Given / When / Then).
- Acceptance criteria may be vague or insufficiently testable.
