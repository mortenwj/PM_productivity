# Open questions — Process Builder

Captured during BMAD discovery. Resolve before locking brief scope.

| # | Question | Status |
|---|----------|--------|
| 1 | Is Process Builder a new product surface, an evolution of PMC/Plan & Build, or an AI-assisted authoring layer? | **Resolved:** Web app productizing the Cursor skill; long-term full modeling; v1 = WU/XAML gen + deploy |
| 2 | Primary user: implementation consultant, tenant process builder, or both? | **Resolved:** Customer process builders (primary) |
| 3 | v1 form factor: web app, in-product extension, CLI/spike tooling, or hybrid? | **Resolved:** Web application |
| 4 | Relationship to existing `ai-model-creator-spike` — absorb, replace, or parallel track? | Open — likely parallel (JSON model vs WU/XAML layer) |
| 5 | What is explicitly out of scope for v1? | **Resolved** — see brief Scope section |
| 6 | Process Builder = ADO #400794? | **Resolved:** Yes |
| 7 | Deploy path: filesystem vs WorkUnitRegistry? | **Resolved:** v1 = local repo output + manual copy; auto-deploy later |
| 8 | PMC/stage wiring in v1? | **Resolved:** Out of v1 — Administrator only |
