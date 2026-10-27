# Information Act Request Module Page - Update Sections

## Section 1: Update Key Info Section

**Location:** In the "Key info" box at the top

**Find this line:**
```
* Applies to version(s):''' 360° version 4.1 Service Pack 8 or newer '''
```

**Replace with:**
```
* Applies to version(s):''' 360° version 4.1 Service Pack 8 or newer ''' (Note: Many recent features require version 5.16+ or 6.0+)
```

---

## Section 2: Add Recent Enhancements Section

**Location:** Add this NEW section right after the bullet list about reports (after "Number of requests per paragraph per department") and BEFORE "==== What's new in which version===="

**Add this content:**
```
=== Recent Enhancements (2023-2025) ===
The Information Act Request module has received significant updates to improve handling of large requests, file version management, and eArchive integration:

* '''Access Request Reports''': Handle very large requests efficiently with automated report generation (Word overview + merged PDF). Reports can be created from document/file search, saved searches, or directly from Access Request cases. Now also available for eArchive 360° servers.
* '''eArchive Integration''': Reports now available for eArchive 360° servers, enabling access request handling for historical documents stored in eArchive.
* '''File Version Management''': Select specific file versions for requests, receive notifications when newer versions exist, and protection against deleting active file versions.
* '''Enhanced Notifications''': Automated notifications for expired cases, unclosed cases after dispatch, and newer file versions available.
* '''Response Document Improvements''': Preview functionality before dispatch, anonymization options for file titles, automatic report overview generation.
* '''Process Automation''': AutoIfar improvements with configurable responsibility handling, automatic closing of activities when partial replies are dispatched.

=== Key Features ===
==== Request Management ====
* Manual or automatic request creation (from portals, email scanners)
* Support for entire cases or individual documents
* File version selection and management
* Notification system for expired and unclosed cases
* Integration with eArchive 360° for historical documents

==== Decision and Response ====
* Individual file-level decisions
* Online redaction capabilities
* Preview response letters before dispatch
* Anonymization options for file titles in response documents
* Automatic PDF merging for granted/partially-granted requests
* Large file dispatch with download links (24-hour validity)
* Multiple response templates per language (with/without anonymization, with/without comments)

==== Reporting and Analytics ====
* Access Request Reports for large requests (Word overview + merged PDF)
* Reports available from document/file search and saved searches
* eArchive 360° report support
* Department-level statistics and processing time tracking
* Number of requests per paragraph per department

==== Automation ====
* AutoIfar process for automated request processing
* Auto-closing of activities when partial replies are dispatched
* Configurable responsibility handling for AutoIfar-processed cases
* Email scanner integration for automatic case creation
```

---

## Section 3: Update "What's new" Section - Add Version 6.7

**Location:** At the very top of the "==== What's new in which version====" section, BEFORE "'''Version 6.0''':"

**Add this:**
```
'''Version 6.7 (December 2025)''':<BR>
* Access Request Reports now available for eArchive 360° servers
* Create reports from eArchive document/file search
* Create reports from Saved Searches in eArchive
* Requires feature toggles: IfarReportsEarchive and IfarReportUseLocalConversionForSeparators
* Requires setting: requestforaccess.reportoverviewforsmallifarcases (not set to "No")
Read more: [[6.7_release_information#360° Information Act Request: Access Request Reports]]

```

---

## Section 4: Update "What's new" Section - Add Version 6.2

**Location:** After Version 6.7, BEFORE "'''Version 6.0''':"

**Add this:**
```
'''Version 6.2 (May 2024)''':<BR>
* Notification icon displayed when a newer file version exists for the selected file
* File versions active in Request for Access cases can no longer be deleted
* Request for access activities automatically closed when partial reply is dispatched
* New setting for AutoIfar responsibility handling (requestforaccess.responsibleforautoifar)
Read more: [[6.2_release_information#360° Information Act Request]]

```

---

## Section 5: Update "What's new" Section - Add Version 5.18

**Location:** After Version 6.2, BEFORE "'''Version 6.0''':"

