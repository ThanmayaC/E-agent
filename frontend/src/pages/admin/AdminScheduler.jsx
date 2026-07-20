// Scheduler — heartbeat control and schedule health.
import { useState } from 'react'
import { api } from '../../api/client'
import {
  AsyncSection, Badge, PageHeader, Panel, PanelEmpty, Stat, useAsync, when,
} from '../../components/ui'

export default function AdminScheduler() {
  const [refresh, setRefresh] = useState(0)
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState('')
  const state = useAsync(async () => {
    const [status, jobs] = await Promise.all([api.runtimeStatus(), api.runtimeJobs().catch(() => null)])
    return { status, jobs }
  }, [refresh])
  const reload = () => setRefresh((n) => n + 1)

  const toggleScheduler = async (running) => {
    setBusy(true); setError('')
    try { await (running ? api.stopScheduler() : api.startScheduler()) }
    catch (e) { setError(String(e.message || e)) }
    finally { setBusy(false); reload() }
  }

  return (
    <>
      <PageHeader title="Scheduler" subtitle="The autonomous heartbeat: state, cadence, and degraded schedules" />
      {error && <div className="card-pad border-rose-500/40 text-rose-300 text-sm mb-4">{error}</div>}
      <AsyncSection state={state} empty="Scheduler unavailable.">
        {({ status, jobs }) => {
          const sched = status.scheduler || {}
          const jobList = jobs?.jobs || (Array.isArray(jobs) ? jobs : [])
          return (
            <div className="space-y-5">
              <div className="grid gap-4 md:grid-cols-4">
                <div className="card-pad">
                  <div className="eyebrow">Heartbeat</div>
                  <div className={`metric mt-1.5 !text-xl ${status.running ? 'text-emerald-400' : 'text-slate-400'}`}>
                    {status.running ? 'running' : 'stopped'}
                  </div>
                  <button className="btn-ghost !py-1 !text-xs mt-3" disabled={busy}
                          onClick={() => toggleScheduler(status.running)}>
                    {busy ? 'Working…' : status.running ? 'Stop scheduler' : 'Start scheduler'}
                  </button>
                </div>
                <Stat label="Jobs enabled" value={sched.jobs_enabled} />
                <Stat label="Jobs total" value={sched.jobs_total ?? jobList.length} />
                <Stat label="Degraded" value={(sched.degraded_jobs || []).length}
                      tone={(sched.degraded_jobs || []).length > 0 ? 'text-rose-400' : 'text-slate-100'} />
              </div>

              <Panel title="Degraded jobs">
                {(sched.degraded_jobs || []).length === 0
                  ? <PanelEmpty text="All schedules healthy." />
                  : <div className="flex gap-2 flex-wrap">{sched.degraded_jobs.map((j) => <Badge key={j} tone="danger">{j}</Badge>)}</div>}
              </Panel>

              <Panel title="Schedule">
                {jobList.length === 0 ? <PanelEmpty text="No scheduled jobs." /> : (
                  <div className="overflow-x-auto">
                    <table className="table-base">
                      <thead><tr><th>Job</th><th>Kind</th><th>Status</th><th>Last run</th><th>Next run</th></tr></thead>
                      <tbody>
                        {jobList.map((j) => (
                          <tr key={j.name}>
                            <td className="font-mono text-xs text-slate-200">{j.name}</td>
                            <td className="text-xs">{j.kind}</td>
                            <td><Badge tone={j.enabled ? (j.status === 'degraded' ? 'danger' : 'success') : 'default'}>
                              {j.enabled ? j.status || 'ok' : 'disabled'}</Badge></td>
                            <td className="text-xs">{when(j.last_run_at)}</td>
                            <td className="text-xs">{when(j.next_run_at)}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                )}
              </Panel>
            </div>
          )
        }}
      </AsyncSection>
    </>
  )
}
