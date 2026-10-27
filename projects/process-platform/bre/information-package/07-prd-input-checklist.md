# BRE PRD — input checklist

Use with BMad `bmad-prd` Discovery. Information package assembled; **PRD not started**.

---

## Already evidenced

- [x] Product purpose and platform positioning
- [x] Customer scenario register (18 scoped + first-wave themes)
- [x] DevOps epic and feature tree (partial live refresh)
- [x] Wiki product intent (cached; live refresh pending)
- [x] Codebase reverse-engineered capabilities and gaps
- [x] Pilot readiness verdict and blockers

---

## Needs your decision (PRD scope)

1. **Stakes:** hobby / **internal pilot** / **customer-facing launch**?
2. **PRD audience:** engineering only, or sales/consulting/customers too?
3. **Time horizon:** align to epic 2026-12-30, validation pilot 2026, or commitment H2 2027?
4. **MVP cut:** validation-only pilot vs include first automation (RunProcess)?
5. **Form factor:** admin UI + runtime only, or API-first for integrations?
6. **Success metrics:** what proves pilot success? (e.g. #219865 demonstrable on tenant X)

---

## Working mode (pick one)

- **Fast path** — draft PRD from this package + `[ASSUMPTION]` tags for gaps
- **Coaching path** — Vision + Features or Journey-led section by section

---

## Suggested PRD relationship to existing docs

| Doc | PRD role |
|-----|----------|
| `BRE_Reverse_Engineered_PRD.md` | **As-built baseline** — merge vs supersede? |
| `information-package/` | **Evidence bundle** for decisions |
| `_bmad-output/.../prd.md` | **Target PRD** (normative forward-looking) |

---

## Gaps to close before finalize

- [ ] Live wiki refresh (MCP 403)
- [ ] Full ADO tree refresh (all epic children + commitment tags)
- [ ] Admin UI status in webadmin/BIF repos
- [ ] Sign-off on pilot tenant and customer (Tullverket? Aurskog-Høland?)
