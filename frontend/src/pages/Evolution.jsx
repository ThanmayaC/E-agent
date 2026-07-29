// Six-month Evolution — the continuously-evolving digital twin (V8.0). Replays
// 180 days of the UPI ecosystem: user-base lifecycle, bank & PSP competition,
// product lifecycle, forecast validation, executive decision outcomes, the
// connected weekly storyline, and an executive Q&A. Every number is read from
// the V8.0 evolution cubes via /executive/evolution/*.
import { useState } from 'react'
import { api, fmt } from '../api/client'
import EChart, { PALETTE, axisStyle } from '../components/EChart'
import {
  AsyncSection, Badge, PageHeader, Panel, PanelEmpty, Stat, Tabs,
  useAsync,
} from '../components/ui'

const INR = (v) => (v == null ? '—' : `₹${fmt.num(v)}`)
const CR = (v) => (v == null ? '—' : `₹${fmt.num(v)} cr`)
const pctColor = (g) => (g > 0 ? '#34d399' : g < 0 ? '#fb7185' : '#64748b')

function lineOption(x, series, { area = false } = {}) {
  return {
    tooltip: { trigger: 'axis' },
    legend: { textStyle: { color: '#94a3b8' }, top: 0 },
    grid: { left: 56, right: 20, top: 32, bottom: 40 },
    xAxis: { type: 'category', data: x, ...axisStyle,
      axisLabel: { ...axisStyle.axisLabel, interval: Math.ceil(x.length / 8) } },
    yAxis: { type: 'value', ...axisStyle, scale: true },
    series: series.map((s, i) => ({
      name: s.name, type: 'line', smooth: true, showSymbol: false,
      data: s.data, lineStyle: { width: 2, color: s.color || PALETTE[i] },
      itemStyle: { color: s.color || PALETTE[i] },
      areaStyle: area ? { opacity: 0.12 } : undefined,
    })),
  }
}

