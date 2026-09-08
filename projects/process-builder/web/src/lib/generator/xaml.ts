import {
  argBool,
  argString,
  milestoneArgName,
  type GenerationContext,
  type IndexedInstance,
  type WuArgument,
} from './context'
import { collectWuArguments } from './wu'

function renderXamlMember(arg: WuArgument): string {
  let xamlType = 'InArgument(x:String)'
  if (arg.type === 'bool') xamlType = 'InArgument(x:Boolean)'
  if (arg.type === 'int') xamlType = 'InArgument(x:Int32)'
  return `    <x:Property Name="${arg.name}" Type="${xamlType}" />`
}

function docSuffix(item: IndexedInstance, ctx: GenerationContext): string {
  const pafSingle =
    ctx.namingScheme === 'paf-single' &&
    ctx.phaseInstances.filter((i) => i.kind === 'DocumentFlowWizard').length === 1
  return pafSingle ? '' : String(item.index)
}


function reviewBinding(item: IndexedInstance, ctx: GenerationContext, kind: 'Review' | 'Approval' | 'Dispatch'): string {
  const n = item.index
  if (ctx.namingScheme === 'hearing-style') {
    return `Do${kind}${n}`
  }
  const sfx = docSuffix(item, ctx)
  if (sfx) return `Create${kind}${sfx}`
  return `Create${kind}`
}

function milestoneXaml(item: IndexedInstance, ctx: GenerationContext): string {
  const show = milestoneArgName('ShowMilestoneDialogue', ctx, item.index)
  const title = milestoneArgName('MilestoneActivityTitle', ctx, item.index)
  const auto = milestoneArgName('MilestoneAutomationId', ctx, item.index)
  const label = ctx.milestoneCount === 1 && !milestoneArgName('ShowMilestoneDialogue', ctx, item.index).endsWith('1')
    ? '1'
    : String(item.index)
  return `                    <sbcpap:MilestoneDialog AllowFutureDatesOnly="{x:Null}" AllowPastDatesOnly="{x:Null}" RunWithoutDialog="{x:Null}" CustomMilestoneName="{x:Null}" CustomMilestoneNameAvailable="{x:Null}" DescriptionLocalizationId="{x:Null}" DialogDescription="{x:Null}" DialogDescriptionLocalizationId="{x:Null}" DialogTitleLocalizationId="{x:Null}" DocumentId="{x:Null}" GetMilestoneByWorkUnit="{x:Null}" MilestoneDate="{x:Null}" MilestoneProcessMark="{x:Null}" MilestoneStatus="{x:Null}" Notes="{x:Null}" OpenOnExistingProcessMark="{x:Null}" OrgUnitId="{x:Null}" OurRefId="{x:Null}" Description="[${title}]" DialogTitle="[${title}]" Disabled="[Not (${show})]" DisplayName="User: Milestone dialog ${label}" sap2010:WorkflowViewState.IdRef="MilestoneDialog_${item.index}" MilestoneConfigAutomationId="[${auto}]" MilestoneDropdownAvailable="[True]" ProcessModelId="[progressPlanInt]" StageId="[_stageId]" StatusDropdownAvailable="[True]" />`
}

function waitTaskBlock(item: IndexedInstance, ctx: GenerationContext): string {
  const reminder = ctx.wizardReminders.get(item.index)
  if (!reminder) return ''
  const sfx = docSuffix(item, ctx)
  const deadlineArg = sfx ? `DeadlineDays${sfx}` : `DeadlineDays${item.index}`
  const expiryGuid = argString(reminder.arguments.expiryWorkUnitGuid)
  const expiryAttr = expiryGuid
    ? ` WaitExpiredAction="${expiryGuid} =&gt; ${expiryGuid}"`
    : ''
  return `
                      <sbcpap:DocumentFlowWizard.RelatedWaitTask>
                        <sbcpap:WaitTask AccessGroupId="{x:Null}" ActivityCategoryId="{x:Null}" CompletedAction="{x:Null}" Notes="{x:Null}" OrgUnitId="{x:Null}" OurRefId="{x:Null}" TemplateId="{x:Null}" WaitDate="{x:Null}" Description="Response Deadline" DescriptionLocalizationId="{x:Null}" Disabled="{x:Null}" DisplayName="Response Deadline" sap2010:WorkflowViewState.IdRef="WaitTask_${item.index}" WaitDateCalculation="WorkDays" WaitDays="[Convert.ToInt32(${deadlineArg})]"${expiryAttr} />
                      </sbcpap:DocumentFlowWizard.RelatedWaitTask>`
}

