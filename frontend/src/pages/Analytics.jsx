import { useState } from 'react'
import { useParams } from 'react-router-dom'
import { api } from '../api/client'
import { AsyncSection, PageHeader, useAsync } from '../components/ui'
import EChart, { axisStyle, PALETTE } from '../components/EChart'

export default function Analytics() {
  const { projectId } = useParams()
  const breakdowns = useAsync(() => api.breakdowns(projectId), [projectId])
  const [sql, setSql] = useState('')
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)
  const [running, setRunning] = useState(false)

  async function run() {
    setRunning(true); setError(null)
    try { setResult(await api.query(projectId, sql)) }
    catch (e) { setError(e.message); setResult(null) }
    finally { setRunning(false) }
  }

  return (
    <>
      <PageHeader title="Analytics" subtitle="Auto-generated breakdowns plus ad-hoc SQL over the DuckDB warehouse" />

      <AsyncSection state={breakdowns} empty="No dimensional breakdowns available.">
        {(charts) => (
          <div className="grid lg:grid-cols-2 gap-4 mb-6">
            {charts.map((c, idx) => (
              <div key={idx} className="card-pad">
                <div className="h-title mb-1">{c.title}</div>
                <div className="text-xs text-slate-600 mb-2">{c.dataset}</div>
                <EChart height={260} option={{
                  tooltip: { trigger: 'axis' },
                  xAxis: { type: 'category', ...axisStyle, data: c.rows.map((r) => String(r[0])), axisLabel: { color: '#64748b', rotate: 25 } },
                  yAxis: { type: 'value', ...axisStyle },
                  series: [{ type: 'bar', data: c.rows.map((r) => r[1]),
                             itemStyle: { color: PALETTE[idx % PALETTE.length], borderRadius: [4, 4, 0, 0] } }],
                }} />
              </div>
            ))}
          </div>
        )}
      </AsyncSection>

      <div className="card-pad">
        <div className="h-title mb-3">SQL Workbench <span className="text-xs text-slate-600 font-normal">(read-only SELECT)</span></div>
        <textarea className="input font-mono h-28" placeholder={'SELECT ... FROM "dataset_id" GROUP BY 1'}
                  value={sql} onChange={(e) => setSql(e.target.value)} />
        <div className="mt-3 flex items-center gap-3">
          <button className="btn" onClick={run} disabled={running || !sql.trim()}>{running ? 'Running…' : 'Run query'}</button>
          {error && <span className="text-sm text-rose-400">{error}</span>}
        </div>
        {result && (
          <div className="overflow-auto max-h-96 mt-4 card">
            <table className="table-base whitespace-nowrap">
              <thead><tr>{result.columns.map((c) => <th key={c}>{c}</th>)}</tr></thead>
              <tbody>
                {result.rows.map((row, i) => (
                  <tr key={i}>{row.map((v, j) => <td key={j}>{v === null ? '∅' : String(v)}</td>)}</tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </>
  )
}
