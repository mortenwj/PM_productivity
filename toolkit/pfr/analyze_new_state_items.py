"""
Script to analyze Product First Requests in 'New' state and identify missing ImpactedModule tags.
This will process the work items fetched from Azure DevOps.
"""

import json
from collections import Counter, defaultdict
from datetime import datetime

# This script will be used to process the fetched work items
# We'll fetch work items using MCP tools and then analyze them here

def analyze_new_state_items(work_items):
    """Analyze work items in New state to find missing ImpactedModule."""
    
    new_state_items = []
    new_with_module = []
    new_without_module = []
    
    for item in work_items:
        fields = item.get("fields", {})
        state = fields.get("System.State", "")
        
        if state == "New":
            module = fields.get("Custom.ImpactedModule", None)
            work_item = {
                "id": item.get("id"),
                "title": fields.get("System.Title", "No Title"),
                "state": state,
                "module": module,
                "work_item_type": fields.get("System.WorkItemType", ""),
                "created_date": fields.get("System.CreatedDate", ""),
                "description": fields.get("System.Description", "")
            }
            
            new_state_items.append(work_item)
            
            if module:
                new_with_module.append(work_item)
            else:
                new_without_module.append(work_item)
    
    return {
        "total_new": len(new_state_items),
        "new_with_module": len(new_with_module),
        "new_without_module": len(new_without_module),
        "items_without_module": new_without_module,
        "items_with_module": new_with_module
    }

if __name__ == "__main__":
    print("This script processes work items fetched from Azure DevOps.")
    print("Run the MCP tools to fetch work items first.")

