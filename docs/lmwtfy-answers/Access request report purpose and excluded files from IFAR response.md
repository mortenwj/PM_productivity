# Access request report purpose and excluded files from IFAR response

The Access Request Report is a bulk-handling tool for large IFAR cases (Word overview plus optional merged PDF). It lists the material registered on the request or selected in search; it does **not** mirror the IFAR response document. Files marked excluded from the response are **not** filtered out of the report. In detailed overview they are labeled **Excluded**; report content still includes their file bytes unless the user edits the output or limits the selection manually.

---

## Original Question

> What is the purpose of the access request report? Is it supposed to show all files, or should it exclude files that has been excluded from the IFAR response?

## Context

Colleague question about IFAR Access Request Reports: purpose of the feature and whether report scope should match files included on the outbound IFAR response versus files excluded at file-level decision.

## Findings

### Purpose

The **Access Request Report** helps organisations handle **very large** access requests without working document-by-document through the normal IFAR UI alone. It produces up to two artefacts:

- **Report overview** — a Word list of cases, documents, and (depending on mode) files.
- **Report content** — an optional merged PDF of file content, built asynchronously.

Reports can be ordered from **document or file search**, **saved searches**, or **Case functions → Produce access request report**. The setting `requestforaccess.reportoverviewforsmallifarcases` must allow simple or detailed report overview (not "off") for case and search report actions to be available.

Wiki purpose statement:

https://wiki.software-innovation.com/wiki/Request_for_Access_reports_and_shared_document_searches

Admin setting description (Ratatoskr `lookup_config`, **Report overview for small IFAR cases**):

https://help.360online.com/6.8.0000/SIAdminHelp/1033/HH_Start.htm#!Documents/requestforaccessifar.htm

The wiki also documents a **"reports only"** workflow: generate the report pack, **manually redact or remove pages** in the PDF, align the Word overview, then attach both to a reply letter. That workflow assumes the report is a **working set for casework**, not an automatic copy of what the requester receives.

### What the report includes (by entry point)

**From an IFAR case**

When you produce a report from the case menu, the product loads **all documents registered on the case** as access-request documents (`AccessRequestDocument` role). There is **no** filter on file-level include/exclude decision.

Code: `GetIfarDocumentsFromCase` in ReportHelper.cs

https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-client-api-build/SI.Client.Api.IFAR/Report/ReportHelper.cs

The same "all case documents" list is used when regenerating the report overview on the report document (`RegenerateReport` in IFARCaseManager.cs).

https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-support-build/SI.Biz.Core.IFAR/SI.Biz.Core.IFAR/Manager/IFARCaseManager.cs

**Report content (merged PDF)**

`ReportProcessor.GetFiles` takes the document list passed in and merges **all active files** on those documents. It does not read IFAR file decisions.

https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-support-build/SI.Biz.Core.Report/FromSearch/ReportProcessor.cs

**Detailed report overview (case-based, including small-case overview on the response document)**

`GetIfarFileInfosDetailedReport` queries **all** request-for-access activities and files on the case. Excluded files are **not** dropped from the list. The model maps `FileDecisionKey == 0` to the localized label **Excluded** and `FileDecisionKey == -1` to **Included**.

Query:

https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-support-build/SI.Biz.Core.IFAR/SI.Biz.Core.IFAR/Helpers/IfarQueryHelper.cs

Label mapping:

https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-support-build/SI.Biz.Core.IFAR/SI.Biz.Core.IFAR/Manager/IFARDocumentManager.cs

**Simple report overview**

Same file list without decision columns; no automatic exclusion.

**From document or file search**

The order dialog lets the user **deselect** rows before ordering. That is the main built-in way to limit scope when not generating from a full case.

Wiki (order dialogue from search):

https://wiki.software-innovation.com/wiki/Request_for_Access_reports_and_shared_document_searches

### How that differs from the IFAR response

On the **IFAR response document**, a file marked **excluded from response** (`Decision == 0`) is handled by `FileDecisionHandler`: the file is **removed** from the response document (or never copied onto it). Included files (`Decision == -1`) are copied onto the response.

https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-support-build/SI.Biz.Core.IFAR/SI.Biz.Core.IFAR/Manager/FileDecisionHandler.cs

That response logic is **separate** from Access Request Report generation. The report is **not** "what we dispatch"; it is **what was requested / selected for bulk export**, with optional manual editing afterward.

### Short answer for the colleague

1. **Purpose:** Bulk overview and optional merged PDF for large IFAR work; alternative path to normal per-file dispatch on the response document.
2. **Show all files?** From a case, **yes** for all documents (and their files in report content) registered on the case, unless the user limits selection from search.
3. **Exclude files excluded from IFAR response?** **No.** Exclusion from response affects the **response document only**. The detailed Word overview may **show** excluded files labeled **Excluded**; simple overview and report content do not apply that filter automatically.

### Confidence

**High** — behaviour verified in core-bl (ReportHelper, IfarQueryHelper, IFARDocumentManager, ReportProcessor, FileDecisionHandler) and aligned with wiki purpose and workflows.

**Medium** for customer-specific UX wording (exact menu labels, template columns) without seeing their version and language pack.

## Documentation assessment

- **Status:** partially_documented
- **Explanation:** The wiki page https://wiki.software-innovation.com/wiki/Request_for_Access_reports_and_shared_document_searches explains purpose, entry points, and the manual redaction workflow well. Admin help describes the report overview setting and that detailed mode includes decisions and remarks. Neither verified source states clearly that **excluded-from-response files remain in Access Request Reports** (detailed mode labels them; simple and report content do not filter them).
- **Suggested documentation changes:**
  - Add a subsection on **Request for Access reports and shared document searches** titled **Relationship to IFAR response and file decisions**: report scope is case/search selection, not response dispatch; excluded files stay in report overview (labeled in detailed mode) and in report content unless manually edited or deselected at order time.
  - Extend admin help topic **Request for access (IFAR)** under **Report overview for small IFAR cases** with one sentence that detailed overview lists all requested files and marks excluded ones; it does not remove them from the list.

## Risks and Limitations

- If a customer expects the report to match **only granted / included** material automatically, current product behaviour will look wrong. They need search-based selection, manual PDF/Word editing, or the normal IFAR response path for the outbound package.
- **Report overview for small IFAR cases** on the response document is a related but separate artefact (attached when the response is created). It uses the same case-wide file queries; the same exclusion semantics apply.
- This note reflects **core-bl master**; confirm on the customer's shipped version if they report different behaviour.

## References

- https://wiki.software-innovation.com/wiki/Request_for_Access_reports_and_shared_document_searches
- https://help.360online.com/6.8.0000/SIAdminHelp/1033/HH_Start.htm#!Documents/requestforaccessifar.htm
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-client-api-build/SI.Client.Api.IFAR/Report/ReportHelper.cs
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-support-build/SI.Biz.Core.IFAR/SI.Biz.Core.IFAR/Manager/IFARCaseManager.cs
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-support-build/SI.Biz.Core.IFAR/SI.Biz.Core.IFAR/Helpers/IfarQueryHelper.cs
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-support-build/SI.Biz.Core.IFAR/SI.Biz.Core.IFAR/Manager/IFARDocumentManager.cs
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-support-build/SI.Biz.Core.Report/FromSearch/ReportProcessor.cs
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-support-build/SI.Biz.Core.IFAR/SI.Biz.Core.IFAR/Manager/FileDecisionHandler.cs

Azure DevOps was not used (no work item in the question). Prior lmwtfy answers in `./docs/lmwtfy-answers/` cover related IFAR topics but not this exact question.
