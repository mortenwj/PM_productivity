import {
  argBool,
  argNumber,
  argString,
  boolText,
  milestoneArgName,
  type GenerationContext,
  type IndexedInstance,
  type WuArgument,
} from './context'

function wuArg(
  name: string,
  type: WuArgument['type'],
  options: { comment?: string; value?: string; category?: string } = {},
): WuArgument {
  return { name, type, category: options.category ?? 'General', ...options }
}

function milestoneArgs(item: IndexedInstance, ctx: GenerationContext): WuArgument[] {
  const args = item.instance.arguments
  const showName = milestoneArgName('ShowMilestoneDialogue', ctx, item.index)
  const titleName = milestoneArgName('MilestoneActivityTitle', ctx, item.index)
  const autoName = milestoneArgName('MilestoneAutomationId', ctx, item.index)
  return [
    wuArg(showName, 'bool', {
      comment: 'Do you want to show this milestone? (true/false)',
      value: boolText(argBool(args.showDialogue)),
      category: 'Milestone',
    }),
    wuArg(titleName, 'string', {
      comment: 'name of the activity',
      value: argString(args.activityTitle),
      category: 'Milestone',
    }),
    wuArg(autoName, 'string', {
      value: argString(args.automationId),
      category: 'Milestone',
    }),
  ]
}

function documentReviewArgs(n: number, ctx: GenerationContext, args: Record<string, unknown>): WuArgument[] {
  const review = argBool(args.createReview, false)
  const approval = argBool(args.createApproval, false)
  const dispatch = argBool(args.createDispatch, false)

  if (ctx.namingScheme === 'hearing-style') {
    return [
      wuArg(`DoReview${n}`, 'bool', { value: boolText(review), category: `CreateDocument` }),
      wuArg(`DoApproval${n}`, 'bool', { value: boolText(approval), category: `CreateDocument` }),
      wuArg(`DoDispatch${n}`, 'bool', { value: boolText(dispatch), category: `CreateDocument` }),
    ]
  }

  const suffix = ctx.namingScheme === 'paf-single' && ctx.phaseInstances.filter((i) => i.kind === 'DocumentFlowWizard').length === 1 ? '' : String(n)
  const reviewName = suffix ? `CreateReview${suffix}` : 'CreateReview'
  const approvalName = suffix ? `CreateApproval${suffix}` : 'CreateApproval'
  const dispatchName = suffix ? `CreateDispatch${suffix}` : 'CreateDispatch'

  return [
    wuArg(reviewName, 'bool', { value: boolText(review), category: `CreateDocument` }),
    wuArg(approvalName, 'bool', { value: boolText(approval), category: `CreateDocument` }),
    wuArg(dispatchName, 'bool', { value: boolText(dispatch), category: `CreateDocument` }),
  ]
}

