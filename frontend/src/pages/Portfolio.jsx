// Portfolio — every product and business as an executive card: health,
// growth, risk, revenue, trend, and what to do next.
import { Link } from 'react-router-dom'
import { api } from '../api/client'
import {
  AsyncSection, Badge, HealthRing, PageHeader, Panel, PanelEmpty, Trend,
  healthTone, useAsync,
} from '../components/ui'

const PRIORITY_TONE = { invest: 'success', protect: 'info', fix: 'danger', question: 'warn', measure: 'default' }

function ScoreBar({ label, value }) {
  const pct = value == null ? 0 : Math.max(0, Math.min(100, value))
  const tone = value == null ? 'bg-slate-700' : value >= 70 ? 'bg-emerald-500' : value >= 50 ? 'bg-amber-500' : 'bg-rose-500'
  return (
    <div className="flex items-center gap-2 text-xs">
      <span className="w-14 text-slate-500">{label}</span>
      <div className="flex-1 h-1.5 rounded bg-surface-overlay overflow-hidden">
        <div className={`h-full rounded ${tone}`} style={{ width: `${pct}%` }} />
      </div>
      <span className="w-7 text-right tabular-nums text-slate-400">{value == null ? '—' : Math.round(value)}</span>
    </div>
  )
}

function ProductCard({ p }) {
  return (
    <Link to={`/portfolio/product/${encodeURIComponent(p.product_id)}`}
          className="card-pad card-hover block">
      <div className="flex items-start gap-4">
        <HealthRing score={p.health_score} size={56} label="health" />
        <div className="min-w-0 flex-1">
          <div className="flex items-center justify-between gap-2">
            <div className="font-medium text-slate-100 truncate">{p.product}</div>
            <Trend change={p.change} />
          </div>
          <div className="text-xs text-slate-500 mt-0.5 truncate">
            {p.owner || 'Unassigned'}{p.lifecycle ? ` · ${p.lifecycle}` : ''}
          </div>
          <div className="mt-2">
            <Badge tone={PRIORITY_TONE[p.investment_priority] || 'default'}>{(p.investment_priority || 'unranked').replace(/_/g, ' ')}</Badge>
          </div>
        </div>
      </div>
      <div className="mt-4 space-y-1.5">
        <ScoreBar label="Growth" value={p.growth_score} />
        <ScoreBar label="Risk" value={p.risk_score} />
        <ScoreBar label="Revenue" value={p.revenue_score} />
      </div>
      {p.priority_reason && (
        <div className="mt-3 pt-3 border-t border-surface-border/60 text-xs text-slate-500">{p.priority_reason}</div>
      )}
    </Link>
  )
}

export default function Portfolio() {
  const state = useAsync(async () => {
    const [products, overview] = await Promise.all([
      api.managerProducts().catch(() => null),
      api.managerPortfolio().catch(() => null),
    ])
    const ranking = products?.status === 'active'
      ? await api.productPortfolio().then((p) => p.product_ranking || []).catch(() => [])
      : []
    return { products, overview, ranking }
  }, [])

  return (
    <>
      <PageHeader title="Portfolio" subtitle="Health, growth, risk, and revenue across every product and business" />
      <AsyncSection state={state} empty="No portfolio yet — connect a data source under Settings.">
        {({ products, overview, ranking }) => {
          const ph = overview?.portfolio_health || {}
          const active = products?.status === 'active'
          return (
            <div className="space-y-6">
              <div className="grid gap-4 md:grid-cols-4">
                <div className="card-pad flex items-center gap-4">
                  <HealthRing score={active ? products.portfolio_health?.score : ph.average_health_score} size={56} />
                  <div>
                    <div className="eyebrow">Portfolio health</div>
                    <div className="text-sm text-slate-300 mt-1 capitalize">
                      {active ? (products.portfolio_health?.band || '—') : (ph.average_health_score != null ? '' : 'not measured')}
                    </div>
                  </div>
                </div>
                <div className="card-pad">
                  <div className="eyebrow">Products</div>
                  <div className="metric mt-1.5">{active ? products.products?.total ?? 0 : '—'}</div>
                  {active && <div className="text-xs text-slate-500 mt-1">{products.products?.measured ?? 0} measured</div>}
                </div>
                <div className="card-pad">
                  <div className="eyebrow">Growth</div>
                  <div className="metric mt-1.5 capitalize !text-xl">{active ? (products.portfolio_growth?.band || '—') : '—'}</div>
                </div>
                <div className="card-pad">
                  <div className="eyebrow">Risk</div>
                  <div className="metric mt-1.5 capitalize !text-xl">{active ? (products.portfolio_risk?.band || '—') : '—'}</div>
                </div>
              </div>

              {ranking.length > 0 && (
                <section>
                  <div className="h-sub mb-3">Products</div>
                  <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
                    {ranking.map((p) => <ProductCard key={p.product_id} p={p} />)}
                  </div>
                </section>
              )}

              {active && (products.open_recommendations || []).length > 0 && (
                <Panel title="Recommended strategy">
                  <ul className="space-y-2.5">
                    {products.open_recommendations.map((r, i) => (
                      <li key={i} className="text-sm text-slate-300 flex gap-2 items-start">
                        {r.priority && <Badge tone="accent">P{r.priority}</Badge>}
                        <span>
                          {r.action || r.recommendation || r.summary}
                          {r.product && <span className="text-slate-500"> — {r.product}</span>}
                        </span>
                      </li>
                    ))}
                  </ul>
                </Panel>
              )}

              {overview && (
                <section>
                  <div className="h-sub mb-3">Businesses under analysis</div>
                  <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
                    {(overview.projects || []).map((pr) => (
                      <Link key={pr.project_id} to={`/reports/${pr.project_id}`} className="card-pad card-hover block">
                        <div className="flex items-center gap-4">
                          <HealthRing score={pr.health_score} size={48} />
                          <div className="min-w-0">
                            <div className="font-medium text-slate-100 truncate">{pr.name}</div>
                            <div className="text-xs text-slate-500 mt-0.5">
                              <Badge tone={{ ready: 'success', failed: 'danger', awaiting_clarification: 'warn', analyzing: 'info' }[pr.status] || 'default'}>
                                {pr.status === 'awaiting_clarification' ? 'needs your input' : pr.status}
                              </Badge>
                              {pr.report_version ? <span className="ml-2">report v{pr.report_version}</span> : null}
                            </div>
                          </div>
                        </div>
                      </Link>
                    ))}
                  </div>
                </section>
              )}

              <div className="grid gap-5 lg:grid-cols-2">
                <Panel title="Portfolio risks">
                  {(overview?.risks || []).length === 0 ? <PanelEmpty text="No open risks." /> : (
                    <ul className="space-y-2">{overview.risks.slice(0, 6).map((r, i) =>
                      <li key={i} className="text-sm text-slate-300">{r.insight}</li>)}</ul>
                  )}
                </Panel>
                <Panel title="What moved">
                  {(overview?.historical_comparison || []).length === 0
                    ? <PanelEmpty text="Needs at least two reports per business." />
                    : <ul className="space-y-2">
                        {overview.historical_comparison.slice(0, 6).map((c, i) => (
                          <li key={i} className="text-sm text-slate-300 flex items-center gap-2">
                            <Trend change={c.change} /> {c.project_id}: {c.previous} → <span className={healthTone(c.latest)}>{c.latest}</span>
                          </li>
                        ))}
                      </ul>}
                </Panel>
              </div>
            </div>
          )
        }}
      </AsyncSection>
    </>
  )
}
