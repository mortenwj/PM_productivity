import type { ComponentInstance } from './components'

export type ProcessTemplateScope = 'global' | 'stage-specific'

export type ProcessStatus = 'draft' | 'active' | 'inactive'

/** Discovery Q0 — progress-plan (phase activities) vs background (no phase list) */
export type ProcessProfile = 'progress-plan' | 'background'

/** Discovery Q5 — argument naming scheme */
export type NamingScheme = 'suffixed-nve' | 'paf-single' | 'hearing-style'

export interface ProcessDefinition {
  id: string
  name: string
  status: ProcessStatus
  description: string
  templateScope: ProcessTemplateScope
  processProfile: ProcessProfile
  namingScheme: NamingScheme
  /** Discovery Q4 — comma-separated feature toggle names, or empty for none */
  featureToggles: string
  /** Optional phase metadata (templates.md §19) */
  phaseDeadlineDays: string
  phaseWarningDays: string
  /** Stable work unit GUID — regenerated on first save if empty */
  workUnitId: string
  components: ComponentInstance[]
  updatedAt: string
}

export const TEMPLATE_SCOPE_OPTIONS: { value: ProcessTemplateScope; labelEn: string }[] = [
  { value: 'global', labelEn: 'Global process template' },
  { value: 'stage-specific', labelEn: 'Stage-specific process' },
]

export const PROCESS_PROFILE_OPTIONS: { value: ProcessProfile; labelEn: string }[] = [
  { value: 'progress-plan', labelEn: 'Progress-plan process (phase activities)' },
  { value: 'background', labelEn: 'Background process (automatic, no phase steps)' },
]

export const NAMING_SCHEME_OPTIONS: { value: NamingScheme; labelEn: string }[] = [
  { value: 'suffixed-nve', labelEn: 'Suffixed NVE (default)' },
  { value: 'paf-single', labelEn: 'PAF single-document (unprefixed)' },
  { value: 'hearing-style', labelEn: 'Hearing-style (DoReview / DoApproval / …)' },
]

export function createEmptyProcess(): ProcessDefinition {
  return {
    id: crypto.randomUUID(),
    name: '',
    status: 'draft',
    description: '',
    templateScope: 'stage-specific',
    processProfile: 'progress-plan',
    namingScheme: 'suffixed-nve',
    featureToggles: '',
    phaseDeadlineDays: '',
    phaseWarningDays: '',
    workUnitId: '',
    components: [],
    updatedAt: new Date().toISOString(),
  }
}
