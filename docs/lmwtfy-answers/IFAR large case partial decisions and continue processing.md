# IFAR large case: send decisions on processed documents and continue on the rest

**Yes, that is how the product is designed to work for Information Act Request (IFAR) cases.** You can record decisions per document or file as you go, dispatch or prepare a response for the subset you have finished, and keep working on remaining requests in the same access request case. Exact behaviour depends on version, settings, and whether you use Auto IFAR, so confirm your customer’s build if they see something different.

## Evidence ledger (this run)

**Claim:** You can make **individual file-level** decisions in IFAR and handle a large case incrementally rather than all-or-nothing at once.

**Source:** https://wiki.software-innovation.com/wiki/360%C2%B0_Information_Act_Request (module overview, “Decision and Response” and related bullets).

**Verified how:** Read full wiki page via MediaWiki `mediawiki_get_page`.

---

**Claim:** The product explicitly mentions **partial replies** being dispatched and activities closing in that scenario (6.2 release notes on the same page).

**Source:** Same wiki page, “Recent Enhancements” and “What’s new in which version” for 6.2.

**Verified how:** Same full page read.

---

**Claim:** Core business logic supports **per-file** include/exclude decisions and **granted / partially granted / denied** at request level while the case and activity are still open.

**Source:** https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-support-build/SI.Biz.Core.IFAR/SI.Biz.Core.IFAR/Manager/DecisionManager.cs#L62-L165

**Verified how:** Read implementation of `SetDecisionForFile` and `SetDecisionForDocument` (open case, open activity, `Partiallygranted_2` branch).

---

**Claim:** Admin help describes the IFAR module as integrated with dispatch and response documents (templates, format converter), consistent with sending a response when part of the work is ready.

**Source:** https://help.360online.com/6.8.0000/SIAdminHelp/1033/Index.html#!Documents/360informationactrequest.htm

**Verified how:** Read full topic via Ratatoskr `read_topic`.

---

**Claim:** No prior lmwtfy note in this repo answered this exact “partial progress then continue” wording.

**Source:** Grep under `./docs/lmwtfy-answers/` for IFAR + decision (related notes exist for dispatch, eInnsyn, access request wording, not this question).

**Verified how:** Workspace search.

---

## Short answer for the colleague

1. **Decisions while the case stays open:** Internal wiki documents **individual file-level decisions** and the overall flow for large access requests, including reports and collaboration patterns. See https://wiki.software-innovation.com/wiki/360%C2%B0_Information_Act_Request

2. **Partial reply / incremental dispatch:** The same page states that from **6.2**, **request for access activities can be closed automatically when a partial reply is dispatched**, which matches the idea of sending a decision on what is ready and continuing on the rest. Always match that to the customer’s **version**.

3. **What the code is doing:** `DecisionManager` applies decisions per **file** (`SetDecisionForFile`) and per **set of request activities** (`SetDecisionForDocuments`), including **partially granted** handling, while the IFAR case and activity are **not closed**. That supports incremental processing in the backend. See https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-support-build/SI.Biz.Core.IFAR/SI.Biz.Core.IFAR/Manager/DecisionManager.cs#L62-L165

4. **What you should still verify with the customer:** **Auto IFAR** settings (`requestforaccess.responsibleforautoifar` and related), **which response template** they use, and whether they use **large file dispatch** or merged PDF paths. Those change UX and steps but do not contradict incremental decisions.

## Confidence

**High** for “product supports incremental decisions and partial response flow” because **wiki + code + admin help** align. **Medium** for any sentence about **their** exact screen flow without seeing their version and configuration.

## Sources

- Wiki module overview: https://wiki.software-innovation.com/wiki/360%C2%B0_Information_Act_Request  
- Admin help (Information Act Request): https://help.360online.com/6.8.0000/SIAdminHelp/1033/Index.html#!Documents/360informationactrequest.htm  
- Code (`DecisionManager`): https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-support-build/SI.Biz.Core.IFAR/SI.Biz.Core.IFAR/Manager/DecisionManager.cs#L62-L165  

Azure DevOps was **not** used for this question (no work item id in the prompt). Ratatoskr `search_topics` for a few IFAR phrases returned **no** hits; the run relied on the **360° Information Act Request** topic from a broader **Information Act** search plus `read_topic` (within the default **≤3** reads budget).
