# DRAFT: 360° Flow — Module page (wiki)

**Status:** **Published** on wiki (rev **59679**, page id **7389**, 2026-06-02). Not linked from [[Module overview]] or other hub pages yet. Local file remains the working copy for edits.  
**Target page title:** `360° Flow`  
**Template basis:** [[Product information article template]] (rev 2026-06-01) + patterns from [[360° Process Engine]].  
**Content source (functional):** *Internal release presentation public 360 June (6.10).pptx* — slides 10–46 (local file).  
**Release / pilot:** [[6.10 release information#360° Flow (Pilot)]].  
**Related pages:** [[Process Framework]] (platform narrative), [[360° Process Engine]] (legacy programmable toolkit), [[Module overview]].  
**ADO:** #414623, #410938 · **Authors:** Tone Fjeller (PDM), Morten Jensen (PM)

---

## Pre-publish checklist (human)

| # | Item | Owner | Done |
|---|------|-------|------|
| 1 | Product number from MDM / Enablement | PM + Enablement | ☑ **P00285** (2026-09-16) |
| 2 | Register in ServiceNow per [[Establish new module/service]] | Enablement | ☐ |
| 3 | Add row on [[Module overview]] (likely **Modules not yet released** until GA) | PM | ☐ |
| 4 | Align naming with Process Framework draft (avoid duplicate positioning) | PM | ☐ |
| 5 | P&S approval for customer-facing claims | PM + P&S | ☐ |
| 6 | Product sheets / help.360online.com links when available | Enablement | ☑ ENG sheet **P00285** done locally (`360_Flow_Product_Sheet_ENG.pptx`); ☐ PDF on help.360online.com |
| 7 | Remove or resolve `TBD` markers in wikitext below | PM | ☐ |

---

## Complete wikitext (copy when approved)

```wikitext
<div style="border: 2px solid #c00; background: #ffe0e0; padding: 0.5em 1em; margin-bottom: 1em;">'''DRAFT''' – This page is under development and has not been approved for publication. Content may change. Functionality is in controlled pilot; licensing and packaging are not finalised.</div>

{| cellpadding="0" cellspacing="0" width="100%"
|-
| style="vertical-align:top" |
<div style="margin: 0 10px 0 0; border: 2px solid #0E76B7; padding: 0em 1em 1em 1em; background-color: #FFFDCA;">
==Key info==
Product number: '''P00285'''
{{Early release phase}}
* '''Part of:''' [[Public 360°]] · [[Process Framework]]
* '''Applies to version(s):''' '''Public 360° version 6.10 and newer'''
* '''Availability - Lead offering(s):''' [[Public 360°]] <!-- TBD: Business 360° if applicable -->
* '''Availability - Edition(s):''' <!-- TBD: Public cloud, domestic cloud, on-prem — confirm per Module_platform_support_overview -->
* '''Availability - Markets:''' '''Pilot markets only''' until GA — see commercial aspects
* '''Other requirements:''' Controlled pilot enablement (feature toggles and implementation-led activation); not a standalone BPM product
* '''Product Manager:''' Morten Jensen — see [[Product teams]]
* '''Product Development Manager:''' Tone Fjeller
* Page last updated: {{REVISIONYEAR}}-{{REVISIONMONTH}}-{{REVISIONDAY}}
</div>
<div style="margin: 0 10px 0 0; border: 2px solid #0E76B7; padding: 0em 1em 1em 1em; background-color: #FFFFFF;">

== Product information ==
{{PSNote}}

''360° Flow'' is a Public 360° module for '''process-oriented case processing'''. Work on a case is organised through a '''process model''' (template), '''case processing phases''', and the building blocks '''processes''', '''checklists''', and '''milestones''' — with status, deadlines, and reporting on the case.

Flow is part of the [[Process Framework]] on Public 360°. It is '''not''' a separate BPM product. For custom workunits and advanced programmable processes, see [[360° Process Engine]]. Former internal name: '''PAF''' (Process Automation Framework). Capabilities are introduced in the '''6.10 pilot''' (scope varies by tenant).

=== Conceptual model: how it fits together ===
A case can have one or more '''process models'''. Only one model can be '''active''' at a time. The model consists of '''phases''' that group activities and decision points / milestones.

The case processing flow:

{| class="wikitable"
! Step !! Description
|-
| '''Case processing model''' || The template for the case — defines structure from registration to completion
|-
| '''Case processing phase''' || Workspace for part of the case, with its own status
|-
| '''Work in the phase''' || Activities and control — tasks, checklists, and processes carried out here
|-
| '''Status and reporting''' || Deadlines and milestones — follow-up and reporting on the case
|}

'''Processes''' — tasks and activities that can be performed '''in parallel''' within a phase.

'''Checklists''' — checkpoints that can be '''standard''', '''organisation-specific''', or '''private''' (case-specific).

'''Milestones''' — clear steps that provide '''status''', '''deadline follow-up''', and '''reporting'''.

Several phases can be active on the same case when work does not proceed linearly. Files and maps relevant to the active phase are available in the phase workspace so users do not search the whole case for context.

Typical sequence on a case: link a process model → open the active phase → perform work (including parallel processes and checklists) → update status via milestones and activities → add phases or tasks when needed.

<!-- TBD: upload diagram from internal 6.10 deck (conceptual model slide) when approved for wiki -->

=== Process model — core components ===
The process model brings together five component areas. Each supports a defined operational outcome on the case.

==== 1. Process models and phases ====
'''Capability:''' Process models and phases with configurable templates.

* Link a process model to a case type; activate one model per case
* Phases structure the case; templates can be reused across similar case types
* Automation and notifications where configured (e.g. missing attachments, deadline notification)

'''Outcome:''' '''Efficiency''' — more automation, less manual work and follow-up.

==== 2. Checklists ====
'''Capability:''' Checklists with automatic follow-up where configured.

* Standard checklists by department or case type; organisation-specific checklists; private or ad hoc checklists on a case
* Checkpoint outcomes (e.g. Yes / No / Not relevant, Done / Not done)
* Filter checkpoints, manage deficiencies, see triggered tasks, automate checks when data is already verified

'''Outcome:''' '''Quality''' — better overview and fewer errors in case handling.

==== 3. Milestones and processes ====
'''Capability:''' Milestones and processes — clear steps, status, and parallel work.

* '''Processes''' — workflows within a phase; can be added per case; some repeatable, some single-run; parallel assignment to users
* '''Milestones''' — planned steps; status and dates when linked activities complete; next-step visibility; reporting (including public access / "My page" where configured); constraints per milestone type (e.g. one "Decision" per phase)

'''Outcome:''' '''Equal treatment''' — standardized processes per case type and application type.

==== 4. Deadline calculation ====
'''Capability:''' Flexible deadline logic per process model and case type.

* Deadline calculation on phases; automatic phase status for worklists and portfolios
* Milestones can set phase to '''On hold''' or '''Under processing'''; filtering in worklists reflects hold status while cases remain traceable

'''Outcome:''' '''Predictability''' — clear deadlines and better reporting on case processing time.

==== 5. Portfolio management ====
'''Capability:''' Portfolio views and process-oriented desktop (pilot / release scope varies).

* Worklists and portfolio overview use phase status, deadlines, and milestones
* Managers and teams can prioritise and follow up cases across the organisation

'''Outcome:''' '''Usability''' — easier navigation and better prioritisation on the portfolio.

<!-- TBD: upload "Process model - Core components" diagram from internal 6.10 deck when approved for wiki -->

=== Platform context ====
Flow is delivered through the [[Process Framework]] on Public 360° (standard structure with configurable processes). Related platform components:

{| class="wikitable"
! Component !! Role
|-
| '''Process models''' || Structure, phases, and milestones on the case
|-
| '''[[360° Process Engine]]''' || Programmable processes and workunits (legacy and advanced scenarios)
|-
| '''Business Rules Engine''' || Rules and deadlines in the process (availability varies by release)
|}

See [[Process Framework]] and [[Process Framework - Process models|Process Framework – Process models]] for more detail. Integrations (e.g. SIF, notifications, documents) use standard Public 360° mechanisms.

=== Scope and limitations (pilot) ====
* '''Controlled pilot''' on Public 360° 6.10 — not generally available; enablement is implementation-led
* Not all [[360° Process Engine]] scenarios are replaced in pilot
* Commercial packaging and self-service modeling for all customers are not finalised — see commercial aspects
* Not a standalone BPM SKU

=== What's new in which version ====
'''Version 6.10 (pilot)''':<BR>
* 360° Flow in controlled pilot — process-oriented case workspace, phases, checklists, processes, and milestones (scope varies by tenant)
* Licensing, packaging, and customer-facing product documentation not finalised
Read more: [[6.10 release information#360° Flow (Pilot)]]

<!-- TBD: Add GA version blocks when generally available -->

=== Commercial aspects ===
360° Flow is offered as part of the [[Process Framework]] on Public 360°. Packaging, process entitlement, and list prices are maintained by Enablement and are '''not finalised during pilot'''. Do not use this page alone for customer quotes until the GA catalogue is published.

{{Price model in 360°}}

[[360° Hosted Processes]] (when released) is documented separately. [[360° Process Engine]] pricing may still apply for some deployments until transition is agreed.

Implementation is delivered through standard project and consultancy engagement (see Implementation guidelines when published).

=== Product documentation ===
Below, please find documentation developed and maintained by Enablement.

==== Product sheets ====
{| class="wikitable"
| DAN
| ENG
| FIN
| NOR
| SWE
|}
<!-- TBD: help.360online.com product sheet URLs when published -->

==== End-user documentation ====
{| class="wikitable"
| DAN
| ENG
| FIN
| NOR
| SWE
|}
<!-- TBD: help.360online.com administrator / user topics when GA -->

==== Additional material ====
* [[6.10 release information#360° Flow (Pilot)|6.10 release information — 360° Flow (Pilot)]]
* [[Process Framework]] — platform narrative, consumption models, and component map
* [[Product training sessions]]
* Internal pilot training manuscript (Flow introduction) — link TBD when published on wiki
* Hotfixes and known issues: For hotfixes on the latest release, see [[Release Information]]. All hotfixes are published on {{360° Setups and Hotfixes}}.

| width="40%" style="vertical-align:top" |

<div style="margin: 0 10px 0 0; border: 2px solid #0E76B7; padding: 0em 1em 1em 1em; background-color: #E5F6FE;">

== Documentation from other units ==
Quality assurance relies on the individual departments owning the material.

=== Value proposition / Selling points ===
''360° Flow'' organises case work through a process model on the case. The five component areas above translate into:

* '''Efficiency''' — process models and phases with templates; automation where configured; less manual work
* '''Quality''' — checklists with follow-up; better overview; fewer errors
* '''Equal treatment''' — milestones and processes; standardized steps and parallel work per case type
* '''Predictability''' — deadline calculation per model; clear deadlines and reporting
* '''Usability''' — portfolio management and worklists; easier navigation and prioritisation

Caseworkers work in phase context (tasks, checklists, files, maps). Managers use status, deadlines, and portfolio views. See [[Process Framework]] for packaging and expansion on the platform.

=== Implementation guidelines ===
(When applicable. Implementation guidelines for Flow and process models to be added by Consultancy SPOC. See [[Implementation guidelines - template]].)

=== Installation / deployment / technical ====
<!-- TBD: help.360online.com technical PDFs when published -->
* Process models: [[Process Framework - Process models|Process Framework – Process models]]
* Process Engine (legacy / custom development): [[Process Engine|Process Engine (CIE landing page)]] · [[360° Process Engine]]

=== Service descriptions ====
Service Descriptions can be found in 360° on [https://si.business360online.com/locator/CRM/Project/Details/Simplified/1?recno=201981&module=Project&subtype=1&VerID= project 12-356]. Look under "Service Descriptions - Modules". We recommend navigating in the project via the "Treeview".

The Service Descriptions in 360° are currently being updated.

New documents and updates will be published in English.

=== Training material ====
<!-- TBD: CIE wiki subtree when published — mirror [[Process Engine]] pattern -->
* For caseworkers, managers, and super users: process model, phase, process, milestone, and checklist concepts — contact Product Manager

=== Demo setup (pilot) ===
Internal instructions for preparing a pilot/demo tenant and running the standard '''application with right of appeal''' scenario. The page describes toggles, import files (process models, checklists, templates), and a suggested demo story.

'''[[360° Flow - Demo setup|Go to demo setup]]'''

=== Nice to know ===
* Flow pilot content is also summarised under '''Coming soon (Ongoing Pilots)''' on current release information pages until GA
* [[360° Hosted Processes]] (when released) is a separate commercial line — standardised Tieto-maintained processes on subscription; upgrade path to configurable Flow is separate
* External customer-facing release notes may exclude Flow until P&S approves GA messaging

=== Known limitations (pilot) ===
* '''Not generally available''' — controlled pilot only; capabilities vary by tenant and template
* Some capabilities still under development or being refined
* Licensing, pricing, and catalogue SKUs not finalised — do not use this page for customer quotes
* Not all [[360° Process Engine]] investments or custom workunits are superseded by Flow in pilot
* Self-service process modeling for all customers is not in pilot scope — implementation-led activation
* Feature toggles and settings must be validated per environment before go-live

</div>

|}

__NOTOC__
[[Category: Product information]]
[[Category:360°]]
[[Category:Draft]]
```

---

## Summary of draft choices

### Structure (module catalogue)
- **Central narrative:** `=== Conceptual model: how it fits together ===` (deck conceptual-model slide) — model → phase → work → status/reporting; definitions of processes, checklists, milestones.
- **Core components:** `=== Process model — core components ===` — five areas from deck slide 36, each with capability + outcome (Efficiency, Quality, Equal treatment, Predictability, Usability).
- **Value proposition (right column):** mirrors the five outcomes; no duplicate marketing blocks in the left column.
- **Platform context, pilot scope, What's new, commercial, docs:** unchanged pattern vs other module pages.
- **TBD:** upload deck diagrams (conceptual model + core components) when approved for wiki.

### Published
- Wiki: [360° Flow](https://wiki.software-innovation.com/wiki/360%C2%B0_Flow) (rev 59679). No inbound links from Module overview etc. yet.

---

## Review decisions (confirmed)

| Topic | Decision |
|-------|----------|
| Page title | **`360° Flow`** |
| Product Manager | **Morten Jensen** |
| Product Development Manager | **Tone Fjeller** |
| Version floor | **Public 360° 6.10 and newer** |
| DRAFT treatment | Keep red **DRAFT** banner and `[[Category:Draft]]` until explicitly approved for publication |

After further edits, say when to apply to the wiki (preview via MCP with `preview=true` first).
