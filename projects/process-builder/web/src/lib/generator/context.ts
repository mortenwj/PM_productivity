import type { ComponentInstance, ComponentKind } from '../../types/components'
import { isPhaseChildKind } from '../../types/components'
import type { NamingScheme, ProcessDefinition } from '../../types/process'

export interface WuArgument {
  name: string
  type: 'string' | 'bool' | 'int'
  comment?: string
  value?: string
  category?: string
}

export interface IndexedInstance {
  kind: ComponentKind
  index: number
  instance: ComponentInstance
}

export interface WizardReminder {
  wizardIndex: number
  instance: ComponentInstance
}

export interface GenerationContext {
  displayName: string
  className: string
  workUnitId: string
  processProfile: ProcessDefinition['processProfile']
  namingScheme: NamingScheme
  featureToggles: string[]
  phaseDeadlineDays: string
  phaseWarningDays: string
  /** Phase children only — excludes DocumentReminder */
  phaseInstances: IndexedInstance[]
  /** Preceding wizard index → reminder config */
  wizardReminders: Map<number, ComponentInstance>
  milestoneCount: number
  hasOpenUrl: boolean
  hasEmailAndMeeting: boolean
  useMinimalShell: boolean
}

const COUNTER_KINDS: ComponentKind[] = [
  'MilestoneDialog',
  'DocumentFlowWizard',
  'SendEmailDialog',
  'MeetingInviteDialog',
  'StartSubprocess',
  'OpenUrl',
  'ShareWithDialog',
  'ClientAction',
  'Checkpoint',
  'ProcessTask',
]

export function toClassName(name: string): string {
  const cleaned = name.trim().replace(/[^a-zA-Z0-9\s_-]/g, '')
  const parts = cleaned.split(/[\s_-]+/).filter(Boolean)
  if (parts.length === 0) return 'NewProcess'
  return parts.map((p) => p[0].toUpperCase() + p.slice(1)).join('')
}

export function resolveProcessComponents(components: ComponentInstance[]): {
  phaseInstances: IndexedInstance[]
  wizardReminders: Map<number, ComponentInstance>
  milestoneCount: number
} {
  const counters = Object.fromEntries(COUNTER_KINDS.map((k) => [k, 0])) as Record<ComponentKind, number>
  const phaseInstances: IndexedInstance[] = []
  const wizardReminders = new Map<number, ComponentInstance>()
  let lastWizardIndex = 0
  let milestoneCount = 0

  for (const instance of components) {
    if (instance.kind === 'DocumentReminder') {
      if (lastWizardIndex > 0) {
        wizardReminders.set(lastWizardIndex, instance)
      }
      continue
    }

    if (!isPhaseChildKind(instance.kind)) continue

    counters[instance.kind] += 1
    const index = counters[instance.kind]
    phaseInstances.push({ kind: instance.kind, index, instance })

    if (instance.kind === 'DocumentFlowWizard') {
      lastWizardIndex = index
    }
    if (instance.kind === 'MilestoneDialog') {
      milestoneCount += 1
    }
  }

  return { phaseInstances, wizardReminders, milestoneCount }
}

export function buildGenerationContext(process: ProcessDefinition): GenerationContext {
  const { phaseInstances, wizardReminders, milestoneCount } = resolveProcessComponents(
    process.components,
  )

  const hasOpenUrl = phaseInstances.some((i) => i.kind === 'OpenUrl')
  const hasEmail = phaseInstances.some((i) => i.kind === 'SendEmailDialog')
  const hasMeeting = phaseInstances.some((i) => i.kind === 'MeetingInviteDialog')
  const useMinimalShell =
    process.processProfile === 'progress-plan' &&
    phaseInstances.length === 1 &&
    phaseInstances[0].kind === 'ProcessTask'

  const featureToggles = process.featureToggles
    .split(/[,;\n]+/)
    .map((s) => s.trim())
    .filter(Boolean)

  return {
    displayName: process.name.trim(),
    className: toClassName(process.name),
    workUnitId: process.workUnitId || crypto.randomUUID().toUpperCase(),
    processProfile: process.processProfile,
    namingScheme: process.namingScheme,
    featureToggles,
    phaseDeadlineDays: process.phaseDeadlineDays.trim(),
    phaseWarningDays: process.phaseWarningDays.trim(),
    phaseInstances,
    wizardReminders,
    milestoneCount,
    hasOpenUrl,
    hasEmailAndMeeting: hasEmail && hasMeeting,
    useMinimalShell,
  }
}

export function argBool(value: unknown, fallback = true): boolean {
  if (typeof value === 'boolean') return value
  return fallback
}

export function argString(value: unknown): string {
  return typeof value === 'string' ? value : ''
}

export function argNumber(value: unknown, fallback = 0): number {
  if (typeof value === 'number' && !Number.isNaN(value)) return value
  if (typeof value === 'string' && value.trim()) {
    const n = Number(value)
    if (!Number.isNaN(n)) return n
  }
  return fallback
}

export function boolText(value: boolean): string {
  return value ? 'true' : 'false'
}

export function escapeXml(text: string): string {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
}

/** Milestone arg suffix — unprefixed when exactly one milestone and suffixed NVE scheme */
export function milestoneSuffix(ctx: GenerationContext, index: number): string {
  if (ctx.milestoneCount === 1 && ctx.namingScheme === 'suffixed-nve') return ''
  return String(index)
}

export function milestoneArgName(base: string, ctx: GenerationContext, index: number): string {
  const suffix = milestoneSuffix(ctx, index)
  return suffix ? `${base}${suffix}` : base
}
