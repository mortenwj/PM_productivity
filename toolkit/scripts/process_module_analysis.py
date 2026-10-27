"""
Process the fetched work items to analyze ImpactedModule field.
"""

from collections import Counter

# Work items fetched from API (from the batch responses)
# This is a simplified version - in production would load from JSON

def count_impacted_modules():
    """Count items with and without ImpactedModule from actual API responses."""
    
    # Items WITH ImpactedModule (from actual API responses)
    items_with_module = [
        (401007, 'Teams Integration'),
        (401599, 'Contact'),
        (402252, 'Personal Digital Signing'),
        (402357, 'Plan&Build'),
        (402362, 'Plan&Build'),
        (402745, 'Public link'),
        (402792, 'Plan&Build'),
        (402793, 'Process Engine'),
        (403124, 'Surveying case'),
        (397379, 'Document'),
        (398055, 'Document'),
        (398834, 'Board meeting'),
        (398835, 'Board meeting'),
        (398940, 'Access matrix'),
        (399225, 'Document'),
        (399242, 'Plan&Build'),
        (400621, 'Webparts'),
        (400641, 'Plan&Build'),
        (400804, 'Plan&Build'),
        (400835, 'Plan&Build'),
        (392920, 'File center'),
        (392945, 'Document'),
        (392964, 'UI Configuration'),
        (393445, 'SIF'),
        (393959, 'SIF'),
        (395009, 'eArchive'),
        (395112, 'Plan&Build'),
        (395353, 'Building application case'),
        (391763, 'Mimir'),
        (391820, 'Plan&Build'),
        (391822, 'Plan&Build'),
        (391824, 'Plan&Build'),
        (391826, 'Plan&Build'),
        (391912, 'Complaint case'),
        (391940, 'UI Configuration'),
        (387052, 'Web admin'),
        (387074, 'Building application case'),
        (387189, 'UI Configuration'),
        (388359, 'UI-UX'),
        (388622, 'Fileviewer'),
        (388982, 'Webparts'),
        (389652, 'Board meeting'),
        (390252, 'eSignature'),
        (390555, 'Mimir'),
    ]
    
    # Items WITHOUT ImpactedModule (sampled from responses)
    items_without_module_ids = [
        401257, 402057, 402058, 402061, 402064, 402067, 402069, 402096, 402404,
        402494, 402776, 396070, 396439, 396473, 397219, 397521, 398108, 398392,
        398991, 399477, 392245, 392252, 393194, 393428, 393469, 394093, 394094,
        394101, 394294, 394522, 394858, 395112, 395352, 390575, 390577, 390828,
        390901, 391097, 391108, 391329, 391333, 391931, 391955, 392197, 392221,
        392223, 386857, 387124, 388115, 388699, 388830, 388885, 390086, 390243,
        390304, 390480, 390501
    ]
    
    total = len(items_with_module) + len(items_without_module_ids)
    with_count = len(items_with_module)
    without_count = len(items_without_module_ids)
    
    modules_counter = Counter([module for _, module in items_with_module])
    
    print("=" * 80)
    print("IMPACTED MODULE ANALYSIS - Product First Requests")
    print("=" * 80)
    print(f"\nTotal Work Items Analyzed: {total}")
    print(f"\nItems WITH ImpactedModule: {with_count} ({with_count/total*100:.1f}%)")
    print(f"Items WITHOUT ImpactedModule: {without_count} ({without_count/total*100:.1f}%)")
    
    print("\n" + "-" * 80)
    print("MODULE DISTRIBUTION (Top 15):")
    print("-" * 80)
    for module, count in modules_counter.most_common(15):
        percentage = (count / with_count * 100) if with_count > 0 else 0
        print(f"  {module:40s}: {count:3d} ({percentage:5.1f}% of items with module)")
    
    print("\n" + "-" * 80)
    print("SUMMARY:")
    print("-" * 80)
    print(f"  • More than half ({without_count/total*100:.1f}%) of Product First Requests")
    print(f"    are missing the ImpactedModule tag")
    print(f"  • This makes it difficult to route items to appropriate teams")
    print(f"  • Most common module when specified: {modules_counter.most_common(1)[0][0]}")
    
    return {
        'total': total,
        'with_module': with_count,
        'without_module': without_count,
        'modules': dict(modules_counter)
    }

if __name__ == "__main__":
    count_impacted_modules()

