# Workflow Designer Plugin Components – te-industry-public360/core-bl

## Repository Structure

| Location | Purpose |
|----------|---------|
| **Repo** | `te-industry-public360/core-bl` |
| **Project** | `SI.Biz.Core.ProcessEngine.Activities.Design` |
| **Path** | `Source/si-bl-process-platform-build/SI.Biz.Core.ProcessEngine.Activities.Design/` |
| **Delivery** | `PEToolkit.nuspec` → NuGet package (Process Engine Toolkit) |

---

## Visual Studio Workflow Designer Integration

- **Framework:** `System.Activities.Presentation`, `System.Activities`
- **Targets:** `net48` (VS), `net10.0-windows` (UiPath.Workflow)
- **VS Integration:** `IVsToolbox`, `VSSDK.Shell.10` – `Registrator.cs` registers activities as toolbox items

---

## Activity Designer Components (Design folder)

| Designer | Activity (runtime) |
|----------|----------|
| `BypassAccessControlDesigner` | BypassAccessControl |
| `CallWorkUnitDesigner` | CallWorkUnitAction |
| `CallWorkUnitFunc` (via InvokeWorkUnitParameterDesigner) | CallWorkUnitFunc |
| `CheckInProcessDesigner` | — |
| `ClientActionDesigner` | ClientAction (base) |
| `ClosePhaseDesigner` | — |
| `ContextBinderDesigner` | ContextBinder |
| `CreateGenericActivityDesigner` | CreateActivityBase |
| `CreateWaitTaskDesigner` | CreateWaitTask |
| `DecisionDesigner` | Decision |
| `EditFileDesigner` | EditFile |
| `EnsureDesigner` | Ensure |
| `IgnoreDesigner` | Ignore |
| `InvokeWorkUnitDesigner` | InvokeWorkUnit |
| `InvokeWorkUnitParameterDesigner` | InvokeWorkUnitParameter |
| `NewDocumentDialogDesigner` | NewDocumentDialog |
| `NewDocumentWizardDesigner` | NewDocumentWizard |
| `OpenUrlDesigner` | OpenUrl |
| `OutboundDocumentDesigner` | — |
| `PhaseContainerDesigner` | PhaseContainer |
| `PhaseDesigner` | Phase |
| `SetCaseStatusDesigner` | — |
| `SetDecisionForPhaseDesigner` | — |
| `SetProcessResponsibleDesigner` | — |
| `SetWaitTaskConnectionDesigner` | — |
| `TaskDesigner` | Task |
| `TraceLineDesigner` | TraceLine |
| `WaitForDecisionDesigner` | WaitForDecision |
| `WaitForExternalResponseDesigner` | WaitForExternalResponse |
| `WaitForExternalTimeoutDesigner` | WaitForExternalTimeout |
| `WaitForPhaseClosedDesigner` | WaitForPhaseClosed |
| `WaitTaskDesigner` | WaitTask |
| `WfWizardDesigner` | WfWizard |
| `WorkUnitServerActionDesigner` | WorkUnitServerAction |

---

## Supporting Components

| Component | Path | Purpose |
|-----------|------|---------|
| **Registrator** | `Registrator.cs` | Registers activities with VS toolbox (IVsToolbox) |
| **RegisterMetadata** | `Design/RegisterMetadata.cs` | Registers ActivityDesigner ↔ Activity mappings |
| **Pickers** | `Design/Pickers/` | BaseEntityPicker, AccessCodeAndLawPicker |
| **PropertyEditor** | `Design/PropertyEditor/` | Property editor UI |
| **Images** | `Design/Images/` | Activity icons (Activity_*.png) |
| **BusinessLogicCallSite** | `Design/BusinessLogicCallSite.cs` | Shared logic for .NET 10 / UiPath |

---

## Progress Plan Activities (Runtime)

**Path:** `SI.Biz.Core.ProcessEngine.Activities/ProgressPlan/`

| File | Purpose |
|------|---------|
| `Decision.cs` | Decision activity |
| `Phase.cs` | Phase container |
| `PhaseChildBase.cs` | Base for phase children |
| `PhaseContainer.cs` | Phase container |
| `Task.cs` | Task activity |
| `WaitTask.cs` | Wait task |
| `WaitForDecision.cs` | Wait for decision |
| `WaitForPhaseClosed.cs` | Wait for phase closed |
| `WorkUnitServerAction.cs` | Server action |
| **ClientActions/** | EditFile, NewDocumentDialog, NewDocumentWizard, OpenUrl, WfWizard |

---

## URL Reference

- **Design folder:** https://github.com/te-industry-public360/core-bl/tree/30b58a466b329f9e08aed800c52853092c4b758b/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessEngine.Activities.Design/Design
- **Progress Plan:** https://github.com/te-industry-public360/core-bl/tree/30b58a466b329f9e08aed800c52853092c4b758b/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessEngine.Activities/ProgressPlan
