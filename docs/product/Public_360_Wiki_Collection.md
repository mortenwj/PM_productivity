# Public 360° – Wiki Content Collection for LLM Processing

**Purpose:** High-level description, main use cases, personas, and jobs to be done.  
**Source:** Public 360° wiki (MediaWiki).  
**Principle:** More is more – comprehensive collection for downstream LLM processing.

---

## 1. High-Level Description

### 1.1 Core Product Definition

**Public 360°** enables more efficient, transparent and cutting-edge digital administration processes, collaboration and citizen dialogues. As a case and records management system, it meets internationally recognized standards for information security and archiving.

**From Public 360° product page:**
- Product numbers: 126106 (online), 125837 (on-premise)
- Availability: All countries
- Public 360° can be installed with Danish, Finnish, Norwegian or Swedish setup. Main features are the same for all setups, but there are differences in code tables, settings and access matrices.

### 1.2 What is 360°? (OnBoarding FAQ)

360° is an ECM system and a platform for an information management system. The most common and "out-of-the-box" implementation is a case and document management system.

Each Nordic country has a national standard for how they archive public records. The version "Public 360" has a pre-defined setup for each country to make the application comply with these standards and regulations.

**In many ways you can say that Public 360 supports the foundation of democracy; it contributes and helps the Public sector to enforce transparency.**

### 1.3 Public 360° vs Business 360°

- **Public 360°** – Used by customers in the public sector (municipalities, counties, etc.)
- **Business 360°** – Aimed at the private sector. A more "lightweight" version since NOARK standards are not required in private companies.

### 1.4 360° vs 360° Online

- **360°** – On-premise installation of Public/Business 360° at customers
- **360° Online** – Cloud offer to mainly smaller businesses in both public and private sector. Monthly payment per license. Lower price than on-premise but generates revenue over longer time.

### 1.5 Product Family

The 360° product family has four main products (Lead offerings):

1. **Public 360°**
2. **Business 360°**
3. **eArchive 360°**
4. **Plan & Build 360°**
5. **RDF 360°** – Not yet released

All products can be installed separately; additional modules can be added for more functionality.

### 1.6 Mission (Digitalization Journey)

*"We want to be the preferred and trusted partner for a larger part of our customers value chain, by helping our customers make value-based decisions about digitalization and continuous improvements in the Public 360° ecosystem."*

*"Thereby enabling the Tieto Strategy: 'Make customers more competitive' by co-creating business outcomes and deliver great everyday experiences to all stakeholders."*

---

## 2. Main Use Cases

### 2.1 Case and Document Management

- Case and records management
- Document management
- File management
- Case handling processes
- Case types (varies by setup and add-on modules)

### 2.2 Transparency and Open Government

**360° OpenGov Cases and Documents:**
- Publishes case information, documents, and files from Public 360°, Plan & Build 360°, and eArchive 360° in a unified portal
- Fosters increased transparency – a cornerstone of democratic integrity
- Publishing options: Semi-automatic, Fully automatic, Hybrid
- Request for access: Citizens and journalists can request access to restricted documents via registration form

**360° Information Act Request:**
- Handles requests for document access (Freedom of Information Act)
- Supports manual or automatic request creation (portals, email scanners)
- Supports entire cases or individual documents
- Online redaction, response dispatch, reporting

**360° Public Journal:**
- Public journal functionality (being replaced by OpenGov 2.0)

### 2.3 Digital Communication and Dispatch

- 360° Integration: SvarInn (NO)
- 360° Dispatch adapter: SvarUt (NO)
- 360° Dispatch adapter: DPI (NO)
- 360° Dispatch adapter: eFormidling (NO)
- 360° Dispatch adapter: Mina meddelanden (SE)
- 360° Dispatch adapter: Suomi.fi (FI)
- 360° Dispatch adapter: Deltagon (FI)
- 360° Integration with NgDP (DK)

### 2.4 Board and Meeting Management

