"""
Generate pilot_weekly_report_YYYY-MM-DD.md from MCP-exported JSON batches.
Run after refreshing:
- projects/process-platform/pilot/tools/pilot_weekly_batch1.json (+ batch2) from wit_get_work_items_batch_by_ids
- projects/process-platform/pilot/tools/pilot_weekly_parents_level1.json (parent closure pass)
- projects/process-platform/pilot/tools/pilot_weekly_bugs_batch.json from wit_query_by_wiql (Bug slice) + wit_get_work_items_batch_by_ids (≤200 IDs per call)
- projects/process-platform/pilot/tools/pilot_weekly_descriptions_overlay.json — optional second pass: same IDs with
  System.Description + Microsoft.VSTS.Common.AcceptanceCriteria + Microsoft.VSTS.Common.StateChangeDate
  (≤200 IDs per MCP call; StateChangeDate supports New items + activity display, see spec)
- projects/process-platform/pilot/tools/pilot_weekly_what_it_does_summaries.json — stakeholder one-liners (not raw Description);
  keyed by work item id as string; preferred for *What it does* / bug symptom lines.
"""
from __future__ import annotations

import json
import pathlib
import re
from collections import defaultdict
from html import unescape

TARGET_EPICS = {
    411612: "PAF – NVE Pilot",
    414727: "PAF – User Experience (UX)",
    414328: "PAF – Standard Artifacts",
    411614: "PAF – Core Platform",
}
PROGRAM = 414623
NVE_FEATURE_PARENT = 413948  # NVE Specific process definitions before go-live — rich process text from Description

TOOLS = pathlib.Path(__file__).resolve().parent

_RE_HTML = re.compile(r"<[^>]+>", re.DOTALL)


def html_to_plain(html: str | None) -> str:
    if not html or not isinstance(html, str):
        return ""
    text = _RE_HTML.sub(" ", html)
    text = unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def excerpt(text: str, max_len: int = 380) -> str:
    if not text:
        return ""
    if len(text) <= max_len:
        return text
    cut = text[: max_len + 1]
    if " " in cut:
        cut = cut[: cut.rfind(" ")]
    return cut.rstrip(" ,.;") + "…"


def load_stakeholder_summaries(path: pathlib.Path) -> dict[str, str]:
    if not path.exists():
        return {}
    raw = json.loads(path.read_text(encoding="utf-8"))
    out: dict[str, str] = {}
    for k, v in raw.items():
        if isinstance(k, str) and isinstance(v, str) and v.strip():
            out[k.strip()] = v.strip()
    return out


def extract_purpose_clause(full_plain: str) -> str | None:
    """Pull the first Purpose: line from stripped description (often under Details)."""
    m = re.search(r"purpose:\s*(.+?)(?=\s+(?:Arguments|Workunit|ProgressPlan|$))", full_plain, flags=re.I | re.S)
    if not m:
        return None
    chunk = re.sub(r"\s+", " ", m.group(1).strip())
    return chunk if len(chunk) > 12 else None


def synthesize_want_so_that(refined_head: str) -> str | None:
    """Restructure classic user-story wording into a short third-person summary line."""
    # ADO text often uses "so the …" / "so we …" instead of strict "so that …"
    m = re.search(
        r"i want\s+(.+?)\s+so (?:that|the|we)\s+(.+?)(?:\.|$)",
        refined_head,
        flags=re.I | re.S,
    )
    if not m:
        return None
    want = normalize_want_clause(m.group(1))
    goal = re.sub(r"\s+", " ", m.group(2).strip())
    goal_first = goal.split(".")[0].strip()
    out = f"Lets teams {want[0].lower()}{want[1:]}; expected outcome: {goal_first}."
    return excerpt(out, 340)


def normalize_want_clause(want: str) -> str:
    want = re.sub(r"\s+", " ", want.strip())
    want = re.sub(r"^(to be able to|to be|to)\s+", "", want, flags=re.I)
    want = re.sub(r"^be\s+", "", want, flags=re.I)
    return want.rstrip(" ,.;")


def synthesize_want_only(refined_head: str) -> str | None:
    """User story with I want … but no so-that / so-the outcome (common in short ADO blurbs)."""
    if re.search(r"\s+so (?:that|the|we)\s+", refined_head, flags=re.I):
        return None
    m = re.search(r"i want\s+(.+)$", refined_head.strip(), flags=re.I | re.S)
    if not m:
        return None
    want = normalize_want_clause(m.group(1))
    if len(want) < 8:
        return None
    out = f"Lets teams {want[0].lower()}{want[1:]}."
    return excerpt(out, 360)


