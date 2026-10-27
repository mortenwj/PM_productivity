"""
Analyze ambiguous items for ImpactedModule suggestions.
This script analyzes items that require further analysis.
"""

from analyze_query_for_impacted_module import analyze_work_item_for_module
import json

# Sample items for analysis - will be populated with actual fetched data
def analyze_ambiguous_items(work_items):
    """Analyze ambiguous items and generate suggestions."""
    results = []
    
    for item in work_items:
        item_id = item.get("id")
        fields = item.get("fields", {})
        title = fields.get("System.Title", "")
        
        # Analyze the item
        suggestion = analyze_work_item_for_module(item)
        
        # Only include if we got a suggestion
        if suggestion.get("suggested_module"):
            results.append({
                "id": item_id,
                "title": title,
                "suggested_module": suggestion["suggested_module"],
                "confidence": suggestion["confidence"],
                "reasoning": suggestion["reasoning"],
                "score": suggestion.get("score", 0)
            })
    
    return results

if __name__ == "__main__":
    print("Analyzing ambiguous items for ImpactedModule suggestions...")
    print("Use analyze_ambiguous_items() function with work item data.")












