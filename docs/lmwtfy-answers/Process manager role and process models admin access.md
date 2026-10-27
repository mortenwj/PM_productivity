# Process manager role and process models admin access

**Process manager** (system role id **28**) is treated like **administrator** or **registrar** for the **process model configuration** APIs under `SI.Client.Api.Process`: those endpoints allow access if the user is an admin, a registrar, **or** a process manager. You do **not** need registrar or full system administrator for that guard. Whether **every** WebAdmin menu tile or SPA route is visible with **only** process manager was not fully traced; server APIs for process models are aligned with **yes** for that layer.

---

## Original Question

> What does the role process manager do? Can I get access to the admin page of process models with this role but without anything else?

## Context

Colleague question about Public 360° **system roles**, **process platform** administration, and least-privilege access (process models admin without broader admin roles). Research used read-only **`gh`** / GitHub API against **`te-industry-public360/core-bl`**. **360 Online admin help (Ratatoskr)** returned no title hit for “Process manager” on `admin-en` in this session; **wiki** was not read. Evidence ledger was approved for persistence in chat.

## Findings

### What the Process manager role does (from code)

- **Stable role id:** The product uses **`EnumSysrole.ProcessManager_28`** (numeric **28**) for this role. It appears in process-platform and template code paths (for example next to `UserSessionExtensions` / `UserManager` patterns in the same repository; the clearest single read is the guard below).

- **Process model configuration APIs:** **`ProcessModelUtility.ValidateAccessAdminOrRegistrar()`** allows access if **`UserIsolator.IsUserAdmin()`** OR **`IsUserRegistrar()`** OR the current **`GetUserRoleId()`** equals **`ProcessManager_28`**. If none of those hold, it throws **`BizInfoException`** with a localized “no permission” message.  
  https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-process-platform-build/SI.Client.Api.Process/ProcessModelConfig/ProcessModelUtility.cs

- **Where that guard is used:** The same **`ValidateAccessAdminOrRegistrar()`** call appears on the process-platform **Client.Api** surface, including (non-exhaustive list from repository search) **ProcessModelConfigApi**, **ProcessModelConfigApiTreeView**, **StageConfigApi**, **StageTemplateConfigApiTreeView**, **StageProcessConfigApi**, and **MilestoneConfigApi**. That is the shared access pattern for those configuration operations.

- **Tests:** Unit tests list role **28** as a **valid** role for some process-model-config operations (for example draft PMC delete alongside admin and registrar roles), which matches the intent that process manager is a first-class elevated role for that area, not a mistake.  
  https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessPlatform.UnitTest/ClientApi/ProcessModelConfig/ProcessModelConfigApiTest.cs#L2285-L2320

- **Templates (narrower, separate surface):** **`TemplateMetaHandler`** contains a **`ValidateUserIsAdmin()`** path that **returns without** calling **`SecurityAdmin.VerifyAdminRole()`** when the user’s role id is **Process manager**. That is an extra “admin-like” escape for **templates**, not a guarantee that every admin-only feature in the product behaves the same way.  
  https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/Template/TemplateMetaHandler.cs

- **Work unit registry (documented hook only):** **`IProcessManagerAccessChecker`** describes an optional pattern to tie **work unit registry** write access to process managers. A bounded search in this run surfaced the **interface** only; do not over-claim shipped behaviour beyond what your deployment wires in.

### Can you use process models “admin” with only this role?

- **For the APIs guarded by `ValidateAccessAdminOrRegistrar`:** **Yes.** A user who has **only** process manager (role **28**) and **does not** have admin or registrar flags used in that method still passes, because **`isUserProcessManager`** is an explicit **OR** condition.

- **For “the admin page” as full WebAdmin navigation:** **`MenuManagerAdmin.GetWebAdminToolsMenu`** (read in a bounded slice) builds the familiar **MetaAdmin / CodeTable / …** tool entries for **Technical** and **System** administrators. Process manager is recognized separately (**`HasProcManagerButNotAdmin`**) but is **not** dropped into that same module list in the lines reviewed. So if a colleague means “I see the same left nav as a system admin,” that may still depend on **SPA routing**, **feature flags**, or other entry points not exhaustively mapped in this answer. If they mean “the backend lets me load and save process model configuration,” the guard above supports **yes** for that API family.

### Confidence

**Medium** for the overall answer: behaviour is **verified in product source** only. Admin help did not yield a matching topic title in the attempted **Ratatoskr** search on **admin-en**; no wiki page was opened in this run.

## Follow-up (English)

**Paraphrased question:** Is it correct that **any** user who is either a **regular administrator**, a **registrar (archivist)**, or a **process manager** can configure processes? And if someone is **only** a process manager **plus** a typical **case handler** profile, are **all** main WebAdmin menu choices hidden, or do they only see something like **“process administration”**?

### Who can configure process models (roles)

- **Server (core-bl):** `ProcessModelUtility.ValidateAccessAdminOrRegistrar()` allows **`UserIsolator.IsUserAdmin()`** OR **`IsUserRegistrar()`** OR role id **28 (Process manager)**. That is the shared gate for the process-platform configuration APIs described in the main findings.  
  https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-process-platform-build/SI.Client.Api.Process/ProcessModelConfig/ProcessModelUtility.cs

