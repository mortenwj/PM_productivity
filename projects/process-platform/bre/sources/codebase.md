# BRE — codebase inventory

**Repo:** `core-bl/Source/si-bl-process-platform-build/`  
**Primary assembly:** `SI.Biz.Core.ProcessPlatform.RulesEngine`  
**Admin API:** `SI.Client.Api.Process/RuleSet/Admin/`

---

## Feature toggle

| Toggle | Effect |
|--------|--------|
| `BusinessRuleEngineEnabled` | Required for runtime event handler, rule execution, admin APIs |

If off: `RuleSetEventHandler` logs and exits; APIs throw `Feature 'BusinessRuleEngineEnabled' is not enabled`.

---

## Project structure

```
SI.Biz.Core.ProcessPlatform.RulesEngine/
├── Runtime/
│   ├── RuleSetExecuter.cs          # DMN execution (internal)
│   ├── IRuleSetExecuter.cs
│   ├── RuleSetEventHandler.cs      # Meta event bindings
│   ├── RuleSetInspector.cs         # Find matching rule sets
│   ├── ExecutableRuleSet.cs
│   └── RuleSetExecutionResult.cs
├── InputResolution/
│   ├── InputResolverService.cs
│   └── Resolvers/
│       ├── EntityFieldResolver.cs
│       ├── StatementFieldResolver.cs
│       ├── StaticInputResolver.cs
│       └── ManualInputResolver.cs
├── MetaToDmn/                      # Meta → DMN model
│   └── DmnModelBuilder.cs
├── DmnToMeta/                      # DMN → Meta statements
│   ├── DmnToMetaGenerator.cs
│   └── StatementBuilder*.cs
└── Integration tests:
    IntegrationTest.ProcessPlatform/RulesEngine/
```

---

## Meta entities (from tests and handlers)

| Entity | Role |
|--------|------|
| `BusinessRuleSet` | Root rule set; status, published date, enabled flag |
| `BusinessRuleDecision` | DMN decision |
| `BusinessRuleDecisionRule` | Decision table rules |
| `BusinessRuleInputOutput` | Inputs/outputs |
| `BusinessRuleExpression` | Expressions |
| `BusinessRuleKnowledgeSource` | Knowledge sources |

**Publish lifecycle** (`RuleSetAdminApi`):
- Update status → Published
- Set PublishedDate
- Enable/disable via `IsEnabled`

---

## Runtime execution

### RuleSetExecuter

- Resolves inputs via `IInputResolverService`
- Executes DMN decisions using `ProcessPlatform.RuntimeEngines.Dmn.Engine`
- `ExecuteMatchingRuleSets(triggerType, triggerSubType, abortOnFailure)` — batch execution
- Class is **`internal`** — extension from outside assembly limited

### RuleSetEventHandler

- Implements `IEventSetup` with `[BizEventSetup]`
- When feature on: binds to `DocumentManagerEventShim` meta events:
  - OnInsert, BeforeInsert, AfterInsert
  - OnUpdate, BeforeUpdate, AfterUpdate
  - OnDelete, BeforeDelete, AfterDelete
- Maps event type → `EnumBreTriggerType.Event` + trigger subtype
- Unsupported entities abort gracefully

---

## Admin API (`RuleSetAdminApi`)

- List rule sets (`AdminRuleSetListItem`)
- Publish / enable rule sets
- DMN ↔ Meta conversion via `DmnModelBuilder`, `DmnToMetaGenerator`
- Gated by `BusinessRuleEngineEnabled`

**Related:** `PluginMethodApi` — discover plugin methods for rule actions

---

## UI (React — separate repo)

From Flow PRD reconstruction:
- Routes: `Admin/BusinessRules/*` in `process-views`
- Files: `AdminRulesRoutes.tsx`
- Rule set dashboard / editor / manager
- **Separate from ProcessView** (case execution UI)
- WebAdmin tile: **Business Rules** (process admin + feature flag)

---

## Position in Flow platform

From `360_Flow_PRD_Reconstruction_Unredacted_v4.md`:

| Attribute | Value |
|-----------|-------|
| Capability | Rules (DMN rule sets) |
| Maturity | Shipped (engine internal) |
| Layer | Rules & Governance Capabilities |
| Configurability | Medium — rule artifacts and registration |
| Pilot usage | Medium (if rules used in pilot) |
| Limitation | No DMN editor in `process-components`; authoring elsewhere |

**Governance:** Rules (DMN) — functional user defines outcomes with consultant; developer implements resolvers/plugins; `internal` executer boundary.

---

## Plugin extensibility

From Process Platform developer guidelines (PRD appendix):
- Plugin DLLs in `ProcessPlatform.PluginPath`
- Filename must contain `pluginengine` or `rulesetplugin`
- Strong name public key token validation
- `[Action]` / `[Query]` methods for custom rule logic

---

## Key files for deep dive

| File | Why read |
|------|----------|
| `RuleSetExecuter.cs` | Execution path |
| `RuleSetEventHandler.cs` | Event trigger integration |
| `RuleSetAdminApi.cs` | Publish/admin surface |
| `DmnModelBuilder.cs` | Meta → DMN |
| `IntegrationTest.ProcessPlatform/RulesEngine/RunTime/RuntimeTests.cs` | Behaviour examples |