function documentXaml(item: IndexedInstance, ctx: GenerationContext): string {
  const sfx = docSuffix(item, ctx)
  const title = sfx ? `DocumentActivityTitle${sfx}` : 'DocumentActivityTitle'
  const review = reviewBinding(item, ctx, 'Review')
  const approval = reviewBinding(item, ctx, 'Approval')
  const dispatch = reviewBinding(item, ctx, 'Dispatch')
  const archive = sfx ? `OutboundArchive${sfx}` : 'OutboundArchive'
  const category = sfx ? `OutboundCategory${sfx}` : 'OutboundCategory'
  const cc = sfx ? `CaseRoleCC${sfx}` : 'CaseRoleCC'
  const role = sfx ? `CaseRole${sfx}` : 'CaseRole'
  const template = sfx ? `DocumentTemplateId${sfx}` : 'DocumentTemplateId'
  const docTitle = sfx ? `DocumentTitle${sfx}` : 'DocumentTitle'
  const showDoc = sfx ? `ShowDocumentDialogue${sfx}` : 'ShowDocumentDialogue'
  const disabledAttr =
    ctx.namingScheme === 'hearing-style' ? '' : ` Disabled="[Not (${showDoc})]"`

  return `                    <sbcpap:DocumentFlowWizard DescriptionLocalizationId="{x:Null}" ErrorMessageLocalizedId="{x:Null}" ErrorMessageText="{x:Null}" GetDocBehavior="{x:Null}" NewDocumentAccessCodeAndLaw="{x:Null}" NewDocumentAccessGroup="{x:Null}" NewDocumentCopyRecipients="{x:Null}" NewDocumentCopyRecipientsContactCategory="{x:Null}" NewDocumentCopyRecipientsFromCaseRoles="[${cc}]" NewDocumentNotes="{x:Null}" NewDocumentProcessId="{x:Null}" NewDocumentProcessMark="{x:Null}" NewDocumentProject="{x:Null}" NewDocumentPublicTitle="{x:Null}" NewDocumentPublicTitleBehaviour="{x:Null}" NewDocumentRecipients="{x:Null}" NewDocumentRecipientsContactCategory="{x:Null}" NewDocumentResponsibleContact="{x:Null}" NewDocumentScreenContacts="{x:Null}" NewDocumentSendersReference="{x:Null}" Notes="{x:Null}" OnDialogCloseRunWorkUnitId="{x:Null}" OpenOnExistingCategory="{x:Null}" OpenOnExistingProcessMark="{x:Null}" OrgUnitId="{x:Null}" OurRefId="{x:Null}" RelatedWaitTask="{x:Null}" SearchOnCaseForExistingDocument="{x:Null}" SearchOnStageForExistingDocument="{x:Null}" RunWithoutDialog="{x:Null}" WizardCustomUrl="{x:Null}" Description="[${title}]"${disabledAttr} DisplayName="User: Document Flow - Wizard ${item.index}" sap2010:WorkflowViewState.IdRef="DocumentFlowWizard_${item.index}" NewDocumentArchive="[${archive}]" NewDocumentCase="[_caseId]" NewDocumentCategory="[${category}]" NewDocumentRecipientsFromCaseRoles="[${role}]" NewDocumentStageId="[_stageId]" NewDocumentTemplateId="[${template}]" NewDocumentTitle="[${docTitle}]" WizardTitle="[${title}]">${waitTaskBlock(item, ctx)}
                      <sbcpap:DocumentFlowWizard.RelatedPostExecutionActivities>
                        <sbcpap:DocumentFlowReview DocumentIDs="{x:Null}" DueDate="{x:Null}" DueDatePeriod="{x:Null}" GetDocByCategory="{x:Null}" GetDocByProcessMark="{x:Null}" GetDocByWorkUnit="{x:Null}" GetOnlyLatest="{x:Null}" Notes="{x:Null}" OnDialogCloseRunWorkUnitId="{x:Null}" OrgUnitId="{x:Null}" OurRefId="{x:Null}" RelatedWaitTask="{x:Null}" ProcessModelId="{x:Null}" StageID="{x:Null}" RunWithoutDialog="{x:Null}" WizardCustomUrl="{x:Null}" WizardTitle="{x:Null}" Description="do review" DescriptionLocalizationId="899D78C2-0984-4bc9-AE76-2C28CB52D37D" Disabled="[Not (${review})]" DisplayName="User: Document Flow - Review" sap2010:WorkflowViewState.IdRef="DocumentFlowReview_${item.index}" WorkflowType="50020" />
                        <sbcpap:DocumentFlowApproval DocumentIDs="{x:Null}" DueDate="{x:Null}" DueDatePeriod="{x:Null}" GetDocByCategory="{x:Null}" GetDocByProcessMark="{x:Null}" GetDocByWorkUnit="{x:Null}" GetOnlyLatest="{x:Null}" Notes="{x:Null}" OnDialogCloseRunWorkUnitId="{x:Null}" OrgUnitId="{x:Null}" OurRefId="{x:Null}" RelatedWaitTask="{x:Null}" ProcessModelId="{x:Null}" StageID="{x:Null}" RunWithoutDialog="{x:Null}" WizardCustomUrl="{x:Null}" WizardTitle="{x:Null}" Description="do approval" DescriptionLocalizationId="7A30FE68-E171-46de-A54E-73396FDAC13B" Disabled="[Not (${approval})]" DisplayName="User: Document Flow - Approval" sap2010:WorkflowViewState.IdRef="DocumentFlowApproval_${item.index}" WorkflowType="50021" />
                        <sbcpap:DocumentFlowDispatch GetDocBehavior="{x:Null}" GetDocByCategory="{x:Null}" GetDocById="{x:Null}" GetDocByProcessMark="{x:Null}" GetDocByStageId="{x:Null}" Notes="{x:Null}" OrgUnitId="{x:Null}" OurRefId="{x:Null}" RelatedWaitTask="{x:Null}" SearchOnCaseForExistingDocument="{x:Null}" SearchOnStageForExistingDocument="{x:Null}" Description="do dispatch" DescriptionLocalizationId="2EFCB113-8BB6-4D8E-B988-5191BDA23E0B" Disabled="[Not (${dispatch})]" DisplayName="User: Dispatch" sap2010:WorkflowViewState.IdRef="DocumentFlowDispatch_${item.index}" />
                      </sbcpap:DocumentFlowWizard.RelatedPostExecutionActivities>
                    </sbcpap:DocumentFlowWizard>`
}

