"""
Systematic batch processor for analyzing New state items.
Processes work items in batches and aggregates results.
"""

import json
from collections import defaultdict

class BatchProcessor:
    def __init__(self):
        self.total_processed = 0
        self.new_state_items = []
        self.new_with_module = []
        self.new_without_module = []
        
    def process_batch(self, work_items):
        """Process a batch of work items."""
        batch_new_state = []
        batch_with_module = []
        batch_without_module = []
        
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
                
                batch_new_state.append(work_item_data)
                self.new_state_items.append(work_item_data)
                
                if module:
                    batch_with_module.append(work_item_data)
                    self.new_with_module.append(work_item_data)
                else:
                    batch_without_module.append(work_item_data)
                    self.new_without_module.append(work_item_data)
        
        self.total_processed += len(work_items)
        
        return {
            "batch_size": len(work_items),
            "new_state_count": len(batch_new_state),
            "with_module": len(batch_with_module),
            "without_module": len(batch_without_module)
        }
    
    def get_summary(self):
        """Get aggregated summary statistics."""
        return {
            "total_processed": self.total_processed,
            "total_new_state": len(self.new_state_items),
            "new_with_module": len(self.new_with_module),
            "new_without_module": len(self.new_without_module),
            "percentage_without_module": round(
                len(self.new_without_module) / len(self.new_state_items) * 100, 1
            ) if self.new_state_items else 0
        }

# This will be used to process all batches systematically

