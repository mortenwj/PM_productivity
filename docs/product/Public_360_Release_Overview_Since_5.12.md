# Public 360° Online – Upgrade Benefits: New Functionality and Modules Since Version 5.12

*This document summarises the benefits your organisation gains when upgrading from version 5.12 (April 2022) to the latest Public 360° Online release. It is intended to support upgrade discussions and business cases.*

---

## Executive Summary

Since version 5.12, Public 360° has seen **16+ new modules**, **100+ major improvements** across existing modules, and **significant enhancements** to core product capabilities. Upgrading provides:

- **Future-ready Microsoft 365 integration** – Including New Outlook support, cloud-based Office without local installation
- **Stronger privacy and quality assurance** – Archive Inspector, advanced access control, improved notifications
- **Higher productivity** – Workflow distribution groups, automated archiving, improved search
- **Modern digital services** – AI assistant (Mimir), Management Reporting API, advanced integrations
- **Lower cost of ownership** – Cloud-based Office, GEMI replacing shared mailbox import, reduced manual work

---

## 1. Microsoft 365 & Office Integration

### New Outlook Support (Version 6.4, February 2025)

**360° Integration with MS Office Apps now officially includes support for New Outlook.**

*Preparation began in version 6.3 (October 2024), when New Outlook was introduced as a pilot feature for selected customers. Version 6.4 made it generally available.*

- **Archive emails directly from New Outlook** using the new side panel hosted as an Azure microservice.
- **Full document registration wizard** – All registration fields available, same as Classic Outlook or browser.
- **No local 360° Client required** for basic archiving – works with Microsoft 365 cloud subscriptions.
- **Requirements:** 360° version 6.4 or newer, 360° Integration with MS Office Apps module. *V5 LTS is not supported.*

**Note:** Drag-and-drop for New Outlook on Windows is currently limited by Microsoft. Direct archiving into a case via drag-and-drop works on New Outlook for Mac when using Safari. Archive-to-Unregistered-documents from New Outlook is on the roadmap.

**Customer benefit:** Organisations moving to New Outlook can keep full 360° email archiving without reverting to Classic Outlook. Reduces reliance on locally installed Office and 360° Client for archiving.

### Cloud-Based Office Without Local Installation

- Work with Word, Excel, PowerPoint and Outlook Online – no need for expensive on-premises Microsoft Office licences.
- Save, edit and check in files directly from Office Online.
- Support for Mac and iPad.
- **Customer benefit:** Cheaper Microsoft 365 Apps licences, faster editing, device flexibility.

### Standard Texts in Word Online (Version 6.7, Pilot)

- Insert standard text files (docx) into Word Online documents.
- Administered from Template administrator in 360° – no network shares.
- **Customer benefit:** Standard texts available for Word Online users, better fit for cloud/SaaS setups.

### Outlook Side Panel – New Drop Zones

- **Separate documents** (5.15): One document for the email, separate documents for attachments.
- **Import to Unregistered documents** (5.16): Archive one or more emails quickly to Unregistered documents.
- **Customer benefit:** Faster archiving, clearer structure, fewer manual steps.

### Reply by Email in the Browser (Version 6.2)

- Send emails directly from 360° without 360° Client or Outlook.
- Outbound email automatically archived and shown in audit trail.
- **Customer benefit:** Supports Office Online and hybrid setups; fewer dependencies on local Outlook.

### Browser Support for Archiving Emails Directly into a Case (Version 6.2)

- Drag an email (.msg or .eml) onto the document wizard on a case – no Outlook side panel needed.
- Metadata (subject, contacts, attachments) extracted automatically.
- Single upload for email + attachments (instead of 11 uploads for 10 attachments via Client).
- **Customer benefit:** Faster archiving, works from any browser, fewer client installs.

---

## 2. New Modules (Full Release)

### 360° Integration with Navet (SE) – Version 5.12  
*Swedish people registry (Folkbokföringen)*

- Lookup citizens by national ID, name, address or date of birth.
- Import contacts from case, document and contact wizards.
- **Customer benefit:** Faster, more accurate contact data; fewer typing errors.

### 360° Integration with Det Centrale Personregister (CPR) (DAN) – Version 5.12  
*Danish CPR*

- Fetch and update contact data from CPR when creating contacts.
- Nightly CPR sync job (5.13).
- Protected persons and departed status clearly marked (5.13).
- **Customer benefit:** Correct, up-to-date citizen data; less manual entry.

### 360° Dispatch adapter: Suomi.fi (FI) – Version 5.12  
*Finnish government digital mail*

- Send digital mail to citizens and enterprises via Suomi.fi.
- Instant lookup of reachable recipients.
- **Customer benefit:** Faster, more secure external communication.