function emailXaml(item: IndexedInstance): string {
  const m = item.index
  return `                    <sbcpap:SendEmailDialog DefaultAttachmentDocumentIds="{x:Null}" DefaultRecipientCaseRoles="{x:Null}" DefaultRecipientContactCategory="{x:Null}" DescriptionLocalizationId="{x:Null}" DialogDescription="{x:Null}" DialogDescriptionLocalizationId="{x:Null}" DialogTitle="{x:Null}" DialogTitleLocalizationId="{x:Null}" EmailBody="{x:Null}" EmailBodyLocalizationId="{x:Null}" EmailSubject="{x:Null}" EmailSubjectLocalizationId="{x:Null}" Notes="{x:Null}" OrgUnitId="{x:Null}" OurRefId="{x:Null}" RunWithoutDialog="{x:Null}" ContactsFromCaseAvailable="[ShowRecipients${m}]" Description="[EmailActivityTitle${m}]" Disabled="[Not (ShowEmailDialogue${m})]" DisplayName="Send Mail ${m}" EmailMessageTemplateRecno="[If(String.IsNullOrEmpty(EmailMessageTemplateRecno${m}), Nothing, CInt(EmailMessageTemplateRecno${m}))]" FileSelectionAvailable="[ShowAttatchments${m}]" sap2010:WorkflowViewState.IdRef="SendEmailDialog_${m}" ProcessModelId="[Integer.Parse(ProgressPlanId)]" ShowAllFilesOnAllStagesByDefault="[ShowAttatchments${m}]" StageId="[_stageId]">
                      <sbcpap:SendEmailDialog.RelatedPostExecutionActivities>
                        <sbcpap:MilestoneDialog AllowFutureDatesOnly="{x:Null}" AllowPastDatesOnly="{x:Null}" CustomMilestoneName="{x:Null}" CustomMilestoneNameAvailable="{x:Null}" DialogDescription="{x:Null}" DialogDescriptionLocalizationId="{x:Null}" DialogTitleLocalizationId="{x:Null}" DocumentId="{x:Null}" GetMilestoneByWorkUnit="{x:Null}" MilestoneDate="{x:Null}" MilestoneProcessMark="{x:Null}" MilestoneStatus="{x:Null}" Notes="{x:Null}" OpenOnExistingProcessMark="{x:Null}" OrgUnitId="{x:Null}" OurRefId="{x:Null}" StatusDropdownAvailable="{x:Null}" RunWithoutDialog="[True]" Description="trigger milestone" DescriptionLocalizationId="[EmailMilestoneAutomationId${m}]" DialogTitle="trigger milestone" Disabled="[Not (EmailMilestoneTrigger${m})]" DisplayName="User: Milestone dialog" sap2010:WorkflowViewState.IdRef="MilestoneDialog_email_${m}" MilestoneConfigAutomationId="[EmailMilestoneAutomationId${m}]" MilestoneDropdownAvailable="[False]" ProcessModelId="[progressPlanInt]" StageId="[_stageId]" />
                      </sbcpap:SendEmailDialog.RelatedPostExecutionActivities>
                    </sbcpap:SendEmailDialog>`
}

