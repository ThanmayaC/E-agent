import { useState } from 'react'
import { useParams } from 'react-router-dom'
import { api, fmt } from '../api/client'
import { AsyncSection, Badge, PageHeader, useAsync } from '../components/ui'

function Preview({ projectId, datasetId }) {
  const state = useAsync(() => api.preview(projectId, datasetId), [projectId, datasetId])
  return (
    <AsyncSection state={state} empty="Preview unavailable">
      {(d) => (
        <div className="overflow-auto max-h-96 card">
          <table className="table-base whitespace-nowrap">
            <thead><tr>{d.columns.map((c) => <th key={c}>{c}</th>)}</tr></thead>
            <tbody>
              {d.rows.map((row, i) => (
                <tr key={i}>{row.map((v, j) => <td key={j}>{v === null ? <span className="text-slate-700">∅</span> : String(v)}</td>)}</tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </AsyncSection>
  )
}

export default function Datasets() {
  const { projectId } = useParams()
  const state = useAsync(() => api.datasets(projectId), [projectId])
  const [selected, setSelected] = useState(null)

  return (
    <>
      <PageHeader title="Dataset Explorer" subtitle="Logical datasets discovered and merged from your workbooks" />
      <AsyncSection state={state}>
        {(datasets) => (
          <div className="space-y-4">
            <div className="grid md:grid-cols-2 xl:grid-cols-3 gap-4">
              {datasets.map((d) => (
                <button key={d.dataset_id}
                        onClick={() => setSelected(selected === d.dataset_id ? null : d.dataset_id)}
                        className={`card-pad text-left transition-colors ${selected === d.dataset_id ? 'border-accent' : 'hover:border-accent/40'}`}>
                  <div className="flex justify-between items-start gap-2">
                    <div className="font-medium text-slate-200">{d.name}</div>
                    <Badge tone={d.is_fact ? 'accent' : 'info'}>{d.is_fact ? 'fact' : d.is_dimension ? 'dimension' : 'reference'}</Badge>
                  </div>
                  <div className="text-xs text-slate-500 mt-2">{d.description}</div>
                  <div className="flex gap-4 mt-3 text-xs text-slate-400">
                    <span>{fmt.num(d.row_count)} rows</span>
                    <span>{d.column_count} cols</span>
                    {d.time_grain && <span>{d.time_grain}</span>}
                    <span>conf {Math.round(d.confidence * 100)}%</span>
                  </div>
                  {d.merged_from?.length > 1 && (
                    <div className="mt-2 text-[11px] text-amber-400/80">
                      ⧉ auto-merged from {d.merged_from.length} partitions
                    </div>
                  )}
                </button>
              ))}
            </div>
            {selected && <Preview projectId={projectId} datasetId={selected} />}
          </div>
        )}
      </AsyncSection>
    </>
  )
}
