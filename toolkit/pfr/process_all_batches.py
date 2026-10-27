"""
Script to process all batches of work items and analyze New state items missing ImpactedModule.
This will be used to systematically process all work items from the backlog.
"""

# Batch processing strategy:
# 1. Extract all work item IDs from backlog responses
# 2. Process in batches of 200
# 3. Filter for New state
# 4. Identify missing ImpactedModule
# 5. Aggregate results

def process_batch(work_items):
    """Process a batch of work items and return statistics."""
    new_state = []
    new_with_module = []
    new_without_module = []
    
    for item in work_items:
        fields = item.get("fields", {})
        state = fields.get("System.State", "")
        
        if state == "New":
            module = fields.get("Custom.ImpactedModule", None)
            work_item_data = {
                "id": item.get("id"),
                "title": fields.get("System.Title", "No Title"),
                "module": module,
                "work_item_type": fields.get("System.WorkItemType", ""),
            }
            
            new_state.append(work_item_data)
            
            if module:
                new_with_module.append(work_item_data)
            else:
                new_without_module.append(work_item_data)
    
    return {
        "total_new": len(new_state),
        "with_module": len(new_with_module),
        "without_module": len(new_without_module),
        "items_without_module": new_without_module
    }

if __name__ == "__main__":
    print("Ready to process batches")