function meetingXaml(item: IndexedInstance, ctx: GenerationContext): string {
  const m = item.index
  const args = item.instance.arguments
  const recipients = ctx.hasEmailAndMeeting ? `ShowMeetingRecipients${m}` : `ShowRecipients${m}`
  const attachments = ctx.hasEmailAndMeeting ? `ShowMeetingAttatchments${m}` : `ShowAttatchments${m}`
  const contactsBinding = `[${recipients} And ${attachments}]`
  const subjectBinding = argString(args.meetingSubject)
    ? `[MeetingSubject${m}]`
    : `[MeetingActivityTitle${m}]`
  const bodyAttr = argString(args.meetingBody)
    ? ` MeetingBody="[MeetingBody${m}]"`
    : ` MeetingBody="{x:Null}"`

  return `                    <sbcpap:MeetingInviteDialog DefaultAttachmentDocumentIds="{x:Null}" DefaultRecipientCaseRoles="{x:Null}" DefaultRecipientContactCategory="{x:Null}" DescriptionLocalizationId="{x:Null}" DialogDescription="{x:Null}" DialogDescriptionLocalizationId="{x:Null}" DialogTitle="{x:Null}" DialogTitleLocalizationId="{x:Null}" MeetingBodyLocalizationId="{x:Null}" MeetingSubject="${subjectBinding}" MeetingSubjectLocalizationId="{x:Null}" Notes="{x:Null}" OrgUnitId="{x:Null}" OurRefId="{x:Null}" RunWithoutDialog="{x:Null}" ContactsFromCaseAvailable="${contactsBinding}" Description="[MeetingActivityTitle${m}]" Disabled="[Not (ShowMeetingDialogue${m})]" DisplayName="Meeting invite ${m}" FileSelectionAvailable="[${attachments}]" sap2010:WorkflowViewState.IdRef="MeetingInviteDialog_${m}" ProcessModelId="[Integer.Parse(ProgressPlanId)]" ShowAllFilesOnAllStagesByDefault="[${attachments}]" StageId="[_stageId]"${bodyAttr}>
                      <sbcpap:MeetingInviteDialog.RelatedPostExecutionActivities>
                        <sbcpap:MilestoneDialog AllowFutureDatesOnly="{x:Null}" AllowPastDatesOnly="{x:Null}" CustomMilestoneName="{x:Null}" CustomMilestoneNameAvailable="{x:Null}" DialogDescription="{x:Null}" DialogDescriptionLocalizationId="{x:Null}" DialogTitleLocalizationId="{x:Null}" DocumentId="{x:Null}" GetMilestoneByWorkUnit="{x:Null}" MilestoneDate="{x:Null}" MilestoneProcessMark="{x:Null}" MilestoneStatus="{x:Null}" Notes="{x:Null}" OpenOnExistingProcessMark="{x:Null}" OrgUnitId="{x:Null}" OurRefId="{x:Null}" StatusDropdownAvailable="{x:Null}" RunWithoutDialog="[True]" Description="trigger milestone" DescriptionLocalizationId="[MeetingMilestoneAutomationId${m}]" DialogTitle="trigger milestone" Disabled="[Not (MeetingMilestoneTrigger${m})]" DisplayName="User: Milestone dialog" sap2010:WorkflowViewState.IdRef="MilestoneDialog_meeting_${m}" MilestoneConfigAutomationId="[MeetingMilestoneAutomationId${m}]" MilestoneDropdownAvailable="[False]" ProcessModelId="[progressPlanInt]" StageId="[_stageId]" />
                      </sbcpap:MeetingInviteDialog.RelatedPostExecutionActivities>
                    </sbcpap:MeetingInviteDialog>`
}

