# Process Engine Module Page - Update Sections

## Section 1: Update Key Info Section

**Location:** In the "Key info" box at the top

**Find this line:**
```
* Applies to version(s): '''360° version 5.x or 4.1 SP7 feature pack 3 or newer'''
```

**Replace with:**
```
* Applies to version(s): '''360° version 5.x or 4.1 SP7 feature pack 3 or newer''' (Note: Many recent features require version 5.13+ or 5.17+)
```

**Also find:**
```
* Other requirements: '''Visual Studio Tools for 360 - Meta Administrator''' and '''Microsoft Visual Studio 2012 or newer'''
```

**Replace with:**
```
* Other requirements: '''Visual Studio Tools for 360 - Meta Administrator''' and '''Microsoft Visual Studio 2012 or newer''' (Note: Visual Studio 2019 onwards versions are unsupported for workunit creations)
```

---

## Section 2: Add Recent Enhancements Section

**Location:** Add this NEW section right after the paragraph ending with "enhance support for complex scenarios." and BEFORE "==== '''How it works''' ===="

**Add this content:**
```
=== Recent Enhancements (2021-2025) ===
The Process Engine module has received significant updates to improve process management, time tracking, and collaboration:

* '''Distribution Groups for Progress Plans''': Expand workflow distribution group functionality to progress plans, enabling better workload distribution and collaboration (Pilot in 6.7)
* '''Improved Time Calculation''': Enhanced active/passive time tracking with automatic nightly calculations and synchronization between progress plans and phases
* '''Deadline Management''': Automatic deadline recalculation for progress plans in passive state, ensuring accurate due dates
* '''Enhanced Development Tools''': Extended Process Engine BL with additional methods for metadata access and data type handling
* '''Visual Studio Compatibility''': Support for Visual Studio up to 2019 for workunit development
```

---

## Section 3: Add Key Features Section

**Location:** Add this NEW section right after "Recent Enhancements" and BEFORE "==== '''How it works''' ===="

**Add this content:**
```
=== Key Features ===
==== Process Design ====
* Design custom processes using predefined and automated components
* Support for sequential and dynamic processes
* Processes that change based on decisions or status
* Hibernate processes until events occur or time periods elapse
* Stop/start the clock on case progress

==== Process Execution ====
* Queue manager monitors deadlines and activities
* Automatic triggering of new activities in processes
* Distribution groups for progress plans (Pilot in 6.7)
* Pick/unpick functionality for task assignment
* Active/passive time tracking with automatic calculations

==== Development & Integration ====
* Visual Studio Tools for 360 - Meta Administrator integration
* Support for Visual Studio 2012-2019
* Extended Process Engine BL with metadata access methods
* Methods for saving datatypes
* Workunit creation and job execution
```

---

## Section 4: Enhance "How it works" Section

**Location:** Find the existing "==== '''How it works''' ====" section

**Find this (at the end of the section):**
```
360° Process Engine is also equipped with a queue manager that monitors deadlines and activities in order to trigger new activities in the process.
```

**Add this after it:**
```
==== Recent Improvements ====
* '''Time Tracking''': Enhanced active/passive time calculations with automatic nightly synchronization and validation
* '''Deadline Management''': Automatic recalculation of deadlines for progress plans in passive state
* '''Collaboration''': Distribution groups enable better workload distribution across teams (Pilot)
* '''Development''': Extended Business Logic layer with additional methods for metadata and data type handling
```

---

## Section 5: Update "What's new" Section - Add Version 6.7

**Location:** At the very top of the "==== What's new in this version====" section, BEFORE "'''Version 5.4'''"

**Add this:**
```
'''Version 6.7 (December 2025) - Pilot''':<BR>
* Distribution groups for static Progress Plans - Distribution groups feature (known from workflows) expanded to Progress Plans
* Pick/unpick functionality for progress plans, phases, and activities from Tasks web part
* Distribution to any member of the group (for Administrator/Registrar roles)
* Requires setting: workflow.enabledistributiongroups and feature toggle ProgressPlanDistributionGroups
Read more: [[6.7_release_information#Distribution_groups_for_static_Progress_Plans_(Pilot)]]

```

---

## Section 6: Update "What's new" Section - Add Version 5.17

**Location:** After Version 6.7, BEFORE "'''Version 5.4'''"

**Add this:**
```
'''Version 5.17''':<BR>
* Improved active and Passive time calculation on progress plans and phases
* Both active and passive time (days) calculated each night
* Active/Passive time on progress plan synchronized with phases
* New validation prevents setting active/passive time prior to completion of previous phase
* Recalculation triggered when changing between active and passive states
Read more: [[5.17_release_information#Process_Engine:_Improved_active_and_Passive_time_calculation]]

```

---

## Section 7: Update "What's new" Section - Add Version 5.14

