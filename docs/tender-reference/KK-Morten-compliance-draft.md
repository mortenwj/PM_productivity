# KK Plan og Byg — Compliance draft (Morten)

**Source:** `source/KK Tender tool.xlsx` (sheet 1, Responsible = Morten)  
**Generated:** 2026-07-07  
**Status in tool:** All 30 rows **Not Started (0%)**  
**Answer documents:** None of the linked `Bilag 2 - …docx` files exist in `source/` yet — names are **planned deliverables only**.

---

## Summary

| Metric | Count |
|--------|------:|
| Total requirements (Morten) | 30 |
| MK — Minimumskrav (Verify) | 9 |
| K — Konkurrencekrav (Check) | 4 |
| IK — Informationskrav (Answer) | 17 |
| Tool: «1. Fully met» | 9 |
| Open / needs clarification | 8 |
| Answer bilag not created | 17 |

### Draft compliance (working)

| Status | Count | Meaning |
|--------|------:|---------|
| **Met** | 9 | MK verify rows + clear product fit; confirm in bid text |
| **Met / Partial** | 6 | Core met; PnB scope, BI/LIS split, or scoring nuance |
| **Clarify** | 5 | Question to buyer or internal (PnB, SSO, IFAR, templates) |
| **Draft needed** | 10 | IK Answer — no bilag yet; prior art in NND/KUM/Nationalbanken |

---

## Compliance matrix

| Req ID | Title | Type | Action | Draft compliance | Prior art / module | Answer bilag | Risk | Next action |
|--------|-------|------|--------|------------------|-------------------|--------------|------|-------------|
| **5.2.6.6.** | Overblik på sagsdokumenter | IK | Answer | **Draft** | PnB case docs; NND granskning/arbeidsflyt | Planned — **missing** | Medium | Draft bilag; confirm PnB document tree/tagging |
| **5.2.7.1.** | Sagsoverblik og adviseringer | K | Check | **Clarify** | Webdele, saved searches, notifications | — | High | Confirm dashboard/advis vs desktop; PnB UX |
| **5.2.7.2.** | Tilpasset overbliksvisning | IK | Answer | **Met / Partial** | Lagrede søg, skrivebord (NND 02.01) | Planned — **missing** | Medium | Draft bilag; map personal/team views |
| **5.2.8.8.** | Kommunikation | IK | Answer | **Met / Partial** | Digital Post, e-mail; **BOM → PnB** | Planned — **missing** | Medium | Align with PnB on BOM; draft bilag |
| **5.2.8.13.** | Skabeloner (case templates?) | K | Check | **Clarify** | Case templates / 360° Administrator | — | High | Confirm PnB case templates; ask if K means case types |
| **B2-06** | Sagsflow og processer | MK | Verify | **Met** | 360° Flow (KUM processtyring bilag) | — | Low | One-line verify + reference Flow |
| **5.2.12.1.** | Sagens overblik | IK | Answer | **Draft** | Case history, relations (NND) | Planned — **missing** | Medium | Draft bilag; PnB-specific dates (BT/IBT) |
| **5.2.12.2** | Understøtte sagsflow | IK | Answer | **Draft** | Flow, overlevering, historik | Planned — **missing** | Medium | Draft bilag; tie to 360° Flow |
| **B2-10** | Advis og notifikationer | MK | Verify | **Met** | Notifications, frister, status (verify breadth) | — | Medium | Confirm due-date coverage; short verify text |
| **B2-15** | LIS — ekstern efterbehandling | MK | Verify | **Met** | Management Reporting API | — | Low | Verify sentence + API ref |
| **5.2.18.1.** | Rapportering og dataoverførsel | IK | Answer | **Met / Partial** | Mgmt Reporting API; lagrede søg (NND) | Planned — **missing** | Medium | **Draft in progress**; no «vedlagte» until bilag exists |
| **B2-16** | AI planer (MK) | MK | Verify | **Met** | AI governance; Mimir/roadmap | — | Medium | Verify + align with 5.2.19.1 IK |
| **5.2.19.1.** | AI beskrivelse | IK | Answer | **Draft** | `docs/product/context/ai-governance-principles.md` | Planned — **missing** | Medium | Draft bilag: shipped vs planned vs tilkøb |
| **5.3.1.4.** | Notatpligt | MK | Verify | **Met** | Notes / documents on case | — | Low | Short verify; notes vs dokument mindset |
| **5.3.1.5.** | Aktindsigt | IK | Answer | **Clarify** | IFAR / aktindsigt module in PnB? | Planned — **missing** | High | Confirm IFAR in PnB; Digital Post intake |
| **5.3.2.2** | Løst koblet arkitektur | IK | Answer | **Draft** | BRE/Flow, modular platform | Planned — **missing** | Medium | Architecture narrative + regelmotor (BRE) |
| **5.3.3.1.1** | Datakvalitet | IK | Answer | **Draft** | Metadata, code tables, validation | Planned — **missing** | Low | Standard product answer |
| **5.3.4.2** | Fejltekster | IK | Answer | **Draft** | Configurable messages | Planned — **missing** | Low | Draft bilag |
| **5.3.4.4** | Danske tegn | MK | Verify | **Met** | UTF-8 UI + integrations | — | Low | Short verify |
| **5.3.5.1** | Pålidelighed / concurrent users | IK | Answer | **Draft** | Consider **reassign** (comment: Salg DK) | Planned — **missing** | Medium | Confirm owner; ops/SaaS narrative |
| **5.3.5.3** | Genoptagelse efter nedbrud | IK | Answer | **Draft** | Autosave, recovery | Planned — **missing** | Medium | Draft bilag |
| **5.3.5.4** | Fejltilstand ved forkert input | K | Check | **Met** | Validation, no system halt | — | Medium | Check competition text; SIF errors (5.3.3.1.2 ref) |
| **5.3.7.1** | CIA | IK | Answer | **Draft** | Security standard text | Planned — **missing** | Low | Reuse Nationalbanken/KUM security |
| **5.3.7.2** | Privacy by design | IK | Answer | **Draft** | GDPR, encryption, minimization | Planned — **missing** | Low | Reuse prior bids |
| **5.3.7.3** | Security by default | IK | Answer | **Draft** | Least privilege, defense in depth | Planned — **missing** | Low | Reuse prior bids |
| **5.3.7.1.4** | Session timeout | K | Check | **Clarify** | SSO vs idle timeout | — | High | **Spørgsmål til ordregiver** (SSO clash?) |
| **5.3.7.2.1.** | Transaktionslogning | MK | Verify | **Met** | Audit trail / brugslog | — | Low | Short verify |
| **5.3.7.2.2.** | Administratorlogning | MK | Verify | **Met** | Admin-audit | — | Low | Same as KUM position |
| **5.3.7.2.3.** | Systemlogning | MK | Verify | **Met** | Admin-audit config changes | — | Low | Same as KUM position |
| **5.3.7.2.7.** | Beskyttelse af log | IK | Answer | **Draft** | Azure logging, RBAC | Planned — **missing** | Low | Reuse security bilag |

