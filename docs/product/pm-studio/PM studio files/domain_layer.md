# Artifact 2: Domain Layer

## Product Reality
Public 360 is a mature Nordic public-sector case and records management platform. It is infrastructure for public administration, not a generic SaaS tool.

## Domain Constraints
### Hard constraints
- Auditability must be preserved
- Archival integrity must be maintained
- Role-based workflows are mandatory
- Compliance with national standards

### Soft constraints
- Standardization preferred
- Proven patterns dominate
- Moving toward flexibility within constraints

## Core Mental Model
Case → Document → Workflow → Archive → Publish

## Core Process Areas
- Document Registration
- Quality Assurance
- Case Management
- Publishing
- Collaboration

## Core Objects
Case, Document, Workflow, Role, Archive, Access Request

## Personas
- Case worker
- Registrar / Archivist
- Manager
- Board secretary
- External users

## Guardrails
- Do not delete records casually
- Do not bypass workflows
- Do not remove roles without accountability

## Reasoning Heuristics
1. Process area
2. Objects
3. Roles
4. Constraints
5. Trade-offs
