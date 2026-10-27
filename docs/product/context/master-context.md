# Master Context Document

Public 360° PM work. Working draft for internal ChatGPT project context and product-management content generation.

**Author:** Sebastian Reichmann / 03 2026

**Used sources:** 2026 Public 360° Business / Sales value messages; Public 360° online help resource; Archiving by Design d|lab report; Archive basic dictionary; Agile Product Management playbook; Reference cases research input.

**Projects / programs used in:** ChatGPT project(s); PM reference material; concept work such as Reference Cases; future product discovery and collateral programs.

**Review comments:** This document is intentionally stable and reusable. It should be updated only when core market, domain, governance, or PM framing changes materially.

## How to use this document

- Use this as the default context layer for PM work in Public 360° projects.
- Pair it with feature-specific discovery, customer input, roadmap themes, and implementation notes.
- Keep it broad enough to guide new work, but not so detailed that it becomes a maintenance burden.
- Do not treat it as a full product specification or a legal source of truth.

## 1. Business context

Public 360° is a purpose-built case, document, and records-management platform for the Nordic public sector. It is positioned as a long-term, public-sector-specialized product that supports efficient administration, compliant information handling, transparency, and stronger citizen services.

- **Primary market:** Nordic public sector, especially central government, local government / municipalities, education, and healthcare.
- **Business mission:** improve everyday work in the public sector for the good of citizen services.
- **Value proposition:** combine operational efficiency, records quality, compliance, transparency, and secure modernization in one connected platform.
- **Market characteristics:** high regulatory complexity, long procurement cycles, fragmented system landscapes, high trust expectations, and low tolerance for risky change.
- **Business model implication:** customers usually value dependable modernization, control, and public-sector fit more than novelty alone.

**Implication for PM work:**

- Frame value as a combination of efficiency, quality, compliance, transparency, safety, and trust.
- Avoid consumer-style product framing that assumes speed alone defines success.
- Show awareness of public-sector constraints without letting them prevent innovative solution thinking.

## 2. Product and domain context

Public 360° supports the operational chain from incoming information and registration to case handling, archiving, quality assurance, publishing, and collaboration. It should be treated as a workflow platform, a records-management platform, and a transparency-enabling platform at the same time.

### Core processes

- **Document Registration:** Receive, assess, classify, and register incoming or created content correctly; decide whether to connect to an existing case or create a new one.
- **Quality Assurance:** Verify metadata, access settings, privacy/sensitivity, publication readiness, and archive quality.
- **Case Management:** Create, connect, progress, and complete cases with correct traceability and decision support.
- **Publishing:** Make information available internally or externally in line with openness principles, restrictions, and public-access rules.
- **Collaboration:** Enable work across roles and tools while preserving records quality, control, and auditability.

### Core domain model

- **Case:** a structured container for handling a matter over time; connects documents, metadata, responsibility, and status.
- **Document:** a metadata entity representing a record unit, connected to zero or more files.
- **File / fulltext file:** the logical file object and the physical file content such as PDF, Word, or PowerPoint.
- **Archive:** the archive context that carries important business rules for how documents are handled.
- **Archiving:** the act of placing and committing a document into a proper archive so it becomes part of the visible formal record.
- **Restriction / access code / paragraph:** the concepts that govern lawful visibility limits and public access treatment.
- **Access group:** the role- and rights-based access context affecting who can see and work on cases and documents.
- **Channel:** the incoming source type, such as e-mail, forms, integrations, physical mail, Teams, or other systems.
- **Unregistered document:** content present in Public 360° but not yet fully committed and still awaiting archiving work.

**Domain reality for PM work:**

- The product is not just about storing information; it is about preserving usable, trustworthy, and governable records over time.
- Registration quality affects later search, reporting, publishing, follow-up, and decision quality.
- The product must support both operational task completion and long-term institutional accountability.

## 3. User and customer context

Different roles participate in the same end-to-end process but optimize for different outcomes. PM work should not write for a generic "user"; it should specify which role is being helped, which handoff is improved, and what downstream quality effect matters.

