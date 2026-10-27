# StandardProcesses

WorkUnit processes that are part of the Process Platform delivery. The **StandardProcesses** folder is copied to setup during build and becomes part of the product delivery after the nightly build.

**Consultants:** See the [PAF WorkUnits README](../README.md) for a step-by-step guide on how to work with XAML and .wu files.

## WorkUnit ID Rules

### Pure GUID Only

Every WorkUnit (`.wu` file) **must** have an `id` attribute that is a **pure GUID string** in standard format:

```
XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
```

**Correct:**
```xml
id="6A1C71C0-4B93-43D5-A7F9-E616867678EB"
```

**Incorrect** (text mixed with GUID):
```xml
id="MyProcess{6A1C71C0-4B93-43D5-A7F9-E616867678EB}"
id="PE Test CreateUrl.wu[6A1C71C0-4B93-43D5-A7F9-E616867678EB]"
```

### No Duplicate GUIDs

**Duplicate GUIDs are not allowed.** Each WorkUnit must have a unique ID across the entire codebase.

When creating or updating WorkUnit IDs:

1. Use a GUID creation tool (e.g. Visual Studio **Tools → Create GUID**, or `[guid]::NewGuid()` in PowerShell).
2. Generate a **new** GUID for each WorkUnit.
3. Never reuse an existing GUID.

### Updating References

When you change a WorkUnit ID, you must update all references in:

- **XAML files** – attributes such as `WorkUnit`, `CompletedAction`, `WaitExpiredAction`, `GetDocByWorkUnit`, `OnDialogCloseRunWorkUnitId`, `UrlWorkUnit`
- **Other `.wu` files** – if they reference the process by ID

Reference format in XAML: `"DisplayName => GUID"` (the part after `=>` is the ID used for lookup):

```xml
WorkUnit="Server Action that does nothing => 14E09BBB-4D46-4C54-BF2C-246EF94A6D82"
```

## Structure

| Folder | Description |
|--------|-------------|
| `TemplateStructuredProcess` | Example processes for demonstration and testing |
