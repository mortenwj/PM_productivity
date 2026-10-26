# WIQL templates (Module Health)

Project: **360**. Execute via Azure DevOps MCP `wit_query` with `action: "wiql"`.

## Bugs — created in last 90 days

```sql
SELECT [System.Id], [System.Title], [System.State],
       [Custom.ImpactedModule], [Microsoft.VSTS.Common.Priority],
       [System.CreatedDate]
FROM WorkItems
WHERE [System.TeamProject] = '360'
  AND [System.WorkItemType] = 'Bug'
  AND [System.CreatedDate] >= @Today - 90
  AND [Custom.ImpactedModule] <> ''
  AND [Custom.ImpactedModule] <> '0 - Not applicable'
ORDER BY [System.CreatedDate] DESC
```

## Open Product First Requests

```sql
SELECT [System.Id], [System.Title], [System.State],
       [Custom.ImpactedModule], [Custom.Customername],
       [System.CreatedDate]
FROM WorkItems
WHERE [System.TeamProject] = '360'
  AND [System.AreaPath] UNDER '360\Product First Requests'
  AND [System.State] IN ('New', 'Active', 'Pending')
  AND [Custom.ImpactedModule] <> ''
  AND [Custom.ImpactedModule] <> '0 - Not applicable'
ORDER BY [System.CreatedDate] DESC
```

## Batch fields

After WIQL, if only IDs return:

`System.Id`, `System.Title`, `System.State`, `Custom.ImpactedModule`, `Microsoft.VSTS.Common.Priority`, `Custom.Customername`

Chunk size: **200** IDs per `wit_get_work_items_batch_by_ids` call.

## Optional — single module filter

Add to `WHERE`:

```sql
AND [Custom.ImpactedModule] = 'Dispatch'
```

## Optional — team scoping

There is no ADO field for product team. Filter **after merge** using `module_taxonomy.json` → `module_to_team`, or pass `--team` to `build_scorecard.py`.
