# PAF pilot — weekly stakeholder update

**Oslo calendar note:** Generated from Azure DevOps WIQL using `@Today - 14` in the **organisation query timezone** (see spec for strict Oslo parity in a future hardening pass).
**ADO query as-of (UTC):** 2026-04-21T20:31Z (from MCP `wit_query_by_wiql`; see `projects/process-platform/pilot/tools/pilot_weekly_query_meta.json`).

**Disclaimer:** Draft for pilot communication — not a signed-off product release note. PR links and engineering identifiers are omitted from this weekly view.

## Scope (this run)

- Non-Bug work items: `Area Path` under `360\Core-Process-platform`, last **14 days** per WIQL (`PAF_pilot_weekly_report_SPEC.md`): **Closed/Resolved** dates for done work; **`Microsoft.VSTS.Common.StateChangeDate`** for **New** (not `System.ChangedDate` alone—stack rank updates); other states may use **ChangedDate**—see `projects/process-platform/pilot/tools/pilot_weekly_wiql_reference.md`.
- Epic assignment: walk `System.Parent` using MCP `wit_get_work_items_batch_by_ids` closure (`projects/process-platform/pilot/tools/pilot_weekly_parents_level1.json`).
- Epics in this run (in order): **411612** (NVE Pilot), **414727** (UX), **414328** (Standard Artifacts), **411614** (Core Platform). Work items that do not roll up under one of these four epics are **omitted** from this weekly view.
- *What it does* comes from **`projects/process-platform/pilot/tools/pilot_weekly_what_it_does_summaries.json`** when provided (stakeholder summary, not raw ADO text); otherwise a short **synthesized** line from `Purpose:` / user-story patterns. **`Microsoft.VSTS.Common.AcceptanceCriteria`** is still shown as *Outcome / acceptance* when present (overlay).
- User stories under Feature **413948** (NVE pilot processes) also get a **Process description** line: intent + blocks + flow extracted from the long HTML template in Description (similar depth to acceptance-style lines under Feature 400794).

---

## Epic 411612 — PAF – NVE Pilot

### Parent 411612

