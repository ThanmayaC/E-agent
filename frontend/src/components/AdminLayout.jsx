// Admin Console shell — every engineering surface lives here, behind the
// administrator switch. Business users never see this chrome.
import { Link, NavLink, Outlet, useLocation } from 'react-router-dom'
import { isAdmin } from '../lib/prefs'
import ErrorBoundary from './ErrorBoundary'

// The admin nav names real subsystems only. Each entry is a live operational
// surface backed by genuine runtime metrics — no vanity pages.
const NAV = [
  { section: 'Console' },
  { to: '/admin', label: 'Subsystems', icon: '◈', end: true },
  { section: 'Data & Intelligence' },
  { to: '/admin/warehouse', label: 'Warehouse', icon: '▦' },
  { to: '/admin/models', label: 'ML Engine', icon: '∴' },
  { to: '/admin/brain', label: 'Enterprise Brain', icon: '◉' },
  { to: '/admin/graph', label: 'Knowledge Graph', icon: '✦' },
  { to: '/admin/llm', label: 'LLM', icon: '◆' },
  { section: 'Integration' },
  { to: '/admin/data-sources', label: 'Connectors', icon: '⊞' },
  { to: '/admin/sync', label: 'Sync & Ingestion', icon: '⇄' },
  { section: 'Operations' },
  { to: '/admin/runtime', label: 'Runtime', icon: '⟳' },
  { to: '/admin/jobs', label: 'Jobs & Queues', icon: '≡' },
  { to: '/admin/diagnostics', label: 'Diagnostics', icon: '✓' },
]

export default function AdminLayout() {
  const location = useLocation()
  if (!isAdmin()) {
    return (
      <div className="min-h-screen flex items-center justify-center p-6">
        <div className="card-pad max-w-md text-center py-10">
          <div className="text-2xl mb-3">⛭</div>
          <div className="text-slate-100 font-semibold">Admin Console</div>
          <p className="text-sm text-slate-500 mt-2">
            This area contains engineering controls and is limited to administrators.
            Enable administrator mode in Settings to continue.
          </p>
          <div className="mt-5 flex gap-2 justify-center">
            <Link to="/settings" className="btn">Open Settings</Link>
            <Link to="/" className="btn-ghost">Back to workspace</Link>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="flex min-h-screen">
      <aside className="w-[212px] shrink-0 border-r border-surface-border bg-surface-raised/50 flex flex-col
                        lg:sticky lg:top-0 lg:h-screen">
        <Link to="/" className="px-5 py-4 border-b border-surface-border block">
          <div className="text-[15px] font-bold text-slate-100 tracking-tight">
            Enterprise Agent <span className="ml-1 align-middle chip chip-warn font-semibold tracking-wide">ADMIN</span>
          </div>
          <div className="text-[11px] text-slate-500 mt-0.5">← Back to workspace</div>
        </Link>
        <nav className="flex-1 overflow-y-auto py-3 space-y-0.5">
          {NAV.map((item, i) => (
            item.section ? (
              <div key={`s-${i}`} className="nav-section">{item.section}</div>
            ) : (
              <NavLink key={item.to} to={item.to} end={item.end}
                       className={({ isActive }) => `nav-item ${isActive ? 'nav-item-active' : 'nav-item-idle'}`}>
                <span className="w-4 text-center opacity-70">{item.icon}</span>
                {item.label}
              </NavLink>
            )
          ))}
        </nav>
        <div className="px-5 py-3 border-t border-surface-border text-[11px] text-slate-600">
          Engineering surfaces — hidden from the executive workspace.
        </div>
      </aside>
      <main className="flex-1 min-w-0 p-4 lg:p-8 max-w-content w-full mx-auto">
        <ErrorBoundary routeKey={location.pathname}>
          <Outlet />
        </ErrorBoundary>
      </main>
    </div>
  )
}
