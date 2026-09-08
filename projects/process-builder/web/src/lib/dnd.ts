import type { ComponentKind } from '../types/components'

export const PALETTE_DRAG_TYPE = 'application/x-process-builder-component'
export const INSTANCE_DRAG_TYPE = 'application/x-process-builder-instance'
const PLAIN_DRAG_TYPE = 'text/plain'

export type PaletteDragPayload = { source: 'palette'; kind: ComponentKind }
export type InstanceDragPayload = { source: 'instance'; instanceId: string }

export type DragPayload = PaletteDragPayload | InstanceDragPayload

/** Tracks the active drag because dataTransfer is restricted during dragover in some browsers. */
let activeDrag: DragPayload | null = null

export function getActiveDrag(): DragPayload | null {
  return activeDrag
}

export function setActiveDrag(payload: DragPayload | null): void {
  activeDrag = payload
}

export function setDragPayload(dataTransfer: DataTransfer, payload: DragPayload): void {
  setActiveDrag(payload)
  const serialized = JSON.stringify(payload)
  dataTransfer.effectAllowed = payload.source === 'palette' ? 'copy' : 'move'
  dataTransfer.setData(
    payload.source === 'palette' ? PALETTE_DRAG_TYPE : INSTANCE_DRAG_TYPE,
    serialized,
  )
  // Fallback for browsers that only expose plain text reliably on drop.
  dataTransfer.setData(PLAIN_DRAG_TYPE, serialized)
}

export function clearDragPayload(): void {
  setActiveDrag(null)
}

export function readDragPayload(dataTransfer: DataTransfer): DragPayload | null {
  const candidates = [
    dataTransfer.getData(PALETTE_DRAG_TYPE),
    dataTransfer.getData(INSTANCE_DRAG_TYPE),
    dataTransfer.getData(PLAIN_DRAG_TYPE),
  ].filter(Boolean)

  for (const raw of candidates) {
    try {
      const parsed = JSON.parse(raw) as DragPayload
      if (parsed.source === 'palette' && parsed.kind) return parsed
      if (parsed.source === 'instance' && parsed.instanceId) return parsed
    } catch {
      // try next candidate
    }
  }

  return activeDrag
}

export function insertAt<T>(items: T[], item: T, index: number): T[] {
  const next = [...items]
  next.splice(index, 0, item)
  return next
}

export function moveItem<T>(items: T[], fromIndex: number, toIndex: number): T[] {
  if (fromIndex === toIndex || fromIndex < 0 || toIndex < 0) return items
  const next = [...items]
  const [removed] = next.splice(fromIndex, 1)
  next.splice(toIndex, 0, removed)
  return next
}
