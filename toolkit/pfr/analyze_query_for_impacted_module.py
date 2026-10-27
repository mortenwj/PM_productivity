"""
Analyze Product First requests based on query structure
and generate ImpactedModule assignment suggestions.

Based on query: https://dev.azure.com/tieto-si/360/_queries/query-edit/72a30e06-aede-48bb-b9e8-aa35d0cce63f/
"""

import json
from typing import List, Dict, Any
from collections import Counter, defaultdict

# The base WIQL from your query - modified to find items MISSING ImpactedModule
BASE_WIQL = """
select [System.Id], [System.WorkItemType], [System.Title], [System.AssignedTo], 
       [System.State], [System.Tags], [Custom.ImpactedModule], [System.Description]
from WorkItems 
where [System.TeamProject] = '360' 
  and [System.AreaPath] under '360\\Product First Requests' 
  and [System.WorkItemType] <> '' 
  and [System.State] = 'New'
"""

# Valid ImpactedModule dropdown values
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

# Enhanced keywords mapping for module suggestions
MODULE_KEYWORDS = {
    "IFAR": ["ifar", "information act", "access to information", "access request", 
             "freedom of information", "offentlighetsloven"],
    "Workflow": ["workflow", "process engine", "approval flow", "activity types", 
                 "workflow recipients", "submitting to workflow"],
    "Document": ["document", "file", "pdf", "letter template", "dispatch", 
                 "sign off", "document overview", "case documents", "transfer of document"],
    "Search": ["search", "global search", "search results", "keyword", 
               "elastic search", "search filters", "search parameter"],
    "Contact": ["contact", "contact person", "contactlist", "enterprise name", 
                "private person", "duplicate national id"],
    "Plan&Build": ["casetype", "case type", "milestone", "process", "estate", 
                   "plan", "title mask", "access code", "complaint case"],
    "UI Configuration": ["desktop tab", "list view", "column", "configure", 
                        "bookmark", "ui configuration", "code table"],
    "UI-UX": ["button", "scroll", "visibility", "interface", "user experience", 
              "spacing", "alignment", "role in ui"],
    "Dispatch": ["dispatch", "recipient", "send", "deliver", "dispatch window", 
                 "dispatch dialog", "distribution"],
    "Access matrix": ["permission", "access group", "access code", "access control", 
                     "delete permission", "accessgroup reports"],
    "eArchive": ["archive", "earcive", "einnsyn", "fgs-export", "archive code", 
                 "archive documents", "360 archive"],
    "Public link": ["opengov", "publishing", "public link", "publishing duration"],
    "Web admin": ["web admin", "webadmin", "administrator", "web admin configuration"],
    "Massupdate": ["mass update", "bulk update", "mass-update", "mass update function"],
    "Webparts": ["webpart", "web part", "all stages", "ongoing events"],
    "SIF": ["sif", "sif service", "getcases", "activityservice"],
    "Reports": ["report", "handläggningstider", "accessgroup reports"],
    "First Agenda": ["first agenda", "deactivation of users"],
    "Board meeting": ["board meeting", "meeting", "agenda", "digital dashboard"],
    "Building application case": ["building", "dispensation", "matrikkel", "matrikkelintegrasjon"],
    "Complaint case": ["complaint case", "complaint cases"],
    "Integrations": ["integration", "freg", "matrikkel", "teams integration"],
    "Format converter": ["conversion", "convert", "pdf conversion"],
    "Email alerts": ["notification", "email alert", "promptly notified"],
    "Logs": ["log", "logbook", "unregistered documents"],
}

def analyze_work_item_for_module(item: Dict) -> Dict[str, Any]:
    """
    Analyze a single work item to suggest ImpactedModule.
    Returns dict with suggested module, confidence, and reasoning.
    """
    fields = item.get("fields", {})
    title = fields.get("System.Title", "").lower()
    description = fields.get("System.Description", "").lower() if fields.get("System.Description") else ""
    
    # Combine title and description for analysis
    text_to_analyze = f"{title} {description}"
    
    # Score each module based on keyword matches
    module_scores = {}
    
    for module, keywords in MODULE_KEYWORDS.items():
        score = 0
        matched_keywords = []
        
        for keyword in keywords:
            if keyword.lower() in text_to_analyze:
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
            "reasoning": "No clear module indicators found in title or description",
            "score": 0
        }
    
    best_module = max(module_scores.items(), key=lambda x: x[1]["score"])
    module_name, module_data = best_module
    
    # Determine confidence level based on score and explicit mentions
    if module_data["score"] >= 3:
        confidence = "Very High"
    elif module_data["score"] == 2:
        confidence = "High"
    elif module_data["score"] == 1:
        confidence = "Medium-High"
    else:
        confidence = "Medium"
    
    # Boost confidence for explicit module mentions
    explicit_mentions = [
        ("ifar", "IFAR"),
        ("workflow", "Workflow"),
        ("document", "Document"),
        ("search", "Search"),
        ("contact", "Contact"),
        ("dispatch", "Dispatch"),
        ("sif", "SIF"),
        ("web admin", "Web admin"),
        ("mass update", "Massupdate"),
    ]
    
    for keyword, module in explicit_mentions:
        if keyword in title and module_name.lower() == module.lower():
            confidence = "Very High"
            break
    
    reasoning = f"Found {module_data['score']} matching keyword(s): {', '.join(module_data['matched_keywords'][:3])}"
    if len(module_data['matched_keywords']) > 3:
        reasoning += f" (and {len(module_data['matched_keywords']) - 3} more)"
    
    return {
        "suggested_module": module_name,
        "confidence": confidence,
        "reasoning": reasoning,
        "score": module_data["score"],
        "all_matched_keywords": module_data["matched_keywords"]
    }

def analyze_work_items(work_items: List[Dict]) -> Dict[str, Any]:
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
        state = fields.get("System.State", "")
        
        # Only analyze items in "New" state (matching your query criteria)
        if state != "New":
            continue
        
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
                "state": state,
                "assigned_to": fields.get("System.AssignedTo")
            })
            
            # Generate suggestion
            suggestion = analyze_work_item_for_module(item)
            if suggestion["suggested_module"] and suggestion["confidence"] in ["Very High", "High", "Medium-High"]:
                suggestions.append({
                    "id": item_id,
                    "title": title,
                    "suggested_module": suggestion["suggested_module"],
                    "confidence": suggestion["confidence"],
                    "reasoning": suggestion["reasoning"],
                    "score": suggestion.get("score", 0),
                    "assigned_to": fields.get("System.AssignedTo")
                })
    
    # Group suggestions by module
    suggestions_by_module = defaultdict(list)
    for suggestion in suggestions:
        module = suggestion["suggested_module"]
        suggestions_by_module[module].append(suggestion)
    
    return {
        "total_items_analyzed": len([i for i in work_items if i.get("fields", {}).get("System.State") == "New"]),
        "items_with_module": len(items_with_module),
        "items_without_module": len(items_without_module),
        "total_suggestions": len(suggestions),
        "suggestions": suggestions,
        "suggestions_by_module": dict(suggestions_by_module),
        "module_distribution": Counter(item["module"] for item in items_with_module)
    }

if __name__ == "__main__":
    print("Product First ImpactedModule Analysis")
    print("=" * 60)
    print("\nBased on query: pf dynamic query")
    print("Query ID: 72a30e06-aede-48bb-b9e8-aa35d0cce63f")
    print("\nThis script analyzes work items and generates ImpactedModule suggestions.")
    print("To use: Fetch work items and pass them to analyze_work_items()")











