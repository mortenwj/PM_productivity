import { useState } from 'react'
import { ComponentPalette } from './components/ComponentPalette'
import { ProcessCanvas } from './components/ProcessCanvas'
import { downloadWorkUnitPair } from './lib/download'
import { generateWorkUnitPair } from './lib/generator'
import { exportProcessJson, loadProcesses, normalizeProcess, saveProcesses } from './lib/storage'
import type { ComponentInstance } from './types/components'
import {
  createEmptyProcess,
  TEMPLATE_SCOPE_OPTIONS,
  PROCESS_PROFILE_OPTIONS,
  NAMING_SCHEME_OPTIONS,
  type ProcessDefinition,
} from './types/process'

const COPY = {
  productName: 'Process Builder',
  productTagline: '360° Flow — process definitions',
  v1Badge: 'v1 POC',
  sidebarTitle: 'Processes',
  newProcess: 'New process',
  emptyList: 'No processes yet',
  pageTitle: 'Process editor',
  pageSubtitle: 'Drag components from the palette, reorder them, and configure arguments',
  templateScope: 'Treatment form',
  templateScopeHint:
    'Defines whether this configuration uses a global process template or a stage-specific process.',
  processName: 'Process name',
  processNamePlaceholder: 'E.g. Application handling',
  description: 'Description',
  status: 'Status',
  save: 'Save process',
  reset: 'Reset',
  generate: 'Generate .wu + .xaml',
  generated: 'Generated .wu and .xaml files',
  componentsRequired: 'Add at least one component before generating',
  export: 'Export JSON',
  saved: 'Process saved',
  nameRequired: 'Process name is required',
} as const