function subprocessXaml(item: IndexedInstance): string {
  const k = item.index
  return `                    <sbcpap:ProcessDialog DeadlineDays="{x:Null}" DescriptionLocalizationId="{x:Null}" DialogDescription="{x:Null}" DialogDescriptionLocalizationId="{x:Null}" DialogTitleLocalizationId="{x:Null}" Notes="{x:Null}" OpenOnExistingProcessMark="{x:Null}" OrgUnitId="{x:Null}" OurRefId="{x:Null}" ProcessProcessMark="{x:Null}" ResponsibleOrgUnitRecno="{x:Null}" ResponsiblePersonRecno="{x:Null}" RunWithoutDialog="[True]" CustomTitle="[SubProcessActivityTitle${k}]" Description="[SubProcessActivityTitle${k}]" DialogTitle="[SubProcessActivityTitle${k}]" Disabled="[Not (ShowSubProcessDialogue${k})]" DisplayName="Start subprocess ${k}" sap2010:WorkflowViewState.IdRef="ProcessDialog_${k}" ParentProgressPlanRecno="[progressPlanInt]" ProcessConfigAutomationId="[SubProcessAutomationId${k}]" ProcessDropdownAvailable="[False]" ProcessModelId="[progressPlanInt]" StageRecno="[_stageId]" />`
}

function openUrlXaml(item: IndexedInstance): string {
  const p = item.index
  return `                    <sbcpap:OpenUrl AccessGroupId="{x:Null}" ActivityCategoryId="{x:Null}" DescriptionLocalizationId="{x:Null}" Notes="{x:Null}" OrgUnitId="{x:Null}" OurRefId="{x:Null}" RelatedWaitTask="{x:Null}" UrlWorkUnit="{x:Null}" Description="[OpenUrlActivityTitle${p}]" Disabled="[Not (ShowOpenUrlDialogue${p})]" DisplayName="Open URL" sap2010:WorkflowViewState.IdRef="OpenUrl_${p}" UrlManually="[OpenUrl${p}]">
                      <sbcpap:OpenUrl.CloseActivityWhenClicked>
                        <InArgument x:TypeArguments="s:Nullable(x:Boolean)">
                          <Literal x:TypeArguments="s:Nullable(x:Boolean)" Value="True" />
                        </InArgument>
                      </sbcpap:OpenUrl.CloseActivityWhenClicked>
                    </sbcpap:OpenUrl>`
}

