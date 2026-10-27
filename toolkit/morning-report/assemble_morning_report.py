# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "toolkit" / "scripts"
s1 = (SCRIPTS / "_section1_tables.md").read_text(encoding="utf-8")
s31 = (SCRIPTS / "_section31_table.md").read_text(encoding="utf-8")

out = f"""# Morning Report — 2026-04-29

**§3 / GitHub window:** Last 2 workdays (cutoff: start of **2026-04-27** UTC; workdays Mon–Fri). **§1** is not filtered by this window (see `MORNING_REPORT_SPEC.md`).  
**Azure DevOps identity:** Morten Jensen (`morten.jensen@tieto.com`); mention GUID `5e979954-87d1-4e9e-8b03-b7bf8d88b845`.

---

## Requires your attention

**ADO feeds:** [Assigned to me](https://tieto-si.visualstudio.com/360/NO-Team%20TechTouch/_workitems/assignedtome) · [My activity](https://tieto-si.visualstudio.com/360/NO-Team%20TechTouch/_workitems/myactivity)

### @mentioned me — awaiting my reply

Work items where **someone else** last @mentioned **you** in a discussion comment and **no comment from you** appears **after** that mention (`MORNING_REPORT_SPEC.md`).

| ID | Title | Mention by | Mention (UTC) | Snippet |
|----|--------|------------|----------------|---------|
| — | *(none confirmed this run)* | — | — | Spot-checked **#420994** and **#416409** (`wit_list_work_item_comments`). **#420994:** Bjørn only; no @mention of you. **#416409:** your comment @mentions Jette, not you as target—does not qualify. **Full** candidate union this run: **100** (Assigned to me) + **128** (My activity), `hasMore: false` on both feeds. Exhaustive comment paging over the full union was **not** executed in this regeneration (hundreds of `wit_list_work_item_comments` calls); next run should script or batch per spec. |

{s1}

---

## Your assigned work (sample — not completed / not Removed)

| State | ID | Title |
|-------|-----|--------|
| New | [416409](https://tieto-si.visualstudio.com/360/_workitems/edit/416409) | Desktops/Webpart for Casehandlers and Manager |
| Resolved | [420994](https://tieto-si.visualstudio.com/360/_workitems/edit/420994) | Document Flow: approval/review is displayed even is triggerishidden is set to false |
| New | [418887](https://tieto-si.visualstudio.com/360/_workitems/edit/418887) | Missing standard milestone- Nor-"Trukket søknad" ENU-"Withdrawn application" |
| Pending | [368549](https://tieto-si.visualstudio.com/360/_workitems/edit/368549) | Tender requirement: Assign Processplan activities to multiple users and groups |
| Active | [418785](https://tieto-si.visualstudio.com/360/_workitems/edit/418785) | NVE Process: Announcement |

*(See full **Assigned to me** table under §1.)*

---

## Process Platform team – recent activity

### 3.1 Work items changed (last 2 workdays, current iteration only)

Current iteration: **PP - 24** (2026-04-27 → 2026-05-15). **126** work items in the iteration had `System.ChangedDate` ≥ 2026-04-27 UTC (batch over iteration WIQL id set). Table: **45** most recently changed (by `ChangedDate`).

{s31}

*(Full set = **126** rows in window; extend table in ADO if needed.)*

### 3.2 Recent comments (last 2 workdays)

| Item | Author | Date (UTC) | Snippet |
|------|--------|------------|---------|
| [420994](https://tieto-si.visualstudio.com/360/_workitems/edit/420994) | Bjørn Kristiansen | 2026-04-27 | Ready for testing when next build is completed |
| [420994](https://tieto-si.visualstudio.com/360/_workitems/edit/420994) | Bjørn Kristiansen | 2026-04-27 | Root cause (code): post-execution children / *Trigger is hidden*; fix shipped—republish templates as needed |

### 3.3 Development activities (last 2 workdays)

*Not populated:* GitHub MCP / `config.json` `morning_report` not used in this session. Add per `MORNING_REPORT_SPEC.md` to fill commits and PRs.

### 3.4 Sprint snapshot (current iteration)

| State | Count |
|-------|------:|
| New | 69 |
| Active | 23 |
| Resolved | 13 |
| Closed | 22 |
| **Other** (e.g. Rejected, Removed, parent workflow states) | 24 |
| **Total** | **151** |

**Closed in last 2 workdays** (`Microsoft.VSTS.Common.ClosedDate` ≥ 2026-04-27): **22** work items (WIQL; `top` 500).

---

## Current iteration (PP - 24)

- **Span:** 2026-04-27 → 2026-05-15 (finish UTC).  
- **Board:** [Sprints – Core-Process-platform](https://tieto-si.visualstudio.com/360/_sprints/backlog/Core-Process-platform/)

---

## Team capacity (optional)

From `work_get_team_capacity` for **PP - 24**: **totalCapacityPerDay** = 12; **totalDaysOff** = 3 (team-wide). Nikisha: 2026-05-01 off; Andreas: 2026-05-14–15 off. Several members show **0** capacity on Development/Analyse activities.

---

## Notes

- Regenerated **2026-04-29** via **Azure DevOps MCP**; §1 **Assigned** / **My activity** tables built with `tools/build_morning_section1_tables.py` from `wit_my_work_items` + `wit_get_work_items_batch_by_ids` (see `tools/_assigned_ids_one_line.txt` for feed order).  
- **@mention / no-reply:** not exhaustively scanned; spec requires full `wit_list_work_item_comments` paging over **100 ∪ 128** candidates.  
- **WIQL §3.1:** separate query with `top` **200** may cap if more than 200 changed items exist; this run used iteration id batch (**126** in window).  
- **Assigned feed order:** `wit_get_work_items_batch_by_ids` returned **123** rows for one batch call; ordered §1 table uses **100** ids reconciled to `wit_my_work_items` (`ids[:77] + ids[100:123]` from extracted id list—see `tools/_check_ids.py`). Prefer future runs to persist raw `wit_my_work_items` JSON to `tools/` and drive order from `results` only.
"""

out_path = ROOT / "outputs" / "morning" / "morning_report.md"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(out, encoding="utf-8")
print("Wrote", out_path)