function documentArgs(item: IndexedInstance, ctx: GenerationContext): WuArgument[] {
  const n = item.index
  const args = item.instance.arguments
  const pafSingle =
    ctx.namingScheme === 'paf-single' &&
    ctx.phaseInstances.filter((i) => i.kind === 'DocumentFlowWizard').length === 1
  const sfx = pafSingle ? '' : String(n)

  const showName = sfx ? `ShowDocumentDialogue${sfx}` : 'ShowDocumentDialogue'
  const titleName = sfx ? `DocumentActivityTitle${sfx}` : 'DocumentActivityTitle'
  const archiveName = sfx ? `OutboundArchive${sfx}` : 'OutboundArchive'
  const categoryName = sfx ? `OutboundCategory${sfx}` : 'OutboundCategory'
  const roleName = sfx ? `CaseRole${sfx}` : 'CaseRole'
  const ccName = sfx ? `CaseRoleCC${sfx}` : 'CaseRoleCC'
  const docTitleName = sfx ? `DocumentTitle${sfx}` : 'DocumentTitle'
  const templateName = sfx ? `DocumentTemplateId${sfx}` : 'DocumentTemplateId'
  const cat = sfx ? `CreateDocument` : 'CreateDocument'

  const result: WuArgument[] = []

  if (ctx.namingScheme !== 'hearing-style') {
    result.push(
      wuArg(showName, 'bool', {
        comment: 'Do you want to show this document wizard? (true/false)',
        value: boolText(argBool(args.showDialogue)),
        category: cat,
      }),
    )
  }

  result.push(
    wuArg(titleName, 'string', {
      comment: 'name of the activity',
      value: argString(args.activityTitle),
      category: cat,
    }),
    wuArg(archiveName, 'string', { value: argString(args.outboundArchive), category: cat }),
    wuArg(categoryName, 'string', { value: argString(args.outboundCategory), category: cat }),
    wuArg(roleName, 'string', { value: argString(args.caseRole), category: cat }),
    wuArg(ccName, 'string', {
      comment: 'Optional: case role(s) used as CC on the outbound document',
      value: argString(args.caseRoleCC),
      category: cat,
    }),
    wuArg(docTitleName, 'string', { value: argString(args.documentTitle), category: cat }),
    wuArg(templateName, 'string', { value: argString(args.documentTemplateId), category: cat }),
    ...documentReviewArgs(n, ctx, args),
  )

  const reminder = ctx.wizardReminders.get(n)
  if (reminder) {
    const deadlineName = sfx ? `DeadlineDays${sfx}` : `DeadlineDays${n}`
    result.push(
      wuArg(deadlineName, 'int', {
        comment: 'Response deadline in working days',
        value: String(argNumber(reminder.arguments.deadlineDays, 3)),
        category: cat,
      }),
    )
  }

  return result
}

function emailArgs(item: IndexedInstance): WuArgument[] {
  const m = item.index
  const args = item.instance.arguments
  const cat = `create email${m}`
  return [
    wuArg(`ShowEmailDialogue${m}`, 'bool', {
      comment: 'Do you want to show this send-email step? (true/false)',
      value: boolText(argBool(args.showDialogue)),
      category: cat,
    }),
    wuArg(`EmailActivityTitle${m}`, 'string', {
      comment: 'name of the activity',
      value: argString(args.activityTitle),
      category: cat,
    }),
    wuArg(`ShowRecipients${m}`, 'bool', { value: boolText(argBool(args.showRecipients, false)), category: cat }),
    wuArg(`ShowAttatchments${m}`, 'bool', { value: boolText(argBool(args.showAttachments, false)), category: cat }),
    wuArg(`EmailMessageTemplateRecno${m}`, 'string', {
      value: argString(args.emailMessageTemplateRecno),
      category: cat,
    }),
    wuArg(`EmailMilestoneTrigger${m}`, 'bool', { value: boolText(argBool(args.milestoneTrigger, false)), category: cat }),
    wuArg(`EmailMilestoneAutomationId${m}`, 'string', {
      value: argString(args.milestoneAutomationId),
      category: cat,
    }),
  ]
}

function meetingArgs(item: IndexedInstance, ctx: GenerationContext): WuArgument[] {
  const m = item.index
  const args = item.instance.arguments
  const cat = 'Create meeting invite'
  const recipientsName = ctx.hasEmailAndMeeting ? `ShowMeetingRecipients${m}` : `ShowRecipients${m}`
  const attachmentsName = ctx.hasEmailAndMeeting ? `ShowMeetingAttatchments${m}` : `ShowAttatchments${m}`
  const result: WuArgument[] = [
    wuArg(`ShowMeetingDialogue${m}`, 'bool', {
      comment: 'Do you want to show this meeting-invite step? (true/false)',
      value: boolText(argBool(args.showDialogue)),
      category: cat,
    }),
    wuArg(`MeetingActivityTitle${m}`, 'string', {
      comment: 'name of the activity',
      value: argString(args.activityTitle),
      category: cat,
    }),
    wuArg(recipientsName, 'bool', { value: boolText(argBool(args.showRecipients, false)), category: cat }),
    wuArg(attachmentsName, 'bool', { value: boolText(argBool(args.showAttachments, false)), category: cat }),
    wuArg(`MeetingMilestoneTrigger${m}`, 'bool', { value: boolText(argBool(args.milestoneTrigger, false)), category: cat }),
    wuArg(`MeetingMilestoneAutomationId${m}`, 'string', {
      value: argString(args.milestoneAutomationId),
      category: cat,
    }),
  ]

  const subject = argString(args.meetingSubject)
  const body = argString(args.meetingBody)
  if (subject) result.push(wuArg(`MeetingSubject${m}`, 'string', { value: subject, category: cat }))
  if (body) result.push(wuArg(`MeetingBody${m}`, 'string', { value: body, category: cat }))

  return result
}

