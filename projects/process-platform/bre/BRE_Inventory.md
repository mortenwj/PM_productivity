# Business Rules Engine (BRE) — inventory

**Last updated:** 2026-06-08  
**Sources:** DevOps, MediaWiki (live), ProductPlan, OneDrive materials, **core-bl source scan**, Flow PRD reconstruction

---

## 1. What BRE is

The **Business Rules Engine (BRE)** is Public 360°'s **rules and governance layer** within the **Process Framework**. It externalizes operational decision logic — validations, automated updates, notifications, and constraints — so customers can tailor system behaviour **without bespoke code**.

In Process Framework terms (wiki draft):

| Component | Question it answers |
|-----------|---------------------|
| Process Models | **What** the process looks like |
| Process Engine / Flow | **How** the process runs |
| **Business Rules Engine** | **When** actions are allowed or required |

BRE is **not** a standalone module page in the wiki yet. Live pages reference it from [[Process Framework]] (draft) and [[Flexibility initiatives]] — which lists nine planned core features (no-code builder, rule types, invocation, versioning, auditing, API access, etc.).

---

## 2. Problem BRE is intended to solve

### Strategic intent (DevOps Epic #11122)

> Support configurable (no/low code) business rules in 360 so customers can tailor how the system behaves in various situations.

After an early **InRule** evaluation did not meet needs, the team chose an **internal engine** based on the **DMN (Decision Model and Notation)** standard ([OMG DMN](https://www.omg.org/dmn/)).

**Intended benefits:**
- **Configurable validations** — e.g. block dispatch if files are checked out; milestone prerequisites
- **IFTTT-style automation** (often combined with processes) — e.g. on dispatch create wait task; on project creation spawn related cases
- **Portable rules** — import/export via DMN for reuse across customers and potentially other systems

### Public-sector tension (Process Framework / Flow)

Organizations need **standardization, compliance, auditability** *and* **local adaptation**. Today much logic lives in customizations, consultants, or opaque configuration. BRE aims to make **operational governance semantics** explicit, versionable, and reportable.

### Oslo workshop framing (*Flexibility in standard*)

BRE sits under **"Responsive Business Logic"** in the 360 value chain (Collect → Engage → **Process** → Publish → Archive). It enables **individual standard** — commercial standard with segment-specific flexibility.

---

## 3. Rule model (product concept)

From Oslo workshop deck and scope materials:

```
Trigger (WHEN)  →  Condition (IF)  →  Action (WHAT)
```

### Trigger types (invoke types)

| Type | Examples |
|------|----------|
| **Event** | Case updated, document dispatched, process step completes |
| **Scheduled / Job** | Daily, once, timed batch |
| **Invoked** | From integration, process, UI |
| **FFUI** | Full-Flex UI entity creation / field validation |

### Action types (rule types)

| Type | Examples |
|------|----------|
| **Raise Error** | Block user action; validation message |
| **Update data** | Set case status, set due date, sync responsible person |
| **Send notification** | Email / alert |
| **Push event** | Raise event for external system |

### Example patterns (from deck + scope register)

1. **Close-case validation** — mandatory fields; no working documents on close; prevent cancel if documents not cancelled
2. **Auto-close cases** — e.g. status "ready from case handler" + all docs journalized → close (scheduled)
3. **Responsible person sync** — case responsible change propagates to documents
4. **FFUI validation** — meeting document file types, mandatory contact roles

See [sources/scenarios-register.md](./sources/scenarios-register.md) for full customer scenario list.

---

## 4. How BRE fits in Public 360°

```
Public 360°
└── Process Framework
    ├── Process Models        (structure)
    ├── 360 Flow / Process Engine   (execution, ProcessView, progress plans)
    └── Business Rules Engine (DMN rules, validations, automation)
            ↑
    Also relates to: case/document meta events, FFUI, integrations, AI/agentic (future)
```

**In 360 Flow capability model** (PRD reconstruction):
- Layer: **Rules & Governance Capabilities**
- Canonical term: **Rules** = operational governance semantics
- Lifecycle layer: **Governance semantics** alongside structural lifecycle, executable progression, runtime execution

**Feature flag:** `BusinessRuleEngineEnabled` — must be on for runtime and admin APIs.

**Admin access:** WebAdmin tile **Business Rules** (gated by process admin + feature flag). Admin UI routes: `Admin/BusinessRules/*` in `process-views`.

---

## 5. Technical architecture (codebase — current)

**Assembly:** `SI.Biz.Core.ProcessPlatform.RulesEngine`  
**Path:** `core-bl/Source/si-bl-process-platform-build/`

| Area | Key components |
|------|----------------|
| **Runtime** | `RuleSetExecuter` — executes DMN decisions; resolves inputs; `internal` |
| **Event integration** | `RuleSetEventHandler` — binds to meta insert/update/delete events when feature enabled |
| **Input resolution** | Entity fields, statement fields, static/manual inputs |
| **Meta model** | `BusinessRuleSet`, decisions, inputs/outputs, expressions, knowledge sources |
| **DMN bridge** | `MetaToDmn` / `DmnToMeta` — bidirectional meta ↔ DMN |
| **Admin API** | `RuleSetAdminApi`, `PluginMethodApi` — publish, enable/disable rule sets |
| **Plugins** | Signed plugin DLLs for custom rule methods |

**Execution flow (simplified):**
1. Trigger fires (event, schedule, invoke)
2. `RuleSetInspector` finds matching published rule sets
3. Inputs resolved from 360 entities/context
4. DMN engine evaluates decisions
5. Actions applied (error, update, notification, etc.)

Detail: [sources/codebase.md](./sources/codebase.md)

---

## 6. Maturity snapshot (code-verified 2026-06-08)

See **[BRE_Pilot_Readiness_Assessment.md](./BRE_Pilot_Readiness_Assessment.md)** for full analysis.

| Area | Status | Code evidence |
|------|--------|---------------|
| DMN meta model + bridge | **Strong** | Meta/Bre + DmnFromMeta/DmnToMeta; extensive unit tests |
| Publish lifecycle | **Strong** | RuleSetManager validators; PublishRuleSet API |
| Admin APIs | **Medium** | List/save/publish; no delete API |
| Event runtime | **Partial** | Handler wired; **ContextEntity + IsEnabled not filtered** |
| ValidationMessage action | **Works** | Throws BizInfoException on DMN Message output |
| RunProcess / automation actions | **Stub** | Empty branch in HandleResult |
| Job / scheduled triggers | **Not built** | Enum + meta validation only |
| Input resolution | **Partial** | Static, EntityField, StatementField; not SystemFunction/CustomFunction |
| End-to-end runtime proof | **Weak** | RuntimeTests loads cache only — "TO BE EXTENDED" |
| Admin UI | **External** | Not in core-bl; flag refs webadmin + BIF |
| Feature flag | **OFF default** | Development toggle since 6.6 |

**Pilot readiness (validation-only, Case OnUpdate): ~55–60%** after fixing 2 runtime blockers.  
**Full scope sheet / Oslo deck scenarios: ~30–35%.**

### Commitment-driven timeline (planning assumption)

If customer **Commitment**-tagged DevOps items define delivery pressure (rather than epic #11122 target **2026-12-30**), BRE hard dates cluster in **mid–late 2027**:

| Window | ID | Customer / driver | Target | Tag |
|--------|-----|-------------------|--------|-----|
| **Jun 2027** | [#422713](https://dev.azure.com/tieto-si/360/_workitems/edit/422713) | Danish tender K — auto-close docs on case close | 2027-06-14 | `conditional commitment` |
| **Sep 2027** | [#420587](https://dev.azure.com/tieto-si/360/_workitems/edit/420587) | IVO tender — mandatory fields on create/close | 2027-09-30 | `Commitment` |
| **Sep 2027** | [#420590](https://dev.azure.com/tieto-si/360/_workitems/edit/420590) | IVO tender — multivalue field dependency | 2027-09-30 | `Commitment` |
| **Sep 2027** | [#420282](https://dev.azure.com/tieto-si/360/_workitems/edit/420282) | IVO tender — cleaning job on case close | 2027-09-30 | *(no Commitment tag; same tender cluster)* |

**Earlier / overlapping pressure (not mid-2027):**

| ID | Target | Status |
|----|--------|--------|
| [#312153](https://dev.azure.com/tieto-si/360/_workitems/edit/312153) Helsedirektoratet due dates | 2025-06-30 | **Past** — `Commitment` + `Pri 1` |
| [#231319](https://dev.azure.com/tieto-si/360/_workitems/edit/231319) Svenska Kyrkan doc cleanup | *(none)* | Description: upgrade agreement **Feb 2026** |

**Implication:** Epic #11122 (2026-12-30) is **6–9 months ahead** of the commitment cluster. That gap is plausible for a **narrow validation pilot** in 2026, but **not** for IVO/Danish tender scenarios — those need RunProcess, field rules, and/or cleanup automation the code does not deliver today. **Planning anchor: H2 2027** if commitments drive the roadmap.

**Commercial note:** Flow commercial spec says *"deep BRE automation beyond Year 1 emphasis"* is backlog — do not oversell at GA without date qualifier.

---

## 7. Scope prioritization (OneDrive)

From `BRE_scope_and_scenarios.xlsx` — **Scope** column:

| Wave | Representative scenarios |
|------|------------------------|
| **First** | Close-case validation (#219865); void-only for empty cases (#239187); auto-close (#311335) |
| **Second** | Checked-out file validation (#202616); 90-day auto-close (#255097); document archive move rules |

Priority scoring (sheet 3): **Rules editor** scores highest on customer + strategic value.

Full register: [sources/scenarios-register.md](./sources/scenarios-register.md)

---

## 8. Known risks (OneDrive risk register)

Top themes from `Risk assesment Business_Rules.xlsx`:

| Risk | Mitigation direction |
|------|---------------------|
| Privileged access to rules calling BL/data | Rule authoring as privileged action (#364641) |
| No formal price strategy | Enablement / pricing meeting |
| Event system not designed for ad hoc runtime | Accepted — covered in other tasks |
| Shortage of PE/consultant capacity for processes | Consultant education |
| Camunda open-source license | Sourcing verification |
| Long-running rules → bad UX | Performance limits / async patterns |

Detail: [sources/risk-register-summary.md](./sources/risk-register-summary.md)

---

## 9. Azure DevOps structure

**Epic:** [#11122 DMN - Business Rules Engine](https://dev.azure.com/tieto-si/360/_workitems/edit/11122)

**Child features (20 total):**

| ID | Title | State | Owner |
|----|-------|-------|-------|
| 301056 | BRE - Data model | **Active** | Bjørn |
| 371193 | BRE - DMN - Input Resolution Service | **Active** | Bjørn |
| 362499 | BRE - Validations on RuleSets | **Active** | Bjørn |
| 364464 | BRE - Standard (BuiltIn) Queries and Actions | **Active** | Bjørn |
| 301062 | BRE - Executing RuleSets from Meta Events | New | Bjørn |
| 364641 | BRE - Business Rules Admin UX | New | Bjørn |
| 373120 | BRE - BusinessRuleSet Version & Publishing Support | New | Bjørn |
| 392248 | BRE - Admin Design | New | Bjørn |
| 369221 | BRE - Admin - DMN ↔ Meta Model Synchronization | New | Bjørn |
| 301063 | BRE - standard rule-set for 360 | New | — |
| 301068 | DMN - rules library | New | — |
| 301078 | DMN - Query interface for 360 | New | — |
| 364034 | BRE - Statistics and monitoring | New | — |
| 351872 | BRE - PM - Common Project Infrastructure | Closed | Bjørn |
| 90638 | evaluate InRule engine | Closed | Andreas |

Customer-linked features tagged **Business rules**: #219865, #283950 (AST), #311335, etc.

Full list: [sources/ado-work-items.md](./sources/ado-work-items.md)

---

## 10. Wiki, roadmap & product documentation status

| Asset | Status |
|-------|--------|
| [Flexibility initiatives](https://wiki.software-innovation.com/wiki/Flexibility_initiatives) (live) | BRE section + nine core features; contact Morten |
| [Process Framework](https://wiki.software-innovation.com/wiki/Process_Framework) (draft) | BRE as core component — "when" actions allowed/required |
| [360° Flow](https://wiki.software-innovation.com/wiki/360%C2%B0_Flow) (draft) | BRE in platform table; availability varies by release |
| [Feature Toggles 2025-2026](https://wiki.software-innovation.com/wiki/Feature_Toggles_2025-2026) | `BusinessRuleEngineEnabled` — OFF since 6.6 |
| Dedicated BRE module page | **Not yet** — planned when product released |
| ProductPlan — Process Platform | BRE bar **parked**, 52%, stale 2022 dates |
| ProductPlan — PP now next later | Discovery projects BRE; 3 customers (Feb–May 2025) |
| 360 Online help center | No BRE-specific customer docs |
| Oslo workshop deck | Internal product overview — see [sources/oslo-workshop-deck.md](./sources/oslo-workshop-deck.md) |
| UI prototype | https://business-rules-360.lovable.app/ |

Detail: [sources/wiki-and-product.md](./sources/wiki-and-product.md) · [sources/productplan-roadmap.md](./sources/productplan-roadmap.md)

---

## 11. Open questions for team alignment

1. **Pilot scope:** Which invoke types + action types are in first customer-facing release?
2. **Authoring vs runtime:** Four Active DevOps features are runtime foundation; Admin UX still New — gap to close
3. **Roadmap hygiene:** Unpark/update ProductPlan BRE bar; document outcome of "3 customers for discovery"
4. **Process integration:** How do rules connect to Flow progress plans / milestones today?
5. **FFUI vs event rules:** Which wave for FFUI triggers?
6. **AI/agentic:** Rules as guardrails for agentic case management — product hypothesis to validate with customers
7. **Commercial:** Pricing / packaging — risk register flags gap

---

## 12. Related materials outside this folder

- [`../flow/360_Flow_PRD_Reconstruction_Unredacted_v4.md`](../flow/360_Flow_PRD_Reconstruction_Unredacted_v4.md) — Rules in Flow capability model
- [`../process-models/Process_Framework_Wiki_Landing_Page.wikitext`](../process-models/Process_Framework_Wiki_Landing_Page.wikitext) — Framework positioning
- Copenhagen workshop June 2026 — BRE session 13:20–14:50 Day 1