- 360° Board & Council Manager (Public)
- 360° Decision tracking
- 360° eMeetings Prepare
- 360° eMeetings Live
- 360° Meeting management (business)
- 360° eManager

### 2.5 Process Automation and Workflow

**Process Engine:**
- Part of Public 360; enables easier development and deployment of custom processes
- Used in events, jobs, progress plans, webservices
- Shipped with standard – no separate module installation required (for processes without custom code)

**360° Process definition with simulation:**
- Investigate customer case handling processes
- Define and modify case management processes
- Document processes in detail
- Simulate processes in 360° to educate customers

### 2.6 Archiving and Records Management

**eArchive 360°:**
- Stand-alone records management solution
- Safe-keeping of digital information
- Medium and long-term storage
- XML import/export framework
- OAIS standard
- Hierarchical content structure

### 2.7 Plan & Build (Construction Cases)

**Plan & Build 360°:**
- Solution for processing building applications in public sector
- Norway: eByggesak standard version 2.1 (KS, DiBK)
- Case types: Construction, Dividing, Complaint, Supervision, Illegality, Requests, Planning, Surveying

### 2.8 Data Collection and eServices

**360° Collect:**
- Automates and secures data collection
- Replaces fragmented form workflows
- Integrated, cloud-based platform
- Connects to existing systems
- Ideal for municipalities and agencies digitizing services quickly

**360° eServices Platform / 360° eServices Connect:**
- eService integration

### 2.9 Integration Use Cases

- Central registries (Enhetsregisteret, Folkeregisteret, CPR, CVR, Navet)
- MS Office Apps integration
- MS Teams integration
- SharePoint integration
- Webcruiter integration
- Power Automate Connector
- SIF (Simple Integration Framework)
- Fiks Arkiv

---

## 3. Personas and Roles

### 3.1 Internal Roles (Public 360 Roles Overview)

**Products & Technology:**
- Product Manager (Empowered Product Team)
- Lead Product Designer
- UX Designer
- Public 360 Business Developer
- Public 360 Release Manager
- Public 360 Technical Documentation Specialist
- Public 360 Software Architect
- Public 360 Software Engineer
- Public 360 Test Engineer
- Public 360 Test Manager
- Public 360 Technical Lead (Empowered Teams)
- Public 360 Customer Support Specialist
- Public 360 Continuous Service Manager
- Public 360 Technical Specialist Production IT
- Public 360 Security Manager

**Professional Services:**
- Public 360° Consulting Line Manager
- Public 360° Project Manager
- Public 360° Solution Consultant
- Public 360° Delivery Manager
- Public 360 Solution Architect
- Public 360 Technical Consulting Developer
- Public 360 Deployer

**Sales:**
- Public 360° Head of Sales Country
- Public 360° Bid Manager
- Public 360° Sales Manager

**Cross functional:**
- Public 360° Process Lead and Quality SPOC
- Public 360 Privacy Manager

### 3.2 Customer User Types (from Training, Module Pages, Implementation Guidelines)

**Source:** Customer training and courses, module implementation guidelines, service descriptions, OpenGov FAQ.

#### Core user roles (from standard courses)

| Role | Description | Typical tasks |
|------|-------------|---------------|
| **Case worker** | Day-to-day case and document handling | Create cases and documents, use workflows, dispatch, reply/sign off. Basic document handling. |
| **Registrar** | Archive/case management specialist | Worklists, search, case/document handling, move and copy documents, mass update, quality assurance. Document distribution. |
| **Administrator** | System configuration | Users, access groups, configuration, code tables. |
| **User administrator** | User management | User administration (subset of Administrator). |
| **Archivist** | Archive specialist (eArchive, quality assurance) | Quality assurance for archivists, document registration, publish/depublish for OpenGov. In eArchive: "Permanently delete" option only for Registrar role. |
| **Board secretary** | Board and council administration | Prepare and administer meetings, follow up afterwork for boards, councils, political and non-political committees. |
| **Manager** | Managerial role | Manager dashboard, allocation of cases/documents/tasks, approvals, statistics and reports, administration of deputies, rights and access control. |

