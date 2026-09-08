# v0 prototype — Process arguments design

**Status:** Public deployment available  
**Updated:** 2026-09-08

## URLs

| Version | URL | Access |
|---------|-----|--------|
| **Public deploy (use this)** | https://processmaker-gamma.vercel.app/ | ✅ No login required |
| v2 build chat | https://v0.app/tonefjeller-5562/chat/process-arguments-design-2-Ch0JWkexgI1 | v0 login |
| v1 (ADO #400794) | https://v0.app/chat/process-arguments-design-bMgrPOiYsjh?ref=Z52ANW | v0 login |

## Observed UI structure (from public deploy)

```
┌────────────────────┬─────────────────────────────────────────────┐
│ Opprettede         │  Prosessopprettingssystem                   │
│ prosesser          │  [Argumenter | Egenskaper]                  │
│ (list, empty)      │                                             │
│                    │  Behandlingsform * (global vs fase-spes.)   │
│ [EN] language      │  Navn på prosessen *                        │
│                    │                                             │
│                    │  ▼ Opprett aktivitet for å lage dokument    │
│                    │  ▼ Registrer mottatt dato                   │
│                    │  ▼ Send oppgave til "X"                     │
│                    │  ▼ Opprett møte/avtale                      │
│                    │  ▼ Åpne lenke                               │
│                    │  ▼ Registrer dato                           │
│                    │                                             │
│                    │  [Lagre prosess]  [Nullstill]               │
└────────────────────┴─────────────────────────────────────────────┘
```

### Key scope signals

1. **No stage editor inside the process** — flat accordion of activity types, not a stage graph. Stage vs global is handled by **Behandlingsform** dropdown at process level.
2. **Six activity types** — matches ADO user story chapters D–I; maps 1:1 to skill palette (minus StartSubprocess/Checkpoint as separate sections — may be inside accordions when expanded).
3. **Manage** — left sidebar lists saved processes (CRUD intent); prototype uses client-side state only today.
4. **Argumenter vs Egenskaper tabs** — arguments vs metadata split.
5. **Norwegian primary** + EN toggle — customer-facing locale assumption.

## UX ↔ skill mapping

| Prototype accordion | Skill activity type |
|--------------------|---------------------|
| Opprett aktivitet for å lage dokument | `DocumentFlowWizard` |
| Registrer mottatt dato | `MilestoneDialog` / date pattern |
| Send oppgave til "X" | `Checkpoint` / `Task` |
| Opprett møte/avtale | `MeetingInviteDialog` |
| Åpne lenke | `OpenUrl` |
| Registrer dato | `MilestoneDialog` (generic date) |

**Behandlingsform** → likely maps to WU categories (`ProgressPlan Process` vs `Stage Process`) or PMC attachment context — needs product decision.

## Gaps vs full ADO user story

| In prototype | In full US | v1 call |
|--------------|------------|---------|
| Flat activity accordions | Stages + activities | ✅ Prototype = simpler; aligns with 80% rule |
| Argument tab | Per-activity conditional rules | TBD — expand accordions to verify |
| Process list sidebar | Clone from standard library | Not visible — may be missing from POC |
| Lagre prosess | Deploy WU/XAML to instance | Not implemented in POC |

## Evidence files

- `../evidence/v0-prototype/homepage.html` — static snapshot of deploy homepage
