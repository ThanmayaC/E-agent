// Products — every UPI product as a clean card: current status, last-week
// trend, open issues, latest release, recent reports, recent decisions.
import { Link } from 'react-router-dom'
import { api } from '../api/client'
import { AsyncSection, Badge, HealthRing, PageHeader, useAsync } from '../components/ui'

function ProductCard({ p, reports, decisions }) {
  const productReports = reports.filter((r) => (r.related_products || []).includes(p.product))
  const productDecisions = decisions.filter((d) => (d.affected_products || []).includes(p.product))
  const release = productReports.find((r) => r.category === 'Product Reports')
  return (
    <Link to={`/products/${encodeURIComponent(p.product)}`} className="card-pad card-hover block">
      <div className="flex items-start gap-4">
        <HealthRing score={p.health} size={56} label="status" />
        <div className="min-w-0 flex-1">
          <div className="font-medium text-slate-100 truncate">{p.product}</div>
          <div className="text-xs text-slate-500 mt-0.5 truncate">{p.owner || p.team || 'Unassigned'}</div>
          <div className="mt-2">
            <Badge tone={p.status === 'healthy' ? 'success' : p.status === 'recovered' ? 'info' : 'warn'}>
              {(p.status || 'status unknown').replace(/_/g, ' ')}
            </Badge>
          </div>
        </div>
      </div>
      <p className="text-xs text-slate-500 mt-3">{p.note}</p>
      <div className="mt-3 pt-3 border-t border-surface-border/60 space-y-1 text-xs text-slate-500">
        <div>Open issues: <span className="text-slate-300">{p.status === 'healthy' ? 0 : 1}</span></div>
        <div>Latest release: <span className="text-slate-300">{release?.title || 'None this month'}</span></div>
        <div>Recent reports: <span className="text-slate-300">{productReports.length}</span></div>
        <div>Recent decisions: <span className="text-slate-300">{productDecisions.length}</span></div>
      </div>
    </Link>
  )
}

export default function Products() {
  const state = useAsync(async () => {
    const [kpis, reportsRes, decisionsRes] = await Promise.all([
      api.executiveKpis().catch(() => null),
      api.executiveReports().catch(() => ({ reports: [] })),
      api.executiveDecisions().catch(() => ({ decisions: [] })),
    ])
    return {
      products: kpis?.health?.products || [],
      reports: reportsRes.reports || [],
      decisions: decisionsRes.decisions || [],
    }
  }, [])

  return (
    <>
      <PageHeader title="Products" subtitle="Status, trend, issues, releases, reports, and decisions for every UPI product" />
      <AsyncSection state={state} empty="No product data yet — the enterprise corpus may not be ingested.">
        {({ products, reports, decisions }) => (
          <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
            {products.map((p) => (
              <ProductCard key={p.product} p={p} reports={reports} decisions={decisions} />
            ))}
          </div>
        )}
      </AsyncSection>
    </>
  )
}
