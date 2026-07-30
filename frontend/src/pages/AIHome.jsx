// Workspace — the single landing page. It answers, in this order: what can I
// ask, what happened, what needs me, what have I got.
//
// This page absorbed the separate PMHome dashboard. The two were competing
// homes — one ask-first, one status-first — and PMHome had no inbound link from
// anywhere in the app, so its status strip, brief, approvals and incident
// panels were unreachable. They live here now, below the prompt.
import { useEffect, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { api } from '../api/client'
import { Badge, Empty, Panel, Stat, useAsync } from '../components/ui'
import { Reveal, Skeleton, Stagger, StaggerItem } from '../components/premium'

const FALLBACK_PROMPTS = [
  'What happened across UPI this month?',
  'Why did transaction value change?',
  'Which banks are improving?',
  'Generate an executive report.',
  'Which decision generated the most business value?',
  'Summarize the latest incident and its RCA.',
]

function greeting() {
  const h = new Date().getHours()
  return h < 12 ? 'Good morning' : h < 18 ? 'Good afternoon' : 'Good evening'
}

// A compact list panel — the repeated shape across the lower half of the page.
function ListPanel({ title, action, items, empty, render }) {
  return (
    <Panel title={title} action={action}>
      {items.length === 0
        ? <p className="text-xs text-slate-500 py-1">{empty}</p>
        : <ul className="-mx-1.5 space-y-0.5">{items.map(render)}</ul>}
    </Panel>
  )
}

function Row({ children, onClick, to }) {
  const cls = 'w-full text-left px-1.5 py-1.5 rounded-md text-sm text-slate-300 flex items-center gap-2 hover:bg-surface-overlay/60 transition-colors'
  if (to) return <li><Link to={to} className={cls}>{children}</Link></li>
  if (onClick) return <li><button onClick={onClick} className={cls}>{children}</button></li>
  return <li className={cls}>{children}</li>
}

export default function AIHome() {
  const nav = useNavigate()
  const [input, setInput] = useState('')
  const [feed, setFeed] = useState(null)
  const [loading, setLoading] = useState(true)
  const [refresh, setRefresh] = useState(0)

  useEffect(() => {
    api.workspaceHome().then(setFeed).catch(() => setFeed({})).finally(() => setLoading(false))
  }, [])

  // The operational half refreshes on its own; the feed above does not need to.
  useEffect(() => {
    const id = setInterval(() => setRefresh((n) => n + 1), 60000)
    return () => clearInterval(id)
  }, [])

  const brief = useAsync(() => api.executiveBrief().catch(() => null), [refresh])
  const ws = useAsync(() => api.managerWorkspace().catch(() => null), [refresh])
  const notifications = useAsync(() => api.managerNotifications(true).catch(() => null), [refresh])
  const tasksState = useAsync(() => api.managerTasks().catch(() => null), [refresh])

  const ask = (q) => {
    const question = (q ?? input).trim()
    if (!question) return
    nav('/assistant', { state: { ask: question } })
  }

  const prompts = (feed?.suggestions?.length ? feed.suggestions : FALLBACK_PROMPTS).slice(0, 6)
  const convos = feed?.recent_conversations || []
  const files = feed?.recent_files || []
  const reports = feed?.recent_reports || []
  const recs = feed?.recommendations || []
  const pinned = feed?.pinned || []
  const artifacts = feed?.recent_artifacts || []

  const b = brief.data
  const openIncidents = (b?.critical_events || []).filter((e) => e.status !== 'resolved')
  const priorities = b?.priorities || []
  const pendingApprovals = notifications.data?.notifications
    ?.filter((n) => (n.kind || n.type || '').toLowerCase().includes('approval')) || []
  const openTasks = (tasksState.data?.tasks || []).filter((t) =>
    ['open', 'todo', 'pending', 'in_progress'].includes((t.status || '').toLowerCase()))
  const openActionItems = ws.data?.todays_summary?.open_action_items ?? openTasks.length

  return (
    <div className="max-w-6xl mx-auto space-y-8">
      {/* ---------------------------------------------------------- ask first */}
      <Reveal>
        <section className="pt-4 pb-2 text-center">
          <div className="text-2xl mb-2 text-accent" aria-hidden>✦</div>
          <h1 className="h-page">Enterprise AI Workspace</h1>
          <p className="prose-sm mt-1.5 max-w-xl mx-auto">
            Ask anything across the UPI ecosystem — grounded in the Knowledge Graph,
            six-month history, reports and your files.
          </p>
          <form onSubmit={(e) => { e.preventDefault(); ask() }}
                className="mt-5 max-w-2xl mx-auto flex gap-2">
            <input autoFocus value={input} onChange={(e) => setInput(e.target.value)}
                   placeholder="Ask, analyze, compare, or generate…"
                   className="input flex-1 !py-3 !text-base" />
            <button className="btn !px-6" type="submit" disabled={!input.trim()}>Ask</button>
          </form>
          <div className="mt-3.5 flex flex-wrap gap-1.5 justify-center">
            {prompts.map((p) => (
              <button key={p} onClick={() => ask(p)}
                      className="px-3 py-1.5 rounded-full text-xs bg-surface-overlay/60 text-slate-400
                                 border border-surface-border transition-colors
                                 hover:text-slate-100 hover:border-accent/40">
                {p}
              </button>
            ))}
          </div>
        </section>
      </Reveal>

      {/* -------------------------------------------------- today, at a glance */}
      <section className="space-y-4">
        <div className="card-pad grid-backdrop relative overflow-hidden">
          <div className="absolute top-0 right-0 w-72 h-72 bg-accent/10 blur-3xl rounded-full pointer-events-none" />
          <div className="relative">
            <div className="eyebrow">Today · {new Date().toLocaleDateString(undefined, { dateStyle: 'medium' })}</div>
            <h2 className="text-lg lg:text-xl font-semibold text-slate-100 mt-1.5">
              {greeting()}. {openIncidents.length > 0
                ? `${openIncidents.length} incident${openIncidents.length > 1 ? 's' : ''} need attention.`
                : 'UPI Products is steady today.'}
            </h2>
            {brief.loading
              ? <Skeleton className="h-3 w-2/3 mt-2" />
              : <p className="prose-sm mt-1.5 max-w-3xl">{b?.business_summary || 'No brief available yet.'}</p>}
          </div>
        </div>

        <Stagger className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          <StaggerItem>
            <Stat label="Open incidents" value={openIncidents.length}
                  tone={openIncidents.length ? 'fg-danger' : 'fg-success'}
                  hint="view timeline" onClick={() => nav('/timeline')} />
          </StaggerItem>
          <StaggerItem>
            <Stat label="Major decisions" value={(b?.major_decisions || []).length}
                  hint="review" onClick={() => nav('/decisions')} />
          </StaggerItem>
          <StaggerItem>
            <Stat label="Pending approvals" value={pendingApprovals.length}
                  tone={pendingApprovals.length ? 'fg-warn' : 'fg-primary'}
                  hint="notifications" onClick={() => nav('/notifications')} />
          </StaggerItem>
          <StaggerItem>
            <Stat label="Open action items" value={openActionItems}
                  hint="tasks" onClick={() => nav('/tasks')} />
          </StaggerItem>
        </Stagger>
      </section>

      {/* --------------------------------------------------- what needs me now */}
      <section className="grid gap-4 lg:grid-cols-3">
        <Panel accent className="lg:col-span-2" title="Today’s highlights"
               action={<Link to="/assistant" className="btn-quiet">Ask AI →</Link>}>
          {brief.loading ? (
            <div className="space-y-2.5">{[0, 1, 2].map((i) => <Skeleton key={i} className="h-3.5" style={{ width: `${85 - i * 12}%` }} />)}</div>
          ) : (b?.critical_events || []).length === 0 ? (
            <p className="text-sm text-slate-500">No major events today — steady state.</p>
          ) : (
            <ul className="space-y-2.5">
              {b.critical_events.map((e, i) => (
                <li key={i} className="flex items-start gap-2.5 text-sm">
                  <span className={`w-1.5 h-1.5 rounded-full mt-1.5 shrink-0 ${
                    e.status === 'resolved' ? 'bg-emerald-400' : 'bg-rose-400'}`} />
                  <div className="min-w-0">
                    <div className="text-slate-200">{e.event}</div>
                    {e.detail && <div className="text-xs text-slate-500 mt-0.5">{e.detail}</div>}
                  </div>
                </li>
              ))}
            </ul>
          )}
        </Panel>

        <div className="space-y-4">
          <ListPanel title="Needs attention" empty="Nothing needs you right now."
                     action={<Link to="/decisions" className="btn-quiet">All →</Link>}
                     items={priorities.slice(0, 5)}
                     render={(p, i) => (
                       <Row key={i}>
                         <span className="text-accent shrink-0" aria-hidden>▹</span>
                         <span className="truncate">{p.title}</span>
                       </Row>
                     )} />
          <ListPanel title="Pending approvals" empty="Nothing waiting on you."
                     action={<Link to="/notifications" className="btn-quiet">All →</Link>}
                     items={pendingApprovals.slice(0, 5)}
                     render={(n, i) => <Row key={i}><span className="truncate">{n.title || n.message}</span></Row>} />
        </div>
      </section>

      {/* ------------------------------------------------------- what I've got */}
      {loading ? (
        <div className="grid gap-4 lg:grid-cols-2">
          {[0, 1, 2, 3].map((i) => (
            <div key={i} className="card-pad space-y-2.5">
              <Skeleton className="h-3 w-32" />
              {[0, 1, 2].map((j) => <Skeleton key={j} className="h-3.5" style={{ width: `${90 - j * 14}%` }} />)}
            </div>
          ))}
        </div>
      ) : (
        <section className="grid gap-4 lg:grid-cols-2 pb-4">
          <ListPanel title="Recent conversations" empty="No conversations yet — ask something above."
                     action={<button className="btn-quiet" onClick={() => nav('/assistant')}>Open chat →</button>}
                     items={convos.slice(0, 6)}
                     render={(c) => (
                       <Row key={c.conversation_id} onClick={() => nav('/assistant', { state: { open: c.conversation_id } })}>
                         <span className="truncate">{c.pinned && '★ '}{c.title || 'Untitled'}</span>
                       </Row>
                     )} />

          <ListPanel title="Recent files" empty="No files yet — drop files on the Files page for instant AI understanding."
                     action={<button className="btn-quiet" onClick={() => nav('/files')}>Upload / view →</button>}
                     items={files.slice(0, 6)}
                     render={(f) => (
                       <Row key={f.id} onClick={() => nav('/files', { state: { open: f.id } })}>
                         <Badge tone="info">{f.type}</Badge>
                         <span className="truncate flex-1">{f.file}</span>
                       </Row>
                     )} />

          <ListPanel title="Recent reports" empty="No reports available."
                     action={<button className="btn-quiet" onClick={() => nav('/reports')}>All reports →</button>}
                     items={reports.slice(0, 6)}
                     render={(r, i) => (
                       <Row key={i} to={r.project_id ? `/reports/${r.project_id}` : '/reports'}>
                         <Badge tone="default">{r.category || 'report'}</Badge>
                         <span className="truncate flex-1">{r.title || r.id}</span>
                       </Row>
                     )} />

          <ListPanel title="Recommendations" empty="No recommendations yet."
                     action={<button className="btn-quiet" onClick={() => nav('/evolution')}>Evolution →</button>}
                     items={recs.slice(0, 5)}
                     render={(r, i) => (
                       <Row key={i}>
                         <span className="text-accent shrink-0" aria-hidden>→</span>
                         <span className="truncate flex-1">{r.title || r.decision_id}</span>
                         {r.business_value_cr != null && (
                           <span className="text-xs text-slate-500 num shrink-0">₹{r.business_value_cr}cr</span>
                         )}
                       </Row>
                     )} />

          {(pinned.length > 0 || artifacts.length > 0) && (
            <Panel title="Pinned & generated" className="lg:col-span-2">
              <div className="flex flex-wrap gap-2">
                {pinned.map((p) => (
                  <button key={p.id} onClick={() => p.link && nav(p.link)}
                          className="text-xs inset px-2.5 py-1 text-slate-300 hover:border-accent/50 transition-colors">
                    📌 {p.title}
                  </button>
                ))}
                {artifacts.map((a) => (
                  <a key={a.file} href={api.artifactUrl(a.file)} target="_blank" rel="noreferrer"
                     className="text-xs inset px-2.5 py-1 text-slate-300 hover:border-accent/50 transition-colors">
                    ⬇ {a.file}
                  </a>
                ))}
              </div>
            </Panel>
          )}
        </section>
      )}

      {!loading && convos.length === 0 && files.length === 0 && reports.length === 0 && (
        <Empty title="Your workspace is empty" icon="✦"
               hint="Ask a question above, or upload business data to get reports, forecasts and recommendations."
               action={<Link to="/data" className="btn">Upload business data</Link>} />
      )}
    </div>
  )
}