### 360° Archive Inspector – Version 5.13 (pilot) → 6.0 (GA)

- Detects personal and sensitive data in text and metadata.
- Flags Norwegian personal ID, bank accounts, passwords, health information.
- Review and screening in the 360° UI.
- **Version 6.0:** Regular vs full-archive scan, improved filtering, pagination, better metadata.
- **Version 6.2:** Health-word analysis, sensitivity statistics.
- **Version 6.7:** In-flow support in Unregistered Documents, smart context analysis for health info (SWE/DK pilot).
- **Customer benefit:** Stronger privacy and GDPR handling; clearer quality assurance and compliance.

### 360° Integration with SharePoint – Version 5.18 / 6.0

- Archive files from SharePoint team sites into 360°.
- Real-time archiving status in SharePoint.
- Two-way sync between SharePoint and 360°.
- **Version 6.2:** Import from 360° to SharePoint; archive without registration (centralised archiving).
- **Customer benefit:** One place for collaboration and archiving; less duplicate work.

### 360° Process library: Email archiving – Version 5.18 / 6.0

- Automatically archives emails imported by GEMI.
- Analyses subject lines for document/case numbers; files to existing cases or creates new ones.
- **Customer benefit:** Less manual archiving; faster processing of incoming mail.

### 360° Integration with Webcruiter (NOR) – Version 6.3

- Automatic archiving of recruitment documents from Webcruiter.
- Direct import via Webcruiter API; no external FTP server.
- **Customer benefit:** Fewer manual steps; better traceability and record-keeping.

### 360° Mimir – Version 6.4  
*AI platform assistant*

- Combines 360° help with your organisation’s policy documents.
- Natural language questions via a chat interface.
- Answers based on trusted sources; access control respected.
- Links to source documentation.
- **Customer benefit:** Quicker access to guidance; better compliance; less time searching.

### Management Reporting API – Version 6.7

- Extract data across any 360° entity for reporting and BI.
- Integrate with your own report tools and dashboards.
- **Customer benefit:** Full flexibility for management reporting; no custom coding per entity.

### 360° Sign – Version 5.16  
*Personal digital signing*

- Send documents for signing from Public 360°.
- Internal and external signers; status visible in 360°.
- **Version 6.7:** Norwegian Bank ID, BuyPass smart cards (pilot).
- **Customer benefit:** Simple, legally binding digital signing; fewer paper processes.

---

## 3. Email & Archiving

### Generic E-Mail Importer (GEMI) – Version 5.14

- Archive emails without Outlook or specific mail client.
- Multiple mailboxes; configurable rules.
- **Version 5.17:** IMAP; Gmail (app password); Google Workspace (OAuth2).
- **Version 6.3:** Microsoft Graph API, ADFS, NTLM.
- **Customer benefit:** Modern, flexible email archiving; replaces shared mailbox import.

### 360° AutoSaver – Version 6.2

- Configure automatic archiving without programming.
- Map external data to 360°; multiple archiving processes.
- **Version 6.3:** Contact handling, Archive Metadata File option, clearer error messages.
- **Version 6.7:** Schema Mapping UI (pilot).
- **Customer benefit:** Less manual archiving; more consistent quality; faster throughput.

---

## 4. Integration & Dispatch

### 360° Integration with Folkeregisteret (NO)

- **Version 5.14:** KS FIKS Lookup.
- **Version 5.18/6.0:** KS FIKS Update (synchronisation).
- **Version 6.7:** Postal address support; person/address code mapping; improved country handling.
- **Customer benefit:** Accurate citizen data; choice of Infotorg or KS; better control over special statuses.

### 360° Ekspedering adapter: SvarUt (NO)

- **Version 5.15:** Separate SvarUt channel for IFAR (Access Request).
- **Version 6.0:** SvarUt Sensitive channel; taushetsbelagt post.
- **Version 6.4:** KS eDialog – citizens can reply with messages and attachments.
- **Version 6.7:** Improved DPI and eFormidling status jobs.
- **Customer benefit:** Better handling of sensitive post; two-way communication with citizens.

### 360° Integration: SvarInn (NO)

- **Version 5.15–5.17:** Large zip decrypt (BouncyCastle, >100 MB).
- **Customer benefit:** Handles larger SvarInn batches; fewer failures.

### Power Automate Connector – Version 6.7

- Create unregistered documents from Power Automate.
- Works with AutoSaver for automatic case matching.
- **Customer benefit:** More integration options without raw HTTP/SIF coding.

---

## 5. Information Act Request (IFAR)

### Access Request Reports – Version 5.16

