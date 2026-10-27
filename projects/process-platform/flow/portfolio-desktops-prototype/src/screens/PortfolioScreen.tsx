import { useMemo, useState } from 'react'
import { portfolioCases } from '../data/mockPortfolio'
import { StatusBadge } from '../components/StatusBadge'

type PortfolioScreenProps = {
  onOpenCase: (caseId: string) => void
}

export function PortfolioScreen({ onOpenCase }: PortfolioScreenProps) {
  const [search, setSearch] = useState('')
  const [assigneeFilter, setAssigneeFilter] = useState('all')

  const assignees = useMemo(
    () => ['all', ...new Set(portfolioCases.map((c) => c.assignee))],
    [],
  )

  const filtered = useMemo(() => {
    const query = search.trim().toLowerCase()
    return portfolioCases
      .filter((c) => c.phase !== 'Closed')
      .filter((c) => assigneeFilter === 'all' || c.assignee === assigneeFilter)
      .filter(
        (c) =>
          !query ||
          c.title.toLowerCase().includes(query) ||
          c.id.toLowerCase().includes(query) ||
          c.municipality.toLowerCase().includes(query),
      )
  }, [search, assigneeFilter])

  const byPhase = useMemo(() => {
    const groups = new Map<string, number>()
    for (const item of filtered) {
      groups.set(item.phase, (groups.get(item.phase) ?? 0) + 1)
    }
    return [...groups.entries()]
  }, [filtered])

  return (
    <div className="screen">
      <header className="screen-header">
        <div>
          <h1>Portfolio desktop</h1>
          <p className="lede">
            Cross-case overview by process model and phase — prototype for ADO #414651.
          </p>
        </div>
      </header>

      <div className="portfolio-layout">
        <aside className="side-panel">
          <h2>Filters</h2>
          <label className="filter-select block">
            <span>Search</span>
            <input
              type="search"
              placeholder="Case, title, municipality…"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
            />
          </label>
          <label className="filter-select block">
            <span>Assignee</span>
            <select value={assigneeFilter} onChange={(e) => setAssigneeFilter(e.target.value)}>
              {assignees.map((name) => (
                <option key={name} value={name}>
                  {name === 'all' ? 'All assignees' : name}
                </option>
              ))}
            </select>
          </label>

          <h3 className="side-heading">By phase</h3>
          <ul className="phase-list">
            {byPhase.map(([phase, count]) => (
              <li key={phase}>
                <span>{phase}</span>
                <span className="count-pill">{count}</span>
              </li>
            ))}
          </ul>
        </aside>

        <section className="card-grid">
          {filtered.map((item) => (
            <article key={item.id} className="case-card">
              <div className="case-card-top">
                <span className="case-id">{item.id}</span>
                <StatusBadge urgency={item.urgency} />
              </div>
              <h3>{item.title}</h3>
              <dl className="case-meta">
                <div>
                  <dt>Process</dt>
                  <dd>{item.processModel}</dd>
                </div>
                <div>
                  <dt>Phase</dt>
                  <dd>{item.phase}</dd>
                </div>
                <div>
                  <dt>Assignee</dt>
                  <dd>{item.assignee}</dd>
                </div>
                <div>
                  <dt>Deadline</dt>
                  <dd>{item.deadline}</dd>
                </div>
              </dl>
              <button type="button" className="primary-btn" onClick={() => onOpenCase(item.id)}>
                View case
              </button>
            </article>
          ))}
        </section>
      </div>
    </div>
  )
}
