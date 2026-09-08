import type { DragEvent } from 'react'
import { COMPONENT_CATALOG, type ComponentKind } from '../types/components'
import { clearDragPayload, setDragPayload } from '../lib/dnd'

interface ComponentPaletteProps {
  open: boolean
}

export function ComponentPalette({ open }: ComponentPaletteProps) {
  if (!open) return null

  function onDragStart(kind: ComponentKind, event: DragEvent) {
    setDragPayload(event.dataTransfer, { source: 'palette', kind })
  }

  function onDragEnd() {
    clearDragPayload()
  }

  return (
    <div className="component-palette">
      <p className="component-palette__hint">Drag components into the process canvas</p>
      <ul className="component-palette__list">
        {COMPONENT_CATALOG.map((entry) => (
          <li key={entry.kind}>
            <div
              className="palette-item"
              draggable
              onDragStart={(e) => onDragStart(entry.kind, e)}
              onDragEnd={onDragEnd}
            >
              <span className="palette-item__drag" aria-hidden>⠿</span>
              <div className="palette-item__body">
                <span className="palette-item__label">{entry.label}</span>
                <span className="palette-item__meta">{entry.kind}</span>
              </div>
            </div>
          </li>
        ))}
      </ul>
    </div>
  )
}
