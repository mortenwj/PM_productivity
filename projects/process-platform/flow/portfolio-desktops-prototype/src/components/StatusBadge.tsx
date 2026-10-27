import type { Urgency } from '../types/portfolio'

const labels: Record<Urgency, string> = {
  overdue: 'Overdue',
  'due-soon': 'Due soon',
  'on-track': 'On track',
}

type StatusBadgeProps = {
  urgency: Urgency
}

export function StatusBadge({ urgency }: StatusBadgeProps) {
  return <span className={`badge badge-${urgency}`}>{labels[urgency]}</span>
}