function subprocessArgs(item: IndexedInstance): WuArgument[] {
  const k = item.index
  const args = item.instance.arguments
  const cat = `Subprocess ${k}`
  return [
    wuArg(`ShowSubProcessDialogue${k}`, 'bool', {
      comment: 'Do you want to show this subprocess step? (true/false)',
      value: boolText(argBool(args.showDialogue)),
      category: cat,
    }),
    wuArg(`SubProcessActivityTitle${k}`, 'string', {
      comment: 'name of the activity',
      value: argString(args.activityTitle),
      category: cat,
    }),
    wuArg(`SubProcessAutomationId${k}`, 'string', {
      value: argString(args.automationId),
      category: cat,
    }),
  ]
}

function openUrlArgs(item: IndexedInstance): WuArgument[] {
  const p = item.index
  const args = item.instance.arguments
  const cat = 'OpenURL'
  return [
    wuArg(`ShowOpenUrlDialogue${p}`, 'bool', {
      comment: 'Do you want to show this open-URL step? (true/false)',
      value: boolText(argBool(args.showDialogue)),
      category: cat,
    }),
    wuArg(`OpenUrlActivityTitle${p}`, 'string', {
      comment: 'name of the activity',
      value: argString(args.activityTitle),
      category: cat,
    }),
    wuArg(`OpenUrl${p}`, 'string', { value: argString(args.url), category: cat }),
  ]
}

function shareArgs(item: IndexedInstance): WuArgument[] {
  const r = item.index
  const args = item.instance.arguments
  const cat = 'Give assignment'
  return [
    wuArg(`ShowAssignmentDialogue${r}`, 'bool', {
      value: boolText(argBool(args.showDialogue)),
      category: cat,
    }),
    wuArg(`AssignmentActivityTitle${r}`, 'string', {
      comment: 'name of the activity',
      value: argString(args.activityTitle),
      category: cat,
    }),
    wuArg('ShowConnectedMilestoneDialogue1', 'bool', {
      value: boolText(argBool(args.showConnectedMilestone1)),
      category: cat,
    }),
    wuArg('ConnectedMilestoneActivityTitle1', 'string', {
      comment: 'name of the activity',
      value: argString(args.connectedMilestoneTitle1),
      category: cat,
    }),
    wuArg('ConnectedMilestoneAutomationId1', 'string', {
      value: argString(args.connectedMilestoneAutomationId1),
      category: cat,
    }),
    wuArg('ShowConnectedMilestoneDialogue2', 'bool', {
      value: boolText(argBool(args.showConnectedMilestone2)),
      category: cat,
    }),
    wuArg('ConnectedMilestoneActivityTitle2', 'string', {
      comment: 'name of the activity',
      value: argString(args.connectedMilestoneTitle2),
      category: cat,
    }),
    wuArg('ConnectedMilestoneAutomationId2', 'string', {
      value: argString(args.connectedMilestoneAutomationId2),
      category: cat,
    }),
  ]
}

function clientActionArgs(item: IndexedInstance): WuArgument[] {
  const c = item.index
  const args = item.instance.arguments
  const cat = 'Open Case Wizard'
  const showName = c === 1 ? 'ShowCaseWizardDialogue' : `ShowCaseWizardDialogue${c}`
  const titleName = c === 1 ? 'ActivityTitle' : `ActivityTitle${c}`
  const result: WuArgument[] = [
    wuArg(showName, 'bool', {
      value: boolText(argBool(args.showDialogue)),
      category: cat,
    }),
    wuArg(titleName, 'string', {
      comment: 'name of the activity',
      value: argString(args.activityTitle),
      category: cat,
    }),
  ]
  if (argBool(args.useLegacyClientAction, false)) {
    result.push(
      wuArg(c === 1 ? 'LegacyClientAction' : `LegacyClientAction${c}`, 'string', {
        value: argString(args.legacyClientAction),
        category: cat,
      }),
    )
  }
  return result
}

