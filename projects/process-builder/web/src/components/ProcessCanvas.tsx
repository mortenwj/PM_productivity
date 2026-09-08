import { useState } from 'react'
import {
  createComponentInstance,
  getCatalogEntry,
  getInstanceIndex,
  getInstanceLabel,
  isPhaseChildKind,
  type ComponentInstance,
  type ComponentKind,
} from '../types/components'
import { resolveProcessComponents } from '../lib/generator/context'
import {
  clearDragPayload,
  getActiveDrag,
  insertAt,
  moveItem,
  readDragPayload,
  setDragPayload,
} from '../lib/dnd'
import { ArgumentInspector } from './ArgumentInspector'
import type { ArgumentValue } from '../types/components'

interface ProcessCanvasProps {
  components?: ComponentInstance[]
  selectedId: string | null
  onSelect: (id: string | null) => void
  onChange: (components: ComponentInstance[]) => void
  disabled?: boolean
}

export function ProcessCanvas({
  components = [],
  selectedId,
  onSelect,
  onChange,
  disabled = false,
}: ProcessCanvasProps) {
  const [dragOverIndex, setDragOverIndex] = useState<number | null>(null)
  const [draggingInstanceId, setDraggingInstanceId] = useState<string | null>(null)
  const [paletteDragActive, setPaletteDragActive] = useState(false)

  function resolveDropIndex(rawIndex: number): number {
    return Math.max(0, Math.min(rawIndex, components.length))
  }

  function handleDropAt(index: number, event: React.DragEvent) {
    event.preventDefault()
    event.stopPropagation()
    setDragOverIndex(null)
    setPaletteDragActive(false)
    setDraggingInstanceId(null)

    const payload = readDragPayload(event.dataTransfer)
    clearDragPayload()
    if (!payload) return

    const targetIndex = resolveDropIndex(index)

    if (payload.source === 'palette') {
      const instance = createComponentInstance(payload.kind as ComponentKind)
      onChange(insertAt(components, instance, targetIndex))
      onSelect(instance.id)
      return
    }

    const fromIndex = components.findIndex((c) => c.id === payload.instanceId)
    if (fromIndex === -1) return

    let toIndex = targetIndex
    if (fromIndex < toIndex) toIndex -= 1
    if (fromIndex === toIndex) return
    onChange(moveItem(components, fromIndex, toIndex))
    onSelect(payload.instanceId)
  }

  function allowDrop(event: React.DragEvent) {
    const drag = getActiveDrag()
    if (!drag) return
    event.preventDefault()
    event.dataTransfer.dropEffect = drag.source === 'palette' ? 'copy' : 'move'
    if (drag.source === 'palette') setPaletteDragActive(true)
  }

  const selected = components.find((c) => c.id === selectedId) ?? null
  const { wizardReminders } = resolveProcessComponents(components)

  function isOrphanReminder(instance: ComponentInstance): boolean {
    if (instance.kind !== 'DocumentReminder') return false
    return !Array.from(wizardReminders.values()).some((r) => r.id === instance.id)
  }

  function updateArgument(instanceId: string, key: string, value: ArgumentValue) {
    onChange(
      components.map((c) =>
        c.id === instanceId ? { ...c, arguments: { ...c.arguments, [key]: value } } : c,
      ),
    )
  }

  function removeInstance(instanceId: string) {
    onChange(components.filter((c) => c.id !== instanceId))
    if (selectedId === instanceId) onSelect(null)
  }

  function renderDropSlot(index: number) {
    const isActive = dragOverIndex === index
    return (
      <div
        key={`slot-${index}`}
        className={`drop-slot ${isActive ? 'is-active' : ''}`}
        onDragEnter={(e) => {
          allowDrop(e)
          setDragOverIndex(index)
        }}
        onDragOver={allowDrop}
        onDragLeave={(e) => {
          if (e.currentTarget.contains(e.relatedTarget as Node)) return
          setDragOverIndex((prev) => (prev === index ? null : prev))
        }}
        onDrop={(e) => handleDropAt(index, e)}
      />
    )
  }

  return (
    <div className={`process-canvas ${disabled ? 'is-disabled' : ''}`}>
      <div
        className={`process-canvas__list ${components.length === 0 ? 'is-empty' : ''} ${paletteDragActive ? 'is-palette-drag' : ''}`}
        onDragOver={(e) => {
          allowDrop(e)
          if (components.length === 0) setDragOverIndex(0)
        }}
        onDrop={(e) => {
          if (components.length === 0) handleDropAt(0, e)
          else handleDropAt(components.length, e)
        }}
      >
        {components.length === 0 ? (
          <div className="process-canvas__empty">
            <p>Drag components from the palette to build your process</p>
            <p className="hint">Order matters — activities run top to bottom</p>
          </div>
        ) : (
          <>
            {renderDropSlot(0)}
            {components.map((instance, index) => {
              const instanceIndex = instance.kind === 'DocumentReminder'
                ? 0
                : getInstanceIndex(components, instance.id)
              const entry = getCatalogEntry(instance.kind)
              const label = getInstanceLabel(instance, instanceIndex)
              const isSelected = instance.id === selectedId
              const isDragging = draggingInstanceId === instance.id
              const isModifier = !isPhaseChildKind(instance.kind)
              const isOrphan = isOrphanReminder(instance)

              return (
                <div key={instance.id} className="canvas-row">
                  <div
                    className={`canvas-card ${isSelected ? 'is-selected' : ''} ${isDragging ? 'is-dragging' : ''} ${isModifier ? 'canvas-card--modifier' : ''} ${isOrphan ? 'canvas-card--warning' : ''}`}
                    draggable={!disabled}
                    onDragStart={(e) => {
                      setDraggingInstanceId(instance.id)
                      setDragPayload(e.dataTransfer, { source: 'instance', instanceId: instance.id })
                    }}
                    onDragEnd={() => {
                      clearDragPayload()
                      setDraggingInstanceId(null)
                      setDragOverIndex(null)
                      setPaletteDragActive(false)
                    }}
                    onDragOver={(e) => {
                      if (getActiveDrag()?.source === 'palette') {
                        allowDrop(e)
                        setDragOverIndex(index + 1)
                      }
                    }}
                    onDrop={(e) => {
                      if (getActiveDrag()?.source === 'palette') {
                        handleDropAt(index + 1, e)
                      }
                    }}
                    onClick={() => onSelect(instance.id)}
                  >
                    <span className="canvas-card__handle" aria-hidden>⠿</span>
                    <div className="canvas-card__body">
                      {!isModifier && <span className="canvas-card__step">{index + 1}</span>}
                      <div>
                        <div className="canvas-card__title">{label}</div>
                        <div className="canvas-card__meta">
                          {isModifier ? 'Extends preceding wizard' : entry.kind}
                          {isOrphan && ' — place after a document wizard'}
                        </div>
                      </div>
                    </div>
                  </div>
                  {renderDropSlot(index + 1)}
                </div>
              )
            })}
          </>
        )}
      </div>

      {selected && (
        <ArgumentInspector
          instance={selected}
          allInstances={components}
          onChange={updateArgument}
          onRemove={removeInstance}
        />
      )}
    </div>
  )
}