function Table({ rows, cols, keyField = 'name' }) {
  if (!rows?.length) return <PanelEmpty text="No data." />
  return (
    <div className="overflow-x-auto">
      <table className="w-full text-sm">
        <thead>
          <tr className="text-left text-xs uppercase tracking-wide text-slate-500 border-b border-surface-border">
            {cols.map((c) => <th key={c.key} className={`py-2 pr-4 ${c.right ? 'text-right' : ''}`}>{c.label}</th>)}
          </tr>
        </thead>
        <tbody>
          {rows.map((r, i) => (
            <tr key={r[keyField] || i} className="border-b border-surface-border/50 hover:bg-surface-overlay/40">
              {cols.map((c) => (
                <td key={c.key} className={`py-2 pr-4 tabular-nums ${c.right ? 'text-right' : 'text-slate-200'}`}>
                  {c.render ? c.render(r) : r[c.key]}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

// -------------------------------------------------------------- Overview
function Overview({ data }) {
  const o = data.overview || {}
  const u = o.users || {}
  const g = o.user_growth || {}
  return (
    <div className="space-y-4">
      <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-4">
        <Stat label="Registered base" value={`${g.registered_base_m?.end ?? '—'}M`}
          hint={`from ${g.registered_base_m?.start ?? '—'}M · 6 months`} />
        <Stat label="MAU" value={`${u.mau_m ?? '—'}M`}
          hint={`DAU ${u.dau_m ?? '—'}M · stickiness ${u.stickiness_pct ?? '—'}%`} />
        <Stat label="Retention" value={`${u.retention_pct ?? '—'}%`}
          hint={`churn ${u.churn_pct ?? '—'}%`} />
        <Stat label="Decision value" value={CR(o.decisions?.total_business_value_cr)}
          hint={`${o.decisions?.count ?? 0} decisions · avg success ${o.decisions?.avg_success_score ?? '—'}`} />
      </div>
      <div className="grid gap-4 lg:grid-cols-2">
        <Panel title="Banks improving">
          <Table keyField="bank" rows={o.banks_improving} cols={[
            { key: 'bank', label: 'Bank' },
            { key: 'sr', label: 'Δ success', right: true,
              render: (r) => <span style={{ color: pctColor(r.sr_change_pct) }}>{r.sr_change_pct > 0 ? '+' : ''}{r.sr_change_pct}%</span> },
            { key: 'lat', label: 'Δ latency', right: true, render: (r) => `${r.latency_change_ms}ms` },
          ]} />
        </Panel>
        <Panel title="PSPs losing share">
          <Table keyField="psp" rows={o.psps_losing_share} cols={[
            { key: 'psp', label: 'PSP' },
            { key: 'share', label: 'Share', right: true, render: (r) => `${r.market_share_pct}%` },
            { key: 'chg', label: 'Δ share', right: true,
              render: (r) => <span style={{ color: pctColor(r.share_change_pct) }}>{r.share_change_pct}%</span> },
          ]} />
        </Panel>
        <Panel title="Features approaching saturation">
          <Table keyField="feature" rows={o.features_saturating} cols={[
            { key: 'feature', label: 'Feature' },
            { key: 'share_pct', label: 'Share', right: true, render: (r) => `${r.share_pct}%` },
            { key: 'stage', label: 'Stage', right: true, render: (r) => <Badge tone="warn">{r.stage}</Badge> },
          ]} />
        </Panel>
        <Panel title="Where to invest next">
          <Table keyField="product" rows={o.products_investable} cols={[
            { key: 'product', label: 'Product' },
            { key: 'mom_growth_pct', label: 'Growth', right: true,
              render: (r) => <span style={{ color: pctColor(r.mom_growth_pct) }}>+{r.mom_growth_pct}%</span> },
            { key: 'lifecycle_stage', label: 'Stage', right: true, render: (r) => <Badge tone="success">{r.lifecycle_stage}</Badge> },
          ]} />
        </Panel>
      </div>
    </div>
  )
}

// ----------------------------------------------------------------- Users
function Users({ data }) {
  const c = data.customers || {}
  const s = c.series || []
  if (!s.length) return <PanelEmpty text="No customer evolution." />
  const x = s.map((r) => r.date)
  const latest = c.latest || {}
  return (
    <div className="space-y-4">
      <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-4">
        <Stat label="DAU / WAU / MAU" value={`${latest.dau_m} / ${latest.wau_m} / ${latest.mau_m}M`} />
        <Stat label="Power users" value={`${latest.power_users_m}M`} hint={`dormant ${latest.dormant_users_m}M`} />
        <Stat label="New / day" value={`${latest.new_users_k}K`} hint={`returned ${latest.returned_users_k}K/day`} />
        <Stat label="Feature adopters" value={`${latest.feature_adopters_m}M`} />
      </div>
      <Panel title="User base — DAU · WAU · MAU (millions)">
        <EChart option={lineOption(x, [
          { name: 'DAU', data: s.map((r) => r.dau_m) },
          { name: 'WAU', data: s.map((r) => r.wau_m) },
          { name: 'MAU', data: s.map((r) => r.mau_m) },
        ], { area: true })} height={300} />
      </Panel>
      <div className="grid gap-4 lg:grid-cols-2">
        <Panel title="Retention & churn (%)">
          <EChart option={lineOption(x, [
            { name: 'Retention', data: s.map((r) => r.retention_pct), color: '#34d399' },
            { name: 'Churn', data: s.map((r) => r.churn_pct), color: '#fb7185' },
          ])} height={240} />
        </Panel>
        <Panel title="Power vs dormant users (millions)">
          <EChart option={lineOption(x, [
            { name: 'Power', data: s.map((r) => r.power_users_m), color: PALETTE[2] },
            { name: 'Dormant', data: s.map((r) => r.dormant_users_m), color: '#64748b' },
          ])} height={240} />
        </Panel>
      </div>
    </div>
  )
}

// ------------------------------------------------------- Banks / PSPs
function Competition({ data }) {
  const b = data.banks || {}
  const p = data.psps || {}
  return (
    <div className="space-y-4">
      <Panel title="Bank market share (latest week)">
        <Table keyField="bank" rows={b.banks?.slice(0, 12)} cols={[
          { key: 'bank', label: 'Bank' },
          { key: 'tier', label: 'Tier' },
          { key: 'market_share_pct', label: 'Share', right: true, render: (r) => `${r.market_share_pct}%` },
          { key: 'success_rate', label: 'Success', right: true, render: (r) => `${r.success_rate}%` },
          { key: 'p95_latency_ms', label: 'p95', right: true, render: (r) => `${r.p95_latency_ms}ms` },
          { key: 'health_grade', label: 'Health', right: true, render: (r) => <Badge tone={r.health_grade === 'Healthy' ? 'success' : r.health_grade === 'At risk' ? 'danger' : 'default'}>{r.health_grade}</Badge> },
        ]} />
      </Panel>
      <div className="grid gap-4 lg:grid-cols-2">
        <Panel title="Improving banks (6-month)">
          <Table keyField="bank" rows={b.improving} cols={[
            { key: 'bank', label: 'Bank' },
            { key: 'sr_change_pct', label: 'Δ success', right: true, render: (r) => <span style={{ color: pctColor(r.sr_change_pct) }}>{r.sr_change_pct > 0 ? '+' : ''}{r.sr_change_pct}%</span> },
            { key: 'latency_change_ms', label: 'Δ latency', right: true, render: (r) => `${r.latency_change_ms}ms` },
            { key: 'total_incidents', label: 'Incidents', right: true },
          ]} />
        </Panel>
        <Panel title="PSP competition — share movement">
          <Table keyField="psp" rows={p.psps?.slice(0, 12)} cols={[
            { key: 'psp', label: 'PSP' },
            { key: 'market_share_pct', label: 'Share', right: true, render: (r) => `${r.market_share_pct}%` },
            { key: 'share_change_pct', label: 'Δ share', right: true, render: (r) => <span style={{ color: pctColor(r.share_change_pct) }}>{r.share_change_pct > 0 ? '+' : ''}{r.share_change_pct}%</span> },
            { key: 'is_market_leader', label: '', right: true, render: (r) => (r.is_market_leader ? <Badge tone="success">Leader</Badge> : null) },
          ]} />
        </Panel>
      </div>
    </div>
  )
}

// -------------------------------------------------------------- Products
function Products({ data }) {
  const pr = data.products || {}
  const fe = data.features || {}
  return (
    <div className="space-y-4">
      <Panel title="Product lifecycle (latest month)">
        <Table keyField="product" rows={pr.products} cols={[
          { key: 'product', label: 'Product' },
          { key: 'lifecycle_stage', label: 'Stage', render: (r) => <Badge tone={r.lifecycle_stage === 'Growth' ? 'success' : r.lifecycle_stage === 'Decline' ? 'danger' : 'default'}>{r.lifecycle_stage}</Badge> },
          { key: 'market_share_pct', label: 'Share', right: true, render: (r) => `${r.market_share_pct}%` },
          { key: 'revenue_contribution_pct', label: 'Revenue', right: true, render: (r) => `${r.revenue_contribution_pct}%` },
          { key: 'adoption_m', label: 'Adoption', right: true, render: (r) => `${r.adoption_m}M` },
          { key: 'avg_ticket_inr', label: 'Avg ticket', right: true, render: (r) => INR(r.avg_ticket_inr) },
          { key: 'mom_growth_pct', label: 'Growth', right: true, render: (r) => <span style={{ color: pctColor(r.mom_growth_pct) }}>{r.mom_growth_pct > 0 ? '+' : ''}{r.mom_growth_pct}%</span> },
        ]} />
      </Panel>
      <Panel title="Feature adoption & stage">
        <Table keyField="feature" rows={fe.features} cols={[
          { key: 'feature', label: 'Feature' },
          { key: 'stage', label: 'Stage', render: (r) => <Badge tone={r.stage === 'Growth' || r.stage === 'Introduction' ? 'success' : r.stage === 'Decline' ? 'danger' : 'default'}>{r.stage}</Badge> },
          { key: 'share_pct', label: 'Share', right: true, render: (r) => `${r.share_pct}%` },
          { key: 'adopters_m', label: 'Adopters', right: true, render: (r) => `${r.adopters_m}M` },
          { key: 'mom_growth_pct', label: 'Growth', right: true, render: (r) => <span style={{ color: pctColor(r.mom_growth_pct) }}>{r.mom_growth_pct > 0 ? '+' : ''}{r.mom_growth_pct}%</span> },
        ]} />
      </Panel>
    </div>
  )
}

// ------------------------------------------------------------- Forecasts
function Forecasts({ data }) {
  const fa = data.forecastAccuracy || {}
  const v = fa.validations || []
  return (
    <div className="space-y-4">
      <div className="grid gap-3 sm:grid-cols-3">
        <Stat label="Mean forecast accuracy" value={`${fa.mean_accuracy_pct ?? '—'}%`} />
        <Stat label="Direction hit rate" value={`${fa.direction_hit_rate_pct ?? '—'}%`} />
        <Stat label="KPIs validated" value={v.length} hint="predicted vs realised" />
      </div>
      <Panel title="Forecast validation — predicted vs actual (backtest)">
        <Table keyField="kpi" rows={v} cols={[
          { key: 'kpi', label: 'KPI' },
          { key: 'predicted_end', label: 'Predicted', right: true },
          { key: 'actual_end', label: 'Actual', right: true },
          { key: 'accuracy_pct', label: 'Accuracy', right: true, render: (r) => <span style={{ color: pctColor(r.accuracy_pct - 90) }}>{r.accuracy_pct}%</span> },
          { key: 'mape_pct', label: 'MAPE', right: true, render: (r) => `${r.mape_pct}%` },
          { key: 'direction_correct', label: 'Direction', right: true, render: (r) => <Badge tone={String(r.direction_correct).toLowerCase() === 'true' ? 'success' : 'danger'}>{String(r.direction_correct).toLowerCase() === 'true' ? '✓' : '✗'}</Badge> },
          { key: 'confidence_pct', label: 'Confidence', right: true, render: (r) => `${r.confidence_pct}%` },
        ]} />
      </Panel>
    </div>
  )
}

// ------------------------------------------------------------- Decisions
function Decisions({ data }) {
  const d = data.decisions || {}
  return (
    <div className="space-y-4">
      <div className="grid gap-3 sm:grid-cols-4">
        <Stat label="Decisions tracked" value={d.count ?? 0} />
        <Stat label="Resolved" value={`${d.resolved ?? 0}/${d.count ?? 0}`} />
        <Stat label="Avg success score" value={d.avg_success_score ?? '—'} />
        <Stat label="Business value protected" value={CR(d.total_business_value_cr)} />
      </div>
      <Panel title="Executive decisions — expected vs actual impact">
        <Table keyField="decision_id" rows={d.decisions} cols={[
          { key: 'decision_id', label: 'ID' },
          { key: 'title', label: 'Decision' },
          { key: 'target_kpi', label: 'KPI' },
          { key: 'recovery_pct', label: 'Recovery', right: true, render: (r) => `${r.recovery_pct}%` },
          { key: 'success_score', label: 'Success', right: true, render: (r) => <span style={{ color: pctColor(r.success_score - 60) }}>{r.success_score}</span> },
          { key: 'business_value_cr', label: 'Value', right: true, render: (r) => CR(r.business_value_cr) },
          { key: 'status', label: 'Status', right: true, render: (r) => <Badge tone={r.status === 'Resolved' ? 'success' : 'warn'}>{r.status}</Badge> },
        ]} />
      </Panel>
    </div>
  )
}

// ----------------------------------------------------------------- Story
function Story({ data }) {
  const weeks = data.stories?.weeks || []
  const [wk, setWk] = useState(weeks.length ? weeks[weeks.length - 1].week : 1)
  const cur = weeks.find((w) => w.week === wk) || weeks[0]
  if (!weeks.length) return <PanelEmpty text="No storyline." />
  return (
    <div className="space-y-4">
      <div className="flex flex-wrap gap-1.5">
        {weeks.map((w) => (
          <button key={w.week} onClick={() => setWk(w.week)}
            className={`px-2.5 py-1 rounded text-xs tabular-nums ${w.week === wk ? 'bg-accent text-white' : 'bg-surface-overlay/60 text-slate-400 hover:text-slate-200'} ${w.has_incident === 'True' || w.has_incident === true ? 'ring-1 ring-rose-500/40' : ''}`}>
            W{w.week}
          </button>
        ))}
      </div>
      <Panel title={`Week ${cur?.week} — ${cur?.week_start}`}>
        <ol className="relative border-l border-surface-border ml-2 space-y-4">
          {(cur?.steps || []).map((s, i) => (
            <li key={i} className="ml-4">
              <div className="absolute -left-1.5 w-3 h-3 rounded-full bg-accent" />
              <div className="flex items-center gap-2">
                <Badge tone="default">{s.stage}</Badge>
                <span className="text-xs text-slate-500">{s.actor_team}</span>
                <span className="text-xs text-slate-600">· {s.linked_kpi}</span>
              </div>
              <p className="text-sm text-slate-200 mt-1">{s.event}</p>
            </li>
          ))}
        </ol>
      </Panel>
    </div>
  )
}

// ------------------------------------------------------------------- Ask
const PRESETS = [
  'Why did transaction value increase?',
  'Which banks are improving?',
  'Which PSP is losing market share?',
  'Which feature is approaching saturation?',
  'Where should Product invest next?',
  'Which decision generated measurable business value?',
  'How accurate were the forecasts?',
]

function Ask() {
  const [q, setQ] = useState('')
  const [ans, setAns] = useState(null)
  const [busy, setBusy] = useState(false)
  const run = async (question) => {
    setQ(question); setBusy(true)
    try { setAns(await api.evolutionAsk(question)) }
    catch { setAns({ answer: 'Query failed.' }) }
    finally { setBusy(false) }
  }
  return (
    <div className="space-y-4">
      <Panel title="Executive workspace — ask the six-month history">
        <div className="flex gap-2">
          <input value={q} onChange={(e) => setQ(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && q.trim() && run(q)}
            placeholder="e.g. Which PSP is losing market share?"
            className="flex-1 bg-surface-overlay/60 border border-surface-border rounded px-3 py-2 text-sm text-slate-100 outline-none focus:border-accent" />
          <button onClick={() => q.trim() && run(q)} disabled={busy}
            className="px-4 py-2 rounded bg-accent text-white text-sm disabled:opacity-50">
            {busy ? '…' : 'Ask'}
          </button>
        </div>
        <div className="flex flex-wrap gap-1.5 mt-3">
          {PRESETS.map((p) => (
            <button key={p} onClick={() => run(p)}
              className="px-2.5 py-1 rounded text-xs bg-surface-overlay/60 text-slate-400 hover:text-slate-200">
              {p}
            </button>
          ))}
        </div>
      </Panel>
      {ans && (
        <Panel title="Answer">
          <p className="text-sm text-slate-100 leading-relaxed">{ans.answer}</p>
          {ans.evidence?.length ? (
            <div className="flex flex-wrap gap-1.5 mt-3">
              <span className="text-xs text-slate-500">Evidence:</span>
              {ans.evidence.map((e) => <Badge key={e} tone="default">{e}</Badge>)}
            </div>
          ) : null}
        </Panel>
      )}
    </div>
  )
}

const TABS = [
  { value: 'overview', label: 'Overview' },
  { value: 'users', label: 'Users' },
  { value: 'competition', label: 'Banks & PSPs' },
  { value: 'products', label: 'Products' },
  { value: 'forecasts', label: 'Forecasts' },
  { value: 'decisions', label: 'Decisions' },
  { value: 'story', label: 'Storyline' },
  { value: 'ask', label: 'Ask' },
]

export default function Evolution() {
  const [tab, setTab] = useState('overview')
  const state = useAsync(async () => {
    const [overview, customers, banks, psps, products, features, forecastAccuracy, decisions, stories] =
      await Promise.all([
        api.evolutionOverview().catch(() => ({})),
        api.evolutionCustomers().catch(() => ({})),
        api.evolutionBanks().catch(() => ({})),
        api.evolutionPsps().catch(() => ({})),
        api.evolutionProducts().catch(() => ({})),
        api.evolutionFeatures().catch(() => ({})),
        api.evolutionForecastAccuracy().catch(() => ({})),
        api.evolutionDecisions().catch(() => ({})),
        api.evolutionStories().catch(() => ({})),
      ])
    return { overview, customers, banks, psps, products, features, forecastAccuracy, decisions, stories }
  }, [])

  return (
    <>
      <PageHeader title="Six-Month Evolution"
        subtitle="The continuously-evolving digital twin — user lifecycle, bank & PSP competition, product lifecycle, forecast validation, decision outcomes and the weekly storyline" />
      <AsyncSection state={state} empty="No evolution data — generate and ingest the 180-day enterprise corpus (V8.0).">
        {(data) => (
          <>
            <Tabs tabs={TABS} active={tab} onChange={setTab} />
            {tab === 'overview' && <Overview data={data} />}
            {tab === 'users' && <Users data={data} />}
            {tab === 'competition' && <Competition data={data} />}
            {tab === 'products' && <Products data={data} />}
            {tab === 'forecasts' && <Forecasts data={data} />}
            {tab === 'decisions' && <Decisions data={data} />}
            {tab === 'story' && <Story data={data} />}
            {tab === 'ask' && <Ask />}
          </>
        )}
      </AsyncSection>
    </>
  )
}
