"""
Analyze the full Product First Request dataset from the saved query.
This script retrieves all work items and performs comprehensive analysis.
"""

import json
from datetime import datetime, timezone
from collections import Counter, defaultdict
from typing import Dict, List, Any

# The query returned 500+ items. We'll need to process them in batches.
# For now, let's create a script that can analyze the data we've retrieved

def calculate_age_in_days(created_date_str: str, reference_date: datetime = None) -> int:
    """Calculate age in days from created date to reference date (default: now)"""
    if reference_date is None:
        reference_date = datetime.now(timezone.utc)
    
    try:
        created_date = datetime.fromisoformat(created_date_str.replace('Z', '+00:00'))
        if created_date.tzinfo is None:
            created_date = created_date.replace(tzinfo=timezone.utc)
        delta = reference_date - created_date
        return delta.days
    except:
        return 0

def analyze_work_items(work_items: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Analyze a list of work items and return statistics"""
    
    now = datetime.now(timezone.utc)
    stats = {
        'total': len(work_items),
        'states': Counter(),
        'impacted_modules': Counter(),
        'sources': Counter(),
        'priorities': Counter(),
        'assignments': Counter(),
        'missing_impacted_module': [],
        'placeholder_impacted_module': [],
        'new_state_items': [],
        'age_distribution': {
            '0-30_days': 0,
            '31-90_days': 0,
            '91-180_days': 0,
            '181-365_days': 0,
            '365+_days': 0
        },
        'target_dates': {
            'with_target_date': 0,
            'past_due': [],
            'future_due': []
        },
        'commitments': {
            'total': 0,
            'past_due': 0
        }
    }
    
    for item in work_items:
        fields = item.get('fields', {})
        
        # State
        state = fields.get('System.State', 'Unknown')
        stats['states'][state] += 1
        
        # Impacted Module
        impacted_module = fields.get('Custom.ImpactedModule', '')
        if not impacted_module:
            stats['missing_impacted_module'].append({
                'id': item.get('id'),
                'title': fields.get('System.Title', ''),
                'state': state,
                'created': fields.get('System.CreatedDate', '')
            })
        elif impacted_module == '0 - Not applicable':
            stats['placeholder_impacted_module'].append({
                'id': item.get('id'),
                'title': fields.get('System.Title', ''),
                'state': state,
                'created': fields.get('System.CreatedDate', '')
            })
        else:
            stats['impacted_modules'][impacted_module] += 1
        
        # Source
        source = fields.get('Custom.Source', 'Unknown')
        stats['sources'][source] += 1
        
        # Priority
        priority = fields.get('Microsoft.VSTS.Common.Priority', 'Unknown')
        stats['priorities'][priority] += 1
        
        # Assignment
        assigned_to = fields.get('System.AssignedTo', {})
        if isinstance(assigned_to, dict):
            assignee_name = assigned_to.get('displayName', 'Unassigned')
        else:
            assignee_name = 'Unassigned'
        stats['assignments'][assignee_name] += 1
        
        # Age analysis for "New" state items
        if state == 'New':
            created_date = fields.get('System.CreatedDate', '')
            age_days = calculate_age_in_days(created_date, now)
            
            stats['new_state_items'].append({
                'id': item.get('id'),
                'title': fields.get('System.Title', ''),
                'age_days': age_days,
                'created': created_date,
                'impacted_module': impacted_module,
                'assigned_to': assignee_name
            })
            
            # Age distribution
            if age_days <= 30:
                stats['age_distribution']['0-30_days'] += 1
            elif age_days <= 90:
                stats['age_distribution']['31-90_days'] += 1
            elif age_days <= 180:
                stats['age_distribution']['91-180_days'] += 1
            elif age_days <= 365:
                stats['age_distribution']['181-365_days'] += 1
            else:
                stats['age_distribution']['365+_days'] += 1
        
        # Target dates and commitments
        target_date = fields.get('Microsoft.VSTS.Scheduling.TargetDate', '')
        if target_date:
            stats['target_dates']['with_target_date'] += 1
            try:
                target_dt = datetime.fromisoformat(target_date.replace('Z', '+00:00'))
                if target_dt.tzinfo is None:
                    target_dt = target_dt.replace(tzinfo=timezone.utc)
                
                if target_dt < now:
                    stats['target_dates']['past_due'].append({
                        'id': item.get('id'),
                        'title': fields.get('System.Title', ''),
                        'target_date': target_date,
                        'days_overdue': (now - target_dt).days,
                        'state': state
                    })
                    stats['commitments']['past_due'] += 1
                else:
                    stats['target_dates']['future_due'].append({
                        'id': item.get('id'),
                        'title': fields.get('System.Title', ''),
                        'target_date': target_date,
                        'days_remaining': (target_dt - now).days,
                        'state': state
                    })
            except:
                pass
        
        # Check for commitment tag
        tags = fields.get('System.Tags', '')
        if 'Commitment' in str(tags):
            stats['commitments']['total'] += 1
    
    # Sort new state items by age
    stats['new_state_items'].sort(key=lambda x: x['age_days'], reverse=True)
    
    return stats

def format_analysis_report(stats: Dict[str, Any]) -> str:
    """Format the analysis statistics into a readable report"""
    
    report = []
    report.append("# Full Product First Request Dataset Analysis\n")
    report.append(f"**Analysis Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    report.append(f"**Total Items Analyzed**: {stats['total']}\n")
    
    # State Distribution
    report.append("\n## State Distribution\n")
    total = stats['total']
    for state, count in stats['states'].most_common():
        percentage = (count / total * 100) if total > 0 else 0
        report.append(f"- **{state}**: {count} ({percentage:.1f}%)")
    
    # Age Analysis for New State Items
    report.append("\n## Age Analysis - Items in 'New' State\n")
    new_items = stats['new_state_items']
    report.append(f"**Total items in 'New' state**: {len(new_items)}\n")
    
    if new_items:
        report.append("### Age Distribution\n")
        for range_name, count in stats['age_distribution'].items():
            if count > 0:
                report.append(f"- **{range_name.replace('_', ' ')}**: {count} items")
        
        report.append("\n### Oldest Items in 'New' State (Top 20)\n")
        report.append("| Item ID | Age (Days) | Age (Months) | Title | Impacted Module | Assigned To |")
        report.append("|---------|------------|--------------|-------|-----------------|-------------|")
        
        for item in new_items[:20]:
            age_days = item['age_days']
            age_months = f"{age_days / 30:.1f}"
            title = item['title'][:50] + '...' if len(item['title']) > 50 else item['title']
            report.append(f"| {item['id']} | {age_days} | {age_months} | {title} | {item.get('impacted_module', 'N/A')} | {item.get('assigned_to', 'Unassigned')} |")
    
    # Assignment Analysis
    report.append("\n## Assignment Distribution\n")
    report.append("**Top 10 Assignees**:\n")
    for assignee, count in stats['assignments'].most_common(10):
        percentage = (count / total * 100) if total > 0 else 0
        report.append(f"- **{assignee}**: {count} items ({percentage:.1f}%)")
    
    # Impacted Module Analysis
    report.append("\n## Impacted Module Distribution\n")
    total_with_module = sum(stats['impacted_modules'].values())
    for module, count in stats['impacted_modules'].most_common(15):
        percentage = (count / total_with_module * 100) if total_with_module > 0 else 0
        report.append(f"- **{module}**: {count} ({percentage:.1f}%)")
    
    # Missing Impacted Module
    report.append("\n## Data Quality - Missing Impacted Module\n")
    missing_count = len(stats['missing_impacted_module'])
    placeholder_count = len(stats['placeholder_impacted_module'])
    total_issues = missing_count + placeholder_count
    percentage = (total_issues / total * 100) if total > 0 else 0
    
    report.append(f"**Items with missing Impacted Module**: {missing_count}")
    report.append(f"**Items with placeholder '0 - Not applicable'**: {placeholder_count}")
    report.append(f"**Total data quality issues**: {total_issues} ({percentage:.1f}%)\n")
    
    if stats['missing_impacted_module']:
        report.append("### Items Missing Impacted Module\n")
        report.append("| Item ID | Title | State | Created Date |")
        report.append("|---------|-------|-------|--------------|")
        for item in stats['missing_impacted_module'][:20]:
            title = item['title'][:60] + '...' if len(item['title']) > 60 else item['title']
            created = item['created'][:10] if item['created'] else 'N/A'
            report.append(f"| {item['id']} | {title} | {item['state']} | {created} |")
    
    # Source Distribution
    report.append("\n## Source Distribution\n")
    for source, count in stats['sources'].most_common():
        percentage = (count / total * 100) if total > 0 else 0
        report.append(f"- **{source}**: {count} ({percentage:.1f}%)")
    
    # Priority Distribution
    report.append("\n## Priority Distribution\n")
    for priority, count in sorted(stats['priorities'].items()):
        percentage = (count / total * 100) if total > 0 else 0
        report.append(f"- **Priority {priority}**: {count} ({percentage:.1f}%)")
    
    # Commitments Analysis
    report.append("\n## Commitments Analysis\n")
    report.append(f"**Total items with 'Commitment' tag**: {stats['commitments']['total']}")
    report.append(f"**Items with target dates**: {stats['target_dates']['with_target_date']}")
    report.append(f"**Past due commitments**: {stats['commitments']['past_due']}\n")
    
    if stats['target_dates']['past_due']:
        report.append("### Past Due Items (Top 20)\n")
        report.append("| Item ID | Days Overdue | Target Date | Title | State |")
        report.append("|---------|--------------|-------------|-------|-------|")
        
        sorted_past_due = sorted(stats['target_dates']['past_due'], 
                                key=lambda x: x['days_overdue'], reverse=True)
        for item in sorted_past_due[:20]:
            title = item['title'][:50] + '...' if len(item['title']) > 50 else item['title']
            target = item['target_date'][:10] if item['target_date'] else 'N/A'
            report.append(f"| {item['id']} | {item['days_overdue']} | {target} | {title} | {item['state']} |")
    
    return "\n".join(report)

if __name__ == "__main__":
    print("This script provides analysis functions for PFR work items.")
    print("To use, import the functions and pass work item data to analyze_work_items()")
    print("Then format the results with format_analysis_report()")






