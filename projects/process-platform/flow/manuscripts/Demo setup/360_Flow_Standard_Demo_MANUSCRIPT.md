# Manuscript — 360° Flow standard demo (application with right of appeal)

| Field | Value |
|-------|--------|
| **Catalogue row** | Standard Flow demo — NVE-style application processing |
| **Audience** | Presales, implementation consultants, product enablement (internal); adaptable for customer-facing with anonymized tenant |
| **Target length** | 20 min (short) / 45 min (standard) / 60 min (with manager view + Q&A) |
| **Language** | **English** (master narrative); run demo in DA/NO/SV/FI using matching wiki asset bundle |
| **Companion wiki** | [360° Flow - Demo setup](https://wiki.software-innovation.com/wiki/360%C2%B0_Flow_-_Demo_setup) — tenant setup, ZIPs, troubleshooting |
| **Platform minimum** | Public 360° **6.12+** (360° Flow GA) |
| **Status** | v1 skeleton — 2026-10-01 |
| **Presenter notes** | `[SAY]` = spoken; `[SHOW]` = screen action; `[SKIP]` = optional or time-boxed out |

---

## 1. Purpose of this manuscript

Wiki **Demo setup** answers *how to install* the demo. This manuscript answers *how to perform* it: story, timing, checklist choreography, and recovery when something breaks.

**Do not** read the wiki aloud. Use this script plus ProcessView in a prepared tenant.

---

## 2. Before you start

### 2.1 Tenant readiness (cross-check wiki)

- [ ] Toggles: `NVE`, `ProcessModelImportExportEnabling`, `EnableChecklistsP360`; **`FFUI.CaseCreation` disabled**
- [ ] Checklist setting active (`checklist.updatechecklist`)
- [ ] Process model imported, **published**, linked to case type / application type used in demo
- [ ] Checklist imported (same language as process model)
- [ ] Document categories active in code table editor: **Major Deficiency letter**, **Decision letter** (99002), **Additional information — significant deficiency** (434), **Klage** (99024); 433 recommended; matching `.dotm` templates imported
- [ ] Process Model Admin: **Application received** / **Review application** — **create email1** shows email template field (demo: none / `#null#`)

### 2.2 Demo case data (fill before session)

| Item | Your tenant value | Notes |
|------|-------------------|--------|
| Case type / application type | | Must match checklist + model scope |
| Applicant contact + case role | | Required for outbound letter/e-mail |
| Sample inbound document (application) | | Optional but helps “review” beat |
| User accounts | Case officer + approver (decision) | Decision process uses review + approval |

### 2.3 Language selection

| Language | Process model file (wiki ZIP) | Checklist file |
|----------|------------------------------|----------------|
| English | `Handle application with right of appeal (English).json` | `Checklist for application processing with right of appeal (English).json` |
| Danish | `Behandle ansøgning m. klageret (Danish).json` | `Tjekliste for ansøgningsbehandling med klageret (Danish).json` |
| Norwegian | `Behandle søknad m_klagerett.json` | `Sjekkliste_for_søknadsbehandling_med_klagerett_….json` |
| Swedish | `Behandla ansökan med överklaganderätt (Swedish).json` | `Checklista för ansökningsbehandling med överklaganderätt (Swedish).json` |
| Finnish | `Käsittele hakemus valitusoikeudella (Finnish).json` | `Tarkistuslista hakemuksen käsittelyyn valitusoikeudella (Finnish).json` |

---

## 3. Audience variants

| Audience | Emphasize | De-emphasize |
|----------|-----------|--------------|
| **Sales / executive** | One model on case, milestones, checklist as compliance story, 28-day phase | PMC argument XML, subprocess innards |
| **Implementation / PS** | Import order, publish, application type scope, template categories, 6.12 email args | Long legal checklist text |
| **Case workers (UAT)** | ProcessView tasks, checklist items, document wizards | Architecture, toggles |

---

## 4. Core story (memorize)

1. **Railway track** — the process model and milestones move the case forward in time.
2. **Inspector** — the checklist defines what must be true at each station; “no” answers justify deficiency paths.
3. **Right of appeal** — checklist items **20–21** + decision letter + appeal deadline milestone.

---

## 5. Standard session — 45 minutes

### Block A — Framing (5 min)

| Time | [SAY] | [SHOW] |
|------|-------|--------|
| 0:00 | “We’ll walk a standard permit-style application with right of appeal — the same scenario our demo assets use across five languages.” | Case list or empty slide |
| 0:02 | “Everything you’ll see lives in **ProcessView**: one process model, phases, parallel processes, checklist, milestones.” | Open case with model linked |
| 0:04 | “The model is the railway track; the checklist is the inspector.” | ProcessView phase overview |

### Block B — Intake (10 min)

| Time | [SAY] | [SHOW] |
|------|-------|--------|
| 0:05 | “First the system confirms receipt — automatic dispatch.” | Run **Automatic confirmation of received application** (if auto-started, point it out) |
| 0:07 | “Formal processing starts when we register receipt and notify the applicant.” | **Application received** — letter + e-mail + milestone |
| 0:09 | “Checklist items 1–3: registered, dated, applicant identified.” | Checklist panel, items 1–3 |
| 0:12 | “If something is missing — e.g. power of attorney — the checklist ‘no’ path is why we’d ask for more.” | [Optional] Item 4 outcome or describe without clicking |

### Block C — Review and deficiency (12 min)

| Time | [SAY] | [SHOW] |
|------|-------|--------|
| 0:15 | “Review is where we judge completeness — minor gap by e-mail, major gap by formal deficiency letter.” | **Review application** |
| 0:17 | “Minor path: e-mail to obtain information.” | Send-mail step (6.12: optional template — demo uses none) |
| 0:20 | “Major path: subprocess with Major Deficiency letter, wait, reminder, final warning.” | [SHOW] **Significant deficiency** subprocess OR [SKIP] if short on time |
| 0:24 | “When the file is ready we mark application complete.” | Milestone / checklist items 8–13 (brief) |

### Block D — Decision and closure (10 min)

| Time | [SAY] | [SHOW] |
|------|-------|--------|
| 0:27 | “Decision is a controlled document: review and approval before dispatch.” | **Decision made** — wizard, `process_decision.dotm` (or locale) |
| 0:30 | “Items 20–21: appeal information and deadline — the right-of-appeal proof.” | Checklist 20–21 |
| 0:33 | “Close verifies checklist completion and sends closure correspondence.” | **Close case processing** |
| 0:35 | “Appeal deadline milestone links to phase 2 if the citizen appeals.” | Milestone timeline OR [SKIP] |

### Block E — Wrap (8 min)

| Time | [SAY] | [SHOW] |
|------|-------|--------|
| 0:37 | “Managers see workload and deadlines when portfolio/worklists are configured.” | [Optional] manager desktop |
| 0:40 | Recap three layers: model, checklist, documents/e-mail | ProcessView |
| 0:43 | Q&A; point to wiki Demo setup for tenant build | — |

---

## 6. Short session — 20 minutes

| Step | Include | [SKIP] |
|------|---------|--------|
| 1 | Framing (2 min) | Manager view |
| 2 | Auto receipt + Application received + checklist 1–3 | Item 4 deep dive |
| 3 | Review — **minor e-mail only** | Major deficiency subprocess |
| 4 | Decision made + checklist 20–21 | Close (mention only) |
| 5 | One-sentence recap | Phase 2 appeal |

---

## 7. Checklist choreography (English IDs)

Use when you want deliberate “no” → deficiency story:

| Checkpoint | Purpose in demo |
|------------|-----------------|
| 1–3 | Intake with **Application received** |
| 4 | Power of attorney — trigger for deficiency narrative |
| 7 | Sufficient case file (untagged — preparation) |
| 14–19 | Decision quality (brief) |
| **20–21** | **Right of appeal — must show** |
| 23–25 | Closure with **Close case processing** |

---

## 8. Failure playbook

| Symptom | Likely cause | Recovery [SAY] |
|---------|--------------|----------------|
| `Missing arguments (EmailMessageTemplateRecno1)` | Old process model or blank template arg | “We need the 6.12 demo bundle published — I’ll use a fresh case.” Switch case or reschedule after re-import |
| Checklist empty | Setting / scope | Wiki troubleshooting — checklist.updatechecklist, application type |
| Wrong UI for new case | `FFUI.CaseCreation` on | Wiki setup — toggle off for this demo |
| Process not listed | Model not published / not linked | PMC publish + case type mapping |
| Approver step blocked | No approver user | Pre-create user with rights; or skip approval in dry-run tenant |

---

## 9. Process name map (English → localized display names)

Fill from wiki process model titles when presenting in non-English:

| English (EN) | Danish (DA) | Norwegian (NO) | Swedish (SV) | Finnish (FI) |
|--------------|-------------|----------------|--------------|--------------|
| Process application with right of appeal | Behandle ansøgning m. klageret | Behandle søknad m/klagerett | Behandla ansökan med överklaganderätt | Käsittele hakemus valitusoikeudella |
| Application received | Ansøgning modtaget | Mottatt søknad | Ansökan mottagen | Hakemus vastaanotettu |
| Review application | Kontroller ansøgning | Kontroller søknad | Granska ansökan | Tarkista hakemus |
| Decision made | Afgørelse truffet | Vedtak fattet | Beslut fattat | Päätös tehty |
| Close case processing | Afslut sagsbehandling | Avslutt saksbehandling | Avsluta ärendebehandling | Sulje asian käsittely |
| Request for additional documentation - Significant deficiency | (see tenant / model) | (see tenant / model) | (see tenant / model) | (see tenant / model) |

---

## 10. Recording / customer-facing hygiene

- Use a **demo tenant**; no real citizen data
- Blur case numbers, names, org numbers in screenshots
- Do not promise features outside [[360° Flow]] / 6.12 GA scope without checking module page

---

## 11. Revision log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| v1 skeleton | 2026-10-01 | | Initial structure; 6.12 email note; links to wiki draft refresh |

---

## 12. TODO (next manuscript iteration)

- [ ] Add anonymized screenshot asset IDs (ProcessView, checklist, document wizard, e-mail dialog)
- [ ] Localized [SAY] paragraphs for DA/NO (optional appendix)
- [ ] Align checkpoint 22 wording after checklist copy-edit ships
- [ ] Optional email message template demo beat (if tenant gets codetable presets)