function checkpointArgs(item: IndexedInstance): WuArgument[] {
  const q = item.index
  const args = item.instance.arguments
  return [
    wuArg(`ShowCheckpointDialogue${q}`, 'bool', {
      comment: 'Do you want to show this checkpoint task? (true/false)',
      value: boolText(argBool(args.showDialogue)),
      category: 'Checkpoint',
    }),
    wuArg(`CheckpointActivityTitle${q}`, 'string', {
      comment: 'name of the activity',
      value: argString(args.activityTitle),
      category: 'Checkpoint',
    }),
  ]
}

function processTaskArgs(item: IndexedInstance): WuArgument[] {
  const args = item.instance.arguments
  return [
    wuArg(`ShowProcessTaskDialogue${item.index}`, 'bool', {
      value: boolText(argBool(args.showDialogue)),
      category: 'Process Task',
    }),
    wuArg('ActionTitle', 'string', {
      comment: 'name of the activity',
      value: argString(args.activityTitle),
      category: 'Process Task',
    }),
  ]
}

export function collectWuArguments(ctx: GenerationContext): WuArgument[] {
  const args: WuArgument[] = [wuArg('ProgressPlanId', 'string', { category: 'General' })]

  for (const item of ctx.phaseInstances) {
    switch (item.kind) {
      case 'MilestoneDialog':
        args.push(...milestoneArgs(item, ctx))
        break
      case 'DocumentFlowWizard':
        args.push(...documentArgs(item, ctx))
        break
      case 'SendEmailDialog':
        args.push(...emailArgs(item))
        break
      case 'MeetingInviteDialog':
        args.push(...meetingArgs(item, ctx))
        break
      case 'StartSubprocess':
        args.push(...subprocessArgs(item))
        break
      case 'OpenUrl':
        args.push(...openUrlArgs(item))
        break
      case 'ShareWithDialog':
        args.push(...shareArgs(item))
        break
      case 'ClientAction':
        args.push(...clientActionArgs(item))
        break
      case 'Checkpoint':
        args.push(...checkpointArgs(item))
        break
      case 'ProcessTask':
        args.push(...processTaskArgs(item))
        break
    }
  }

  return args
}

function renderWuArgument(arg: WuArgument): string {
  const attrs = [
    `name="${arg.name}"`,
    `type="${arg.type}"`,
    `category="${arg.category ?? 'General'}"`,
  ]
  if (arg.comment) attrs.push(`comment="${arg.comment}"`)

  if ((arg.type === 'bool' || arg.type === 'int') && arg.value !== undefined) {
    return `        <argument ${attrs.join(' ')}>${arg.value}</argument>`
  }

  if (arg.type === 'string' && arg.value) {
    return `        <argument ${attrs.join(' ')}>${escapeWuValue(arg.value)}</argument>`
  }

  return `        <argument ${attrs.join(' ')}/>`
}

function escapeWuValue(value: string): string {
  return value
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
}

export function generateWu(ctx: GenerationContext): string {
  const args = collectWuArguments(ctx)
  const argumentXml = args.map(renderWuArgument).join('\n')
  const categories =
    ctx.processProfile === 'background'
      ? `    <category>Background Process</category>
    <category>ProgressPlan Process</category>`
      : `    <category>ProgressPlan Process</category>
    <category>Stage Process</category>`

  const featureTogglesXml =
    ctx.featureToggles.length > 0
      ? `  <featuretoggles>
${ctx.featureToggles.map((t) => `    <featuretoggle>${escapeWuValue(t)}</featuretoggle>`).join('\n')}
  </featuretoggles>
`
      : ''

  return `<?xml version="1.0" encoding="utf-8"?>
<workUnit xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="..\\..\\WorkUnit.xsd"
    id="${ctx.workUnitId}"
    visibility="public"
    displayName="${escapeWuValue(ctx.displayName)}">
  <description>${escapeWuValue(ctx.displayName)}</description>
  <categories>
${categories}
  </categories>
${featureTogglesXml}  <executable>
    <wf startOption="application">
      <arguments>
${argumentXml}
      </arguments>
    </wf>
  </executable>
</workUnit>
`
}
