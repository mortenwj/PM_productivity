import { portfolioCases } from '../data/mockPortfolio'
import { StatusBadge } from '../components/StatusBadge'

type CaseDetailScreenProps = {
  caseId: string
  onBack: () => void
}

export function CaseDetailScreen({ caseId, onBack }: CaseDetailScreenProps) {
  const item = portfolioCases.find((c) => c.id === caseId)

  if (!item) {
    return (
      <div className="screen">
        <button type="button" className="ghost-btn" onClick={onBack}>
          ← Back
        </button>
        <p>Case not found.</p>
      </div>
    )
  }

  return (
    <div className="screen">
      <button type="button" className="ghost-btn back-btn" onClick={onBack}>
        ← Back to portfolio
      </button>

      <header className="detail-header">
        <div>
          <p className="case-id">{item.id}</p>
          <h1>{item.title}</h1>
          <p className="meta">{item.municipality}</p>
        </div>
        <StatusBadge urgency={item.urgency} />
      </header>

      <div className="detail-grid">
        <section className="panel">
          <h2>Process context</h2>
          <dl className="detail-list">
            <div>
              <dt>Process model</dt>
              <dd>{item.processModel}</dd>
            </div>
            <div>
              <dt>Current phase</dt>
              <dd>{item.phase}</dd>
            </div>
            <div>
              <dt>Days in phase</dt>
              <dd>{item.daysInPhase}</dd>
            </div>
            <div>
              <dt>Deadline</dt>
              <dd>{item.deadline}</dd>
            </div>
            <div>
              <dt>Assignee</dt>
              <dd>{item.assignee}</dd>
            </div>
          </dl>
        </section>

        <section className="panel">
          <h2>Manager actions (prototype)</h2>
          <p className="panel-note">
            Placeholder for follow-up, reassignment, and escalation — not wired in v0.
          </p>
          <div className="action-row">
            <button type="button" className="primary-btn">
              Mark follow-up
            </button>
            <button type="button" className="ghost-btn">
              Reassign
            </button>
            <button type="button" className="ghost-btn">
              Open ProcessView
            </button>
          </div>
        </section>
      </div>
    </div>
  )
}
