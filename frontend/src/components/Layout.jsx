import { NavLink, Link } from 'react-router-dom'

const NAV = [
  { to: '', label: 'Executive Dashboard', icon: '◈' },
  { to: 'datasets', label: 'Dataset Explorer', icon: '▤' },
  { to: 'schema', label: 'Schema Explorer', icon: '≡' },
  { to: 'relationships', label: 'Relationships', icon: '⇄' },
  { to: 'graph', label: 'Knowledge Graph', icon: '◉' },
  { to: 'analytics', label: 'Analytics', icon: '∑' },
  { to: 'kpis', label: 'KPIs', icon: '△' },
  { to: 'insights', label: 'Insights', icon: '✦' },
  { to: 'predictions', label: 'Predictions', icon: '↗' },
  { to: 'recommendations', label: 'Recommendations', icon: '☑' },
  { to: 'copilot', label: 'Copilot', icon: '❯_' },
  { to: 'reports', label: 'Reports', icon: '▣' },
  { to: 'quality', label: 'Data Quality', icon: '✓' },
  { to: 'knowledge', label: 'Knowledge Explorer', icon: '🧠' },
  { to: 'workflows', label: 'Workflows', icon: '⟳' },
  { to: 'admin', label: 'Settings & Admin', icon: '⚙' },
]

export default function Layout({ projectId, children }) {
  return (
    <div className="flex min-h-screen">
      <aside className="w-60 shrink-0 border-r border-surface-border bg-surface-raised/60 flex flex-col">
        <Link to="/" className="px-5 py-4 border-b border-surface-border block">
          <div className="text-base font-bold text-slate-100">EAPIP</div>
          <div className="text-[11px] text-slate-500">Autonomous Product Intelligence</div>
        </Link>
        <nav className="flex-1 overflow-y-auto py-3">
          {NAV.map((item) => (
            <NavLink
              key={item.to}
              to={`/p/${projectId}/${item.to}`}
              end={item.to === ''}
              className={({ isActive }) =>
                `flex items-center gap-3 px-5 py-2 text-sm transition-colors ${
                  isActive
                    ? 'text-white bg-accent/15 border-r-2 border-accent'
                    : 'text-slate-400 hover:text-slate-200 hover:bg-surface-overlay'
                }`
              }
            >
              <span className="w-4 text-center opacity-70">{item.icon}</span>
              {item.label}
            </NavLink>
          ))}
        </nav>
        <div className="px-5 py-3 border-t border-surface-border text-[11px] text-slate-600">
          project: <span className="text-slate-400 font-mono">{projectId}</span>
        </div>
      </aside>
      <main className="flex-1 min-w-0 p-6 lg:p-8">{children}</main>
    </div>
  )
}