- **Feature** [413948](https://dev.azure.com/tieto-si/360/_workitems/edit/413948) — NVE Specific process definitions before go-live — *New* (activity ****)

### Parent 413948

- **User Story** [418785](https://dev.azure.com/tieto-si/360/_workitems/edit/418785) — NVE Process: Announcement — *Active* (activity **2026-04-17**)
  - *What it does:* Lets teams add a process for Announcement to a process model; expected outcome: I can support the announcement.
  - *Process description:* Product intent (NVE Process: Announcement): Creates an announcement process — Building blocks (3): Create new document, create email, register milestone — Default flow: 1: Create new document 2: Create e-mail 3: Create new document 4: Create new document 5: Create e-mail 6: Create new document 7: Create e-mail 8: Create new document 9: Create e-mail 10: Register or update date - milestone

### Parent 418785

- **Task** [419626](https://dev.azure.com/tieto-si/360/_workitems/edit/419626) — create process — *Active* (activity **2026-04-17**)

---

## Epic 414727 — PAF – User Experience (UX)

### Parent 414727

- **Feature** [420133](https://dev.azure.com/tieto-si/360/_workitems/edit/420133) — Make the display configurable in process overview — *New* (activity **2026-04-21**)
  - *What it does:* Lets teams configure which sections in the right-hand side menu in process overview that should be shown. For instance, I want to be able to toggle map on/off. Same with deficiencies, application etc.

---

## Epic 414328 — PAF – Standard Artifacts

### Parent 400794

- **User Story** [414618](https://dev.azure.com/tieto-si/360/_workitems/edit/414618) — Create document with review and approval — *Resolved* (activity **2026-04-07**)
  - *What it does:* Lets teams enabled automatic creation of a document through a stage defined process with options for subsequent review and approval of same document.
- **User Story** [414862](https://dev.azure.com/tieto-si/360/_workitems/edit/414862) — Process Withdrawn — *Resolved* (activity **2026-04-17**)
  - *What it does:* Lets teams trigger an "application withrawn" process at all places in the process.
- **Task** [419704](https://dev.azure.com/tieto-si/360/_workitems/edit/419704) — Global Custom Localization Tasks — *New* (activity **2026-04-20**)
- **Task** [419719](https://dev.azure.com/tieto-si/360/_workitems/edit/419719) — Global Standard Localization Used in processes — *New* (activity **2026-04-20**)

### Parent 414328

- **Feature** [400794](https://dev.azure.com/tieto-si/360/_workitems/edit/400794) — PAF - Artifacts - Process Definitions — *New* (activity ****)
- **Feature** [411623](https://dev.azure.com/tieto-si/360/_workitems/edit/411623) — PAF - Artifacts - Deadline Calculation Types — *New* (activity ****)
- **Feature** [414353](https://dev.azure.com/tieto-si/360/_workitems/edit/414353) — PAF - Artifacts - ProcessEngine - Designer Components — *Active* (activity ****)
- **Feature** [414516](https://dev.azure.com/tieto-si/360/_workitems/edit/414516) — PAF - Artifacts - Standard Milestones — *New* (activity ****)
- **Feature** [415996](https://dev.azure.com/tieto-si/360/_workitems/edit/415996) — PAF - Artifacts - Document Categories — *New* (activity ****)
- **Feature** [418321](https://dev.azure.com/tieto-si/360/_workitems/edit/418321) — PAF artifacts : create email — *New* (activity ****)

### Parent 414353

- **User Story** [414765](https://dev.azure.com/tieto-si/360/_workitems/edit/414765) — PE deigner create designer action for notification — *Active* (activity **2026-04-17**)
  - *What it does:* Lets teams invoke the creation of a notification to be sent. check P&B solution. They point to activity 39.
- **User Story** [420113](https://dev.azure.com/tieto-si/360/_workitems/edit/420113) — Add stage ID to createdocument designer component — *New* (activity **2026-04-21**)
  - *What it does:* Lets teams use the createdocument component and ensure that the document I create is connected to the correct stage, We need to extend the createdoument component to accept stage id in addition to case ID etc.

### Parent 415996

- **User Story** [415997](https://dev.azure.com/tieto-si/360/_workitems/edit/415997) — Add document categories — *Closed* (activity **2026-04-21**)

### Parent 415997

- **Task** [419086](https://dev.azure.com/tieto-si/360/_workitems/edit/419086) — Adding New Categories and Renaming few — *Closed* (activity **2026-04-17**)

### Parent 418321

- **User Story** [419167](https://dev.azure.com/tieto-si/360/_workitems/edit/419167) — new email dialogue — *New* (activity **2026-04-15**)
  - *What it does:* Lets teams create a nee email where it is possible to select attachments, recipients and other relevant values, so thai I can easily crete an email from a process without having to manually navigate around, Implement a dialogue with the current layout. Should load all case contacts and files on the case. Files should be listed from all attached douments on…

---

## Epic 411614 — PAF – Core Platform

### Parent 411614

- **Feature** [414600](https://dev.azure.com/tieto-si/360/_workitems/edit/414600) — PAF - Core Platform - Trigger Data Model and Automation Relationships — *New* (activity ****)
- **Feature** [417484](https://dev.azure.com/tieto-si/360/_workitems/edit/417484) — PAF - trigger milestone on document dispatch — *New* (activity ****)
- **Feature** [419789](https://dev.azure.com/tieto-si/360/_workitems/edit/419789) — PAF - BPMN modeler — *New* (activity **2026-04-20**)

### Parent 417484

- **User Story** [417485](https://dev.azure.com/tieto-si/360/_workitems/edit/417485) — Add document trigger on milestone config — *Active* (activity **2026-04-21**)
  - *What it does:* Lets teams specify which document types that trigger a milestones when dispatching or receiving a document; expected outcome: I can be sure milestones are triggered an updated automatically.
  - *Outcome / acceptance:* Given I have added a milestone to a process model, I am able to ad one or more documents and categories that should trigger the milestone.

### Parent 417485

- **Task** [419698](https://dev.azure.com/tieto-si/360/_workitems/edit/419698) — Document Category Changes — *Closed* (activity **2026-04-21**)

### Parent 419789

- **User Story** [419790](https://dev.azure.com/tieto-si/360/_workitems/edit/419790) — React - BPMN editor — *New* (activity **2026-04-20**)
- **User Story** [419791](https://dev.azure.com/tieto-si/360/_workitems/edit/419791) — BIF - Edit process using BPMN editor — *New* (activity **2026-04-20**)

---

## Bugs — `360\\Core-Process-platform` (from WIQL, last 14 days)

*Bug rows show Symptom / details from Description (overlay) when present; IDs already listed above are omitted.*

- **Bug** [362462](https://dev.azure.com/tieto-si/360/_workitems/edit/362462) — Manage participants - Contacts - Top Node department is not showing up in the list — *Active* (activity **2026-04-07**)
- **Bug** [411332](https://dev.azure.com/tieto-si/360/_workitems/edit/411332) — Process model both PNB and 360 - Not reached icon is not shown for the milestone when it is auto generated with case initialisation — *Active* (activity **2026-04-21**)
- **Bug** [412066](https://dev.azure.com/tieto-si/360/_workitems/edit/412066) — Process model - Previous milestone is shown in the add milestone dialog  when there is no milestone to add on a new stage — *Closed* (activity **2026-04-15**)
- **Bug** [413978](https://dev.azure.com/tieto-si/360/_workitems/edit/413978) — UI bugs on new admin pages — *Closed* (activity **2026-04-16**)
- **Bug** [416511](https://dev.azure.com/tieto-si/360/_workitems/edit/416511) — Adding a New Document Wizard on Xaml files, gives error on UI — *Closed* (activity **2026-04-20**)
- **Bug** [416629](https://dev.azure.com/tieto-si/360/_workitems/edit/416629) — Adding new workflow on a xaml file , gives error on UI — *Closed* (activity **2026-04-20**)
- **Bug** [417230](https://dev.azure.com/tieto-si/360/_workitems/edit/417230) — Milestone Automation ID should be unique message is not shown to user when given the same ID — *Resolved* (activity **2026-04-13**)
- **Bug** [418130](https://dev.azure.com/tieto-si/360/_workitems/edit/418130) — Dispatch template for the partial dispatch does not show the already processed document details — *New* (activity **2026-04-08**)
- **Bug** [418577](https://dev.azure.com/tieto-si/360/_workitems/edit/418577) — The views list in Process overview on case is not showing fields from the right column — *Rejected* (activity **2026-04-15**)
- **Bug** [418887](https://dev.azure.com/tieto-si/360/_workitems/edit/418887) — Missing standard milestone- Nor-"Trukket søknad" ENU-"Withdrawn application" — *New* (activity **2026-04-13**)
- **Bug** [418927](https://dev.azure.com/tieto-si/360/_workitems/edit/418927) — After the dispatch of the Receipt the process should be closed automatically — *New* (activity **2026-04-13**)
- **Bug** [418928](https://dev.azure.com/tieto-si/360/_workitems/edit/418928) — Document should be connected to stage entity and shown in the third column for the selected stage — *Active* (activity **2026-04-20**)
- **Bug** [418950](https://dev.azure.com/tieto-si/360/_workitems/edit/418950) — Work unit arguments tab is shown blank when created New version or copy of the Process model/stage templates — *Closed* (activity **2026-04-20**)
- **Bug** [419032](https://dev.azure.com/tieto-si/360/_workitems/edit/419032) — Document Creation dialogue: Stage value not loaded — *Resolved* (activity **2026-04-16**)
- **Bug** [419083](https://dev.azure.com/tieto-si/360/_workitems/edit/419083) — Uploading of some file formats after Rotation is not happening in the file viewer — *New* (activity **2026-04-14**)
- **Bug** [419093](https://dev.azure.com/tieto-si/360/_workitems/edit/419093) — Rotate and Redaction does not convert the file into Tiff and User is able to See the redacted text even if FT "FileViewerRedactionTiffMode" is ON — *New* (activity **2026-04-14**)
- **Bug** [419133](https://dev.azure.com/tieto-si/360/_workitems/edit/419133) — Milestones do not control time logging correctly on deadline calculation type "Calculate from Start/Finish milestones" — *New* (activity **2026-04-14**)
- **Bug** [419135](https://dev.azure.com/tieto-si/360/_workitems/edit/419135) — Milestone recno 201- "Tilleggsdokumentasjon etterspurt - vesentlig mangel" - description appears 2 times — *New* (activity **2026-04-14**)
- **Bug** [419288](https://dev.azure.com/tieto-si/360/_workitems/edit/419288) — Spelling mistake in Default document title — *Active* (activity **2026-04-20**)
- **Bug** [419306](https://dev.azure.com/tieto-si/360/_workitems/edit/419306) — Save button is shown on a published Process model and stage templates — *Closed* (activity **2026-04-20**)
- **Bug** [419308](https://dev.azure.com/tieto-si/360/_workitems/edit/419308) — Error message should be user friendly if user forgets creating the contact role while creating case with process model — *Active* (activity **2026-04-20**)
- **Bug** [419406](https://dev.azure.com/tieto-si/360/_workitems/edit/419406) — Dispatch dialogue should show Print as the  default option if Dispatch channel is selected as Print in work unit — *New* (activity **2026-04-16**)
- **Bug** [419435](https://dev.azure.com/tieto-si/360/_workitems/edit/419435) — Process is initiated even if it is marked as Upcoming — *New* (activity **2026-04-16**)
- **Bug** [419682](https://dev.azure.com/tieto-si/360/_workitems/edit/419682) — Writeoff of wait tasks doen not wait for registration — *New* (activity **2026-04-20**)
- **Bug** [419693](https://dev.azure.com/tieto-si/360/_workitems/edit/419693) — If IFAR Module is not installed then Ordering the reports from Advanced Search should not be possible — *New* (activity **2026-04-20**)
- **Bug** [419847](https://dev.azure.com/tieto-si/360/_workitems/edit/419847) — Using code table: YesNo in WU arguments does not work. — *New* (activity **2026-04-20**)
- **Bug** [419855](https://dev.azure.com/tieto-si/360/_workitems/edit/419855) — BIF - Progress plan connected directly to a case - client action will not be shown as Closed after execution — *New* (activity **2026-04-20**)
- **Bug** [420127](https://dev.azure.com/tieto-si/360/_workitems/edit/420127) — Adding WaitTask to "User: Document Flow - Wizard" creates an error — *New* (activity **2026-04-21**)

*Total in Bug WIQL batch: **28**; listed here after dedupe: **28**.*

---

_End of generated draft._