import { createEmptyProcess, type ProcessDefinition, type ProcessProfile, type NamingScheme } from '../types/process'
import type { ComponentInstance, ComponentKind } from '../types/components'

const STORAGE_KEY = 'process-builder.definitions.v2'

function normalizeComponents(raw: unknown): ComponentInstance[] {
  if (!Array.isArray(raw)) return []
  return raw.filter(
    (item): item is ComponentInstance =>
      Boolean(
        item &&
          typeof item === 'object' &&
          typeof (item as ComponentInstance).id === 'string' &&
          typeof (item as ComponentInstance).kind === 'string' &&
          (item as ComponentInstance).arguments &&
          typeof (item as ComponentInstance).arguments === 'object',
      ),
  ).map((item) => ({
    ...item,
    kind: item.kind as ComponentKind,
  }))
}

export function normalizeProcess(raw: unknown): ProcessDefinition {
  const base = createEmptyProcess()
  if (!raw || typeof raw !== 'object') return base

  const record = raw as Partial<ProcessDefinition>
  const templateScope =
    record.templateScope === 'global' || record.templateScope === 'stage-specific'
      ? record.templateScope
      : base.templateScope
  const status =
    record.status === 'draft' || record.status === 'active' || record.status === 'inactive'
      ? record.status
      : base.status

  const processProfile: ProcessProfile =
    record.processProfile === 'background' ? 'background' : 'progress-plan'
  const namingScheme: NamingScheme =
    record.namingScheme === 'paf-single' || record.namingScheme === 'hearing-style'
      ? record.namingScheme
      : 'suffixed-nve'

  return {
    ...base,
    ...record,
    id: typeof record.id === 'string' ? record.id : base.id,
    name: typeof record.name === 'string' ? record.name : '',
    description: typeof record.description === 'string' ? record.description : '',
    templateScope,
    status,
    processProfile,
    namingScheme,
    featureToggles: typeof record.featureToggles === 'string' ? record.featureToggles : '',
    phaseDeadlineDays: typeof record.phaseDeadlineDays === 'string' ? record.phaseDeadlineDays : '',
    phaseWarningDays: typeof record.phaseWarningDays === 'string' ? record.phaseWarningDays : '',
    workUnitId: typeof record.workUnitId === 'string' ? record.workUnitId : '',
    components: normalizeComponents(record.components),
    updatedAt: typeof record.updatedAt === 'string' ? record.updatedAt : base.updatedAt,
  }
}

export function loadProcesses(): ProcessDefinition[] {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    if (!raw) return []
    const parsed = JSON.parse(raw) as unknown
    if (!Array.isArray(parsed)) return []
    return parsed.map(normalizeProcess)
  } catch {
    return []
  }
}

export function saveProcesses(processes: ProcessDefinition[]): void {
  const normalized = processes.map(normalizeProcess)
  localStorage.setItem(STORAGE_KEY, JSON.stringify(normalized))
}

export function exportProcessJson(process: ProcessDefinition): string {
  return JSON.stringify(normalizeProcess(process), null, 2)
}
