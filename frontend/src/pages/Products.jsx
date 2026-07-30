// Products — every NPCI product ranked by real transaction volume, straight
// from the warehouse. Clicking any card opens its full Product Intelligence
// Dashboard (daily/monthly trends, banks, PSPs, merchants, MCCs, failures,
// forecast, AI summary) — nothing here is a stored or fabricated figure.
import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { api, fmt } from '../api/client'
import { AsyncSection, Badge, PageHeader, Panel, Tabs, useAsync } from '../components/ui'
import { CompareTable, DrillHint, FilterInput, useDrilldown } from '../components/drilldown'

const inr = (v) => `₹${fmt.num(v)}`

function ProductCard({ p }) {
  const healthy = p.success_rate >= 99
  return (
    <Link to={`/products/${encodeURIComponent(p.product_code)}`} className="card-pad card-hover block">
      <div className="flex items-start justify-between gap-3">
        <div className="min-w-0">
          <div className="font-medium text-slate-100 truncate">{p.product_name}</div>
          <div className="text-xs text-slate-500 mt-0.5 font-mono">{p.product_code}</div>
        </div>
        <Badge tone={healthy ? 'success' : p.success_rate >= 97 ? 'warn' : 'danger'}>
          {p.success_rate}% success
        </Badge>
      </div>
      <div className="mt-3 grid grid-cols-2 gap-3 text-xs">
        <div>
          <div className="text-slate-500">Attempts</div>
          <div className="text-slate-200 tabular-nums">{fmt.num(p.attempts)}</div>
        </div>
        <div>
          <div className="text-slate-500">Settled value</div>
          <div className="text-slate-200 tabular-nums">{inr(p.value_inr)}</div>
        </div>
        <div>
          <div className="text-slate-500">Share of volume</div>
          <div className="text-slate-200 tabular-nums">{p.share_pct}%</div>
        </div>
        <div>
          <div className="text-slate-500">Growth</div>
          <div className="text-slate-200 tabular-nums">
            {p.growth_pct == null ? '—' : fmt.pct(p.growth_pct)}
          </div>
        </div>
      </div>
      <div className="mt-3 pt-3 border-t border-surface-border/60">
        <div className="h-1.5 rounded-full bg-surface-overlay/60 overflow-hidden">
          <div className="h-full rounded-full bg-[var(--chart-1)]"
               style={{ width: `${Math.min(100, p.share_pct)}%` }} />
        </div>
      </div>
    </Link>
  )
}

const VIEWS = [{ value: 'cards', label: 'Cards' }, { value: 'compare', label: 'Compare' }]

function CompareView({ rows }) {
  const d = useDrilldown(rows, { key: 'product_code' })
  const navigate = useNavigate()
  return (
    <Panel title="Product portfolio"
           action={<FilterInput value={d.filter} onChange={d.setFilter} placeholder="Filter products…" />}>
      <DrillHint />
      <CompareTable rows={d.rows} idKey="product_code" filter={d.filter}
                    selected={d.selected}
                    onRowClick={(r) => navigate(`/products/${encodeURIComponent(r.product_code)}`)}
                    defaultSort="attempts"
                    cols={[
                      { key: 'product_name', label: 'Product' },
                      { key: 'attempts', label: 'Attempts', right: true,
                        render: (r) => fmt.num(r.attempts) },
                      { key: 'success_rate', label: 'Success %', right: true },
                      { key: 'value_inr', label: 'Value', right: true,
                        render: (r) => inr(r.value_inr) },
                      { key: 'share_pct', label: 'Share %', right: true },
                      { key: 'technical_decline_pct', label: 'Tech. decline %', right: true },
                      { key: 'retry_rate_pct', label: 'Retry %', right: true },
                    ]} />
    </Panel>
  )
}

export default function Products() {
  const [view, setView] = useState('cards')
  const state = useAsync(() => api.intelProducts(), [])

  return (
    <>
      <PageHeader title="Products"
                  subtitle="Every NPCI product ranked by real transaction volume, success rate, and settled value" />
      <AsyncSection state={state} empty="No transactions ingested yet — the warehouse holds no data.">
        {(data) => {
          const rows = data.products || []
          return (
            <div className="space-y-4">
              <Tabs tabs={VIEWS} active={view} onChange={setView} />
              {view === 'cards' ? (
                <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
                  {rows.map((p) => <ProductCard key={p.product_code} p={p} />)}
                </div>
              ) : (
                <CompareView rows={rows} />
              )}
            </div>
          )
        }}
      </AsyncSection>
    </>
  )
}
