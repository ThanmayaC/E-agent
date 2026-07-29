// UPI Ecosystem — analytics over the simulated transaction ledger: overview,
// feature / bank / PSP comparison, cities, trends & forecasts, and BI signals.
// Every number is read from the V7.0 aggregate cubes via /executive/ecosystem/*.
import { useState } from 'react'
import { api, fmt } from '../api/client'
import EChart, { PALETTE, axisStyle } from '../components/EChart'
import {
  AsyncSection, Badge, PageHeader, Panel, PanelEmpty, Stat, Tabs, Trend,
  severityTone, useAsync,
} from '../components/ui'

const INR = (v) => (v == null ? '—' : `₹${fmt.num(v)}`)

function barOption(names, values, { horizontal = false, color = PALETTE[0], rotate = 0 } = {}) {
  const cat = { type: 'category', data: names, ...axisStyle, axisLabel: { ...axisStyle.axisLabel, rotate } }
  const val = { type: 'value', ...axisStyle }
  return {
    tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
    grid: { left: horizontal ? 120 : 56, right: 20, top: 16, bottom: rotate ? 80 : 40 },
    xAxis: horizontal ? val : cat,
    yAxis: horizontal ? { ...cat, inverse: true } : val,
    series: [{
      type: 'bar',
      data: Array.isArray(color)
        ? values.map((v, i) => ({ value: v, itemStyle: { color: color[i] } }))
        : values,
      itemStyle: Array.isArray(color) ? undefined : { color, borderRadius: horizontal ? [0, 4, 4, 0] : [4, 4, 0, 0] },
      barMaxWidth: 34,
    }],
  }
}

const growthColor = (g) => (g > 0 ? '#34d399' : g < 0 ? '#fb7185' : '#64748b')

