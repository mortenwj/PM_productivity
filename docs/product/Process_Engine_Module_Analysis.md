# Process Engine Module Page - Analysis and Update Suggestions

## Current Module Page Status

The current module page is quite minimal and only includes:
- Basic product information
- "What's new" section with only Version 5.4 mentioned
- Links to documentation

## Process Engine Changes Found in Release Notes (Last 2+ Years)

### Version 6.7 (December 2025) - **MISSING FROM MODULE PAGE**
**Distribution groups for static Progress Plans (Pilot)**
- Distribution groups feature (known from workflows) expanded to Progress Plans
- Requires setting: `workflow.enabledistributiongroups` and feature toggle `ProgressPlanDistributionGroups`
- Responsible dialog expanded with "Distribution group" field
- Progress plans, phases, and activities can be picked by users in the distribution group
- Pick/unpick functionality from Tasks web part and progress plan overview
- Distribution to any member of the group (for Administrator/Registrar roles)
- Known limitations: Designer components don't support distribution groups; Dynamic progress plans have specific behavior; Progress plans attached to Projects cannot be assigned to distribution groups

### Version 5.17 (2023) - **MISSING FROM MODULE PAGE**
**Process Engine: Improved active and Passive time calculation**
- Important change: Improved calculations for active/passive time on progress plans and phases
- Both active and passive time (days) calculated each night
- Active/Passive time on progress plan now synchronized with phases
- Recalculation triggered when changing from passive to active and vice versa
- New validation: Prevents setting active/passive time prior to completion of previous phase
- New validation: Prevents setting active/passive time before previous active/passive time periods
- Note: Some progress plans created prior to 5.17 may not have required data for validation
- Users can still manipulate overlapping times in the "Edit phases" dialog if needed

### Version 5.14 (2022) - **MISSING FROM MODULE PAGE**
**Process Engine support - Visual Studio compatibility**
- For workunit creations, Process Engine supports Visual Studio version up until Visual Studio 2019
- Visual Studio 2019 onwards versions are unsupported

### Version 5.13 (2022) - **MISSING FROM MODULE PAGE**
**Process engine: deadline calculation when progress plan is in passive state**
- On progress plans and phases, deadline and warning dates automatically recalculated every hour based on how long the progress plan has been in passive state
- If passive for more than 24 hours, dates extended by a day
- Previously, recalculation was only done when progress plan changed status to active
- This fix ensures due dates and 'remaining days' display correctly when progress plan is in passive state

### Version 5.4 (2021) - **PARTIALLY DOCUMENTED**
**New functionality in process engine**
- Currently mentioned on module page but could be more detailed
- Functionality moved from Process management framework into standard 360°
- Method calls in Process Engine BL to access individual metadata
- Namespace extended with additional meta properties
- Methods for saving datatypes now available
- Future plans mentioned: Support in "Handler" for higher level business logic like "Progressplan.Setstatus" and "Process Data" functionality

## Suggested Updates to Module Page

### 1. **Update "What's new in this version" Section**

**Current state:** Only mentions Version 5.4

**Suggested additions:**

```
==== What's new in which version====
'''Version 6.7 (December 2025) - Pilot''':<BR>
* Distribution groups for static Progress Plans - Distribution groups feature (known from workflows) expanded to Progress Plans
* Pick/unpick functionality for progress plans, phases, and activities from Tasks web part
* Distribution to any member of the group (for Administrator/Registrar roles)
* Requires setting: workflow.enabledistributiongroups and feature toggle ProgressPlanDistributionGroups
Read more: [[6.7_release_information#Distribution_groups_for_static_Progress_Plans_(Pilot)]]

'''Version 5.17''':<BR>
* Improved active and Passive time calculation on progress plans and phases
* Both active and passive time (days) calculated each night
* Active/Passive time on progress plan synchronized with phases
* New validation prevents setting active/passive time prior to completion of previous phase
* Recalculation triggered when changing between active and passive states
Read more: [[5.17_release_information#Process_Engine:_Improved_active_and_Passive_time_calculation]]

'''Version 5.14''':<BR>
* Visual Studio compatibility: Process Engine supports Visual Studio up until Visual Studio 2019 for workunit creations
* Visual Studio 2019 onwards versions are unsupported
Read more: [[5.14_release_information#Process_Engine_support]]

'''Version 5.13''':<BR>
* Deadline calculation when progress plan is in passive state - Automatic recalculation every hour
* If passive for more than 24 hours, dates extended by a day
* Ensures correct display of due dates and remaining days when progress plan is in passive state
Read more: [[5.13_release_information]]

'''Version 5.4''':<BR>
To make it easier to develop using Process engine, additional functionality has been moved into standard 360°. For details, see [[5.4 release information]].
* Method calls in Process Engine BL to access individual metadata
* Namespace extended with additional meta properties
* Methods for saving datatypes now available
* Foundation for future enhancements including "Handler" support for higher level business logic
```

