# BRE — Reverse-engineered PRD (from code)

**Purpose:** Describe what the codebase actually implements — not aspirational wiki/DevOps text.  
**Date:** 2026-06-08 · **Evidence:** `core-bl` Process Platform RulesEngine assembly

---

## 1. Product intent (inferred)

Allow administrators to define **DMN 1.3 decision models** stored as 360 meta entities, publish them as **Business Rule Sets**, and execute them when **meta CRUD events** occur on supported entities — primarily to **block operations with validation messages**.

Secondary intent (partially modeled, not delivered): trigger **process actions** and **scheduled jobs** from rule outcomes.

---

## 2. Users and permissions

| Actor | Capability (code) |
|-------|-------------------|
| Process admin + feature flag | Access admin APIs / WebAdmin tile (external UI) |
| End user | Subject to ValidationMessage blocks on CRUD |
| Developer | Plugin DLL discovery; no runtime plugin invoke path |
| Service account (`allaccess_serviceaccount`) | Loads rule cache at startup |

**Gating:** `BusinessRuleEngineEnabled` must be ON (tenant-level feature flag, default OFF).

---

## 3. Core concepts (implemented)

### 3.1 Rule set

A versioned, publishable artifact with:

- Name, description
- Trigger configuration (type + subtype + context entity)
- DMN decision graph (decisions, rules, inputs, expressions)
- Lifecycle: Draft → Published → Archived
- Enable/disable flag (`IsEnabled`) — **stored but not enforced at runtime**

### 3.2 Trigger model

| TriggerType | Runtime | Meta validation |
|-------------|---------|-----------------|
| **Event** | **Implemented** via DocumentManager shim | Requires ContextEntity + TriggerSubType |
| **Job** | **Not implemented** | Requires ScheduledTime (Nightly, Hourly, EveryThreeMinutes) |
| **Manual** | **Not implemented** | Allowed in meta |

**Event subtypes:** OnInsert, OnUpdate, OnDelete — all Before/On/After event variants map to the **same** subtype.

### 3.3 Context entities

**Enum supports 10 entities:** Case, Document, ProcessModel, Stage, Milestone, StageProcess, ProcessModelConfig, MilestoneConfig, StageConfig, Contact.

**Admin picker exposes:** Case, Document only.  
**Publish validation restricts to:** Case, Document.  
**Runtime matching:** Trigger type/subtype only — **ContextEntity not filtered**.

### 3.4 Decision outcomes (actions)

| DecisionExecutionType | Behavior |
|----------------------|----------|
| **None** | Evaluate only; no side effect |
| **ValidationMessage** | If DMN output includes `Message` variable → throw `BizInfoException` → **blocks CRUD** |
| **RunProcess** | **Empty stub** — no process invocation |

This is narrower than Oslo deck actions (Raise Error ✓, Update data ✗, Send notification ✗, Push event ✗).

### 3.5 Input binding

Rules resolve DMN inputs from:

- Static values (JSON config)
- Fields on the triggering entity (`EntityField`)
- Fields on the current `MetaStatement` (`StatementField`)
- Manual input dictionary (programmatic invoke — no user UI path found)

---

## 4. User journeys (as code supports them)

### Journey A — Author and publish a validation rule *(API-complete)*

1. Admin opens Business Rules UI *(external repo)*
2. Creates/edits rule set as DMN XML
3. `SaveRuleSet` → `DmnToMetaGenerator` → meta entities created/updated (Draft)
4. `PublishRuleSet(recno, setEnabled: true)` → status Published, cache refreshed
5. Rule set appears in `RuleSetInspector` memory store

**Gap:** `SaveRuleSetProps.IsEnabled` not applied on save.

### Journey B — Block case update *(partially working)*

1. User updates case (MetaStatement Update on Case)
2. DocumentManager fires BeforeUpdate/OnUpdate/AfterUpdate
3. `RuleSetEventHandler` runs all Published rule sets matching Event + OnUpdate
4. DMN evaluates; ValidationMessage decision throws message
5. User sees error; update blocked

**Gaps:** May also run rules for wrong ContextEntity; disabled rules may run; wrong decision if multi-decision model.

