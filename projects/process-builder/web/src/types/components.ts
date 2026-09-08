export type ComponentKind =
  | 'MilestoneDialog'
  | 'DocumentFlowWizard'
  | 'DocumentReminder'
  | 'SendEmailDialog'
  | 'MeetingInviteDialog'
  | 'StartSubprocess'
  | 'OpenUrl'
  | 'ShareWithDialog'
  | 'ClientAction'
  | 'Checkpoint'
  | 'ProcessTask'

/** Components that appear as direct children under Phase.PhaseActivities */
export const PHASE_CHILD_KINDS: ComponentKind[] = [
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

export type ArgumentValue = string | boolean | number

export interface ArgumentField {
  key: string
  label: string
  type: 'string' | 'bool' | 'text' | 'number'
  defaultValue: ArgumentValue
  hint?: string
}

export interface ComponentCatalogEntry {
  kind: ComponentKind
  label: string
  description: string
  xamlType: string
  /** If false, extends a preceding wizard instead of adding a phase child */
  isPhaseChild: boolean
  argumentFields: ArgumentField[]
}

export interface ComponentInstance {
  id: string
  kind: ComponentKind
  arguments: Record<string, ArgumentValue>
}

export const COMPONENT_CATALOG: ComponentCatalogEntry[] = [
  {
    kind: 'MilestoneDialog',
    label: 'Milestone dialog',
    description: 'Register a milestone or date on the case',
    xamlType: 'sbcpap:MilestoneDialog',
    isPhaseChild: true,
    argumentFields: [
      { key: 'showDialogue', label: 'Show dialogue', type: 'bool', defaultValue: true },
      { key: 'activityTitle', label: 'Activity title', type: 'string', defaultValue: '' },
      { key: 'automationId', label: 'Milestone automation ID', type: 'string', defaultValue: '' },
    ],
  },
  {
    kind: 'DocumentFlowWizard',
    label: 'Document flow wizard',
    description: 'Create and route a document through review, approval, and dispatch',
    xamlType: 'sbcpap:DocumentFlowWizard',
    isPhaseChild: true,
    argumentFields: [
      { key: 'showDialogue', label: 'Show dialogue', type: 'bool', defaultValue: true },
      { key: 'activityTitle', label: 'Activity title', type: 'string', defaultValue: '' },
      { key: 'outboundArchive', label: 'Outbound archive', type: 'string', defaultValue: '' },
      { key: 'outboundCategory', label: 'Outbound category', type: 'string', defaultValue: '' },
      { key: 'caseRole', label: 'Case role (recipients)', type: 'string', defaultValue: '' },
      { key: 'caseRoleCC', label: 'Case role CC', type: 'string', defaultValue: '' },
      { key: 'documentTitle', label: 'Document title', type: 'string', defaultValue: '' },
      { key: 'documentTemplateId', label: 'Document template ID', type: 'string', defaultValue: '' },
      { key: 'createReview', label: 'Create review', type: 'bool', defaultValue: false },
      { key: 'createApproval', label: 'Create approval', type: 'bool', defaultValue: false },
      { key: 'createDispatch', label: 'Create dispatch', type: 'bool', defaultValue: false },
    ],
  },
  {
    kind: 'DocumentReminder',
    label: 'Document response deadline',
    description: 'Adds a WaitTask to the preceding document wizard (place directly after a wizard)',
    xamlType: '(extends DocumentFlowWizard)',
    isPhaseChild: false,
    argumentFields: [
      {
        key: 'deadlineDays',
        label: 'Deadline (working days)',
        type: 'number',
        defaultValue: 3,
        hint: 'Maps to DeadlineDaysN on the preceding wizard',
      },
      {
        key: 'expiryWorkUnitGuid',
        label: 'Expiry hook work unit GUID',
        type: 'string',
        defaultValue: '',
        hint: 'Optional invoker WU when the deadline expires',
      },
    ],
  },
  {
    kind: 'SendEmailDialog',
    label: 'Send email',
    description: 'Send an email from the case with optional milestone',
    xamlType: 'sbcpap:SendEmailDialog',
    isPhaseChild: true,
    argumentFields: [
      { key: 'showDialogue', label: 'Show dialogue', type: 'bool', defaultValue: true },
      { key: 'activityTitle', label: 'Activity title', type: 'string', defaultValue: '' },
      { key: 'emailMessageTemplateRecno', label: 'Email template recno', type: 'string', defaultValue: '' },
      { key: 'showRecipients', label: 'Show recipients', type: 'bool', defaultValue: false },
      { key: 'showAttachments', label: 'Show attachments', type: 'bool', defaultValue: false },
      { key: 'milestoneTrigger', label: 'Milestone after send', type: 'bool', defaultValue: false },
      { key: 'milestoneAutomationId', label: 'Milestone automation ID', type: 'string', defaultValue: '' },
    ],
  },
  {
    kind: 'MeetingInviteDialog',
    label: 'Meeting invite',
    description: 'Create a meeting or appointment from the case',
    xamlType: 'sbcpap:MeetingInviteDialog',
    isPhaseChild: true,
    argumentFields: [
      { key: 'showDialogue', label: 'Show dialogue', type: 'bool', defaultValue: true },
      { key: 'activityTitle', label: 'Activity title', type: 'string', defaultValue: '' },
      { key: 'showRecipients', label: 'Show recipients', type: 'bool', defaultValue: false },
      { key: 'showAttachments', label: 'Show attachments', type: 'bool', defaultValue: false },
      { key: 'milestoneTrigger', label: 'Milestone after invite', type: 'bool', defaultValue: false },
      { key: 'milestoneAutomationId', label: 'Milestone automation ID', type: 'string', defaultValue: '' },
      { key: 'meetingSubject', label: 'Meeting subject', type: 'string', defaultValue: '' },
      { key: 'meetingBody', label: 'Meeting body', type: 'text', defaultValue: '' },
    ],
  },
  {
    kind: 'StartSubprocess',
    label: 'Start subprocess',
    description: 'Launch a configured subprocess via ProcessDialog',
    xamlType: 'sbcpap:ProcessDialog',
    isPhaseChild: true,
    argumentFields: [
      { key: 'showDialogue', label: 'Show dialogue', type: 'bool', defaultValue: true },
      { key: 'activityTitle', label: 'Activity title', type: 'string', defaultValue: '' },
      { key: 'automationId', label: 'Process automation ID', type: 'string', defaultValue: '' },
    ],
  },
  {
    kind: 'OpenUrl',
    label: 'Open URL',
    description: 'Open an external link from the process (manual URL mode)',
    xamlType: 'sbcpap:OpenUrl',
    isPhaseChild: true,
    argumentFields: [
      { key: 'showDialogue', label: 'Show dialogue', type: 'bool', defaultValue: true },
      { key: 'activityTitle', label: 'Activity title', type: 'string', defaultValue: '' },
      { key: 'url', label: 'URL', type: 'string', defaultValue: '' },
    ],
  },
  {
    kind: 'ShareWithDialog',
    label: 'Share with (internal)',
    description: 'Internal share with two connected milestones (auto + manual)',
    xamlType: 'sbcpap:ShareWithDialog',
    isPhaseChild: true,
    argumentFields: [
      { key: 'showDialogue', label: 'Show dialogue', type: 'bool', defaultValue: true },
      { key: 'activityTitle', label: 'Activity title', type: 'string', defaultValue: '' },
      { key: 'showConnectedMilestone1', label: 'Show connected milestone 1 (auto)', type: 'bool', defaultValue: true },
      { key: 'connectedMilestoneTitle1', label: 'Connected milestone 1 title', type: 'string', defaultValue: '' },
      { key: 'connectedMilestoneAutomationId1', label: 'Connected milestone 1 automation ID', type: 'string', defaultValue: '' },
      { key: 'showConnectedMilestone2', label: 'Show connected milestone 2 (manual)', type: 'bool', defaultValue: true },
      { key: 'connectedMilestoneTitle2', label: 'Connected milestone 2 title', type: 'string', defaultValue: '' },
      { key: 'connectedMilestoneAutomationId2', label: 'Connected milestone 2 automation ID', type: 'string', defaultValue: '' },
    ],
  },
  {
    kind: 'ClientAction',
    label: 'Client action (Case Wizard)',
    description: 'Open Case Wizard (ClientActionId 19) or legacy client action picker',
    xamlType: 'sbcpap:ClientAction',
    isPhaseChild: true,
    argumentFields: [
      { key: 'showDialogue', label: 'Show dialogue', type: 'bool', defaultValue: true },
      { key: 'activityTitle', label: 'Activity title', type: 'string', defaultValue: '' },
      {
        key: 'useLegacyClientAction',
        label: 'Use legacy client action picker',
        type: 'bool',
        defaultValue: false,
        hint: 'When off, uses fixed Case Wizard id 19',
      },
      { key: 'legacyClientAction', label: 'Legacy client action', type: 'string', defaultValue: '' },
    ],
  },
  {
    kind: 'Checkpoint',
    label: 'Checkpoint',
    description: 'Manual checkpoint task for case handler follow-up',
    xamlType: 'sbcpap:Task',
    isPhaseChild: true,
    argumentFields: [
      { key: 'showDialogue', label: 'Show dialogue', type: 'bool', defaultValue: true },
      { key: 'activityTitle', label: 'Activity title', type: 'string', defaultValue: '' },
    ],
  },
  {
    kind: 'ProcessTask',
    label: 'Process task',
    description: 'Product-style process task (ShowProcessTaskDialogue / ActionTitle)',
    xamlType: 'sbcpap:Task',
    isPhaseChild: true,
    argumentFields: [
      { key: 'showDialogue', label: 'Show dialogue', type: 'bool', defaultValue: true },
      { key: 'activityTitle', label: 'Action title', type: 'string', defaultValue: '' },
    ],
  },
]

export function getCatalogEntry(kind: ComponentKind): ComponentCatalogEntry {
  const entry = COMPONENT_CATALOG.find((c) => c.kind === kind)
  if (!entry) throw new Error(`Unknown component kind: ${kind}`)
  return entry
}

export function createDefaultArguments(kind: ComponentKind): Record<string, ArgumentValue> {
  const entry = getCatalogEntry(kind)
  return entry.argumentFields.reduce<Record<string, ArgumentValue>>((acc, field) => {
    acc[field.key] = field.defaultValue
    return acc
  }, {})
}

export function createComponentInstance(kind: ComponentKind): ComponentInstance {
  return {
    id: crypto.randomUUID(),
    kind,
    arguments: createDefaultArguments(kind),
  }
}

export function getInstanceIndex(instances: ComponentInstance[], instanceId: string): number {
  const target = instances.find((i) => i.id === instanceId)
  if (!target) return 0
  return instances.filter((i) => i.kind === target.kind).findIndex((i) => i.id === instanceId) + 1
}

export function getInstanceLabel(instance: ComponentInstance, index: number): string {
  const entry = getCatalogEntry(instance.kind)
  if (instance.kind === 'DocumentReminder') {
    return 'Document response deadline'
  }
  return `${entry.label} #${index}`
}

export function isPhaseChildKind(kind: ComponentKind): boolean {
  return getCatalogEntry(kind).isPhaseChild
}
