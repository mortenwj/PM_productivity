# KK KLE support — scope note (minimum vs parity vs full lift)

**Audience:** Anita Odsbjerg Pedersen, Jarle Steira, bid/gate stakeholders  
**Purpose:** Size the work to move KLE from eDoc to Public 360° for Københavns Kommune (KK)  
**Date:** 27 Aug 2026  
**Sources:** eDoc `eDoc-eDoc` (Emneord / ClassificationPlan), ADO [#387587](https://dev.azure.com/tieto-si/360/_workitems/edit/387587), [#430983](https://dev.azure.com/tieto-si/360/_workitems/edit/430983), KK tender drafts (klassifikation / kodetabeller)

---

## Executive summary

KLE in eDoc is **not** a thin “import a spreadsheet + lookup” integration. It is a **Danish-specific classification stack**: automated sync from FK/KOMBIT, hierarchical emneplan + handlingsfacetter, disposal/scrap codes, access sensitivity, and case-registration field logic.

Public 360° **already has** the generic classification model (class types, hierarchical class codes, admin, case/document pickers, retention/disposal tied to classification). The lift work is therefore:

1. **Getting KLE data into P360** (once or continuously), and  
2. **Configuring KK to use it** (case types, FFUI, archive/disposal rules).

**Do not treat this as a small task** unless the bid explicitly limits scope to Tier 1 below.

---

## What eDoc does today (reference)

| Component | eDoc location | Function |
|-----------|---------------|----------|
| FK nightly sync | `FuBatchClassificationPlanJob` / `Fujitsu.eDoc.STS.ClassificationPlan` | Pull KLE hierarchy from FK KlassifikationSystem (WCF + STS cert); create/update emneplan (3 levels) + handlingsfacetter in classification tables |
| Scrap/disposal codes | `FuBatchScrapCodeJob` / `Fujitsu.eDoc.ScrapCode` | Pull kassationskoder from kle-online.dk XML; update class codes |
| Access sync | `UseraccessKLESyncRepository` | Stored proc sync of KLE-related access groups |
| Case UX | FFUI / eDoc views + UserAccess integration | Emne/facet pickers, field dependencies, KLE sensitivity, links to kle-online.dk |

Production issue [#430983](https://dev.azure.com/tieto-si/360/_workitems/edit/430983): sync **fails on hierarchy edge cases** (“Parent does not exist”) — fix required for any automated tier.

P360 lift tracker: [#387587](https://dev.azure.com/tieto-si/360/_workitems/edit/387587) — **two explicit parts:** (1) integration, (2) use in case creation incl. field relations. ~21 child stories closed (Part 1 dev), feature still **New**, code **not on `core-bl` master** in local clones (PRs #5250 / #5326).

---

## Three scope tiers for KK

### Tier 1 — Minimum viable (bid-friendly baseline)

**Promise:** KK can classify cases/documents with **valid KLE emneplan and handlingsfacetter** using standard P360 classification UI. Values are **correct at go-live**; ongoing FK updates are handled manually or via existing classification export/import until automated sync ships.

| In scope | Out of scope |
|----------|--------------|
| One-time (or periodic manual) load of KLE tree into P360 classification types/codes | Automated FK nightly job in production |
| KK archive setup: emneplan + facet class types mapped to P360 model | KLE-Online scrap-code auto-sync job |
| Standard class-code pickers on configured case types | KLE-specific access-group auto-sync |
| Administrator maintenance of codes in WebAdmin | KLE-online deep links in UI |
| Validation that chosen codes exist in tree (standard P360) | Full eDoc field-logic parity |
| Disposal/retention **configured** on classification (manual/scrap codes set per admin process) | Fixing [#430983](https://dev.azure.com/tieto-si/360/_workitems/edit/430983) in product |

**Rough effort:** **15–25 man-days**  
(config + test + one import cycle + KK case-type/archive workshop; assumes classification export/import or controlled manual entry path exists)

**Tender language:** *“Systemet understøtter KLE via standard klassifikationssystem. KLE-værdier etableres og vedligeholdes i klassifikationssystemet; automatisk synkronisering mod FK kan leveres som del af produktroadmap (#387587).”*

**Risk:** FK publishes new KLE numbers between import and automated sync go-live → **operational gap** unless manual process agreed with customer.

---

### Tier 2 — Operational parity (recommended for KK if they use eDoc sync today)

**Promise:** Tier 1 **plus** automated ongoing sync from FK/KOMBIT (equivalent to eDoc nightly job), monitored and hardened for known failure modes.

| In scope | Out of scope |
|----------|--------------|
| Everything in Tier 1 | KLE-Online scrap-code job (unless added) |
| P360 nightly job: STS cert/token, FK WCF fetch, hierarchical upsert into classification tables | Full UserAccess KLE sensitivity parity |
| Job configuration (property values, certificates, scheduling) | KLE-online UX links |
| Error logging + ops runbook ([#429634](https://dev.azure.com/tieto-si/360/_workitems/edit/429634) direction) | Part 2 case-registration field logic (separate FFUI work) |
| Fix/harden hierarchy handling ([#430983](https://dev.azure.com/tieto-si/360/_workitems/edit/430983)) | |
| Merge/release of #387587 Part 1 work to product line used by KK | |

**Rough effort:** **40–60 man-days** incremental on top of Tier 1  
(Part 1 largely built in ADO; remaining = hardening, release, env/cert setup, UAT, KK cutover — **not** greenfield)

**Note:** Internal dev investment under #387587 already reflects this magnitude (~21 closed stories). Treat Tier 2 as **finish + ship + validate**, not “copy eDoc in a week.”

**Tender language:** *“Løsningen synchroniserer klassifikationssystemet med FK/KLE (KL Emnesystematik) via et planlagt baggrundsjob, svarende til etableret eDoc-praksis.”*

---

### Tier 3 — Full eDoc parity

**Promise:** Tier 2 **plus** scrap-code sync, KLE access/sensitivity behaviour, registration UX (emne ↔ facet logic), and KLE-online guidance links — matching what Danish eDoc municipalities expect from Emneord stack.

| In scope | Out of scope |
|----------|--------------|
| Everything in Tier 2 | Unrelated KK PFRs (SIEM, Flow, GIS, etc.) |
| `FuBatchScrapCodeJob` equivalent → disposal codes on class codes | |
| UserAccess / KLE sensitivity rules (or agreed P360-native substitute) | |
| #387587 **Part 2:** FFUI field dependencies on KK case types | |
| KLE-online links from registration UI | |
| Regression suite for FK + kle-online schema changes | |

**Rough effort:** **+30–50 man-days** on top of Tier 2  
(**70–110 man-days** total from zero; less if Tier 2 already delivered)

**Tender language:** Only commit if product confirms Part 2 and scrap/access items in KK go-live plan.

---

## KK tender — how requirements map

| KK / tender theme | Tier 1 | Tier 2 | Tier 3 |
|-------------------|--------|--------|--------|
| Kodetabeller / klassifikation (5.3.3.1.1) | Met via standard P360 | Met | Met |
| Kassation/bevaring knyttet til klassifikation (5.3.7.2) | Met if scrap codes configured | Partial auto | Full auto (kle-online job) |
| “KLE support” (implicit for DK eDoc customers) | Functional at go-live | Operational sync | eDoc-equivalent |
| Data quality / external registers (5.3.3.1.1) | Manual maintenance | FK as register | FK + kle-online |

KK tender PFR query ([#434005](https://dev.azure.com/tieto-si/360/_workitems/edit/434005) portfolio) does **not** list #387587 — treat KLE as **eDoc migration / DK baseline**, not a separate KK PFR line, unless explicitly added to bid baseline.

---

## Recommendation for gate / bid

| Decision | Suggested tier |
|----------|----------------|
| KK must match **current eDoc automated KLE updates** before/at migration | **Tier 2 minimum** |
| Bid needs **lowest commitment**; accept manual KLE maintenance short term | **Tier 1** (document operational risk) |
| KK expects **same registration UX and disposal automation as eDoc** | **Tier 3** |

**Default for Copenhagen:** Plan **Tier 2** for implementation budget; write tender text so Tier 1 is defensible but Tier 2 is the **intended** delivery. Reserve Tier 3 for explicit customer ask or post-go-live wave.

---

## Open questions for Anita / Jarle (sign-off)

1. Does KK contractually require **automated FK sync**, or only **KLE-capable classification**?
2. Is #387587 Part 1 targeted for **KK go-live** or **Ringkøbing-Skjern / generic DK** first?
3. Are **scrap codes** (kle-online job) in KK archive compliance scope, or handled by admin import?
4. Is **KLE sensitivity / access groups** in scope for KK, or covered by separate access-code / data-delimitation work ([#434352](https://dev.azure.com/tieto-si/360/_workitems/edit/434352))?
5. Who owns **Part 2** (case-type FFUI) — product (#387587) or KK implementation project?

---

## References

- **eDoc repo:** `https://github.com/te-industry-public360/eDoc-eDoc` → `5.0/Source/Emneord/Fujitsu.eDoc.STS.ClassificationPlan/`
- **P360 feature:** [#387587](https://dev.azure.com/tieto-si/360/_workitems/edit/387587) Integration with classification system KLE
- **Production bug:** [#430983](https://dev.azure.com/tieto-si/360/_workitems/edit/430983) New KLE numbers not inserted in eDoc
- **Related DK classification:** [#387370](https://dev.azure.com/tieto-si/360/_workitems/edit/387370) FKK integration (separate system)
- **People:** Rajdeep Majumder (KLE lift dev), Brian Rasmussen / Jan Kammersgaard (eDoc ops), Jarle Steira (DK product)
