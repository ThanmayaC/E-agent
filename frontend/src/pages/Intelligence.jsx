// Intelligence (V10.0) — the multi-layer analyst surface. WHY-first insights
// with accept/reject feedback (continuous learning), and the Layer-2 ML models
// (forecast with confidence band, anomalies, segmentation, churn, failure) —
// every prediction tagged with model, version, confidence and features.
import { useEffect, useState } from 'react'
import { api } from '../api/client'
import EChart, { PALETTE, axisStyle } from '../components/EChart'
import {
  AsyncSection, Badge, PageHeader, Panel, PanelEmpty, Stat, Tabs, useAsync,
} from '../components/ui'

const confTone = (c) => (c >= 80 ? 'success' : c >= 55 ? 'warn' : 'danger')
const prioTone = (p) => ({ Critical: 'danger', High: 'danger', Medium: 'warn', Low: 'default' }[p] || 'default')

function ModelTag({ card, model, confidence }) {
  const c = card || {}
  return (
    <div className="flex flex-wrap items-center gap-1.5 text-[11px] text-slate-500 mt-1">
      <Badge tone="info">{c.model || model}</Badge>
      {c.version && <span>v{c.version}</span>}
      {confidence != null && <Badge tone={confTone(confidence)}>{confidence}% conf</Badge>}
      {c.features && <span>· features: {c.features.join(', ')}</span>}
    </div>
  )
}

// -------------------------------------------------------------- Insights
function Insights() {
  const [data, setData] = useState(null)
  const [acted, setActed] = useState({})
  useEffect(() => { api.insights().then(setData).catch(() => setData({ insights: [] })) }, [])
  const feedback = async (id, action) => {
    setActed((a) => ({ ...a, [id]: action }))
    try { await api.sendFeedback(id, action) } catch { /* non-fatal */ }
  }
  if (!data) return <PanelEmpty text="Loading insights…" />
  if (!data.available) return <PanelEmpty text="No insights — generate the enterprise corpus." />
  return (
    <div className="space-y-3">
      <div className="text-xs text-slate-500">{data.count} insights · {data.generated_for}</div>
      {data.insights.map((i) => (
        <div key={i.id} className="card-pad">
          <div className="flex items-start gap-2 flex-wrap">
            <Badge tone={prioTone(i.priority)}>{i.priority}</Badge>
            <span className="text-sm font-semibold text-slate-100 flex-1">{i.title}</span>
            <Badge tone={confTone(i.confidence)}>{i.confidence_label}</Badge>
          </div>
          <p className="text-sm text-slate-200 mt-2">{i.what}</p>
          <div className="mt-2 grid gap-1.5 text-xs">
            <div><span className="text-slate-500">Why: </span><span className="text-slate-300">{i.why}</span></div>
            <div><span className="text-slate-500">Impact: </span><span className="text-slate-400">{i.impact}</span></div>
            {i.alternative_explanations?.length > 0 && (
              <div><span className="text-slate-500">Alternatives: </span><span className="text-slate-400">{i.alternative_explanations.join(' · ')}</span></div>
            )}
            {i.business_risks?.length > 0 && (
              <div><span className="text-slate-500">Risks: </span><span className="text-slate-400">{i.business_risks.join(' · ')}</span></div>
            )}
            {i.recommended_actions?.length > 0 && (
              <div><span className="text-slate-500">Actions: </span><span className="text-slate-300">{i.recommended_actions.join(' · ')}</span></div>
            )}
            <div className="flex flex-wrap gap-3 text-slate-500 pt-1">
              <span>ROI: <span className="text-slate-400">{i.expected_roi}</span></span>
              <span>Complexity: <span className="text-slate-400">{i.implementation_complexity}</span></span>
              <span>Owner: <span className="text-slate-400">{i.owner}</span></span>
            </div>
          </div>
          <div className="mt-2 pt-2 border-t border-surface-border flex items-center gap-2 flex-wrap">
            <span className="text-[11px] text-slate-500">Evidence:</span>
            {(i.supporting_evidence || []).map((e, j) => <Badge key={j} tone="default">{e}</Badge>)}
            <span className="text-[11px] text-slate-600">· {i.source_layer} / {i.model}</span>
            <div className="flex-1" />
            {acted[i.id] ? (
              <span className="text-[11px] text-slate-500">Marked {acted[i.id]} ✓</span>
            ) : (
              <>
                <button onClick={() => feedback(i.id, 'accepted')}
                  className="chip chip-success hover:brightness-125">Accept</button>
                <button onClick={() => feedback(i.id, 'rejected')}
                  className="chip chip-danger hover:brightness-125">Dismiss</button>
              </>
            )}
          </div>
        </div>
      ))}
    </div>
  )
}

