# WF to bpmn.io Migration Analysis – Client Actions Focus

## Executive Summary

This document analyses how to convert the Visual Studio Workflow Designer plugins (client actions) to bpmn.io equivalents. The migration involves moving from a .NET/WPF-based designer with WF runtime to a JavaScript-based BPMN 2.0 designer with a new execution model.

---

## 1. Current Architecture (Windows Workflow Foundation)

### 1.1 Client Actions Overview

| Activity | Purpose | Key Properties |
|----------|---------|----------------|
| **ClientAction** | Generic client action from code table | ClientActionId, TemplateOrGroupId |
| **EditFile** | Open document for editing (e.g. Word) | GetDocById, GetDocByWorkUnit, GetDocByCategory, GetDocByProcessMark, etc. |
| **OpenUrl** | Open custom URL in UI | UrlWorkUnit, UrlManually, CloseActivityWhenClicked |
| **NewDocumentDialog** | Simplified new document dialog (eBy) | Template, archive, category, recipients, dialog options |
| **NewDocumentWizard** | Full document wizard | Template, archive, access, recipients, etc. |
| **WfWizard** | Workflow wizard | WorkflowType, GetDocByCategory, GetDocByWorkUnit |

### 1.2 Current Component Structure

```
┌─────────────────────────────────────────────────────────────────────────┐
│  VISUAL STUDIO WORKFLOW DESIGNER                                        │
├─────────────────────────────────────────────────────────────────────────┤
│  Registrator.cs          → Registers activities in IVsToolbox           │
│  RegisterMetadata.cs     → Activity ↔ Designer mapping, property editors│
│  PEToolkit.nuspec        → NuGet package for VS extension               │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  DESIGNER LAYER (XAML + C#)                                              │
├─────────────────────────────────────────────────────────────────────────┤
│  *Designer.xaml          → ActivityDesigner UI (icon, WorkflowItemPresenter)│
│  *Designer.xaml.cs       → Code-behind (minimal)                         │
│  PropertyEditor/*        → Custom pickers (code tables, work units)      │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  RUNTIME LAYER (C#)                                                      │
├─────────────────────────────────────────────────────────────────────────┤
│  PhaseChildBase          → Base: Description, ActivityCategoryId, etc.   │
│  PhaseChildBaseWaitTaskContainer → Adds RelatedWaitTask (nested activity)│
│  ClientAction, EditFile, etc. → ProcessResultData() → MetaStatement → DB │
└─────────────────────────────────────────────────────────────────────────┘
```

### 1.3 Key Characteristics

- **Property editing**: Property grid with custom editors (e.g. `SingleCodeTableClientActionPropertyEditor`, `SingleWorkUnitPropertyEditor`) that open dialogs and call 360 APIs for code tables, templates, work units.
- **Nesting**: `ClientAction` has `RelatedWaitTask` (WorkflowItemPresenter) – optional child activity.
- **Persistence**: `ProcessResultData()` writes to `MetaStatement` → database inserts. Activity type is stored as `EnumCodeTableActivitytype.Clientaction_18`; process data as key-value pairs.
- **Platform**: .NET Framework 4.8, WPF, System.Activities.Presentation.

---

## 2. bpmn.io Architecture

### 2.1 Extension Model

| Concept | bpmn.io Approach |
|---------|------------------|
| **Custom elements** | Use standard BPMN elements (e.g. Service Task) with custom `type` or `taskType` |
| **Custom data** | `extensionElements` with custom namespace URI (e.g. `http://si.biz/360`) |
| **Visual rendering** | Custom renderer (e.g. different icon/label per task type) |
| **Properties panel** | Properties provider module – groups and inputs for selected element |
| **Palette** | Custom palette provider – adds entries to toolbox |

### 2.2 bpmn.io Stack

- **bpmn-js**: Core modeler
- **bpmn-js-properties-panel**: Properties panel (Camunda-oriented)
- **Custom modules**: Model extension, custom renderer, properties provider, palette provider
- **Tech**: JavaScript/TypeScript, ES modules

### 2.3 BPMN 2.0 Mapping Options

