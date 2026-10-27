# BRE — Code risk assessment

**Basis:** Source scan 2026-06-08 · Complements OneDrive risk register (commercial/organizational)  
**Focus:** Technical risks that affect pilot delivery and production safety

---

## Risk summary

| Severity | Count | Theme |
|----------|-------|-------|
| **Critical** | 3 | Wrong rules execute; core actions missing |
| **High** | 4 | No e2e proof; feature off; incomplete triggers |
| **Medium** | 5 | Scalability, extensibility, operability |
| **Low** | 3 | Code quality, minor API gaps |

---

## Critical risks

### R-C1 — ContextEntity not enforced at runtime

**Evidence:** `RuleSetInspector.GetExecutableRuleSets` filters only `TriggerType` and `TriggerSubType`. `ContextEntity` is loaded into `ExecutableRuleSet` but never used in matching. `RuleSetEventHandler` computes `contextEntity` but does not pass it to executer.

**Impact:** A Case update could execute Document-targeted rules (and vice versa). Unpredictable validation errors or silent wrong behavior.

**Mitigation:** Add ContextEntity filter before pilot. One-line predicate in `GetExecutableRuleSets`.

**Pilot blocker:** Yes

---

### R-C2 — IsEnabled not enforced at runtime

**Evidence:** Cache loads all Published rule sets. No check for `IsEnabled` in inspector or executer.

**Impact:** Operators cannot disable a bad rule without unpublishing/archiving. Incident response impaired.

**Mitigation:** Filter `IsEnabled == true` in cache load or matching.

**Pilot blocker:** Yes

---

### R-C3 — RunProcess action is a no-op

**Evidence:** `RuleSetExecuter.HandleResult` — RunProcess branch is empty comment.

**Impact:** Any rule modeled with RunProcess silently succeeds without action. Auto-close, data sync, and process automation scenarios fail without error.

**Mitigation:** Do not document RunProcess as available; implement or reject at meta validation for pilot.

**Pilot blocker:** Yes for automation scenarios; No for validation-only pilot

---

## High risks

### R-H1 — No end-to-end runtime test

**Evidence:** `RuntimeTests.RunCaseUpdateRules` loads cache and updates case to "HolyBanana" but does **not assert** rule fired. Comment: "TO BE EXTENDED".

**Impact:** Regression risk; unknown if ValidationMessage path works in production meta pipeline.

**Mitigation:** Extend test with ValidationMessage rule set; assert BizInfoException.

---

### R-H2 — StartingPoint ignored

**Evidence:** `RuleSetExecuter` uses `dmnContext.Decisions.LastOrDefault()` instead of `ruleSet.StartingPoint`.

**Impact:** Multi-decision models execute wrong decision; unpredictable outcomes.

**Mitigation:** Pilot constraint: single-decision rule sets only. Fix executer for GA.

---

### R-H3 — Before/On/After events collapsed

**Evidence:** BeforeInsert, OnInsert, AfterInsert all map to `OnInsert` subtype.

**Impact:** Cannot implement "validate before save" vs "act after save" — important for close-case validation timing.

**Mitigation:** Product decision on which event hook close validation needs; may require enum extension.

---

### R-H4 — Feature flag off by default

**Evidence:** `FeatureFlags.json` — `IsOnByDefault: false`, ToggleType Development.

**Impact:** Pilot tenants forget to enable → "BRE doesn't work" support incidents.

**Mitigation:** Pilot checklist; consider pilot-specific enablement automation.

---

## Medium risks

### R-M1 — Job/Manual triggers validated but not executed

**Impact:** Customers or consultants configure scheduled rules that never run.

**Mitigation:** Meta validation should reject Job/Manual until runtime exists, or admin UI must hide them.

---

### R-M2 — Full cache refresh on every meta change

**Evidence:** RuleSetMetaInsert/Update — "Temp approach" full Refresh().

**Impact:** Performance degradation with many rule sets; publish latency.

**Mitigation:** Accept for pilot scale; incremental cache update for GA.

---

### R-M3 — Plugin catalog without execution

**Impact:** Designer shows plugin actions that cannot run — false capability impression.

**Mitigation:** Hide plugin actions in pilot UI; document as future.

---

### R-M4 — SystemFunction / CustomFunction inputs undefined

**Impact:** Rule sets referencing these value sources fail at input resolution.

**Mitigation:** Validator rejects unsupported value sources at publish time.

---

### R-M5 — RuntimeState / LastLoadErrors never updated

**Impact:** No admin visibility into load failures except logs.

**Mitigation:** Populate on inspector load failure; surface in admin list API.

---

## Low risks

### R-L1 — Duplicate output entry loop in DmnModelBuilder

**Evidence:** Subagent noted duplicate loop in `CreateDecisionTableRulesFromMeta`.

**Impact:** Possible duplicate DMN output entries in edge cases.

**Mitigation:** Code review fix.

---

### R-L2 — RuleSetMetaDelete empty

**Impact:** Orphan meta; cache not invalidated on delete attempt.

**Mitigation:** Implement delete or block delete in admin.

---

### R-L3 — SaveRuleSetProps.IsEnabled not wired

**Impact:** Save draft cannot set enabled flag; must use Publish API.

**Mitigation:** Document workflow; fix if confusing in UI.

---

## Risk vs OneDrive register (crosswalk)

| OneDrive risk | Code assessment |
|---------------|-----------------|
| Privileged access to rules calling BL/data | RunProcess stub limits blast radius today; ValidationMessage throws are safer |
| Event system not designed for ad hoc runtime | Confirmed — 9 event hooks, no async, synchronous throw |
| Long-running rules → bad UX | Low risk now — DMN eval is sync on CRUD path |
| No price strategy | Unchanged — product/commercial |
| Camunda license | N/A — internal DMN engine used |

---

## Pilot go/no-go criteria

**Go** (validation-only pilot) when:

- [ ] R-C1 fixed (ContextEntity filter)
- [ ] R-C2 fixed (IsEnabled filter)
- [ ] R-H1 fixed (e2e test green)
- [ ] Pilot scope doc signed (no RunProcess, no Job)
- [ ] Feature flag enablement runbook

**No-go** if:

- Customer expects auto-close, data updates, or scheduled rules
- Multi-decision DMN models required without StartingPoint fix
- Production rollout without Before/On/After semantics decision
