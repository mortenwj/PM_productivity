# BRE — wiki, product docs, and commercial context

**Collected:** 2026-06-08 (MediaWiki MCP — live fetch)

---

## MediaWiki (live)

**Status:** Fetched successfully via MediaWiki MCP.

### Key pages

| Page | Status | BRE content |
|------|--------|-------------|
| [Flexibility initiatives](https://wiki.software-innovation.com/wiki/Flexibility_initiatives) | Live | Full BRE section + core features list |
| [Process Framework](https://wiki.software-innovation.com/wiki/Process_Framework) | **DRAFT** | BRE as core component — "when" actions allowed/required |
| [360° Flow](https://wiki.software-innovation.com/wiki/360%C2%B0_Flow) | **DRAFT** | BRE in platform context table; availability varies by release |
| [Feature Toggles 2025-2026](https://wiki.software-innovation.com/wiki/Feature_Toggles_2025-2026) | WIP | `BusinessRuleEngineEnabled` — OFF, since 6.6 |
| **Business Rules Engine** (dedicated module) | **Does not exist** | Planned when product released |

---

## Flexibility initiatives — BRE section (extract)

> The Business Rules Engine (BRE) will allow Public 360 users to define, manage, and invoke business rules across the platform in a no-code interface. These rules can be triggered through the web interface, integrated into workflows, or invoked via API calls. This will enhance the customization capabilities of the solution for customer- or segment-specific processes.
>
> Contact: Morten Jensen (morten.jensen@tietoevry.com)

**Core features (wiki list):**

- No-code Rule Builder (drag-and-drop or form-based)
- Rule Types — validation, calculation, decision, routing, etc.
- Rule Invocation — UI, workflows, API
- Contextual Data Inputs — form data, workflow states, external APIs
- Rule Prioritization and Conflict Handling
- Version Control — history and rollbacks
- Auditing and Logging — compliance
- Extensibility and Scalability — external APIs, large customer bases
- API Access — invoke rules from external systems

*Last wiki revision: 2026-02-04*

---

## Process Framework (draft) — BRE positioning

From core components table:

| Component | Purpose |
|-----------|---------|
| **Business Rules Engine (BRE)** | Decide **when** actions are allowed or required: no-code/low-code rules, event- and time-based triggers, compliance and constraints |

Documentation link: [[Flexibility initiatives]] until dedicated BRE page exists.

*Last wiki revision: 2026-02-25*

---

## 360° Flow (draft) — platform context

| Component | Role |
|-----------|------|
| **Business Rules Engine** | Rules and deadlines in the process (**availability varies by release**) |

Flow is part of Process Framework; not a separate BPM product. Pilot on 6.10; commercial packaging not finalised.

*Last wiki revision: 2026-06-04*

---

## Feature toggle

| Toggle | Description | Default | Since |
|--------|-------------|---------|-------|
| `BusinessRuleEngineEnabled` | Enables business rules engine framework | **OFF** | 6.6 |

Source: [Feature Toggles 2025-2026](https://wiki.software-innovation.com/wiki/Feature_Toggles_2025-2026) — Process Platform / Process Model section.

---

## Local wiki drafts

**Path:** `projects/process-platform/process-models/`

Local drafts align with live wiki content. Process Framework landing page draft was used to seed the live page.

---

## 360 Online help center

**Search (Ratatoskr):** "Business Rules Engine" — **no results**

**Search:** "business rules" — one tangential hit in case settings (responsible inheritance note).

**Conclusion:** Customer-facing help for BRE is **not yet published** in help center.

---

## Flow PRD reconstruction

**Path:** `projects/process-platform/flow/360_Flow_PRD_Reconstruction_Unredacted_v4.md`

- **Rules** = operational governance semantics
- Rules Engine = operational DMN runtime
- Shipped but runtime-oriented; authoring UX limited in current slice
- AI direction: future — rules provide structure for governed AI participation
- Commercial appendix: rules admin separate from ProcessView

---

## Flow commercial spec

**Path:** `projects/process-platform/flow/360_Flow_Commercial_Spec_v1.md`

- Enterprise may include "Advanced rules lifecycle" when GA
- **Backlog (do not sell at GA):** "deep BRE automation beyond Year 1 emphasis"

---

## Admin access (verified answer)

**Path:** `docs/lmwtfy-answers/Process manager role and process models admin access.md`

- WebAdmin **Business Rules** tile gated by `isProcessAdmin` + `BusinessRuleEngineEnabled`
- Process manager alone does not unlock other admin tiles

---

## UI prototype

**URL:** https://business-rules-360.lovable.app/  
**Source shortcut:** OneDrive `business-rules-360.lovable.app.url`

Likely exploration for Admin UX (#364641, #392248) — not necessarily production UI.

---

## Oslo workshop deck

Product narrative for internal workshops — see [oslo-workshop-deck.md](./oslo-workshop-deck.md)

---

## ProductPlan roadmap

See [productplan-roadmap.md](./productplan-roadmap.md) for Process Platform and PP now-next-later BRE bars.