### 2. **Add "Recent Enhancements" Section**

Add a new section highlighting major improvements:

```
=== Recent Enhancements (2021-2025) ===
The Process Engine module has received significant updates to improve process management, time tracking, and collaboration:

* '''Distribution Groups for Progress Plans''': Expand workflow distribution group functionality to progress plans, enabling better workload distribution and collaboration (Pilot in 6.7)
* '''Improved Time Calculation''': Enhanced active/passive time tracking with automatic nightly calculations and synchronization between progress plans and phases
* '''Deadline Management''': Automatic deadline recalculation for progress plans in passive state, ensuring accurate due dates
* '''Enhanced Development Tools''': Extended Process Engine BL with additional methods for metadata access and data type handling
* '''Visual Studio Compatibility''': Support for Visual Studio up to 2019 for workunit development
```

### 3. **Add "Key Features" Section**

Add a comprehensive features section:

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

### 4. **Update "How it works" Section**

Enhance the existing section with more detail:

```
==== '''How it works''' ====
The ''360° Process Engine'' is a toolkit for designing custom processes in 360°.

Basically, the 360° Process Engine lets you set up simple sequential processes in addition to dynamic ones that changes based on what decisions you make or what status is set. The module can also handle processes that hibernate until an event happens or a fixed period of time has elapsed. This makes it possible to stop/start the clock on case progress.

360° Process Engine is also equipped with a queue manager that monitors deadlines and activities in order to trigger new activities in the process.

==== Recent Improvements ====
* '''Time Tracking''': Enhanced active/passive time calculations with automatic nightly synchronization and validation
* '''Deadline Management''': Automatic recalculation of deadlines for progress plans in passive state
* '''Collaboration''': Distribution groups enable better workload distribution across teams (Pilot)
* '''Development''': Extended Business Logic layer with additional methods for metadata and data type handling
```

### 5. **Add "Configuration & Requirements" Section**

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

### 6. **Update "Value proposition / Selling points" Section**

Currently empty - add:

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

### 7. **Add "Known Limitations" Section**

```
=== Known Limitations ===
* Visual Studio 2019 onwards versions are unsupported for workunit creations
* Distribution groups: Designer components for Visual Studio do not support distribution groups
* Distribution groups: Progress plans attached to Projects cannot be assigned to distribution groups (phases and tasks work fine)
* Distribution groups: For dynamic progress plans with decision points, new phases will be assigned to executing user's department
* Active/passive time validation: Some progress plans created prior to 5.17 may not have required data for validation
```

## Summary of Missing Content

### High Priority (Major Features):
1. ✅ Version 6.7: Distribution groups for Progress Plans (Pilot)
2. ✅ Version 5.17: Improved active/passive time calculation
3. ✅ Version 5.13: Deadline calculation in passive state

### Medium Priority (Technical Information):
4. ✅ Version 5.14: Visual Studio compatibility limitations
5. ✅ Enhanced "How it works" section with recent improvements
6. ✅ Key Features section

### Low Priority (Nice to Have):
7. ✅ Recent Enhancements summary section
8. ✅ Configuration & Requirements section
9. ✅ Value proposition content
10. ✅ Known Limitations section

## Recommended Update Order

1. Update "What's new" section with all missing versions
2. Add "Recent Enhancements" section
3. Add "Key Features" section
4. Enhance "How it works" section
5. Add "Configuration & Requirements" section
6. Update "Value proposition" section
7. Add "Known Limitations" section















