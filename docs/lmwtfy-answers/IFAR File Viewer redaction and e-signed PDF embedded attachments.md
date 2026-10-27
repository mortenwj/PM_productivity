# IFAR File Viewer redaction and e-signed PDF embedded attachments

**Summary:** Oslo P&B’s concern is consistent with how the product gates redaction today. Optional **flattening** before burn applies to **emails and PDFs that have form fields** when **`FileViewerRedactionTiffMode`** is on. There is **no** redaction-path use of **`MergeSignedPdfFiles`**, which is where the codebase explicitly clears PDF **Attachments**. E-signed PDFs whose sensitive payload lives in **embedded attachments** without triggering that flatten path can still surface unredacted bytes outside the main viewer canvas, so a **database-wide hunt for “all signed PDFs”** is a reasonable operational response, not something this research found as a first-class product report.

---

## Original Question

> Hi
>
> Can someone help clarify this issue from OSlo P&B:
> Hint: they are mentioning redaction, which is a part of the IFAR module
>
> Document files must be stored without hidden attachments when they are redacted. This is currently not the case. The redacted content is still accessible as attachments.
>
> File 2 is an e‑signed document.
> It was redacted using the built‑in redaction function and saved as File 3 (now deleted).
>
> The unredacted document was publicly available online because e‑signed PDFs contain embedded attachments with signature data and the original document.
> The redaction function only shows the document file itself, without revealing these attachments.
>
> We now need to identify and review all signed documents in the database.
>
> Document files must be stored without hidden attachments when they are redacted.

## Context

Colleagues need a **product-grounded** explanation for Oslo **Plan & Build** about **IFAR-related** **File Viewer** redaction versus **PAdES-style** PDFs where **original content** can remain in **embedded attachments**, plus whether internal documentation already warns about it.

## Findings

1. **What “built-in redaction” does in code.** Redaction **burn** uploads the active file version to Prizm, applies the redaction markup, waits for completion, downloads a **PDF**, and stores it back through **`RedactionFileManager`** (including IFAR-specific **`UploadRedactedIfarDocument`** wiring). See burn and upload flow: https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/FileViewer/RedactionBurner.cs#L31-L110 and IFAR entry: https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/FileViewer/RedactionFileManager.cs#L76-L134

2. **When an extra convert/flatten step runs.** Before burn, **`InitiateBurnAndVariantCreation`** optionally runs **`RedactionConverter`** (upload → TIFF → PDF) **only** for file versions where **`DetermineFlatteningRequirements`** set **`Flatten == true`**. Others go straight from archive stream to burn with **`RemoteFileId`** unset. See: https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/DocumentDispatchModule/DocumentDispatchProcess.cs#L1855-L1878

3. **What turns on `Flatten` for PDFs.** Under **`FileViewerRedactionTiffMode`**, **EML/MSG** are always marked to flatten. For **PDF**, the code opens the file and sets **`Flatten`** only when **`PdfTool.HasFormFields`** returns true. That helper is literally **`document.Form?.Fields.Count > 0`**. It does **not** scan **`PdfLoadedDocument.Attachments`** or other embedded-file carriers used by some e-signatures. See: https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/FileViewer/RedactionHelper.cs#L30-L58 and https://github.com/te-industry-public360/core-utils/blob/master/SI.Common.Utils/SI.Common.FileUtils/Pdf/PdfTool.cs#L668-L672

4. **Where attachments *are* stripped in product code.** **`PdfTool.MergeSignedPdfFiles`** removes **`loadedDoc.Attachments`** before merging signed PDF streams. That path is used from **`MergeFiles`** in **`DocumentDispatchProcess`** when merging dispatch streams (feature branch), **not** from **`InitiateBurnAndVariantCreation`**. So redaction burn does **not** inherit that attachment clear by default. See: https://github.com/te-industry-public360/core-utils/blob/master/SI.Common.Utils/SI.Common.FileUtils/Pdf/PdfTool.cs#L231-L234 and merge call site: https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/DocumentDispatchModule/DocumentDispatchProcess.cs#L1761-L1777

5. **IFAR vs generic files.** IFAR uses the same File Viewer redaction stack; the wiki describes online redaction as part of IFAR when File Viewer is installed. Product page: https://wiki.software-innovation.com/wiki/360%C2%B0_Information_Act_Request (no attachment caveat on that page).

