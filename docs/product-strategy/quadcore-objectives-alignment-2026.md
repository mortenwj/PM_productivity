# QuadCore — team objectives alignment (2026–2027)

**Purpose:** Detail for **§7 Platform enablers** in the **[QCLT objectives alignment pack](qclt-objectives-alignment-pack-2026.md)**. QuadCore is not a separate product feature team in ProductPlan, but **co-delivers* *BL2**, **TP1**, **TP2**, and **CE1** infrastructure.

**Read first:** [qclt-objectives-alignment-pack-2026.md](qclt-objectives-alignment-pack-2026.md) (company + team objectives, Phase A, AI, agentic spike). **Do not** use this file alone as the meeting pre-read.

**Status:** Draft for alignment · **Date:** 21 September 2026  
**Parent context:** [Strategy brief](team-objectives-strategy-brief-2026.md) · [Refresh workbook](team-objectives-refresh-workbook-2026.md) · [Agent appendix D7/D9](agent-strategy-appendix-d7.md)

---

## 1. Why this meeting

- UIM and Copenhagen timelines require **Online deployment**, **logging/SIEM**, and (if approved) **AI hosting** to be **named in objectives**, not assumed.
- ProductPlan today lists *Supporting cont. deployments (TUXIT)* on **Core BL + QuadCore** — we propose **merging it into Core BL objective BL2**, with **QuadCore KRs** spelled out explicitly.
- QuadCore does **not** get a fourth parallel product OKR set; we agree **who signs which KRs** and **capacity** against UIM/Copenhagen/merger.

---

## 2. Company themes (context only — owned by QCLT)

| ID | Theme | QuadCore touch |
|----|--------|----------------|
| **CO1** | Platform-ready for growth | Online readiness, migration enablers (fold *Develop product capabilities to support continuation of Nordic Public 360° Online migrations and further growth*) |
| **CO2** | Desirable, accessible case handling | Indirect (stable Online) |
| **CO3** | Governed AI on the case platform | **T2 hosting / residency** if **D9b** approved |
| eDoc merger Q2 2026 | Container/Online path for merger |

---

## 3. Where QuadCore fits in the proposed product OKRs

### A. Primary — **Core BL BL2** (Online deployment maturity)

**Proposed owner in ProductPlan:* *Core BL** (LPM accountable).  
**QuadCore role:* *Co-deliver** containerization / TUXIT / continuous deployment for 360° Online.

| Today (ProductPlan) | Phase A proposal |
|---------------------|------------------|
| *Supporting cont. deployments (TUXIT)* TUXIT / containerization (teams **5102 Core BL** + **5268 QuadCore**) | Merge into **BL2**; archive duplicate framing |

**Draft BL2 themes (product org view):**

1. TUXIT / containerization milestones for Online growth, UIM integration hosts, *Succeed with eDoc product merger by Q2 2026* merger.
2. Outlook integration (*Outlook integration*) — Core BL product scope; QuadCore only if infra/hosting involved.

**Ask QuadCore:** Confirm which **BL2 key results** QuadCore LPM co-owns vs supports; publish **FTE envelope** for UIM peak (gate briefs cite **Tech Platform ~1–2 FTE** on UIM logging cluster — validate for full BL2 scope).

---

### B. Program KRs — **TP1 / TP2** (no QuadCore team slot in ProductPlan today)

If QuadCore/Tech Platform does not get a dedicated ProductPlan team objective, these live as **program KRs** (company **CO1/CO3** or joint BL/AI charter):

| ID | Theme | Enables | UIM / Copenhagen |
|----|--------|---------|------------------|
| **TP1** | **Tenant residency and platform monitoring** (sovereignty, SIEM) | **BL1** logging, **AI1**, KK **435501** | UIM logs / open architecture (**MK-160**) — CloudOps sign-off in gate briefs |
| **TP2** | **T2 AI inference ops** (if **D9b** approved) | **CO3**, native agents, small/mid kommuner turnkey | Copenhagen domestic-cloud narrative (with AI & Insights) |

