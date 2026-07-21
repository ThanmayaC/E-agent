// Home — the executive workspace (V2.4). Not a passive dashboard: the first
// thing an executive sees is what requires attention — today's brief, the
// top decisions the Brain proposes, recommended actions, critical risks,
// pending approvals, and what changed in the organization.
import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { api } from '../api/client'
import { AsyncSection, Badge, HealthRing, Panel, PanelEmpty, useAsync } from '../components/ui'

const ASK_IDEAS = [
  'What should I focus on today?',
  'Prepare today’s executive brief.',
  'Show products requiring attention.',
  'Why is growth slowing?',
]

function greeting() {
  const h = new Date().getHours()
  return h < 12 ? 'Good morning' : h < 18 ? 'Good afternoon' : 'Good evening'
}

export default function Home() {
  const [refresh, setRefresh] = useState(0)
  const [ask, setAsk] = useState('')
  const navigate = useNavigate()
  const state = useAsync(() => api.managerWorkspace(), [refresh])
  // The executive brief and the overnight summary are composed by the platform
  // on its own heartbeat — the manager reads them, never generates them.
  const brief = useAsync(() => api.dailyBrief(), [refresh])
  const overnight = useAsync(() => api.overnightSummary(), [refresh])
  // The Decision Intelligence brief: top decisions, recommended actions,
  // and organizational changes — composed by the Brain, read here.
  const intel = useAsync(() => api.intelligenceBrief().catch(() => null), [refresh])
  const reload = () => setRefresh((n) => n + 1)

  const goAsk = (q) => navigate('/copilot', { state: { ask: q } })
  const actionId = (ref) => ref.replace(/^action:/, '')
  const approve = (ref) => api.approveAction(actionId(ref), 'executive').then(reload)
  const reject = (ref) => api.rejectAction(actionId(ref), 'executive', 'rejected from Home').then(reload)
  const completeTask = (id) => api.setTaskStatus(id, 'completed').then(reload)
  const decide = (id, status) =>
    api.setIntelligenceDecision(id, status, 'executive', `${status} from Home`).then(reload)

  return (
    <AsyncSection state={state} empty="Your workspace is warming up — connect a data source under Settings.">
      {(ws) => {
        const health = ws.portfolio_health?.average_health_score
        const summary = ws.todays_summary || {}
        const approvals = ws.pending_approvals || []
        const risks = ws.critical_risks || []
        const tasks = ws.pending_tasks || []
        const decisions = ws.recent_decisions || []
        const topDecisions = intel.data?.top_decisions || []
        const recommended = intel.data?.recommended_actions || []
        const changes = intel.data?.recent_changes || []
        return (
          <div className="space-y-6">
            {/* Hero: greeting + ask bar. The Copilot is the primary interface. */}
            <section className="pt-4 lg:pt-10 pb-2 max-w-3xl mx-auto text-center">
              <div className="flex justify-center mb-5"><HealthRing score={health} size={84} label="health" /></div>
              <h1 className="text-2xl lg:text-3xl font-bold tracking-tight text-slate-100">
                {greeting()}. {risks.length > 0
                  ? `${risks.length} risk${risks.length > 1 ? 's' : ''} need${risks.length > 1 ? '' : 's'} your attention.`
                  : 'The portfolio is steady.'}
              </h1>
              <p className="text-sm text-slate-500 mt-2">
                {summary.open_action_items ?? 0} open action items · {approvals.length} awaiting approval · {summary.unread_notifications ?? 0} unread notifications
              </p>
              <form className="mt-6 flex gap-2"
                    onSubmit={(e) => { e.preventDefault(); if (ask.trim()) goAsk(ask.trim()) }}>
                <input className="input !py-3 !px-4 !text-base shadow-lg shadow-black/20" autoFocus
                       placeholder="Ask anything about your business…"
                       value={ask} onChange={(e) => setAsk(e.target.value)} />
                <button className="btn !px-5" type="submit" disabled={!ask.trim()}>Ask</button>
              </form>
              <div className="mt-3 flex flex-wrap gap-2 justify-center">
                {ASK_IDEAS.map((q) => (
                  <button key={q} onClick={() => goAsk(q)}
                          className="px-3 py-1.5 rounded-full border border-surface-border text-xs text-slate-400 hover:text-slate-200 hover:border-accent/50 transition-colors">
                    {q}
                  </button>
                ))}
              </div>
            </section>

            {/* Today's executive brief — composed overnight, read here. */}
            <Panel title="Today's executive brief"
                   action={<Link to="/reports" className="btn-quiet">Full brief →</Link>}>
              {brief.loading ? <PanelEmpty text="Composing…" /> : brief.error ? (
                <PanelEmpty text="Brief unavailable." />
              ) : (
                <div className="space-y-3">
                  <p className="text-sm text-slate-300">
                    {(brief.data?.date || summary.date) ? `For ${brief.data?.date || summary.date}. ` : ''}
                    Portfolio health {health != null ? Math.round(health) : '—'} ·{' '}
                    {(brief.data?.high_priority_issues ?? summary.high_priority_issues ?? 0)} high-priority issue(s) ·{' '}
                    {summary.open_action_items ?? 0} open action item(s).
                  </p>
                  {(brief.data?.recommendations || []).length > 0 && (
                    <div>
                      <div className="eyebrow mb-1.5">Recommended focus</div>
                      <ul className="space-y-1.5">
                        {brief.data.recommendations.slice(0, 3).map((r, i) => (
                          <li key={i} className="text-sm text-slate-300 flex gap-2">
                            <Badge tone="accent">rec</Badge>
                            <span>{r.action || r.recommendation || r.title}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}
                </div>
              )}
            </Panel>

            {/* Decision Intelligence: what the Brain proposes, ranked. */}
            <div className="grid gap-5 lg:grid-cols-2">
              <Panel title="Top decisions"
                     action={<Link to="/decisions" className="btn-quiet">All decisions →</Link>}>
                {intel.loading ? <PanelEmpty text="Reasoning…" /> : topDecisions.length === 0 ? (
                  <PanelEmpty text="No open decisions — the Brain has nothing urgent to propose." />
                ) : (
                  <ul className="space-y-3">
                    {topDecisions.slice(0, 5).map((d) => (
                      <li key={d.decision_id} className="text-sm">
                        <div className="flex items-start justify-between gap-3">
                          <div className="min-w-0">
                            <div className="text-slate-200">
                              <Badge tone={d.priority <= 2 ? 'danger' : 'accent'}>P{d.priority}</Badge>{' '}
                              {d.action}
                            </div>
                            <div className="text-slate-500 text-xs mt-0.5 truncate">
                              {d.kind} · confidence {Math.round((d.confidence ?? 0) * 100)}% · score {d.score}
                              {d.status !== 'proposed' ? ` · ${d.status}` : ''}
                            </div>
                          </div>
                          {(d.status === 'proposed' || d.status === 'modified') && (
                            <span className="shrink-0 space-x-2.5 text-xs">
                              <button onClick={() => decide(d.decision_id, 'approved')}
                                      className="text-emerald-400 hover:underline">Approve</button>
                              <button onClick={() => decide(d.decision_id, 'rejected')}
                                      className="text-slate-500 hover:underline">Reject</button>
                            </span>
                          )}
                        </div>
                      </li>
                    ))}
                  </ul>
                )}
              </Panel>

              <Panel title="Recommended actions">
                {intel.loading ? <PanelEmpty text="Ranking…" /> : recommended.length === 0 ? (
                  <PanelEmpty text="No recommendations awaiting a call." />
                ) : (
                  <ul className="space-y-3">
                    {recommended.slice(0, 5).map((r) => (
                      <li key={r.decision_id} className="text-sm">
                        <div className="text-slate-200">{r.action}</div>
                        {r.reasoning && (
                          <div className="text-slate-500 text-xs mt-0.5">{r.reasoning}</div>
                        )}
                      </li>
                    ))}
                  </ul>
                )}
              </Panel>
            </div>

            <div className="grid gap-5 lg:grid-cols-3">
              <Panel title="Completed overnight"
                     action={<Link to="/dashboard" className="btn-quiet">Activity →</Link>}>
                {overnight.loading ? <PanelEmpty text="Loading…" /> : overnight.data ? (
                  <div className="space-y-3">
                    <div className="flex flex-wrap gap-x-5 gap-y-1.5 text-sm text-slate-400">
                      <span><span className="text-slate-100 font-semibold tabular-nums">{overnight.data.totals?.workflows ?? 0}</span> workflows</span>
                      <span><span className="text-slate-100 font-semibold tabular-nums">{overnight.data.totals?.reports ?? 0}</span> reports</span>
                      <span><span className="text-slate-100 font-semibold tabular-nums">{overnight.data.totals?.awaiting_approval ?? 0}</span> awaiting approval</span>
                      <span><span className="text-slate-100 font-semibold tabular-nums">{overnight.data.totals?.notifications ?? 0}</span> alerts</span>
                    </div>
                    {(overnight.data.awaiting_approval || []).length > 0 && (
                      <ul className="space-y-1.5">
                        {overnight.data.awaiting_approval.slice(0, 3).map((a) => (
                          <li key={a.action_id} className="text-sm text-slate-400 truncate">• {a.title}</li>
                        ))}
                      </ul>
                    )}
                  </div>
                ) : <PanelEmpty text="Nothing ran overnight yet." />}
              </Panel>

              <Panel title="Recent decisions"
                     action={<Link to="/decisions" className="btn-quiet">All decisions →</Link>}>
                {decisions.length === 0 ? <PanelEmpty text="No decisions recorded yet." /> : (
                  <ul className="space-y-2.5">
                    {decisions.slice(0, 5).map((d, i) => (
                      <li key={i} className="text-sm">
                        <div className="text-slate-200 truncate">{d.decision || d.title}</div>
                        {(d.context || d.rationale) && (
                          <div className="text-slate-500 text-xs mt-0.5 truncate">{d.context || d.rationale}</div>
                        )}
                      </li>
                    ))}
                  </ul>
                )}
              </Panel>

              <Panel title="Organizational changes">
                {changes.length === 0 ? <PanelEmpty text="No recent changes recorded." /> : (
                  <ul className="space-y-2">
                    {changes.slice(0, 6).map((ch, i) => (
                      <li key={i} className="text-sm text-slate-400 truncate">
                        <span className="text-slate-200">{ch.kind}</span>
                        <span className="text-xs text-slate-500"> · {ch.summary}</span>
                      </li>
                    ))}
                  </ul>
                )}
              </Panel>
            </div>

            <div className="grid gap-5 lg:grid-cols-3">
              <Panel title="Needs your approval"
                     action={<Link to="/tasks" className="btn-quiet">All tasks →</Link>}>
                {approvals.length === 0 ? <PanelEmpty text="Nothing is waiting on you." /> : (
                  <ul className="space-y-2.5">
                    {approvals.slice(0, 5).map((a) => (
                      <li key={a.ref} className="flex items-start justify-between gap-3 text-sm">
                        <div className="min-w-0">
                          <div className="text-slate-200 truncate">{a.title}</div>
                          {a.detail && <div className="text-slate-500 text-xs mt-0.5 truncate">{a.detail}</div>}
                        </div>
                        {a.kind === 'action_approval' ? (
                          <span className="shrink-0 space-x-2.5 text-xs">
                            <button onClick={() => approve(a.ref)} className="text-emerald-400 hover:underline">Approve</button>
                            <button onClick={() => reject(a.ref)} className="text-slate-500 hover:underline">Reject</button>
                          </span>
                        ) : a.kind === 'report_review' ? (
                          <Link className="text-accent text-xs shrink-0" to="/reports">Review →</Link>
                        ) : (
                          <Link className="text-accent text-xs shrink-0" to="/tasks">Open →</Link>
                        )}
                      </li>
                    ))}
                  </ul>
                )}
              </Panel>

              <Panel title="Critical alerts"
                     action={<Link to="/notifications" className="btn-quiet">All alerts →</Link>}>
                {risks.length === 0 ? <PanelEmpty text="No open business risks." /> : (
                  <ul className="space-y-2.5">
                    {risks.slice(0, 5).map((r, i) => (
                      <li key={i} className="text-sm text-slate-300 flex gap-2">
                        <Badge tone="danger">risk</Badge><span>{r.insight}</span>
                      </li>
                    ))}
                  </ul>
                )}
              </Panel>

              <Panel title="Today's tasks"
                     action={<Link to="/tasks" className="btn-quiet">All tasks →</Link>}>
                {tasks.length === 0 ? <PanelEmpty text="No open tasks — enjoy the quiet." /> : (
                  <ul className="space-y-2.5">
                    {tasks.slice(0, 5).map((t) => (
                      <li key={t.task_id} className="flex items-start justify-between gap-3 text-sm">
                        <div className="min-w-0 truncate">
                          {t.priority && <Badge tone="accent">P{t.priority}</Badge>}{' '}
                          <span className="text-slate-200">{t.title}</span>
                        </div>
                        <button onClick={() => completeTask(t.task_id)}
                                className="text-emerald-400 text-xs shrink-0 hover:underline">Done ✓</button>
                      </li>
                    ))}
                  </ul>
                )}
              </Panel>
            </div>

            <div className="grid gap-5 lg:grid-cols-2">
              <Panel title="Recent reports" action={<Link to="/reports" className="btn-quiet">Report center →</Link>}>
                {(ws.recent_reports || []).length === 0 ? <PanelEmpty text="No reports yet." /> : (
                  <ul className="space-y-2">
                    {ws.recent_reports.slice(0, 5).map((r, i) => (
                      <li key={i} className="flex justify-between gap-3 text-sm">
                        <Link to={`/reports/${r.project_id}`} className="text-slate-200 hover:text-accent truncate">{r.title}</Link>
                        <span className="text-slate-500 shrink-0 tabular-nums">
                          {r.health_score != null ? `health ${Math.round(r.health_score)}` : ''}
                        </span>
                      </li>
                    ))}
                  </ul>
                )}
              </Panel>

              <Panel title="Growth opportunities" action={<Link to="/dashboard" className="btn-quiet">Dashboard →</Link>}>
                {(ws.growth_opportunities || []).length === 0 ? <PanelEmpty text="None surfaced yet." /> : (
                  <ul className="space-y-2.5">
                    {ws.growth_opportunities.slice(0, 5).map((o, i) => (
                      <li key={i} className="text-sm text-slate-300 flex gap-2">
                        <Badge tone="success">opportunity</Badge><span>{o.insight}</span>
                      </li>
                    ))}
                  </ul>
                )}
              </Panel>
            </div>
          </div>
        )
      }}
    </AsyncSection>
  )
}
