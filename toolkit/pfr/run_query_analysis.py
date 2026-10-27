"""
Run ImpactedModule analysis based on Product First query structure.
This script fetches work items and generates suggestions.
"""

import json
from analyze_query_for_impacted_module import analyze_work_items, analyze_work_item_for_module

# Sample work items from the batch we fetched
work_items = [
    {
        "id": 114859,
        "fields": {
            "System.Id": 114859,
            "System.State": "New",
            "System.AssignedTo": "Mikko Koponen <mikko.koponen@tietoevry.com>",
            "System.Title": "Findwise search module",
            "Custom.ImpactedModule": "Search",
            "System.Description": "<div>Currently Public360 searches...</div>"
        }
    },
    {
        "id": 132525,
        "fields": {
            "System.Id": 132525,
            "System.State": "New",
            "System.Title": "Execute on plan for handling Phase 1 Customers",
            "Custom.ImpactedModule": None,
            "System.Description": ""
        }
    },
    {
        "id": 132532,
        "fields": {
            "System.Id": 132532,
            "System.State": "New",
            "System.Title": "Create a Product First project success story repository",
            "Custom.ImpactedModule": None,
            "System.Description": ""
        }
    },
    {
        "id": 132533,
        "fields": {
            "System.Id": 132533,
            "System.State": "New",
            "System.Title": "Update Product First pages on WIKI",
            "Custom.ImpactedModule": None,
            "System.Description": ""
        }
    },
    {
        "id": 132546,
        "fields": {
            "System.Id": 132546,
            "System.State": "New",
            "System.Title": "Establish meeting forums and WoW with PF",
            "Custom.ImpactedModule": None,
            "System.Description": ""
        }
    },
    {
        "id": 132543,
        "fields": {
            "System.Id": 132543,
            "System.State": "New",
            "System.AssignedTo": "Jenny Felldin <jenny.felldin@tietoevry.com>",
            "System.Title": "1:1s",
            "Custom.ImpactedModule": None,
            "System.Description": "<ul><li>Kjersti G </li><li>Gunnar </li>...</ul>"
        }
    }
]

if __name__ == "__main__":
    print("Analyzing work items...")
    results = analyze_work_items(work_items)
    
    print(f"\nAnalysis Results:")
    print(f"Total items analyzed: {results['total_items_analyzed']}")
    print(f"Items with ImpactedModule: {results['items_with_module']}")
    print(f"Items without ImpactedModule: {results['items_without_module']}")
    print(f"Suggestions generated: {results['total_suggestions']}")
    
    print("\nSuggestions by Module:")
    for module, suggestions in results['suggestions_by_module'].items():
        print(f"\n{module} ({len(suggestions)} items):")
        for s in suggestions:
            print(f"  - [{s['id']}] {s['title'][:60]}...")
            print(f"    Confidence: {s['confidence']}, Score: {s['score']}")