**Ask QuadCore:** Prefer **TP1/TP2 as explicit QuadCore-signed KRs** under CO3/CO1, or **embedded KRs under BL2 + AI1** with QuadCore named as deliverer?

---

### C. Dependencies on other teams (QuadCore as enabler, not owner)

| Upstream need | Product objective | QuadCore contribution |
|---------------|-------------------|------------------------|
| Stable Online / deploy pipeline | **CE1** (Collect), **INT1**, **CU1** | Hosting, env promotion, test→prod infra for config migration |
| SIEM-ready platform logs | **BL1**, **INT1**, **AI1** | LogPoint / monitoring feasibility (KK gate: sign-off or Q&A narrow) |
| Nordic managed inference | **AI1**, **AI2** | T2 ops pattern ([agent appendix](agent-strategy-appendix-d7.md)) |

---

## 4. What is **not** proposed for QuadCore this cycle

- **No** standalone ProductPlan objective duplicating **BL2** unless QCLT insists on a QuadCore team slot.
- *Operational Reporting* Operational Reporting — **out of OKR set** (partial path via Core UI **CU1** search refactoring).
- **IFAR / PP3** — dropped as product OKR; no QuadCore objective tied to IFAR handover.

---

## 5. UIM + Copenhagen — QuadCore-relevant commitments

| Source | Requirement | Proposed home |
|--------|-------------|---------------|
| UIM | Platform logging / analytics export (**MK-160**), Tech Platform PFRs | **TP1** + **BL1** coordination |
| UIM | Online / integration deployment | **BL2** |
| Copenhagen KK | SIEM / governance surface (**435501**) | **TP1**, **BL1**, **AI1** |
| Copenhagen / CO3 | Domestic-cloud / T2 hosting story | **TP2** (decision **D9b**) |
| eDoc *Succeed with eDoc product merger by Q2 2026* | Online merger readiness | **BL2** |

---

## 6. Decisions for the meeting (agenda)

1. *Supporting cont. deployments (TUXIT)* → **BL2:** Agree merge; split **KR ownership** Core BL vs QuadCore.
2. **TP1 (residency + monitoring):** QuadCore-signed KRs — where in ProductPlan (CO1, BL2, or new Tech Platform slot)?
3. **TP2 (T2 inference):** In scope for 2026–2027 or **defer** until D9b — capacity yes/no.
4. **UIM timeline:** Confirm FTE and milestones for logging/deploy vs UIM bid dates.
5. **KK / SIEM:** LogPoint feasibility — commit, partial, or Q&A-only (align with gate brief action).
6. **CE1 config migration:** QuadCore role in **test→prod** environments (supporting Collect + Core BL).

---

## 7. Suggested pre-read (attach or link)

| Doc | Use |
|-----|-----|
| [team-objectives-refresh-workbook-2026.md](team-objectives-refresh-workbook-2026.md) — § Core BL **BL2**, § Tech Platform / QuadCore | Full proposal |
| [team-objectives-strategy-brief-2026.md](team-objectives-strategy-brief-2026.md) — Trends 1–2, decisions **D8/D9** | Why sovereignty + AI hosting matter |
| [agent-strategy-appendix-d7.md](agent-strategy-appendix-d7.md) — T1–T4, **TP2** | Hosting patterns |
| UIM / KK management gate briefs (`docs/tender-reference/`) — Tech Platform FTE rows | Capacity sanity check |

---

## 8. One-page summary for email

**Subject:** Product objectives 2026–27 — QuadCore alignment (BL2 / TP1 / TP2)

We are consolidating product team OKRs around **UIM**, **Copenhagen**, and **merger**. QuadCore is central to **Online deployment (BL2)** and likely **platform monitoring/residency (TP1)** and **T2 AI ops (TP2)** if leadership approves D9b.

ProductPlan objective *Supporting cont. deployments (TUXIT)* would merge into **Core BL BL2** with **QuadCore co-owned KRs** — not a separate duplicate objective.

Please review the attached brief and come prepared to agree: (1) BL2 vs QuadCore KR split, (2) where TP1/TP2 live in ProductPlan, (3) UIM/deploy/logging capacity.

---

## Revision log

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-09-21 | Initial QuadCore alignment brief |
