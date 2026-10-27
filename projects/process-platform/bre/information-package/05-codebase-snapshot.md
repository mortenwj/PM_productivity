# BRE — codebase snapshot

**Repo:** `te-industry-public360/core-bl`  
**Path:** `Source/si-bl-process-platform-build/SI.Biz.Core.ProcessPlatform.RulesEngine/`  
**Scanned:** 2026-06-16 (static; confirms June 2026 assessment)

**Detail:** [`../sources/codebase-pilot-assessment.md`](../sources/codebase-pilot-assessment.md), [`../BRE_Reverse_Engineered_PRD.md`](../BRE_Reverse_Engineered_PRD.md)

---

## What exists (high level)

| Layer | Status |
|-------|--------|
| DMN meta model (`Meta/Bre/`) | Strong — RuleSet, Decision, InputOutput, Expression, versioning |
| Meta ↔ DMN bridge | Bidirectional (`DmnFromMetaBuilder`, `DmnToMetaGenerator`) |
| Publish lifecycle | RuleSetManager validators; publish API |
| Runtime executor | `RuleSetExecuter` — DMN evaluate + ValidationMessage |
| Event hooks | `RuleSetEventHandler` — gated by `BusinessRuleEngineEnabled` |
| Input resolution | Static, EntityField, StatementField, Manual (partial set) |
| Admin API | `RuleSetAdminApi`, `PluginMethodApi` |
| Tests | ~70 unit tests; integration tests load cache but weak e2e assertions |

---

## Runtime flow (implemented path)

1. Meta CRUD event → `RuleSetEventHandler` (if feature ON)
2. `RuleSetInspector.GetExecutableRuleSets(triggerType, triggerSubType)`
3. `InputResolverService` resolves DMN inputs
4. DMN engine executes decision
5. `HandleResult` — **ValidationMessage** throws `BizInfoException`; **RunProcess** stub empty

---

## Critical gaps (code defects)

| # | Issue | Location |
|---|-------|----------|
| 1 | **ContextEntity not filtered** at runtime | `RuleSetInspector.GetExecutableRuleSets` |
| 2 | **IsEnabled not checked** at runtime | Same |
| 3 | **RunProcess action empty** | `RuleSetExecuter.HandleResult` |
| 4 | **StartingPoint ignored** | `RuleSetExecuter` |
| 5 | Before/On/After collapsed to one subtype | `RuleSetEventHandler` |
| 6 | No Job scheduler | — |
| 7 | No e2e ValidationMessage proof | `RuntimeTests.cs` |

---

## Feature gating

```csharp
// RuleSetEventHandler.cs — skips setup when flag OFF
if (!Is.Feature<BusinessRuleEngineEnabled>.On())
```

Default: **OFF** per wiki feature toggles.

---

## Admin UI

Not in `core-bl`; WebAdmin tile + `process-views` routes referenced in product docs. Separate repos (webadmin, BIF).

---

## Codebase path for PRD technical appendix

```
core-bl/Source/si-bl-process-platform-build/
├── SI.Biz.Core.ProcessPlatform.RulesEngine/   # runtime, DMN bridge, input resolution
├── SI.Biz.Core.ProcessPlatform.Meta/Bre/      # meta entities + managers
├── SI.Client.Api.Process/RuleSet/Admin/       # admin APIs
└── IntegrationTest.ProcessPlatform/RulesEngine/
```
