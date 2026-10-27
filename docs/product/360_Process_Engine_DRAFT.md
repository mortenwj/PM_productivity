# DRAFT: Updated 360° Process Engine Module Page

## Complete Updated Wiki Content

```wikitext
{| cellpadding="0" cellspacing="0" width="100%"
|-
| style="vertical-align:top" |
<div style="margin: 0 10px 0 0; border: 2px solid #0E76B7; padding: 0em 1em 1em 1em; background-color: #FFFDCA;">
==Key info==
Product number: '''125925'''
* Applies to version(s): '''360° version 5.x or 4.1 SP7 feature pack 3 or newer''' (Note: Many recent features require version 5.13+ or 5.17+)
* Availability: '''Available in all countries'''
* Other requirements: '''Visual Studio Tools for 360 - Meta Administrator''' and '''Microsoft Visual Studio 2012 or newer''' (Note: Visual Studio 2019 onwards versions are unsupported for workunit creations)
* Page last updated: {{REVISIONYEAR}}-{{REVISIONMONTH}}-{{REVISIONDAY}}

</div> 
<div style="margin: 0 10px 0 0; border: 2px solid #0E76B7; padding: 0em 1em 1em 1em; background-color: #FFFFFF;">

== Product information==
{{PSNote}}

'''Complete digital support for your organization'''

''360° Process Engine'' makes it possible to design work process support in 360° using predefined and automated components. In this way your organization can get tailored processes without investing in programming or complex configurations. 

360° Process Engine builds on 360°'s progress plans to further automate your organization's work processes. The module lets you cut down on the manual work associated with designing and executing work processes, while adding new standard components to enhance support for complex scenarios.

=== Recent Enhancements (2021-2025) ===
The Process Engine module has received significant updates to improve process management, time tracking, and collaboration:

* '''Distribution Groups for Progress Plans''': Expand workflow distribution group functionality to progress plans, enabling better workload distribution and collaboration (Pilot in 6.7)
* '''Improved Time Calculation''': Enhanced active/passive time tracking with automatic nightly calculations and synchronization between progress plans and phases
* '''Deadline Management''': Automatic deadline recalculation for progress plans in passive state, ensuring accurate due dates
* '''Enhanced Development Tools''': Extended Process Engine BL with additional methods for metadata access and data type handling
* '''Visual Studio Compatibility''': Support for Visual Studio up to 2019 for workunit development

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

==== '''How it works''' ====
The ''360° Process Engine'' is a toolkit for designing custom processes in 360°.

Basically, the 360° Process Engine lets you set up simple sequential processes in addition to dynamic ones that changes based on what decisions you make or what status is set. The module can also handle processes that hibernate until an event happens or a fixed period of time has elapsed. This makes it possible to stop/start the clock on case progress.

360° Process Engine is also equipped with a queue manager that monitors deadlines and activities in order to trigger new activities in the process.

==== Recent Improvements ====
* '''Time Tracking''': Enhanced active/passive time calculations with automatic nightly synchronization and validation
* '''Deadline Management''': Automatic recalculation of deadlines for progress plans in passive state
* '''Collaboration''': Distribution groups enable better workload distribution across teams (Pilot)
* '''Development''': Extended Business Logic layer with additional methods for metadata and data type handling

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

=== Commercial aspects ===
360° Process Engine is a part of the Process Automation concept. 

{{Price model in 360°}}

=== Product documentation ===
Below, please find documentation developed and maintained by Enablement.

==== Product sheets ====
{| class="wikitable"
|[https://help.360online.com/360productsheets/Process%20Engine/Process_Engine_DAN.pdf DAN]
|[https://help.360online.com/360productsheets/Process%20Engine/Process_Engine_ENG.pdf ENG]
|FIN
|[https://help.360online.com/360productsheets/Process%20Engine/Process_Engine_NOR.pdf NOR]
|[https://help.360online.com/360productsheets/Process%20Engine/Process_Engine_SWE.pdf SWE]
|}

=== Additional material ===
* [https://si.business360online.com/locator/DMS/Document/Details/Simplified/200018?module=Document&subtype=200018&recno=392313&VerID=356820 Sales presentation] in internal 360°
* [[Product training sessions]] 
* Hotfixes and known issues: For hotfixes on the latest release, see [[Release Information]]. All hotfixes are published on {{360° Setups and Hotfixes}}. 

| width="40%" style="vertical-align:top" |

<div style="margin: 0 10px 0 0; border: 2px solid #0E76B7; padding: 0em 1em 1em 1em; background-color: #E5F6FE;">

== Documentation from other units ==
Quality assurance relies on the individual departments owning the material.

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

=== Installation/ deployment/ technical  ===
* [https://help.360online.com/360TechnicalDocuments/Process%20Engine/How_to_create_a_360_Process_Engine_process.pdf How to create a 360 Process Engine process]
* [https://help.360online.com/360TechnicalDocuments/Process%20Engine/Process_Engine_How_it_works_and_how_to_use_it.pdf How it works and how to use Process Engine]
* [https://help.360online.com/360TechnicalDocuments/Process%20Engine/Process_Engine_Tools_whitepaper.pdf Process Engine Developer Tools Whitepaper]    
=== Service descriptions ===
Service Descriptions can be found in 360° on [https://si.business360online.com/locator/CRM/Project/Details/Simplified/1?recno=201981&module=Project&subtype=1&VerID= project 12-356]. Look under "Service Descriptions - Modules". We recommend navigating in the project via the "Treeview". 

The Service Descriptions in 360° are currently being updated.

New documents and updates will be published in English.

=== Training material ===
See [[Process Engine|'''this Wiki page''']] (maintained by CIE) containing Learning material, Common Way of Work and How-to's.  

=== Known Limitations ===
* Visual Studio 2019 onwards versions are unsupported for workunit creations
* Distribution groups: Designer components for Visual Studio do not support distribution groups
* Distribution groups: Progress plans attached to Projects cannot be assigned to distribution groups (phases and tasks work fine)
* Distribution groups: For dynamic progress plans with decision points, new phases will be assigned to executing user's department
* Active/passive time validation: Some progress plans created prior to 5.17 may not have required data for validation

</div>

__NOTOC__
[[Category: Product information]]
|}
```

