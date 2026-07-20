// Executive Dashboard — the whole business on one screen.
// Sections: Today's Summary, Critical Alerts, Portfolio Health, Top
// Opportunities, Products At Risk, Pending Approvals, Recent Reports,
// Recommended Actions, Upcoming Deadlines, AI Executive Brief.
import { useState } from 'react'
import { Link } from 'react-router-dom'
import { api } from '../api/client'
import OvernightSummary from '../components/OvernightSummary'
import {
  AsyncSection, Badge, HealthRing, PageHeader, Panel, PanelEmpty, Stat, Trend,
  healthTone, useAsync,
} from '../components/ui'

export default function ExecutiveDashboard() {
  const [refresh, setRefresh] = useState(0)
  const [regenerating, setRegenerating] = useState(false)
  const state = useAsync(async () => {
    const [ws, brief, products] = await Promise.all([
      api.managerWorkspace(),
      api.dailyBrief().catch(() => null),
      api.managerProducts().catch(() => null),
    ])
    return { ws, brief, products }
  }, [refresh])
  const reload = () => setRefresh((n) => n + 1)

  const regenerateBrief = async () => {
    setRegenerating(true)
    try { await api.dailyBrief(true) } finally { setRegenerating(false); reload() }
  }
  const actionId = (ref) => ref.replace(/^action:/, '')
  const approve = (ref) => api.approveAction(actionId(ref), 'executive').then(reload)
  const reject = (ref) => api.rejectAction(actionId(ref), 'executive', 'rejected from the dashboard').then(reload)
  const acceptTask = (id) => api.setTaskStatus(id, 'pending').then(reload)
  const dismissTask = (id) => api.setTaskStatus(id, 'dismissed').then(reload)

  return (
    <>
      <PageHeader title="Executive Dashboard" subtitle="Business health, priorities, and what changed — updated continuously" />
      <AsyncSection state={state} empty="No business data yet — connect a data source under Settings.">
        {({ ws, brief, products }) => {
          const summary = ws.todays_summary || {}
          const ph = ws.portfolio_health || {}
          const approvals = ws.pending_approvals || []
          const deadlines = brief?.upcoming_deadlines || []
          const atRisk = products?.attention || []
          return (
            <div className="space-y-5">
              {/* Today's Summary */}
              <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
                <div className="card-pad flex items-center gap-4">
                  <HealthRing score={ph.average_health_score} size={64} />
                  <div>
                    <div className="eyebrow">Portfolio health</div>
                    <div className={`text-sm mt-1 font-medium ${healthTone(ph.average_health_score)}`}>
                      {ph.average_health_score == null ? 'Not measured yet'
                        : ph.average_health_score >= 70 ? 'Healthy'
                        : ph.average_health_score >= 50 ? 'Needs attention' : 'At risk'}
                    </div>
                    <div className="text-xs text-slate-500 mt-0.5">{ph.projects_total ?? 0} businesses tracked</div>
                  </div>
                </div>
                <Stat label="High-priority issues" value={(summary.high_priority_issues || []).length}
                      tone={(summary.high_priority_issues || []).length > 0 ? 'text-rose-400' : 'text-slate-100'}
                      hint="from today's brief" />
                <Stat label="Awaiting your approval" value={approvals.length}
                      tone={approvals.length > 0 ? 'text-amber-400' : 'text-slate-100'}
                      hint="approvals and reviews" />
                <Stat label="Open action items" value={summary.open_action_items}
                      hint={`${summary.unread_notifications ?? 0} unread notifications`} />
              </div>

              {/* Overnight Summary (V2 — the autonomous platform's report) */}
              <OvernightSummary />

              {/* AI Executive Brief */}
              <Panel title="AI Executive Brief"
                     action={
                       <div className="flex items-center gap-3">
                         {brief?.generated_at && (
                           <span className="text-xs text-slate-600">
                             {brief.date} · {new Date(brief.generated_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                           </span>
                         )}
                         <button onClick={regenerateBrief} disabled={regenerating} className="btn-ghost !py-1 !text-xs">
                           {regenerating ? 'Regenerating…' : 'Regenerate'}
                         </button>
                       </div>
                     }>
                {!brief ? <PanelEmpty text="No brief yet — it is generated automatically each day." /> : (
                  <div className="grid gap-4 md:grid-cols-2">
                    <div>
                      <div className="h-sub mb-2">High-priority issues</div>
                      {(brief.high_priority_issues || []).length === 0
                        ? <PanelEmpty text="No open issues." />
                        : <ul className="space-y-1.5">
                            {brief.high_priority_issues.slice(0, 4).map((i, k) => (
                              <li key={k} className="text-sm text-slate-300">
                                <Badge tone="danger">{(i.kind || 'issue').replace(/_/g, ' ')}</Badge> {i.title}
                              </li>
                            ))}
                          </ul>}
                      <div className="h-sub mb-2 mt-4">What changed</div>
                      {(brief.portfolio_changes || []).length === 0
                        ? <PanelEmpty text="No material changes." />
                        : <ul className="space-y-1.5">
                            {brief.portfolio_changes.slice(0, 4).map((c, k) => (
                              <li key={k} className="text-sm text-slate-300 flex items-center gap-2">
                                <Trend change={c.change} /> {c.project_id}: {c.previous} → {c.latest}
                              </li>
                            ))}
                          </ul>}
                    </div>
                    <div>
                      <div className="h-sub mb-2">Recommendations</div>
                      {(brief.recommendations || []).length === 0
                        ? <PanelEmpty text="No recommendations right now." />
                        : <ul className="space-y-1.5">
                            {brief.recommendations.slice(0, 4).map((r, k) => (
                              <li key={k} className="text-sm text-slate-300">
                                {r.priority && <Badge tone="accent">P{r.priority}</Badge>} {r.action}
                              </li>
                            ))}
                          </ul>}
                      <div className="h-sub mb-2 mt-4">Important reports</div>
                      {(brief.important_reports || []).length === 0
                        ? <PanelEmpty text="No recent reports." />
                        : <ul className="space-y-1.5">
                            {brief.important_reports.slice(0, 4).map((r, k) => (
                              <li key={k} className="text-sm text-slate-300 flex justify-between gap-3">
                                <span className="truncate">{r.title}</span>
                                {r.health_score != null &&
                                  <span className={`shrink-0 tabular-nums text-xs ${healthTone(r.health_score)}`}>
                                    {Math.round(r.health_score)}
                                  </span>}
                              </li>
                            ))}
                          </ul>}
                    </div>
                  </div>
                )}
              </Panel>

              <div className="grid gap-5 lg:grid-cols-2">
                {/* Critical Alerts */}
                <Panel title="Critical alerts" action={<Link to="/notifications" className="btn-quiet">All →</Link>}>
                  {(ws.critical_risks || []).length === 0 ? <PanelEmpty text="No open business risks." /> : (
                    <ul className="space-y-2.5">
                      {ws.critical_risks.slice(0, 6).map((r, i) => (
                        <li key={i} className="text-sm text-slate-300 flex gap-2">
                          <Badge tone="danger">risk</Badge><span>{r.insight}</span>
                        </li>
                      ))}
                    </ul>
                  )}
                </Panel>

                {/* Top Opportunities */}
                <Panel title="Top opportunities" action={<Link to="/portfolio" className="btn-quiet">Portfolio →</Link>}>
                  {(ws.growth_opportunities || []).length === 0 ? <PanelEmpty text="None surfaced yet." /> : (
                    <ul className="space-y-2.5">
                      {ws.growth_opportunities.slice(0, 6).map((o, i) => (
                        <li key={i} className="text-sm text-slate-300 flex gap-2">
                          <Badge tone="success">opportunity</Badge><span>{o.insight}</span>
                        </li>
                      ))}
                    </ul>
                  )}
                </Panel>

                {/* Products At Risk */}
                <Panel title="Products at risk" action={<Link to="/portfolio" className="btn-quiet">Portfolio →</Link>}>
                  {atRisk.length === 0 ? <PanelEmpty text="No products need intervention right now." /> : (
                    <ul className="space-y-3">
                      {atRisk.slice(0, 5).map((p) => (
                        <li key={p.product_id} className="flex items-center gap-3 text-sm">
                          <HealthRing score={p.health_score} size={40} />
                          <div className="min-w-0 flex-1">
                            <Link to={`/portfolio/product/${encodeURIComponent(p.product_id)}`}
                                  className="text-slate-200 hover:text-accent truncate block">{p.product}</Link>
                            <div className="text-xs text-slate-500 truncate">{p.priority_reason || p.investment_priority}</div>
                          </div>
                          <Trend change={p.change} />
                        </li>
                      ))}
                    </ul>
                  )}
                </Panel>

                {/* Pending Approvals */}
                <Panel title="Pending approvals" action={<Link to="/decisions" className="btn-quiet">Decisions →</Link>}>
                  {approvals.length === 0 ? <PanelEmpty text="Nothing awaiting your approval." /> : (
                    <ul className="space-y-2.5">
                      {approvals.slice(0, 6).map((a) => (
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
                          ) : (
                            <Link className="text-accent text-xs shrink-0"
                                  to={a.kind === 'report_review' ? '/reports' : '/tasks'}>Open →</Link>
                          )}
                        </li>
                      ))}
                    </ul>
                  )}
                </Panel>

                {/* Recent Reports */}
                <Panel title="Recent reports" action={<Link to="/reports" className="btn-quiet">Report center →</Link>}>
                  {(ws.recent_reports || []).length === 0 ? <PanelEmpty text="No reports yet." /> : (
                    <ul className="space-y-2">
                      {ws.recent_reports.slice(0, 6).map((r, i) => (
                        <li key={i} className="flex justify-between gap-3 text-sm">
                          <Link to={`/reports/${r.project_id}`} className="text-slate-200 hover:text-accent truncate">{r.title}</Link>
                          {r.health_score != null &&
                            <span className={`shrink-0 tabular-nums text-xs ${healthTone(r.health_score)}`}>
                              health {Math.round(r.health_score)}
                            </span>}
                        </li>
                      ))}
                    </ul>
                  )}
                </Panel>

                {/* Recommended Actions */}
                <Panel title="Recommended actions" action={<Link to="/tasks" className="btn-quiet">Tasks →</Link>}>
                  {(ws.suggested_actions || []).length === 0 ? <PanelEmpty text="No suggestions right now." /> : (
                    <ul className="space-y-2.5">
                      {ws.suggested_actions.slice(0, 6).map((t) => (
                        <li key={t.task_id} className="flex items-start justify-between gap-3 text-sm">
                          <span className="text-slate-300 min-w-0 truncate">{t.title}</span>
                          <span className="shrink-0 space-x-2.5 text-xs">
                            <button onClick={() => acceptTask(t.task_id)} className="text-accent hover:underline">Accept</button>
                            <button onClick={() => dismissTask(t.task_id)} className="text-slate-500 hover:underline">Dismiss</button>
                          </span>
                        </li>
                      ))}
                    </ul>
                  )}
                </Panel>

                {/* Upcoming Deadlines */}
                <Panel title="Upcoming deadlines" action={<Link to="/tasks" className="btn-quiet">Tasks →</Link>}>
                  {deadlines.length === 0 ? <PanelEmpty text="No deadlines in the next 7 days." /> : (
                    <ul className="space-y-2">
                      {deadlines.slice(0, 6).map((t, i) => (
                        <li key={i} className="flex justify-between gap-3 text-sm">
                          <span className="text-slate-300 truncate">{t.title}</span>
                          <span className="text-amber-400 text-xs shrink-0">due {t.due_date}</span>
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
    </>
  )
}