**Case worker**
- Goals: Understand context, prepare decisions, progress cases, find relevant history
- Pain points: Weak search, missing context, fragmented workflows, too much dependence on personal memory
- Success: Gets a complete enough picture quickly and can act with confidence

**Registrar / Archivist**
- Goals: Ensure correct registration, metadata quality, compliance, archive integrity
- Pain points: Unstructured input, many clicks, duplicate contacts, unclear case linkage, high manual effort
- Success: Registers correctly and efficiently with fewer corrections later

**Manager**
- Goals: Control workload, process quality, throughput, and compliance confidence
- Pain points: Weak visibility into quality problems, uneven practices, poor cross-role consistency
- Success: Can see quality and process status early and improve routines

**Board secretary**
- Goals: Prepare meetings, control agenda material, manage publication readiness
- Pain points: Scattered supporting documentation, version uncertainty, sensitivity handling effort
- Success: Has complete, controlled material ready for board and political workflows

**External users**
- Goals: Submit information securely, get timely handling, understand interaction
- Pain points: Fragmented digital experience, poor transparency, repeated requests for more information
- Success: Experience secure, understandable, and timely interaction

**Cross-role insight:**

- Case workers often optimize for progress and decision quality.
- Registrars and archivists optimize for archive quality, compliance, and publication correctness.
- Managers optimize for consistency, visibility, and controlled throughput.
- Good product design reduces friction between these goals instead of shifting work from one role to another.

## 4. Domain rules and governance principles

These rules should shape product decisions whether or not AI is involved.

### Hard constraints

- Auditability must be preserved.
- Archival integrity must be maintained.
- Role-based workflows are mandatory.
- Compliance with national standards and public-sector regulations is required.

### Soft constraints

- Standardization is preferred because it reduces error, improves retrieval, and supports training.
- Proven patterns dominate in high-trust environments; major change should remain understandable and governable.
- The product should move toward flexibility within constraints, not freedom without control.

### Default governance principles for PM work

- **Traceability by default:** important actions, decisions, and information relationships should be understandable after the fact.
- **Quality at the point of work:** the system should help users do the right thing in the workflow, not rely only on later correction.
- **Controlled openness:** support transparency and publishing while preserving lawful restrictions and privacy.
- **Role-aware responsibility:** workflows should clarify who decides, who quality-assures, and who owns the next step.
- **Long-term information value:** optimize not only for today's task, but also for later retrieval, review, and public accountability.

## 5. AI-specific governance principles

AI should be treated as a governed support capability layered onto the core Public 360° domain. It must follow the same domain rules as the rest of the product, plus additional safeguards.

- **Human agency:** AI augments human workers. Humans keep final authority, responsibility, and override ability.
- **Transparency:** AI interactions and suggestions must be clearly labeled and understandable.
- **Failover security:** Core software and operational workflows must remain usable if AI is unavailable or disabled.
- **Data privacy:** Apply strict data minimization, tenant isolation, and GDPR-aligned treatment for sensitive public data.
- **Non-discrimination:** Actively test for and mitigate biased or unfair outcomes across citizen groups and user contexts.
- **Auditability:** Keep logs of what AI suggested, what evidence or context informed it, and who made the final decision.
- **Robustness:** Protect models and workflows against manipulation, unsafe inputs, poisoning, and unauthorized change.
- **Feedback loops:** Provide easy ways for users to flag inaccurate outputs and support continuous learning and monitoring.

### Recommended AI role in Public 360°

- Good AI use cases: search support, summarization, classification support, linkage suggestions, registration support, quality-assurance support, and decision-preparation support.
- Poor AI use cases: silent autonomous decisions on critical domain actions, opaque recommendations, bypassing access/publication rules, or becoming a hard dependency for core operations.
- Every AI concept should define what remains human-controlled, how outputs are verified, and how failure or uncertainty is handled.

## 6. Product management working context / methodologies

PM work should stay problem-first, outcome-oriented, and traceable from business context to delivery. This document should help AI-generated PM content reflect a pragmatic operating model rather than a generic feature factory.

