# SBST — Bilag 1 §3 gap scan (F2 menu vs Public 360°)

**Tender:** Social- og Boligstyrelsen · SKI 02.06 Standardsoftware kategori 1  
**Source:** Bilag 1 Kundens opgavebeskrivelse (§3 eksisterende softwarefunktionalitet + §3.1.1 kundespecifik)  
**Date:** 18 Sep 2026  
**Method:** Feature-menu assessment against incumbent **cBrain F2** description — **not** a formal krav matrix (none in pack). Confidence **Medium** until `profile:tender-evidence` per row.  
**Equivalence rule:** Opfordringsskrivelse §3.2 — cBrain/F2 references are **"eller tilsvarende"**; tilbud must **godtgøre tilsvarende** where architecture differs.

---

## High scrutiny / likely gaps vs F2 menu (Bilag 1 §3)

| F2 / SBST expectation (Bilag 1) | Fit | Bid risk | Response angle / notes |
|---------------------------------|-----|----------|-------------------------|
| **Desktop-version on PC** (§3.1.1 licensserver: *desktop-version* + mobile; deploy *on-prem … på medarbejdernes pc'er*) | Partial | **Medium–High** | **PC:** browser against on-prem Public 360° (Statens IT). **Mail/journalisering:** Outlook-integration (side panel) per Bilag 1 Outlook-krav — tilsvarende F2 mailflow without a thick F2-style desktop client. §3.1.1 licensserver is **incumbent-specific**, not a generic mindstekrav. **Q&A:** confirm browser + Outlook counts as *tilsvarende* PC-adgang. Evidence: KK architecture (web + Outlook-sidepanel). |
| **AI-assistent via lokal LLM hos Statens It** (akt-niveau: udkast, resume, oversættelse) | Gap / Partial | **High** | Do not assume cloud/SaaS AI. Align to on-prem / customer-controlled inference; Bilag 9 + Bilag 17 tillægspakke B. Scope in afklaringsfase or phased if allowed. |
| **Chat** (informel koordinering uden formelle sagsmapper) | Partial | **Medium** | Teams as official channel vs in-app chat — argue *tilsvarende* samarbejde or gap if chat is mandatory day-one. |
| **Fælles indbakker (unit inboxes)** | Unknown | **Medium** | Verify product/config; no prior art in this scan. |
| **Selvbetjening / registre** | Partial | **Medium** | May touch eManager/OpenGov or process config — clarify in Bilag 3. |
| **Mobil iOS + tablet** (platform list; Bilag 4: **150** mobil + **10** tablet × 72 mdr) | Partial | **Medium** | Priced as separate apps — must match offered mobile/tablet capability; PC ≠ same app story as desktop row above. |
| **Klassificeret miljø** (*Til tjenestebrug*) | Partial | **Medium** | Graded/confidentiality instance (B/K); map labels and hosting to Statens IT zones. |
| **Kundespecifik programmel** (licensserver, analytics datalister, VIAS/CMM Datadoc/Topdesk, legacy arkiv) | Partial | **Medium–High** | Rebuild integrations + Bilag 4 §5 *kundespecifik programmel*; customer **1M DKK** fixed skifteomkostning in eval model. |
| **REST API / Data Transfer Service** (§3 integration menu) | Partial | **Medium** | REST/SIF depth vs cBrain custom API — standard integrations + project for line systems. |
| **Hybrid arbejde** (kontor, hjemme, felt — sikker adgang) | Partial | **Medium** | Browser/VPN + mobile apps; do not imply full offline desktop unless verified. |

---

## Strong alignment (core ESDH — lower scrutiny in §3 narrative)

| Area | Fit | Notes |
|------|-----|--------|
| Sagsstyring & dokumenter, status, frister, samlesager | Met | Core product; DK tender library supports. |
| Outlook / e-mail journalisering | Met | Side panel + Exchange; central to desktop-row equivalence story. |
| Workflows, godkendelser, aktindsigt (process menu) | Met / Partial | Process depth not specified as separate engine in Bilag 1. |
| Arkiv, GDPR, Rigsarkiv (inkl. periodic + extraordinary on switch) | Met | Supplier T&M assistance per Bilag 1. |
| Søg, lister, mapper, nøgleord, audit trail | Met | |
| AD + SSO (ADFS, Statens IT) | Met | On-prem B/K responsibility split in answers. |
| On-prem SQL @ Statens IT, driftsmodel 1A | Met | Bilag 12 split: Statens IT infra; supplier application drift. |

---

## Related artifacts

- Extracted Bilag 1: `extracted/SBST/Bilag 1 Kundens opgavebeskrivelse.txt`
- Source pack: `source/SBST/`
- Prior bid architecture (Outlook): `docs/product/Tender Response - KK - Krav 5.3.2.2.md`
