import { useParams } from 'react-router-dom'
import { api } from '../api/client'
import { AsyncSection, Badge, PageHeader, severityTone, useAsync } from '../components/ui'

export default function DataQuality() {
  const { projectId } = useParams()
  const state = useAsync(() => api.quality(projectId), [projectId])

  return (
    <>
      <PageHeader title="Data Quality" subtitle="Automatic checks: nulls, duplicates, outliers, drift, invalid values" />
      <AsyncSection state={state}>
        {(q) => (
          <div className="space-y-5">
            <div className="grid sm:grid-cols-3 gap-4">
              <div className="card-pad text-center">
                <div className="h-sub">Overall score</div>
                <div className={`text-4xl font-bold mt-2 ${q.overall_score >= 80 ? 'text-emerald-400' : q.overall_score >= 60 ? 'text-amber-400' : 'text-rose-400'}`}>
                  {q.overall_score}
                </div>
                <div className="text-xs text-slate-600">/ 100</div>
              </div>
              <div className="card-pad text-center">
                <div className="h-sub">Issues found</div>
                <div className="text-4xl font-bold mt-2 text-slate-100">{q.issues.length}</div>
              </div>
              <div className="card-pad text-center">
                <div className="h-sub">Datasets assessed</div>
                <div className="text-4xl font-bold mt-2 text-slate-100">{Object.keys(q.per_dataset).length}</div>
              </div>
            </div>

            <div className="card-pad">
              <div className="h-title mb-3">Per-dataset confidence</div>
              <div className="space-y-2">
                {Object.entries(q.per_dataset).map(([ds, score]) => (
                  <div key={ds} className="flex items-center gap-3 text-sm">
                    <span className="font-mono text-xs text-slate-500 w-64 truncate">{ds}</span>
                    <div className="flex-1 h-2 bg-surface-overlay rounded-full">
                      <div className={`h-full rounded-full ${score >= 80 ? 'bg-emerald-500' : score >= 60 ? 'bg-amber-500' : 'bg-rose-500'}`}
                           style={{ width: `${score}%` }} />
                    </div>
                    <span className="w-10 text-right text-slate-300">{score}</span>
                  </div>
                ))}
              </div>
            </div>

            <div className="card overflow-auto">
              <table className="table-base">
                <thead><tr><th>Severity</th><th>Issue</th><th>Dataset</th><th>Column</th><th>Count</th><th>Detail</th></tr></thead>
                <tbody>
                  {q.issues.map((i, idx) => (
                    <tr key={idx} className="hover:bg-surface-overlay/40">
                      <td><Badge tone={severityTone(i.severity)}>{i.severity}</Badge></td>
                      <td className="text-slate-200">{i.kind.replace(/_/g, ' ')}</td>
                      <td className="font-mono text-xs text-slate-500">{i.dataset_id}</td>
                      <td>{i.column || '—'}</td>
                      <td>{i.count || '—'}</td>
                      <td className="text-slate-500 text-xs">{i.detail}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}
      </AsyncSection>
    </>
  )
}
