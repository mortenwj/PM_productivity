# BRE — pilot readiness and gaps

**Sources:** `BRE_Pilot_Readiness_Assessment.md`, `BRE_Code_Risk_Assessment.md`, `BRE_Inventory.md` §6

---

## Executive verdict

Backend framework is **substantial** but product is **not customer-ready** for full Oslo-deck / scope-sheet scenarios.

| Scope | Readiness |
|-------|-----------|
| **Narrow pilot** (Event → Case OnUpdate → ValidationMessage) | **~55–60%** after 2 runtime fixes |
| **Full scenario register** | **~30–35%** |

---

## Recommended pilot slice

| Element | Choice |
|---------|--------|
| Trigger | Event / Case OnUpdate |
| Action | ValidationMessage (block with message) |
| Inputs | EntityField, StatementField, Static |
| Tenant | 1 pilot tenant, flag ON, 1–2 published rule sets |

**Maps to:** #219865, #239187 (partial #202616 needs Document OnUpdate in admin picker)

---

## Engineering blockers (before customer pilot)

1. Fix ContextEntity + IsEnabled filtering in `GetExecutableRuleSets`
2. Honor StartingPoint OR constrain pilot to single-decision models
3. Complete `RuntimeTests` — assert ValidationMessage blocks update
4. Enable feature flag on pilot tenant
5. Wire admin UI to existing APIs (if not done in webadmin)

**Estimate in assessment:** ~3–5 sprints depending on team (June 2026 baseline).

---

## Timeline tension

| Anchor | Date | Notes |
|--------|------|-------|
| Epic #11122 target | 2026-12-30 | Platform delivery ambition |
| Commitment cluster (IVO, Danish K) | H2 2027 | Needs automation beyond ValidationMessage |
| Past commitment | #312153 2025-06-30 | Helsedirektoratet — overdue pressure |

**Planning implication:** 2026 = narrow validation pilot plausible; tender commitments need RunProcess, jobs, field rules not in code today.

---

## Commercial guardrail

Flow commercial spec: deep BRE automation is **Year 1+ backlog**. PRD should date-scope automation vs validation clearly.

---

## Risks (summary)

See `sources/risk-register-summary.md` and `BRE_Code_Risk_Assessment.md` for ranked technical and commercial risks.
