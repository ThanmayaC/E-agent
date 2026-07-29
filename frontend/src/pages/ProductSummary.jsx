// Product executive summary — one product, explained in business terms:
// health, growth signals, risks, and the recommended next moves.
import { Link, useParams } from 'react-router-dom'
import { api } from '../api/client'
import {
  AsyncSection, Badge, HealthRing, PageHeader, Panel, PanelEmpty, Trend,
  severityTone, useAsync,
} from '../components/ui'

const KIND_TONE = {
  growth_opportunity: 'success', expansion: 'success', cross_sell: 'info',
  declining_product: 'danger', cannibalization: 'warn', gap: 'warn',
}

export default function ProductSummary() {
  const { productId } = useParams()
  const productName = decodeURIComponent(productId)
  const state = useAsync(async () => {
    const [catalog, health, reviews, growth, recs, kpis, reportsRes, decisionsRes] = await Promise.all([
      api.productCatalogItem(productId).catch(() => null),
      api.productHealth().catch(() => ({ health: [] })),
      api.productReviewsFor(productId, 1).catch(() => ({ reviews: [] })),
      api.productGrowth(productId).catch(() => ({ findings: [] })),
      api.productRecommendations(productId).catch(() => ({ recommendations: [] })),
      api.executiveKpis().catch(() => null),
      api.executiveReports().catch(() => ({ reports: [] })),
      api.executiveDecisions().catch(() => ({ decisions: [] })),
    ])
    const healthRecord = (health.health || []).find((h) => h.product_id === productId) || null
    const execProduct = (kpis?.health?.products || []).find((p) => p.product === productName) || null
    return {
      catalog,
      health: healthRecord,
      execProduct,
      review: (reviews.reviews || [])[0] || null,
      findings: growth.findings || [],
      recommendations: recs.recommendations || [],
      reports: (reportsRes.reports || []).filter((r) => (r.related_products || []).includes(productName)),
      decisions: (decisionsRes.decisions || []).filter((d) => (d.affected_products || []).includes(productName)),
    }
  }, [productId])

  return (
    <AsyncSection state={state} empty="This product has no data yet.">
      {({ catalog, health, execProduct, review, findings, recommendations, reports, decisions }) => {
        const name = catalog?.name || execProduct?.product || review?.product || productName
        const scores = health?.scores || {}
        return (
          <>
            <div className="text-xs text-slate-500 mb-3">
              <Link to="/products" className="hover:text-accent">Products</Link> <span className="mx-1">/</span> {name}
            </div>
            <PageHeader title={name}
                        subtitle={[catalog?.owner && `Owned by ${catalog.owner}`,
                                   catalog?.business_unit, catalog?.lifecycle,
                                   !catalog && execProduct?.owner && `Owned by ${execProduct.owner}`,
                                   !catalog && execProduct?.team]
                          .filter(Boolean).join(' · ') || 'Executive summary'} />
            <div className="space-y-5">
              <div className="card-pad flex flex-wrap items-center gap-6 lg:gap-10">
                <HealthRing score={health?.health_score ?? execProduct?.health} size={88} label="status" />
                <div className="flex-1 min-w-[220px] grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
                  {['growth', 'risk', 'revenue', 'engagement'].filter((k) => scores[k] != null).map((k) => (
                    <div key={k}>
                      <div className="eyebrow capitalize">{k}</div>
                      <div className="metric !text-xl mt-1">{Math.round(scores[k])}</div>
                    </div>
                  ))}
                  <div>
                    <div className="eyebrow">Trend</div>
                    <div className="mt-2"><Trend change={health?.change} suffix=" pts" /></div>
                  </div>
                  {health?.band && (
                    <div>
                      <div className="eyebrow">Standing</div>
                      <div className="mt-2"><Badge tone={health.band === 'healthy' ? 'success' : health.band === 'watch' ? 'warn' : 'danger'}>{health.band}</Badge></div>
                    </div>
                  )}
                </div>
              </div>

              {review?.executive_summary && (
                <Panel title="Executive summary"
                       action={review.generated_at &&
                         <span className="text-xs text-slate-600">{new Date(review.generated_at).toLocaleDateString()}</span>}>
                  <p className="text-sm text-slate-300 leading-relaxed whitespace-pre-wrap">{review.executive_summary}</p>
                </Panel>
              )}

              <div className="grid gap-5 lg:grid-cols-2">
                <Panel title="Risks">
                  {((review?.risks || []).filter((r) => r.severity !== 'none')).length === 0
                    ? <PanelEmpty text="No open risks for this product." />
                    : <ul className="space-y-2.5">
                        {review.risks.filter((r) => r.severity !== 'none').map((r, i) => (
                          <li key={i} className="text-sm text-slate-300 flex gap-2 items-start">
                            <Badge tone={severityTone(r.severity)}>{r.severity}</Badge>
                            <span>{r.risk || r.summary || r.detail}</span>
                          </li>
                        ))}
                      </ul>}
                </Panel>

                <Panel title="Growth signals">
                  {findings.length === 0 ? <PanelEmpty text="No growth signals yet." /> : (
                    <ul className="space-y-2.5">
                      {findings.slice(0, 8).map((f, i) => (
                        <li key={i} className="text-sm text-slate-300 flex gap-2 items-start">
                          <Badge tone={KIND_TONE[f.kind] || 'default'}>{(f.kind || 'signal').replace(/_/g, ' ')}</Badge>
                          <span>{f.summary || f.finding || f.detail}</span>
                        </li>
                      ))}
                    </ul>
                  )}
                </Panel>

                <Panel title="Recommended actions">
                  {recommendations.length === 0 ? <PanelEmpty text="No open recommendations." /> : (
                    <ul className="space-y-3">
                      {recommendations.slice(0, 8).map((r, i) => (
                        <li key={i} className="text-sm">
                          <div className="text-slate-200">
                            {r.priority && <Badge tone="accent">P{r.priority}</Badge>} {r.action || r.recommendation}
                          </div>
                          {(r.impact || r.effort) && (
                            <div className="text-xs text-slate-500 mt-0.5">
                              {r.impact && <>impact: {r.impact}</>}{r.impact && r.effort && ' · '}{r.effort && <>effort: {r.effort}</>}
                            </div>
                          )}
                        </li>
                      ))}
                    </ul>
                  )}
                </Panel>

                <Panel title="Action items from the latest review">
                  {(review?.action_items || []).length === 0 ? <PanelEmpty text="No action items recorded." /> : (
                    <ul className="space-y-2">
                      {review.action_items.map((a, i) => (
                        <li key={i} className="text-sm text-slate-300">• {typeof a === 'string' ? a : a.action || a.title}</li>
                      ))}
                    </ul>
                  )}
                </Panel>

                <Panel title="Recent reports">
                  {reports.length === 0 ? <PanelEmpty text="No reports for this product yet." /> : (
                    <ul className="space-y-2">
                      {reports.slice(0, 6).map((r) => (
                        <li key={r.report_id} className="text-sm text-slate-300 truncate">
                          <Badge tone="default">{r.category}</Badge> {r.title}
                        </li>
                      ))}
                    </ul>
                  )}
                </Panel>

                <Panel title="Recent decisions">
                  {decisions.length === 0 ? <PanelEmpty text="No decisions for this product yet." /> : (
                    <ul className="space-y-2">
                      {decisions.slice(0, 6).map((d) => (
                        <li key={d.decision_id} className="text-sm text-slate-300 truncate">
                          <Badge tone={d.status === 'executed' ? 'success' : 'warn'}>{d.status}</Badge> {d.title}
                        </li>
                      ))}
                    </ul>
                  )}
                </Panel>
              </div>
            </div>
          </>
        )
      }}
    </AsyncSection>
  )
}
