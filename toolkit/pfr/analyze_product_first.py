"""
Script to analyze Product First Requests from Azure DevOps.
This script will extract data from the backlog and provide insights for process optimization.
"""

import json
from datetime import datetime, timezone
from collections import Counter, defaultdict
from typing import List, Dict, Any

# Sample data structure - we'll populate this with actual API calls
# For now, this script outlines the analysis framework

def extract_work_item_ids_from_backlog(backlog_response: Dict) -> List[int]:
    """Extract work item IDs from backlog API response."""
    ids = []
    for item in backlog_response.get("workItems", []):
        if "target" in item and "id" in item["target"]:
            ids.append(item["target"]["id"])
    return ids

def calculate_age_days(created_date: str) -> int:
    """Calculate age in days from creation date."""
    if not created_date:
        return None
    try:
        created = datetime.fromisoformat(created_date.replace('Z', '+00:00'))
        now = datetime.now(timezone.utc)
        return (now - created).days
    except Exception as e:
        print(f"Error parsing date {created_date}: {e}")
        return None

def analyze_work_items(work_items: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Analyze a collection of work items and return statistics."""
    
    analysis = {
        "total_count": len(work_items),
        "by_type": Counter(),
        "by_state": Counter(),
        "by_priority": Counter(),
        "by_module": Counter(),
        "by_age_category": Counter(),
        "oldest_items": [],
        "newest_items": [],
        "without_module": 0,
        "average_age_days": 0,
        "total_age_days": 0,
        "age_distribution": {
            "0-30": 0,
            "31-90": 0,
            "91-180": 0,
            "181-365": 0,
            "365+": 0
        }
    }
    
    items_with_age = []
    
    for item in work_items:
        fields = item.get("fields", {})
        
        # Work item type
        work_type = fields.get("System.WorkItemType", "Unknown")
        analysis["by_type"][work_type] += 1
        
        # State
        state = fields.get("System.State", "Unknown")
        analysis["by_state"][state] += 1
        
        # Priority
        priority = fields.get("Microsoft.VSTS.Common.Priority", "Not Set")
        analysis["by_priority"][priority] += 1
        
        # Impacted Module
        module = fields.get("Custom.ImpactedModule", None)
        if module:
            analysis["by_module"][module] += 1
        else:
            analysis["without_module"] += 1
        
        # Age analysis
        created_date = fields.get("System.CreatedDate", None)
        age_days = calculate_age_days(created_date)
        
        if age_days is not None:
            items_with_age.append({
                "id": item.get("id"),
                "title": fields.get("System.Title", "No Title"),
                "age_days": age_days,
                "created_date": created_date,
                "state": state,
                "work_type": work_type,
                "module": module
            })
            
            analysis["total_age_days"] += age_days
            
            # Age category
            if age_days <= 30:
                analysis["age_distribution"]["0-30"] += 1
            elif age_days <= 90:
                analysis["age_distribution"]["31-90"] += 1
            elif age_days <= 180:
                analysis["age_distribution"]["91-180"] += 1
            elif age_days <= 365:
                analysis["age_distribution"]["181-365"] += 1
            else:
                analysis["age_distribution"]["365+"] += 1
    
    # Calculate average age
    if items_with_age:
        analysis["average_age_days"] = round(analysis["total_age_days"] / len(items_with_age), 1)
        
        # Sort by age
        items_with_age.sort(key=lambda x: x["age_days"], reverse=True)
        analysis["oldest_items"] = items_with_age[:10]
        analysis["newest_items"] = sorted(items_with_age, key=lambda x: x["age_days"])[:10]
    
    return analysis

def print_analysis_report(analysis: Dict[str, Any]):
    """Print a formatted analysis report."""
    
    print("=" * 80)
    print("PRODUCT FIRST REQUESTS - ANALYSIS REPORT")
    print("=" * 80)
    print(f"\nTotal Work Items: {analysis['total_count']}")
    
    print("\n" + "-" * 80)
    print("DISTRIBUTION BY TYPE:")
    print("-" * 80)
    for item_type, count in analysis["by_type"].most_common():
        percentage = (count / analysis["total_count"]) * 100
        print(f"  {item_type:20s}: {count:4d} ({percentage:5.1f}%)")
    
    print("\n" + "-" * 80)
    print("DISTRIBUTION BY STATE:")
    print("-" * 80)
    for state, count in analysis["by_state"].most_common():
        percentage = (count / analysis["total_count"]) * 100
        print(f"  {state:20s}: {count:4d} ({percentage:5.1f}%)")
    
    print("\n" + "-" * 80)
    print("DISTRIBUTION BY PRIORITY:")
    print("-" * 80)
    for priority, count in sorted(analysis["by_priority"].items()):
        percentage = (count / analysis["total_count"]) * 100
        print(f"  Priority {priority}: {count:4d} ({percentage:5.1f}%)")
    
    print("\n" + "-" * 80)
    print("DISTRIBUTION BY IMPACTED MODULE (Top 15):")
    print("-" * 80)
    for module, count in analysis["by_module"].most_common(15):
        percentage = (count / analysis["total_count"]) * 100
        print(f"  {module:30s}: {count:4d} ({percentage:5.1f}%)")
    
    print(f"\n  Items without module specified: {analysis['without_module']}")
    
    print("\n" + "-" * 80)
    print("AGE ANALYSIS:")
    print("-" * 80)
    print(f"  Average Age: {analysis['average_age_days']} days")
    print(f"\n  Age Distribution:")
    for category, count in analysis["age_distribution"].items():
        percentage = (count / analysis["total_count"]) * 100
        print(f"    {category:10s}: {count:4d} ({percentage:5.1f}%)")
    
    if analysis["oldest_items"]:
        print("\n" + "-" * 80)
        print("TOP 10 OLDEST ITEMS:")
        print("-" * 80)
        for i, item in enumerate(analysis["oldest_items"], 1):
            print(f"\n  {i}. ID: {item['id']} | Age: {item['age_days']} days | {item['work_type']}")
            print(f"     Title: {item['title'][:70]}")
            print(f"     State: {item['state']} | Module: {item['module'] or 'Not specified'}")

def save_work_items_to_file(work_items: List[Dict], filename: str = "product_first_work_items.json"):
    """Save work items to a JSON file for further analysis."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(work_items, f, indent=2, ensure_ascii=False, default=str)
    print(f"\nWork items saved to {filename}")

if __name__ == "__main__":
    print("Product First Requests Analysis Tool")
    print("=" * 80)
    print("\nThis script requires Azure DevOps API access to fetch work items.")
    print("To use this script:")
    print("1. Fetch work items using Azure DevOps MCP tools")
    print("2. Save the response to a JSON file")
    print("3. Load and analyze using the functions above")
    print("\nExample usage:")
    print("  - Use the MCP tools to get backlog work items")
    print("  - Pass the work items data to analyze_work_items()")
    print("  - Use print_analysis_report() to display results")