// -------------------------------------------------------------- Forecast
function Forecast() {
  const [data, setData] = useState(null)
  const [kpi, setKpi] = useState('Success Rate (%)')
  useEffect(() => { setData(null); api.mlForecast(kpi).then(setData).catch(() => setData({ available: false })) }, [kpi])
  const KPIS = ['Success Rate (%)', 'UPI Transactions (M/day)', 'Technical Declines (%)', 'Response Time (ms)']
  return (
    <div className="space-y-3">
      <div className="flex gap-1.5 flex-wrap">
        {KPIS.map((k) => (
          <button key={k} onClick={() => setKpi(k)}
            className={`px-2.5 py-1 rounded text-xs ${k === kpi ? 'bg-accent text-white' : 'bg-surface-overlay/60 text-slate-400'}`}>{k}</button>
        ))}
      </div>
      {!data ? <PanelEmpty text="Training…" /> : !data.available ? <PanelEmpty text="Not enough history to forecast." /> : (
        <Panel title={`30-day forecast — ${data.kpi}`}>
          <EChart height={300} option={{
            tooltip: { trigger: 'axis' },
            legend: { textStyle: { color: '#94a3b8' }, top: 0 },
            grid: { left: 56, right: 20, top: 30, bottom: 40 },
            xAxis: { type: 'category', data: data.forecast.map((r) => `+${r.step}`), ...axisStyle },
            yAxis: { type: 'value', scale: true, ...axisStyle },
            series: [
              { name: 'Upper', type: 'line', data: data.forecast.map((r) => r.upper), lineStyle: { opacity: 0 }, stack: 'band', symbol: 'none' },
              { name: 'Band', type: 'line', data: data.forecast.map((r) => r.lower), lineStyle: { opacity: 0 }, areaStyle: { color: 'rgba(79,142,247,0.12)' }, stack: 'band', symbol: 'none' },
              { name: 'Forecast', type: 'line', data: data.forecast.map((r) => r.forecast), smooth: true, lineStyle: { width: 2, color: PALETTE[0] }, symbol: 'none' },
            ],
          }} />
          <ModelTag card={data.card} confidence={data.confidence} />
        </Panel>
      )}
    </div>
  )
}