- Generate report overview (Word) and report content (merged PDF).
- From document/file search or from an Access Request case.
- Background processing; email with download links.
- **Version 6.7:** From eArchive; from Saved Searches.
- **Customer benefit:** Easier handling of large requests; clearer structure; fewer manual merges.

### Responsibility & Workflow

- **Version 5.13:** Redesigned email scanner responsibility logic.
- **Version 5.17:** Report overview on reply document; expired-case notifications; file version selection; preview; optional email subject.
- **Version 5.18/6.0:** Notification when case cannot be closed at dispatch; anonymise file titles setting.
- **Version 6.2:** Notification when newer file version exists; file version protection; AutoIfar responsibility setting.
- **Customer benefit:** Better control; fewer mistakes; clearer audit trail.

### Large File Dispatch – Version 5.16

- Dispatch large files via download link when file exceeds email limit.
- **Customer benefit:** Fewer failed dispatches; no need to split large responses.

---

## 6. Workflows & Approvals

### Workflow Distribution Groups – Version 5.13–5.14

- Send workflows to a group (e.g. all managers); one person picks up the task.
- Support for both approval and relay (e.g. secretary → manager).
- **Version 5.16:** Configure who may approve; managers pre-selected.
- **Version 5.17:** Take responsibility; show responsible person; mandatory approval before dispatch.
- **Version 6.7:** Distribution groups for progress plans (pilot).
- **Customer benefit:** Clearer delegation; fewer orphaned workflows; better role-based routing.

### Workflow Layout & UX

- **Version 5.13:** New workflow layout; instructions, recipients, documents on one page.
- **Version 5.14:** Reference material; mandatory reading; copy-recipient read task.
- **Version 5.15:** Separate documents dropzone; mandatory main-file reading.
- **Version 5.16:** PDF viewer choice (Accusoft for redaction; PDF.js for speed).
- **Version 5.17:** Workflow section on document detail view.
- **Customer benefit:** Faster task handling; better overview; fewer errors.

---

## 7. Search & Discovery

### Advanced Elastic Search – Version 5.14 (pilot) → 6.0 (GA)

- Search across cases, documents, contacts, files.
- **Version 5.16:** Metadata + file content (pilot).
- **Version 5.17:** Index config; QuickSearchConfig; AES improvements.
- **Version 6.0:** Default for migrated customers; exact match; improved phrase search.
- **Customer benefit:** More relevant results; search in file content; better control over indexing.

### Public File Links – Version 5.13 (pilot) → 5.16 (GA)

- Create shareable links to files in 360°.
- **Version 5.17:** Option to include file name.
- **Customer benefit:** Easy sharing (intranet, guidelines); no duplicate uploads.

---

## 8. Notifications & Follow-Up

### Notification Center – Version 5.12 (pilot) → 5.13 (GA)

- All notifications in one panel; filter by type; mark read/unread.
- **Version 5.14:** Follow cases and documents; administrator defaults; new macros.
- **Version 5.15:** Email notifications for follow; due date expiring today.
- **Version 5.17:** Shared item comment notifications.
- **Customer benefit:** Better overview; less email clutter; fewer missed items.

### Notifications for Failed Jobs & Inactive Cases – Version 5.18/6.0

- Notify when system jobs fail.
- Notify when cases have been inactive for a configured number of days.
- **Customer benefit:** Earlier detection of problems and stalled cases.

### Follow Saved Searches – Version 5.18/6.0

- Subscribe to saved searches; get notifications when results change.
- **Customer benefit:** Stay updated on specific topics without manual checks.

### Redesigned Reminders – Version 5.18/6.0

- Reminder notifications before due date.
- Share reminders with responsible person, internal contacts, managers.
- **Customer benefit:** Better follow-up; shared deadlines.

---

## 9. Unregistered Documents

- **Version 5.16:** Bulk edit (pilot).
- **Version 5.18/6.0:** Edit and bulk edit GA; new default access matrix.
- **Version 6.2:** New filter section; registration category.
- **Version 6.3:** Large file upload (chunk-based); source filter; PDF.js preview; Download all.
- **Version 6.4:** Default sort; document date/responsible unit saved; case-level unregistered contact search.
- **Version 6.7:** Responsible Unit filter; timestamp on Created Date.
- **Customer benefit:** Faster registration; better filtering; support for large files.

---

## 10. File Viewer & Document Handling

### 360° File Viewer

- **Version 5.13:** Image tools; proximity search (PrizmDoc 13.20).
- **Version 5.17:** PrizmDoc 13.23; blacklisted file types.
- **Version 6.0:** Rotate pages and upload to 360°.
- **Version 6.3:** PrizmDoc 14.0.
- **Version 6.7:** PrizmDoc 14.5.
- **Customer benefit:** Better viewing; security updates; rotate and save corrections.

