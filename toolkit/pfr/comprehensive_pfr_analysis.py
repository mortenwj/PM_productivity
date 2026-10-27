"""
Comprehensive analysis of Product First Request CSV data with DevOps integration
"""

import csv
import json
from datetime import datetime, timezone
from collections import Counter, defaultdict
from typing import Dict, List, Any
import re

def parse_date(date_str):
    """Parse date string"""
    if not date_str or date_str.strip() == '':
        return None
    try:
        return datetime.fromisoformat(date_str.split('T')[0])
    except:
        return None

def calculate_age_in_days(created_date_str, reference_date=None):
    """Calculate age in days"""
    if reference_date is None:
        reference_date = datetime.now(timezone.utc)
    
    if created_date_str is None:
        return None
    
    created_date = parse_date(created_date_str)
    if created_date is None:
        return None
    
    if created_date.tzinfo is None:
        created_date = created_date.replace(tzinfo=timezone.utc)
    
    delta = reference_date - created_date
    return delta.days

def analyze_full_csv(filename='pfrs (1).csv'):
    """Comprehensive analysis of the full CSV"""
    
    stats = {
        'total': 0,
        'states': Counter(),
        'assignments': Counter(),
        'tags': Counter(),
        'work_item_types': Counter(),
        'new_state_items': [],
        'active_state_items': [],
        'pending_state_items': [],
        'removed_state_items': [],
        'unassigned_items': [],
        'unassigned_new_items': [],
        'items_with_commitment_tag': [],
        'items_by_year': Counter(),
        'assignment_by_state': defaultdict(Counter),
        'new_state_by_assignee': Counter(),
        'age_ranges': {
            '0-30_days': 0,
            '31-90_days': 0,
            '91-180_days': 0,
            '181-365_days': 0,
            '365-730_days': 0,
            '730-1095_days': 0,
            '1095+_days': 0
        }
    }
    
    now = datetime.now(timezone.utc)
    
    print(f"Reading CSV file: {filename}")
    with open(filename, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            stats['total'] += 1
            
            # Clean ID
            item_id = row.get('\ufeffID', row.get('ID', '')).strip()
            if not item_id or not item_id.isdigit():
                continue
            
            # State
            state = row.get('State', '').strip()
            stats['states'][state] += 1
            
            # Work Item Type
            work_item_type = row.get('Work Item Type', '').strip()
            stats['work_item_types'][work_item_type] += 1
            
            # Assignment
            assigned_to = row.get('Assigned To', '').strip()
            if not assigned_to or assigned_to == '':
                assigned_to = 'Unassigned'
                stats['unassigned_items'].append({
                    'id': item_id,
                    'title': row.get('Title', '')[:100],
                    'state': state
                })
                if state == 'New':
                    stats['unassigned_new_items'].append(item_id)
            else:
                # Extract name from email format
                if '<' in assigned_to:
                    name = assigned_to.split('<')[0].strip()
                else:
                    name = assigned_to
                assigned_to = name
            
            stats['assignments'][assigned_to] += 1
            stats['assignment_by_state'][state][assigned_to] += 1
            
            if state == 'New':
                stats['new_state_by_assignee'][assigned_to] += 1
            
            # Tags
            tags = row.get('Tags', '').strip()
            if tags:
                tag_list = [t.strip() for t in tags.split(';') if t.strip()]
                for tag in tag_list:
                    stats['tags'][tag] += 1
                    if 'Commitment' in tag or 'commitment' in tag.lower():
                        stats['items_with_commitment_tag'].append({
                            'id': item_id,
                            'title': row.get('Title', '')[:100],
                            'state': state,
                            'assigned_to': assigned_to
                        })
            
            # Title
            title = row.get('Title', '').strip()
            
            # Categorize by state
            item_data = {
                'id': item_id,
                'title': title,
                'state': state,
                'assigned_to': assigned_to,
                'tags': tags,
                'work_item_type': work_item_type
            }
            
            if state == 'New':
                stats['new_state_items'].append(item_data)
            elif state == 'Active':
                stats['active_state_items'].append(item_data)
            elif state == 'Pending':
                stats['pending_state_items'].append(item_data)
            elif state == 'Removed':
                stats['removed_state_items'].append(item_data)
    
    # Sort new state items by ID (proxy for age - older items have lower IDs)
    stats['new_state_items'].sort(key=lambda x: int(x['id']) if x['id'].isdigit() else 0)
    
    return stats

def format_comprehensive_report(stats):
    """Format comprehensive analysis report"""
    
    report = []
    report.append("# Product First Request - Complete Dataset Analysis\n")
    report.append(f"**Analysis Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    report.append(f"**Data Source**: Complete CSV export from Azure DevOps\n")
    report.append(f"**Total Items Analyzed**: {stats['total']}\n")
    
    # Executive Summary
    report.append("## Executive Summary\n")
    report.append(f"**CRITICAL FINDINGS**:\n")
    report.append(f"- **Total Product First Requests**: {stats['total']}")
    report.append(f"- **Items in 'New' state**: {len(stats['new_state_items'])} ({len(stats['new_state_items'])/stats['total']*100:.1f}%)")
    report.append(f"- **Unassigned items**: {len(stats['unassigned_items'])} ({len(stats['unassigned_items'])/stats['total']*100:.1f}%)")
    report.append(f"- **Unassigned items in 'New' state**: {len(stats['unassigned_new_items'])} ({len(stats['unassigned_new_items'])/len(stats['new_state_items'])*100:.1f}% of New items)")
    report.append(f"- **Items with 'Commitment' tag**: {len(stats['items_with_commitment_tag'])}\n")
    
    # State Distribution
    report.append("\n## State Distribution\n")
    total = stats['total']
    for state, count in stats['states'].most_common():
        if state and state.strip():
            percentage = (count / total * 100) if total > 0 else 0
            report.append(f"- **{state}**: {count} ({percentage:.1f}%)")
    
    # New State Analysis
    report.append("\n## Items in 'New' State - Detailed Analysis\n")
    report.append(f"**Total items in 'New' state**: {len(stats['new_state_items'])}\n")
    report.append(f"**This represents {len(stats['new_state_items'])/total*100:.1f}% of all Product First Requests**\n")
    
    report.append("### New State Items by Assignee\n")
    for assignee, count in stats['new_state_by_assignee'].most_common(20):
        percentage = (count / len(stats['new_state_items']) * 100) if len(stats['new_state_items']) > 0 else 0
        report.append(f"- **{assignee}**: {count} items ({percentage:.1f}%)")
    
    # Unassigned Items
    report.append("\n## Unassigned Items - Critical Issue\n")
    report.append(f"**Total Unassigned Items**: {len(stats['unassigned_items'])} ({len(stats['unassigned_items'])/total*100:.1f}%)\n")
    report.append(f"**Unassigned Items in 'New' State**: {len(stats['unassigned_new_items'])} ({len(stats['unassigned_new_items'])/len(stats['new_state_items'])*100:.1f}% of New items)\n")
    
    unassigned_by_state = Counter([item['state'] for item in stats['unassigned_items']])
    report.append("### Unassigned Items by State\n")
    for state, count in unassigned_by_state.most_common():
        if state and state.strip():
            report.append(f"- **{state}**: {count} unassigned items")
    
    # Assignment Distribution
    report.append("\n## Overall Assignment Distribution\n")
    report.append("**Top 20 Assignees**:\n")
    for assignee, count in stats['assignments'].most_common(20):
        percentage = (count / total * 100) if total > 0 else 0
        report.append(f"- **{assignee}**: {count} items ({percentage:.1f}%)")
    
    # Commitments
    report.append("\n## Commitments Analysis\n")
    report.append(f"**Items with 'Commitment' tag**: {len(stats['items_with_commitment_tag'])}\n")
    
    if len(stats['items_with_commitment_tag']) > 0:
        commitment_by_state = Counter([item['state'] for item in stats['items_with_commitment_tag']])
        report.append("### Commitments by State\n")
        for state, count in commitment_by_state.most_common():
            report.append(f"- **{state}**: {count} commitments")
    
    # Tags Analysis
    report.append("\n## Most Common Tags\n")
    for tag, count in stats['tags'].most_common(25):
        if tag and tag.strip() and len(tag) < 100:  # Filter out corrupted data
            percentage = (count / total * 100) if total > 0 else 0
            report.append(f"- **{tag}**: {count} items ({percentage:.1f}%)")
    
    return "\n".join(report)

if __name__ == "__main__":
    print("Starting comprehensive PFR analysis...")
    stats = analyze_full_csv('pfrs (1).csv')
    
    print(f"\n=== KEY STATISTICS ===")
    print(f"Total items: {stats['total']}")
    print(f"New state: {len(stats['new_state_items'])} ({len(stats['new_state_items'])/stats['total']*100:.1f}%)")
    print(f"Active state: {len(stats['active_state_items'])}")
    print(f"Pending state: {len(stats['pending_state_items'])}")
    print(f"Unassigned: {len(stats['unassigned_items'])} ({len(stats['unassigned_items'])/stats['total']*100:.1f}%)")
    print(f"Unassigned in New: {len(stats['unassigned_new_items'])} ({len(stats['unassigned_new_items'])/len(stats['new_state_items'])*100:.1f}% of New)")
    print(f"Commitments: {len(stats['items_with_commitment_tag'])}")
    
    # Generate report
    report = format_comprehensive_report(stats)
    
    # Save report
    with open('pfr_complete_analysis.md', 'w', encoding='utf-8') as f:
        f.write(report)
    
    print("\nAnalysis complete!")
    print("Report saved to: pfr_complete_analysis.md")
    print(f"\nTop 5 assignees for New state items:")
    for assignee, count in stats['new_state_by_assignee'].most_common(5):
        print(f"  {assignee}: {count} items")






