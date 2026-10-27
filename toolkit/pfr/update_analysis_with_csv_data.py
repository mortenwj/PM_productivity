"""
Update the Product First Request analysis with complete CSV dataset
"""

import csv
from datetime import datetime, timezone
from collections import Counter, defaultdict

def calculate_age_in_days(created_date_str, reference_date=None):
    """Calculate age in days"""
    if reference_date is None:
        reference_date = datetime.now(timezone.utc)
    
    if not created_date_str:
        return None
    
    try:
        created_date = datetime.fromisoformat(created_date_str.replace('Z', '+00:00'))
        if created_date.tzinfo is None:
            created_date = created_date.replace(tzinfo=timezone.utc)
        delta = reference_date - created_date
        return delta.days
    except:
        return None

def analyze_csv_with_ages(filename='pfrs (1).csv'):
    """Analyze CSV and calculate ages for items we have DevOps data for"""
    
    # Known items with DevOps data (from previous queries)
    devops_data = {
        '44760': {'created': '2020-02-06T08:50:40.237Z', 'impacted_module': None, 'assigned_to': None},
        '70014': {'created': '2020-08-31T06:01:47.27Z', 'impacted_module': 'UI-UX', 'assigned_to': 'Jarle Steira'},
        '70591': {'created': '2020-09-02T13:49:16.31Z', 'impacted_module': None, 'assigned_to': None},
        '76721': {'created': '2020-10-09T09:47:33.407Z', 'impacted_module': None, 'assigned_to': None},
        '81262': {'created': '2020-11-06T10:37:52.993Z', 'impacted_module': None, 'assigned_to': None},
        '93675': {'created': '2021-02-08T10:05:25.06Z', 'impacted_module': None, 'assigned_to': None},
        '98916': {'created': '2021-03-11T03:33:28.02Z', 'impacted_module': 'Process Engine', 'assigned_to': None},
        '105333': {'created': '2021-04-28T10:32:47.43Z', 'impacted_module': None, 'assigned_to': None},
        '114199': {'created': '2021-07-01T12:52:14.073Z', 'impacted_module': 'Search', 'assigned_to': None},
        '127699': {'created': '2021-10-04T09:42:01.873Z', 'impacted_module': 'Transfer to Public 360', 'assigned_to': None},
        '134549': {'created': '2021-11-23T14:32:45.06Z', 'impacted_module': None, 'assigned_to': None},
        '141216': {'created': '2022-01-13T09:27:58.533Z', 'impacted_module': 'Plan&Build', 'assigned_to': 'Tone Fjeller'},
        '141222': {'created': '2022-01-13T09:36:59.177Z', 'impacted_module': 'Plan&Build', 'assigned_to': None},
        '151816': {'created': '2022-03-29T10:52:14.237Z', 'impacted_module': 'Plan&Build', 'assigned_to': 'Tone Fjeller'},
        '166475': {'created': '2022-07-07T08:29:36.21Z', 'impacted_module': 'Charts', 'assigned_to': 'Bjørn Tore Eriksen'},
        '166648': {'created': '2022-07-08T10:17:36.27Z', 'impacted_module': 'Process Engine', 'assigned_to': 'Bjørn Kristiansen'},
        '175102': {'created': '2022-09-09T11:57:32.473Z', 'impacted_module': 'Doc production', 'assigned_to': 'Willy Koch'},
        '175426': {'created': '2022-09-13T06:52:12.163Z', 'impacted_module': 'Dispatch', 'assigned_to': 'Willy Koch'},
        '177276': {'created': '2022-09-21T10:50:38.19Z', 'impacted_module': 'Document', 'assigned_to': 'Jarle Steira'},
        '177289': {'created': '2022-09-21T11:17:22.913Z', 'impacted_module': 'IFAR', 'assigned_to': 'Morten Jensen'},
        '177814': {'created': '2022-09-26T06:55:09.04Z', 'impacted_module': 'IFAR', 'assigned_to': 'Morten Jensen'},
        '177823': {'created': '2022-09-26T07:18:11.113Z', 'impacted_module': 'IFAR', 'assigned_to': 'Morten Jensen'},
        '178225': {'created': '2022-09-27T13:39:37.927Z', 'impacted_module': 'Webparts', 'assigned_to': 'Morten Jensen'},
        '178371': {'created': '2022-09-28T06:28:05.83Z', 'impacted_module': 'IFAR', 'assigned_to': 'Morten Jensen'},
        '179962': {'created': '2022-10-05T09:14:43.717Z', 'impacted_module': 'File Operations', 'assigned_to': 'Willy Koch'},
        '180555': {'created': '2022-10-07T13:46:58.807Z', 'impacted_module': 'eArchive', 'assigned_to': 'Willy Koch'},
        '182730': {'created': '2022-10-20T06:14:58.61Z', 'impacted_module': '0 - Not applicable', 'assigned_to': None},
        '189357': {'created': '2022-12-02T09:07:25.793Z', 'impacted_module': 'Reports', 'assigned_to': 'Lisa Olausson'},
        '196608': {'created': '2023-01-04T08:51:34.14Z', 'impacted_module': 'Access Group', 'assigned_to': 'Willy Koch'},
        '197887': {'created': '2023-01-11T12:06:35.893Z', 'impacted_module': 'Progress plan', 'assigned_to': None},
    }
    
    stats = {
        'total': 0,
        'states': Counter(),
        'assignments': Counter(),
        'new_state_items': [],
        'unassigned_new': [],
        'oldest_new_items': [],
        'impacted_modules': Counter(),
        'missing_impacted_module': [],
    }
    
    now = datetime.now(timezone.utc)
    
    with open(filename, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            stats['total'] += 1
            
            item_id = row.get('\ufeffID', row.get('ID', '')).strip()
            if not item_id or not item_id.isdigit():
                continue
            
            state = row.get('State', '').strip()
            stats['states'][state] += 1
            
            assigned_to = row.get('Assigned To', '').strip()
            if not assigned_to:
                assigned_to = 'Unassigned'
            else:
                if '<' in assigned_to:
                    assigned_to = assigned_to.split('<')[0].strip()
            
            stats['assignments'][assigned_to] += 1
            
            if state == 'New':
                title = row.get('Title', '').strip()
                
                # Get DevOps data if available
                devops_info = devops_data.get(item_id, {})
                created_date = devops_info.get('created')
                impacted_module = devops_info.get('impacted_module')
                
                age_days = None
                if created_date:
                    age_days = calculate_age_in_days(created_date, now)
                
                item_data = {
                    'id': item_id,
                    'title': title,
                    'assigned_to': assigned_to,
                    'age_days': age_days,
                    'created_date': created_date,
                    'impacted_module': impacted_module
                }
                
                stats['new_state_items'].append(item_data)
                
                if assigned_to == 'Unassigned':
                    stats['unassigned_new'].append(item_data)
                
                if impacted_module:
                    if impacted_module == '0 - Not applicable':
                        stats['missing_impacted_module'].append(item_data)
                    else:
                        stats['impacted_modules'][impacted_module] += 1
                else:
                    stats['missing_impacted_module'].append(item_data)
                
                if age_days:
                    stats['oldest_new_items'].append(item_data)
    
    # Sort by age
    stats['oldest_new_items'].sort(key=lambda x: x['age_days'] if x['age_days'] else 0, reverse=True)
    stats['new_state_items'].sort(key=lambda x: int(x['id']))
    
    return stats

if __name__ == "__main__":
    print("Analyzing CSV with age calculations...")
    stats = analyze_csv_with_ages('pfrs (1).csv')
    
    print(f"\nTotal: {stats['total']}")
    print(f"New state: {len(stats['new_state_items'])}")
    print(f"Unassigned in New: {len(stats['unassigned_new'])}")
    print(f"Oldest items with dates: {len(stats['oldest_new_items'])}")
    print(f"\nTop 10 oldest items:")
    for item in stats['oldest_new_items'][:10]:
        age = item['age_days']
        age_years = age / 365.25 if age else 0
        print(f"  ID {item['id']}: {age} days ({age_years:.1f} years) - {item['title'][:50]}")






