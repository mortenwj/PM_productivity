"""
Analyze batches of work items to extract New state items missing ImpactedModule.
"""

def analyze_batch(work_items):
    """Analyze a batch of work items."""
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
                "module": module
            }
            
            new_state.append(work_item_data)
            
            if module:
                new_with_module.append(work_item_data)
            else:
                new_without_module.append(work_item_data)
    
    return {
        "total_processed": len(work_items),
        "new_state_count": len(new_state),
        "with_module": len(new_with_module),
        "without_module": len(new_without_module),
        "items_without_module": new_without_module
    }

if __name__ == "__main__":
    print("Batch analyzer ready")












