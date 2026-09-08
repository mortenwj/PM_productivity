# ADO #400794 — Process Definitions (evidence summary)

**Feature:** [PAF - Artifacts - Process Definitions](https://dev.azure.com/tieto-si/360/_workitems/edit/400794)  
**Parent epic:** [#414328 PAF - Standard Artifacts](https://dev.azure.com/tieto-si/360/_workitems/edit/414328)  
**Area:** Core-Process-platform | **State:** Active  
**Assigned:** Bjørn Kristiansen | **Created:** Tone Fjeller (Dec 2025)

## What this feature is

Reusable **process definitions** stored in the PAF artifact repository — executable workflow logic (WWF/XAML today) referenced by stages/process models. Includes a **standard process library** customers can clone, customize (activities + argument rules), and save.

**User persona in attachments:** *Prosessansvarlig* / Process Owner — aligns with customer **process builder**, not implementation consultant.

## v0 prototype (linked in ADO description)

- **Chat/build URL:** https://v0.app/chat/process-arguments-design-bMgrPOiYsjh?ref=Z52ANW  
- **Note:** Requires v0 login; not publicly previewable from outside Tone's account unless published/deployed.

## Attachments (extracted)

| File | Path |
|------|------|
| Norwegian user story (full) | `NOR_Prosess_bibliotek_US_til_utvikling.txt` |
| English summary (partial) | `Process_Description_English.txt` |

### Core user story (from Norwegian attachment)

> As process owner, customize and manage a standardized process template with activities, tasks, client/server actions, and **argument-driven rules**.

**Capabilities:**
- Retrieve, activate, or **clone** standard templates (Mottak, Saksbehandling, Vedtak, Sluttbehandling)
- Edit metadata (name, status draft/active/inactive, description)
- Edit activities and argument logic
- Save as new process, modified process, or new template (role-gated)

**Activity types (US scope):**
- Document (type, category, milestone, roles, review/approval, templates)
- Register received date / generic dates
- Send task to role/person
- Meeting/appointment
- Open URL
- *(Future: server actions, client actions)*

**Argument model:**
- Per-activity conditions: field + operator + value → include activity
- Evaluated at process instantiation on a case

## Child work items (32) — grouped

### Standard stage processes (library seeds)
| ID | Title | State |
|----|-------|-------|
| 391652 | Mottak / Received | New |
| 391653 | Saksbehandling | New |
| 391656 | Vedtak | New |
| 391657 | Sluttbehandling | New |

### NVE / shipped standard processes (implementation)
| ID | Title | State |
|----|-------|-------|
| 414030 | Major deficiency letter | Closed |
| 414452 | Autoreceipt | Closed |
| 414618 | Create document with review and approval | Closed |
| 414621 | Minor Deficiency letter | New |
| 414862 | Process Withdrawn | Closed |
| 414983 | Minor deficiency - write notification | Closed |
| 416287 | Open URL with arguments | Active |
| 416932 | Create process task | Closed |
| 418107 | Reject application | Active |
| 434348 | Auto-receipt stage + background | Closed |

### Platform / toolkit
| ID | Title | State |
|----|-------|-------|
| 414799 | Application Master example in PEToolkit | Closed |
| 416108 | Invoke subprocess as server action | Closed |
| 405446 | Automation on application received | New |

### Related feature
| ID | Title |
|----|-------|
| 414386 | PAF - Artifacts - HOW TO |

## Alignment with Process Builder (this project)

| ADO #400794 | Your Process Builder direction |
|-------------|-------------------------------|
| Process library + clone/customize | ✅ Same product intent |
| Process Owner (customer) | ✅ Matches your primary audience |
| Activity types + argument rules | ✅ Maps to skill activity palette + Show* toggles |
| CRUD + draft/active lifecycle | ✅ "Manage" — broader than create-only |
| Generates/stores process definitions | Your v1: WU/XAML deploy; ADO US is UI-level spec |
| Stages within process editor | ⚠️ Broader than skill's linear PhaseActivities — scope tension |

## Coaching note

ADO #400794 is **already the formal backlog** for what you're calling Process Builder. Your Cursor skill is the **generation engine**; Tone's US + v0 prototype is the **UX contract**. Worth explicitly linking this BMAD brief to #400794 as upstream authority.
