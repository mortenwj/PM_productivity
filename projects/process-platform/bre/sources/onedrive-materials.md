# OneDrive — BRE materials

**Folder:** `C:\Users\MortenJensen\OneDrive - Tieto\Technology & Development - Public 360 - Business Rules Engine`  
**Indexed:** 2026-06-08

---

## Files in folder

| File | Type | Purpose |
|------|------|---------|
| `BRE_scope_and_scenarios.xlsx` | Excel | Customer scenarios, scope waves, priority scoring |
| `Risk assesment Business_Rules.xlsx` | Excel | Project risk register for BRE |
| `Oslo BRE workshop.pptx` | PowerPoint | Internal product overview (*Flexibility in standard*) |
| `business-rules-360.lovable.app.url` | Shortcut | UI prototype link |

**Prototype URL:** https://business-rules-360.lovable.app/

---

## BRE_scope_and_scenarios.xlsx

### Sheet 1 — Scenario register

Columns: **Invoke Type | Rule Type | Description | Customer | DevOps | Comments | Scope | Discovery**

**Scope values observed:**
- **First** — priority wave 1 scenarios
- **Second** — priority wave 2 scenarios

**Invoke types in register:** Event, Job, FFUI

**Rule types:** Update, Raise Error, FFUI

See [scenarios-register.md](./scenarios-register.md) for row-by-row extract.

### Sheet 2 — Additional scenario ideas (unlinked)

Examples (Norwegian/Danish notes):
- Approved documents not dispatched → notify responsible
- Checklist checkpoints → only allowed action is close case
- Milestone deadline reached → close case or notify case handler
- Attach rules to individual milestones

### Sheet 3 — Priority scoring

| Area | Customer value | Strategic value | Implementation cost | Risk |
|------|----------------|-----------------|---------------------|------|
| Rules editor | 5 | 5 | 4 | 2 |
| Rules analysis | 3 | 4 | 5 | 3 |

**Interpretation:** Rules **editor** is highest priority on customer + strategic dimensions.

---

## Risk assesment Business_Rules.xlsx

Standard risk template with register + matrix sheets.

Key risks extracted — see [risk-register-summary.md](./risk-register-summary.md).

Linked DevOps item from register: [#364641 BRE - Business Rules Admin UX](https://dev.azure.com/tieto-si/360/_workitems/edit/364641) (security / privileged authoring).

---

## Oslo BRE workshop.pptx

16 slides — internal overview deck used in Oslo workshop.

Full text summary: [oslo-workshop-deck.md](./oslo-workshop-deck.md)

---

## Usage notes

- Excel files are **source of truth** for scenario prioritization workshops
- Keep OneDrive folder synced; this repo holds **extracts and summaries** only
- Re-import when scope sheet is updated before Copenhagen BRE session