def stakeholder_what_it_does_line(
    wid: int,
    title: str,
    description_html: str | None,
    summaries: dict[str, str],
) -> tuple[str | None, bool]:
    """
    Return (line body, is_curated_override).
    Prefer JSON summaries; else synthesize from Purpose or user-story pattern — not a raw excerpt.
    """
    key = str(wid)
    if key in summaries:
        return summaries[key], True

    full = html_to_plain(description_html)
    if not full:
        return None, False

    head = refine_what_it_does_plain(full)
    syn = synthesize_want_so_that(head)
    if syn:
        return syn, False

    syn2 = synthesize_want_only(head)
    if syn2:
        return syn2, False

    p = extract_purpose_clause(full)
    if p:
        if re.match(r"^define\b", p, flags=re.I):
            p = "Adds " + p[7:].strip()
        elif re.match(r"^create\b", p, flags=re.I):
            p = "Adds " + p[6:].strip()
        return excerpt(p, 360), False

    return None, False


def build_nve_process_description(
    description_html: str | None,
    *,
    title: str | None = None,
    max_total: int = 1300,
) -> str | None:
    """
    For NVE template user stories (parent 413948): extract product intent, block list, and flow sequence
    from the HTML description — comparable in richness to *Outcome / acceptance* lines elsewhere.
    """
    full = html_to_plain(description_html)
    if not full or "details:" not in full.lower():
        return None
    parts: list[str] = []
    title = (title or "").strip()

    m = re.search(
        r"One-Sentence Description:\s*(.+?)(?=\s*2\.\s*Business|\s*Functional Behavior|\Z)",
        full,
        flags=re.I | re.S,
    )
    if m:
        s = re.sub(r"\s+", " ", m.group(1).strip())
        if len(s) > 4:
            label = f"Product intent ({title}): " if title else "Product intent: "
            parts.append(f"{label}{excerpt(s, 240)}")

    m2 = re.search(
        r"This process consists of\s+(\d+)\s+blocks:\s*(.+?)(?:\.\s*)?(?=We will first|The sequence|Block\s*1|\Z)",
        full,
        flags=re.I | re.S,
    )
    if m2:
        names = re.sub(r"\s+", " ", m2.group(2).strip().rstrip("."))
        parts.append(f"Building blocks ({m2.group(1)}): {excerpt(names, 360)}")

    m3 = re.search(
        r"The sequence in the process will be:\s*(.+?)(?:Dependencies|6\.\s*Dependencies|Submission Outcome|\Z)",
        full,
        flags=re.I | re.S,
    )
    if m3:
        seq = re.sub(r"\s+", " ", m3.group(1).strip())
        seq = re.sub(r"[\u2610\u2611\u2612☐☑✓]", "", seq)
        parts.append(f"Default flow: {excerpt(seq, 560)}")

    if not parts:
        return None
    return excerpt(" — ".join(parts), max_total)


def stakeholder_bug_symptom_line(
    wid: int,
    description_html: str | None,
    summaries: dict[str, str],
) -> str | None:
    """Bug: prefer curated summary; else one tight sentence from description (not the long body)."""
    key = str(wid)
    if key in summaries:
        return summaries[key]
    full = html_to_plain(description_html)
    if not full:
        return None
    head = refine_what_it_does_plain(full)
    if not head:
        head = excerpt(full, 400)
    # First sentence or two, compressed
    one = re.split(r"(?<=[.!?])\s+", head.strip())
    blob = " ".join(one[:2]).strip() if one else head
    return excerpt(blob, 280) if blob else None


def refine_what_it_does_plain(plain: str) -> str:
    """Drop common ADO template tails so *What it does* stays readable."""
    if not plain:
        return ""
    low = plain.lower()
    for marker in (" details:", "\ndetails:", " scope ", " acceptance criteria", "1. component identity"):
        idx = low.find(marker)
        if idx > 40:
            plain = plain[:idx].strip()
            low = plain.lower()
    return plain.strip()


def merge_description_overlay(wits: dict[int, dict], overlay_path: pathlib.Path) -> None:
    """Merge description-, text-, and date fields from a follow-up MCP batch export."""
    if not overlay_path.exists():
        return
    for w in json.loads(overlay_path.read_text(encoding="utf-8")):
        f = w.get("fields") or {}
        i = f.get("System.Id")
        if i is None:
            continue
        i = int(i)
        if i not in wits:
            continue
        tgt = wits[i]
        for key in (
            "System.Description",
            "Microsoft.VSTS.Common.AcceptanceCriteria",
            "System.Title",
            "System.WorkItemType",
            "Microsoft.VSTS.Common.StateChangeDate",
        ):
            if f.get(key) is not None and f.get(key) != "":
                tgt[key] = f[key]


