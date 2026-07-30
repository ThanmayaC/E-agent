// Product Intelligence Dashboard — one NPCI product, fully derived from its
// raw transactions: overview, daily/monthly trends, banks, PSPs, merchants,
// MCCs, failures, ML forecast (with confidence, drivers, risks, actions), and
// a grounded AI summary. Nothing here is a stored dashboard — every figure is
// a live query over /intel/products/{code}.
import { useMemo, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { api, fmt } from '../api/client'
import { AsyncSection, Badge, PageHeader, Panel, PanelEmpty, Stat, useAsync } from '../components/ui'
import EChart from '../components/EChart'
import { MLForecastPanel } from '../components/MLForecast'
import AskAI from '../components/AskAI'
import DimensionTable from '../components/DimensionTable'

const inr = (v) => `₹${fmt.num(v)}`
const KPI_ORDER = ['attempts', 'successful', 'success_rate', 'value_inr',
  'avg_ticket_inr', 'active_customers', 'p95_latency_ms', 'retry_rate_pct']

function DailyChart({ daily }) {
  const METRICS = [
    ['attempts', 'Attempts'], ['success_rate', 'Success rate %'],
    ['value_inr', 'Settled value'], ['technical_decline_pct', 'Technical decline %'],
    ['retry_rate_pct', 'Retry rate %'], ['p95_latency_ms', 'p95 latency (ms)'],
  ]
  const [metric, setMetric] = useState('attempts')
  const label = METRICS.find(([k]) => k === metric)?.[1] || metric
  const option = useMemo(() => ({
    tooltip: { trigger: 'axis' },
    grid: { left: 56, right: 20, top: 20, bottom: 32 },
    xAxis: { type: 'category', data: daily.map((d) => d.date),
             axisLabel: { rotate: 45, fontSize: 10, interval: Math.floor(daily.length / 20) } },
    yAxis: { type: 'value', axisLabel: { fontSize: 10 } },
    series: [{ type: 'line', data: daily.map((d) => d[metric]), symbol: 'none', smooth: 0.15,
               areaStyle: { opacity: 0.08 } }],
  }), [daily, metric])

  return (
    <Panel title="Daily trend"
           action={
             <select className="input !py-1 !text-xs" value={metric}
                     onChange={(e) => setMetric(e.target.value)}>
               {METRICS.map(([k, l]) => <option key={k} value={k}>{l}</option>)}
             </select>
           }>
      <EChart option={option} height={260} />
      <div className="text-[11px] fg-muted mt-1">{label} · {daily.length} day(s)</div>
    </Panel>
  )
}

function MonthlyTable({ monthly }) {
  if (!monthly.length) return null
  return (
    <Panel title="Monthly trend">
      <div className="overflow-x-auto">
        <table className="table-base">
          <thead>
            <tr><th>Month</th><th>Attempts</th><th>Success %</th><th>Value</th><th>Active customers</th></tr>
          </thead>
          <tbody>
            {monthly.map((m) => (
              <tr key={m.month}>
                <td className="text-xs font-mono">{m.month}</td>
                <td className="text-xs tabular-nums">{fmt.num(m.attempts)}</td>
                <td className="text-xs tabular-nums">{m.success_rate}%</td>
                <td className="text-xs tabular-nums">{inr(m.value_inr)}</td>
                <td className="text-xs tabular-nums">{fmt.num(m.active_customers)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </Panel>
  )
}

function FailuresPanel({ failures }) {
  const byCode = failures?.by_code || []
  const byOwner = failures?.by_owner || []
  const byBank = failures?.by_bank || []
  return (
    <div className="grid lg:grid-cols-2 gap-4">
      <Panel title="Top failure reasons">
        {byCode.length === 0 ? <PanelEmpty text="No failures in this window." /> : (
          <div className="overflow-x-auto">
            <table className="table-base">
              <thead><tr><th>Code</th><th>Reason</th><th>Owner</th><th>Share</th></tr></thead>
              <tbody>
                {byCode.slice(0, 10).map((f) => (
                  <tr key={f.code}>
                    <td className="text-xs font-mono">{f.code}</td>
                    <td className="text-xs">{f.reason}</td>
                    <td className="text-xs"><Badge tone={f.retryable ? 'warn' : 'danger'}>{f.owner}</Badge></td>
                    <td className="text-xs tabular-nums">{f.share_pct}%</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </Panel>
      <Panel title="Failure ownership & top failing banks">
        <div className="flex flex-wrap gap-2 mb-3">
          {byOwner.map((o) => (
            <Badge key={o.owner} tone="default">{o.owner}: {o.share_pct}%</Badge>
          ))}
        </div>
        {byBank.length === 0 ? <PanelEmpty text="No bank-level failures." /> : (
          <div className="overflow-x-auto">
            <table className="table-base">
              <thead><tr><th>Bank</th><th>Failure rate</th><th>Technical %</th></tr></thead>
              <tbody>
                {byBank.slice(0, 8).map((b) => (
                  <tr key={b.bank}>
                    <td className="text-xs">{b.bank}</td>
                    <td className="text-xs tabular-nums">{b.failure_rate_pct}%</td>
                    <td className="text-xs tabular-nums">{b.technical_pct}%</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </Panel>
    </div>
  )
}

export default function ProductSummary() {
  const { productId } = useParams()
  const state = useAsync(() => api.intelProduct(productId, { horizon: 14 }), [productId])

  return (
    <AsyncSection state={state} empty="This product has no transactions in the warehouse.">
      {(d) => {
        const p = d.product
        const kpiByKey = Object.fromEntries((d.kpis || []).map((k) => [k.key, k]))
        return (
          <>
            <div className="text-xs text-slate-500 mb-3">
              <Link to="/products" className="hover:text-accent">Products</Link>
              <span className="mx-1">/</span> {p.product_name}
            </div>
            <PageHeader title={p.product_name}
                        subtitle={[p.product_code, p.family, p.owning_team, p.lifecycle]
                          .filter(Boolean).join(' · ')} />
            {p.description && <p className="text-sm fg-muted -mt-3 mb-5">{p.description}</p>}

            <div className="space-y-5">
              <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
                {KPI_ORDER.filter((k) => kpiByKey[k]).map((k) => {
                  const kpi = kpiByKey[k]
                  return (
                    <Stat key={k} label={kpi.label}
                          value={kpi.unit === '₹' ? inr(kpi.value)
                                 : kpi.unit === '%' ? `${kpi.value}%` : fmt.num(kpi.value)}
                          hint={kpi.change_pct != null ? fmt.pct(kpi.change_pct) : undefined} />
                  )
                })}
              </div>

              <DailyChart daily={d.daily} />
              <MonthlyTable monthly={d.monthly} />

              <div className="grid lg:grid-cols-2 gap-4">
                <DimensionTable title="Banks" rows={d.banks} nameLabel="Bank" />
                <DimensionTable title="PSPs" rows={d.psps} nameLabel="PSP" />
              </div>
              <div className="grid lg:grid-cols-2 gap-4">
                <DimensionTable title="Top merchants" rows={d.top_merchants} nameLabel="Merchant" />
                <DimensionTable title="Top MCCs" rows={d.top_mccs} nameLabel="MCC subcategory" />
              </div>
              <DimensionTable title="Customer segments" rows={d.segments} nameLabel="Segment" />

              <FailuresPanel failures={d.failures} />

              <AskAI title="AI summary"
                     question={`Summarize ${p.product_name}'s performance, growth, risks, and recommended actions using the real transaction data.`} />

              <div>
                <div className="h-sub mb-2">Forecast</div>
                <MLForecastPanel d={d.forecast} compact />
              </div>
            </div>
          </>
        )
      }}
    </AsyncSection>
  )
}