| Option | Pros | Cons |
|--------|------|------|
| **A: Service Task + custom type** | Standard BPMN, portable | Limited to single task shape |
| **B: Custom task (model extension)** | Distinct shapes, full control | Non-standard, requires moddle extension |
| **C: Call Activity** | Reusable subprocess | Different semantics |

**Recommendation**: Option A for initial migration – use Service Tasks with `taskType` (e.g. `360:ClientAction`, `360:EditFile`) and store all 360-specific data in `extensionElements`.

---

## 3. Gap Analysis

### 3.1 Design-Time Gaps

| WF Capability | bpmn.io Equivalent | Notes |
|---------------|--------------------|-------|
| ActivityDesigner (XAML) | Custom renderer | Replace with SVG/HTML renderer |
| Property grid | Properties panel provider | Custom groups and inputs |
| Custom property editors (pickers) | Async properties panel | Need API for code tables, work units, templates |
| WorkflowItemPresenter (nested activity) | BPMN subprocess or data association | WaitTask link – different model |
| Toolbox registration | Palette provider | Add custom entries |
| DesignerAttribute mapping | Moddle extension + custom type | Map activity type → BPMN element |

### 3.2 Runtime Gaps

| WF Capability | bpmn.io / New Runtime | Notes |
|---------------|------------------------|-------|
| NativeActivity.Execute() | BPMN engine or custom executor | No built-in WF runtime |
| ProcessResultData → MetaStatement | Execution engine reads BPMN + extensionElements | New execution layer |
| InArgument binding | BPMN data flow / expressions | Different expression model |
| Phase/PhaseChild hierarchy | BPMN subprocess or custom | Structural difference |

### 3.3 Property Editor Gaps (Client Actions)

| Property Type | WF Editor | bpmn.io Approach |
|---------------|-----------|------------------|
| ClientActionId (code table) | SingleCodeTableClientActionPropertyEditor | Async dropdown + API |
| TemplateOrGroupId | SingleTemplateGroupPropertyEditor | Async dropdown + API |
| WorkUnit (GetDocByWorkUnit, UrlWorkUnit) | SingleWorkUnitPropertyEditor | Async dropdown + API |
| Document category, archive | SingleCodeTableDocumentCategoryPropertyEditor | Async dropdown + API |
| Access group | SingleAccessGroupPropertyEditor | Async dropdown + API |
| Activity category | SingleCodeTableActivityCategoryPropertyEditor | Async dropdown + API |

