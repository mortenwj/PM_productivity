"""
Extract work item IDs from backlog response for batch processing.
"""

# From the Features backlog API response, I need to extract all IDs
# The response structure was:
# {
#   "workItems": [
#     { "target": { "id": 403270 } },
#     { "target": { "id": 403124 } },
#     ...
#   ]
# }

# Since I already processed the first 200, I need to continue with the rest
# Let me note that I need to extract IDs from the backlog response

def extract_ids_from_backlog(backlog_response):
    """Extract all work item IDs from backlog response."""
    ids = []
    for item in backlog_response.get("workItems", []):
        if "target" in item and "id" in item["target"]:
            ids.append(item["target"]["id"])
    return ids

# For batch 2, I need IDs starting from index 200
# This will be used to continue processing