function shareXaml(item: IndexedInstance): string {
  const r = item.index
  return `                    <sbcpap:ShareWithDialog DefaultNotes="{x:Null}" DefaultNotesLocalizationId="{x:Null}" DescriptionLocalizationId="{x:Null}" DialogTitle="{x:Null}" DialogTitleLocalizationId="{x:Null}" Notes="{x:Null}" OrgUnitId="{x:Null}" OurRefId="{x:Null}" RelatedWaitTask="{x:Null}" Description="[AssignmentActivityTitle${r}]" Disabled="[Not (ShowAssignmentDialogue${r})]" DisplayName="User: Share with ${r}" sap2010:WorkflowViewState.IdRef="ShareWithDialog_${r}">
                      <sbcpap:ShareWithDialog.RelatedPostExecutionActivities>
                        <sbcpap:MilestoneDialog AllowFutureDatesOnly="{x:Null}" AllowPastDatesOnly="{x:Null}" CustomMilestoneName="{x:Null}" CustomMilestoneNameAvailable="{x:Null}" DescriptionLocalizationId="{x:Null}" DialogDescription="{x:Null}" DialogDescriptionLocalizationId="{x:Null}" DialogTitleLocalizationId="{x:Null}" DocumentId="{x:Null}" GetMilestoneByWorkUnit="{x:Null}" MilestoneDate="{x:Null}" MilestoneProcessMark="{x:Null}" MilestoneStatus="{x:Null}" Notes="{x:Null}" OpenOnExistingProcessMark="{x:Null}" OrgUnitId="{x:Null}" OurRefId="{x:Null}" Description="[ConnectedMilestoneActivityTitle1]" DialogTitle="[ConnectedMilestoneActivityTitle1]" Disabled="[Not (ShowConnectedMilestoneDialogue1)]" DisplayName="User: Milestone dialog (auto)" sap2010:WorkflowViewState.IdRef="MilestoneDialog_share_${r}_1" MilestoneConfigAutomationId="[ConnectedMilestoneAutomationId1]" MilestoneDropdownAvailable="[True]" ProcessModelId="[progressPlanInt]" RunWithoutDialog="[True]" StageId="[_stageId]" StatusDropdownAvailable="[True]" />
                        <sbcpap:MilestoneDialog AllowFutureDatesOnly="{x:Null}" AllowPastDatesOnly="{x:Null}" CustomMilestoneName="{x:Null}" CustomMilestoneNameAvailable="{x:Null}" DescriptionLocalizationId="{x:Null}" DialogDescription="{x:Null}" DialogDescriptionLocalizationId="{x:Null}" DialogTitleLocalizationId="{x:Null}" DocumentId="{x:Null}" GetMilestoneByWorkUnit="{x:Null}" MilestoneDate="{x:Null}" MilestoneProcessMark="{x:Null}" MilestoneStatus="{x:Null}" Notes="{x:Null}" OpenOnExistingProcessMark="{x:Null}" OrgUnitId="{x:Null}" OurRefId="{x:Null}" Description="[ConnectedMilestoneActivityTitle2]" DialogTitle="[ConnectedMilestoneActivityTitle2]" Disabled="[Not (ShowConnectedMilestoneDialogue2)]" DisplayName="User: Milestone dialog (manual)" sap2010:WorkflowViewState.IdRef="MilestoneDialog_share_${r}_2" MilestoneConfigAutomationId="[ConnectedMilestoneAutomationId2]" MilestoneDropdownAvailable="[True]" ProcessModelId="[progressPlanInt]" RunWithoutDialog="[False]" StageId="[_stageId]" StatusDropdownAvailable="[True]" />
                      </sbcpap:ShareWithDialog.RelatedPostExecutionActivities>
                    </sbcpap:ShareWithDialog>`
}

function clientActionXaml(item: IndexedInstance): string {
  const c = item.index
  const args = item.instance.arguments
  const showName = c === 1 ? 'ShowCaseWizardDialogue' : `ShowCaseWizardDialogue${c}`
  const titleName = c === 1 ? 'ActivityTitle' : `ActivityTitle${c}`
  const clientIdAttr = argBool(args.useLegacyClientAction, false)
    ? `ClientActionId="[${c === 1 ? 'LegacyClientAction' : `LegacyClientAction${c}`}]"`
    : 'ClientActionId="19"'
  return `                    <sbcpap:ClientAction AccessGroupId="{x:Null}" ActivityCategoryId="{x:Null}" DescriptionLocalizationId="{x:Null}" Notes="{x:Null}" OrgUnitId="{x:Null}" OurRefId="{x:Null}" RelatedWaitTask="{x:Null}" TemplateOrGroupId="{x:Null}" ${clientIdAttr} Description="[${titleName}]" Disabled="[Not (${showName})]" DisplayName="Client action - Case Wizard" sap2010:WorkflowViewState.IdRef="ClientAction_${c}" />`
}

function checkpointXaml(item: IndexedInstance): string {
  const q = item.index
  return `                    <sbcpap:Task AccessGroupId="{x:Null}" ActivityCategoryId="{x:Null}" Date="{x:Null}" DescriptionLocalizationId="{x:Null}" Disabled="[Not (ShowCheckpointDialogue${q})]" Notes="{x:Null}" OrgUnitId="{x:Null}" OurRefId="{x:Null}" Description="[CheckpointActivityTitle${q}]" DisplayName="Checkpoint" sap2010:WorkflowViewState.IdRef="Task_checkpoint_${q}" />`
}