function CompareTable({ rows, cols }) {
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
            <tr key={r.name || i} className="border-b border-surface-border/50 hover:bg-surface-overlay/40">
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

function Overview({ data }) {
  const { overview, features, mix } = data
  const o = overview || {}
  const topFeat = (features || []).slice(0, 8)
  return (
    <div className="space-y-4">
      <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-4">
        <Stat label="Sampled transactions" value={fmt.num(o.sample_transactions)} hint={`${o.period?.days || 0} days`} />
        <Stat label="Sampled value" value={INR(o.sample_value_inr)} />
        <Stat label="Top feature" value={o.top_feature?.name || '—'}
              hint={o.top_feature ? `${o.top_feature.growth_pct > 0 ? '+' : ''}${o.top_feature.growth_pct}% m/m` : ''} />
        <Stat label="Top PSP" value={o.top_psp?.name || '—'}
              hint={o.top_psp ? `${o.top_psp.share_pct}% share` : ''} />
      </div>
      <div className="grid gap-4 lg:grid-cols-2">
        <Panel title="Top features by volume">
          <EChart height={300} option={barOption(topFeat.map((f) => f.name), topFeat.map((f) => f.txns), { horizontal: true })} />
        </Panel>
        <Panel title="Transaction mix">
          <EChart height={300} option={{
            tooltip: { trigger: 'item', formatter: '{b}: {c} ({d}%)' },
            series: [{
              type: 'pie', radius: ['45%', '72%'], center: ['50%', '50%'],
              data: (mix || []).map((m, i) => ({ name: m.payment_type, value: m.sample_txns, itemStyle: { color: PALETTE[i % PALETTE.length] } })),
              label: { color: '#94a3b8', fontSize: 11 },
            }],
          }} />
        </Panel>
      </div>
    </div>
  )
}

function Features({ data }) {
  const rows = data.features || []
  return (
    <div className="space-y-4">
      <Panel title="Feature growth (month over month)">
        <EChart height={300} option={barOption(rows.map((r) => r.name), rows.map((r) => r.growth_pct),
          { rotate: 35, color: rows.map((r) => growthColor(r.growth_pct)) })} />
      </Panel>
      <Panel title="All UPI features">
        <CompareTable rows={rows} cols={[
          { key: 'name', label: 'Feature' },
          { key: 'txns', label: 'Txns', right: true, render: (r) => fmt.num(r.txns) },
          { key: 'avg_ticket_inr', label: 'Avg ticket', right: true, render: (r) => INR(r.avg_ticket_inr) },
          { key: 'avg_success_rate', label: 'Success', right: true, render: (r) => (r.avg_success_rate == null ? '—' : `${r.avg_success_rate}%`) },
          { key: 'share_pct', label: 'Share', right: true, render: (r) => `${r.share_pct}%` },
          { key: 'growth_pct', label: 'Growth', right: true, render: (r) => <Trend change={r.growth_pct} suffix="%" /> },
        ]} />
      </Panel>
    </div>
  )
}

function EntityTab({ rows, label }) {
  const top = (rows || []).slice(0, 12)
  return (
    <div className="space-y-4">
      <Panel title={`${label} by sampled volume`}>
        <EChart height={320} option={barOption(top.map((r) => r.name), top.map((r) => r.txns), { horizontal: true })} />
      </Panel>
      <Panel title={`All ${label.toLowerCase()}`}>
        <CompareTable rows={rows} cols={[
          { key: 'name', label: label.replace(/s$/, '') },
          { key: 'txns', label: 'Txns', right: true, render: (r) => fmt.num(r.txns) },
          { key: 'share_pct', label: 'Share', right: true, render: (r) => `${r.share_pct}%` },
          { key: 'avg_success_rate', label: 'Success', right: true, render: (r) => (r.avg_success_rate == null ? '—' : `${r.avg_success_rate}%`) },
          { key: 'growth_pct', label: 'Growth', right: true, render: (r) => <Trend change={r.growth_pct} suffix="%" /> },
        ]} />
      </Panel>
    </div>
  )
}

function Cities({ data }) {
  const rows = data.cities || []
  const top = rows.slice(0, 12)
  return (
    <div className="space-y-4">
      <Panel title="Top cities by sampled volume">
        <EChart height={320} option={barOption(top.map((r) => r.name), top.map((r) => r.txns), { horizontal: true, color: PALETTE[4] })} />
      </Panel>
      <Panel title="All cities">
        <CompareTable rows={rows} cols={[
          { key: 'name', label: 'City' },
          { key: 'txns', label: 'Txns', right: true, render: (r) => fmt.num(r.txns) },
          { key: 'value_inr', label: 'Value', right: true, render: (r) => INR(r.value_inr) },
          { key: 'share_pct', label: 'Share', right: true, render: (r) => `${r.share_pct}%` },
        ]} />
      </Panel>
    </div>
  )
}

function TrendsForecast({ data }) {
  const fc = data.forecasts || []
  const totals = fc.filter((f) => f.series.startsWith('total::'))
  const featureFc = fc.filter((f) => f.series.startsWith('feature::'))
  const label = (s) => s.split('::')[1].replace(/_/g, ' ')
  return (
    <div className="space-y-4">
      <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-4">
        {totals.map((f) => (
          <Stat key={f.series} label={label(f.series)} value={fmt.num(f.today)}
                hint={<span>7d → {fmt.num(f.forecast_7d)} <Trend change={f.growth_pct} suffix="%" /></span>} />
        ))}
      </div>
      <Panel title="Feature volume — today vs 7-day forecast">
        <EChart height={320} option={{
          tooltip: { trigger: 'axis' },
          legend: { data: ['Today', 'Forecast +7d'], textStyle: { color: '#94a3b8' }, top: 0 },
          grid: { left: 56, right: 20, top: 32, bottom: 80 },
          xAxis: { type: 'category', data: featureFc.map((f) => label(f.series)), ...axisStyle, axisLabel: { ...axisStyle.axisLabel, rotate: 35 } },
          yAxis: { type: 'value', ...axisStyle },
          series: [
            { name: 'Today', type: 'bar', data: featureFc.map((f) => f.today), itemStyle: { color: PALETTE[0], borderRadius: [4, 4, 0, 0] }, barMaxWidth: 22 },
            { name: 'Forecast +7d', type: 'bar', data: featureFc.map((f) => f.forecast_7d), itemStyle: { color: PALETTE[1], borderRadius: [4, 4, 0, 0] }, barMaxWidth: 22 },
          ],
        }} />
      </Panel>
    </div>
  )
}

function Signals({ data }) {
  const findings = data.anomalies?.findings || data.anomalies?.anomalies || []
  if (!findings.length) return <PanelEmpty text="No business-intelligence signals detected." />
  return (
    <div className="space-y-2">
      {findings.map((f, i) => (
        <div key={i} className="card-pad flex items-start gap-3">
          <Badge tone={severityTone(f.severity)}>{f.severity}</Badge>
          <div className="min-w-0">
            <div className="text-sm text-slate-200">{f.finding}</div>
            <div className="text-xs text-slate-500 mt-0.5">
              {f.category?.replace(/_/g, ' ')}{f.entity ? ` · ${f.entity}` : ''}
            </div>
          </div>
        </div>
      ))}
    </div>
  )
}

const TABS = [
  { value: 'overview', label: 'Overview' },
  { value: 'features', label: 'Features' },
  { value: 'banks', label: 'Banks' },
  { value: 'psps', label: 'PSPs' },
  { value: 'cities', label: 'Cities' },
  { value: 'trends', label: 'Trends & Forecast' },
  { value: 'signals', label: 'BI / Anomalies' },
]

export default function EcosystemDashboard() {
  const [tab, setTab] = useState('overview')
  const state = useAsync(async () => {
    const [overview, features, banks, psps, cities, mix, forecasts, anomalies] = await Promise.all([
      api.ecosystemOverview().catch(() => ({})),
      api.ecosystemFeatures().catch(() => ({ features: [] })),
      api.ecosystemBanks().catch(() => ({ banks: [] })),
      api.ecosystemPsps().catch(() => ({ psps: [] })),
      api.ecosystemCities().catch(() => ({ cities: [] })),
      api.ecosystemMix().catch(() => ({ mix: [] })),
      api.ecosystemForecasts().catch(() => ({ forecasts: [] })),
      api.ecosystemAnomalies().catch(() => ({})),
    ])
    return {
      overview, features: features.features, banks: banks.banks, psps: psps.psps,
      cities: cities.cities, mix: mix.mix, forecasts: forecasts.forecasts, anomalies,
    }
  }, [])

  return (
    <>
      <PageHeader title="UPI Ecosystem"
        subtitle="Transaction-driven analytics — features, banks, PSPs, cities, trends and forecasts, from the simulated ledger" />
      <AsyncSection state={state} empty="No ecosystem data — generate and ingest the enterprise corpus (V7.0).">
        {(data) => (
          <>
            <Tabs tabs={TABS} active={tab} onChange={setTab} />
            {tab === 'overview' && <Overview data={data} />}
            {tab === 'features' && <Features data={data} />}
            {tab === 'banks' && <EntityTab rows={data.banks} label="Banks" />}
            {tab === 'psps' && <EntityTab rows={data.psps} label="PSPs" />}
            {tab === 'cities' && <Cities data={data} />}
            {tab === 'trends' && <TrendsForecast data={data} />}
            {tab === 'signals' && <Signals data={data} />}
          </>
        )}
      </AsyncSection>
    </>
  )
}