### Large Files – Version 6.3–6.4

- Upload files over 2 GB; chunk-based upload; progress bar; abort option.
- **Customer benefit:** Support for media and other large files; fewer failed uploads.

---

## 11. MS Teams Integration

- **Version 5.12:** Save to existing documents; search documents; improved permissions.
- **Version 5.16:** Revision documents; enable/disable import.
- **Version 5.17:** Option to prevent import of restricted documents.
- **Version 6.7:** Progress updates for large imports; better meeting archiving; automatic case binding.
- **Customer benefit:** Smoother collaboration; better control over restricted content; clearer import status.

---

## 12. Administration & Configuration

### 360° Administrator

- **Version 5.14:** 360° Meta Admin in web (replacing MMC for meta).
- **Version 5.16:** React codetable admin.
- **Version 5.17:** GEMI IMAP; user audit for Project; notification subscription review; blacklisted file types.
- **Version 6.3:** Access Control Extension; read-only Access Control view.
- **Version 6.4:** SCIM with Omada; grace period for closing cases; webhook for case insert/update (pilot).
- **Version 6.6:** Improved regenerate permission (pilot).
- **Version 6.7:** Users unavailable for assignment; cancellation reason; classification periodization controls.
- **Customer benefit:** More configuration in browser; fewer MMC dependencies; better automation options.

### Grace Period for Closing Cases – Version 6.4

- Configure a period after “Closed” before cases get a final status.
- Nightly job updates status after the delay.
- **Customer benefit:** Time for last changes; stricter control over closed cases.

---

## 13. eArchive 360°

- **Version 5.12:** Grant read permissions; series removed from case/doc number; SIF ImportedCaseNumber/ImportedDocumentNumber.
- **Version 5.15:** SAPA export (FIN); Estate/Project support (pilot).
- **Version 5.16:** Copy document from eArchive GA.
- **Version 6.0:** Workflow display; custom fields (pilot).
- **Version 6.2:** Unregistered documents web part; scanning into eArchive.
- **Version 6.3:** Custom fields GA; saved search edit/delete.
- **Version 6.4:** Project detail view config; strike-through for cancelled.
- **Version 6.7:** Restrict permission granting for non-registrar roles; Access Request Reports from eArchive.
- **Customer benefit:** More flexible archive; better integration with Public 360°; stronger access control.

---

## 14. Mobile & Stand-In

### 360° eManager – Version 6.7 (New App)

- Document viewing (QuickLook); sharing; offline mode.
- Conditional Access and device compliance.
- Stand-in workflows; workflow distribution groups.
- Landscape mode; push notifications; document editing.
- **Customer benefit:** Full manager workflow on mobile; works offline; better security.

### Extended Stand-In – Version 6.0 (GA)

- Stand-in can act for colleagues on cases, documents and workflows.
- **Customer benefit:** Coverage during absence; fewer blocked workflows.

---

## 15. Technical & Security

- **Version 5.12:** Client WebView2 (Edge); MailKit; ASP.NET Core 6.
- **Version 5.14:** Internet Explorer blocked; Basic MessageQueue (RabbitMQ).
- **Version 6.0:** Tika file metadata; signed file detection.
- **Version 6.3:** Cipher hardening; pdf.js 4.2.67.
- **Version 6.7:** SIF OpenAPI; SIF RabbitMQ Event System (pilot).
- **Customer benefit:** Modern tech stack; better security; clearer integration options.

---

## Release Timeline

| Version | Release Date | Type |
|---------|--------------|------|
| 5.12 | 2022-04-29 | On-prem |
| 5.13 | 2022-06-27 | On-prem |
| 5.14 | 2022-10-11 | On-prem |
| 5.15 | 2022-12-22 | On-prem |
| 5.16 | 2023-03-08 | On-prem |
| 5.17 | 2023-06-26 | On-prem |
| 5.18 (LTS) | 2024-01-18 | On-prem LTS |
| 6.0 | 2024-01-04 | 360° Online |
| 6.2 | 2024-05-22 | 360° Online |
| 6.3 | 2024-10-22 | 360° Online |
| 6.4 | 2025-02-24 | 360° Online |
| 6.5 | 2025-06-02 | 360° Online |
| 6.6 | 2025-09-02 | 360° Online |
| 6.7 | 2025-11-28 | 360° Online |

---

## Planned Releases

- **6.8** – February 2026
- **6.9** – Dedicated eDoc release, April 2026
- **6.10** – Functionality release, May 2026

---

*Based on release information from the Public 360° wiki. For full details, see the [Release Information](https://help.360online.com/Release_information/Index.html) page and individual release notes.*
