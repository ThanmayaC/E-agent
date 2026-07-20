import { useState } from 'react'
import { useParams } from 'react-router-dom'
import { api } from '../api/client'
import { AsyncSection, Badge, Empty, PageHeader, useAsync } from '../components/ui'

// Workflow Monitoring — the autonomous side of the platform: registered
// workflows (available + planned), run history for this project, recurring
// schedules, and the agent/tool/connector catalogue behind them.
export default function Workflows() {
  const { projectId } = useParams()
  const [refresh, setRefresh] = useState(0)
  const defs = useAsync(() => api.platformWorkflows(), [refresh])
  const runs = useAsync(() => api.workflowRuns(projectId), [projectId, refresh])
  const schedules = useAsync(() => api.workflowSchedules(projectId), [projectId, refresh])
  const agents = useAsync(() => api.platformAgents(), [])
  const tools = useAsync(() => api.platformTools(), [])
  const connectors = useAsync(() => api.platformConnectors(), [])

  return (
    <>
      <PageHeader
        title="Workflows"
        subtitle="Autonomous workflows, run history, schedules, and the agents/tools/connectors that power them"
      />
      <div className="space-y-5">
        <div className="card-pad">
          <div className="h-title mb-3">Registered workflows</div>
          <AsyncSection state={defs}>
            {(list) => (
              <table className="table-base">
                <thead><tr><th>Workflow</th><th>Description</th><th>Status</th></tr></thead>
                <tbody>
                  {list.map((w) => (
                    <tr key={w.name}>
                      <td className="text-slate-200 font-medium">{w.name}</td>
                      <td className="text-slate-400">{w.description}</td>
                      <td>
                        {w.available
                          ? <Badge tone="success">available</Badge>
                          : <Badge tone="warn">planned — {w.unavailable_reason}</Badge>}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            )}
          </AsyncSection>
        </div>

        <div className="grid lg:grid-cols-2 gap-5">
          <div className="card-pad">
            <div className="h-title mb-3">Run history</div>
            <AsyncSection state={runs} empty="No workflow runs yet — click Analyze on the project.">
              {(list) => (
                <table className="table-base">
                  <thead><tr><th>Workflow</th><th>Status</th><th>Started</th><th>Finished</th></tr></thead>
                  <tbody>
                    {list.slice().reverse().map((r) => (
                      <tr key={r.run_id}>
                        <td className="text-slate-200">{r.workflow}</td>
                        <td>
                          <Badge tone={r.status === 'completed' ? 'success' : r.status === 'failed' ? 'danger' : 'info'}>
                            {r.status}
                          </Badge>
                          {r.error && <div className="text-xs text-rose-400 mt-1 max-w-[14rem] truncate">{r.error}</div>}
                        </td>
                        <td className="text-xs text-slate-500">{new Date(r.started_at).toLocaleString()}</td>
                        <td className="text-xs text-slate-500">{r.finished_at ? new Date(r.finished_at).toLocaleString() : '—'}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )}
            </AsyncSection>
          </div>

          <ScheduleCard projectId={projectId} schedules={schedules} onSaved={() => setRefresh((n) => n + 1)} />
        </div>

        <div className="grid lg:grid-cols-3 gap-5">
          <CatalogueCard title="Agents" state={agents}
                         render={(a) => ({ key: a.name, label: a.name, detail: a.role, available: true })} />
          <CatalogueCard title="Tools" state={tools}
                         render={(t) => ({ key: t.name, label: t.name, detail: t.description, available: t.available, reason: t.unavailable_reason })} />
          <CatalogueCard title="Data connectors" state={connectors}
                         render={(c) => ({ key: c.name, label: c.name, detail: c.description, available: c.available, reason: c.unavailable_reason })} />
        </div>
      </div>
    </>
  )
}

function ScheduleCard({ projectId, schedules, onSaved }) {
  const [workflow, setWorkflow] = useState('full_analysis')
  const [cadence, setCadence] = useState('weekly')
  const [busy, setBusy] = useState(false)
  const submit = async (e) => {
    e.preventDefault()
    setBusy(true)
    try {
      await api.addWorkflowSchedule(projectId, workflow, cadence)
      onSaved()
    } finally { setBusy(false) }
  }
  return (
    <div className="card-pad">
      <div className="h-title mb-3">Recurring schedules</div>
      <form onSubmit={submit} className="flex gap-2 mb-4">
        <select className="input" value={workflow} onChange={(e) => setWorkflow(e.target.value)}>
          <option value="full_analysis">full_analysis</option>
        </select>
        <select className="input" value={cadence} onChange={(e) => setCadence(e.target.value)}>
          <option value="daily">daily</option>
          <option value="weekly">weekly</option>
          <option value="monthly">monthly</option>
        </select>
        <button className="btn" disabled={busy}>{busy ? 'Saving…' : 'Schedule'}</button>
      </form>
      <AsyncSection state={schedules} empty="No recurring work scheduled.">
        {(list) => (
          <ul className="space-y-2 text-sm">
            {list.map((s) => (
              <li key={s.schedule_id} className="flex justify-between py-1.5 px-2 rounded hover:bg-surface-overlay/40">
                <span className="text-slate-300">{s.workflow}</span>
                <span className="flex items-center gap-2">
                  <Badge tone="info">{s.cadence}</Badge>
                  <Badge tone={s.active ? 'success' : 'default'}>{s.active ? 'active' : 'paused'}</Badge>
                </span>
              </li>
            ))}
          </ul>
        )}
      </AsyncSection>
    </div>
  )
}

function CatalogueCard({ title, state, render }) {
  return (
    <div className="card-pad">
      <div className="h-title mb-3">{title}</div>
      <AsyncSection state={state}>
        {(list) => (
          <ul className="space-y-2 text-sm">
            {list.map((item) => {
              const row = render(item)
              return (
                <li key={row.key} className="py-1.5 px-2 rounded hover:bg-surface-overlay/40">
                  <div className="flex justify-between gap-2">
                    <span className="text-slate-200 font-medium">{row.label}</span>
                    {row.available
                      ? <Badge tone="success">ready</Badge>
                      : <Badge tone="warn">planned</Badge>}
                  </div>
                  <div className="text-xs text-slate-500 mt-0.5">{row.detail}</div>
                  {!row.available && row.reason && (
                    <div className="text-[11px] text-amber-400/80 mt-0.5">{row.reason}</div>
                  )}
                </li>
              )
            })}
          </ul>
        )}
      </AsyncSection>
    </div>
  )
}
