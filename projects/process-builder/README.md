# Process Builder — product discovery

Greenfield product exploration for **Process Builder** within the 360° Process Platform story.

**Owner:** Morten Jensen  
**Started:** 2026-09-08  
**BMAD phase:** 2-spec (SPEC kernel complete) + v1 POC with generator  
**Status:** Web POC on `feature/process-builder-poc`; dogfood S1–S3 per SPEC

---

## Decision to reach

Brief and SPEC lock v1 scope. Next: **`bmad-create-architecture`** or **`bmad-prd`** slice, then dogfood scenarios S1–S3.

---

## Folder map

| Path | Purpose |
|------|---------|
| [information-package/](./information-package/) | Evidence bundle for BMAD skills |
| [brand-kit/](./brand-kit/) | Tietoevry brand assets + tokens for UI |
| [web/](./web/) | React POC (Vite) — run `npm run dev` |
| `_bmad-output/planning-artifacts/briefs/brief-process-builder-2026-09-08/` | Product brief |
| `_bmad-output/specs/spec-process-builder/` | **SPEC kernel** + scenarios, evaluation, generator contract |

---

## Recommended BMAD sequence

1. ~~**`bmad-product-brief`**~~ — done (refresh recommended against SPEC)
2. ~~**`bmad-spec`**~~ — **`spec-process-builder`** created 2026-09-08
3. **`bmad-create-architecture`** — output folder, tests, deploy script
4. **`bmad-prd`** → **`bmad-ux`** (formalize canvas flows if needed)
5. **`bmad-dev-story`** — dogfood blockers (localization, golden files)

Related context: [`projects/process-platform/`](../process-platform/README.md), AI model creator spike, Flow process-builder role in training manuscripts.
