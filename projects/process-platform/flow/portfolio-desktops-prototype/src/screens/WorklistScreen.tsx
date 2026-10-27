import { useMemo, useState } from 'react'
import { phases, portfolioCases, processModels } from '../data/mockPortfolio'
import type { PortfolioCase } from '../types/portfolio'
import { StatusBadge } from '../components/StatusBadge'

type WorklistScreenProps = {
  onOpenCase: (caseId: string) => void
}

type UrgencyFilter = 'all' | 'overdue' | 'due-soon' | 'follow-up'

export function WorklistScreen({ onOpenCase }: WorklistScreenProps) {
  const [processFilter, setProcessFilter] = useState<string>('all')
  const [phaseFilter, setPhaseFilter] = useState<string>('all')
  const [urgencyFilter, setUrgencyFilter] = useState<UrgencyFilter>('all')

  const filtered = useMemo(() => {
    return portfolioCases
      .filter((c) => c.phase !== 'Closed')
      .filter((c) => processFilter === 'all' || c.processModel === processFilter)
      .filter((c) => phaseFilter === 'all' || c.phase === phaseFilter)
      .filter((c) => {
        if (urgencyFilter === 'all') return true
        if (urgencyFilter === 'follow-up') return Boolean(c.followUp)
        return c.urgency === urgencyFilter
      })
      .sort((a, b) => urgencyRank(a) - urgencyRank(b))
  }, [processFilter, phaseFilter, urgencyFilter])

  return (
    <div className="screen">
      <header className="screen-header">
        <div>
          <h1>Manager worklist</h1>
          <p className="lede">
            Prioritise cases by deadline, phase, and follow-up — prototype for ADO #411634.
          </p>
        </div>
        <div className="stat-strip">
          <Stat label="In queue" value={filtered.length} />
          <Stat
            label="Overdue"
            value={filtered.filter((c) => c.urgency === 'overdue').length}
            tone="danger"
          />
          <Stat
            label="Follow-up"
            value={filtered.filter((c) => c.followUp).length}
            tone="accent"
          />
        </div>
      </header>

      <section className="filter-bar">
        <FilterSelect
          label="Process model"
          value={processFilter}
          onChange={setProcessFilter}
          options={['all', ...processModels]}
        />
        <FilterSelect
          label="Phase"
          value={phaseFilter}
          onChange={setPhaseFilter}
          options={['all', ...phases.filter((p) => p !== 'Closed')]}
        />
        <div className="chip-group" role="group" aria-label="Urgency">
          {(
            [
              ['all', 'All'],
              ['overdue', 'Overdue'],
              ['due-soon', 'Due soon'],
              ['follow-up', 'Follow-up'],
            ] as const
          ).map(([value, label]) => (
            <button
              key={value}
              type="button"
              className={urgencyFilter === value ? 'chip active' : 'chip'}
              onClick={() => setUrgencyFilter(value)}
            >
              {label}
            </button>
          ))}
        </div>
      </section>

      <div className="table-wrap">
        <table className="data-table">
          <thead>
            <tr>
              <th>Case</th>
              <th>Process / phase</th>
              <th>Assignee</th>
              <th>Deadline</th>
              <th>Status</th>
              <th />
            </tr>
          </thead>
          <tbody>
            {filtered.map((item) => (
              <tr key={item.id} className={item.followUp ? 'row-follow-up' : undefined}>
                <td>
                  <button type="button" className="link-btn" onClick={() => onOpenCase(item.id)}>
                    <span className="case-id">{item.id}</span>
                    <span className="case-title">{item.title}</span>
                  </button>
                  <span className="meta">{item.municipality}</span>
                </td>
                <td>
                  <span className="stack-text">{item.processModel}</span>
                  <span className="meta">{item.phase}</span>
                </td>
                <td>{item.assignee}</td>
                <td>
                  {item.deadline}
                  <span className="meta">{item.daysInPhase}d in phase</span>
                </td>
                <td>
                  <StatusBadge urgency={item.urgency} />
                  {item.followUp && <span className="follow-flag">Follow-up</span>}
                </td>
                <td>
                  <button type="button" className="ghost-btn" onClick={() => onOpenCase(item.id)}>
                    Open
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}

function urgencyRank(item: PortfolioCase) {
  if (item.urgency === 'overdue') return 0
  if (item.urgency === 'due-soon') return 1
  return 2
}

function Stat({
  label,
  value,
  tone,
}: {
  label: string
  value: number
  tone?: 'danger' | 'accent'
}) {
  return (
    <div className={tone ? `mini-stat mini-stat-${tone}` : 'mini-stat'}>
      <span className="mini-stat-value">{value}</span>
      <span className="mini-stat-label">{label}</span>
    </div>
  )
}

function FilterSelect({
  label,
  value,
  onChange,
  options,
}: {
  label: string
  value: string
  onChange: (value: string) => void
  options: readonly string[]
}) {
  return (
    <label className="filter-select">
      <span>{label}</span>
      <select value={value} onChange={(e) => onChange(e.target.value)}>
        {options.map((option) => (
          <option key={option} value={option}>
            {option === 'all' ? 'All' : option}
          </option>
        ))}
      </select>
    </label>
  )
}
