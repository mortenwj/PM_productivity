# BRE — purpose and vision

**Evidence:** Epic [#11122](https://dev.azure.com/tieto-si/360/_workitems/edit/11122), `BRE_Inventory.md`, `sources/wiki-and-product.md`, Flow PRD reconstruction

---

## One-line definition

The **Business Rules Engine (BRE)** is Public 360°'s **rules and governance layer** within the **Process Framework**: configurable operational decision logic (validations, constraints, automation) without bespoke code.

---

## Process Framework role

| Component | Question |
|-----------|----------|
| Process Models | **What** the process looks like |
| 360 Flow / Process Engine | **How** the process runs |
| **Business Rules Engine** | **When** actions are allowed or required |

---

## Strategic intent (DevOps epic #11122)

> Support configurable (no/low code) business rules in 360 so customers can tailor how the system behaves in various situations.

**Key decisions already made:**

- Early **InRule** evaluation did not meet needs → **internal engine**
- Must support **DMN (Decision Model and Notation)** — [OMG DMN](https://www.omg.org/dmn/)
- DMN enables **import/export** and portability of rule sets

**Intended benefit categories:**

1. **Configurable validations** — e.g. block dispatch if files checked out; milestone prerequisites; close-case rules
2. **IFTTT-style automation** (often with processes) — e.g. on dispatch create wait task; on project creation spawn related cases
3. **Portable rules** — share rule packs across customers and potentially systems

---

## Customer / market tension

Public-sector customers need **standardization, compliance, auditability** *and* **local adaptation**. Today much logic lives in customizations, consultants, or opaque configuration. BRE aims to make **operational governance semantics** explicit, versionable, and reportable.

**Oslo workshop framing:** BRE under **"Responsive Business Logic"** in the 360 value chain (Collect → Engage → **Process** → Publish → Archive) — *flexibility in standard*.

---

## Rule model (product concept)

```
Trigger (WHEN)  →  Condition (IF)  →  Action (WHAT)
```

### Trigger types (target)

| Type | Examples |
|------|----------|
| Event | Case/document updated, process step completes |
| Scheduled / Job | Daily batch, timed auto-close |
| Invoked | Integration, process, UI |
| FFUI | Entity creation / field validation |

### Action types (target)

| Type | Examples |
|------|----------|
| Raise Error | Block user action; validation message |
| Update data | Set status, due date, sync responsible |
| Send notification | Email / alert |
| Push event | External system event |

---

## Wiki aspiration (not yet a dedicated module page)

From [Flexibility initiatives](https://wiki.software-innovation.com/wiki/Flexibility_initiatives) — planned capabilities include no-code builder, rule types, invocation paths, versioning, auditing, API access. **Dedicated BRE module wiki page does not exist yet.**

---

## Relationship to 360 Flow

- Flow PRD: **Rules & Governance Capabilities** layer; canonical term **Rules** = operational governance semantics
- Flow commercial spec: *deep BRE automation beyond Year 1* is backlog — avoid overselling at Flow GA without date qualifiers
- Feature toggle `BusinessRuleEngineEnabled` — **OFF** by default since 6.6

---

## Prototype / UX reference

- https://business-rules-360.lovable.app/ (design exploration; not production)