function App() {
  const [processes, setProcesses] = useState<ProcessDefinition[]>(() => loadProcesses())
  const [current, setCurrent] = useState<ProcessDefinition>(() => createEmptyProcess())
  const [paletteOpen, setPaletteOpen] = useState(false)
  const [savedProcessesCollapsed, setSavedProcessesCollapsed] = useState(false)
  const [selectedComponentId, setSelectedComponentId] = useState<string | null>(null)
  const [message, setMessage] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)

  function openDesignMode() {
    setPaletteOpen(true)
    setSavedProcessesCollapsed(true)
  }

  function selectProcess(id: string) {
    const found = processes.find((p) => p.id === id)
    if (found) {
      setCurrent(normalizeProcess(found))
      openDesignMode()
      setSelectedComponentId(null)
      setError(null)
      setMessage(null)
    }
  }

  function startNewProcess() {
    setCurrent(createEmptyProcess())
    openDesignMode()
    setSelectedComponentId(null)
    setError(null)
    setMessage(null)
  }

  function updateCurrent(patch: Partial<ProcessDefinition>) {
    setCurrent((prev) => ({ ...prev, ...patch }))
  }

  function updateComponents(components: ComponentInstance[]) {
    updateCurrent({ components })
  }

  function handleSave() {
    if (!current.name.trim()) {
      setError(COPY.nameRequired)
      setMessage(null)
      return
    }

    const saved = normalizeProcess({
      ...current,
      updatedAt: new Date().toISOString(),
    })

    const next = processes.some((p) => p.id === saved.id)
      ? processes.map((p) => (p.id === saved.id ? saved : p))
      : [...processes, saved]

    setProcesses(next)
    saveProcesses(next)
    setCurrent(saved)
    setError(null)
    setMessage(COPY.saved)
  }

  function handleReset() {
    setCurrent(createEmptyProcess())
    setSelectedComponentId(null)
    openDesignMode()
    setError(null)
    setMessage(null)
  }

  function handleExport() {
    const blob = new Blob([exportProcessJson(current)], { type: 'application/json' })
    const url = URL.createObjectURL(blob)
    const anchor = document.createElement('a')
    anchor.href = url
    anchor.download = `${current.name.trim() || 'process'}.json`
    anchor.click()
    URL.revokeObjectURL(url)
  }

  function handleGenerate() {
    const result = generateWorkUnitPair(current)
    if (!result.ok) {
      setError(result.error.message)
      setMessage(null)
      return
    }

    const withWorkUnitId = normalizeProcess({
      ...current,
      workUnitId: result.pair.workUnitId,
      updatedAt: new Date().toISOString(),
    })
    setCurrent(withWorkUnitId)
    const next = processes.some((p) => p.id === withWorkUnitId.id)
      ? processes.map((p) => (p.id === withWorkUnitId.id ? withWorkUnitId : p))
      : [...processes, withWorkUnitId]
    setProcesses(next)
    saveProcesses(next)

    downloadWorkUnitPair(result.pair.basename, result.pair.wu, result.pair.xaml)
    setError(null)
    setMessage(COPY.generated)
  }

  return (
    <div className="app-shell">
      <header className="app-header">
        <div className="app-header__brand">
          <img className="app-header__logo" src="/assets/tieto-logo-blue.svg" alt="Tietoevry" />
          <div className="app-header__title-block">
            <h1>{COPY.productName}</h1>
            <p>{COPY.productTagline}</p>
          </div>
        </div>
        <span className="app-header__badge">{COPY.v1Badge}</span>
      </header>

      <div className="workspace">
        <aside className={`sidebar ${paletteOpen ? 'sidebar--design' : ''}`}>
          <h2 className="sidebar__title">{COPY.sidebarTitle}</h2>

          <button
            type="button"
            className={`btn btn--secondary sidebar__new ${paletteOpen ? 'is-active' : ''}`}
            onClick={startNewProcess}
            aria-expanded={paletteOpen}
          >
            + {COPY.newProcess}
          </button>

          <ComponentPalette open={paletteOpen} />

          <section
            className={`sidebar__saved ${savedProcessesCollapsed ? 'is-collapsed' : ''}`}
            aria-label="Saved processes"
          >
            <button
              type="button"
              className="sidebar__saved-toggle"
              onClick={() => setSavedProcessesCollapsed((prev) => !prev)}
              aria-expanded={!savedProcessesCollapsed}
            >
              <span className="sidebar__saved-toggle-label">
                Saved processes
                {processes.length > 0 && (
                  <span className="sidebar__saved-count">{processes.length}</span>
                )}
              </span>
              <span className="sidebar__saved-chevron" aria-hidden />
            </button>

            {!savedProcessesCollapsed && (
              <div className="sidebar__saved-body">
                {processes.length === 0 ? (
                  <p className="process-list__empty">{COPY.emptyList}</p>
                ) : (
                  <ul className="process-list">
                    {processes.map((process) => (
                      <li key={process.id}>
                        <button
                          type="button"
                          className={`process-list__item ${process.id === current.id ? 'is-active' : ''}`}
                          onClick={() => selectProcess(process.id)}
                        >
                          <div>{process.name || 'Untitled process'}</div>
                          <span className="status-pill">{process.status}</span>
                        </button>
                      </li>
                    ))}
                  </ul>
                )}
              </div>
            )}
          </section>
        </aside>

        <main className="editor">
          <div className="editor__inner">
            <h2 className="page-title">{COPY.pageTitle}</h2>
            <p className="page-subtitle">{COPY.pageSubtitle}</p>

            <div className="card card--process">
              <div className="process-meta">
                <div className="field">
                  <label htmlFor="templateScope">{COPY.templateScope} *</label>
                  <select
                    id="templateScope"
                    value={current.templateScope}
                    onChange={(e) =>
                      updateCurrent({ templateScope: e.target.value as ProcessDefinition['templateScope'] })
                    }
                  >
                    {TEMPLATE_SCOPE_OPTIONS.map((opt) => (
                      <option key={opt.value} value={opt.value}>
                        {opt.labelEn}
                      </option>
                    ))}
                  </select>
                  <p className="hint">{COPY.templateScopeHint}</p>
                </div>

                <div className="field">
                  <label htmlFor="processName">{COPY.processName} *</label>
                  <input
                    id="processName"
                    value={current.name}
                    placeholder={COPY.processNamePlaceholder}
                    onChange={(e) => updateCurrent({ name: e.target.value })}
                  />
                </div>

                <div className="field">
                  <label htmlFor="description">{COPY.description}</label>
                  <textarea
                    id="description"
                    rows={2}
                    value={current.description}
                    onChange={(e) => updateCurrent({ description: e.target.value })}
                  />
                </div>

                <div className="field field--inline">
                  <label htmlFor="processProfile">Process profile</label>
                  <select
                    id="processProfile"
                    value={current.processProfile}
                    onChange={(e) =>
                      updateCurrent({ processProfile: e.target.value as ProcessDefinition['processProfile'] })
                    }
                  >
                    {PROCESS_PROFILE_OPTIONS.map((opt) => (
                      <option key={opt.value} value={opt.value}>
                        {opt.labelEn}
                      </option>
                    ))}
                  </select>
                </div>

                {current.processProfile === 'progress-plan' && (
                  <div className="field field--inline">
                    <label htmlFor="namingScheme">Naming scheme</label>
                    <select
                      id="namingScheme"
                      value={current.namingScheme}
                      onChange={(e) =>
                        updateCurrent({ namingScheme: e.target.value as ProcessDefinition['namingScheme'] })
                      }
                    >
                      {NAMING_SCHEME_OPTIONS.map((opt) => (
                        <option key={opt.value} value={opt.value}>
                          {opt.labelEn}
                        </option>
                      ))}
                    </select>
                  </div>
                )}

                <div className="field field--full">
                  <label htmlFor="featureToggles">Feature toggles</label>
                  <input
                    id="featureToggles"
                    placeholder="None — leave empty, or comma-separated names (e.g. NVE)"
                    value={current.featureToggles}
                    onChange={(e) => updateCurrent({ featureToggles: e.target.value })}
                  />
                  <p className="hint">Maps to &lt;featuretoggles&gt; in the .wu file. Omit when empty.</p>
                </div>

                {current.processProfile === 'progress-plan' && (
                  <>
                    <div className="field">
                      <label htmlFor="phaseDeadlineDays">Phase deadline (days)</label>
                      <input
                        id="phaseDeadlineDays"
                        placeholder="Optional"
                        value={current.phaseDeadlineDays}
                        onChange={(e) => updateCurrent({ phaseDeadlineDays: e.target.value })}
                      />
                    </div>
                    <div className="field">
                      <label htmlFor="phaseWarningDays">Phase warning (days)</label>
                      <input
                        id="phaseWarningDays"
                        placeholder="Optional"
                        value={current.phaseWarningDays}
                        onChange={(e) => updateCurrent({ phaseWarningDays: e.target.value })}
                      />
                    </div>
                  </>
                )}

                <div className="field field--inline">
                  <label htmlFor="status">{COPY.status}</label>
                  <select
                    id="status"
                    value={current.status}
                    onChange={(e) => updateCurrent({ status: e.target.value as ProcessDefinition['status'] })}
                  >
                    <option value="draft">Draft</option>
                    <option value="active">Active</option>
                    <option value="inactive">Inactive</option>
                  </select>
                </div>
              </div>

              {current.processProfile === 'background' && (
                <p className="hint process-canvas__notice">
                  Background processes are not yet supported for .wu / .xaml generation. Switch to progress-plan
                  to design phase activities.
                </p>
              )}

              <ProcessCanvas
                components={current.components}
                selectedId={selectedComponentId}
                onSelect={setSelectedComponentId}
                onChange={updateComponents}
                disabled={current.processProfile === 'background'}
              />

              {error && <p className="form-message form-message--error">{error}</p>}
              {message && <p className="form-message form-message--success">{message}</p>}

              <div className="actions">
                <button type="button" className="btn btn--secondary" onClick={handleSave}>
                  {COPY.save}
                </button>
                <button type="button" className="btn btn--primary" onClick={handleGenerate}>
                  {COPY.generate}
                </button>
                <button type="button" className="btn btn--secondary" onClick={handleReset}>
                  {COPY.reset}
                </button>
                <button type="button" className="btn btn--secondary" onClick={handleExport}>
                  {COPY.export}
                </button>
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  )
}

export default App
