"""
Comprehensive analysis of Product First Request CSV data
"""

import csv
import json
from datetime import datetime, timezone
from collections import Counter, defaultdict
from typing import Dict, List, Any
import re

def parse_date(date_str):
    """Parse date string, return None if invalid"""
    if not date_str or date_str.strip() == '':
        return None
    # Try various date formats
    formats = ['%Y-%m-%d', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%dT%H:%M:%S.%f', '%Y-%m-%dT%H:%M:%SZ']
    for fmt in formats:
        try:
            return datetime.strptime(date_str.split('T')[0], '%Y-%m-%d')
        except:
            continue
    return None

def calculate_age_in_days(created_date, reference_date=None):
    """Calculate age in days"""
    if reference_date is None:
        reference_date = datetime.now(timezone.utc)
    
    if created_date is None:
        return None
    
    if isinstance(created_date, str):
        created_date = parse_date(created_date)
        if created_date is None:
            return None
    
    if created_date.tzinfo is None:
        created_date = created_date.replace(tzinfo=timezone.utc)
    
    delta = reference_date - created_date
    return delta.days

def extract_impacted_module(description):
    """Try to extract Impacted Module from description or tags"""
    if not description:
        return None
    
    # Common patterns
    patterns = [
        r'Impacted Module[:\s]+([A-Za-z0-9\s&]+)',
        r'Module[:\s]+([A-Za-z0-9\s&]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, description, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    
    return None

def analyze_csv(filename='pfrs (1).csv'):
    """Analyze the entire CSV file"""
    
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
        'items_with_commitment_tag': [],
        'age_distribution': {
            '0-30_days': 0,
            '31-90_days': 0,
            '91-180_days': 0,
            '181-365_days': 0,
            '365-730_days': 0,
            '730-1095_days': 0,
            '1095+_days': 0
        },
        'items_by_year': Counter(),
        'longest_in_new': [],
        'assignment_by_state': defaultdict(Counter),
    }
    
    now = datetime.now(timezone.utc)
    
    with open(filename, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            stats['total'] += 1
            
            # Clean ID (remove BOM if present)
            item_id = row.get('\ufeffID', row.get('ID', '')).strip()
            if not item_id:
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
            else:
                # Extract name from email format
                if '<' in assigned_to:
                    name = assigned_to.split('<')[0].strip()
                else:
                    name = assigned_to
                assigned_to = name
            
            stats['assignments'][assigned_to] += 1
            stats['assignment_by_state'][state][assigned_to] += 1
            
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
            
            # Description (for potential Impacted Module extraction)
            description = row.get('Description', '')
            
            # Try to extract created date from description or other fields
            # For now, we'll need to query DevOps for dates
            created_date = None
            
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
    
    # Sort new state items (we'll add age later after querying DevOps)
    stats['new_state_items'].sort(key=lambda x: int(x['id']) if x['id'].isdigit() else 0)
    
    return stats

def format_analysis_report(stats):
    """Format comprehensive analysis report"""
    
    report = []
    report.append("# Product First Request - Complete CSV Dataset Analysis\n")
    report.append(f"**Analysis Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    report.append(f"**Total Items Analyzed**: {stats['total']}\n")
    
    # State Distribution
    report.append("\n## State Distribution\n")
    total = stats['total']
    for state, count in stats['states'].most_common():
        percentage = (count / total * 100) if total > 0 else 0
        report.append(f"- **{state}**: {count} ({percentage:.1f}%)")
    
    # Work Item Types
    report.append("\n## Work Item Type Distribution\n")
    for witype, count in stats['work_item_types'].most_common():
        percentage = (count / total * 100) if total > 0 else 0
        report.append(f"- **{witype}**: {count} ({percentage:.1f}%)")
    
    # Assignment Analysis
    report.append("\n## Assignment Distribution\n")
    report.append(f"**Total Unassigned Items**: {len(stats['unassigned_items'])} ({len(stats['unassigned_items'])/total*100:.1f}%)\n")
    report.append("**Top 15 Assignees**:\n")
    for assignee, count in stats['assignments'].most_common(15):
        percentage = (count / total * 100) if total > 0 else 0
        report.append(f"- **{assignee}**: {count} items ({percentage:.1f}%)")
    
    # Assignment by State
    report.append("\n## Assignment Distribution by State\n")
    for state in ['New', 'Active', 'Pending']:
        if state in stats['assignment_by_state']:
            report.append(f"\n### {state} State Assignments\n")
            for assignee, count in stats['assignment_by_state'][state].most_common(10):
                report.append(f"- **{assignee}**: {count} items")
    
    # Unassigned Items
    report.append("\n## Unassigned Items Analysis\n")
    report.append(f"**Total Unassigned**: {len(stats['unassigned_items'])}\n")
    unassigned_by_state = Counter([item['state'] for item in stats['unassigned_items']])
    for state, count in unassigned_by_state.most_common():
        report.append(f"- **{state}**: {count} unassigned items")
    
    if len(stats['unassigned_items']) > 0:
        report.append("\n### Sample Unassigned Items (First 20)\n")
        report.append("| Item ID | Title | State |")
        report.append("|---------|-------|-------|")
        for item in stats['unassigned_items'][:20]:
            title = item['title'][:60] + '...' if len(item['title']) > 60 else item['title']
            report.append(f"| {item['id']} | {title} | {item['state']} |")
    
    # New State Items
    report.append("\n## Items in 'New' State\n")
    report.append(f"**Total items in 'New' state**: {len(stats['new_state_items'])}\n")
    
    if len(stats['new_state_items']) > 0:
        new_unassigned = [item for item in stats['new_state_items'] if item['assigned_to'] == 'Unassigned']
        report.append(f"**Unassigned items in 'New' state**: {len(new_unassigned)} ({len(new_unassigned)/len(stats['new_state_items'])*100:.1f}%)\n")
        
        report.append("### New State Items by Assignee\n")
        new_assignments = Counter([item['assigned_to'] for item in stats['new_state_items']])
        for assignee, count in new_assignments.most_common(15):
            percentage = (count / len(stats['new_state_items']) * 100) if len(stats['new_state_items']) > 0 else 0
            report.append(f"- **{assignee}**: {count} items ({percentage:.1f}%)")
    
    # Active State Items
    report.append("\n## Items in 'Active' State\n")
    report.append(f"**Total items in 'Active' state**: {len(stats['active_state_items'])}\n")
    
    # Pending State Items
    report.append("\n## Items in 'Pending' State\n")
    report.append(f"**Total items in 'Pending' state**: {len(stats['pending_state_items'])}\n")
    
    # Commitments
    report.append("\n## Commitments Analysis\n")
    report.append(f"**Items with 'Commitment' tag**: {len(stats['items_with_commitment_tag'])}\n")
    
    if len(stats['items_with_commitment_tag']) > 0:
        commitment_by_state = Counter([item['state'] for item in stats['items_with_commitment_tag']])
        report.append("### Commitments by State\n")
        for state, count in commitment_by_state.most_common():
            report.append(f"- **{state}**: {count} commitments")
        
        report.append("\n### Sample Commitment Items (First 20)\n")
        report.append("| Item ID | Title | State | Assigned To |")
        report.append("|---------|-------|-------|-------------|")
        for item in stats['items_with_commitment_tag'][:20]:
            title = item['title'][:50] + '...' if len(item['title']) > 50 else item['title']
            report.append(f"| {item['id']} | {title} | {item['state']} | {item['assigned_to']} |")
    
    # Tags Analysis
    report.append("\n## Most Common Tags\n")
    for tag, count in stats['tags'].most_common(20):
        percentage = (count / total * 100) if total > 0 else 0
        report.append(f"- **{tag}**: {count} items ({percentage:.1f}%)")
    
    return "\n".join(report)

if __name__ == "__main__":
    print("Analyzing PFR CSV file...")
    stats = analyze_csv('pfrs (1).csv')
    
    print(f"\nTotal items: {stats['total']}")
    print(f"New state: {len(stats['new_state_items'])}")
    print(f"Active state: {len(stats['active_state_items'])}")
    print(f"Pending state: {len(stats['pending_state_items'])}")
    print(f"Unassigned: {len(stats['unassigned_items'])}")
    print(f"Commitments: {len(stats['items_with_commitment_tag'])}")
    
    # Generate report
    report = format_analysis_report(stats)
    
    # Save report
    with open('pfr_csv_analysis_report.md', 'w', encoding='utf-8') as f:
        f.write(report)
    
    # Save stats as JSON for further analysis
    # Convert Counter objects to dicts for JSON serialization
    stats_json = {
        'total': stats['total'],
        'states': dict(stats['states']),
        'assignments': dict(stats['assignments']),
        'tags': dict(stats['tags']),
        'work_item_types': dict(stats['work_item_types']),
        'new_state_count': len(stats['new_state_items']),
        'active_state_count': len(stats['active_state_items']),
        'pending_state_count': len(stats['pending_state_items']),
        'unassigned_count': len(stats['unassigned_items']),
        'commitments_count': len(stats['items_with_commitment_tag']),
    }
    
    with open('pfr_csv_stats.json', 'w', encoding='utf-8') as f:
        json.dump(stats_json, f, indent=2)
    
    print("\nAnalysis complete!")
    print("Reports saved to:")
    print("  - pfr_csv_analysis_report.md")
    print("  - pfr_csv_stats.json")






