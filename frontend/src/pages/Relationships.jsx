import { useParams } from 'react-router-dom'
import { api } from '../api/client'
import { AsyncSection, Badge, PageHeader, useAsync } from '../components/ui'

const typeTone = { foreign_key: 'accent', shared_dimension: 'info', date_alignment: 'warn', partition_of: 'success' }

export default function Relationships() {
  const { projectId } = useParams()
  const state = useAsync(() => api.relationships(projectId), [projectId])

  return (
    <>
      <PageHeader title="Relationship Explorer"
                  subtitle="Joins detected across files — even when column names differ" />
      <AsyncSection state={state} empty="No cross-dataset relationships detected.">
        {(rels) => (
          <div className="card overflow-auto">
            <table className="table-base">
              <thead>
                <tr><th>From</th><th></th><th>To</th><th>Type</th><th>Cardinality</th><th>Overlap</th><th>Confidence</th><th>Evidence</th></tr>
              </thead>
              <tbody>
                {rels.sort((a, b) => b.confidence - a.confidence).map((r) => (
                  <tr key={r.id} className="hover:bg-surface-overlay/40">
                    <td>
                      <div className="font-mono text-xs text-slate-500">{r.from_dataset}</div>
                      <div className="text-slate-200">{r.from_column}</div>
                    </td>
                    <td className="text-accent text-lg">→</td>
                    <td>
                      <div className="font-mono text-xs text-slate-500">{r.to_dataset}</div>
                      <div className="text-slate-200">{r.to_column}</div>
                    </td>
                    <td><Badge tone={typeTone[r.rel_type] || 'default'}>{r.rel_type.replace('_', ' ')}</Badge></td>
                    <td className="font-mono">{r.cardinality}</td>
                    <td>{Math.round(r.overlap * 100)}%</td>
                    <td>
                      <div className="w-20 h-1.5 bg-surface-overlay rounded-full">
                        <div className="h-full bg-accent rounded-full" style={{ width: `${r.confidence * 100}%` }} />
                      </div>
                    </td>
                    <td className="text-xs text-slate-500 max-w-xs">{r.evidence}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </AsyncSection>
    </>
  )
}