### Artifact framing rules

- **Epic:** A significant user problem with business context, desired value, scope now, risks, and measurable success criteria.
- **Epic press release / value statement:** A plain-language articulation of the promised user improvement and why it matters now.
- **User story:** A thin slice of user-visible value for a specific role, linked clearly to the parent epic.
- **Acceptance criteria:** Testable boundaries and important rules; not implementation detail.
- **Success criteria:** Outcome metrics, leading indicators, quality guardrails, and learning goals.
- **Roadmap item:** Business-facing narrative of sequence and priority; not a backlog dump.

### PM defaults for generated content

- Start with business context and user problem before describing solution shape.
- Show why the work matters now: customer pain, risk reduction, strategic fit, regulatory change, or quality impact.
- Frame acceptance criteria around real workflow behavior, permissions, traceability, and quality implications.
- For prioritization, weigh user pain, strategic importance, compliance risk, frequency, adoption likelihood, and feasibility.
- For discovery summaries, state the evidence, the affected role, the current workaround, and the opportunity to improve.

### Important anti-patterns to avoid

- Epic = feature name with no context.
- Roadmap = detailed backlog.
- User story = technical task with no user-visible intent.
- Success = shipped output only, with no outcome or guardrail.

## 7. Language, terminology, and output guidance

Use domain language that is correct enough for public-sector case and records management, but still understandable for product, design, and engineering teams that are not deep domain experts.

### Preferred writing style

- Clear, practical, and credible.
- Domain-aware but not overly legalistic.
- Explicit about role, workflow, and constraints.
- Outcome-oriented and non-hyped.
- Concrete enough for delivery teams to act on.

### Tone of voice for public-sector product collateral

- Professional and trustworthy rather than promotional or flashy.
- Confident but restrained; avoid exaggerated claims.
- Value-led and evidence-aware; show how the solution improves quality, control, efficiency, transparency, or citizen service.
- Respectful of public-sector responsibility, privacy, and governance expectations.
- When describing AI, be explicit about human control, explainability, and safe operational fit.

### Preferred expressions

case handling, records quality, archive quality, registration support, decision support, traceability, controlled publishing, role-based workflow, quality assurance, public-sector users, citizen service impact, secure modernization.

### Use carefully

When using any of these terms, clarify what the system does, what the user controls, how the output is validated, and what guardrails apply:

- automation
- assistant
- recommendation
- prediction
- intelligence

## 8. Short domain dictionary for software teams

Use these interpretations when drafting PM or technical material.

- **Case:** Structured container for handling a matter over time; not just a folder.
- **Document:** Registered information object with metadata and one or more related files.
- **File / Fulltext file:** The logical file object and the physical content file.
- **Archive:** The governing archival context that defines key business logic for handling records.
- **Archiving:** Committing content into the proper archive context so it becomes part of the formal record.
- **Archive-worthy:** Content that should be formally registered and preserved as part of the official record.
- **Restriction:** The rule context that influences whether information is available to the public.
- **Access code / paragraph:** Mechanisms used to define and justify restricted visibility.
- **Access group:** The access-control grouping affecting who can see and handle cases and documents.
- **Channel:** The source type for inbound content, such as e-mail, physical mail, forms, or integrations.
- **Unregistered document:** A document in the system that is not yet fully committed and still requires archiving work.
- **Reference case:** A prior case or related content item surfaced to support understanding, reuse, registration, or decision-making.

## 9. Boundaries and maintenance guidance

- Assume public-sector context, multiple roles, mixed process maturity, and a strong need to balance efficiency with correctness and control.
- Do not assume one customer workflow fits all, or that automation is inherently better than guided control.
- Keep this document stable. Update it when market positioning, core terminology, governance assumptions, or PM ways of working change materially.
- Keep feature-specific requirements, customer-specific nuances, and detailed solution design outside this master context document.

**Source basis used for this draft:** 2026 Public 360° Business / Sales value messages; P360 end-user help resource; Archiving by Design d|lab customer need assessment report; Archive basic dictionary; Agile Product Management playbook; Reference cases research input.
