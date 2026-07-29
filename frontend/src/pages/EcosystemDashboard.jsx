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
import {
  CompareTable, DrillHint, EntityDrawer, FilterInput, useDrilldown,
} from '../components/drilldown'

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

const pct = (v) => (v == null ? '—' : `${v}%`)

// Metric spec for the drill-down drawer — shared by every ecosystem entity
// (features, banks, PSPs, cities). Absent metrics are skipped automatically.
const ENTITY_METRICS = [
  ['Transactions', 'txns', true, fmt.num],
  ['Value ₹', 'value_inr', true, INR],
  ['Market share %', 'share_pct', true, pct],
  ['Success rate %', 'avg_success_rate', true, pct],
  ['Growth % m/m', 'growth_pct', true, pct],
  ['Avg ticket ₹', 'avg_ticket_inr', true, INR],
]

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

// One interactive entity tab, reused for features / banks / PSPs / cities:
// chart click and row click drive the same selection, columns sort, the filter
// narrows the table, and the drawer ranks the picked entity against its peers.
function EntityTab({ rows, label, cols, chart = 'volume', singular }) {
  const d = useDrilldown(rows)
  // naive de-pluralisation mangles irregulars ("Cities" → "Citie"), so the
  // caller passes the singular whenever stripping a trailing "s" is wrong
  const one = singular || label.replace(/s$/, '')
  const top = d.rows.slice(0, 12)
  const chartOption = chart === 'growth'
    ? barOption(d.rows.map((r) => r.name), d.rows.map((r) => r.growth_pct),
                { rotate: 35, color: d.rows.map((r) => growthColor(r.growth_pct)) })
    : barOption(top.map((r) => r.name), top.map((r) => r.txns),
                { horizontal: true, color: chart === 'cities' ? PALETTE[4] : PALETTE[0] })
  return (
    <div className="space-y-4">
      <Panel title={chart === 'growth'
        ? `${label} growth (month over month)` : `${label} by sampled volume`}>
        <EChart height={320} option={chartOption} onClick={(p) => d.selectByName(p.name)} />
      </Panel>
      <Panel title={`All ${label.toLowerCase()}`}
             action={<FilterInput value={d.filter} onChange={d.setFilter}
                                  placeholder={`Filter ${label.toLowerCase()}…`} />}>
        <DrillHint />
        <CompareTable rows={d.rows} filter={d.filter} selected={d.selected}
                      onRowClick={d.setSelected}
                      cols={[{ key: 'name', label: one }, ...cols]} />
      </Panel>
      <EntityDrawer entity={d.selected} peers={d.rows} label={one}
                    metrics={ENTITY_METRICS} onClose={d.close} />
    </div>
  )
}

const COL_TXNS = { key: 'txns', label: 'Txns', right: true, render: (r) => fmt.num(r.txns) }
const COL_SHARE = { key: 'share_pct', label: 'Share', right: true, render: (r) => pct(r.share_pct) }
const COL_SUCCESS = { key: 'avg_success_rate', label: 'Success', right: true, render: (r) => pct(r.avg_success_rate) }
const COL_GROWTH = { key: 'growth_pct', label: 'Growth', right: true, render: (r) => <Trend change={r.growth_pct} suffix="%" /> }
const COL_TICKET = { key: 'avg_ticket_inr', label: 'Avg ticket', right: true, render: (r) => INR(r.avg_ticket_inr) }
const COL_VALUE = { key: 'value_inr', label: 'Value', right: true, render: (r) => INR(r.value_inr) }

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
            {tab === 'features' && (
              <EntityTab rows={data.features} label="Features" chart="growth"
                         cols={[COL_TXNS, COL_TICKET, COL_SUCCESS, COL_SHARE, COL_GROWTH]} />
            )}
            {tab === 'banks' && (
              <EntityTab rows={data.banks} label="Banks"
                         cols={[COL_TXNS, COL_SHARE, COL_SUCCESS, COL_GROWTH]} />
            )}
            {tab === 'psps' && (
              <EntityTab rows={data.psps} label="PSPs"
                         cols={[COL_TXNS, COL_SHARE, COL_SUCCESS, COL_GROWTH]} />
            )}
            {tab === 'cities' && (
              <EntityTab rows={data.cities} label="Cities" chart="cities" singular="City"
                         cols={[COL_TXNS, COL_VALUE, COL_SHARE]} />
            )}
            {tab === 'trends' && <TrendsForecast data={data} />}
            {tab === 'signals' && <Signals data={data} />}
          </>
        )}
      </AsyncSection>
    </>
  )
}
