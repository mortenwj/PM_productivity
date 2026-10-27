# DRAFT: 360° Flow — Demo setup (wiki)

**Status:** Ready to publish to [360° Flow - Demo setup](https://wiki.software-innovation.com/wiki/360%C2%B0_Flow_-_Demo_setup) (page id **7396**). Process models **6.12-aligned** (registry `ms_6.12.0`, model version **9**); re-upload **process models** ZIP when publishing.  
**Wiki title:** `360° Flow - Demo setup`  
**Source:** `projects/process-platform/flow/manuscripts/Demo setup/` + `FLow setup instructions.md`  
**Presenter script (repo):** `manuscripts/Demo setup/360_Flow_Standard_Demo_MANUSCRIPT.md`

---

## Complete wikitext (copy when approved)

```wikitext
<div style="border: 2px solid #c00; background: #ffe0e0; padding: 0.5em 1em; margin-bottom: 1em;">'''Internal enablement — standard demo scenario.''' Maintained demo assets for presales, consultants, and product; not a turnkey production package for customer tenants without implementation review. Tenant URLs and toggles may change.</div>

This page describes how to prepare a '''demo tenant''' and run the standard '''360° Flow''' demo: '''application processing with right of appeal''' (NVE-style scenario).

Product context: [[360° Flow]] (P00285). GA from Public 360° '''6.12''' — see [[6.12 release information#360° Flow - Now Generally Available|360° Flow in 6.12 release information]]. Process model concepts: [[Process Framework - Process models|Process Framework – Process models]].

For a full '''presenter script''' (timing, fallbacks, audience variants), use the demo manuscript in the product documentation repository: '''360_Flow_Standard_Demo_MANUSCRIPT.md''' (Demo setup folder).

== Purpose ==

* Prepare a test tenant with the correct feature toggles, settings, and imported templates
* Run a repeatable demo of process-oriented case handling (process model, phases, checklists, processes, milestones) in '''ProcessView'''
* Give presales, consultants, and product the same baseline scenario and asset bundle

== Prerequisites ==

* Public 360° '''6.12 or newer''' (360° Online, domestic cloud, or local installation) with '''360° Flow''' enabled for the tenant
* '''Older builds (e.g. 6.10 pilot):''' do not use the current process model ZIP — email steps require the 6.12 work unit layout
* Administrator access to the demo tenant (examples below use Danish test cloud URLs; adjust host for your tenant)
* Process model import/export and checklist import available in the tenant
* Demo asset files — see '''Import assets''' below
* Use '''one language''' per demo session: matching process model, checklist, and document templates

== Demo asset version (6.12) ==

{| class="wikitable"
! Item !! Value
|-
| '''Bundle''' || 2026-10 refresh (process models v9; checklists unchanged; document templates unchanged)
|-
| '''Process model export version''' || 9 (English master; DA/NO/SV/FI generated from same structure)
|-
| '''Work unit registry''' || Aligned to '''ms_6.12.0''' (consolidated stage process arguments — validate after platform upgrade)
|-
| '''Email steps''' || Optional '''Email message template''' on send-mail activities; demo ships with template unset ('''#null#''')
|}

After importing process models: '''publish''' the version used on cases. After replacing assets on an existing tenant, prefer '''new cases''' for verification — in-flight activities may retain old workflow arguments.

== Environment setup ==

Standard setup for the '''application with right of appeal''' demo. Perform steps in order.

# Activate feature toggles '''NVE''' and '''ProcessModelImportExportEnabling'''
# '''Disable''' feature toggle '''FFUI.CaseCreation'''
# Activate feature toggle '''EnableChecklistsP360''' (if not already enabled on the tenant)
# Activate checklists in settings: [checklist.updatechecklist](https://test-dan.public360online.com/locator/Admin/Setting/Details?Id=checklist.updatechecklist) (adjust host for your tenant)
# '''Import process model''' (see Import assets — '''publish''' after import if required by your tenant)
# '''Import checklist''' and '''connect it to each process model phase (stage)''' — see [[#Import checklist and connect to phases|Import checklist and connect to phases]]
# '''Activate document categories''' required for milestones and templates — see [[#Activate document categories|Activate document categories]]
# '''Import document templates''' for '''Major Deficiency letter''' and '''Decision letter''' (see Import assets — document templates)
# '''Validate email configuration (6.12):''' in Process Model Admin, open stage processes '''Application received''' and '''Review application''' — under '''create email1''', confirm '''Email message template''' can be left empty / none (demo uses '''#null#''' in export)

=== Activate document categories ===

The v9 process model registers '''milestones''' when incoming or outgoing documents use specific '''document categories'''. Categories that ship '''expired''' or inactive in the tenant must be '''activated''' in '''Code table editor → Document category''' (edit the row and set status to active; use the language column that matches your demo UI).

Activate at least the categories below before running the demo on '''new cases'''. Recnos are stable in product seed data; labels differ by language — search by ID or by the name in your demo language.

{| class="wikitable"
! Recno !! Name (ENU) !! Example (NOR) !! Role in demo
|-
| 434 || '''Additional information — significant deficiency''' || Tilleggsinformasjon — vesentlig mangel || '''Incoming''' supplementary documentation → '''Additional documentation received''' milestone (type 203)
|-
| 433 || '''Additional information — minor deficiency''' || Tilleggsinformasjon — mindre mangel || Same milestone (use when demoing the minor supplementary path)
|-
| — || '''Major Deficiency letter''' || (demo template category name) || Outgoing '''Significant deficiency''' letter wizard; import matching document template after activation
|-
| 99002 || '''Decision letter''' || Vedtak || '''Decision made''' wizard (outgoing); import decision letter template after activation
|-
| 99024 || '''Klage''' || Klage || '''Incoming''' appeal document → '''Appeal received''' milestone (phase 2)
|}

If a milestone does not fire after document registration, confirm the registered document used one of these categories (not a look-alike label) and that the category is active — see [[#Troubleshooting|Troubleshooting]].

== Import assets ==

Demo files are attached on this wiki as ZIP packages (the wiki does not allow direct <code>.json</code> / <code>.dotm</code> uploads). '''Download → extract → import''' in the tenant.

=== Download files ===

* [[File:360 Flow demo - process models.zip|'''Process models''' (English, Danish, Norwegian, Swedish, Finnish)]]
* [[File:360 Flow demo - checklists.zip|'''Checklists''' (English, Danish, Norwegian, Swedish, Finnish)]]
* [[File:360 Flow demo - document templates.zip|'''Document templates''' (Major Deficiency letter and Decision letter, all languages)]]

{| class="wikitable"
! ZIP package !! Folder inside ZIP !! Import in tenant
|-
| [[File:360 Flow demo - process models.zip|Process models]] || <code>process-models/</code> || Process Model Management → import JSON → publish if required
|-
| [[File:360 Flow demo - checklists.zip|Checklists]] || <code>checklists/</code> || [[#Import checklist and connect to phases|Import checklist and connect to phases]] (match language to demo)
|-
| [[File:360 Flow demo - document templates.zip|Document templates]] || <code>document-templates/</code> || Template import after '''Major Deficiency letter''' and '''Decision letter''' categories are active
|}

Canonical copies are maintained in the product documentation repository under '''Demo setup''' (<code>projects/process-platform/flow/manuscripts/Demo setup/</code>).

=== Process model ===

{| class="wikitable"
! Language !! File name !! Process model title
|-
| English || <code>Handle application with right of appeal (English).json</code> || Process application with right of appeal
|-
| Danish || <code>Behandle ansøgning m. klageret (Danish).json</code> || Behandle ansøgning m. klageret
|-
| Norwegian || <code>Behandle søknad m_klagerett.json</code> || Behandle søknad m/klagerett
|-
| Swedish || <code>Behandla ansökan med överklaganderätt (Swedish).json</code> || Behandla ansökan med överklaganderätt
|-
| Finnish || <code>Käsittele hakemus valitusoikeudella (Finnish).json</code> || Käsittele hakemus valitusoikeudella
|}

Use '''one''' language per demo session, aligned with the checklist and template language.

=== Checklists ===

{| class="wikitable"
! Language !! File name !! Checklist name
|-
| English || <code>Checklist for application processing with right of appeal (English).json</code> || Checklist for application processing with right of appeal
|-
| Danish || <code>Tjekliste for ansøgningsbehandling med klageret (Danish).json</code> || Tjekliste for ansøgningsbehandling med klageret
|-
| Norwegian || <code>Sjekkliste_for_søknadsbehandling_med_klagerett_fcba25b7-4d74-49ba-92c0-a03909c51d02.json</code> || Sjekkliste for søknadsbehandling med klagerett
|-
| Swedish || <code>Checklista för ansökningsbehandling med överklaganderätt (Swedish).json</code> || Checklista för ansökningsbehandling med överklaganderätt
|-
| Finnish || <code>Tarkistuslista hakemuksen käsittelyyn valitusoikeudella (Finnish).json</code> || Tarkistuslista hakemuksen käsittelyyn valitusoikeudella
|}

'''Note:''' English checklist checkpoint '''22''' title may be corrected in a follow-up bundle (copy-edit — merged section heading in current export). Appeal proof points remain items '''20–21'''.

=== Import checklist and connect to phases ===

The demo checklist JSON contains all '''checkpoints''' and '''milestone tags''', but the bundled process model export does '''not''' attach a checklist to each '''phase (stage)'''. After import you must link the checklist in '''Process Model Management''' so it appears in '''ProcessView''' on cases using that model.

'''Recommended order:''' import and '''publish''' the process model first, then import the checklist, then attach the checklist to '''both''' phases and save/publish the model again.

==== 1. Import the checklist definition ====

# Confirm '''EnableChecklistsP360''' and setting [checklist.updatechecklist](https://test-dan.public360online.com/locator/Admin/Setting/Details?Id=checklist.updatechecklist) are active (adjust host for your tenant).
# Open '''Checklist Library''' in the client (route: <code>/locator/DMS/ProcessSupport/ChecklistLibrary</code> — typically under '''DMS''' → '''Process support''' → '''Checklist library''').
# Select '''Import''' (shown when your user has checklist update rights per the setting above).
# Choose the JSON file from the extracted ZIP folder <code>checklists/</code> that matches your demo language (see table above).
# Confirm the checklist appears in the library with the expected name (e.g. ''Checklist for application processing with right of appeal'').

'''Optional — review after import:'''

* '''Edit''' the checklist → '''Details''': confirm '''case types''' (demo export uses '''all case types''') and '''scope''' are suitable for your tenant.
* '''Checkpoints''' tab: each item may have a '''milestone type''' tag. Tags are stored as codetable recnos from the export environment. On a '''new''' tenant, open a checkpoint and verify the milestone name still matches your process model (e.g. ''Application received'', ''Decision made'', ''Case processing completed''). Re-select the milestone type if the tag is missing or wrong — otherwise ProcessView may not group checkpoints correctly as milestones are reached.

==== 2. Connect the checklist to each phase (stage) ====

# Open '''Process Model Management''' (<code>/locator/Admin/ProcessManagement/ProcessModels</code>).
# Open the demo process model (same language as the checklist). Use an editable '''draft''' version; if only a published version exists, create a new draft/version before changing stages.
# In the model tree, select '''Phase 1''' — ''Process application with right of appeal'' (localized title on DA/NO/SV/FI tenants).
# Open '''Properties''' for that stage.
# In '''Checklist template''' (attach a checklist relevant to this stage), select the imported checklist (same name as in the library table).
# If your tenant shows '''Application type''' on stage properties (Plan & Build–style configuration), select the '''same application type''' you use on demo cases for that phase. Leave unset only if your demo cases do not use application type filtering.
# Repeat for '''Phase 2''' — ''Appeal processing'' (or localized equivalent): same '''Checklist template''' (one definition serves both phases; checkpoint milestone tags control which items apply when).
# '''Save''' the process model and '''publish''' the version used on cases.

==== 3. Verify on a case ====

# Create or open a case whose '''case type''' is included on the process model (demo export is scoped to '''Journal case''' on the source tenant — map to the equivalent case type on your tenant when linking the model).
# Link the '''published''' process model to the case (case wizard or case properties).
# Open the active case processing phase in '''ProcessView''': the checklist panel should list checkpoint groups as milestones are registered. If the checklist is empty, re-check stage '''Checklist template''', case type scope, and the checklist setting.

'''How stages and checkpoints relate:''' Phases in the process model are '''stages'''. The checklist is attached '''per stage''', not per individual process (Application received, Review application, etc.). Checkpoints tagged with a '''milestone type''' become relevant when that milestone exists on the case — aligned with the milestone list under '''Process model: what happens''' below.

=== Document templates (Major Deficiency letter) ===

Word macro-enabled templates (``.dotm``). Same Grow Business / 360° document logic in all languages; only visible labels and body text differ. Rebuild with <code>Build-TranslatedTemplates.ps1</code> in the Demo setup folder if the Norwegian master changes.

{| class="wikitable"
! Language !! File name
|-
| Norwegian || <code>prosess_mangelbrev.dotm</code>
|-
| English || <code>process_deficiency_letter.dotm</code>
|-
| Danish || <code>proces_mangelbrev.dotm</code>
|-
| Swedish || <code>process_bristbrev.dotm</code>
|-
| Finnish || <code>prosessi_puutekirje.dotm</code>
|}

Import after document category '''Major Deficiency letter''' is active. Use the template that matches the demo language (process model + checklist).

=== Document templates (Decision letter) ===

Used in the '''Decision made''' process (document wizard: category '''Decision letter''', review and approval before dispatch). Rebuild with <code>Build-TranslatedVedtakTemplates.ps1</code> from Norwegian master <code>Prosess_vedtak.dotm</code>.

{| class="wikitable"
! Language !! File name
|-
| Norwegian || <code>prosess_vedtak.dotm</code>
|-
| English || <code>process_decision.dotm</code>
|-
| Danish || <code>proces_vedtagelse.dotm</code>
|-
| Swedish || <code>process_beslut.dotm</code>
|-
| Finnish || <code>prosessi_paatos.dotm</code>
|}

Import after document category '''Decision letter''' is active. Use the template that matches the demo language.

== Understanding the demo scenario ==

Scenario narrative below uses '''English labels'''; the same story applies in all localized process models. Use this section when explaining '''what the process does''' and '''how the checklist supports it''' — not only which buttons to click.

=== What you are demonstrating (value) ===

* '''One process model on the case''' drives the case officer through a regulated timeline (28 days for main processing, plus appeal stage), with '''milestones''' that anchor deadlines and reporting
* '''Parallel processes''' inside the active phase (receipt, review, deficiency letters, decision, close) show structured work without losing overview
* '''Automated and guided steps''' (receipt dispatch, document wizards, e-mail with optional message template in 6.12, subprocess for major deficiency with reminders) show efficiency and predictability
* The '''checklist''' is the quality and compliance layer: same case, same application type — checkpoints tagged to milestones so officers know what “done” means at each stage
* '''Right of appeal''' is explicit in the checklist (items 20–21) and in the model (appeal deadline milestone, second phase for appeal processing)

=== Process model: what happens ===

'''Model:''' ''Process application with right of appeal'' — two '''phases (stages)'''.

==== Phase 1 — Process application with right of appeal (28-day phase deadline) ====

Processes appear in the active case processing phase (several can run in parallel; typical story order below):

{| class="wikitable"
! Order !! Process !! What the case officer experiences !! Milestone / output
|-
| 1 || '''Automatic confirmation of received application''' || System-generated receipt to applicant (6.12: no preset template, dispatch off by default in demo export) || —
|-
| 2 || '''Application received''' || Register receipt date; letter and e-mail to applicant; milestone '''Application received''' || Application received
|-
| 3 || '''Review application''' || Assess completeness; e-mail for '''minor''' deficiency; can spawn subprocess for '''major''' deficiency; register '''Application complete''' when file is ready || Application complete; minor-deficiency milestone when used
|-
| 4 || '''Request for additional documentation — Significant deficiency''' || '''Major Deficiency letter''' (demo template); approval + dispatch; waiting period with '''reminder''' and '''final warning''' if response is late || Additional documentation requested — significant deficiency
|-
| 5 || '''Decision made''' || Decision letter with '''review and approval''' before dispatch || Decision made
|-
| 6 || '''Close case processing''' || Checkpoint task to confirm checklist; closure correspondence to applicant || Case processing completed
|}

'''Milestones configured in this phase''' (drive deadlines and checklist alignment):

* '''Application received''' — start of formal processing time
* '''Additional information requested — significant deficiency''' — triggered when outgoing '''Deficiency letter — significant deficiency''' (438) is registered
* '''Additional information requested — minor deficiency''' — triggered when outgoing '''Deficiency letter — minor deficiency''' (437) is registered (e-mail / letter path in demo)
* '''Additional documentation received''' (milestone type 203) — triggered when incoming documents use '''Additional information — minor''' or '''significant deficiency''' categories (433 / 434); recalculates processing time
* '''Application complete''' — case file ready for decision
* '''Decision made''' — decision issued (linked to 21-day '''Appeal deadline''' milestone in the model)
* '''Case processing completed''' — administrative closure

==== Phase 2 — Appeal processing (56-day phase deadline) ====

If the citizen appeals, a second phase opens with at least:

* '''Appeal received''' milestone — triggered when an incoming document uses category '''Klage''' (demo recno 99024)
* '''Application received''' (appeal) process — letter '''Appeal received''' to acknowledge the appeal

(Remaining appeal steps are not fully expanded in the export; treat phase 2 as “appeal intake” in a short demo.)

=== Checklist: how it supports the process ===

'''Checklist:''' ''Checklist for application processing with right of appeal'' — scoped to the same '''application type''' as the process model. It does not replace processes; it defines '''what must be true''' before milestones and decisions hold up in audit.

Checkpoints are grouped by '''milestone tag''' (when present):

{| class="wikitable"
! Phase of work !! Milestone tag (examples) !! Checklist focus !! Tie-in to processes
|-
| '''Intake & registration''' || Application received (items 1–6) || Received in correct system, dated, applicant identified, power of attorney, mandatory fields, attachments || Completed while running '''Application received''' / early '''Review application'''; failures on 4–6 support '''deficiency''' paths
|-
| '''Case preparation''' || Application complete phase (items 8–13); item 7 untagged || Missing info requested, statements, facts, impartiality, GDPR, data minimisation || '''Review application''', e-mails, major/minor deficiency processes; item 7 = sufficient case file before decision
|-
| '''Decision & appeal information''' || Decision made (items 14–22, 26) || Legal basis, reasoning, conditions (with sub-checkpoints), QA, dispatch, appeal text and deadline, access rights || '''Decision made''' process; items 20–21 are the “right of appeal” proof points for demos
|-
| '''Archiving & follow-up''' || Case processing completed (items 23–25) || Registration, archive, follow-up deadlines || '''Close case processing'''; checkpoint to verify checklist completion
|}

Several checkpoints define '''outcomes when answered “no”''' (e.g. missing power of attorney, missing documentation) — use in demo to show how checklist findings justify starting a '''deficiency''' process and the '''Major Deficiency letter''' template.

=== Inner workings — one sentence per concept ===

* '''Phase''' — time-bounded chapter of the case (main processing vs appeal)
* '''Process''' — packaged work (documents, e-mail, subprocess, milestone update) the officer starts or that auto-starts
* '''Milestone''' — dated event on the case; recalculates deadlines and marks checklist progress
* '''Checklist''' — controlled list of requirements; milestone tags show which apply when
* '''Major deficiency process''' — structured request + wait + reminders; first automated reminder uses '''Deficiency letter — significant deficiency''' category (438); connects to deficiency ''.dotm'' template
* '''Decision made''' process — decision letter with appeal information; connects to decision ''.dotm'' template
* '''Create email (6.12)''' — send-mail step with optional '''email message template''' preset; demo leaves template unset ('''#null#''')

=== Suggested talking points for demos ===

# “The model is the '''railway track''' — processes and milestones move the case forward.”
# “The checklist is the '''inspector''' — same case, tells us if the file is legally and administratively sound at each station.”
# Show '''Application received''' process + checklist items 1–3
# Show a failed checkpoint (e.g. power of attorney) → '''Review''' / '''Significant deficiency''' process → Major Deficiency letter
# Show '''Decision made''' + checklist items 20–21 (appeal information)
# End with '''Close case processing''' and checklist verification task

== Demo walkthrough ==

Suggested '''story''' after setup. Maps to the [[360° Flow#Conceptual model: how it fits together|conceptual model]] on the module page. For timed beats and fallbacks, see '''360_Flow_Standard_Demo_MANUSCRIPT.md''' in the repository.

=== Full walkthrough (~45 min) ===

# '''Create or open a case''' — link the imported process model (case wizard or case properties). Confirm one active model on the case
# '''Open the active case processing phase''' — show tasks, checklist, and milestones in '''ProcessView'''
# '''Application received''' — run process; complete checklist items 1–6; set milestone
# '''Review application''' — minor deficiency e-mail or spawn '''Significant deficiency''' + Major Deficiency letter
# '''Checklist''' — show milestone-tagged groups (preparation, decision, archiving)
# '''Decision made''' — '''Decision letter''' document template (<code>process_decision.dotm</code> / language variant); review + approval; checklist items 14–21 (appeal information)
# '''Close case processing''' — verify checklist completion; closure letter
# '''Milestone''' — appeal deadline / phase 2 only if time allows
# '''Manager view''' (if in scope) — worklist or portfolio filtered by phase status / deadlines
# '''Optional''' — files and maps in phase context; notification or automation step if enabled in tenant

=== Short walkthrough (~20 min) ===

Skip major deficiency subprocess and phase 2: '''Automatic confirmation''' → '''Application received''' → '''Review application''' (minor e-mail only) → '''Decision made''' → optional '''Close'''.

Scope and licensing: [[360° Flow]] and [[6.12 release information#360° Flow - Now Generally Available|6.12 release information — 360° Flow]].

== Troubleshooting ==

{| class="wikitable"
! Issue !! Check
|-
| <code>Missing arguments (EmailMessageTemplateRecno1)</code> || Re-import '''6.12-aligned''' process model ZIP; ensure send-mail args include template '''#null#''' (not blank); '''publish''' model; use a '''new case''' (old activities may keep stale arguments)
|-
| E-mail step fails after asset upgrade || Same as above; do not resume pre-upgrade process instances
|-
| Process model import fails || Toggles '''NVE''' and '''ProcessModelImportExportEnabling'''; tenant on '''6.12+'''; export format / model version
|-
| Checklist not visible || Setting [checklist.updatechecklist](https://test-dan.public360online.com/locator/Admin/Setting/Details?Id=checklist.updatechecklist); '''Checklist template''' set on '''both''' process model phases ([[#Import checklist and connect to phases|Import checklist and connect to phases]]); case type on model matches case; checkpoint milestone tags valid on tenant
|-
| Case creation UI unexpected || '''FFUI.CaseCreation''' should be '''disabled''' for this demo setup
|-
| New case type not using Flow || Process model published and linked; correct case type / application type mapping
|-
| Process runs but wrong language || Process model, checklist, and ''.dotm'' templates must match the demo language
|-
| Milestone not reached when document registered || Confirm document '''category''' matches demo export (e.g. incoming supplementary info 433/434, appeal '''Klage''' 99024, minor request letter 437); re-import v9 process model and use a '''new case'''
|-
| '''Process arguments''' tab empty on '''Stage-Defined Process''' (e.g. '''Final processing''' / work unit '''E1A5B6C7…''' on '''Application received''', '''Review application''', '''Close case processing''') || This is expected process type '''Stage-Defined Process''' (not globally defined). The admin UI loads arguments from the '''saved''' '''WorkUnitArguments''' XML on that stage process row — '''not''' from the demo JSON or work unit registry file. An empty tab usually means that XML was never persisted (import/save gap), not that the work unit is missing. Re-selecting '''Workflow definition''' loads the registry default schema (fields appear) but '''Save''' writes merged defaults and can '''wipe demo-prefilled metadata''' (templates, categories, e-mail settings) unless you re-enter them — avoid that workaround on a tuned tenant. '''Verify:''' export the tenant process model and check '''WorkunitArguments''' on the affected rows against the v9 demo ZIP. '''Mitigation:''' re-import into an unpublished model version, or restore argument XML from the demo export then save PMC once; validate '''Review application''' (minor deficiency e-mail) on a '''new case'''

== Page governance ==

* '''Maintainers:''' Product (Flow) — update when demo assets, work unit registry, or toggle names change; republish wiki ZIPs when process model version or checklist content changes
* '''Canonical source:''' product documentation repository, '''Demo setup''' folder
* '''Feedback:''' Product Manager / Product Development Manager on [[360° Flow]]
* '''Discovery:''' linked from [[360° Flow]] '''Additional material'''

__NOTOC__
[[Category:360°]]
```

---

## After publish

- **2026-10-01:** Wiki rev **61610** (v9 assets + copy); process models ZIP re-uploaded. Republish via `Publish-WikiDemoSetupPage.ps1` + `Upload-DemoAssetsToWiki.ps1` after future asset changes.
- Duplicate title `360Â° Flow - Demo setup` (page id 7400) → **#REDIRECT** to canonical [[360° Flow - Demo setup]] (rev 61608).
