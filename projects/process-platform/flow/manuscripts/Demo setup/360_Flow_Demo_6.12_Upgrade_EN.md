# 360° Flow demo assets — 6.12 upgrade (English first)

**Scope:** English process model + checklist in `manuscripts/Demo setup/`. After sign-off, regenerate locales from English:

```powershell
uv run python toolkit/scripts/build_localized_flow_demo_process_models.py
# or: .\projects\process-platform\flow\manuscripts\Demo` setup\Build-TranslatedProcessModels.ps1
```

**Reference:** Wiki [6.12 release information](https://wiki.software-innovation.com/wiki/6.12_release_information) — Process Platform note: work unit registry **`ms_6.12.0`** (consolidated argument layout). Validate stage process configuration after upgrade.

---

## Process model — gap analysis (English export vs 6.12 `.wu` registry)

Compared repo demo JSON to standard work units in `te-industry-public360` … `WorkUnits/FlowWorkUnits/StandardProcesses/`.

| Stage process | Work unit | 6.12 registry file | Required change |
|---------------|-----------|-------------------|-----------------|
| Application received, Review application, Close case processing | `E1A5B6C7-…` | `FinalProcessing.wu` | Add **`EmailMessageTemplateRecno1`** (optional email template); use category **`create email1`** (not `Create email 1`). Preserve existing demo values (titles, milestone IDs, recipients/attachments). |
| Decision made | `89e0ed8c-…` | `HearingProcess.wu` | **No argument schema change** — names and order already match. |
| Significant deficiency | `9E7A8B38-…` | `MajorDeficiencyLetter.wu` | **Reorder** `SendExpiryReminder` **before** `DeadlineDays` (registry order; same values). |
| Auto receipt | `10C6E5A9-…` | `AutoReceipt.wu` | No change detected. |
| Appeal phase — Application received | `6F8C2A1B-…` | `CreateSingleDocument.wu` | No change detected. |

### Create-email component (what changed)

6.12 **`FinalProcessing`** send-mail block argument order:

1. `ShowEmailDialogue1`
2. `EmailActivityTitle1`
3. **`EmailMessageTemplateRecno1`** ← **new in registry** (optional preset from code table *Email message*)
4. `ShowRecipients1`
5. `ShowAttatchments1`
6. `EmailMilestoneTrigger1`
7. `EmailMilestoneAutomationId1`

Demo processes that use email today:

- **Application received** — letter + email + milestone *Application received*
- **Review application** — email *Obtain information — minor deficiency* (optional major-deficiency subprocess)
- **Close case processing** — checkpoint + closure correspondence (email block present in WU; document/checkpoint toggles per demo)

**Recommendation:** Set template recno to **`#null#`** when no preset template (required at runtime — empty string is treated as *missing*). Configure a real recno in PMC only if you add English *Email message* templates in the demo tenant.

---

## Automation

From repo root:

```powershell
uv run python toolkit/scripts/upgrade_english_flow_demo_612.py
uv run python toolkit/scripts/diff_demo_wu_vs_registry.py
```

Expect **no MISSING** for `FinalProcessing` / `MajorDeficiencyLetter` after patch.

---

## Checklist — should we change it?

**Process / schema:** No 6.12 release note implies a new checklist export format. Milestone tags (`99001`, `217`, `218`, …) stay tied to the **process model milestone types** in the same JSON bundle — update checklist only if milestone types or application type change.

**Content review (recommended, not blocking import):**

| Item | Issue | Suggested action |
|------|--------|------------------|
| Checkpoint **22** | Name merges two sections: *"Information about the right of access… 8. Archiving and follow-up"* | Split/fix title when editing checklist (copy-edit only). |
| Items **20–21** | Appeal information | Keep — still the demo proof points for *right of appeal*. |
| Email template (optional) | If demo uses preset email templates in 6.12 | Add checkpoint under *Decision made* or *Application received*: e.g. *"Outgoing email uses approved message template (if configured)."* — **only if** you configure `EmailMessageTemplateRecno1` in the process. |

**Recommendation:** Ship **process model 6.12 patch first**; import checklist unchanged; fix checkpoint 22 text in a **second pass** after one successful 6.12 tenant test.

---

## Test plan (English, 6.12 tenant)

1. Import patched `Handle application with right of appeal (English).json` → publish.
2. Import existing English checklist (unchanged).
3. Walkthrough: auto receipt → application received (email + milestone) → review (minor deficiency email) → significant deficiency subprocess → decision → close.
4. In Process Model Admin, open **Application received** / **Review application** — confirm **create email1** group shows template field without errors.
5. If clean, regenerate other languages and wiki ZIPs (`Upload-DemoAssetsToWiki.ps1`).

---

## Wiki / enablement (later)

- Bump [360° Flow - Demo setup](https://wiki.software-innovation.com/wiki/360%C2%B0_Flow_-_Demo_setup): prerequisites **6.12+**, note optional email message templates.
- Update `360_Flow_Demo_Setup_DRAFT.md` when wiki is edited.

---

## Process model version 9 (phase deadline calculation)

Appeal processing (phase 2) uses **`ToDeadlineCalculationType` 27** — *Calculate from start/end milestones* — same as phase 1 (was default calculation type 10).

---

## Process model version 8 (consultant test corrections)

Applied via `toolkit/scripts/apply_consultant_corrections_flow_demo.py` (then regenerate locales).

| Area | Change |
|------|--------|
| Milestones *Additional information received* (both configs) | Milestone type **203** (*Additional documentation received* / NO: *Tilleggsdokumentasjon mottatt*). Trigger categories **433 + 434** (incoming minor/significant supplementary information). |
| Milestone *Additional information requested - minor deficiency* | Trigger category **437** (outgoing minor deficiency letter). |
| Milestone *Appeal received* (phase 2) | Trigger category **99024** (*Klage*). |
| Major deficiency letter | First reminder **`Expired_DocumentCategory` = 438** (significant deficiency letter, not 437). |
| Auto receipt | **`DocumentTemplateId` = `#null#`**, **`DispatchDocument` = false** (matches `AutoReceipt.wu` / NVE reference). |