**Note:** Course environment (Norway) distinguishes: Kurs Bruker 1–10 = Case worker only; Kurs Bruker 11–22 = Caseworker, Registrar, Administrator, User administrator, Board secretary, Manager (content for Registrar/Admin/Board/Manager roles); Kurs Bruker 23–35 = all roles with content for Caseworker, Registrar, Administrator, Board secretary, Manager.

**Access control (5.17):** "Enduser roles" explicitly listed as caseworker, archivist, leader and board secretaries – each may need separate access groups/mappings.

#### Project and implementation roles (customer side)

| Role | Description | Source |
|------|-------------|--------|
| **Solution manager** | Customer responsible for solution work | Configuration workshop: "Solution manager and people involved in solution work must participate" (Implementation Process) |
| **Project group** | Customer project team | Training for project group before solution work. "Everyone who is to take part in solution work and tests must participate" in Basic and Admin training. |
| **Archive leader** | Customer archive/records lead | IFAR workshop: "Customer participation: Archive leader" |
| **Department leader** | Head of department, SME | Process definition with simulation: "At least registrars, common users and dept leader/s of the chosen department (SMEs) are needed" |
| **Super users** | Power users who deliver internal training | Train the trainer: "Super users who will deliver internal training in the Service" |
| **Testers** | Customer testers | "Testers from the customer needed to verify configuration" (Policy Documents) |

#### Module-specific user types

| Module | User types mentioned | Source |
|--------|----------------------|--------|
| **360° Policy Documents** | Registrars, managers, case workers who develop/distribute policy documents. Training: "Most likely registrars and managers who will distribute" | Implementation guidelines |
| **360° Information Act Request** | Archive leader (workshop). Handlers of access requests. | Implementation guidelines |
| **360° OpenGov** | Publishing/depublishing: "Specific roles (e.g. Archivist)". Configuration: administrators (webadmin). Design: "Dedicated users that get an account in the admin portal". End users: Citizens, journalists | OpenGov FAQ |
| **360° eManager** | Leaders (CxO level). "Optimized to specifically support the work of leaders". "Users who need to approve documents and workflows". "Manager/director" for meeting materials | eManager product page |
| **360° Board & Council Manager** | Board secretaries, meeting participants. "Organizations where a large proportion of decision-making takes place at formal meetings" | Board & Council Manager |
| **360° Floor walking / Open sessions** | "Selected user groups, such as super users and managers" | Customer training for sale |
| **eArchive 360°** | Registrar (archivist) vs non-Registrar. "Permanently delete" only for Registrar. Non-Registrar: Read/View File only when LimitEarchiveAccessForRolesOtherThanArchivist enabled | eArchive, 6.6/6.7 release |

#### External / citizen user types

| Type | Description | Context |
|------|-------------|---------|
| **Citizens** | Request access to documents, use eServices, view published content | OpenGov, Information Act Request, 360° Collect |
| **Journalists** | Request document access, view published content | OpenGov FAQ: "Are the journalists also the direct users? Yes" |
| **Politicians** | Board/council members. OpenGov: "Control what information is published about a politician, per politician" | Board & Council, OpenGov |

#### Organization types (customer segments)

- **Municipalities** – Primary public sector customers
- **Counties** – Regional government
- **Government agencies** – National level
- **State customers** – eInnsyn often expected, partially subsidized (DigDir)

### 3.3 User roles by training course (Norway)

| Course | Target role | Duration |
|--------|-------------|----------|
| Basic course | Case worker | 3 hours |
| Advanced course | All users | 3 hours |
| Registrar course | Registrar | 3 hours |
| Administrator course | Administrator | 3 hours |
| Manager course | Manager | 2 hours |
| Board and Council Management | Board secretary | 5 hours |
| Access request course | IFAR handlers | 1.5 hours |
| Train the trainer | Super users | 2 days |

### 3.4 Implementation Process Intended Audience (Tieto)

