import type { ReactNode } from 'react'
import type { ScreenId } from '../types/portfolio'

type NavItem = {
  id: ScreenId
  label: string
  description: string
}

const navItems: NavItem[] = [
  { id: 'worklist', label: 'Worklist', description: 'Manager queue' },
  { id: 'portfolio', label: 'Portfolio', description: 'All open cases' },
  { id: 'reporting', label: 'Reporting', description: 'Phase metrics' },
]

type AppShellProps = {
  activeScreen: ScreenId
  onNavigate: (screen: ScreenId) => void
  children: ReactNode
}

export function AppShell({ activeScreen, onNavigate, children }: AppShellProps) {
  const showMainNav = activeScreen !== 'case-detail'

  return (
    <div className="app-shell">
      <header className="app-header">
        <div className="brand">
          <span className="brand-mark">360°</span>
          <div>
            <p className="brand-title">Flow</p>
            <p className="brand-subtitle">Portfolio desktop prototype</p>
          </div>
        </div>
        {showMainNav && (
          <nav className="main-nav" aria-label="Primary">
            {navItems.map((item) => (
              <button
                key={item.id}
                type="button"
                className={activeScreen === item.id ? 'nav-btn active' : 'nav-btn'}
                onClick={() => onNavigate(item.id)}
              >
                <span className="nav-label">{item.label}</span>
                <span className="nav-desc">{item.description}</span>
              </button>
            ))}
          </nav>
        )}
      </header>
      <main className="app-main">{children}</main>
    </div>
  )
}
