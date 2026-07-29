// Executive shell — the production experience. Business surfaces only;
// engineering screens live behind the Admin Console.
import { useEffect, useRef, useState } from 'react'
import { Link, NavLink, Outlet, useLocation, useNavigate } from 'react-router-dom'
import { api } from '../api/client'
import { getTheme, isAdmin, setTheme } from '../lib/prefs'
import AISidebar from './AISidebar'
import ErrorBoundary from './ErrorBoundary'

// A single flat nav for the Product Manager workspace. Technical/engineering
// surfaces (graph, workflow monitor, agent activity, knowledge growth,
// decision analytics) live under Admin, not here — see App.jsx.
// Phase 2 #15: eight work-oriented destinations (Settings lives in the footer).
// Search stays in the header bar; Products, Ecosystem, Evolution, Timeline and
// Decisions remain reachable by URL (see App.jsx) and are surfaced as tabs/cards
// inside Workspace, Analytics and Products — demoted from the rail, not removed.
const NAV = [
  { to: '/', label: 'Workspace', icon: '✦', end: true },
  { to: '/assistant', label: 'AI Analyst', icon: '💬' },
  { to: '/files', label: 'Files', icon: '📎' },
  { to: '/reports', label: 'Reports', icon: '▣' },
  { to: '/intelligence', label: 'Analytics', icon: '⚛' },
  { to: '/communications', label: 'Communications', icon: '✉' },
  { to: '/products', label: 'Products', icon: '▦' },
  { to: '/data', label: 'Projects', icon: '▤' },
]

const NAV_INTEL = []

// Light theme leads; dark themes remain available via the header toggle.
const THEMES = ['daylight', 'graphite', 'midnight']
const THEME_ICON = { midnight: '☾', graphite: '◑', daylight: '☀' }

function ThemeToggle() {
  const [theme, setThemeState] = useState(getTheme())
  const cycle = () => {
    const next = THEMES[(THEMES.indexOf(theme) + 1) % THEMES.length]
    setTheme(next); setThemeState(next)
  }
  return (
    <button onClick={cycle} title={`Theme: ${theme} — click to switch`}
      className="w-8 h-8 rounded-lg flex items-center justify-center text-slate-400 hover:text-slate-200 hover:bg-surface-overlay transition-colors">
      {THEME_ICON[theme] || '☾'}
    </button>
  )
}

function GlobalSearch() {
  const [q, setQ] = useState('')
  const [results, setResults] = useState(null)
  const [open, setOpen] = useState(false)
  const boxRef = useRef(null)
  const timer = useRef(null)
  const navigate = useNavigate()

  useEffect(() => {
    const close = (e) => { if (boxRef.current && !boxRef.current.contains(e.target)) setOpen(false) }
    document.addEventListener('mousedown', close)
    return () => document.removeEventListener('mousedown', close)
  }, [])

  function onChange(value) {
    setQ(value)
    clearTimeout(timer.current)
    if (!value.trim()) { setResults(null); setOpen(false); return }
    timer.current = setTimeout(() => {
      api.managerSearch(value.trim())
        .then((r) => { setResults(r.results || []); setOpen(true) })
        .catch(() => { setResults([]); setOpen(true) })
    }, 300)
  }

  return (
    <div ref={boxRef} className="relative w-full max-w-md">
      <input className="input !py-1.5 !bg-surface-overlay/50" placeholder="Search across the organization…  (Enter for full results)"
             value={q} onChange={(e) => onChange(e.target.value)}
             onKeyDown={(e) => { if (e.key === 'Enter' && q.trim()) { setOpen(false); navigate(`/search?q=${encodeURIComponent(q.trim())}`) } }}
             onFocus={() => results && setOpen(true)} />
      {open && (
        <div className="absolute top-full mt-1.5 left-0 right-0 card shadow-2xl shadow-black/40 z-50 max-h-96 overflow-y-auto">
          {(results || []).length === 0
            ? <div className="p-4 text-sm text-slate-500">No matches for “{q}”.</div>
            : results.map((r, i) => (
                <div key={i} className="px-4 py-2.5 border-b border-surface-border/50 last:border-0 hover:bg-surface-overlay/60">
                  <div className="text-sm text-slate-200">{r.title || r.name || r.summary || '—'}</div>
                  <div className="text-xs text-slate-500 mt-0.5">
                    {(r.kind || r.surface || '').replace(/_/g, ' ')}
                    {r.detail ? ` · ${String(r.detail).slice(0, 90)}` : ''}
                  </div>
                </div>
              ))}
        </div>
      )}
    </div>
  )
}

