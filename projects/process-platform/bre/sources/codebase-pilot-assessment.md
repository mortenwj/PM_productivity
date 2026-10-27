# BRE — detailed codebase scan (2026-06-08)

**Assembly:** `SI.Biz.Core.ProcessPlatform.RulesEngine` (33 files)  
**Meta:** `SI.Biz.Core.ProcessPlatform.Meta/Bre/` (31 files)  
**Admin:** `SI.Client.Api.Process/RuleSet/Admin/`  
**Tests:** 8 integration files + ~70 unit test methods in `UnitTest/RulesEngine/`

---

## File inventory

### Runtime (`RulesEngine/Runtime/`)

| File | Purpose |
|------|---------|
| `RuleSetExecuter.cs` | Resolve inputs → DMN execute → HandleResult |
| `IRuleSetExecuter.cs` | Execute single / matching rule sets |
| `RuleSetEventHandler.cs` | DocumentManager event subscriptions |
| `RuleSetInspector.cs` | Published rule cache, DMN compile |
| `ExecutableRuleSet.cs` | Runtime snapshot model |
| `ExecutableRuleSetStatus.cs` | Ready / FailedCritical |
| `RuleSetExecutionResult.cs` | Status, inputs, outputs, exception |
| `DmnLoggerFor360.cs` | DMN engine log adapter |

### Input resolution

| File | ValueSource |
|------|-------------|
| `InputResolverService.cs` | Orchestrator |
| `StaticInputResolver.cs` | Static |
| `EntityFieldResolver.cs` | EntityField |
| `StatementFieldResolver.cs` | StatementField |
| `ManualInputResolver.cs` | ManualInput |
| `NoInputResolver.cs` | None |

### DMN bridge

| Direction | Key classes |
|-----------|-------------|
| Meta → DMN | `DmnFromMetaBuilder`, `IDmnModelBuilder` |
| DMN → Meta | `DmnToMetaGenerator`, `StatementBuilder` (+ partials) |

### Meta managers (`Meta/Bre/`)

RuleSet, Decision, DecisionRule, InputOutput, Expression, DecisionDependency, KnowledgeSource — each with MetaBase/Insert/Update/Delete, Manager, Validator patterns.

---

## Critical code excerpts

### ValidationMessage works; RunProcess stubbed

```143:177:c:\Users\MortenJensen\source\repos\te-industry-public360\core-bl\Source\si-bl-process-platform-build\SI.Biz.Core.ProcessPlatform.RulesEngine\Runtime\RuleSetExecuter.cs
        internal static void HandleResult(DmnExecutionContext dmnContext, RuleSetExecutionResult result, ExecutableRuleSet ruleSet)
        {
           if(result.ResultStatus != EnumBreExecutionResultStatus.Success)           
                return;
            // ...
                if (executionType == EnumBreDecisionExecutionType.ValidationMessage)
                {
                    // ... throws BizInfoException with Message output
                }
                else if (executionType == EnumBreDecisionExecutionType.RunProcess)
                {
                    // Handle process execution
                    
                }
        }
```

### ContextEntity not used in matching

```77:96:c:\Users\MortenJensen\source\repos\te-industry-public360\core-bl\Source\si-bl-process-platform-build\SI.Biz.Core.ProcessPlatform.RulesEngine\Runtime\RuleSetInspector.cs
        internal static IEnumerable<ExecutableRuleSet> GetExecutableRuleSets(
            EnumBreTriggerType triggerType,
            EnumBreTriggerSubType triggerSubType)
        {
            // ...
            return values.Where(new Func<ExecutableRuleSet, bool>(x =>
                x != null &&
                x.TriggerType == triggerType &&
                x.TriggerSubType == triggerSubType));
        }
```

### Event handler skips unsupported entities but doesn't filter by context

```80:112:c:\Users\MortenJensen\source\repos\te-industry-public360\core-bl\Source\si-bl-process-platform-build\SI.Biz.Core.ProcessPlatform.RulesEngine\Runtime\RuleSetEventHandler.cs
            var contextEntity = e.Operation?.Statement?.Entity?.ToBreContextEntity();
            // ...
            if (contextEntity == null)
            {
                return;
            }
            // contextEntity never passed to ExecuteMatchingRuleSets
            results = ruleSetExecuter.ExecuteMatchingRuleSets(
                    triggerType, 
                    triggerSubType.Value, 
                    true);
```

