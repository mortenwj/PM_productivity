# Document responsible org unit defaults to user profile

When a user from **department B** creates a new document on a case owned by **department A**, the document’s responsible organisational unit (`ToOrgUnit`, shown as owner department in the UI) is set to **department B** by default. That matches the core insert logic: the default comes from the **logged-in user’s profile org unit**, not from the case.

---

## Original Question

> “Inherit responsible from case.” I need clarification on system logic in this scenario: I created a case anchored in **department A**. I then log in with a user profile tied to **department B**, but with access to the case. When this user (from department B) creates a new document on the case, the document is automatically assigned **department B** as owner department, even though the case belongs to **department A**. Why?

## Context

Colleague question about Public 360° journal/document behaviour and expectations around inheriting the case’s responsible department. Research used **GitHub `te-industry-public360/core-bl`** (read-only). **360 Online help (Ratatoskr)** and **internal wiki (MediaWiki)** were **not** available in this Cursor session (MCP servers not configured), so official prose was not re-verified here.

## Findings

### Default on document insert (typical UI path)

In `DocumentMetaInsert.Prepare()`, **`SetDefaultValues()`** runs early (before `HandleToCaseValue()` and other preparation). Inside `SetDefaultValues()`, the code sets the default for the document’s organisational unit to the current user’s profile org unit:

`Statement.SetDefaultValue(Name.Document.ToOrgUnit, Get.User.ProfileOrgUnit);`

So for a normal insert, **`ToOrgUnit` is pre-filled with the creator’s department**. It is not left empty so that “inherit from case” logic could apply later in the generic default chain.

Source (implementation order and default):

https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/Document/DocumentMetaInsert.cs#L69-L90

https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/Document/DocumentMetaInsert.cs#L2841-L2843

### When the case’s org unit is applied to the document

In `MultipleDocumentContactHandler`, comments describe setting the logged-in user as responsible person and org unit when “Replied” is not set, with an exception: **if org unit is not set, inherit from case** (when the statement has a `Case` parent and `ToOrgUnit` is empty). That path is **conditional** and tied to that handler’s scenario (response-code / activity-contact context), not a blanket rule for every new document on a case.

Source:

https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/Document/MultipleDocumentContactHandler.cs#L489-L532

### SIF / integration path

For SIF document creation, `DocumentOperation.FixDocumentResponsibles` only calls `SetResponsibleFromCase` when **both** `OurRef` and `ToOrgUnit` are **empty** on the insert. The web admin setting **`sif.inheritresponsiblefromcase`** (`0` / `1` / `2`) then controls whether org unit only (`1`) or org unit and responsible person (`2`) are copied from the case. With **`0`**, that inheritance branch does not apply.

Source:

https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-integration-build/SIF/SI.Data.360/Operations/Common/DocumentOperation.cs#L166-L256

### Relation to “inherit responsible from case” wording

The setting name **`case` / `inheritresponsiblefromDocument`** in `DocumentMetaHandler` is used in **auto-update case** logic (whether the **case** is updated from the **document** under certain conditions). That is largely the **opposite direction** (document influencing case), not “new document always inherits case department.” Do not confuse it with the per-user default on new documents described above.

Search anchor in product code:

https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/Document/DocumentMetaHandler.cs

(see `inheritResponsibleFromDocumentSetting` / `inheritresponsiblefromDocument` near `AutoUpdateCase`.)

### Confidence

**Medium** for this answer file: behaviour is **verified in product source** only. No verified **help centre** or **wiki** section was read in this run.

## Documentation assessment

- **Status:** missing_documentation
- **Explanation:** Official admin or end-user help was not retrieved in this session (MCP not available). The behaviour is explainable from **core-bl** only; we did not verify a matching customer-facing topic title or section.
- **Suggested documentation changes:**
  - Add or extend a **journal / new document** topic stating explicitly that the document’s **default responsible organisational unit** follows the **creating user’s profile org unit** unless the client or integration supplies other values or enabled inheritance settings (SIF).
  - Cross-link from any **“inherit responsible from case”** naming in admin UI to both: (a) **document default from user**, and (b) **SIF** `sif.inheritresponsiblefromcase` and when it applies (empty `ToOrgUnit` / `OurRef` on insert).

## Risks and Limitations

- Line numbers refer to **`master`** on GitHub at research time; a fork or older branch may differ slightly.
- Customer-specific overlays (BIF, extensions) could add UI defaults; this answer reflects **standard core-bl** insert and the cited SIF operation.
- **Ratatoskr** and **MediaWiki** were skipped here; a second verified source could raise confidence to **high** if help agrees with code.

## References

- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/Document/DocumentMetaInsert.cs#L69-L90
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/Document/DocumentMetaInsert.cs#L2841-L2843
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/Document/MultipleDocumentContactHandler.cs#L489-L532
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-integration-build/SIF/SI.Data.360/Operations/Common/DocumentOperation.cs#L166-L256
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/Document/DocumentMetaHandler.cs
