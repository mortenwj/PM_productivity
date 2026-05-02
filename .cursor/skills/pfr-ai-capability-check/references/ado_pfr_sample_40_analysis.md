# Azure DevOps: Product First Requests — sample of 40 Features (analysis)

**Date:** 2026-04-29  
**Project:** `360` (Azure DevOps organization `tieto-si`)  
**Method:** `wit_query_by_wiql` → `wit_get_work_items_batch_by_ids` (Azure DevOps MCP)

## How the list was located (aligned with wiki)

**WIQL** (Features under the Product First Requests area, most recently changed first):

```wiql
SELECT [System.Id], [System.Title], [System.State], [System.AreaPath], [System.CreatedDate], [System.ChangedDate]
FROM WorkItems
WHERE [System.TeamProject] = @project
  AND [System.WorkItemType] = 'Feature'
  AND [System.AreaPath] UNDER '360\Product First Requests'
ORDER BY [System.ChangedDate] DESC
```

**Top:** 40 rows (as returned by the MCP `top` parameter).

**Board URL (wiki):** `https://dev.azure.com/tieto-si/360/_boards/board/t/Product%20First%20Requests/Features`

### Sample caveat

Ordering by **`[System.ChangedDate] DESC`** biases the sample toward items **touched recently** (state edits, comments, field updates). In this pull, that surfaces a **cluster of related Swedish tender (IVO) PFRs** from April 2026 and several fresh CIM-driven items. It is **not** a random or time-stratified sample across the whole backlog.

---

## 1. What kinds of requests appear in this sample?

| Theme | Approx. share | Examples in sample |
|--------|----------------|----------------------|
| **Plan & Build (Norwegian municipalities)** | High (tags + titles) | Repeated `PB360: Change request - …` for Sarpsborg, Kongsvinger, Gjemnes, Kvinesdal, Kristiansand; Bergen “suggestion for improvement” items with rich Norwegian narrative. |
| **Formal tender / bid requirements** | **9/40** with `Custom.Source` = *New Bid/Tender* | **IVO** Swedish tender: multiple `Tender requirement: …` items with SKA/BÖR requirement numbering, Swedish + English text, screenshots. Separate bid item: **Luleå Tekniska universitet** (information management plan). |
| **Customer change orders (ServiceNow-style)** | **7/40** *Change requests from Customer* | Titles prefixed `PB360: Change request`, often `Custom.Supportnumber` **CS…**, tags **Customer informed**, **Support P&B**. |
| **Upgrade / migration** | **1/40** | e.g. **Arbetsmiljöverket – File count** (`Custom.Source` = *Upgrade Project*, tag `SEmigrationblocker`). |
| **Cross-cutting / platform** | Few | e.g. **415368** — 360 Conversion Service / TIFF / RA-FS (internal product wording, tag `6.11`). |
| **Information Act / IFAR** | Several | IFAR-related titles (Stavanger bid, Arbetsmiljöverket, DSS defaults). |
| **ServiceNow / GDPR minimal body** | At least **1** | **190516** — description points to ServiceNow + “Data not added here due to GDPR”. |

**`Custom.ImpactedModule` (top values in this 40):** `Plan&Build` (8), `Case` (6), `Case Handling Model` (4), `Search` (3), `IFAR` (3), `eArchive` (2), `0 - Not applicable` (2), then single counts (Reports, Board meeting, Map, Access matrix, etc.).

---

## 2. Field hygiene vs wiki template

The wiki asks for structured narrative and **`Custom.Source`** populated from a dropdown.

| Signal | Count (of 40) | Comment |
|--------|----------------|---------|
| **`Custom.Source` empty** | **23** | Over half the sample. Many items are still intelligible from title/tags/description, but **triaging, reporting, and SLA logic** that depend on source are weakened. |
| **`Custom.Customername` empty** | **4** | IDs **269922**, **271392**, **415368**, **420968** — mix of bid-only context, internal/KS suggestion, and NAV/CIM follow-up. |
| **`Custom.ImpactedModule` = `0 - Not applicable`** | **2** | **396399**, **396477** — “placeholder” module; undermines module-based routing and dashboards. |
| **`Custom.Conclusion` populated** | **8** | Values seen: *Moved to Discovery* (6), *Idea Bank* (2). Several of these are still **`System.State` = New** — worth checking whether “conclusion” should align with board column / closed state per process. |

