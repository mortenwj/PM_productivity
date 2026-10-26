# Reference — 360° release wiki

## WIQL (Azure DevOps)

**Process Platform — tagged for a release (example 6.12):**

```sql
SELECT [System.Id], [System.Title], [System.WorkItemType], [System.State], [System.Tags]
FROM WorkItems
WHERE [System.TeamProject] = '360'
  AND [System.AreaPath] UNDER '360\Core-Process-platform'
  AND [System.State] <> 'Removed'
  AND ([System.Tags] CONTAINS '6.12' OR [System.Tags] CONTAINS '6.12 RV')
ORDER BY [System.Id]
```

**Process Platform delivery tag (RV fixes, cross-area):**

```sql
SELECT [System.Id], [System.Title], [System.WorkItemType], [System.State], [System.AreaPath], [System.Tags]
FROM WorkItems
WHERE [System.TeamProject] = '360'
  AND [System.State] <> 'Removed'
  AND [System.Tags] CONTAINS 'Process Platform'
  AND ([System.Tags] CONTAINS '6.12' OR [System.Tags] CONTAINS '6.12 RV')
ORDER BY [System.Id]
```

**IFAR / access request (confirm ownership before publishing under PP):**

```sql
SELECT [System.Id], [System.Title], [System.WorkItemType], [System.State], [System.AreaPath], [System.Tags]
FROM WorkItems
WHERE [System.TeamProject] = '360'
  AND [System.State] <> 'Removed'
  AND (
    [System.Title] CONTAINS 'IFAR'
    OR [System.Title] CONTAINS 'innsyn'
    OR [System.Title] CONTAINS 'access request'
  )
  AND ([System.Tags] CONTAINS '6.12' OR [System.Tags] CONTAINS '6.12 RV')
ORDER BY [System.Id]
```

Replace `6.12` / `6.12 RV` with the target release tags.

## Wikitext templates (no ADO IDs in bullets)

### IFAR — under *News and improvements in existing module(s)*

```wikitext
== 360° IFAR (access requests) — corrections in 6.12 ==
'''Market:''' Norway (IFAR / public access requests)

'''Corrections and improvements'''

* '''Email import (GEMI):''' …
* '''Case handling:''' …
* '''Response template:''' …
* '''Administration:''' …
* '''File lifecycle:''' …

'''Related pilot content'''

See also '''Improved Import of Access Requests from eInnsyn (Pilot)''' below.
```

### Flow GA — blocks inside `== 360° Flow - Now Generally Available ==`

**Former name (one line):**

```wikitext
'''Former name:''' PAF — Process Automation Framework.
```

**Highlights in 6.12 (example bullets):**

```wikitext
'''Highlights in 6.12'''

This release includes Flow platform improvements validated through pilot customers:

* '''Background processes''' — … Enable with feature toggle '''FT:EnableBackgroundProcesses''' when agreed for your tenant.
* '''Deadlines''' — …
* '''Process Model Admin''' — Drag-and-drop to reorder processes on a stage, milestones in the process model, and processes/milestones in stage templates. Sort order stays consistent with the Sort ID field.
* '''Process email dialog''' — Standard email templates and macros, optional template/language selection, and localized message body text where configured.
```

**Bug fixes (grouped):**

```wikitext
'''Bug fixes'''

The following corrections are included for Flow and process handling in 6.12:

* …
* '''Email and meeting dialogs''' — Contact fields save correctly when edited; email attachments can be toggled; …
```

**Important notes:**

```wikitext
'''Important notes'''

* Additional Flow capabilities (for example extended localization administration) remain under active development.
* Work unit argument configuration was updated in 6.12; implementers upgrading custom process packages should validate stage process setup after upgrade.
```

### Technical notes — Process Platform

```wikitext
=Technical notes=

== Process Platform (360° Flow) ==
'''Work unit registry (6.12)''' — Process packages use the consolidated work unit arguments layout in registry version '''ms_6.12.0'''. After upgrade, validate stage process configuration and custom process packages in Process Model Admin.

See also the '''Important notes''' under '''360° Flow - Now Generally Available'''.
```

## Mapping ADO → wiki section

| ADO signal | Typical wiki placement |
|------------|-------------------------|
| New product module GA (e.g. RP feature Flow) | `=New module=` |
| Existing module, fixes/features | `=News and improvements in existing module(s)=` |
| Core BL, not a named module | `=New features and improvements in the core product=` |
| Active / pilot-only | `=Coming soon (Ongoing Pilots)=` or Important notes only |
| Registry, on-prem, implementers | `=Technical notes=` |
| Rejected / New not shipped | Omit from customer text |

## Housekeeping (optional, user-approved)

- Remove obsolete HTML comment inventories at page bottom after content is merged into live sections.
- Do **not** update module marketing pages (e.g. `[[360° Flow]]`) unless the user explicitly includes them in scope.