function processTaskXaml(item: IndexedInstance): string {
  const n = item.index
  return `                    <sbcpap:Task AccessGroupId="{x:Null}" ActivityCategoryId="{x:Null}" Date="{x:Null}" DescriptionLocalizationId="{x:Null}" Disabled="[Not (ShowProcessTaskDialogue${n})]" Notes="{x:Null}" OrgUnitId="{x:Null}" OurRefId="{x:Null}" Description="[ActionTitle]" DisplayName="Task" sap2010:WorkflowViewState.IdRef="Task_${n}" />`
}

function renderPhaseActivity(item: IndexedInstance, ctx: GenerationContext): string {
  switch (item.kind) {
    case 'MilestoneDialog':
      return milestoneXaml(item, ctx)
    case 'DocumentFlowWizard':
      return documentXaml(item, ctx)
    case 'SendEmailDialog':
      return emailXaml(item)
    case 'MeetingInviteDialog':
      return meetingXaml(item, ctx)
    case 'StartSubprocess':
      return subprocessXaml(item)
    case 'OpenUrl':
      return openUrlXaml(item)
    case 'ShareWithDialog':
      return shareXaml(item)
    case 'ClientAction':
      return clientActionXaml(item)
    case 'Checkpoint':
      return checkpointXaml(item)
    case 'ProcessTask':
      return processTaskXaml(item)
    default:
      return ''
  }
}

function phaseDeadlineAttrs(ctx: GenerationContext): { deadline: string; warning: string } {
  return {
    deadline: ctx.phaseDeadlineDays
      ? `DeadlineInDays="[${ctx.phaseDeadlineDays}]"`
      : 'DeadlineInDays="{x:Null}"',
    warning: ctx.phaseWarningDays
      ? `WarningInDays="[${ctx.phaseWarningDays}]"`
      : 'WarningInDays="{x:Null}"',
  }
}