- Sales Manager
- Technical Consulting Developer
- Technical Consulting Solution Architect
- Deployer
- Tester
- Delivery Manager
- Project Manager
- Solution Consultant

---

## 4. Jobs to Be Done

### 4.1 Customer Jobs (What Customers Hire Public 360° to Do)

**Efficiency:**
- Digitize case and document handling
- Automate manual workflows
- Reduce processing time
- Ensure compliance with archival standards (NOARK, etc.)

**Transparency:**
- Publish cases and documents publicly
- Handle Information Act / Freedom of Information requests
- Support democratic accountability

**Collaboration:**
- Manage board and council meetings
- Support citizen dialogues
- Enable collaboration in Microsoft 365 (Teams, SharePoint)

**Compliance and Security:**
- Meet information security standards
- Archive according to national regulations
- Handle sensitive data with redaction

**Integration:**
- Connect to national registries (Folkeregisteret, Enhetsregisteret, CPR, CVR, Navet)
- Integrate with digital post (SvarUt, SvarInn, eFormidling, etc.)
- Integrate with finance, HR, and other systems

### 4.2 Jobs from Service Descriptions

**360° In house advisory Services:**
- Implement Public 360 for the first time
- Optimize existing solution
- Strategic guidance and proactive recommendations
- Focus on core business activities with confidence

**360° Education:**
- Build knowledge and skills in Public 360°
- Maximize investment potential
- Smoother implementation and upgrade
- Better user adoption and satisfaction

**360° Gap-Analysis:**
- Analyse progress in use of Public 360°
- Identify adaptation to new system
- Identify need for more training
- Keep dialogue open after implementation

**360° Process definition with simulation:**
- Investigate case handling processes
- Scope project and process work
- Define and modify case management processes
- Support change management
- Educate users from process perspective

**360° Collect:**
- Automate data collection
- Ensure compliance
- Control costs (usage-based pricing)
- Deploy quickly without heavy IT lift

### 4.3 Jobs from Value Propositions

**360° Collect:**
- Save time – automate manual workflows, reduce delays
- Ensure compliance – security and governance built-in
- Control costs – transparent, usage-based pricing
- Deploy quickly – operational in weeks
- Easy to use – intuitive UI, minimal training

**360° OpenGov:**
- Publish information efficiently
- Increase transparency
- Balance quality assurance and automation
- Handle access requests

**360° Information Act Request:**
- Structured handling of access requests
- Document decision process
- Online redactions – safe and fast
- Track completion time
- Handle very large access requests

---

## 5. Module Categories (Public 360°)

### Basic
- 360° AD Sync Service
- 360° Dispatch (e-mail and print)
- 360° Template Designer
- 360° Format converter
- 360° Archive Format Validator

### Board and meeting management
- 360° Board & Council Manager (Public)
- 360° Decision tracking
- 360° eMeetings Prepare
- 360° eMeetings Live
- 360° Meeting management (business)
- 360° eManager

### Digital communication
- SvarInn, SvarUt, DPI, eFormidling, Mina meddelanden, NgDP, Suomi.fi, Deltagon

### Central registries
- Enhetsregisteret, Folkeregisteret, CVR, CPR, Navet, Cadastre

### Transparency
- 360° Information Act Request
- 360° OpenGov Cases and Documents
- 360° OpenGov Meetings
- 360° Public Journal
- 360° Public Journal File Server
- 360° Open Gov Cases/Webservices
- 360° eInnsyn Export (NO)
- 360° File Viewer

### Document management
- 360° Contract management
- 360° Policy documents with document distribution

### eServices
- 360° eServices Platform
- 360° eServices Connect

### Intelligent productivity platform
- 360° Archive Inspector
- 360° Mimir
- 360° Search Assistant

### Third party integration tools
- Power Automate Connector
- Simple Integration Framework (SIF)
- Fiks Arkiv
- GI Services
- Noark 4 Web service
- Package upload

