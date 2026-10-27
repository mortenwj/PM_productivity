# Access request module: verification of customer-facing draft

**Run 3 (2026-05-01, lmwtfy with Ratatoskr):** Same colleague question. **`user-ratatoskr` is working** (VPN/GlobalProtect path). Admin help (SIAdminHelp 6.8) and bundled release sections were searched. **Public 360° end-user help** (full client help, id 4100 tree) is **not** in the same Ratatoskr corpus as the admin TOC; the module overview explicitly sends readers there for the Access requests overview web part.

Your draft is still only **partly** supportable from admin wiki + admin help. Do **not** treat the four customer bullets as fully verified until you align with **Public 360° online help** for the exact screen strings (Historical notes, View access request).

---

## Evidence ledger (Run 3)

- **Historical notes column:** `compare_topic` for the exact phrase **Historical notes** returned **no mentions in any section** (release, admin-en, admin-no). Wiki still does not define that column. **Conclusion:** your detailed bullet list for that column is **not** admin-help-verified; needs **Public 360° help** or UI review.
- **View access request:** `compare_topic` for **View access request** returned **no mentions in any section**. Wiki had no hit earlier. **Conclusion:** purpose and hide/disable are **not** verified from indexed help; needs **Public 360° help** or product.
- **Legal paragraphs / decisions:** Wiki **5.16** (Decision dialog, remove paragraph on files, defaults by outcome). **`lookup_config`** for “paragraph IFAR” surfaces **Report overview for small IFAR cases**: detailed overview **includes decisions, paragraphs and remarks** (admin **Request for access (IFAR)** settings topic). **Conclusion:** paragraph usage in IFAR reporting and decision flow is **supported**; your customer wording on “configure which paragraphs appear” should stay close to **settings, code tables, templates, and decision UI**, not a single unnamed global switch.
- **Always unregistered requester / merge to response:** Admin **Request for access (IFAR)** settings state the response letter **content is merged from a Microsoft Word template**, with four template variants per language (comments / file titles / anonymization). **Conclusion:** recipient and contact behaviour is **heavily template- and channel-dependent**; “always unregistered at document level” is still **not** stated in admin help and must be validated on **customer template + import path** (eInnsyn scanner, manual case, and so on).
- **360 Online help (Ratatoskr):** **Used** this run (`search_topics`, `read_topic`, `compare_topic`, `lookup_config`). No DNS skip.

---

## Original Question

> Colleague preparing a reply about the Public 360° access request module. Confirm whether the drafted explanations are correct for: (1) Historical notes column, (2) configuring legal paragraphs for decisions, (3) always registering requester as unregistered at document level / merge into response, (4) "View access request" link purpose and hide/disable.

## Context

Internal PM verification before customer send. Sources: **`user-ratatoskr`** (admin-en, release, `compare_topic` across sections), **`user-mediawiki`** (product + 5.16 + 6.8 + implementation stub). No ADO item.

## Findings

### 1. Column "Historical notes"

**Confidence: low for the detailed bullet list.**

**Ratatoskr:** `compare_topic` found **zero** occurrences of **Historical notes** in release + admin English + admin Norwegian.

**Wiki:** Product page does not define that column; 6.8 “historical activity” in template logging is a **different** concept.

https://wiki.software-innovation.com/wiki/360%C2%B0_Information_Act_Request

https://wiki.software-innovation.com/wiki/6.8_release_information

**Admin module topic** points to end-user help for the Access requests overview web part (Public 360° online help), not SIAdminHelp body text for list columns:

https://help.360online.com/6.8.0000/SIAdminHelp/1033/Index.html#!Documents/360informationactrequest.htm

**Before sending:** Use Public 360° help (or the customer’s language equivalent) for the screen that shows **Historical notes**, or validate with someone on the same build.

### 2. Legal paragraphs in decisions

**Confidence: medium.**

Wiki **5.16**: Decision dialogue, **Remove paragraph on files**, different defaults for **Granted** vs **Partly granted / Denied**.

https://wiki.software-innovation.com/wiki/5.16_release_information

**Ratatoskr `lookup_config`:** setting **Report overview for small IFAR cases** describes a **detailed** report overview including **decisions, paragraphs and remarks** (confirms paragraphs are first-class in IFAR artefacts, not a footnote).

**Ratatoskr `read_topic`:** **Request for access (IFAR)** settings reference (templates, mail scanner, responsibilities). Full topic:

https://help.360online.com/6.8.0000/SIAdminHelp/1033/Index.html#!Documents/requestforaccessifar.htm

**Suggested tightening for the customer:** Paragraphs appear in **decision and reporting** flows; organizations configure IFAR through **settings, registers, templates, and standard laws/paragraphs** (sub-setup). Avoid implying one unnamed “global configure display” control unless their help names it.

### 3. Requester always as unregistered contact at document level

**Confidence: low.**

Admin help emphasizes **Word templates** for the response document (merge content, variants with comments and file titles, anonymization of file titles). That supports **“behaviour depends on template + settings + import channel”**, not a single **always unregistered** rule.

https://help.360online.com/6.8.0000/SIAdminHelp/1033/Index.html#!Documents/requestforaccessifar.htm

https://wiki.software-innovation.com/wiki/360%C2%B0_Information_Act_Request

Frame unregistered requester and recipient merge as **setup to validate** (template, scanner, case creation rule), not as confirmed standard text.

### 4. Link "View access request" (purpose and hide/disable)

**Confidence: low.**

**Ratatoskr:** `compare_topic` found **no** **View access request** string in any indexed section.

**Wiki:** No exact phrase hit on product page alone.

**Before sending:** Public 360° help for the web client screen where the link appears, or Enablement/R&D for official wording and whether visibility is **setting, role, web part, or customization**.

## Risks and Limitations

- **Corpus gap:** Ratatoskr here is strong on **Administrator** and **release** bundles; exact **Public 360°** UI labels may only appear in the **end-user** help set (linked from the module overview, not fully searched as plain text in this pass).
- **Version:** Help URLs show **6.8.0000** SIAdminHelp; customer may differ slightly by patch.

## References

### Wiki

- https://wiki.software-innovation.com/wiki/360%C2%B0_Information_Act_Request
- https://wiki.software-innovation.com/wiki/360%C2%B0_Information_Act_Request_-_Implementation_guidelines
- https://wiki.software-innovation.com/wiki/5.16_release_information
- https://wiki.software-innovation.com/wiki/6.8_release_information

### 360 Online (Ratatoskr `read_topic` / module entry)

- https://help.360online.com/6.8.0000/SIAdminHelp/1033/Index.html#!Documents/360informationactrequest.htm
- https://help.360online.com/6.8.0000/SIAdminHelp/1033/Index.html#!Documents/requestforaccessifar.htm
- https://help.360online.com/6.8.0000/SIAdminHelp/1033/Index.html#!Documents/accessrequestifar.htm (stub: points to Request for access IFAR topic above)