### Wrong decision selected

```115:120:c:\Users\MortenJensen\source\repos\te-industry-public360\core-bl\Source\si-bl-process-platform-build\SI.Biz.Core.ProcessPlatform.RulesEngine\Runtime\RuleSetExecuter.cs
                var firstDecision = dmnContext.Decisions.LastOrDefault();
                if (firstDecision.Key == null)
                    throw new BizErrorException($"Rule set {ruleSet.Id} has no executable decisions");

                executionResult = dmnContext.ExecuteDecision(firstDecision.Key);
```

---

## Enums (full surface)

From `RuleSetEnums.cs`:

- **TriggerType:** None, Event, Job, Manual
- **TriggerSubType:** None, OnInsert, OnUpdate, OnDelete
- **ContextEntity:** None, Case, Document, ProcessModel, Stage, Milestone, StageProcess, ProcessModelConfig, MilestoneConfig, StageConfig, Contact
- **DecisionExecutionType:** None, RunProcess, ValidationMessage
- **ValueSourceType:** None, Static, ManualInput, SystemFunction, EntityField, StatementField, CustomFunction
- **RuleSetStatus:** Draft, Published, Archived
- **ScheduleTime:** None, Nightly, Hourly, EveryThreeMinutes

---

## Integration test files

| File | What it proves |
|------|----------------|
| `MetaHandlers/RuleSetMetaBaseTest.cs` | Validation rules, publish immutability (~18 tests) |
| `MetaHandlers/RuleSetManagerTest.cs` | Version management |
| `MetaHandlers/DecisionMetaBaseTest.cs` | Decision entity rules |
| `DmnToMeta/DmnToMetaGenerator.cs` | DMN XML → meta entities |
| `MetaToDmn/DmnModelBuilder.cs` | Meta → DMN field parity |
| `RunTime/RuntimeTests.cs` | Cache load only — **not rule outcome** |
| `RunTime/MultipleDecisionsExecution.cs` | Multi-decision load — **TO BE EXTENDED** |
| `RunTime/EntityFieldResolver.cs` | Input resolution integration |
| `ClientApi/RuleSetAdminApiTest.cs` | Admin API with feature flag |

All integration tests return early if `BusinessRuleEngineEnabled` is off.

---

## Feature flag metadata

```365:386:c:\Users\MortenJensen\source\repos\te-industry-public360\core-bl\Source\si-bl-core-build\SI.Util\Resources\FeatureFlags\FeatureFlags.json
  "BusinessRuleEngineEnabled": {
    "ToggleType": "Development",
    "ToggleDescription": "Enables the business rules engine framework",
    "ToggleWorkItemId": "370776",
    "IsOnByDefault": false,
    "ModuleName": "Business rules engine"
  }
```

Referenced UI paths: `core-360-react-views` WelcomePage, BIF AdminMainMenu/Locator sitemaps.

---

## TODOs found in code / tests

| Source | Item |
|--------|------|
| `RuntimeTests.cs` | Extend to assert rule fires on HolyBanana case update |
| `RuleSetMetaUpdateTest.cs` | GUID validation (ADO #377717) |
| `RuleSetMetaInsert/Update` | "Temp approach" — full cache refresh |
| `RuleSetMetaDelete` | Empty implementation |
| `EnumBreDecisionDependencyType` | Comment: "more to come.." |
| `RuleSetEventHandler` | Future: generic exception with admin page reference |

---

## Admin API (RuleSetAdminApi) summary

Gated by `FeatureIsolator<BusinessRuleEngineEnabled>`:

- `GetAdminRuleSetListItem()` — list
- `GetRuleSetDetails(recno)` — details + DMN XML from meta
- `SaveRuleSet(SaveRuleSetProps)` — DMN → meta
- `PublishRuleSet(recno, setEnabled?)` — publish thread + enable
- `GetEntityAndTriggerTypeListOption()` — Case/Document triggers

Internal helpers: `GetPublishRuleSetConfigStatement`, `GetRsWithGuid`, version unpublish logic.

---

## Plugin engine

`PluginMethodApi` scans bin folder for `*pluginengine*` / `*rulesetplugin*` assemblies, reflects `[Query]` and `[Action]` methods. **No RuleSetPlugin project in core-bl.** No runtime invocation from DMN to plugin methods.
