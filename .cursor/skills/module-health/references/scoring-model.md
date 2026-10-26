# Scoring model reference

Normative config: `toolkit/module-health/scoring_config.json`

## Default mode: ADO only (bugs + PFRs)

Revenue and Power BI are **optional**. Default scoring uses Azure DevOps signals only.

```
health = 0.55 × bug_score + 0.45 × pfr_score
```

| Sub-score | Calculation |
|-----------|-------------|
| **bug_score** | `100 - min(100, bugs_90d × 2 + p1_bugs_90d × 10)` |
| **pfr_score** | `100 - min(100, open_pfrs × 3)` |

Higher **health_score** = fewer bugs / open PFRs (healthier module in scope).

## Bands

| Score | Band | Icon |
|-------|------|------|
| ≥ 75 | Healthy | ✅ |
| ≥ 55 | Watch | ⚠️ |
| ≥ 35 | At Risk | 🔴 |
| < 35 | Review | ⬜ |

## ADO insight rules (examples)

| Condition | Meaning |
|-----------|---------|
| bugs_90d ≥ 10 or p1 ≥ 3 | Quality hotspot |
| open_pfrs ≥ 10 and customers ≥ 3 | Strong PFR demand |
| bugs ≥ 5 and open_pfrs ≥ 10 | Combined pressure |
| p1_bugs_90d ≥ 2 | P1 attention |

## Full mode (when revenue returns)

Enable with `--with-revenue` and a revenue Excel path:

```
health = 35% revenue rank + 15% growth + 25% bug + 25% PFR
```

See `weights` and `insights` in scoring config.

## Tuning

Edit `weights_ado_only` or penalties in `scoring_config.json`. Re-run scorecard after changes.