### Process library and Archiving by design
- 360° Process library: Startskudd
- 360° Process library: EveryOne
- 360° Process library: Landbruksdirektoratet
- 360° Process library: Email archiving
- 360° AutoSaver
- 360° Integration with Webcruiter

### Collaboration in Microsoft 365
- 360° Integration with MS Teams
- 360° Integration with MS Office Apps
- 360° Integration with SharePoint
- 360° SharePoint Connect

### File management
- 360° Scanning
- 360° PDF Stamping
- 360° eSigning Connect
- 360° Sign
- 360° Sign Sweden

---

## 6. Service Offerings (Consultancy)

### Solution related
- Implementation (Public 360° or Plan & Build)
- Upgrade and migration to cloud
- Module implementations (per module pages)

### Value added
- 360° System Administration Services
- 360° Configure dashboards
- 360° Education (courses and training)
- 360° Floor walking
- 360° Data quality analysis
- 360° Quality assurance in archiving and records management
- 360° Process automation analysis
- 360° In house advisory Services
- 360° Facilitate customer days/meetings
- 360° Periodical division
- 360° Template designer course
- 360° Gap-Analysis
- 360° Access rules review
- 360° Integration service offering
- 360° Prestudy (for initiation phase)
- 360° Process definition with simulation
- 360° Municipality specific archival codes - update 2024
- 360° Advanced search tips & tricks

---

## 7. Product Teams (Development)

- **Core BL and eArchive** – Business logic, database, security, eArchive
- **Transparency** – OpenGov, eServices, Public Journal, Information Act Request
- **Core UI** – Uniform look & feel, wizards, desktops, workflows
- **Core Integration** – Integrations roadmap, SIF, Power Automate, Teams, SharePoint, Fiks Arkiv, registries
- **Decision Support** – Board and Council Manager, eMeetings, eManager, Contract management, Policy documents
- **Process Platform** – Information Act Requests, Process Engine, Process Management
- **Engage & Collect** – 360 Collect, 360 Engage, RDF, 360 Publish
- **Plan & Build** – Construction cases, Planning cases, Sweden setup
- **AI & Insights** – Archive Inspector, Mimir, Management Reporting API
- **Tech Platform Team** – Cloud Automation Factory, Infrastructure

---

## 8. Implementation Process Principles

1. **Methodology** – Systematic approach, waterfall default (agile for lighthouse projects)
2. **Approach** – Think big, start small, deploy fast
3. **Efficiency** – On time – on budget, profitable projects, minimized risk
4. **Similarity** – Employees perform activities in similar, proven way

### Milestones (MS1–MS8)
- MS1: Contract signed
- MS2: Project plan approved
- MS3: Environment installed and available for customer
- MS4: Solution description approved
- MS5: Solution ready for customer test
- MS6: Contract acceptance criteria fulfilled
- MS7: Solution live and available for end users
- MS8: Project contract fulfilled and project closed

---

## 9. Digitalization Journey (Concept)

Phases: **Initiation → Concepting → Detailing → Execution**

- Enter customer process early (ideation/concepting)
- Uncover what processes/services to prioritize
- Establish mutual consent
- Describe benefits potential before requirements and development
- Focus on benefits throughout
- Help customer prove ROI
- Combine Tieto product knowledge with customer process competence
- Reach CxO level – become preferred and trusted partner
- Product 360° is core of journey and main differentiator

---

## 10. Target Markets and Availability

- **Countries:** Denmark, Finland, Norway, Sweden (all Nordic)
- **Delivery forms:** SaaS (Public cloud, Domestic cloud), On-premise, Online for local installation
- **Plan & Build 360°:** Norway and Sweden only
- **360° Collect:** All markets, early release phase

---

## 11. Key Differentiators and Value Propositions

- **Democracy and transparency** – Supports foundation of democracy, enforces public sector transparency
- **National standards** – Pre-defined setups for NOARK and national archival standards
- **Integrated ecosystem** – Public 360°, Plan & Build, eArchive, RDF work together
- **Process Engine** – Custom process development and deployment
- **Transparency modules** – OpenGov, Information Act Request, Public Journal
- **Nordic focus** – Built for Nordic public sector requirements

