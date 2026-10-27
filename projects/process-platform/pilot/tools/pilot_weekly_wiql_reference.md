# Pilot weekly report — WIQL reference (time window)

Use with MCP `wit_query_by_wiql` (project **360**). Replace area / type filters with your real WIQL from the pilot run.

`@Today` is evaluated in the **organization / project query timezone** (see spec for Oslo parity).

## Problem being solved

Avoid selecting work items whose only recent change was **stack rank** (or similar): use **`Microsoft.VSTS.Common.StateChangeDate`** for **`[System.State] = 'New'`** instead of **`System.ChangedDate`** for that branch.

## Sketch (non-Bug slice — illustration only)

Combine with your real `Area Path`, `WorkItemType`, and `AND`/`OR` groupings. Adjust state names to match your process (e.g. `Resolved` vs `Removed`).

```sql
SELECT [System.Id]
FROM WorkItems
WHERE [System.TeamProject] = @project
  AND [System.AreaPath] UNDER '360\Core-Process-platform'
  AND [System.WorkItemType] <> 'Bug'
  AND (
        ( [System.State] = 'New'
          AND [Microsoft.VSTS.Common.StateChangeDate] >= @Today - 14
        )
     OR ( [System.State] <> 'New'
          AND [System.State] <> 'Closed'
          AND [System.State] <> 'Resolved'
          AND [System.ChangedDate] >= @Today - 14
        )
     OR ( [Microsoft.VSTS.Common.ResolvedDate] >= @Today - 14 )
     OR ( [Microsoft.VSTS.Common.ClosedDate] >= @Today - 14 )
      )
ORDER BY [System.ChangedDate] DESC
```

**Bugs:** mirror the same **New** vs **ChangedDate** split in a separate Bug WIQL, or duplicate the `OR` block with `WorkItemType = 'Bug'`.

## After the query

1. Batch-get details with `wit_get_work_items_batch_by_ids` (≤200 IDs per call), including any fields you need for overlays (`System.Description`, acceptance criteria, `Microsoft.VSTS.Common.StateChangeDate` if you show it in Markdown).

2. Save JSON under `projects/process-platform/pilot/tools/` and run `py -3 projects/process-platform/pilot/tools/generate_pilot_weekly_report.py`.