def activity_timestamp_for_display(f: dict) -> str:
    """
    Date shown as activity **YYYY-MM-DD** in the markdown line.
    For New items, prefer State change date (aligns with WIQL that avoids stack-rank noise on ChangedDate).
    """
    ts = (
        f.get("Microsoft.VSTS.Common.ClosedDate")
        or f.get("Microsoft.VSTS.Common.ResolvedDate")
        or None
    )
    if not ts and (f.get("System.State") == "New" and f.get("Microsoft.VSTS.Common.StateChangeDate")):
        ts = f.get("Microsoft.VSTS.Common.StateChangeDate")
    if not ts:
        ts = f.get("System.ChangedDate") or ""
    if isinstance(ts, str) and ts:
        try:
            return ts[:10]
        except Exception:
            return str(ts)
    return ""


def load_work_items(*paths: pathlib.Path) -> dict[int, dict]:
    out: dict[int, dict] = {}
    for path in paths:
        if not path.exists():
            continue
        for w in json.loads(path.read_text(encoding="utf-8")):
            f = w.get("fields") or {}
            i = f.get("System.Id")
            if i is None:
                continue
            out[int(i)] = f
    return out


def root_epic(parent_by_id: dict[int, int | None], wid: int) -> int | None:
    """Return one of TARGET_EPICS if an ancestor matches; else None."""
    seen: set[int] = set()
    cur: int | None = wid
    while cur and cur not in seen:
        seen.add(cur)
        if cur in TARGET_EPICS:
            return cur
        if cur == PROGRAM:
            return None
        cur = parent_by_id.get(int(cur))
    return None


def fmt_item(
    f: dict,
    *,
    bug_section: bool = False,
    summaries: dict[str, str] | None = None,
) -> str:
    ts = activity_timestamp_for_display(f)
    st = f.get("System.State", "")
    title = f.get("System.Title", "").replace("\n", " ")
    wid = f.get("System.Id")
    typ = f.get("System.WorkItemType", "")
    line = f"- **{typ}** [{wid}](https://dev.azure.com/tieto-si/360/_workitems/edit/{wid}) — {title} — *{st}* (activity **{ts}**)"

    sums = summaries or {}
    wid_int = int(wid)
    ac_plain = excerpt(html_to_plain(f.get("Microsoft.VSTS.Common.AcceptanceCriteria")), max_len=320)

    extra: list[str] = []
    if bug_section:
        bl = stakeholder_bug_symptom_line(wid_int, f.get("System.Description"), sums)
        if bl:
            extra.append(f"  - *Symptom / details:* {bl}")
    else:
        what, curated = stakeholder_what_it_does_line(wid_int, title, f.get("System.Description"), sums)
        if what:
            tag = "*What it does:* "
            if curated:
                tag = "*What it does (stakeholder summary):* "
            extra.append(f"  - {tag}{what}")

        parent = f.get("System.Parent")
        try:
            parent_int = int(parent) if parent is not None else None
        except (TypeError, ValueError):
            parent_int = None
        if (
            typ == "User Story"
            and parent_int == NVE_FEATURE_PARENT
        ):
            proc = build_nve_process_description(f.get("System.Description"), title=title)
            if proc:
                extra.append(f"  - *Process description:* {proc}")

        if ac_plain:
            extra.append(f"  - *Outcome / acceptance:* {ac_plain}")

    if extra:
        return line + "\n" + "\n".join(extra)
    return line


