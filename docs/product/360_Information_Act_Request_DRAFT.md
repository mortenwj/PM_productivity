# DRAFT: Updated 360° Information Act Request Module Page

## Complete Updated Wiki Content

```wikitext
{| cellpadding="0" cellspacing="0" width="100%"
|-
| style="vertical-align:top" |
<div style="margin: 0 10px 0 0; border: 2px solid #0E76B7; padding: 0em 1em 1em 1em; background-color: #FFFDCA;">
==Key info==
Product number:''' 125877'''. 

* Applies to version(s):''' 360° version 4.1 Service Pack 8 or newer ''' (Note: Many recent features require version 5.16+ or 6.0+)
* Availability: Available in all countries. By default configured without public configuration for all setups. Please note that ''Process Based Classification (PBC)'' and ''FIN'' ''Sähke2 configuration'' are not yet supported. 
* Other requirements: 
** [[360° Format Converter]] must be installed to be able to convert files to PDF before dispatch. 
** [[360° File Viewer]] version 1.1 or later is required in order to use redaction.
* Page last updated:  '''{{REVISIONDAY}}.{{REVISIONMONTH}}.{{REVISIONYEAR}}'''.  
</div><br> 

<div style="margin: 0 10px 0 0; border: 2px solid #0E76B7; padding: 0em 1em 1em 1em; background-color: #FFFFFF;">

== Product information==
{{PSNote}}
The Freedom of Information Act states that anyone has the right to apply for access to information or a document that was created by or sent to a public authority and included in the case management process. An increasing number of requests are being made, putting pressure on the organizations that process them. 

With the ''360° Information Act Requests'' module, your organization gets support throughout the process of handling requests for document access. Requests can be created manually, or automatically if opened up for submittal of requests from an Internet portal or a general mailbox (e.g. the Norwegian government www.eInnsyn.no website). 360° Information Act Requests is integrated with the [[360° Public Journal]] module.

The module focuses in the complete process in handling access requests - supporting all aspects of the flow.

The module also handles access requests in entire cases/topics. You can create a request on basis of an existing case, and automatically create requests for all the documents residing on that particular case, or manually add specific document requests to the access request case. The module handles all documentation created as part of the case process - correspondence with the requester, internal memos, etc.

When the request is reviewed and a decision is made, the response can be dispatched directly from 360° to the requester. Response is generated as a regular outbound document, supporting the possibility to send the response for approval; before actual sending. When request(s) are granted or partially-granted, the requested files will automatically be merged into a single PDF when dispatched.

Note that to be able to convert files to PDF before dispatch, [[360° Format Converter]] must be installed.

The module supports online Redaction (hiding sensitive information) as part of the process when 360° File Viewer is installed. By using the [[360° File Viewer]], the user can black out sections of a document containing classified or sensitive information, such as banking info, financial records or citizen identification id's. 

The module also contains reports giving your organization an overview of:
* Number of requests granted, partially-granted and declined in a given period per department
* Average processing time for the request for a given department
* Number of requests per paragraph per department

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

==== What's new in which version====
'''Version 6.7 (December 2025)''':<BR>
* Access Request Reports now available for eArchive 360° servers
* Create reports from eArchive document/file search
* Create reports from Saved Searches in eArchive
* Requires feature toggles: IfarReportsEarchive and IfarReportUseLocalConversionForSeparators
* Requires setting: requestforaccess.reportoverviewforsmallifarcases (not set to "No")
Read more: [[6.7_release_information#360° Information Act Request: Access Request Reports]]

'''Version 6.2 (May 2024)''':<BR>
* Notification icon displayed when a newer file version exists for the selected file
* File versions active in Request for Access cases can no longer be deleted
* Request for access activities automatically closed when partial reply is dispatched
* New setting for AutoIfar responsibility handling (requestforaccess.responsibleforautoifar)
Read more: [[6.2_release_information#360° Information Act Request]]

'''Version 5.18 (January 2024)''':<BR>
* Notification if Access Request case cannot be closed after dispatch (when other documents not signed off or progress plans open)
* New setting to anonymize file titles in response documents (requestforaccess.anonymizefiletitles)
* Four different response templates per language (with/without anonymization, with/without comments column)
Read more: [[5.18_release_information#360° Information Act Request]]

'''Version 6.0''':<BR>
Notification will be created if the Access Request case can not be closed at dispatch.<BR>
Read more: [[6.0_release_information#Request_for_Document_Access]]

'''Version 5.17''':<BR>
* Report overview on reply document for Access Request cases
* New notification for expired Request for Access cases
* Selection of file version for Request for access
* Implemented support for previewing Request for Access response letters
* Changed visibility of the redact button in the Requests section
* Changes in email scanner configuration
Read more: [[5.17_release_information#Request_for_Document_Access]]

'''Version 5.16''':<BR>
* Possibility to work with large Act requests using [[Request for Access reports and shared document searches]]
* Large file dispatching over email [[Request for Access Large file dispatch]]
* Sharing saved Document and file searches for collaboration
* Paragraphs related to historic access request decisions now listed in "Previous request" section
* Expanded purge functionality to include Request for Access Activities

'''Version 5.15''':<BR>
Fully automated processing of requests for access is included in the sub setup and separate installation should no longer be done

'''Version 5.10''':
Fully automated processing of requests for access (requires separate installation of process)

Functionality for specifying paragraph on file level

Expanded functionality for integration with eArchive 360[[360° Format Converter|°]]

Enhanced logging in WebAdmin Job view, displaying summary of each run or error meassages if any

'''Version 5.9'''<BR>
Possibility to attach AUTO IFAR process to mail scanner.

'''Version 5.8'''<BR>
From 360° version 5.8, the Access request Mail Scanner has been rewritten and included as a job in 360° Administrator.

'''Version 5.4'''<BR>
From 360° version 5.4, it is possible to manually add documents from ''eArchive 360°'' to an information act request case in ''Public 360°''.

'''Version 5.1'''<BR>
From 360° version 5.1, we introduced some improvements. Among others the possibility to make decisions on individual files, updated interface and the possibility to use two or more paragraphs. For further details, please refer to the [https://help.360online.com/5.3.0000/documentation/Release%20note%20360%20Version%205.1.0001.pdf 360° version 5.1 Release note].

=== Configuration Settings Reference ===
Key settings for Information Act Request module:

* '''requestforaccess.anonymizefiletitles''' - Control whether file titles are anonymized in response documents (default: "Yes")
* '''requestforaccess.responsibleforautoifar''' - Control responsibility handling for AutoIfar-processed cases (default: "Handle by responsibility matrix")
* '''requestforaccess.reportoverviewforsmallifarcases''' - Control report overview generation (options: No report, Simple report, Detailed report)
* Email scanner configuration - Email subject field is optional (all emails evaluated if not set)

=== Commercial aspects ===
{{Price model in 360°}}

=== Product documentation ===
Below, please find documentation developed and maintained by Enablement.

'''Product sheets '''
{| class="wikitable"
|[https://help.360online.com/360productsheets/Information%20Act%20Request/Information_Act_Request_DAN.PDF DAN] 
|[https://help.360online.com/360productsheets/Information%20Act%20Request/Information_Act_Request_ENG.PDF ENG]
|[https://help.360online.com/360productsheets/Information%20Act%20Request/Information_Act_Request_FIN.PDF FIN]
|[https://help.360online.com/360productsheets/Information%20Act%20Request/Information_Act_Request_NOR.PDF NOR]
|[https://help.360online.com/360productsheets/Information%20Act%20Request/Information_Act_Request_SWE.PDF SWE]
|}

'''End-user documentation ''' 
{| class="wikitable"
|[{{HelpPath}}/full_public_360/1030/360CompleteHelp/HH_Start.htm#?id=4100 DAN]
|[{{HelpPath}}/full_public_360/1033/360CompleteHelp/HH_Start.htm#?id=4100 ENG]
|FIN
|[{{HelpPath}}/full_public_360/1044/360CompleteHelp/HH_Start.htm#?id=4100 NOR]
|[{{HelpPath}}/full_public_360/1053/360CompleteHelp/HH_Start.htm#?id=4100 SWE]
|}

'''Additional material '''
* [https://si.business360online.com/locator/DMS/Document/Details/Simplified/200018?module=Document&subtype=200018&recno=392325&VerID=356832 Sales presentation] in internal 360°

| width="40%" style="vertical-align:top" |

<div style="margin: 0 10px 0 0; border: 2px solid #0E76B7; padding: 0em 1em 1em 1em; background-color: #E5F6FE;">

== Documentation from other units ==
Quality assurance relies on the individual departments owning the material.

=== Value proposition / Selling points ===
* Structured handling of the process for processing Information Act Requests. All applications are treated identically
* Documentation of the decision process.
* Online redactions – safe and fast
* Mass redactions for all occurrences of a name/social security number
* Tracking of completion time and open handlings
* Grant access to an entire document or to individual files
* Integrated to the dispatch module
* '''Handle very large access requests''' with automated report generation (Word overview + merged PDF)
* '''File version management''' with notifications and protection against accidental deletion
* '''Enhanced notifications''' for better case management (expired cases, unclosed cases, newer file versions)
* '''eArchive 360° integration''' for handling access requests on historical documents
* '''Anonymization options''' for response documents to protect sensitive information
* '''Preview functionality''' for response letters before dispatch
* '''Large file dispatch''' with secure download links for files exceeding email size limits

=== Implementation guidelines ===
* [[360° Information Act Request - Implementation guidelines]]

=== Service descriptions ===
[https://si.business360online.com/locator/DMS/File/CurrentRevisionFiles?recno=239202 Service Description - 360 Information Act Request]

=== Training material ===
* [https://si.business360online.com/locator.aspx?name=Common.Details.Navigate&module=Document&subtype=5&recno=368256 18-3337]

=== Additional material ===
* [[Product training sessions]] 
* [[Automatic IFAR process]] 
* [https://help.360online.com/360TechnicalDocuments/InformationActRequest/InformationActRequest-ResponsibilityFlow.pdf 360° Information Act Request - Resposibility flow - version 5.13] (Source file in internal 360° doc: 13-5840)
* [https://wiki.software-innovation.com/img_auth.php/4/4b/Request_for_access_-_Responsibility_flow5.14.pdf Request for access - Responsibility flow 5.14+]
* [[Request for Access reports and shared document searches]]
* [[Request for Access Large file dispatch]]
* Hotfixes and known issues: For hotfixes on the latest release, see [[Release Information]]. All hotfixes are published on {{360° Setups and Hotfixes}}.

===Nice to know===
* [[How to make IFAR Word template work in 5.10]]
* [https://help.360online.com/360TechnicalDocuments/InformationActRequest/InformationActRequest-ResponsibilityFlow.pdf 360° Information Act Request - Resposibility flow - version 5.13] (Source file in internal 360° doc: 13-5840)
* eArchive integration: Reports can be created from eArchive 360° when Request for Access is installed and feature toggles are enabled
* File version management: Select specific file versions, receive notifications for newer versions, and protect active versions from deletion

</div>

__NOTOC__
[[Category: Product information]]
|}
```

