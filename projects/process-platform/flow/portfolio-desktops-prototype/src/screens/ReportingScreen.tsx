import { phaseMetrics, reportingSummary } from '../data/mockPortfolio'

export function ReportingScreen() {
  const maxOpen = Math.max(...phaseMetrics.map((m) => m.openCases))

  return (
    <div className="screen">
      <header className="screen-header">
        <div>
          <h1>Process reporting</h1>
          <p className="lede">
            Operational snapshot across open cases — filtering and follow-up depth TBD with NVE.
          </p>
        </div>
      </header>

      <section className="kpi-row">
        <KpiCard label="Open cases" value={reportingSummary.totalOpen} />
        <KpiCard label="Overdue" value={reportingSummary.overdue} tone="danger" />
        <KpiCard label="Due this week" value={reportingSummary.dueThisWeek} tone="warn" />
        <KpiCard label="Marked follow-up" value={reportingSummary.followUps} tone="accent" />
        <KpiCard
          label="Avg days to decision"
          value={reportingSummary.avgDaysToDecision}
          suffix="d"
        />
      </section>

      <section className="report-panels">
        <div className="panel">
          <h2>Open cases by phase</h2>
          <ul className="bar-chart">
            {phaseMetrics
              .filter((m) => m.phase !== 'Closed')
              .map((metric) => (
                <li key={metric.phase}>
                  <div className="bar-label">
                    <span>{metric.phase}</span>
                    <span>{metric.openCases}</span>
                  </div>
                  <div className="bar-track">
                    <div
                      className="bar-fill"
                      style={{ width: `${(metric.openCases / maxOpen) * 100}%` }}
                    />
                  </div>
                  <span className="bar-sub">
                    {metric.overdue} overdue · avg {metric.avgDaysInPhase}d in phase
                  </span>
                </li>
              ))}
          </ul>
        </div>

        <div className="panel">
          <h2>Reporting questions for next iteration</h2>
          <ul className="question-list">
            <li>Which milestones drive manager alerts vs case-worker tasks?</li>
            <li>Do managers need export (Excel/PDF) or live desktop widgets?</li>
            <li>Should reporting slice by process model, municipality, or program?</li>
            <li>How does this relate to existing Plan&amp;Build deadline webparts?</li>
          </ul>
        </div>
      </section>
    </div>
  )
}

function KpiCard({
  label,
  value,
  suffix,
  tone,
}: {
  label: string
  value: number
  suffix?: string
  tone?: 'danger' | 'warn' | 'accent'
}) {
  return (
    <div className={tone ? `kpi-card kpi-${tone}` : 'kpi-card'}>
      <span className="kpi-value">
        {value}
        {suffix}
      </span>
      <span className="kpi-label">{label}</span>
    </div>
  )
}