export function generateXaml(ctx: GenerationContext): string {
  const wuArgs = collectWuArguments(ctx)
  const members = wuArgs.map(renderXamlMember).join('\n')
  const phaseActivities = ctx.phaseInstances.map((item) => renderPhaseActivity(item, ctx)).join('\n')
  const openUrlNs = ctx.hasOpenUrl
    ? '\n xmlns:s="clr-namespace:System;assembly=mscorlib"'
    : ''

  const shellBlock = ctx.useMinimalShell
    ? ''
    : `            <sbcpa:GetCurrentStageId DisplayName="System: Get Current Stage Id" sap2010:WorkflowViewState.IdRef="GetCurrentStageId_1" ProgressPlanId="[progressPlanInt]" Result="[_stageId]" />
            <sbcpa:GetCurrentCaseId DisplayName="System: Get Current Case Id" sap2010:WorkflowViewState.IdRef="GetCurrentCaseId_1" ProgressPlanId="[progressPlanInt]" Result="[_caseId]" />`

  const stateMachineVars = ctx.useMinimalShell
    ? ''
    : `    <StateMachine.Variables>
      <Variable x:TypeArguments="x:Int32" Name="_caseId" />
      <Variable x:TypeArguments="x:Int32" Name="_stageId" />
    </StateMachine.Variables>`

  const phaseAttrs = phaseDeadlineAttrs(ctx)

  return `<Activity mc:Ignorable="sap sap2010 sads" x:Class="${ctx.className}"
 xmlns="http://schemas.microsoft.com/netfx/2009/xaml/activities"
 xmlns:av="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
 xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
 xmlns:sads="http://schemas.microsoft.com/netfx/2010/xaml/activities/debugger"
 xmlns:sap="http://schemas.microsoft.com/netfx/2009/xaml/activities/presentation"
 xmlns:sap2010="http://schemas.microsoft.com/netfx/2010/xaml/activities/presentation"
 xmlns:sbcpa="clr-namespace:SI.Biz.Core.ProcessEngine.Activities;assembly=SI.Biz.Core.ProcessEngine.Activities"
 xmlns:sbcpap="clr-namespace:SI.Biz.Core.ProcessEngine.Activities.ProgressPlan;assembly=SI.Biz.Core.ProcessEngine.Activities"
 xmlns:scg="clr-namespace:System.Collections.Generic;assembly=mscorlib"
 xmlns:sco="clr-namespace:System.Collections.ObjectModel;assembly=mscorlib"
 xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"${openUrlNs}>
  <x:Members>
${members}
  </x:Members>
  <sap2010:WorkflowViewState.IdRef>Activity1_1</sap2010:WorkflowViewState.IdRef>
  <TextExpression.NamespacesForImplementation>
    <sco:Collection x:TypeArguments="x:String">
      <x:String>System</x:String>
      <x:String>System.Collections.Generic</x:String>
      <x:String>System.Data</x:String>
      <x:String>System.Linq</x:String>
      <x:String>System.Text</x:String>
      <x:String>System.Activities</x:String>
      <x:String>SI.Biz.Core.ProcessEngine.Support</x:String>
    </sco:Collection>
  </TextExpression.NamespacesForImplementation>
  <TextExpression.ReferencesForImplementation>
    <sco:Collection x:TypeArguments="AssemblyReference">
      <AssemblyReference>mscorlib</AssemblyReference>
      <AssemblyReference>System</AssemblyReference>
      <AssemblyReference>System.Core</AssemblyReference>
      <AssemblyReference>System.Data</AssemblyReference>
      <AssemblyReference>System.ServiceModel</AssemblyReference>
      <AssemblyReference>System.Xml</AssemblyReference>
      <AssemblyReference>System.Activities</AssemblyReference>
      <AssemblyReference>System.ComponentModel.Composition</AssemblyReference>
      <AssemblyReference>SI.Biz.Core.ProcessEngine.Support</AssemblyReference>
    </sco:Collection>
  </TextExpression.ReferencesForImplementation>
  <StateMachine DisplayName="${ctx.displayName}" sap2010:WorkflowViewState.IdRef="StateMachine_1">
    <StateMachine.InitialState>
      <State x:Name="__ReferenceID0" DisplayName="Startphase" sap2010:WorkflowViewState.IdRef="State_1">
        <State.Entry>
          <Sequence sap2010:WorkflowViewState.IdRef="Sequence_1">
            <Sequence.Variables>
              <Variable x:TypeArguments="x:Int32" Name="progressPlanInt" />
            </Sequence.Variables>
            <Assign DisplayName="System: Parse Progress Plan Id" sap2010:WorkflowViewState.IdRef="Assign_1">
              <Assign.To>
                <OutArgument x:TypeArguments="x:Int32">[progressPlanInt]</OutArgument>
              </Assign.To>
              <Assign.Value>
                <InArgument x:TypeArguments="x:Int32">[Integer.Parse(ProgressPlanId)]</InArgument>
              </Assign.Value>
            </Assign>
${shellBlock}
            <sbcpap:PhaseContainer DisplayName="Phase container" sap2010:WorkflowViewState.IdRef="PhaseContainer_1" ProgressPlanId="[ProgressPlanId]">
              <sbcpap:PhaseContainer.Phases>
                <sbcpap:Phase ActivityCategoryId="{x:Null}" Complexity="{x:Null}" DeadlineAction="{x:Null}" ${phaseAttrs.deadline} IsFinalPhase="{x:Null}" Notes="{x:Null}" WarningAction="{x:Null}" ${phaseAttrs.warning} AutoCloseActivitiesWhenPhaseIsClosed="False" CalculateOnActivation="False" Description="${ctx.displayName}" DisplayName="Phase" sap2010:WorkflowViewState.IdRef="Phase_1" ReuseOnLoop="False">
                  <sbcpap:Phase.PhaseActivities>
${phaseActivities}
                  </sbcpap:Phase.PhaseActivities>
                  <sbcpap:Phase.Variables>
                    <sco:Collection x:TypeArguments="Variable" />
                  </sbcpap:Phase.Variables>
                </sbcpap:Phase>
              </sbcpap:PhaseContainer.Phases>
              <sbcpap:PhaseContainer.Variables>
                <sco:Collection x:TypeArguments="Variable" />
              </sbcpap:PhaseContainer.Variables>
            </sbcpap:PhaseContainer>
          </Sequence>
        </State.Entry>
        <State.Transitions>
          <Transition DisplayName="T1" sap2010:WorkflowViewState.IdRef="Transition_1">
            <Transition.To>
              <State x:Name="__ReferenceID1" DisplayName="FinalState" sap2010:WorkflowViewState.IdRef="State_2" IsFinal="True" />
            </Transition.To>
          </Transition>
        </State.Transitions>
      </State>
    </StateMachine.InitialState>
    <x:Reference>__ReferenceID0</x:Reference>
    <x:Reference>__ReferenceID1</x:Reference>
${stateMachineVars}
  </StateMachine>
</Activity>
`
}