**Location:** After Version 5.17, BEFORE "'''Version 5.4'''"

**Add this:**
```
'''Version 5.14''':<BR>
* Visual Studio compatibility: Process Engine supports Visual Studio up until Visual Studio 2019 for workunit creations
* Visual Studio 2019 onwards versions are unsupported
Read more: [[5.14_release_information#Process_Engine_support]]

```

---

## Section 8: Update "What's new" Section - Add Version 5.13

**Location:** After Version 5.14, BEFORE "'''Version 5.4'''"

**Add this:**
```
'''Version 5.13''':<BR>
* Deadline calculation when progress plan is in passive state - Automatic recalculation every hour
* If passive for more than 24 hours, dates extended by a day
* Ensures correct display of due dates and remaining days when progress plan is in passive state
Read more: [[5.13_release_information]]

```

---

## Section 9: Update "What's new" Section - Enhance Version 5.4

**Location:** Find the existing "'''Version 5.4'''" section

**Find this:**
```
'''Version 5.4'''<BR>
To make it easier to develop using Process engine, additional functionality has been moved into standard 360°. For details, see [[5.4 release information]].
```

**Replace with:**
```
'''Version 5.4''':<BR>
To make it easier to develop using Process engine, additional functionality has been moved into standard 360°. For details, see [[5.4 release information]].
* Method calls in Process Engine BL to access individual metadata
* Namespace extended with additional meta properties
* Methods for saving datatypes now available
* Foundation for future enhancements including "Handler" support for higher level business logic
```

---

## Section 10: Add Configuration & Requirements Section

**Location:** Add this NEW section right after "'''Version 5.4'''" and BEFORE "=== Commercial aspects ==="

**Add this:**
```
=== Configuration & Requirements ===
==== Visual Studio Support ====
* Process Engine supports Visual Studio 2012-2019 for workunit development
* Visual Studio 2019 onwards versions are unsupported for workunit creations

==== Feature Toggles & Settings ====
* '''ProgressPlanDistributionGroups''' - Enable distribution groups for static Progress Plans (Pilot in 6.7)
* '''workflow.enabledistributiongroups''' - Required setting for distribution groups functionality

==== Technical Requirements ====
* Visual Studio Tools for 360 - Meta Administrator
* Microsoft Visual Studio 2012 or newer (up to 2019 for workunits)
```

---

## Section 11: Update Value Proposition Section

**Location:** In the right column, find "=== Value proposition / Selling points ==="

**Find this:**
```
=== Value proposition / Selling points ===
* <Summarize why a consumer should buy this module/feature. This info can be added by "Sales"?>
```

**Replace with:**
```
=== Value proposition / Selling points ===
* Design tailored processes without investing in programming or complex configurations
* Cut down on manual work associated with designing and executing work processes
* Support for both simple sequential and complex dynamic processes
* Enhanced time tracking with automatic active/passive time calculations
* Improved deadline management with automatic recalculation
* Distribution groups for better workload distribution and collaboration (Pilot)
* Queue manager for automatic activity triggering based on deadlines
* Stop/start clock functionality for case progress tracking
* Integration with Visual Studio for custom development
```

---

## Section 12: Add Known Limitations Section

**Location:** At the bottom of the right column, after "=== Training material ===" and before the closing </div> tag

**Add this:**
```
=== Known Limitations ===
* Visual Studio 2019 onwards versions are unsupported for workunit creations
* Distribution groups: Designer components for Visual Studio do not support distribution groups
* Distribution groups: Progress plans attached to Projects cannot be assigned to distribution groups (phases and tasks work fine)
* Distribution groups: For dynamic progress plans with decision points, new phases will be assigned to executing user's department
* Active/passive time validation: Some progress plans created prior to 5.17 may not have required data for validation
```

---

## Quick Reference: Update Order

1. ✅ Section 1: Update Key Info (add version and VS notes)
2. ✅ Section 2: Add Recent Enhancements section
3. ✅ Section 3: Add Key Features section
4. ✅ Section 4: Enhance "How it works" with Recent Improvements
5. ✅ Section 5: Add Version 6.7 to "What's new"
6. ✅ Section 6: Add Version 5.17 to "What's new"
7. ✅ Section 7: Add Version 5.14 to "What's new"
8. ✅ Section 8: Add Version 5.13 to "What's new"
9. ✅ Section 9: Enhance Version 5.4 entry
10. ✅ Section 10: Add Configuration & Requirements section
11. ✅ Section 11: Update Value Proposition
12. ✅ Section 12: Add Known Limitations section

---

## Notes

- All sections are ready to copy-paste directly
- The wikitext formatting is preserved
- Links to release notes are included
- Each section can be updated independently
- The "What's new" section title should be changed from "What's new in this version" to "What's new in which version" to match the pattern used in other module pages















