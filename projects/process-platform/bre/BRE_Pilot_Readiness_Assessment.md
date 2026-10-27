# BRE — Pilot readiness assessment (from source code)

**Scanned:** 2026-06-08 · **Repo:** `core-bl/Source/si-bl-process-platform-build/`  
**Method:** Static analysis of runtime, meta, admin APIs, feature flags, and test suites

---

## Executive summary

The BRE **backend framework is substantial** — DMN meta model, bidirectional DMN bridge, publish lifecycle, admin APIs, event hooks, and strong validation/unit test coverage. What exists today is closer to an **internal platform skeleton** than a customer-ready product.

**Pilot verdict:** A **narrow, controlled pilot** is technically feasible for one scenario type:

> **Event trigger → Case or Document meta event → ValidationMessage action → Static / EntityField / StatementField inputs**

Everything beyond that — process actions, scheduled jobs, plugin actions, multi-decision models, FFUI — is **not ready** in code.

| Dimension | Readiness | Notes |
|-----------|-----------|-------|
| Meta model & DMN bridge | **High (~85%)** | Publish validation, versioning, round-trip tested |
| Admin APIs | **Medium (~70%)** | Save/list/publish exist; no delete, no generate-version API |
| Event runtime | **Medium (~55%)** | Wired but filtering gaps; Before/On/After collapsed |
| Action types | **Low (~25%)** | ValidationMessage only; RunProcess stubbed |
| Trigger types | **Low (~33%)** | Event only; Job/Manual have meta validation, no runtime |
| Input resolution | **Medium (~60%)** | 4 of 6 value sources implemented |
| Admin UI | **Unknown in core-bl** | Gated by flag in separate repos (webadmin, BIF) |
| End-to-end proof | **Low** | Integration tests load cache; do not assert rule outcomes |
| Feature flag | **Off by default** | Development toggle since 6.6 |

**Overall pilot readiness (narrow scope): ~55–60%**  
**Overall pilot readiness (Oslo deck / scope sheet scenarios): ~30–35%**

---

## What a pilot *can* demonstrate today

Assuming `BusinessRuleEngineEnabled` ON and a tenant with published rule sets:

1. **Block case update** with a user-visible validation message (close-case style rules)
2. **Block document insert** on Document OnInsert events
3. **Author rules** via admin API (DMN XML save) — UI depends on webadmin work
4. **Publish and enable** rule sets with version threading

### Recommended pilot slice (matches First-wave scope)