## Summary of Changes Made

### 1. **Updated Key Info Section**
   - Added note about version requirements for recent features
   - Added important note about Visual Studio 2019+ unsupported for workunits

### 2. **New "Recent Enhancements" Section**
   - Highlights major improvements from 2021-2025
   - Organized by feature category for easy scanning

### 3. **New "Key Features" Section**
   - Organized into logical categories:
     - Process Design
     - Process Execution
     - Development & Integration

### 4. **Enhanced "How it works" Section**
   - Added "Recent Improvements" subsection
   - Highlights time tracking, deadline management, collaboration, and development improvements

### 5. **Updated "What's new" Section**
   - Added Version 6.7 (Distribution groups - Pilot)
   - Added Version 5.17 (Improved time calculation)
   - Added Version 5.14 (Visual Studio compatibility)
   - Added Version 5.13 (Deadline calculation in passive state)
   - Enhanced Version 5.4 entry with more details

### 6. **New "Configuration & Requirements" Section**
   - Visual Studio Support information
   - Feature Toggles & Settings reference
   - Technical Requirements summary

### 7. **Updated "Value Proposition" Section**
   - Filled in the previously empty section
   - Added 9 comprehensive selling points

### 8. **New "Known Limitations" Section**
   - Visual Studio compatibility limitations
   - Distribution groups constraints
   - Active/passive time validation notes

### 9. **Improved Organization**
   - Better structure and flow
   - More comprehensive coverage of recent capabilities
   - Clearer separation between features and documentation

This draft is ready for review. It can be copied directly into the wiki page when approved.