6. **“Identify all signed documents in the database.”** This note does **not** verify a shipped **360°** inventory feature for “all digitally signed PDFs.” Practical follow-up belongs with **R&D**, **security**, or **customer DBA** (format metadata, exports, external PDF tooling), scoped to their **SQL Server** and **file store** conventions.

7. **Help center vs File Viewer redaction.** Admin topics under **Redaction** describe **archive batch** jobs for record metadata redaction, not in-viewer PDF burn. Example: https://help.360online.com/6.8.0000/SIAdminHelp/1033/Index.html#!Documents/redaction.htm End-user redacting in the File Viewer is linked from the **360° File Viewer** wiki (English help path to **redactfiles.htm**): https://wiki.software-innovation.com/wiki/360%C2%B0_File_Viewer

## Documentation assessment

- **Status:** partially_documented

- **Explanation:** Verified wiki pages explain **File Viewer** redaction, **IFAR** use of online redaction, and **6.5** “global redact” with **burn-in** to **PDF** and **P - Public** variant (https://wiki.software-innovation.com/wiki/360%C2%B0_File_Viewer, https://wiki.software-innovation.com/wiki/360%C2%B0_Information_Act_Request, https://wiki.software-innovation.com/wiki/6.5_release_information). The **build log** documents **`FileViewerRedactionTiffMode`** flattening for **emails and PDF forms** before redaction (https://wiki.software-innovation.com/wiki/Build_log_hotfix_packages, DevOps row **413628**, found via on-page search for **`FileViewerRedactionTiffMode`**). None of these verified pages spell out **e-signed PDFs**, **PAdES embedded originals**, or **post-redaction attachment audits**.

- **Suggested documentation changes:**
  - Add a subsection on **[[360° File Viewer]]** or **[[360° Information Act Request]]**: redaction plus **digitally signed PDFs**; state that documented flattening (toggle **`FileViewerRedactionTiffMode`**) targets **PDF forms and email** per build log wording, not every embedded payload; point to **Accusoft PrizmDoc** behaviour limits and recommend **attachment-aware PDF checks** before publishing **public** variants.
  - In **[[6.5 release information]]** (redaction section), narrow strong wording that redaction **“ensures”** protection on public copies: clarify **visible burn-in** plus optional **flatten** path, and note industry risk of **hidden embedded files** in some signed PDFs if flattening does not apply.
  - Optional short link from **[[IFAR FAQ]]** or **[[IFAR and versions and variants]]** on **public variant hygiene** when source files may be **e-signed**.

## Risks and Limitations

- **Prizm output detail** for a given PDF is not re-derived here; claims about exact bytes after burn rest on **customer observation** plus **360** pipeline facts above. Treat forensic conclusions as **environment-specific** unless reproduced on their build.

- **Wiki search** was bounded; a longer audit might surface other pages.

- **Confidence:** **High** for implementation and wiki quotes used. **Medium** for “every Oslo scenario is explained solely by the flatten gate,” because real PDFs vary.

## References

- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/FileViewer/RedactionBurner.cs#L31-L110
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/FileViewer/RedactionFileManager.cs#L76-L134
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/DocumentDispatchModule/DocumentDispatchProcess.cs#L1855-L1878
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/DocumentDispatchModule/DocumentDispatchProcess.cs#L1761-L1777
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/FileViewer/RedactionHelper.cs#L30-L58
- https://github.com/te-industry-public360/core-utils/blob/master/SI.Common.Utils/SI.Common.FileUtils/Pdf/PdfTool.cs#L668-L672
- https://github.com/te-industry-public360/core-utils/blob/master/SI.Common.Utils/SI.Common.FileUtils/Pdf/PdfTool.cs#L231-L234
- https://wiki.software-innovation.com/wiki/360%C2%B0_File_Viewer
- https://wiki.software-innovation.com/wiki/360%C2%B0_Information_Act_Request
- https://wiki.software-innovation.com/wiki/6.5_release_information
- https://wiki.software-innovation.com/wiki/Build_log_hotfix_packages
- https://help.360online.com/6.8.0000/SIAdminHelp/1033/Index.html#!Documents/redaction.htm
