// Admin Console shell — every engineering surface lives here, behind the
// administrator switch. Business users never see this chrome.
import { Link, NavLink, Outlet } from 'react-router-dom'
import { isAdmin } from '../lib/prefs'

const NAV = [
  { to: '/admin', label: 'Overview', icon: '◈', end: true },
  { to: '/admin/operating', label: 'AI Operating', icon: '⬡' },
  { to: '/admin/runtime', label: 'Runtime', icon: '⟳' },
  { to: '/admin/brain', label: 'Brain', icon: '◉' },
  { to: '/admin/scheduler', label: 'Scheduler', icon: '◷' },
  { to: '/admin/jobs', label: 'Jobs', icon: '≡' },
  { to: '/admin/data-sources', label: 'Data sources', icon: '⊞' },
  { to: '/admin/sync', label: 'Sync', icon: '⇄' },
  { to: '/admin/documents', label: 'Documents', icon: '▣' },
  { to: '/admin/knowledge', label: 'Knowledge', icon: '✦' },
  { to: '/admin/logs', label: 'Logs', icon: '▤' },
  { to: '/admin/diagnostics', label: 'Diagnostics', icon: '✓' },
  { to: '/admin/models', label: 'Model status', icon: '∴' },
  { to: '/data', label: 'Data workbench', icon: '▦' },
]

export default function AdminLayout() {
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
      <aside className="w-[212px] shrink-0 border-r border-surface-border bg-surface-raised/50 flex flex-col">
        <Link to="/" className="px-5 py-4 border-b border-surface-border block">
          <div className="text-[15px] font-bold text-slate-100 tracking-tight">
            Enterprise Agent <span className="ml-1 text-[10px] align-middle px-1.5 py-0.5 rounded bg-amber-500/15 text-amber-400 font-semibold tracking-wide">ADMIN</span>
          </div>
          <div className="text-[11px] text-slate-500 mt-0.5">← Back to workspace</div>
        </Link>
        <nav className="flex-1 overflow-y-auto py-3 space-y-0.5">
          {NAV.map((item) => (
            <NavLink key={item.to} to={item.to} end={item.end}
                     className={({ isActive }) => `nav-item ${isActive ? 'nav-item-active' : 'nav-item-idle'}`}>
              <span className="w-4 text-center opacity-70">{item.icon}</span>
              {item.label}
            </NavLink>
          ))}
        </nav>
        <div className="px-5 py-3 border-t border-surface-border text-[11px] text-slate-600">
          Engineering surfaces — hidden from the executive workspace.
        </div>
      </aside>
      <main className="flex-1 min-w-0 p-4 lg:p-8 max-w-content w-full mx-auto">
        <Outlet />
      </main>
    </div>
  )
}