// ------------------------------------------------ ML entity result tables
function MLTable({ loader, empty, columns, rowsKey, title, cardKey = 'card' }) {
  const [data, setData] = useState(null)
  useEffect(() => { loader().then(setData).catch(() => setData({ available: false })) }, []) // eslint-disable-line
  if (!data) return <PanelEmpty text="Training model…" />
  if (!data.available) return <PanelEmpty text={data.reason ? `${empty} (${data.reason})` : empty} />
  const rows = data[rowsKey] || []
  return (
    <Panel title={title}>
      <div className="overflow-x-auto">
        <table className="w-full text-sm">
          <thead><tr className="text-left text-xs uppercase tracking-wide text-slate-500 border-b border-surface-border">
            {columns.map((c) => <th key={c.key} className={`py-2 pr-4 ${c.right ? 'text-right' : ''}`}>{c.label}</th>)}
          </tr></thead>
          <tbody>
            {rows.slice(0, 15).map((r, i) => (
              <tr key={i} className="border-b border-surface-border/50">
                {columns.map((c) => <td key={c.key} className={`py-2 pr-4 tabular-nums ${c.right ? 'text-right' : 'text-slate-200'}`}>{c.render ? c.render(r) : r[c.key]}</td>)}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <ModelTag card={data[cardKey]} confidence={data.confidence} />
      {data.feature_importances && (
        <div className="mt-2 text-[11px] text-slate-500">
          Top drivers: {data.feature_importances.slice(0, 3).map((f) => `${f.feature} (${f.importance})`).join(' · ')}
        </div>
      )}
    </Panel>
  )
}

function Segments() {
  const [data, setData] = useState(null)
  useEffect(() => { api.mlSegments().then(setData).catch(() => setData({ available: false })) }, [])
  if (!data) return <PanelEmpty text="Clustering…" />
  if (!data.available) return <PanelEmpty text="Segmentation unavailable." />
  return (
    <Panel title="Merchant segments (KMeans)">
      <div className="grid gap-3 sm:grid-cols-2">
        {data.segments.map((s) => (
          <div key={s.segment} className="card-pad">
            <div className="flex items-center gap-2">
              <Badge tone={s.label.includes('risk') ? 'danger' : s.label.includes('champion') ? 'success' : 'default'}>{s.label}</Badge>
              <span className="text-xs text-slate-500">{s.size} merchants</span>
            </div>
            <div className="text-xs text-slate-400 mt-1.5">avg growth {s.avg_growth_pct}% · avg health {s.avg_health}</div>
            <div className="text-[11px] text-slate-600 mt-1 truncate">{s.merchants.join(', ')}</div>
          </div>
        ))}
      </div>
      <ModelTag card={data.card} confidence={data.confidence} />
    </Panel>
  )
}

const TABS = [
  { value: 'insights', label: 'Insights' },
  { value: 'forecast', label: 'Forecast' },
  { value: 'anomalies', label: 'Anomalies' },
  { value: 'segments', label: 'Segments' },
  { value: 'churn', label: 'Churn risk' },
  { value: 'failure', label: 'Failure risk' },
]

export default function Intelligence() {
  const [tab, setTab] = useState('insights')
  const state = useAsync(async () => (await api.mlStatus().catch(() => ({ available: false }))), [])
  return (
    <>
      <PageHeader title="Intelligence"
        subtitle="Multi-layer analyst — deterministic KPIs, ML predictions and evidence, each answer explained (model · confidence · features)" />
      <AsyncSection state={state} empty="ML layer unavailable.">
        {() => (
          <>
            <Tabs tabs={TABS} active={tab} onChange={setTab} />
            {tab === 'insights' && <Insights />}
            {tab === 'forecast' && <Forecast />}
            {tab === 'anomalies' && (
              <MLTable loader={api.mlAnomalies} rowsKey="anomalies" title="Detected anomalies (IsolationForest)"
                empty="No anomalies detected." columns={[
                  { key: 'date', label: 'When' },
                  { key: 'success_rate', label: 'Success', right: true, render: (r) => `${r.success_rate}%` },
                  { key: 'technical_decline_pct', label: 'Tech declines', right: true, render: (r) => `${r.technical_decline_pct}%` },
                  { key: 'anomaly_score', label: 'Score', right: true },
                ]} />
            )}
            {tab === 'segments' && <Segments />}
            {tab === 'churn' && (
              <MLTable loader={api.mlChurn} rowsKey="at_risk" title="Merchant churn risk (RandomForest propensity)"
                empty="No churn signal." columns={[
                  { key: 'merchant', label: 'Merchant' },
                  { key: 'status', label: 'Status' },
                  { key: 'health_score', label: 'Health', right: true },
                  { key: 'churn_risk', label: 'Risk', right: true, render: (r) => <span style={{ color: r.churn_risk > 50 ? '#fb7185' : '#94a3b8' }}>{r.churn_risk}%</span> },
                ]} />
            )}
            {tab === 'failure' && (
              <MLTable loader={api.mlFailure} rowsKey="banks_at_risk" title="Bank failure risk (GradientBoosting)"
                empty="No failure signal." columns={[
                  { key: 'bank', label: 'Bank' },
                  { key: 'success_rate', label: 'Success', right: true, render: (r) => `${r.success_rate}%` },
                  { key: 'p95_latency_ms', label: 'p95', right: true, render: (r) => `${r.p95_latency_ms}ms` },
                  { key: 'failure_risk', label: 'Risk', right: true, render: (r) => <span style={{ color: r.failure_risk > 30 ? '#fb7185' : '#94a3b8' }}>{r.failure_risk}%</span> },
                ]} />
            )}
          </>
        )}
      </AsyncSection>
    </>
  )
}