- **Process models SPA (React):** `ProcessModel.tsx` sets `showProcessModels` only when **`_blctxroleid`** equals **`Administrator_0` (0)**, **`Registrar_1` (1)**, or **`ProcessManager_28` (28)**. The localized access error states that only **admins, process managers, and registrars** may view the page.  
  https://github.com/te-industry-public360/core-360-react-views/blob/master/apps/process-views/src/AdminConfigurations/ProcessModel/ProcessModel.tsx

- **Precision on “regular admin”:** The **explicit numeric check** on the process models page uses **`Administrator_0` (role 0)** and **`Registrar_1`**, not **`Useradministrator_8`**. Whether **`IsUserAdmin()`** on the server grants the same people role **8** depends on how that delegate is wired in your environment; do **not** assume “user administrator” and “administrator (0)” are interchangeable for this **SPA** gate without verifying.

### WebAdmin welcome tiles when the user is only a process manager (plus typical case-handler roles)

- **`WelcomePage.tsx` (`webadmin-core-views`)** builds a list of module tiles with per-tile `show` flags. **Process manager alone** does **not** enable templates, archives, classification, user-admin tiles, and so on; those require **administrator or registrar** or **elevated** admin (technical / system / all-access) as coded. The only tile keyed directly on **`isProcessAdmin`** is **Business Rules**, and it is further gated by **`BusinessRuleEngineEnabled`**.  
  https://github.com/te-industry-public360/core-360-react-views/blob/master/apps/webadmin-core-views/src/WelcomePage/WelcomePage.tsx

- There is **no** welcome tile in that file named “process administration” or “process models.” Process model administration is reached via **separate routes** in **`process-views`**, for example **`Admin/ProcessManagement/ProcessModels`**.  
  https://github.com/te-industry-public360/core-360-react-views/blob/master/apps/process-views/src/Routes/FullPageRoutes.tsx

- **Practical reading:** On the **WebAdmin welcome** screen, a user with **only** process manager (and ordinary case-handler roles) will see **none** of the classic admin tiles, except possibly **Business Rules** when the feature flag is on. That is **not** the same as “only Process administration remains,” because that label is not how this welcome page is structured.

### Multi-role caveat (active context role)

- **`WelcomePage`** reads **all** role ids from a **comma-separated** session profile. **`ProcessModel.tsx`** uses **`useSessionPropertyInt('_blctxroleid')`**, i.e. a **single** integer role id for the gate. If the **active context role** is not **0**, **1**, or **28**, the user may see the access-denied path on the process models page **even if** process manager (**28**) is present elsewhere on the profile. Validate in your environment if mixed roles are common.

### Follow-up confidence

**Medium:** verified in **`core-bl`** and **`core-360-react-views`** only; admin help not re-read for this addendum.

## Documentation assessment

- **Status:** missing_documentation
- **Explanation:** Official admin or end-user help was not verified with a full topic read in this run. Role behaviour is grounded in **core-bl** only.
- **Suggested documentation changes:**
  - Add or extend a **360 Online Administrator** topic that names **Process manager (role 28)** and states it may use **process model / stage / milestone configuration** APIs and UI surfaces that call **`ValidateAccessAdminOrRegistrar`**, without being **System administrator** or **Registrar**.
  - Clarify how that role relates to **WebAdmin** navigation versus **process-views** admin configuration, and point admins to the correct entry URL if it differs from generic “WebAdmin tools.”
  - Document the difference between **comma-separated role profiles** (welcome tiles) and **`_blctxroleid`** (single active role) for process-model admin pages, including guidance for users with **process manager plus case handler**.

## Risks and Limitations

- Line anchors refer to **`master`** on GitHub at research time; branches can drift.
- **Ratatoskr** title search for “Process manager” on **admin-en** returned no hits; deeper **`search_content`** or **Norwegian admin** sections were not fully mined in this run.
- Other product areas may still call **`SecurityAdmin.VerifyAdminRole()`** or **`IsUserAdmin()`** without an exception for process manager; this answer focuses on the **process model configuration** API guard and closely related code.
- **`_blctxroleid`** semantics for multi-role users were not traced into **`@si/fib-platform`** in this run; the caveat above is a **code-shape** warning, not a full session-design proof.

## References

- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-process-platform-build/SI.Client.Api.Process/ProcessModelConfig/ProcessModelUtility.cs
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessPlatform.UnitTest/ClientApi/ProcessModelConfig/ProcessModelConfigApiTest.cs#L2285-L2320
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/Template/TemplateMetaHandler.cs
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/_Compatibility/MenuManagers/MenuManagerAdmin.cs#L26-L120
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core.Contracts/User/IProcessManagerAccessChecker.cs
- https://github.com/te-industry-public360/core-360-react-views/blob/master/apps/process-views/src/AdminConfigurations/ProcessModel/ProcessModel.tsx
- https://github.com/te-industry-public360/core-360-react-views/blob/master/apps/webadmin-core-views/src/WelcomePage/WelcomePage.tsx
- https://github.com/te-industry-public360/core-360-react-views/blob/master/apps/process-views/src/Routes/FullPageRoutes.tsx
