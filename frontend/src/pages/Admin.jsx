import { useParams } from 'react-router-dom'
import { api } from '../api/client'
import { AsyncSection, Badge, PageHeader, useAsync } from '../components/ui'

export default function Admin() {
  const { projectId } = useParams()
  const state = useAsync(() => api.getProject(projectId), [projectId])

  return (
    <>
      <PageHeader title="Settings & Admin" subtitle="Project metadata, pipeline runs and platform configuration" />
      <AsyncSection state={state}>
        {(p) => (
          <div className="space-y-5">
            <div className="card-pad">
              <div className="h-title mb-3">Project</div>
              <div className="grid md:grid-cols-4 gap-4 text-sm">
                <div><div className="h-sub">Name</div><div className="text-slate-200 mt-1">{p.name}</div></div>
                <div><div className="h-sub">ID</div><div className="font-mono text-xs text-slate-400 mt-1">{p.project_id}</div></div>
                <div><div className="h-sub">Status</div><div className="mt-1"><Badge tone={p.status === 'ready' ? 'success' : 'warn'}>{p.status}</Badge></div></div>
                <div><div className="h-sub">Created</div><div className="text-slate-400 mt-1">{new Date(p.created_at).toLocaleString()}</div></div>
              </div>
            </div>

            <div className="card-pad">
              <div className="h-title mb-3">Uploaded files</div>
              <table className="table-base">
                <thead><tr><th>File</th><th>Size</th><th>Sheets</th><th>Hidden</th><th>Merged regions</th><th>Tables found</th></tr></thead>
                <tbody>
                  {p.files.map((f) => (
                    <tr key={f.file_name}>
                      <td className="text-slate-200">{f.file_name}</td>
                      <td>{(f.file_size / 1024).toFixed(0)} KB</td>
                      <td>{f.sheet_count}</td>
                      <td>{f.hidden_sheets.length ? f.hidden_sheets.join(', ') : '—'}</td>
                      <td>{f.merged_cell_regions}</td>
                      <td>{f.tables_found}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            <div className="card-pad">
              <div className="h-title mb-3">Pipeline stages (last run)</div>
              <div className="grid md:grid-cols-2 gap-1 text-sm">
                {p.stages.map((s) => (
                  <div key={s.stage} className="flex justify-between py-1.5 px-2 rounded hover:bg-surface-overlay/40">
                    <span className="text-slate-300">{s.stage.replace(/_/g, ' ')}</span>
                    <span className="flex items-center gap-2">
                      {s.detail && <span className="text-xs text-rose-400 max-w-[16rem] truncate">{s.detail}</span>}
                      <Badge tone={s.status === 'completed' ? 'success' : s.status === 'failed' ? 'danger' : 'default'}>{s.status}</Badge>
                    </span>
                  </div>
                ))}
              </div>
            </div>

            <div className="card-pad text-sm text-slate-500">
              Platform configuration is environment-driven (<span className="font-mono text-xs">EDIP_*</span> variables):
              LLM provider, embedding model, vector backend (memory / pgvector), Celery workers, thresholds.
              See <span className="font-mono text-xs">.env.example</span> and docs/INSTALLATION.md.
            </div>
          </div>
        )}
      </AsyncSection>
      <BrainPanel />
    </>
  )
}

// Technical status of the Enterprise Brain (admin-only view — executives
// see business-level operational status in the Executive Workspace).
function BrainPanel() {
  const state = useAsync(() => Promise.all([api.brainStatus(), api.brainStatistics()]), [])
  return (
    <div className="mt-5">
      <AsyncSection state={state} empty="Enterprise Brain status unavailable.">
        {([status, stats]) => (
          <div className="card-pad">
            <div className="h-title mb-3">
              Enterprise Brain{' '}
              <Badge tone={status.state === 'ready' ? 'success' : status.state === 'degraded' ? 'warn' : 'default'}>
                {status.state}
              </Badge>
            </div>
            <div className="grid md:grid-cols-4 gap-4 text-sm">
              <div><div className="h-sub">Knowledge entries</div>
                <div className="text-slate-200 mt-1">
                  {Object.values(stats.knowledge || {}).reduce((a, b) => a + b, 0)}</div></div>
              <div><div className="h-sub">Graph</div>
                <div className="text-slate-200 mt-1">
                  {stats.graph?.node_count ?? 0} nodes · {stats.graph?.edge_count ?? 0} edges
                  <span className="text-slate-500 text-xs"> ({stats.graph?.neo4j})</span></div></div>
              <div><div className="h-sub">Learning events</div>
                <div className="text-slate-200 mt-1">{stats.learning?.events ?? 0}</div></div>
              <div><div className="h-sub">Clarifications learned</div>
                <div className="text-slate-200 mt-1">{stats.clarifications?.answered ?? 0}</div></div>
            </div>
            <div className="grid md:grid-cols-3 gap-1 text-sm mt-4">
              {Object.entries(status.checks || {}).map(([name, check]) => (
                <div key={name} className="flex justify-between py-1 px-2 rounded hover:bg-surface-overlay/40">
                  <span className="text-slate-400">{name.replace(/_/g, ' ')}</span>
                  <Badge tone={check.ok ? 'success' : 'danger'}>{check.ok ? 'ok' : 'failed'}</Badge>
                </div>
              ))}
            </div>
          </div>
        )}
      </AsyncSection>
    </div>
  )
}
