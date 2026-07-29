// Home — the Product Manager's landing page. Answers three questions:
// what happened, what needs attention, what should I do next. No AI/runtime
// jargon — business nouns only (incidents, reports, decisions, meetings).
import { useEffect, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { api } from '../api/client'
import { useAsync } from '../components/ui'
import { GlowPanel, Loader, PremiumHeader, Reveal, Stagger, StaggerItem, StatCard } from '../components/premium'

function greeting() {
  const h = new Date().getHours()
  return h < 12 ? 'Good morning' : h < 18 ? 'Good afternoon' : 'Good evening'
}

const QUICK_ACTIONS = [
  { to: '/reports', label: 'Generate Executive Report', icon: '▣' },
  { to: '/assistant', label: 'Ask AI', icon: '✦' },
  { to: '/reports', label: 'View Reports', icon: '▤' },
  { to: '/decisions', label: 'Review Decisions', icon: '⚖' },
  { to: '/timeline', label: 'View Timeline', icon: '≡' },
]

export default function PMHome() {
  const [refresh, setRefresh] = useState(0)
  const navigate = useNavigate()
  const reload = () => setRefresh((n) => n + 1)

  useEffect(() => {
    const id = setInterval(() => setRefresh((n) => n + 1), 30000)
    return () => clearInterval(id)
  }, [])

  const ws = useAsync(() => api.managerWorkspace().catch(() => null), [refresh])
  const brief = useAsync(() => api.executiveBrief().catch(() => null), [refresh])
  const notifications = useAsync(() => api.managerNotifications(true).catch(() => null), [refresh])
  const tasksState = useAsync(() => api.managerTasks().catch(() => null), [refresh])
  const reports = useAsync(() => api.executiveReports().catch(() => ({ reports: [] })), [refresh])

  const b = brief.data
  const openIncidents = (b?.critical_events || []).filter((e) => e.status !== 'resolved')
  const pendingApprovals = notifications.data?.notifications
    ?.filter((n) => (n.kind || n.type || '').toLowerCase().includes('approval')) || []
  const openTasks = (tasksState.data?.tasks || []).filter((t) =>
    ['open', 'todo', 'in_progress'].includes((t.status || '').toLowerCase()))
  const meetingsToday = openTasks.filter((t) => (t.title || '').toLowerCase().includes('meeting'))
  const latestReports = (reports.data?.reports || []).slice(0, 5)

  return (
    <div className="space-y-6">
      <PremiumHeader title="Home" badge="Live"
        subtitle="What happened, what needs your attention, what to do next." />

      <Reveal>
        <div className="card-pad grid-backdrop relative overflow-hidden">
          <div className="absolute top-0 right-0 w-72 h-72 bg-accent/10 blur-3xl rounded-full pointer-events-none" />
          <div className="relative">
            <h2 className="text-xl lg:text-2xl font-bold text-slate-100">
              {greeting()}. {openIncidents.length > 0
                ? `${openIncidents.length} incident(s) need attention.`
                : 'UPI Products is steady today.'}
            </h2>
            <p className="text-sm text-slate-500 mt-1">
              {b?.business_summary || 'Loading today’s brief…'}
            </p>
          </div>
        </div>
      </Reveal>

      <Loader state={ws} skeleton={<div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4" />}>
        {(w) => {
          const summary = w?.todays_summary || {}
          return (
            <Stagger className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
              <StaggerItem><StatCard label="Open incidents" value={openIncidents.length}
                tone={openIncidents.length ? 'fg-danger' : 'fg-success'}
                onClick={() => navigate('/timeline')} /></StaggerItem>
              <StaggerItem><StatCard label="Pending decisions" value={(b?.major_decisions || []).length}
                onClick={() => navigate('/decisions')} /></StaggerItem>
              <StaggerItem><StatCard label="Pending approvals" value={pendingApprovals.length}
                tone="fg-warn" onClick={() => navigate('/notifications')} /></StaggerItem>
              <StaggerItem><StatCard label="Open tasks" value={summary.open_action_items ?? openTasks.length}
                onClick={() => navigate('/tasks')} /></StaggerItem>
            </Stagger>
          )
        }}
      </Loader>

      <div className="grid gap-5 lg:grid-cols-3">
        <GlowPanel accent className="lg:col-span-2" title="Today's Highlights"
          action={<Link to="/assistant" className="btn-quiet">Ask AI →</Link>}>
          <Loader state={brief} empty="No brief available yet.">
            {() => (
              <div className="space-y-3">
                {b?.critical_events?.length > 0 ? (
                  <ul className="space-y-2.5">
                    {b.critical_events.map((e, i) => (
                      <li key={i} className="flex items-start gap-2.5 text-sm">
                        <span className={`w-1.5 h-1.5 rounded-full mt-1.5 shrink-0 ${
                          e.status === 'resolved' ? 'bg-emerald-400' : 'bg-rose-400'}`} />
                        <div>
                          <div className="text-slate-200">{e.event}</div>
                          <div className="text-xs text-slate-500 mt-0.5">{e.detail}</div>
                        </div>
                      </li>
                    ))}
                  </ul>
                ) : (
                  <div className="text-sm text-slate-500">No major events today — steady state.</div>
                )}
              </div>
            )}
          </Loader>
        </GlowPanel>

        <div className="space-y-5">
          <GlowPanel title="Things Requiring Attention" action={<Link to="/decisions" className="btn-quiet">All →</Link>}>
            <Loader state={brief} empty="Nothing needs attention right now.">
              {() => (b?.priorities || []).length === 0
                ? <div className="text-sm text-slate-500">Nothing needs your attention right now.</div>
                : (
                  <ul className="space-y-2">
                    {b.priorities.slice(0, 5).map((p, i) => (
                      <li key={i} className="text-sm text-slate-300 flex gap-2">
                        <span className="text-accent">▹</span><span className="truncate">{p.title}</span>
                      </li>
                    ))}
                  </ul>
                )}
            </Loader>
          </GlowPanel>

          <GlowPanel title="Pending Approvals" action={<Link to="/notifications" className="btn-quiet">All →</Link>}>
            {pendingApprovals.length === 0
              ? <div className="text-sm text-slate-500">Nothing waiting on you.</div>
              : (
                <ul className="space-y-2">
                  {pendingApprovals.slice(0, 5).map((n, i) => (
                    <li key={i} className="text-sm text-slate-300 truncate">{n.title || n.message}</li>
                  ))}
                </ul>
              )}
          </GlowPanel>
        </div>
      </div>

      <div className="grid gap-5 lg:grid-cols-3">
        <GlowPanel title="Meetings Today">
          {meetingsToday.length === 0
            ? <div className="text-sm text-slate-500">No meetings scheduled today.</div>
            : (
              <ul className="space-y-2">
                {meetingsToday.slice(0, 5).map((t) => (
                  <li key={t.task_id} className="text-sm text-slate-300 truncate">{t.title}</li>
                ))}
              </ul>
            )}
        </GlowPanel>

        <GlowPanel title="Open Incidents" action={<Link to="/timeline" className="btn-quiet">Timeline →</Link>}>
          {openIncidents.length === 0
            ? <div className="text-sm text-slate-500">No open incidents.</div>
            : (
              <ul className="space-y-2">
                {openIncidents.map((e, i) => (
                  <li key={i} className="text-sm text-slate-300 truncate">{e.event}</li>
                ))}
              </ul>
            )}
        </GlowPanel>

        <GlowPanel title="Latest Reports" action={<Link to="/reports" className="btn-quiet">All →</Link>}>
          {latestReports.length === 0
            ? <div className="text-sm text-slate-500">No reports yet.</div>
            : (
              <ul className="space-y-2">
                {latestReports.map((r) => (
                  <li key={r.report_id}>
                    <Link to="/reports" className="text-sm text-slate-300 hover:text-accent truncate block">
                      {r.title}
                    </Link>
                  </li>
                ))}
              </ul>
            )}
        </GlowPanel>
      </div>

      <GlowPanel title="Quick Actions">
        <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-5">
          {QUICK_ACTIONS.map((a) => (
            <Link key={a.label} to={a.to} className="card-pad card-hover !p-3.5 text-center text-sm text-slate-300">
              <div className="text-lg mb-1">{a.icon}</div>
              {a.label}
            </Link>
          ))}
        </div>
      </GlowPanel>
    </div>
  )
}
