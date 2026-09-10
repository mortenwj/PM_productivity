# Agent strategy — appendix to D7

**Purpose:** Short decision input for QCLT before team objective workshops.  
**Parent:** [`team-objectives-strategy-brief-2026.md`](team-objectives-strategy-brief-2026.md) (D7, D8, D9)  
**Status:** Draft for reaction · **Date:** 10 September 2026

---

## The question

How should Public 360° position itself in an **agent-first, sovereignty-aware** market — own agents, enable customer/partner agents, or support external initiatives?

**Why now:** Sandnes wants PnB agents on 360; NKF (66 kommuner) runs Copilot without archive integration; Visma pitches BYO-AI; KK requires REST to municipal AI Assist; FI market requires segregated agent APIs.

---

## Four main themes

### 1. Platform first, not agent monopoly

**Default: B + C, with selective A.**

| Path | Commit | In one line |
|------|--------|-------------|
| **B — AI-enabled platform** | **Primary** | Context, actions, events, credentials, audit — customers and partners bring agents/models |
| **C — Leap / support** | **Yes, funded** | NKF, Sandnes, GAIIA — integration patterns, not competing with every Copilot build |
| **A — Native agents** | **2–3 domains only** | Metadata, summary/timeline, redaction, PnB triage — where domain depth and audit need it |

**Not recommended:** Agent for every module; AI feature-count KRs without platform and governance.

### 2. Governance belongs to 360; hosting is a separate choice

Buyers ask **where inference runs** and **who operates it** — especially **outside sole US hyperscale** for case workloads (AST, KK, NB, Oslo, Vahva). Org Copilot may stay on Microsoft; **case data must be routed, logged, and residency-controlled**.

**360 product must own:** model registry, central routing/proxy, classification gates, human-in-the-loop rules, agent audit (SIEM-ready).

**Hosting patterns (pick per customer, don't custom-build forever):**

| Pattern | Who runs models | 360 role |
|---------|-----------------|----------|
| **T1 BYO** | Customer/partner | Governance + APIs (default for B) |
| **T2 Nordic/EU managed** | **Tieto CloudOps** (+ partner) | Native agents turnkey |
| **T3 Sovereign local** | **Customer IT** (+ optional Tieto TS) | Certified connector + reference architecture |
| **T4 US hyperscale** | Customer (Copilot etc.) | Policy boundary — no case payload by default |

**Ops rule for T3:** Tieto owns connectors and governance; customer owns GPU/model ops unless **explicit TS SKU**. Never claim "local LLM support" without that boundary.

### 3. Sovereignty is handlingsrom, not anti-US

Large customers (Oslo, NAV) want **agnostic architectures** and future optionality. Small/mid kommuner adopt AI fast on **standard Microsoft cloud** and lack IT muscle to swap stacks. Strategy must serve **both**: packaged T2 for turnkey; T1/T3 for sovereign buyers.

### 4. Competitors will sell "open foundation for your agents"

Visma/Framtind narrative: BYO-AI via APIs (still mostly claims). Our answer: **governed case platform + agent-ready APIs + selective native agents** — not a closed AI stack.

---

## Decisions for leadership

| # | Decision | Default |
|---|----------|---------|
| **D7** | Agent mix | **B + C + selective A** |
| **D9** | Hosting & ops | **D9b + D9c** — Tieto-operated Nordic inference (T2) for native agents; certified sovereign pattern (T3) with customer ops default. **Not** full-stack local ops everywhere (D9d) |
| **D8** | Value message | Sovereignty + hosting patterns + BYO-AI — Sebastian + PM (see parent brief) |

**Partnership capacity:** 0.5–1 FTE programme (AI & Insights + Core Integrations) if C is real, not "support will help".

**Pilot customer (pick one):** Sandnes · NKF/Møre og Romsdal · Oslo

---

## Proposed team objectives (preview for Step 2)

| Team | Agent-related objective theme |
|------|------------------------------|
| **AI & Insights** | Governed AI infrastructure (routing, registry, residency) + 2–3 native reference agents + hosting offer owner (T2/T3) |
| **Tech Platform / CloudOps** | T2 inference ops (if D9b approved); tenant residency; platform monitoring |
| **Core Integrations** | Agent-ready API layer as part of #437273 — context, actions, events |
| **Core BL** | Agent identity, audit trail, SIEM-compatible logging |
| **Plan & Build** | PnB agent integration pilot (Sandnes / KK AI Assist pattern) |
| **Process Platform** | Agent actions on Flow tasks, milestones, and process context |
| **Collect & Engage** | GAIIA / intake channel integration at platform edge |

---

## Please react (short list)

1. Confirm **D7** and **D9** defaults — or mark alternatives.
2. **Pilot customer** for agent platform MVP?
3. **GAIIA** in partnership lane 2026–2027 — yes/no?
4. **CloudOps** capacity for T2 inference — yes/no/defer?
5. **T3:** Tieto TS managed ops SKU — yes/no?

---

## Revision log

| Version | Date | Change |
|---------|------|--------|
| 0.1 draft | 2026-09-10 | Initial D7 appendix |
| 0.2 draft | 2026-09-10 | Hosting/governance detail (D9) |
| 0.3 draft | 2026-09-10 | Shortened to main themes; kept team objectives |
