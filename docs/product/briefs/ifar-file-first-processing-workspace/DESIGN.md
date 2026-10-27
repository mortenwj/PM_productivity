---
name: IFAR file-first processing workspace
status: draft
updated: 2026-09-29
# Visual tokens to be filled when aligned with Public 360° Online / Tieto design system.
# EXPERIENCE.md references tokens as {colors.primary} etc. once defined.
colors: {}
typography: {}
rounded: {}
spacing: {}
components: {}
---

# IFAR file-first processing workspace — Design spine (placeholder)

Visual identity for this initiative is **not specified in v1 UX draft**. Implementation should **inherit Public 360° Online** (and org design system) components, density, and accessibility tokens rather than inventing a separate aesthetic.

## Brand and Style

- **Product context:** Enterprise case management (Public 360°), Norwegian public-sector users.
- **Posture:** Utilitarian, high information density, calm status signaling — consistent with existing 360° case views.
- **Pairing:** See `EXPERIENCE.md` for layout and behavior; this file will own colors, typography, and component chrome when a design pass runs (e.g. Stitch, Figma, or internal design system audit).

## Do's and Don'ts (early)

| Do | Don't |
|----|--------|
| Reuse existing 360° buttons, tables, chips, alerts | Introduce a new color language only for IFAR |
| Keep decision/suggestion panel visually distinct but not louder than case header | Use red/green alone for grant/deny |
| Reuse FIB `FileViewer` chrome (Accusoft iframe) | Custom viewer skin — embed already in product |

## Sections to complete in design pass

- Colors (status: undecided, granted, denied, partial, blocked, suggestion)
- Typography (queue density vs. decision panel)
- Layout breakpoints (queue / preview split)
- Components (document group header, suggestion card, exception banner)
