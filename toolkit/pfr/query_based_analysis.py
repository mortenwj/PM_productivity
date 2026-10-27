"""
Analysis script based on query: pf dynamic query
Query ID: 72a30e06-aede-48bb-b9e8-aa35d0cce63f

Modified to find items MISSING ImpactedModule (instead of IFAR items).
"""

from analyze_query_for_impacted_module import analyze_work_items, analyze_work_item_for_module
import json

# Items from the current batch that match the criteria
current_batch_items = [
    {
        "id": 132525,
        "fields": {
            "System.Id": 132525,
            "System.State": "New",
            "System.Title": "Execute on plan for handling Phase 1 Customers",
            "Custom.ImpactedModule": None,
            "System.Description": "",
            "System.AssignedTo": None
        }
    },
    {
        "id": 132532,
        "fields": {
            "System.Id": 132532,
            "System.State": "New",
            "System.Title": "Create a Product First project success story repository",
            "Custom.ImpactedModule": None,
            "System.Description": "",
            "System.AssignedTo": None
        }
    },
    {
        "id": 132533,
        "fields": {
            "System.Id": 132533,
            "System.State": "New",
            "System.Title": "Update Product First pages on WIKI",
            "Custom.ImpactedModule": None,
            "System.Description": "",
            "System.AssignedTo": None
        }
    },
    {
        "id": 132546,
        "fields": {
            "System.Id": 132546,
            "System.State": "New",
            "System.Title": "Establish meeting forums and WoW with PF",
            "Custom.ImpactedModule": None,
            "System.Description": "",
            "System.AssignedTo": None
        }
    },
    {
        "id": 132543,
        "fields": {
            "System.Id": 132543,
            "System.State": "New",
            "System.Title": "1:1s",
            "Custom.ImpactedModule": None,
            "System.Description": "<ul><li>Kjersti G </li><li>Gunnar </li>...</ul>",
            "System.AssignedTo": "Jenny Felldin <jenny.felldin@tietoevry.com>"
        }
    }
]

if __name__ == "__main__":
    print("=" * 70)
    print("ImpactedModule Analysis - Based on Query Structure")
    print("=" * 70)
    print("\nQuery: pf dynamic query")
    print("Query ID: 72a30e06-aede-48bb-b9e8-aa35d0cce63f")
    print("\nModified Query Criteria:")
    print("- Team Project: 360")
    print("- Area Path: Under '360\\Product First Requests'")
    print("- State: New")
    print("- ImpactedModule: MISSING/Empty (modified from original)")
    print("\n" + "=" * 70)
    
    results = analyze_work_items(current_batch_items)
    
    print(f"\nAnalysis Results (Current Batch):")
    print(f"- Total items analyzed: {results['total_items_analyzed']}")
    print(f"- Items with ImpactedModule: {results['items_with_module']}")
    print(f"- Items without ImpactedModule: {results['items_without_module']}")
    print(f"- Suggestions generated: {results['total_suggestions']}")
    
    if results['suggestions']:
        print("\n" + "=" * 70)
        print("Suggestions by Module:")
        print("=" * 70)
        for module, suggestions in results['suggestions_by_module'].items():
            print(f"\n{module} ({len(suggestions)} items):")
            for s in suggestions:
                print(f"  [{s['id']}] {s['title'][:65]}")
                print(f"      Confidence: {s['confidence']} | Score: {s['score']}")
                print(f"      Reasoning: {s['reasoning']}")
    
    print("\n" + "=" * 70)
    print("Note: This is a sample batch. Full analysis requires fetching")
    print("all Product First items in 'New' state missing ImpactedModule.")
    print("=" * 70)











