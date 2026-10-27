export type ProcessPhase =
  | 'Registration'
  | 'Processing'
  | 'Consultation'
  | 'Decision'
  | 'Appeal'
  | 'Closed'

export type Urgency = 'overdue' | 'due-soon' | 'on-track'

export type PortfolioCase = {
  id: string
  title: string
  processModel: string
  phase: ProcessPhase
  assignee: string
  deadline: string
  daysInPhase: number
  urgency: Urgency
  followUp?: boolean
  municipality: string
}

export type PhaseMetric = {
  phase: ProcessPhase
  openCases: number
  overdue: number
  avgDaysInPhase: number
}

export type ScreenId = 'worklist' | 'portfolio' | 'reporting' | 'case-detail'
