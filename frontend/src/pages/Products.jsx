// Products — every UPI product as a clean card, plus a Power-BI-style compare
// view: sortable columns, a filter, and click-to-drill into a product's metrics
// ranked against the rest of the portfolio.
import { useMemo, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { api } from '../api/client'
import { AsyncSection, Badge, HealthRing, PageHeader, Panel, Tabs, useAsync } from '../components/ui'
import {
  CompareTable, DrillHint, EntityDrawer, FilterInput, useDrilldown,
} from '../components/drilldown'

const statusTone = (s) => (s === 'healthy' ? 'success' : s === 'recovered' ? 'info' : 'warn')

function ProductCard({ p }) {
  return (
    <Link to={`/products/${encodeURIComponent(p.product)}`} className="card-pad card-hover block">
      <div className="flex items-start gap-4">
        <HealthRing score={p.health} size={56} label="status" />
        <div className="min-w-0 flex-1">
          <div className="font-medium text-slate-100 truncate">{p.product}</div>
          <div className="text-xs text-slate-500 mt-0.5 truncate">{p.owner || p.team || 'Unassigned'}</div>
          <div className="mt-2">
            <Badge tone={statusTone(p.status)}>{(p.status || 'status unknown').replace(/_/g, ' ')}</Badge>
          </div>
        </div>
      </div>
      <p className="text-xs text-slate-500 mt-3">{p.note}</p>
      <div className="mt-3 pt-3 border-t border-surface-border/60 space-y-1 text-xs text-slate-500">
        <div>Open issues: <span className="text-slate-300">{p.open_issues}</span></div>
        <div>Latest release: <span className="text-slate-300">{p.latest_release || 'None this month'}</span></div>
        <div>Recent reports: <span className="text-slate-300">{p.report_count}</span></div>
        <div>Recent decisions: <span className="text-slate-300">{p.decision_count}</span></div>
      </div>
    </Link>
  )
}

const PRODUCT_METRICS = [
  ['Health score', 'health', true, (v) => Math.round(v)],
  ['Recent reports', 'report_count', true, (v) => v],
  ['Recent decisions', 'decision_count', true, (v) => v],
  ['Open issues', 'open_issues', false, (v) => v],
]

function CompareView({ rows }) {
  const d = useDrilldown(rows, { key: 'product' })
  const navigate = useNavigate()
  return (
    <>
      <Panel title="Product portfolio"
             action={<FilterInput value={d.filter} onChange={d.setFilter}
                                  placeholder="Filter products…" />}>
        <DrillHint />
        <CompareTable rows={d.rows} idKey="product" filter={d.filter}
                      selected={d.selected} onRowClick={d.setSelected}
                      defaultSort="health"
                      cols={[
                        { key: 'product', label: 'Product' },
                        { key: 'owner', label: 'Owner', render: (r) => r.owner || r.team || '—' },
                        { key: 'status', label: 'Status',
                          render: (r) => <Badge tone={statusTone(r.status)}>{(r.status || 'unknown').replace(/_/g, ' ')}</Badge> },
                        { key: 'health', label: 'Health', right: true,
                          render: (r) => (r.health == null ? '—' : Math.round(r.health)) },
                        { key: 'open_issues', label: 'Issues', right: true },
                        { key: 'report_count', label: 'Reports', right: true },
                        { key: 'decision_count', label: 'Decisions', right: true },
                      ]} />
      </Panel>
      <EntityDrawer entity={d.selected} peers={d.rows} label="Product" idKey="product"
                    metrics={PRODUCT_METRICS} onClose={d.close}>
        {d.selected && (
          <button className="btn w-full"
                  onClick={() => navigate(`/products/${encodeURIComponent(d.selected.product)}`)}>
            Open full product summary →
          </button>
        )}
      </EntityDrawer>
    </>
  )
}

const VIEWS = [{ value: 'cards', label: 'Cards' }, { value: 'compare', label: 'Compare' }]

export default function Products() {
  const [view, setView] = useState('cards')
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
        {({ products, reports, decisions }) => <Body products={products} reports={reports}
                                                     decisions={decisions} view={view} setView={setView} />}
      </AsyncSection>
    </>
  )
}

// Joins each product to its reports/decisions once, so both views (and the
// drawer's peer ranking) read the same derived numbers.
function Body({ products, reports, decisions, view, setView }) {
  const rows = useMemo(() => products.map((p) => {
    const productReports = reports.filter((r) => (r.related_products || []).includes(p.product))
    const productDecisions = decisions.filter((d) => (d.affected_products || []).includes(p.product))
    return {
      ...p,
      report_count: productReports.length,
      decision_count: productDecisions.length,
      open_issues: p.status === 'healthy' ? 0 : 1,
      latest_release: productReports.find((r) => r.category === 'Product Reports')?.title || '',
    }
  }), [products, reports, decisions])

  return (
    <>
      <Tabs tabs={VIEWS} active={view} onChange={setView} />
      {view === 'cards' ? (
        <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
          {rows.map((p) => <ProductCard key={p.product} p={p} />)}
        </div>
      ) : (
        <CompareView rows={rows} />
      )}
    </>
  )
}
