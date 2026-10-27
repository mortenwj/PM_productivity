# Refresh NVE «behov – DevOps status» Excel from Azure DevOps

Instructions for updating the NVE tracking workbook **in place** (keeps colors, column widths, and layout). Written for use with **Claude** and the **Azure DevOps MCP** (`user-azure-devops` or equivalent).

---

## What this does

Updates these columns from live DevOps (project **360**):

| Column | Source |
|--------|--------|
| Work item type | `System.WorkItemType` |
| DevOps link | Label + hyperlink (`https://dev.azure.com/tieto-si/360/_workitems/edit/{id}`) |
| ADO Status | `System.State` |
| Sprint | `System.IterationPath` (shows **Ingen sprint** for team backlog) |
| Tags | `System.Tags` |
| Opprettet / Sist oppdatert | Only on sheet **Alle** — created/changed dates |

**Sheets updated:** `Alle`, `Under arbeid`, `Done_Resolved`, `Rejected`.

**Sheets not touched:** e.g. `Ark3`.

---

## Before you start

1. **Close the Excel file** in Excel (otherwise save fails with “Permission denied”).
2. Use a current copy of **`NVE behov - DevOps status.xlsx`** (OneDrive / SharePoint / local download).
3. Open the **PM_productivity** repo in Cursor (or have it cloned locally) — the updater script lives there.
4. Python env: from repo root, use **`uv run python …`** (`uv sync` once; see repo `pyproject.toml` and `.cursor/rules/python-environment.mdc`).

---

## Option A — Recommended: Claude + MCP + repo script

### Step 1 — Tell Claude where the file is

Example path (adjust for your machine):

```text
C:\Users\<you>\Downloads\NVE behov - DevOps status.xlsx
```

or OneDrive:

```text
C:\Users\<you>\OneDrive - Tieto\NVE behov - DevOps status.xlsx
```

### Step 2 — Copy-paste prompt for Claude

Use this (edit the Excel path):

```markdown
Refresh the NVE Excel "NVE behov - DevOps status.xlsx" from Azure DevOps without changing formatting.

Excel path: C:\Users\<YOU>\Downloads\NVE behov - DevOps status.xlsx
Repo: PM_productivity (toolkit/scripts/update_nve_devops_status.py)

Do this in order:

1. Read all work item IDs from sheets Alle, Under arbeid, Done_Resolved, Rejected
   (column "DevOps link" — parse id from text or hyperlink).

2. Call Azure DevOps MCP wit_work_item get_batch:
   - project: 360
   - ids: all unique IDs (chunks of max 200 if needed)
   - fields: System.Id, System.WorkItemType, System.State, System.Title,
     System.IterationPath, System.Tags, System.CreatedDate, System.ChangedDate

3. Save the full MCP JSON array to a file, e.g.:
   toolkit/scripts/_nve_ado_batch_latest.txt
   (Strip any MCP wrapper lines like <<...>> if present — merge script handles that.)

4. From PM_productivity repo root, run:
   uv run python toolkit/scripts/update_nve_devops_status.py "<EXCEL_PATH>" --batch toolkit/scripts/_nve_ado_batch_latest.txt

   If Excel is open, use -o to write a new file first:
   ... -o "<EXCEL_PATH>.updated.xlsx"

5. Report: number of rows refreshed, any IDs missing in ADO, and a short list of
   ADO Status changes (before vs after) if you can diff against the file before update.

Do not rebuild the workbook from scratch — only in-place update via the script.
```

### Step 3 — Run the command Claude gives you

Typical command (repo root):

```powershell
uv run python toolkit/scripts/update_nve_devops_status.py "C:\Users\<YOU>\Downloads\NVE behov - DevOps status.xlsx" --batch toolkit/scripts/_nve_ado_batch_latest.txt
```

Expected output:

```text
Wrote C:\Users\...\NVE behov - DevOps status.xlsx
Rows refreshed: <n>; missing in ADO: 0
```

### Step 4 — Upload / share

Copy the updated file back to **OneDrive / SharePoint** if you edited a local copy.

---

## Option B — MCP only (no repo): not supported

Formatting-safe update **requires** `update_nve_devops_status.py`. Claude should not rewrite the whole `.xlsx` by hand.

---

## Option C — Refresh cache only (optional)

If you already have a batch JSON file and only want to update `nve_behov_ado_cache.json`:

```powershell
uv run python toolkit/scripts/merge_ado_batch_into_cache.py toolkit/scripts/_nve_ado_batch_latest.txt
```

Then run the updater **without** `--batch` (uses existing cache):

```powershell
uv run python toolkit/scripts/update_nve_devops_status.py "C:\path\to\NVE behov - DevOps status.xlsx"
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `Permission denied` on save | Close Excel; or use `-o other-file.xlsx` |
| `Missing ADO cache` | Run once with `--batch` pointing at MCP export |
| `ADO cache is missing work items` (old `build_nve_behov_split.py`) | Add IDs via `--batch` / merge script, then rebuild split if you still use that pipeline |
| New row in Excel, no DevOps link yet | Add link or id in **DevOps link** column first; script skips rows without id |
| `(not found in ADO)` in **ADO Status** | Wrong id or no access to project **360** in MCP |

---

## MCP reference (for Claude)

**Tool:** `wit_work_item`  
**Action:** `get_batch`  
**Project:** `360`  
**IDs:** integers from Excel (unique)  
**Fields:** see table in “What this does” above  

If your MCP names differ (e.g. `wit_get_work_items_batch_by_ids`), use the equivalent batch read — same fields and project.

---

## Files in repo (maintainers)

| File | Role |
|------|------|
| `toolkit/scripts/update_nve_devops_status.py` | In-place Excel refresh |
| `toolkit/scripts/merge_ado_batch_into_cache.py` | MCP JSON → `nve_behov_ado_cache.json` |
| `toolkit/scripts/nve_behov_ado_cache.json` | Last fetched DevOps snapshot |
| `toolkit/scripts/build_nve_behov_split.py` | Older pipeline from `NVE behov.xlsx` → DevOps status (different layout) |

---

## Cadence suggestion

- Refresh before **NVE status meetings** or when consultants ask “what moved in DevOps?”
- Optionally keep a dated copy before refresh: `NVE behov - DevOps status yyyy-mm-dd.xlsx` for diffs

---

*Last updated: 2026-10-06*
