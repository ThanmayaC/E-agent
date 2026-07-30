// Runtime — the autonomous execution layer: queue, actions, goals,
// triggers, decisions, and metrics.
import { useState } from 'react'
import { api } from '../../api/client'
import {
  AsyncSection, Badge, PageHeader, Panel, PanelEmpty, Stat, useAsync, when,
} from '../../components/ui'

const statusTone = {
  completed: 'success', executed: 'success', running: 'info', failed: 'danger',
  rejected: 'danger', pending_approval: 'warn', approved: 'accent',
}

export default function AdminRuntime() {
  const [refresh, setRefresh] = useState(0)
  const state = useAsync(async () => {
    const [status, activity, goals, metrics, triggers, decisions] = await Promise.all([
      api.runtimeStatus(),
      api.runtimeActivity(15).catch(() => null),
      api.runtimeGoals().catch(() => null),
      api.runtimeMetrics().catch(() => null),
      api.runtimeTriggers().catch(() => null),
      api.runtimeDecisions().catch(() => null),
    ])
    return { status, activity, goals, metrics, triggers, decisions }
  }, [refresh])
  const reload = () => setRefresh((n) => n + 1)

  const approve = (id) => api.approveAction(id, 'admin').then(reload)
  const reject = (id) => api.rejectAction(id, 'admin', 'rejected from admin console').then(reload)

  return (
    <>
      <PageHeader title="Runtime" subtitle="Autonomous execution: action queue, goals, triggers, and decision log" />
      <AsyncSection state={state} empty="The runtime is not active.">
        {({ status, activity, goals, metrics, triggers, decisions }) => (
          <div className="space-y-5">
            <div className="grid gap-4 md:grid-cols-4">
              <Stat label="Autonomy" value={status.autonomy}
                    tone={status.running ? 'fg-success' : 'fg-muted'} />
              <Stat label="Queue pending" value={status.queue?.pending_approval} tone="fg-warn" />
              <Stat label="In flight" value={status.queue?.in_flight} />
              <Stat label="Autonomous decisions" value={status.decisions?.autonomous} />
            </div>

            <div className="grid gap-5 lg:grid-cols-2">
              <Panel title="Pending approvals">
                {(activity?.pending_approvals || []).length === 0 ? <PanelEmpty text="Queue is clear." /> : (
                  <ul className="space-y-2.5">
                    {activity.pending_approvals.map((a) => (
                      <li key={a.action_id} className="flex items-start justify-between gap-3 text-sm">
                        <div className="min-w-0">
                          <Badge tone="warn">{(a.kind || '').replace(/_/g, ' ')}</Badge>{' '}
                          <span className="text-slate-200">{a.title}</span>
                          {a.detail && <div className="text-slate-500 text-xs mt-0.5">{a.detail}</div>}
                        </div>
                        <span className="shrink-0 space-x-2.5 text-xs">
                          <button onClick={() => approve(a.action_id)} className="fg-success hover:underline">Approve</button>
                          <button onClick={() => reject(a.action_id)} className="text-slate-500 hover:underline">Reject</button>
                        </span>
                      </li>
                    ))}
                  </ul>
                )}
              </Panel>

              <Panel title="Goals">
                {(goals?.progress?.goals || []).length === 0 ? <PanelEmpty text="No goals defined." /> : (
                  <ul className="space-y-3">
                    {goals.progress.goals.map((g) => (
                      <li key={g.goal_id} className="text-sm">
                        <div className="flex justify-between gap-3">
                          <span className="text-slate-200">{g.objective}</span>
                          <span className="shrink-0 text-slate-500 text-xs tabular-nums">
                            {Math.round((g.progress || 0) * 100)}%{g.days_remaining != null && ` · ${g.days_remaining}d left`}
                          </span>
                        </div>
                        <div className="h-1.5 w-full rounded bg-surface-overlay mt-1">
                          <div className={`h-1.5 rounded ${g.progress >= 0.75 ? 'bg-[var(--status-success-fg)]' : g.progress >= 0.4 ? 'bg-[var(--status-warn-fg)]' : 'bg-[var(--status-danger-fg)]'}`}
                               style={{ width: `${Math.round((g.progress || 0) * 100)}%` }} />
                        </div>
                        {g.status === 'at_risk' && <Badge tone="danger">at risk</Badge>}
                      </li>
                    ))}
                  </ul>
                )}
              </Panel>

              <Panel title="Recent actions">
                {(activity?.recent_actions || []).length === 0 ? <PanelEmpty text="No actions yet." /> : (
                  <ul className="space-y-2">
                    {activity.recent_actions.map((a) => (
                      <li key={a.action_id} className="flex justify-between gap-3 text-sm">
                        <span className="text-slate-300 min-w-0 truncate">
                          <Badge tone={statusTone[a.status] || 'default'}>{(a.status || '').replace(/_/g, ' ')}</Badge>{' '}
                          {a.title}
                        </span>
                        <span className="text-slate-500 text-xs shrink-0">{when(a.updated_at)}</span>
                      </li>
                    ))}
                  </ul>
                )}
              </Panel>

              <Panel title="Workflow runs">
                {(activity?.recent_runs || []).length === 0 ? <PanelEmpty text="No workflow runs yet." /> : (
                  <ul className="space-y-2">
                    {activity.recent_runs.map((r) => (
                      <li key={r.run_id} className="flex justify-between gap-3 text-sm">
                        <span className="text-slate-300">
                          <Badge tone={statusTone[r.status] || 'default'}>{r.status}</Badge>{' '}
                          <span className="font-mono text-xs">{r.workflow}</span>
                        </span>
                        <span className="text-slate-500 text-xs shrink-0">{when(r.started_at)}</span>
                      </li>
                    ))}
                  </ul>
                )}
              </Panel>

              <Panel title="Trigger rules">
                {(triggers?.triggers || triggers?.rules || []).length === 0 ? <PanelEmpty text="No trigger rules." /> : (
                  <ul className="space-y-2 text-sm">
                    {(triggers.triggers || triggers.rules).map((t, i) => (
                      <li key={t.rule_id || i} className="flex justify-between gap-3">
                        <span className="text-slate-300 font-mono text-xs">{t.name || t.rule_id || t.kind}</span>
                        <Badge tone={t.enabled === false ? 'default' : 'success'}>{t.enabled === false ? 'off' : 'on'}</Badge>
                      </li>
                    ))}
                  </ul>
                )}
              </Panel>

              <Panel title="Metrics">
                {!metrics ? <PanelEmpty text="No metrics." /> : (
                  <div className="grid grid-cols-2 gap-3 text-sm">
                    {Object.entries(metrics).filter(([, v]) => typeof v === 'number' || typeof v === 'string').slice(0, 10).map(([k, v]) => (
                      <div key={k} className="flex justify-between gap-2">
                        <span className="text-slate-500 font-mono text-xs">{k}</span>
                        <span className="text-slate-200 tabular-nums">{String(v)}</span>
                      </div>
                    ))}
                  </div>
                )}
              </Panel>
            </div>

            <Panel title="Decision log (autonomous)">
              {(decisions?.decisions || []).length === 0 ? <PanelEmpty text="No autonomous decisions recorded." /> : (
                <ul className="space-y-2 text-sm">
                  {(decisions.decisions || []).slice(0, 12).map((d, i) => (
                    <li key={i} className="flex justify-between gap-3">
                      <span className="text-slate-300 min-w-0 truncate">{d.decision || d.title || d.summary}</span>
                      <span className="text-slate-500 text-xs shrink-0">{when(d.decided_at || d.created_at)}</span>
                    </li>
                  ))}
                </ul>
              )}
            </Panel>
          </div>
        )}
      </AsyncSection>
    </>
  )
}
