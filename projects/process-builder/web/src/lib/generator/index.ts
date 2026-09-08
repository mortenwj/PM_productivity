import type { ProcessDefinition } from '../../types/process'
import { buildGenerationContext, resolveProcessComponents, toClassName } from './context'
import { generateWu } from './wu'
import { generateXaml } from './xaml'

export interface WorkUnitPair {
  basename: string
  className: string
  workUnitId: string
  wu: string
  xaml: string
}

export type GenerationErrorCode =
  | 'NAME_REQUIRED'
  | 'NO_COMPONENTS'
  | 'BACKGROUND_UNSUPPORTED'
  | 'ORPHAN_REMINDER'

export interface GenerationError {
  code: GenerationErrorCode
  message: string
}

export type GenerationResult =
  | { ok: true; pair: WorkUnitPair }
  | { ok: false; error: GenerationError }

export function generateWorkUnitPair(process: ProcessDefinition): GenerationResult {
  if (!process.name.trim()) {
    return { ok: false, error: { code: 'NAME_REQUIRED', message: 'Process name is required' } }
  }

  if (process.components.length === 0) {
    return {
      ok: false,
      error: { code: 'NO_COMPONENTS', message: 'Add at least one component to the process canvas' },
    }
  }

  if (process.processProfile === 'background') {
    return {
      ok: false,
      error: {
        code: 'BACKGROUND_UNSUPPORTED',
        message:
          'Background process generation is not yet supported in Process Builder. Use progress-plan profile.',
      },
    }
  }

  const ctx = buildGenerationContext(process)

  const { wizardReminders } = resolveProcessComponents(process.components)
  const reminderInstances = process.components.filter((c) => c.kind === 'DocumentReminder')
  const mappedReminderIds = new Set(Array.from(wizardReminders.values()).map((r) => r.id))
  const orphanReminder = reminderInstances.find((r) => !mappedReminderIds.has(r.id))
  if (orphanReminder) {
    return {
      ok: false,
      error: {
        code: 'ORPHAN_REMINDER',
        message:
          'Document response deadline must follow a document flow wizard in the canvas (no preceding wizard found).',
      },
    }
  }

  const basename = toClassName(process.name)

  return {
    ok: true,
    pair: {
      basename,
      className: ctx.className,
      workUnitId: ctx.workUnitId,
      wu: generateWu(ctx),
      xaml: generateXaml(ctx),
    },
  }
}