---

## 12. Raw Wiki Snippets (Additional Context)

### From searches
- "Public 360 supports the foundation of democracy, it contributes and helps the Public sector to enforce transparency"
- "Public 360° enables more efficient, transparent and cutting-edge digital administration processes, collaboration and citizen dialogues"
- "360° Collect helps public organizations work faster, ensure compliance, and save money — without adding complexity"
- "The Transparency Team strengthens trust in public administration by ensuring both openness and the integrity of information"
- "360° OpenGov Cases and Documents enables customers to publicly share case information, documents, and files... fostering increased transparency— a cornerstone of democratic integrity"

### Case types (Plan & Build)
- Construction Case (Byggesak/Byggärende)
- Dividing Case (Delesak/Avstyckningsärende)
- Complaint Case (Klagesak/Överklagaärende)
- Supervision (Tilsynssak/Tillsynsärende)
- Illegality (Ulovlighet/Olovlighetsärende)
- Requests (Henvendelse/Förfrågan)
- Planning Cases (Plansak/Planärende)
- Surveying (Oppmålingssak/Kart- och mätärende)

---

## 13. Source Pages Referenced

| Page | Content Type |
|------|--------------|
| Welcome to the Public 360° wiki! | Overview, processes |
| Public 360° | Product info |
| Module overview | Modules, SPOCs |
| OnBoarding 360° consultants - FAQ | What is 360°, democracy |
| Public 360° Digitalization Journey | Mission, methodology |
| Public 360 Roles overview | Internal roles |
| 360° In house advisory Services | Value proposition, service |
| Product teams | Teams, modules |
| Consultancy | Services, processes |
| Implementation Process | Delivery process |
| 360° Collect | Value prop, use cases |
| 360° Education | Training, pedagogy |
| 360° Gap-Analysis | Post-implementation service |
| Process Engine | Custom processes |
| Service overview | Service catalogue |
| 360° OpenGov Cases and Documents | Transparency |
| 360° Information Act Request | Access requests |
| Plan & Build 360° | Construction cases |
| EArchive 360° | Records management |
| 360° Process definition with simulation | Process workshops |
| Product Development Process | Internal process |
| Customer training and courses | User roles, course environment |
| Customer training and courses Sweden | User roles (SWE) |
| Customer training and courses for sale | Course descriptions, Floor walking, Open sessions target groups |
| 360° Policy Documents - Implementation guidelines | Registrars, managers, case workers |
| 360° Information Act Request - Implementation guidelines | Archive leader |
| 360° OpenGov Cases and Document, Boards and Meetings FAQ | Archivist, administrators, citizens, journalists |
| 360° Floor walking | Super users, managers |
| 360° eManager | Leaders, CxO |

---

## 14. Appendix: Additional Search Context

### Workflow and case handling
- Progress plans, workflows configurable from 360 web admin
- Case types in Plan & Build: Building application, Dividing, Supervision, Illegality, Complaint, Request, Surveying, Sectioning, Address
- 360° AutoSaver: Archives emails to Public 360° with case (creates case if needed)
- Reply by email in 360° – creates "360° emails" linked to cases

### Delivery and deployment
- **SAAS:** 360° Online – Public SaaS or Domestic SaaS
- **LOCAL INSTALLATION:** Public 360° Online hosted in customer infrastructure
- **STANDARD WAY:** Configurations in production, verified there
- **PACKAGE WAY:** Configurations in internal test, packaged, deployed to environments

### Training and adoption
- 360° eLearning enables customers to complete courses in Public 360° and Plan & Build 360° online
- Basic training – Education for case worker (standard training for project group)
- Admin Training – Advanced User Training
- Pedagogical platform: Safe learning environments, User-centered learning, Active learning

---

*End of collection. Generated for LLM processing. Source: Public 360° wiki. Fetched via MediaWiki MCP, March 2026.*
