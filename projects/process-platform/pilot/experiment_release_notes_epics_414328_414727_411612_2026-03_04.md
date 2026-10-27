# Draft release overview — PAF (combined epics)

> **Disclaimer:** This document is an **automated draft** generated from Azure DevOps work items (English, customer-facing wording). It is **not** a signed-off release communication. Internal fields, attachment links, and assignee identities from the work tracking system are intentionally omitted.

**Scope:** Deliveries discovered by **walking the work-item tree**: starting from each epic, every item reachable by repeating **`Hierarchy-Forward`** (parent → child) links was collected. **Related**, **Duplicate**, **Successor**, and other non-hierarchy links were **not** traversed. For each qualifying item, **title, description, and acceptance criteria** were read in Azure DevOps, and **Development** links (**ArtifactLink** → GitHub Pull Request / Commit) were resolved where present.

| Epic | Title |
| --- | --- |
| [414328](https://dev.azure.com/tieto-si/360/_workitems/edit/414328) | PAF – Standard Artifacts |
| [414727](https://dev.azure.com/tieto-si/360/_workitems/edit/414727) | PAF – User Experience (UX) |
| [411612](https://dev.azure.com/tieto-si/360/_workitems/edit/411612) | PAF – NVE Pilot |

**Selection rules:**

- **States included:** **Resolved** and **Closed** only.
- **Release timestamp:** **Resolved** → `Microsoft.VSTS.Common.ResolvedDate` (**ResolvedDate**). **Closed** → `Microsoft.VSTS.Common.ClosedDate` (**ClosedDate**).
- **Time window:** **March 2026** or **April 2026** (UTC calendar month of that timestamp).

**Program context:** These epics roll up under **Process Automation Framework (PAF)** ([epic 414623](https://dev.azure.com/tieto-si/360/_workitems/edit/414623)).

---

## Data access note (GitHub)

The **GitHub** integration used here is authorised for **`te-industry-public360`**. Pull-request **state** (open / closed) and **merged** status were read from the GitHub API for repository **[`te-industry-public360/core-bl`](https://github.com/te-industry-public360/core-bl)** on **17 April 2026**.

**Caveats for release owners:** Azure DevOps **Development** links encode a **service connection** and **PR number**. The same PR number can exist only once per repo, but the **connection GUID** on the work item does not always map to the repository you assume. Where GitHub **title/body** disagree with the story, or **`get_pull_request` returns 404** for `core-bl`, treat the link as **traceability debt** until Engineering corrects **Development** or confirms the correct repo (for example ProcessEngineToolkit or another GitHub project).

---

## Evidence and methodology (including tests)

**Goal:** Describe **observable behaviour** for release readers, not implementation detail. Prefer sources in this order, and **merge** them when they agree; when they disagree, say so explicitly.

1. **Azure DevOps — work item** — Title, description, acceptance criteria, and **parent** links set the intended scope.
2. **Azure DevOps — test cases** — Use **Links** (*Tested By*, suites, plans) from the story outward, not only **Development** → GitHub.
3. **GitHub — merged change** — Resolve **repo + PR** from Development, then read merge state and PR title/body.
4. **GitHub — automated tests** — Scan added/modified test files on the PR when you need behaviour detail.
5. **Gap handling** — Where ADO, tests, and GitHub disagree, or GitHub has no tests, call out **traceability or coverage debt**.

**What this combined draft used:** Hierarchy traversal and date/state filtering in ADO; work-item **titles** (and, for overlapping items, the longer narratives from the single-epic experiment **[`experiment_release_notes_epic_414328_2026-03_04.md`](./experiment_release_notes_epic_414328_2026-03_04.md)**); **Development** links where captured; **GitHub API** metadata for `core-bl` PRs listed below. It did **not** systematically attach **ADO Test Case** steps to every story.

---

## Summary counts

| Epic | Qualifying items (Mar/Apr 2026, Resolved/Closed) |
| --- | ---: |
| 414328 — PAF – Standard Artifacts | 24 |
| 414727 — PAF – User Experience (UX) | 1 |
| 411612 — PAF – NVE Pilot | 0 |
| **Total** | **25** |

The headline counts include **Features**, **User Stories**, and **Tasks** that met the rule, not user stories alone. Under **411612**, descendants were **New** or **Active** at export — none met Resolved/Closed with a Mar/Apr 2026 release timestamp.

---

## Epic 414328 — PAF – Standard Artifacts

Structure: **Feature** (parent under epic) → **User Story** (and **Tasks** where they add delivery context).

### PAF – Artifacts – Shortcoming status ([415991](https://dev.azure.com/tieto-si/360/_workitems/edit/415991))

#### [415992](https://dev.azure.com/tieto-si/360/_workitems/edit/415992) — *add shorcmong statuses* (Closed; release **2026-03-25**, ClosedDate)

**What it does:** Adds standard **shortcoming status** values so cases and reporting can classify shortcomings consistently across environments.

**Linked engineering (Development → GitHub):** The work item’s GitHub link points at [`core-bl` PR #9370](https://github.com/te-industry-public360/core-bl/pull/9370) — **closed**, **merged** (GitHub title: *Added log for signing off document while document creation*, 2023). That change is **audit logging at document creation**, not catalogue seeding for **shortcoming status**. **Reconcile** Development before customer-facing text.

---

### PAF – Artifacts – Condition status values ([415993](https://dev.azure.com/tieto-si/360/_workitems/edit/415993))

#### [415994](https://dev.azure.com/tieto-si/360/_workitems/edit/415994) — *add condition statuses* (Closed; **2026-03-25**)

**What it does:** Adds standard **condition status** values for consistent process and reporting language.

**Linked engineering:** Same **`core-bl` PR [#9370](https://github.com/te-industry-public360/core-bl/pull/9370)** as above — **merged**, but **semantically misaligned** with the story title (sign-off logging, not condition statuses).

---

### PAF – Artifacts – Document categories ([415996](https://dev.azure.com/tieto-si/360/_workitems/edit/415996))

#### [415997](https://dev.azure.com/tieto-si/360/_workitems/edit/415997) — *Add document categories* (Resolved; **2026-04-17**)

**What it does:** Extends or standardises **document categories** used with PAF artefacts so outgoing/incoming document handling stays aligned with your taxonomy (exact fields: see ADO description and acceptance criteria).

**Linked engineering:** **Not verified in GitHub** in this pass — open the work item’s **Development** section in Azure DevOps and map each PR to the correct repository before release notes go external.

---

### PAF – Artifacts – Process Definitions ([400794](https://dev.azure.com/tieto-si/360/_workitems/edit/400794))

#### [414799](https://dev.azure.com/tieto-si/360/_workitems/edit/414799) — *Add Application Master as an example in ProcessEngineToolkit* (Closed; **2026-03-20**)

**What it does:** Delivers an **Application Master** sample or documentation path in **ProcessEngineToolkit** so implementers can copy a known-good pattern (see ADO for scope).

**Linked engineering:** ADO **Development** commonly surfaces **`core-bl` PR [#19](https://github.com/te-industry-public360/core-bl/pull/19)** — **closed**, **merged** (GitHub: *Fixed Newtonsoftversion issue*, **2019**). That is **not** an Application Master example in this repository. A **different connection/repo** (or PR number under ProcessEngineToolkit) may be intended — **do not** cite `core-bl` #19 as proof of this story without re-linking.

#### [416108](https://dev.azure.com/tieto-si/360/_workitems/edit/416108) — *Invoke subprocess as server action* (Closed; **2026-03-25**)

**What it does:** Adds a **Create subprocess** server action so a running process can start a **child process** on the current case progression, with options for **child title**, **responsibility** handling, and a noted **future** “deadline after N days” area not yet fully implemented (see single-epic draft for full behaviour paragraph).

**Linked engineering:** [`core-bl` PR #19476](https://github.com/te-industry-public360/core-bl/pull/19476) — **closed**, **merged** **2026-03-24** (*Server Action for CreateSubProcess and dorrect SetResponsibe method*; body references AB#416108).

#### [414618](https://dev.azure.com/tieto-si/360/_workitems/edit/414618) — *Create documment with review and approval* (Resolved; **2026-04-07**)

**What it does:** Ships a **standard document-creation** progress-plan model: stages for **document setup**, optional **review**, **approval**, **dispatch**, and **milestone** registration, driven by configuration comments in the shipped `.wu` / process package (see [`experiment_release_notes_epic_414328_2026-03_04.md`](./experiment_release_notes_epic_414328_2026-03_04.md) for the long-form “what it does”).

**Linked engineering:** [`core-bl` PR #19591](https://github.com/te-industry-public360/core-bl/pull/19591) — **closed**, **merged** **2026-04-14** (*First Draft Version Of Document Process Handling…*); follow-up [`#19753`](https://github.com/te-industry-public360/core-bl/pull/19753) — **closed**, **merged** **2026-04-17** (*Added updated version for the Creation and withdrawal process…*). Both reference AB#414618 / AB#414862 in the PR body.

#### [414862](https://dev.azure.com/tieto-si/360/_workitems/edit/414862) — *Process Withdrawn* (Resolved; **2026-04-17**)

**What it does:** Standard **withdrawn-document** process mirroring creation setup (roles, archive, category, headers, template) with optional **review**, **approval**, **dispatch**, and **milestone** fields tuned for withdrawal (single-epic draft).

**Linked engineering:** Same **`core-bl` PRs [#19591](https://github.com/te-industry-public360/core-bl/pull/19591)** and **[#19753](https://github.com/te-industry-public360/core-bl/pull/19753)** as **414618** (merged as above).

---

### PAF – Artifacts – Standard Checklist ([414351](https://dev.azure.com/tieto-si/360/_workitems/edit/414351))

#### [414620](https://dev.azure.com/tieto-si/360/_workitems/edit/414620) — *Add default outcome types* (Closed; **2026-03-27**)

**What it does:** Intended to add **default checklist outcome types** for consistent checklist configuration.

**Linked engineering:** [`core-bl` PR #9371](https://github.com/te-industry-public360/core-bl/pull/9371) — **closed**, **merged** **2023** (*Removed [(DocumentArchive)] macro from API code which is not required*). **Mismatch** with checklist outcomes — correct Development or add the real repo/PR.

---

### PAF – Artifacts – Standard Milestones ([414516](https://dev.azure.com/tieto-si/360/_workitems/edit/414516))

#### [414619](https://dev.azure.com/tieto-si/360/_workitems/edit/414619) — *PMC - DB - Add standard milestones* (Closed; **2026-03-25**)

**What it does:** Umbrella for **database / backend** milestone catalog and behaviour (ordering, IFAR-related rules, etc.); see single-epic draft for the **multi-PR** breakdown.

**Linked engineering (examples on the work item):** [`core-bl` #9367](https://github.com/te-industry-public360/core-bl/pull/9367), [#9369](https://github.com/te-industry-public360/core-bl/pull/9369), [#9372](https://github.com/te-industry-public360/core-bl/pull/9372), [#9419](https://github.com/te-industry-public360/core-bl/pull/9419) — all **historically merged**; confirm which links still belong to this story after backlog grooming.

#### [414964](https://dev.azure.com/tieto-si/360/_workitems/edit/414964) — *PMC - DB - Expire required Case Type on MilestoneTypes* (Closed; **2026-04-13**)

**What it does:** Combines milestone-type ordering / backend fixes with **SDP v2 return-address validation** and a **closed-without-merge** then **merged** pair on related methods (see single-epic draft § PMC – DB – Expire required Case Type…).

**Linked engineering:** [`core-bl` #9372](https://github.com/te-industry-public360/core-bl/pull/9372), [#9402](https://github.com/te-industry-public360/core-bl/pull/9402), [#19536](https://github.com/te-industry-public360/core-bl/pull/19536) (merged: **No** per prior appendix), [#19538](https://github.com/te-industry-public360/core-bl/pull/19538) (**merged**).

---

### PAF – Artifacts – Milestone status ([415983](https://dev.azure.com/tieto-si/360/_workitems/edit/415983))

#### [415985](https://dev.azure.com/tieto-si/360/_workitems/edit/415985) — *Add standard milestone status* (Closed; **2026-03-25**)

**What it does:** Adds a **standard milestone status** set for consistent milestone reporting across environments.

**Linked engineering:** **No GitHub Pull Request** was present on this user story in the Development export used for this draft.

---

### PAF – Artifacts – Contact - Case roles ([415986](https://dev.azure.com/tieto-si/360/_workitems/edit/415986))

#### [415988](https://dev.azure.com/tieto-si/360/_workitems/edit/415988) — *Add standard contact - case roles* (Closed; **2026-03-26**)

**What it does:** Intended to add or harmonise **contact–case role** catalogue entries.

**Linked engineering:** [`core-bl` PR #9370](https://github.com/te-industry-public360/core-bl/pull/9370) — **merged**, **sign-off logging at document creation** — **misaligned** with contact–case roles (same traceability issue as 415992 / 415994).

---

### PAF – Artifacts – ProcessEngine - Designer Components ([414353](https://dev.azure.com/tieto-si/360/_workitems/edit/414353))

#### [230795](https://dev.azure.com/tieto-si/360/_workitems/edit/230795) — *PE Designer Component - Create a Stage* (Closed; **2026-03-19**)

**What it does:** First-class **“create stage”** designer component so case handling can advance through stages without always spawning separate processes (summary from work-item intent).

**Linked engineering:** **No Pull Request** on the story in the export used here.

#### [414997](https://dev.azure.com/tieto-si/360/_workitems/edit/414997) — *PE Designer Component - Create a Milestone Dialog in Case Handling view* (Resolved; **2026-03-24**)

**What it does:** **Milestone creation** UX in case handling driven by the process definition (labels, optional status, custom naming, dates — see ADO acceptance criteria).

**Linked engineering:** [`core-bl` PR #14132](https://github.com/te-industry-public360/core-bl/pull/14132) — **closed**, **merged** **2024** (*Add Surface callable method for IsFileFormatBlacklisted*). **Semantic mismatch** with milestone dialog — validate Development link.

**Tasks (same feature area):**

- [415238](https://dev.azure.com/tieto-si/360/_workitems/edit/415238) — *Task: Analyse existing code* (Closed; **2026-03-24**)
- [415240](https://dev.azure.com/tieto-si/360/_workitems/edit/415240) — *Task: Implement dialog* (Closed; **2026-03-24**)

#### [415772](https://dev.azure.com/tieto-si/360/_workitems/edit/415772) — *Support Stage pre-selection in New Document Wizard and Dialog when opened from Process Engine client action* (Closed; **2026-04-16**)

**What it does:** Passes **stage context** into the **New document** wizard / document dialog when opened from a Process Engine client action so downstream steps can respect the **active case stage** (see single-epic draft).

**Linked engineering:** [`core-bl` PR #19718](https://github.com/te-industry-public360/core-bl/pull/19718) — **open** **2026-04-16** (*BL Document Dialog, the ProcessDataOnInvoker is missing the stage Rec…*; body references AB#415772, AB#419364). **Not merged** at GitHub snapshot — confirm branch/merge with Engineering before calling this “released”.

**Tasks:**

- [419343](https://dev.azure.com/tieto-si/360/_workitems/edit/419343) — *Task: Analysis* (Closed; **2026-04-16**)
- [419364](https://dev.azure.com/tieto-si/360/_workitems/edit/419364) — *Task: BL change* (Closed; **2026-04-16**)

---

## Epic 414727 — PAF – User Experience (UX)

### PMC - Admin - Stage defined Process - Select Workflow definition ([410828](https://dev.azure.com/tieto-si/360/_workitems/edit/410828))

#### [416667](https://dev.azure.com/tieto-si/360/_workitems/edit/416667) — *UI - Admin panel - Create Extended Search Dialog for Workflow Definition Dropdown in Process Property* (Closed; ClosedDate **2026-04-08**; ResolvedDate **2026-04-02**)

**What it does:** Adds an **extended search** dialog when choosing a **workflow definition** in process properties in the admin experience, so long lists are manageable (see ADO for UX acceptance criteria).

**Linked engineering:** Development listed **`core-bl` PR [#14208](https://github.com/te-industry-public360/core-bl/pull/14208)** — **closed**, **merged** **2024** (*Dont index unoff fields in PR* — unrelated admin UI). **`core-bl` PR #14221** returned **404** via the GitHub API — wrong repo or removed PR. **Traceability gap:** fix links or identify the correct front-end repository.

---

## Epic 411612 — PAF – NVE Pilot

No descendant work items met **Resolved** or **Closed** with **ResolvedDate** / **ClosedDate** in **March or April 2026**.

---

## Appendix — `core-bl` PR verification (17 April 2026)

PR metadata below is from **`te-industry-public360/core-bl`** only. **Merged** follows GitHub’s merge indicator.

| PR | State | Merged | Title (GitHub) |
|----|--------|--------|----------------|
| [19](https://github.com/te-industry-public360/core-bl/pull/19) | closed | Yes | Fixed Newtonsoftversion issue |
| [9370](https://github.com/te-industry-public360/core-bl/pull/9370) | closed | Yes | Added log for signing off document while document creation |
| [9371](https://github.com/te-industry-public360/core-bl/pull/9371) | closed | Yes | Removed [(DocumentArchive)] macro from API code which is not required |
| [14132](https://github.com/te-industry-public360/core-bl/pull/14132) | closed | Yes | Add Surface callable method for IsFileFormatBlacklisted |
| [14208](https://github.com/te-industry-public360/core-bl/pull/14208) | closed | Yes | Dont index unoff fields in PR |
| [19476](https://github.com/te-industry-public360/core-bl/pull/19476) | closed | Yes | Server Action for CreateSubProcess and dorrect SetResponsibe method |
| [19591](https://github.com/te-industry-public360/core-bl/pull/19591) | closed | Yes | First Draft Version Of Document Process Handling Including Creation and Withdrawn |
| [19718](https://github.com/te-industry-public360/core-bl/pull/19718) | open | **No** | BL Document Dialog, the ProcessDataOnInvoker is missing the stage Rec… |
| [19753](https://github.com/te-industry-public360/core-bl/pull/19753) | closed | Yes | Added updated version for the Creation and withdrawal process along with shared component. |

**Not found on `core-bl` at this snapshot:** PR **14221** (404).

---

## Notable exclusions (examples)

- **Closed outside Mar/Apr 2026** — e.g. [399013](https://dev.azure.com/tieto-si/360/_workitems/edit/399013) (Closed **2026-02-12**), [410185](https://dev.azure.com/tieto-si/360/_workitems/edit/410185) (Closed **2026-02-13**), [409878](https://dev.azure.com/tieto-si/360/_workitems/edit/409878) (Closed **2026-02-26**).
- **Closed before 2026** — stories under archived **“Create new process”** feature [230801](https://dev.azure.com/tieto-si/360/_workitems/edit/230801) ([246950](https://dev.azure.com/tieto-si/360/_workitems/edit/246950), [249157](https://dev.azure.com/tieto-si/360/_workitems/edit/249157)) closed in **2023**.

---

_End of combined experiment — hierarchy + Development links + GitHub verification for internal evaluation._
