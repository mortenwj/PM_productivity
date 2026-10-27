"""
Script to analyze ImpactedModule field in Product First Requests.
Counts how many items have vs. don't have the ImpactedModule tag.
"""

import json
from collections import Counter

def analyze_impacted_module(work_items):
    """Analyze ImpactedModule field across work items."""
    
    total_count = len(work_items)
    with_module = 0
    without_module = 0
    modules_counter = Counter()
    
    items_without_module = []
    items_with_module = []
    
    for item in work_items:
        fields = item.get("fields", {})
        module = fields.get("Custom.ImpactedModule", None)
        
        if module:
            with_module += 1
            modules_counter[module] += 1
            items_with_module.append({
                "id": item.get("id"),
                "title": fields.get("System.Title", "No Title"),
                "module": module,
                "created": fields.get("System.CreatedDate", ""),
                "state": fields.get("System.State", "")
            })
        else:
            without_module += 1
            items_without_module.append({
                "id": item.get("id"),
                "title": fields.get("System.Title", "No Title"),
                "created": fields.get("System.CreatedDate", ""),
                "state": fields.get("System.State", "")
            })
    
    percentage_with = (with_module / total_count * 100) if total_count > 0 else 0
    percentage_without = (without_module / total_count * 100) if total_count > 0 else 0
    
    return {
        "total_count": total_count,
        "with_module": with_module,
        "without_module": without_module,
        "percentage_with": round(percentage_with, 1),
        "percentage_without": round(percentage_without, 1),
        "modules_counter": modules_counter,
        "items_without_module": items_without_module,
        "items_with_module": items_with_module
    }

def print_report(analysis):
    """Print formatted analysis report."""
    
    print("=" * 80)
    print("IMPACTED MODULE ANALYSIS - Product First Requests")
    print("=" * 80)
    print(f"\nTotal Work Items Analyzed: {analysis['total_count']}")
    print(f"\nItems WITH ImpactedModule: {analysis['with_module']} ({analysis['percentage_with']}%)")
    print(f"Items WITHOUT ImpactedModule: {analysis['without_module']} ({analysis['percentage_without']}%)")
    
    print("\n" + "-" * 80)
    print("MODULE DISTRIBUTION (Items with module specified):")
    print("-" * 80)
    for module, count in analysis['modules_counter'].most_common():
        percentage = (count / analysis['with_module'] * 100) if analysis['with_module'] > 0 else 0
        print(f"  {module:40s}: {count:3d} ({percentage:5.1f}%)")
    
    if analysis['items_without_module']:
        print("\n" + "-" * 80)
        print("SAMPLE ITEMS WITHOUT ImpactedModule (first 20):")
        print("-" * 80)
        for i, item in enumerate(analysis['items_without_module'][:20], 1):
            print(f"\n  {i}. ID: {item['id']} | {item['state']}")
            print(f"     {item['title'][:70]}")
            if len(item['title']) > 70:
                print(f"     {item['title'][70:140]}")

# Sample data from API calls - this would normally come from saved JSON
sample_work_items = []

if __name__ == "__main__":
    print("ImpactedModule Analysis Tool")
    print("=" * 80)
    print("\nTo use this script:")
    print("1. Load work items data (JSON format)")
    print("2. Pass to analyze_impacted_module() function")
    print("3. Use print_report() to display results")
    print("\nOr run with data inline in the script.")