| Scenario | Invoke | Action | Inputs | Code support |
|----------|--------|--------|--------|--------------|
| Close-case validation (#219865) | Event / Case OnUpdate | ValidationMessage | EntityField, StatementField | **Feasible** with fixes below |
| Void-only empty cases (#239187) | Event / Case OnUpdate | ValidationMessage | EntityField | **Feasible** |
| Checked-out files (#202616) | Event / Document OnUpdate | ValidationMessage | EntityField | **Partial** — Document OnUpdate not in admin picker |

---

## Blockers before any customer pilot

These are **code defects or gaps**, not product polish:

| # | Issue | Impact | Location |
|---|-------|--------|----------|
| 1 | **No ContextEntity filter at runtime** | Case event may run Document rules (and vice versa) | `RuleSetInspector.GetExecutableRuleSets` |
| 2 | **IsEnabled not checked at runtime** | Disabled rule sets may still execute | Same |
| 3 | **RunProcess action empty** | Auto-close, update data, notifications impossible | `RuleSetExecuter.HandleResult` |
| 4 | **StartingPoint ignored** | Wrong decision executed in multi-decision models | `RuleSetExecuter` line 116 |
| 5 | **Before/On/After collapsed** | Cannot distinguish pre-validation vs post-action | `RuleSetEventHandler.GetTriggerSubType` |
| 6 | **No Job scheduler** | Auto-close scheduled rules (#311335) impossible | No handler |
| 7 | **No e2e runtime test** | Unknown if ValidationMessage actually fires on HolyBanana update | `RuntimeTests.cs` — "TO BE EXTENDED" |
| 8 | **Feature off by default** | Must be explicitly enabled per tenant | `FeatureFlags.json` |

---

## Minimum viable pilot (engineering)

**Scope:** 1 tenant, 1–2 rule sets, Case OnUpdate + ValidationMessage only.

**Engineering checklist (~3–5 sprints depending on team):**

1. Fix runtime filtering: ContextEntity + IsEnabled in `GetExecutableRuleSets`
2. Honor StartingPoint (or document single-decision constraint for pilot)
3. Complete `RuntimeTests` — assert ValidationMessage blocks case update
4. Wire admin UI to existing APIs (if not already done in webadmin repo)
5. Operational runbook: enable flag, publish rules, monitor logs
6. Decide BeforeUpdate vs OnUpdate semantics for validation rules

**Out of pilot v1:** RunProcess, Job triggers, plugins, FFUI, rules library, statistics.

---

## Capability matrix (code truth)

| Capability | Meta | Admin API | Runtime | Tests |
|------------|------|-----------|---------|-------|
| Draft / Publish / Archive | Yes | Yes | N/A | Strong |
| Version threading (BaseUID) | Yes | Partial | N/A | Yes |
| IsEnabled | Yes | Publish API | **Not enforced** | No |
| Event trigger | Yes | Yes | Yes | Partial |
| Job trigger | Validated | No | **No** | No |
| Manual trigger | Validated | No | **No** | No |
| ValidationMessage | Yes | Via DMN | **Yes** | No e2e |
| RunProcess | Yes | Via DMN | **Stub** | No |
| Static input | Yes | Yes | Yes | Yes |
| EntityField input | Yes | Yes | Yes | Yes |
| StatementField input | Yes | Yes | Yes | Yes |
| SystemFunction input | Enum only | — | **No** | No |
| CustomFunction / plugins | Discovery API | List only | **No invoke** | No |
| DMN DecisionTable | Yes | Yes | Yes | Strong |
| DMN Expression | Yes | Yes | Yes | Some |
| Case context | Yes | Admin picker | **No filter** | — |
| Document context | Yes | Admin picker (OnInsert only) | **No filter** | — |
| Delete rule set | Stub | No | N/A | No |
| RuntimeState / LastLoadErrors | DB fields | — | **Not written** | No |

---

## Comparison to DevOps / wiki claims

| Claim (DevOps/wiki) | Code reality |
|---------------------|--------------|
| "DMN runtime engine shipped" | **True** — internal DMN engine integrated |
| "Meta event triggers in progress" | **Partially true** — handler exists, gaps in matching |
| "Admin UX in progress" | APIs ready; UI not in core-bl |
| "Rules library backlog" | No library concept in code |
| "Auto-close scheduled" | Job trigger enum exists; **no scheduler** |
| Oslo deck: Raise Error, Update data, Send notification | Only **ValidationMessage** (Raise Error) works |

---

## Recommended workshop decisions (Copenhagen)

1. **Define pilot contract:** Validation-only, Case OnUpdate, max N rule sets per tenant
2. **Assign blocker fixes** to sprint before any customer touch
3. **Do not demo** RunProcess, auto-close jobs, or plugin actions until implemented
4. **Align ProductPlan/DevOps** — epic target 2026-12-30 assumes more than code delivers today
5. **AST / IVO commitments** — assess whether ValidationMessage-only slice satisfies any tender items

---

## Related documents

| Document | Content |
|----------|---------|
| [BRE_Architecture.md](./BRE_Architecture.md) | Component diagram, execution flow |
| [BRE_Reverse_Engineered_PRD.md](./BRE_Reverse_Engineered_PRD.md) | Product spec inferred from code |
| [BRE_Code_Risk_Assessment.md](./BRE_Code_Risk_Assessment.md) | Risks ranked by pilot impact |
| [sources/codebase-pilot-assessment.md](./sources/codebase-pilot-assessment.md) | Detailed file-level inventory |
