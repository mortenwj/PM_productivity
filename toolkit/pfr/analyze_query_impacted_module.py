"""
Analyze Product First requests from an Azure DevOps query
and generate ImpactedModule assignment suggestions.

Usage:
    This script will:
    1. Execute the specified Azure DevOps query
    2. Fetch work items from the query results
    3. Analyze items missing ImpactedModule
    4. Generate high-confidence suggestions based on title/description/comments
"""

import json
from typing import List, Dict, Any
from collections import Counter

# Valid ImpactedModule dropdown values (from previous analysis)
VALID_MODULES = [
    "Plan&Build", "Document", "Board meeting", "UI Configuration", "Webparts", 
    "SIF", "Workflow", "Contact", "Teams Integration", "Personal Digital Signing", 
    "Public link", "Surveying case", "Building application case", "Mimir", 
    "Access matrix", "eArchive", "eSignature", "File center", "Fileviewer", 
    "UI-UX", "Web admin", "IFAR", "Disposal and Retention", "Custom fields", 
    "eManager", "Personal standin", "Municipal planning case", "Search", 
    "Complaint case", "Logs", "Format converter", "Integrations", "Access Group", 
    "Massupdate", "Decision tracking", "Template filters", "Classification", 
    "Dispatch", "Restricted Mode", "Notification Panel", "File validation", 
    "Phrases", "Reports", "First Agenda", "Address Case", "Supervision case", 
    "Desktops", "Outlook client sidepanel", "Map", "Case Handling Model", 
    "Progress plan", "OWA", "Detail view", "Elastic search", "Email alerts", 
    "help", "Usersync", "PDF conversion", "SAPA Export", 
    "Checklists (DiBK and customer specific)"
]

# Keywords mapping for module suggestions
MODULE_KEYWORDS = {
    "IFAR": ["ifar", "information act", "access to information", "access request", "freedom of information"],
    "Workflow": ["workflow", "process engine", "approval flow", "activity types"],
    "Document": ["document", "file", "pdf", "letter template", "dispatch", "sign off"],
    "Search": ["search", "global search", "search results", "keyword", "elastic search"],
    "Contact": ["contact", "contact person", "contactlist", "enterprise name"],
    "Plan&Build": ["casetype", "case type", "milestone", "process", "estate", "plan"],
    "UI Configuration": ["desktop tab", "list view", "column", "configure", "bookmark"],
    "UI-UX": ["button", "scroll", "visibility", "interface", "user experience"],
    "Dispatch": ["dispatch", "recipient", "send", "deliver"],
    "Access matrix": ["permission", "access group", "access code", "access control"],
    "eArchive": ["archive", "earcive", "einnsyn", "fgs-export"],
    "Public link": ["opengov", "publishing", "public link"],
    "Web admin": ["web admin", "webadmin", "administrator"],
    "Massupdate": ["mass update", "bulk update", "mass-update"],
    "Webparts": ["webpart", "web part"],
    "SIF": ["sif", "sif service", "getcases"],
    "Reports": ["report", "handläggningstider"],
    "First Agenda": ["first agenda"],
    "Board meeting": ["board meeting", "meeting", "agenda"],
    "Building application case": ["building", "dispensation", "matrikkel"],
    "Complaint case": ["complaint case"],
    "Integrations": ["integration", "freg", "matrikkel"],
    "Format converter": ["conversion", "convert", "pdf"],
    "Email alerts": ["notification", "email alert"],
    "Logs": ["log", "logbook"],
}

def analyze_work_item_for_module(item: Dict) -> Dict[str, Any]:
    """
    Analyze a single work item to suggest ImpactedModule.
    Returns dict with suggested module, confidence, and reasoning.
    """
    fields = item.get("fields", {})
    title = fields.get("System.Title", "").lower()
    description = fields.get("System.Description", "").lower()
    
    # Combine title and description for analysis
    text_to_analyze = f"{title} {description}"
    
    # Score each module based on keyword matches
    module_scores = {}
    
    for module, keywords in MODULE_KEYWORDS.items():
        score = 0
        matched_keywords = []
        
        for keyword in keywords:
            if keyword in text_to_analyze:
                score += 1
                matched_keywords.append(keyword)
        
        if score > 0:
            module_scores[module] = {
                "score": score,
                "matched_keywords": matched_keywords
            }
    
    # Find highest scoring module
    if not module_scores:
        return {
            "suggested_module": None,
            "confidence": "Low",
            "reasoning": "No clear module indicators found in title or description"
        }
    
    best_module = max(module_scores.items(), key=lambda x: x[1]["score"])
    module_name, module_data = best_module
    
    # Determine confidence level
    if module_data["score"] >= 2:
        confidence = "Very High"
    elif module_data["score"] == 1:
        confidence = "High"
    else:
        confidence = "Medium"
    
    reasoning = f"Found {module_data['score']} matching keyword(s): {', '.join(module_data['matched_keywords'])}"
    
    # Special cases for explicit mentions
    if any(kw in title for kw in ["ifar", "information act", "access to information"]):
        if module_name != "IFAR":
            module_name = "IFAR"
            confidence = "Very High"
            reasoning = "Explicitly mentions IFAR/Information Act Request in title"
    
    return {
        "suggested_module": module_name,
        "confidence": confidence,
        "reasoning": reasoning,
        "score": module_data["score"]
    }

def analyze_query_results(work_items: List[Dict]) -> Dict[str, Any]:
    """
    Analyze a list of work items and generate ImpactedModule suggestions.
    """
    items_without_module = []
    items_with_module = []
    suggestions = []
    
    for item in work_items:
        item_id = item.get("id")
        fields = item.get("fields", {})
        
        current_module = fields.get("Custom.ImpactedModule")
        title = fields.get("System.Title", "No Title")
        
        if current_module:
            items_with_module.append({
                "id": item_id,
                "title": title,
                "module": current_module
            })
        else:
            items_without_module.append({
                "id": item_id,
                "title": title,
                "description": fields.get("System.Description", ""),
                "state": fields.get("System.State", ""),
                "assigned_to": fields.get("System.AssignedTo")
            })
            
            # Generate suggestion
            suggestion = analyze_work_item_for_module(item)
            if suggestion["suggested_module"]:
                suggestions.append({
                    "id": item_id,
                    "title": title,
                    "suggested_module": suggestion["suggested_module"],
                    "confidence": suggestion["confidence"],
                    "reasoning": suggestion["reasoning"],
                    "score": suggestion.get("score", 0)
                })
    
    return {
        "total_items": len(work_items),
        "items_with_module": len(items_with_module),
        "items_without_module": len(items_without_module),
        "suggestions": suggestions,
        "module_distribution": Counter(item["module"] for item in items_with_module)
    }

if __name__ == "__main__":
    print("ImpactedModule Analysis Script")
    print("=" * 50)
    print("\nThis script is designed to work with Azure DevOps query results.")
    print("To use it:")
    print("1. Get your query ID or path")
    print("2. Execute the query via Azure DevOps API")
    print("3. Fetch work items from query results")
    print("4. Run this analysis on the work items")
    print("\nValid ImpactedModule values:", len(VALID_MODULES))