**Priorities:** Priority **2** on 37 items; **1** on one large Nav access item (**384377**); **3** on two items (**421370**, **420902**).

**States:** **New** 35, **Pending** 1, **Closed** 2, **Rejected** 2.

---

## 3. “Quality” against the wiki’s requested sections

Automated **keyword** checks on HTML **Description** (wiki template headings):

| Section heading (wiki) | Items containing phrase (of 40) |
|--------------------------|-----------------------------------|
| “Specification of requested…” | **12** |
| “Consequences of not delivering…” | **12** |
| “Market potential…” | **12** |
| Co-funding wording (“co-fund” / “willing to co-fund”) | **3** |

**Interpretation:** A minority match the **stock Feature template** verbatim. Others use **different but strong** patterns (e.g. *Description / Unwanted behavior / Proposed change* for PB360 change requests, or long bilingual customer text). So **raw heading match understates usefulness** — but it **does** show that **many items are not filed with the canonical template sections**, which makes cross-item comparison and automation harder.

**Thin descriptions** (plain text after HTML strip, **&lt; 400 characters**): **8** items — including **GDPR stub** (190516), **empty body** on a bid title (**269922**), very short **Kristiansand** question (**420839**), short **Oslo** rejected item (**399688**), and a few short P&B notes. These are the **weakest** records for PM evaluation without relying on ServiceNow/CIM or comments.

**Strong examples in sample:** **269184** (template sections + screenshots), **270247** (bid + market + consequence), **394294** (very detailed Norwegian + screenshots), **384377** (long structured Nav need + Norwegian), **420282** / **420624** (tender requirements with SKA/BÖR and rich screenshots).

---

## 4. Concrete quality / process observations

1. **Source field discipline:** 23/40 missing `Custom.Source` is the single largest **structured data** gap relative to the wiki.
2. **CIM / suggestion path:** Items like **421370**, **421353**, **420902** come from Bergen with **priority 2–3** and good narrative but **no** `Custom.Source` — consistent with consultant-raised improvements that skip the dropdown.
3. **Tender cluster quality:** IVO tender items (**420281**–**420624** etc.) are **highly structured**, bilingual, and traceable to requirement IDs — **high quality for evaluation**, at the cost of **many separate Features** for one bid (expected per wiki).
4. **State vs conclusion:** Items with **`Custom.Conclusion`** such as *Moved to Discovery* while **State** remains **New** may confuse reporters and metrics; clarify in governance when state should change.
5. **Rejected sample:** **399688** (automatic categorization of defects — may be miscategorized as PFR vs defect routine); **190516** (minimal DevOps body by design + GDPR) — **evaluation quality depends on linked systems**.

---

## 5. Work item IDs in this sample (for audit)

`190516, 269184, 269202, 269922, 270247, 270979, 271352, 271358, 271392, 271607, 350636, 359572, 374446, 384377, 388690, 388982, 391912, 392267, 393194, 394294, 396399, 396473, 396477, 397332, 399688, 400430, 415368, 420281, 420282, 420587, 420590, 420616, 420621, 420623, 420624, 420839, 420902, 420968, 421353, 421370`

---

## 6. Suggested follow-ups (if you extend this analysis)

- Re-run with **`ORDER BY [System.CreatedDate] DESC`** for “newest intakes” vs **`[System.ChangedDate]`** for “recently touched”.
- Add **`Custom.Conclusion`**, **`System.AssignedTo`**, and date fields to WIQL export for aging analysis.
- Segment by **`Custom.Source`** and compare **description length** and **template section** rates.

Raw MCP batch JSON used for counts: `agent-tools/9ed5015b-53ec-48d7-9c62-f8058c1d673d.txt` (local Cursor agent output, not committed).
