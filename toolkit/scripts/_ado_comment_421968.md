## Standard capability check (AI-assisted)

*Posted from PM_productivity PFR AI capability check (`schema_version` 1.2.2).*

| Field | Value |
|-------|--------|
| **Outcome** | partially_supported |
| **Confidence** | medium |
| **Documentation status** | partially_documented |
| **Human review required** | yes |
| **Assessed at** | 2026-05-05T12:45:00Z |

### Documentation coverage
**Verified** administrator help (**SRC-1**) explains the legacy **Mandatory document date** setting. **Verified** internal settings reference (**SRC-2**) aligns but is **not maintained**. **Verified** wiki pages **[[Flexibility initiatives]]** (**SRC-4**) and **[[Full-Flex UI entity creation]]** (**SRC-5**) explain **FFUI** field properties (**Mandatory**, read-only, hidden) and place **document creation / document wizards** on a **later** roadmap wave—not in the **current** FFUI pilot scope for documents. **[[Full-Flex UI entity creation]]** is explicitly **UNDER CONSTRUCTION**, so schedule and detail text must be **confirmed with PM**. What is **not** fully documented for a single triage decision is the **end-to-end** answer for **all document categories** (legacy setting scope vs future FFUI document wizard) without **T1** or a **single authoritative delivery work item** found by title search.

### Capability analysis
- **Observed capability** — **Today:** Administrator help describes **`document.mandatorydocumentdate`**: when enabled, **Document date** is **mandatory** in the **Document wizard** for **externally produced documents**, **UI-only** validation, default **No** (**SRC-1**, **SRC-2**). **Strategic / roadmap:** **FFUI** is documented as supporting **Mandatory** (and related) **field properties** in configurable wizards, while **document creation** (applying FFUI to **document wizards**) is documented as **not yet supported** / **planned** in the **2026 / post–pilot** horizon (**SRC-4**, **SRC-5**).
- **Required capability** — Mandatory **Document date** on **document creation** across **all** relevant **document categories**, not limited to **incoming** only, to retire a **customization** and move toward **standard** (**C-1**).
- **Assessment** — **Not equivalent** to the **full** stated need on **one** path alone: legacy setting is **narrower** than *all categories* (**C-3**). The **FFUI** track is the documented direction for **configurable mandatory fields** in wizards, but **FFUI document creation** is **explicitly future work** in wiki roadmap/limitations—not a shipped replacement for this PFR today (**C-4**). **Outcome remains `partially_supported`:** **partial** mitigation exists in **legacy** configuration; **full** standard alignment depends on the **FFUI document-creation** wave plus PM confirmation of scope and timing.
- **Key implementation finding** — *No T1 code was retrieved; category-level and wizard-path behaviour were not verified in source.*

### Decision framing
- **Interpreted requirement** — **Wizard / field mandatory** behaviour for **Document date** on **create document**, **across categories** (configuration / validation, not access-control enforcement).
- **Branch** — **Legacy administrator setting** gives **partial** coverage (**externally produced** scope per help). **FFUI** is the documented **platform** approach for **mandatory** field configuration, but **document wizards** on FFUI are **not** in the **current** supported pilot list per wiki (**SRC-4**, **SRC-5**). **Final interpretation** — **`partially_supported`**: triage should **not** treat this as **fully `already_supported`** by FFUI **today**; it should **combine** near-term **legacy** options with **roadmap** tracking on **FFUI document creation**.

### Underlying need
Make **Document date** **required** when **creating documents** for the **categories** the customer needs—**beyond incoming-only**—so **Sjöfartsverket** can **drop a customization** after upgrade. **Longer term**, the organisation's *mandatory in wizard* need aligns with **FFUI**'s documented **Mandatory** field model once **document creation** is delivered on that track.

### Outcome and confidence (rationale)
**`partially_supported`** because **(1)** **legacy** **`document.mandatorydocumentdate`** is **real standard surface** but **scoped** to **externally produced documents** per **two T2** lines (**SRC-1**, **SRC-2**), and **(2)** **FFUI** is documented as the place for **mandatory field** configuration, while **document creation on FFUI** is documented as **future / not yet supported** (**SRC-4**, **SRC-5**). **`medium`** confidence: **no T1**; **FFUI entity** page **under construction**; roadmap **prioritization TBD**.

### Claims (verify before closing)
1. [C-1] The PFR requests Document date to be obligatory when creating a document for all document categories, explicitly beyond incoming document only. — *support:* inferred *(Markdown label: reported in PFR request)* — *sources:* SRC-3  
2. [C-2] Administrator help documents a *Mandatory document date* setting: when Yes, Document date is mandatory in the Document wizard for externally produced documents; validation is UI-only; default is No. — *support:* documented_in_source — *sources:* SRC-1, SRC-2  
3. [C-3] Verified administrator help and internal settings reference do not document mandatory Document date for every document category; they scope mandatory Document date to externally produced documents. — *support:* documented_in_source — *sources:* SRC-1, SRC-2  
4. [C-4] Internal product wiki documents Full-Flex UI as supporting field properties including Mandatory / read-only / hidden, while explicitly deferring Document creation (document wizards) to a later roadmap wave—not part of the current shipped pilot entity set for FFUI document creation. — *support:* documented_in_source — *sources:* SRC-4, SRC-5  

### Evidence consulted
- **SRC-1** (help_360, **T2**): [Administrator help — Document](https://help.360online.com/6.8.0000/SIAdminHelp/1033/Index.html#!Documents/document.htm) — Mandatory document date; externally produced documents; UI-only validation.  
- **SRC-2** (mediawiki, **T2**): [[360° settings - internal reference]] — `document.mandatorydocumentdate`; **not maintained**.  
- **SRC-4** (mediawiki, **T2**): [[Flexibility initiatives]] — FFUI features (incl. **Mandatory**); roadmap **AFTER (2026)** includes **Document creation**.  
- **SRC-5** (mediawiki, **T2**): [[Full-Flex UI entity creation]] — Field **Mandatory** status; **Document creation** planned / future; **UNDER CONSTRUCTION** banner.  
- **SRC-3** (ado_work_item, **T3**): [Feature 421968](https://dev.azure.com/tieto-si/360/_workitems/edit/421968) — PFR context.

### Related ADO items (if queried)
Earlier WIQL sample on titles containing *Document date*: **236004** — *FINSPÅNGS KOMMUN PUBLIC360- Suggestion to make it possible for other document types to have a mandatory document date.* — **New** (likely related theme). **190112** / **188151** — display/detail angles; **partial overlap** with *document date* wording only.

### Unknowns / questions for reporter
- Which **categories** must be in scope, and do they all qualify as **externally produced** for the **legacy** setting?
- Is **`document.mandatorydocumentdate`** already **Yes** where the gap is seen?
- Example **wizard path + category** where **Document date** is optional today.

### Limitations (what AI did not verify)
- **No T1** (product code).  
- **FFUI entity** wiki page **under construction**.  
- **No** Feature/Epic found by a **narrow WIQL** on *Document creation* + *FFUI* in the title—internal tracking id may differ.  
- Help/help-centre **version path** may differ from tenant.

### Recommended next steps
- Tag **PM / FFUI** for **roadmap alignment** with **document creation** on FFUI (**SRC-4**, **SRC-5**).  
- **Near term:** validate **`document.mandatorydocumentdate`** against **externally produced** flows; capture **screens + category codes**.  
- **Backlog:** link or review **236004** for **duplicate / merge** with **421968**.  
- **Schedule:** ask PM for the **authoritative** DevOps **Epic/Feature** id for **FFUI document wizards** if it exists under another name.
