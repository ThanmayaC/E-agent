// Workflow Execution Monitor (V2.5) — what the autonomous platform is
// running, what just ran, and what it can run. Reads /runtime/activity,
// /runtime/executions, and /platform/workflows. Live-refreshing; filterable
// by status. No backend logic — a window onto the scheduler's own records.
import { useEffect, useMemo, useState } from 'react'
import { api } from '../api/client'
import { useAsync } from '../components/ui'
import { timeAgo, when } from '../components/ui'
import {
  ExportMenu, FilterChips, Loader, PremiumHeader, Reveal, StatCard,
  Stagger, StaggerItem,
} from '../components/premium'

const STATUS_TONE = {
  completed: 'text-emerald-400 bg-emerald-500/10',
  running: 'text-accent bg-accent/10',
  failed: 'text-rose-400 bg-rose-500/10',
  degraded: 'text-amber-400 bg-amber-500/10',
  pending: 'text-slate-400 bg-surface-overlay',
}

function dur(a, b) {
  if (!a || !b) return null
  const ms = new Date(b) - new Date(a)
  if (ms < 0) return null
  return ms < 1000 ? `${ms}ms` : `${(ms / 1000).toFixed(1)}s`
}

export default function WorkflowMonitor() {
  const [tick, setTick] = useState(0)
  const [live, setLive] = useState(true)
  const [statusFilter, setStatusFilter] = useState('')

  useEffect(() => {
    if (!live) return
    const id = setInterval(() => setTick((n) => n + 1), 5000)
    return () => clearInterval(id)
  }, [live])

  const activity = useAsync(() => api.runtimeActivity(30), [tick])
  const execs = useAsync(() => api.runtimeExecutions(80), [tick])
  const catalog = useAsync(() => api.platformWorkflows().catch(() => []), [])

  const executions = execs.data || []
  const counts = useMemo(() => {
    const m = {}
    executions.forEach((e) => { m[e.status] = (m[e.status] || 0) + 1 })
    return Object.entries(m).map(([value, count]) => ({ value, label: value, count }))
  }, [executions])

  const filtered = useMemo(
    () => executions.filter((e) => !statusFilter || e.status === statusFilter),
    [executions, statusFilter])

  const running = activity.data?.running_workflows || []
  const recentRuns = activity.data?.recent_runs || []

  return (
    <div>
      <PremiumHeader title="Workflow Execution Monitor" badge={live ? 'Live' : 'Paused'}
        subtitle="Every job and workflow the autonomous platform runs — live, with history and outcomes.">
        <button className="btn-ghost" onClick={() => setLive((v) => !v)}>
          <span className={live ? 'text-emerald-400' : 'text-slate-500'}>●</span> {live ? 'Live' : 'Paused'}
        </button>
        <ExportMenu filename="workflow-executions"
          rows={executions.map((e) => ({ job: e.job, status: e.status, reason: e.reason,
            started: e.started_at, finished: e.finished_at, attempts: e.attempts, error: e.error }))} />
      </PremiumHeader>

      <Loader state={execs}>
        {() => {
          const total = executions.length
          const failed = executions.filter((e) => e.status === 'failed').length
          const ok = executions.filter((e) => e.status === 'completed').length
          return (
            <div className="space-y-6">
              <Stagger className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
                <StaggerItem><StatCard label="Running now" value={running.length}
                  tone={running.length ? 'text-accent' : 'fg-primary'} /></StaggerItem>
                <StaggerItem><StatCard label="Executions (recent)" value={total} /></StaggerItem>
                <StaggerItem><StatCard label="Completed" value={ok} tone="fg-success" /></StaggerItem>
                <StaggerItem><StatCard label="Failed" value={failed}
                  tone={failed ? 'fg-danger' : 'fg-primary'} /></StaggerItem>
              </Stagger>

              {running.length > 0 && (
                <Reveal>
                  <div className="card-pad border-accent/30">
                    <h2 className="text-sm font-semibold text-slate-200 mb-3 flex items-center gap-2">
                      <span className="w-2 h-2 rounded-full bg-accent animate-pulse" /> Running now
                    </h2>
                    <div className="space-y-2">
                      {running.map((w) => (
                        <div key={w.run_id} className="flex items-center justify-between text-sm">
                          <span className="text-slate-200">{w.workflow}</span>
                          <span className="text-xs text-slate-500">{timeAgo(w.started_at)}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                </Reveal>
              )}

              <div className="grid gap-5 lg:grid-cols-3">
                <div className="lg:col-span-2">
                  <div className="flex items-center justify-between mb-3">
                    <h2 className="text-sm font-semibold text-slate-200">Execution history</h2>
                    <FilterChips options={counts} active={statusFilter} onChange={setStatusFilter}
                      allLabel={`All (${total})`} />
                  </div>
                  <div className="card overflow-hidden">
                    <div className="max-h-[560px] overflow-y-auto">
                      <table className="table-base">
                        <thead>
                          <tr><th>Job</th><th>Status</th><th>Trigger</th><th>Duration</th><th>When</th></tr>
                        </thead>
                        <tbody>
                          {filtered.map((e) => (
                            <tr key={e.execution_id} className="hover:bg-surface-overlay/40">
                              <td className="text-slate-200">
                                {e.job}
                                {e.error && <div className="text-[11px] text-rose-400/80 truncate max-w-xs">{e.error}</div>}
                              </td>
                              <td>
                                <span className={`px-2 py-0.5 rounded-md text-[11px] font-medium capitalize ${STATUS_TONE[e.status] || STATUS_TONE.pending}`}>
                                  {e.status}
                                </span>
                              </td>
                              <td className="text-slate-500 text-xs">{e.reason}</td>
                              <td className="text-slate-400 text-xs tabular-nums">{dur(e.started_at, e.finished_at) || '—'}</td>
                              <td className="text-slate-500 text-xs" title={when(e.started_at)}>{timeAgo(e.started_at)}</td>
                            </tr>
                          ))}
                          {filtered.length === 0 && (
                            <tr><td colSpan={5} className="text-center text-slate-600 py-8">No executions match.</td></tr>
                          )}
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>

                <div className="space-y-5">
                  <div className="card-pad">
                    <h2 className="text-sm font-semibold text-slate-200 mb-3">Recent workflow runs</h2>
                    <div className="space-y-2">
                      {recentRuns.slice(0, 8).map((r) => (
                        <div key={r.run_id} className="flex items-center justify-between gap-2 text-sm">
                          <span className="text-slate-300 truncate">{r.workflow}</span>
                          <span className={`shrink-0 px-1.5 py-0.5 rounded text-[10px] capitalize ${STATUS_TONE[r.status] || STATUS_TONE.pending}`}>
                            {r.status}
                          </span>
                        </div>
                      ))}
                      {recentRuns.length === 0 && <div className="text-sm text-slate-500">No recent runs.</div>}
                    </div>
                  </div>

                  <div className="card-pad">
                    <h2 className="text-sm font-semibold text-slate-200 mb-3">Workflow catalog</h2>
                    <div className="space-y-1.5">
                      {(catalog.data || []).map((w) => (
                        <div key={w.name} className="flex items-center justify-between gap-2 text-sm">
                          <span className="text-slate-300 truncate">{w.name.replace(/_/g, ' ')}</span>
                          <span className={`shrink-0 w-2 h-2 rounded-full ${w.available ? 'bg-emerald-400' : 'bg-slate-600'}`}
                            title={w.available ? 'available' : w.unavailable_reason || 'unavailable'} />
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          )
        }}
      </Loader>
    </div>
  )
}