**Add this:**
```
'''Version 5.18 (January 2024)''':<BR>
* Notification if Access Request case cannot be closed after dispatch (when other documents not signed off or progress plans open)
* New setting to anonymize file titles in response documents (requestforaccess.anonymizefiletitles)
* Four different response templates per language (with/without anonymization, with/without comments column)
Read more: [[5.18_release_information#360° Information Act Request]]

```

---

## Section 6: Update "What's new" Section - Enhance Version 5.16

**Location:** Find the existing "'''Version 5.16''':" section

**Find this:**
```
'''Version 5.16''':<BR>
* Possibility to work with large Act requests using [[Request for Access reports and shared document searches]]
* Large file dispatching over email [[Request for Access Large file dispatch]]
```

**Replace with:**
```
'''Version 5.16''':<BR>
* Possibility to work with large Act requests using [[Request for Access reports and shared document searches]]
* Large file dispatching over email [[Request for Access Large file dispatch]]
* Sharing saved Document and file searches for collaboration
* Paragraphs related to historic access request decisions now listed in "Previous request" section
* Expanded purge functionality to include Request for Access Activities
```

---

## Section 7: Add Configuration Settings Reference Section

**Location:** Add this NEW section right after "'''Version 5.1'''" and BEFORE "=== Commercial aspects ==="

**Add this:**
```
=== Configuration Settings Reference ===
Key settings for Information Act Request module:

* '''requestforaccess.anonymizefiletitles''' - Control whether file titles are anonymized in response documents (default: "Yes")
* '''requestforaccess.responsibleforautoifar''' - Control responsibility handling for AutoIfar-processed cases (default: "Handle by responsibility matrix")
* '''requestforaccess.reportoverviewforsmallifarcases''' - Control report overview generation (options: No report, Simple report, Detailed report)
* Email scanner configuration - Email subject field is optional (all emails evaluated if not set)
```

---

## Section 8: Update Value Proposition Section

**Location:** In the right column, find "=== Value proposition / Selling points ==="

**Find this list (at the end):**
```
* Integrated to the dispatch module
```

**Add these new items after it:**
```
* '''Handle very large access requests''' with automated report generation (Word overview + merged PDF)
* '''File version management''' with notifications and protection against accidental deletion
* '''Enhanced notifications''' for better case management (expired cases, unclosed cases, newer file versions)
* '''eArchive 360° integration''' for handling access requests on historical documents
* '''Anonymization options''' for response documents to protect sensitive information
* '''Preview functionality''' for response letters before dispatch
* '''Large file dispatch''' with secure download links for files exceeding email size limits
```

---

## Section 9: Update "Nice to know" Section

**Location:** At the bottom of the right column, find "===Nice to know==="

**Find this (at the end of the section):**
```
* [https://help.360online.com/360TechnicalDocuments/InformationActRequest/InformationActRequest-ResponsibilityFlow.pdf 360° Information Act Request - Resposibility flow - version 5.13] (Source file in internal 360° doc: 13-5840)
```

**Add these new items after it:**
```
* eArchive integration: Reports can be created from eArchive 360° when Request for Access is installed and feature toggles are enabled
* File version management: Select specific file versions, receive notifications for newer versions, and protect active versions from deletion
```

---

## Quick Reference: Update Order

1. ✅ Section 1: Update Key Info (add version note)
2. ✅ Section 2: Add Recent Enhancements + Key Features sections
3. ✅ Section 3: Add Version 6.7 to "What's new"
4. ✅ Section 4: Add Version 6.2 to "What's new"
5. ✅ Section 5: Add Version 5.18 to "What's new"
6. ✅ Section 6: Enhance Version 5.16 entry
7. ✅ Section 7: Add Configuration Settings Reference
8. ✅ Section 8: Update Value Proposition
9. ✅ Section 9: Update Nice to know

---

## Notes

- All sections are ready to copy-paste directly
- The wikitext formatting is preserved
- Links to release notes are included
- Each section can be updated independently