## Summary of Changes Made

### 1. **Updated "What's new" Section**
   - Added Version 6.7 (December 2025) with eArchive report support
   - Added Version 6.2 (May 2024) with file version management features
   - Added Version 5.18 (January 2024) with notifications and anonymization
   - Enhanced Version 5.16 entry with additional details

### 2. **New "Recent Enhancements" Section**
   - Highlights major improvements from 2023-2025
   - Organized by feature category for easy scanning

### 3. **New "Key Features" Section**
   - Organized into logical categories:
     - Request Management
     - Decision and Response
     - Reporting and Analytics
     - Automation

### 4. **New "Configuration Settings Reference" Section**
   - Quick reference for key settings
   - Includes default values and descriptions

### 5. **Enhanced "Value Proposition" Section**
   - Added 7 new selling points based on recent features
   - Emphasizes capabilities for large requests and automation

### 6. **Updated Version Requirements Note**
   - Added note that many recent features require version 5.16+ or 6.0+

### 7. **Enhanced "Nice to Know" Section**
   - Added practical tips about eArchive integration and file version management

### 8. **Improved Organization**
   - Better structure and flow
   - More comprehensive coverage of recent capabilities
   - Clearer separation between features and documentation

This draft is ready for review. It can be copied directly into the wiki page when approved.

