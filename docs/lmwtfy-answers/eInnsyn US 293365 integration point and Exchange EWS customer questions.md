# eInnsyn IFAR import (US 293365) and Exchange EWS retirement

User Story 293365 describes a **proposed** way to pull eInnsyn access requests from the **Digdir integration point** instead of relying on the **IFAR mail scanner** and **order.xml** e-mail path. A second thread asks about **Exchange Web Services (EWS)** end of life and what **Public 360°** plans to do. This note separates **facts from DevOps and Microsoft**, **product backlog intent**, and **what still needs an owner answer** before you e-mail a customer.

---

## Original Question

> Regarding receiving information act requests and how we handled them initially. User Story 293365 (eInnsyn access request, connector from integration point instead of e-mail scanner): will that be standard for all online or cloud customers, or only some, or a paid module or integration? Automatic or something every customer must change? The US said 6.8; is that still valid?  
>  
> A customer on IFAR setup asks about **Exchange Web Services** going EOL and what plans we have to compensate.

## Context

Research run with **`user-azure-devops`** `wit_get_work_item` (**`project`: `360`**), **`user-ratatoskr`** (admin and release help), **`user-mediawiki`**, and public Microsoft messaging on EWS. No core-bl code path was traced in this pass.

---

## Findings

### 1. User Story 293365 (what it actually is today)

**Verified in Azure DevOps (project `360`):**

https://tieto-si.visualstudio.com/360/_workitems/edit/293365

- **State:** **New** (backlog, **not** implemented or released as shipped product behaviour in this record).
- **Work item type:** User Story.
- **Title:** eInnsyn access request – Add connector to retrieve access request directly from integration point.
- **Tags:** **`6.9`** (not `6.8`). If someone quoted “6.8”, the **current tag on the item is 6.9**; treat any old “6.8” mention as **stale unless** you find another field or comment that still says 6.8 (this pass did not load full comment history).
- **Parent Feature:** **281011** – “Refactor and improve IFAR import of accesss requests”, also **State New**:

https://tieto-si.visualstudio.com/360/_workitems/edit/281011

**Intent described in the story (paraphrase, not a promise to customers until PM or R&D signs off):**

- New web-based eInnsyn export toward the integration point would make the **eInnsyn client that generates order.xml e-mails** unnecessary and would avoid the **IFAR e-mail scanner** account and auth complexity for that path.
- Proposed **work unit** “Process eInnsyn access requests” in eInnsyn sub-setup, queue **sys.frequently**, admin-adjustable.
- Proposed setting **“Fetch access request using API”** with **default false**; only when enabled does the new flow run.
- **Risk** in the work item: existing **e-mail scanner job must be disabled** when API-based import is enabled so **duplicates** do not occur.
- Related work mentioned: **#291988** (v2 XML / SystemID), **PR 78603** (save e-mail body as remark), Digdir example **https://docs.digdir.no/docs/eFormidling/Utvikling/Eksempel/innsynskrav**

**Answers you can give carefully:**

- **“Standard for all online or cloud customers?”** The story does **not** state universal rollout. It is **backlog** work on IFAR import. Actual scope (which editions, which regions, on-prem vs online) is **not** decided in the fields read here. **Do not** promise “all customers” without a PM or release note.
- **“Paid module or integration?”** Nothing in the fetched **Description** or **Acceptance Criteria** frames this as a **separate SKU**. It sits under **core BL / IFAR** area. **Commercial packaging is unverified** from this work item alone; sales or PM must confirm.
- **“Automatic or every customer must change?”** The draft design is **opt in**: new property **default false**, admin enables API fetch and must align with **disabling** the scanner to avoid duplicates. So it is **not** “automatic for everyone” in the described design.
- **“US said 6.8, still valid?”** The item is tagged **6.9** as of fetch. **Correct the version label** when you reply, or explain that **tags are planning hints** and the **delivery train** is decided at release planning, not by the tag alone.

### 2. Wiki and Ratatoskr (help center)

**Wiki** (Software Innovation) search hits tie eInnsyn to the **Digdir integration point** at a high level (for example product teams and release material); they do **not** replace the need for a **current roadmap sentence** from PM or release notes for US 293365.

Examples:

https://wiki.software-innovation.com/wiki/Product_teams

https://wiki.software-innovation.com/wiki/6.8_release_information

**Ratatoskr** (admin-en / release corpus used here): **no** topic hits for the exact phrases **“eInnsyn integration point”** or **“Exchange Web Services”** in the searches run for this note. Admin help still documents the **Access request Mail Scanner** path for IFAR; that is the **today** documented operational path until a shipped release documents the API connector.

Reference already useful for “today” IFAR mail scanner:

https://help.360online.com/6.8.0000/SIAdminHelp/1033/Index.html#!Documents/accessrequestmailscanner.htm

### 3. Exchange Web Services (EWS) and “our plans”

**Microsoft’s direction (external, verify dates on official pages before you quote exact months in a contract):**

Microsoft is **retiring EWS for Exchange Online** in favour of **Microsoft Graph** and related APIs. Use Microsoft’s own pages for dates and tenant controls, for example:

https://aka.ms/ews1pageGH

https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/deprecation-of-basic-authentication-exchange-online

**Public 360° product position:** **Not** found in User Story **293365** or Feature **281011** text from this fetch. **IFAR mail scanner** depends on an **e-mail** path; whether your organisation moves customers to **Graph**, **OAuth**-based mail access, or another channel is a **delivery and advisory** topic. **Assign to R&D, PM, or specialist mail integration** for a customer-safe statement. Do **not** invent an internal “compensation plan” from this research alone.

---

## Risks and Limitations

- **Backlog ≠ committed scope or date.** State **New** means the connector story is **not** a shipped commitment in ADO as read.
- **Tags are not a contract.** **6.9** on the story is a planning hint; roadmap and release notes override it.
- **EWS:** timelines and tenant controls are **Microsoft’s**; your answer should **link Learn** and separate **Microsoft facts** from **Tietoevry product actions** once the product team confirms them.

## References

- https://tieto-si.visualstudio.com/360/_workitems/edit/293365
- https://tieto-si.visualstudio.com/360/_workitems/edit/281011
- https://docs.digdir.no/docs/eFormidling/Utvikling/Eksempel/innsynskrav
- https://help.360online.com/6.8.0000/SIAdminHelp/1033/Index.html#!Documents/accessrequestmailscanner.htm
- https://wiki.software-innovation.com/wiki/Product_teams
- https://wiki.software-innovation.com/wiki/6.8_release_information
- https://aka.ms/ews1pageGH
- https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/deprecation-of-basic-authentication-exchange-online
