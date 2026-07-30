// Jobs — the scheduled job registry: run manually, enable, disable, and
// inspect recent executions.
import { useState } from 'react'
import { api } from '../../api/client'
import {
  AsyncSection, Badge, Notice, PageHeader, Panel, PanelEmpty, useAsync, when,
} from '../../components/ui'

const statusTone = { completed: 'success', running: 'info', failed: 'danger' }

export default function AdminJobs() {
  const [refresh, setRefresh] = useState(0)
  const [error, setError] = useState('')
  const state = useAsync(async () => {
    const [jobs, executions] = await Promise.all([
      api.runtimeJobs(),
      api.runtimeExecutions(30).catch(() => null),
    ])
    return { jobs, executions }
  }, [refresh])
  const reload = () => setRefresh((n) => n + 1)

  const run = (name) => { setError(''); api.runJob(name).then(reload).catch((e) => setError(String(e.message || e))) }
  const setEnabled = (name, enabled) => {
    setError('')
    api.setJobEnabled(name, enabled).then(reload).catch((e) => setError(String(e.message || e)))
  }

  return (
    <>
      <PageHeader title="Jobs" subtitle="Scheduled job registry and execution history" />
      {error && <div className="mb-4"><Notice tone="danger" onDismiss={() => setError('')}>{error}</Notice></div>}
      <AsyncSection state={state} empty="No jobs registered.">
        {({ jobs, executions }) => {
          const jobList = jobs?.jobs || (Array.isArray(jobs) ? jobs : [])
          const execList = executions?.executions || (Array.isArray(executions) ? executions : [])
          return (
            <div className="space-y-5">
              <Panel title="Registry">
                {jobList.length === 0 ? <PanelEmpty text="No jobs." /> : (
                  <div className="overflow-x-auto">
                    <table className="table-base">
                      <thead><tr><th>Job</th><th>Description</th><th>Status</th><th>Last run</th><th className="!text-right">Actions</th></tr></thead>
                      <tbody>
                        {jobList.map((j) => (
                          <tr key={j.name}>
                            <td className="font-mono text-xs text-slate-200 whitespace-nowrap">{j.name}</td>
                            <td className="text-xs max-w-[26rem]">{j.description}</td>
                            <td><Badge tone={j.enabled ? (j.status === 'degraded' ? 'danger' : 'success') : 'default'}>
                              {j.enabled ? j.status || 'ok' : 'disabled'}</Badge></td>
                            <td className="text-xs whitespace-nowrap">{when(j.last_run_at)}</td>
                            <td className="text-right whitespace-nowrap space-x-3 text-xs">
                              <button onClick={() => run(j.name)} className="text-accent hover:underline">Run now</button>
                              <button onClick={() => setEnabled(j.name, !j.enabled)} className="text-slate-400 hover:underline">
                                {j.enabled ? 'Disable' : 'Enable'}
                              </button>
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                )}
              </Panel>

              <Panel title="Recent executions">
                {execList.length === 0 ? <PanelEmpty text="No executions yet." /> : (
                  <ul className="space-y-2 text-sm">
                    {execList.map((e) => (
                      <li key={e.execution_id} className="flex justify-between gap-3">
                        <span className="text-slate-300 min-w-0 truncate">
                          <Badge tone={statusTone[e.status] || 'default'}>{e.status}</Badge>{' '}
                          <span className="font-mono text-xs">{e.job}</span>
                          {e.error && <span className="fg-danger text-xs ml-2">{String(e.error).slice(0, 80)}</span>}
                        </span>
                        <span className="text-slate-500 text-xs shrink-0">{when(e.started_at)}</span>
                      </li>
                    ))}
                  </ul>
                )}
              </Panel>
            </div>
          )
        }}
      </AsyncSection>
    </>
  )
}