---

## Gap summary (bid impact)

| Severity | Req IDs | Issue |
|----------|---------|--------|
| **High — clarify before bid** | 5.2.7.1, 5.2.8.13, 5.3.1.5, 5.3.7.1.4 | PnB capability / SSO / IFAR / templates undefined |
| **Medium — scoring risk** | 5.2.18.1, 5.2.7.2, 5.2.8.8 | LIS partly via 3rd party BI; BOM split with PnB |
| **Low — verify only** | B2-06, B2-10, B2-15, B2-16, 5.3.1.4, 5.3.4.4, 5.3.7.2.1–2.3 | Draft short verify statements |

---

## Recommended drafting order

1. **MK Verify (9)** — quick pass/fail statements in matrix (½–1 day)
2. **Clarifications (4)** — buyer questions; block 5.2.8.13, 5.3.1.5 until answered
3. **IK Answer with strong prior art**
   - 5.2.18.1 (LIS) — use NND + KUM processtyring
   - 5.2.19.1 (AI) — governance + roadmap
   - 5.3.7.x security cluster — Nationalbanken PDF extracts
4. **PnB-specific functional (5.2.6, 5.2.12, 5.2.7)** — coordinate with PnB team
5. **Architecture / reliability (5.3.2.2, 5.3.5.x)** — consider handoff per tool comments

---

## Win themes (Morten cluster)

1. **Configurable without code** — saved searches, dashboards, Flow process models  
2. **LIS via open API** — Management Reporting API + Power BI (not black-box reporting)  
3. **Traceability** — case history, audit/admin logs, document change log  
4. **Responsible AI** — clear shipped vs planned (5.2.19.1 / B2-16)

---

## Evidence sources for drafting

| Topic | Prior art path |
|-------|----------------|
| Lagrede søg / reporting | `extracted/NND/02.01-…kravtabell.txt` |
| Management Reporting API | `extracted/KUM-SLKS/Bilag 3 - 11.8 - …Processtyring (1).txt` |
| 360° Flow / process | Same + `KK Tender tool` B2-06 comment |
| Security / logging | `extracted/Nationalbanken/Bilag 9*.txt` |
| AI | `docs/product/context/ai-governance-principles.md` |

---

*Working draft — update «Draft compliance» after internal review and buyer Q&A.*