### Journey C — Auto-close cases on schedule *(not supported)*

1. Rule set with TriggerType = Job, ScheduledTime = Nightly
2. **No scheduler or handler exists**
3. RunProcess action would be needed — **stubbed**

---

## 5. Admin API requirements (implemented)

| ID | Requirement | Status |
|----|-------------|--------|
| ADM-1 | List rule sets with status/triggers | Done |
| ADM-2 | Load rule set details + DMN XML | Done |
| ADM-3 | Save rule set from DMN XML | Done |
| ADM-4 | Publish with enable/disable | Done |
| ADM-5 | List entity/trigger options for designer | Done (Case/Document subset) |
| ADM-6 | List plugin query/action methods | Done (discovery only) |
| ADM-7 | Delete rule set | **Not implemented** |
| ADM-8 | Generate new version | Internal meta only; **not in API** |
| ADM-9 | View runtime load errors per rule set | Fields exist; **not populated** |

---

## 6. Runtime requirements (implemented vs not)

| ID | Requirement | Status |
|----|-------------|--------|
| RT-1 | Load Published rule sets at startup | Done |
| RT-2 | Refresh cache on rule set meta change | Done (full rebuild) |
| RT-3 | Execute on meta CRUD events | Done (feature-gated) |
| RT-4 | Match by trigger type + subtype | Done |
| RT-5 | Match by context entity | **Not done** |
| RT-6 | Respect IsEnabled | **Not done** |
| RT-7 | Execute StartingPoint decision | **Not done** (uses last decision) |
| RT-8 | ValidationMessage blocks operation | Done |
| RT-9 | RunProcess invokes process | **Not done** |
| RT-10 | Job trigger on schedule | **Not done** |
| RT-11 | Manual invoke API | **Not done** |
| RT-12 | Plugin action execution | **Not done** |
| RT-13 | Log execution to RuntimeState | **Not done** |

---

## 7. Non-functional (observed)

| Attribute | Observation |
|-----------|-------------|
| Performance | In-memory cache; full refresh on each meta change |
| Concurrency | Thread-safe snapshot swap in inspector |
| Security | Admin APIs feature-gated; rule execution uses current CallContext user |
| Observability | Log.Info/Error in executer; no structured audit trail |
| Upgrade safety | Published immutability enforced in meta validators |
| i18n | ValidationMessage uses raw DMN Message strings |

---

## 8. Out of scope in code (despite meta/wiki hints)

- FFUI field-dependency rules (separate FFUI stack)
- Rules library / import-export UX
- Query interface for rules
- Statistics and monitoring dashboards
- Standard rule-set pack for 360
- DMN diagram editor (XML round-trip only)
- Multi-tenant rule sharing

---

## 9. Pilot MVP definition (code-aligned)

**In scope:**

- Event-triggered validation rules on **Case OnUpdate**
- ValidationMessage action only
- Static + EntityField + StatementField inputs
- Publish/enable via admin API + UI
- Single-decision rule sets only

**Acceptance criteria:**

1. Published rule set blocks case close when mandatory field empty
2. Disabled rule set does not execute *(requires RT-6 fix)*
3. Document rules do not fire on Case events *(requires RT-5 fix)*
4. Integration test proves ValidationMessage on case update *(requires RT test extension)*

**Out of scope for MVP:**

- Auto-close jobs, data updates, notifications
- Plugin methods, SystemFunction inputs
- ProcessModel / milestone entities
- Customer self-service without consultant

---

## 10. Gap map: Oslo deck → code

| Oslo concept | Code equivalent | Status |
|--------------|-----------------|--------|
| Trigger: Event | Event + OnInsert/Update/Delete | Partial |
| Trigger: Job | Job enum | Meta only |
| Trigger: FFUI | — | Not in BRE |
| Action: Raise Error | ValidationMessage | **Works** |
| Action: Update data | RunProcess (intended?) | **Stub** |
| Action: Send notification | — | **Missing** |
| Action: Push event | — | **Missing** |
| Rule designer | Admin API + external UI | API yes |
| DMN import/export | SaveRuleSet / GetRuleSetDetails | **Works** |