**Reference**: [bpmn-io/properties-panel-async-example](https://github.com/bpmn-io/properties-panel-async-example) for async data in properties panel.

---

## 4. Migration Strategy – Client Actions

### 4.1 Phased Approach

```
Phase 1: Foundation     → Model extension, basic Service Task, palette
Phase 2: Properties     → Properties panel for each client action type
Phase 3: Pickers/API    → Async property editors (code tables, work units)
Phase 4: Runtime       → Execution engine / conversion layer
```

### 4.2 Data Model Design

**BPMN extension namespace**: `http://si.biz/360` (or similar)

**Extension structure for Client Action** (example – EditFile):

```xml
<serviceTask id="Task_1" name="Edit a file" taskType="360:EditFile">
  <extensionElements>
    <si360:EditFileProperties>
      <si360:getDocById>...</si360:getDocById>
      <si360:getDocByWorkUnit>...</si360:getDocByWorkUnit>
      <si360:getDocByCategory>...</si360:getDocByCategory>
      ...
    </si360:EditFileProperties>
    <si360:PhaseChild>
      <si360:description>...</si360:description>
      <si360:activityCategoryId>...</si360:activityCategoryId>
      <si360:relatedWaitTaskId>...</si360:relatedWaitTaskId>
    </si360:PhaseChild>
  </extensionElements>
</serviceTask>
```

### 4.3 Component Mapping

| WF Component | bpmn.io Component |
|--------------|-------------------|
| ClientAction.cs | Moddle descriptor + Service Task type `360:ClientAction` |
| ClientActionDesigner.xaml | Custom renderer (optional icon) |
| RegisterMetadata (DesignerAttribute) | Moddle extension + custom type registration |
| SingleCodeTableClientActionPropertyEditor | Properties panel group + async select |
| ProcessResultData logic | Execution engine (reads BPMN + extensionElements) |

---

## 5. Work Plan for Client Actions

### Phase 1: Foundation (2–3 weeks)

1. **Create bpmn-js project**
   - Set up bpmn-js + properties panel
   - Add TypeScript/ES build

2. **Model extension**
   - Define `si360` namespace and descriptors for all 6 client action types
   - Map PhaseChildBase properties (Description, ActivityCategoryId, etc.)
   - Map each client action’s specific properties

3. **Custom task types**
   - Register `360:ClientAction`, `360:EditFile`, `360:OpenUrl`, etc.
   - Use Service Task as base with custom `taskType`

4. **Palette provider**
   - Add "360 - Client actions" group
   - Add 6 entries for each client action type
   - Use existing icons (Activity_ClientAction.png) or equivalents

### Phase 2: Properties Panel (2–3 weeks)

1. **Properties provider**
   - Create provider for `360:*` task types
   - Add groups: "Trigger activity", "Open document", "Window", etc.

2. **Basic inputs**
   - Text inputs for simple properties (UrlManually, ProcessMark, etc.)
   - Number inputs where applicable
   - Boolean toggles (CloseActivityWhenClicked, etc.)

3. **Property grouping**
   - Mirror WF categories (Open document, Trigger activity, etc.)

### Phase 3: Async Pickers (3–4 weeks)

1. **API layer**
   - Define REST/API for client actions, templates, work units, etc.
   - Or reuse existing 360 APIs if available

2. **Async select components**
   - Implement async dropdown for code tables
   - Implement async dropdown for work units
   - Implement async dropdown for templates/groups

3. **Property editors**
   - ClientActionId → SingleCodeTableClientActionPropertyEditor equivalent
   - GetDocByWorkUnit, UrlWorkUnit → SingleWorkUnitPropertyEditor equivalent
   - GetDocByCategory, NewDocumentCategory → Category picker equivalent
   - etc.

4. **Validation**
   - Port validation rules (e.g. OpenUrl: UrlManually or UrlWorkUnit required)

### Phase 4: Runtime (separate track)

1. **Execution model**
   - Decide: BPMN engine (Camunda, Zeebe, etc.) or custom executor
   - Or: Convert BPMN → existing WF at runtime (translation layer)

2. **Extension to MetaStatement**
   - Map BPMN extensionElements → ProcessResultData / MetaStatement
   - Preserve ActivityType, ProcessMark, process data key-value pairs

3. **RelatedWaitTask**
   - Map to BPMN data flow or reference to WaitTask element

---

## 6. Risks and Decisions

### 6.1 Risks

| Risk | Mitigation |
|------|------------|
| Property editors depend on 360 APIs | Ensure APIs exist or build adapter; use properties-panel-async-example pattern |
| RelatedWaitTask nesting | BPMN has no direct equivalent; use data reference or separate element |
| Large number of properties (NewDocumentWizard) | Consider collapsible groups, tabs, or simplified UI |
| Runtime execution | Separate project; may need WF bridge during transition |

### 6.2 Decisions Needed

1. **Runtime strategy**: New BPMN engine or translate BPMN → WF for existing engine?
2. **API availability**: Are code table, work unit, template APIs available for the properties panel?
3. **Hosting**: Web app or Electron wrapper for desktop?
4. **Coexistence**: Run WF and bpmn.io in parallel during migration?

---

## 7. References

- [bpmn-js-example-custom-elements](https://github.com/bpmn-io/bpmn-js-example-custom-elements)
- [bpmn-js-example-model-extension](https://github.com/bpmn-io/bpmn-js-example-model-extension)
- [bpmn-js-examples/custom-elements](https://github.com/bpmn-io/bpmn-js-examples/tree/main/custom-elements)
- [bpmn-js-properties-panel](https://github.com/bpmn-io/bpmn-js-properties-panel)
- [properties-panel-async-example](https://github.com/bpmn-io/properties-panel-async-example)
- [Camunda: Adding Custom Elements to BPMN Properties Panel](https://camunda.com/blog/2017/04/adding-custom-elements-to-bpmn-properties-panel/)