def main() -> int:
    parent_by_id: dict[int, int | None] = {}
    wits = load_work_items(
        TOOLS / "pilot_weekly_batch1.json",
        TOOLS / "pilot_weekly_batch2.json",
        TOOLS / "pilot_weekly_parents_level1.json",
    )
    bug_only = load_work_items(TOOLS / "pilot_weekly_bugs_batch.json")
    merge_description_overlay(wits, TOOLS / "pilot_weekly_descriptions_overlay.json")
    merge_description_overlay(bug_only, TOOLS / "pilot_weekly_descriptions_overlay.json")
    summaries = load_stakeholder_summaries(TOOLS / "pilot_weekly_what_it_does_summaries.json")
    for f in wits.values():
        i = int(f["System.Id"])
        parent_by_id[i] = f.get("System.Parent")

    # Spec: dedupe — Bugs that already appear in the non-Bug WIQL export (same ID) count once.
    bug_ids_in_main_export = {int(f["System.Id"]) for f in wits.values() if f.get("System.WorkItemType") == "Bug"}

    by_epic: dict[int, list[dict]] = defaultdict(list)
    for i, f in wits.items():
        if f.get("System.WorkItemType") == "Epic":
            continue
        epic = root_epic(parent_by_id, i)
        if epic:
            by_epic[epic].append(f)

    report_date = "2026-04-21"
    lines: list[str] = [
        "# PAF pilot — weekly stakeholder update",
        "",
        f"**Oslo calendar note:** Generated from Azure DevOps WIQL using `@Today - 14` in the **organisation query timezone** (see spec for strict Oslo parity in a future hardening pass).",
        f"**ADO query as-of (UTC):** 2026-04-21T20:31Z (from MCP `wit_query_by_wiql`; see `projects/process-platform/pilot/tools/pilot_weekly_query_meta.json`).",
        "",
        "**Disclaimer:** Draft for pilot communication — not a signed-off product release note. PR links and engineering identifiers are omitted from this weekly view.",
        "",
        "## Scope (this run)",
        "",
        "- Non-Bug work items: `Area Path` under `360\\Core-Process-platform`, last **14 days** per WIQL (`PAF_pilot_weekly_report_SPEC.md`): **Closed/Resolved** dates for done work; **`Microsoft.VSTS.Common.StateChangeDate`** for **New** (not `System.ChangedDate` alone—stack rank updates); other states may use **ChangedDate**—see `projects/process-platform/pilot/tools/pilot_weekly_wiql_reference.md`.",
        "- Epic assignment: walk `System.Parent` using MCP `wit_get_work_items_batch_by_ids` closure (`projects/process-platform/pilot/tools/pilot_weekly_parents_level1.json`).",
        "- Epics in this run (in order): **411612** (NVE Pilot), **414727** (UX), **414328** (Standard Artifacts), **411614** (Core Platform). Work items that do not roll up under one of these four epics are **omitted** from this weekly view.",
        "- *What it does* comes from **`projects/process-platform/pilot/tools/pilot_weekly_what_it_does_summaries.json`** when provided (stakeholder summary, not raw ADO text); otherwise a short **synthesized** line from `Purpose:` / user-story patterns. **`Microsoft.VSTS.Common.AcceptanceCriteria`** is still shown as *Outcome / acceptance* when present (overlay).",
        f"- User stories under Feature **{NVE_FEATURE_PARENT}** (NVE pilot processes) also get a **Process description** line: intent + blocks + flow extracted from the long HTML template in Description (similar depth to acceptance-style lines under Feature 400794).",
        "",
        "---",
        "",
    ]

    order = [411612, 414727, 414328, 411614]
    for eid in order:
        title = TARGET_EPICS[eid]
        lines.append(f"## Epic {eid} — {title}")
        lines.append("")
        items = sorted(by_epic.get(eid, []), key=lambda f: (f.get("System.WorkItemType", ""), str(f.get("System.Title", ""))))
        if not items:
            lines.append("— *No qualifying work items in this export for the rolling window.*")
        else:
            feat_parent: dict[str, list[dict]] = defaultdict(list)
            for f in items:
                p = f.get("System.Parent")
                key = f"Parent {p}" if p else "No parent"
                feat_parent[key].append(f)
            for key in sorted(feat_parent.keys()):
                lines.append(f"### {key}")
                lines.append("")
                for f in sorted(feat_parent[key], key=lambda x: int(x.get("System.Id", 0))):
                    lines.append(fmt_item(f, summaries=summaries))
                lines.append("")

        lines.append("---")
        lines.append("")

    lines.append("## Bugs — `360\\\\Core-Process-platform` (from WIQL, last 14 days)")
    lines.append("")
    lines.append(
        "*Bug rows show Symptom / details from Description (overlay) when present; IDs already listed above are omitted.*"
    )
    lines.append("")
    bugs_for_section = [
        f
        for _bid, f in sorted(bug_only.items(), key=lambda x: int(x[0]))
        if int(f["System.Id"]) not in bug_ids_in_main_export
    ]
    if not bugs_for_section:
        lines.append("— *(none after dedupe, or missing `projects/process-platform/pilot/tools/pilot_weekly_bugs_batch.json`)*")
    else:
        for f in sorted(bugs_for_section, key=lambda x: int(x.get("System.Id", 0))):
            lines.append(fmt_item(f, bug_section=True, summaries=summaries))
        lines.append("")
        lines.append(
            f"*Total in Bug WIQL batch: **{len(bug_only)}**; listed here after dedupe: **{len(bugs_for_section)}**.*"
        )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("_End of generated draft._")

    out = pathlib.Path(__file__).resolve().parents[1] / f"pilot_weekly_report_{report_date}.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