function NotificationBell() {
  const [unread, setUnread] = useState(0)
  useEffect(() => {
    let live = true
    const load = () => api.managerNotifications(true)
      .then((d) => live && setUnread(d.stats?.unread ?? (d.notifications || []).length))
      .catch(() => {})
    load()
    const id = setInterval(load, 60000)
    return () => { live = false; clearInterval(id) }
  }, [])
  return (
    <Link to="/notifications" title="Notifications"
          className="relative w-8 h-8 rounded-lg flex items-center justify-center text-slate-400 hover:text-slate-200 hover:bg-surface-overlay transition-colors">
      ◔
      {unread > 0 && (
        <span className="absolute -top-0.5 -right-0.5 min-w-[16px] h-4 px-1 rounded-full bg-rose-500 text-white text-[10px] font-semibold flex items-center justify-center tabular-nums">
          {unread > 99 ? '99+' : unread}
        </span>
      )}
    </Link>
  )
}

export default function ExecLayout() {
  const [admin, setAdminState] = useState(isAdmin())
  const navigate = useNavigate()
  const location = useLocation()
  useEffect(() => {
    const sync = () => setAdminState(isAdmin())
    window.addEventListener('edip-admin-changed', sync)
    return () => window.removeEventListener('edip-admin-changed', sync)
  }, [])

  return (
    <div className="flex min-h-screen">
      <aside className="w-[232px] shrink-0 border-r border-surface-border bg-surface-raised/50 flex flex-col
                        max-lg:fixed max-lg:inset-y-0 max-lg:left-0 max-lg:z-40 max-lg:hidden lg:flex">
        <button onClick={() => navigate('/')} className="px-5 py-4 border-b border-surface-border text-left">
          <div className="text-[15px] font-bold text-slate-100 tracking-tight">Enterprise Agent</div>
          <div className="text-[11px] text-slate-500 mt-0.5">Executive Workspace</div>
        </button>
        <nav className="flex-1 overflow-y-auto py-3 space-y-0.5">
          {NAV.map((item) => (
            <NavLink key={item.to} to={item.to} end={item.end}
                     className={({ isActive }) => `nav-item ${isActive ? 'nav-item-active' : 'nav-item-idle'}`}>
              <span className="w-4 text-center opacity-70">{item.icon}</span>
              {item.label}
            </NavLink>
          ))}
        </nav>
        <div className="py-2 border-t border-surface-border">
          <NavLink to="/settings"
                   className={({ isActive }) => `nav-item ${isActive ? 'nav-item-active' : 'nav-item-idle'}`}>
            <span className="w-4 text-center opacity-70">⚙</span>
            Settings
          </NavLink>
          {admin && (
            <NavLink to="/admin"
                     className={({ isActive }) => `nav-item ${isActive ? 'nav-item-active' : 'nav-item-idle'}`}>
              <span className="w-4 text-center opacity-70">⛭</span>
              Admin Console
            </NavLink>
          )}
        </div>
      </aside>

      <div className="flex-1 min-w-0 flex flex-col">
        <header className="h-14 shrink-0 border-b border-surface-border bg-surface-raised/30 flex items-center gap-4 px-4 lg:px-6">
          <div className="lg:hidden text-sm font-bold text-slate-100">Enterprise Agent</div>
          <GlobalSearch />
          <div className="flex-1" />
          <ThemeToggle />
          <NotificationBell />
          <Link to="/assistant" title="Ask the AI Assistant"
                className="w-8 h-8 rounded-lg flex items-center justify-center text-accent hover:bg-accent/10 transition-colors">✦</Link>
          <div className="w-8 h-8 rounded-full bg-accent/20 text-accent text-xs font-semibold flex items-center justify-center"
               title="Executive">E</div>
        </header>

        {/* Mobile nav — the sidebar collapses into a scrollable strip */}
        <nav className="lg:hidden flex gap-1 overflow-x-auto border-b border-surface-border px-2 py-1.5 bg-surface-raised/30">
          {[...NAV, ...NAV_INTEL].map((item) => (
            <NavLink key={item.to} to={item.to} end={item.end}
                     className={({ isActive }) =>
                       `px-3 py-1.5 rounded-lg text-xs whitespace-nowrap ${
                         isActive ? 'bg-surface-overlay text-white' : 'text-slate-400'}`}>
              {item.label}
            </NavLink>
          ))}
          <NavLink to="/settings" className="px-3 py-1.5 rounded-lg text-xs whitespace-nowrap text-slate-400">Settings</NavLink>
          {admin && <NavLink to="/admin" className="px-3 py-1.5 rounded-lg text-xs whitespace-nowrap text-slate-400">Admin</NavLink>}
        </nav>

        <main className="flex-1 min-w-0 p-4 lg:p-8 max-w-content w-full mx-auto">
          <ErrorBoundary routeKey={location.pathname}>
            <Outlet />
          </ErrorBoundary>
        </main>
      </div>

      {/* Persistent, context-aware AI panel — available on every page */}
      <AISidebar />
    </div>
  )
}
