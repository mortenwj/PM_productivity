"""
Fetch all Product First Requests related to Svenska kyrkan.

ROOT CAUSE of missed PFRs: Customer name is stored in Custom.Customername field,
NOT in Tags or Description. The CSV export and Tags/Description search miss items
where Svenska kyrkan is only in the Customer name field (e.g. PFR 219865).

QUERY APPROACH:
1. Get all open PFR IDs: wit_get_query_results_by_id (id=bb65b39e-f496-4577-85d2-6211ec66c218, responseType=ids)
2. Batch fetch with Custom.Customername: wit_get_work_items_batch_by_ids with fields including Custom.Customername
   - Azure DevOps limit: max 200 IDs per batch
3. Filter results where Custom.Customername contains "svenska kyrkan" (case insensitive)

WIQL for saved query or REST API (recommended - filters server-side):
  SELECT [System.Id], [System.Title], [System.State], [System.AssignedTo], [System.Tags], [Custom.Customername]
  FROM WorkItems
  WHERE [System.TeamProject] = '360'
    AND [System.IterationPath] UNDER '360\\Product First Requests'
    AND [System.WorkItemType] = 'Feature'
    AND NOT [System.State] IN ('Rejected', 'Closed')
    AND [Custom.Customername] CONTAINS 'Svenska kyrkan'
"""

import json
import re
from pathlib import Path

FIELDS_TO_FETCH = [
    "System.Id",
    "System.Title",
    "System.State",
    "System.AssignedTo",
    "System.Tags",
    "Custom.Customername",
]
BATCH_SIZE = 200  # Azure DevOps limit


def matches_svenska_kyrkan(customername: str) -> bool:
    """Check if Customername field contains Svenska kyrkan (any casing)."""
    if not customername or not isinstance(customername, str):
        return False
    return bool(re.search(r"svenska\s*kyrkan", customername, re.IGNORECASE))


def filter_svenska_kyrkan_from_batch(batch: list) -> list:
    """Filter work items where Custom.Customername contains Svenska kyrkan."""
    result = []
    for wi in batch:
        fields = wi.get("fields", {})
        customername = fields.get("Custom.Customername") or fields.get("Custom.CustomerName")
        if matches_svenska_kyrkan(str(customername or "")):
            result.append(wi)
    return result


if __name__ == "__main__":
    print("Svenska kyrkan PFR fetch - Query approach")
    print("=" * 50)
    print()
    print("ROOT CAUSE: Customer name is in Custom.Customername, NOT Tags/Description.")
    print()
    print("RECOMMENDED: Create saved query in Azure DevOps with WIQL:")
    print("""
SELECT [System.Id], [System.Title], [System.State], [System.AssignedTo], [System.Tags], [Custom.Customername]
FROM WorkItems
WHERE [System.TeamProject] = '360'
  AND [System.IterationPath] UNDER '360\\Product First Requests'
  AND [System.WorkItemType] = 'Feature'
  AND NOT [System.State] IN ('Rejected', 'Closed')
  AND [Custom.Customername] CONTAINS 'Svenska kyrkan'
""")
    print()
    print("ALTERNATIVE: Use MCP wit_get_query_results_by_id (responseType=ids),")
    print("then wit_get_work_items_batch_by_ids in batches of 200 with fields:")
    print("  ", FIELDS_TO_FETCH)
