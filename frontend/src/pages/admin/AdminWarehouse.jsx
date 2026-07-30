// Admin · Transaction Warehouse — the internals of the raw-transaction store.
// Partitions, logical tables, the live query log with real latencies, and the
// transaction schema. Everything is read from the warehouse itself; there is no
// synthetic health number on this page.
import { api, fmt } from '../../api/client'
import { AsyncSection, Badge, PageHeader, Panel, Stat, useAsync } from '../../components/ui'

export default function AdminWarehouse() {
  const state = useAsync(() => api.intelAdminWarehouse(), [])
  return (
    <div className="space-y-6">
      <PageHeader
        title="Transaction Warehouse"
        subtitle="DuckDB over the raw parquet corpus — no aggregate tables, no rollups. Every KPI in the platform is a query against this layer."
      />
      <AsyncSection state={state}>
        {({ status, tables, recent_queries, schema }) => {
          const st = status || {}
          const cache = st.cache || {}
          return (
            <div className="space-y-6">
              <div className="grid gap-3 grid-cols-2 lg:grid-cols-4">
                <Stat label="Transactions" value={fmt.num(st.transactions)} tone="fg-primary" />
                <Stat label="Partitions (days)" value={st.partitions} />
                <Stat label="On disk" value={`${st.mb_on_disk ?? '—'} MB`} />
                <Stat label="Query cache hit-rate" value={`${cache.hit_rate_pct ?? 0}%`}
                      tone="fg-success" hint={`${cache.hits ?? 0} hits · ${cache.misses ?? 0} misses`} />
              </div>

              <div className="grid gap-6 lg:grid-cols-2">
                <Panel title="Logical tables">
                  <div className="space-y-1">
                    {(tables || []).map((t) => (
                      <div key={t.table} className="flex items-center justify-between text-sm py-1 border-b border-surface-border/40 last:border-0">
                        <span className="font-mono text-slate-300">{t.table}</span>
                        <span className="flex items-center gap-2">
                          <Badge tone={t.kind === 'reference' ? 'info' : 'accent'}>{t.kind}</Badge>
                          <span className="text-slate-400 tabular-nums w-24 text-right">{fmt.num(t.rows)}</span>
                        </span>
                      </div>
                    ))}
                  </div>
                </Panel>

                <Panel title="Recent queries" action={<span className="text-xs text-slate-500">live query log</span>}>
                  <div className="space-y-1 max-h-[360px] overflow-y-auto">
                    {(recent_queries || []).slice(0, 24).map((q, i) => (
                      <div key={i} className="flex items-center justify-between gap-3 text-xs py-1 border-b border-surface-border/40 last:border-0">
                        <span className="text-slate-400 truncate flex-1" title={q.label}>{q.label || '(query)'}</span>
                        <span className="tabular-nums text-slate-500 w-14 text-right">{fmt.num(q.rows)} rows</span>
                        <Badge tone={q.cached ? 'success' : q.ms > 500 ? 'warn' : 'default'}>
                          {q.cached ? 'cached' : `${q.ms}ms`}
                        </Badge>
                      </div>
                    ))}
                    {(!recent_queries || recent_queries.length === 0) &&
                      <div className="text-sm text-slate-500">No queries run yet this session.</div>}
                  </div>
                </Panel>
              </div>

              <Panel title="Transaction schema" action={<span className="text-xs text-slate-500">{(schema || []).length} columns</span>}>
                <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-x-6 gap-y-1">
                  {(schema || []).map((col) => (
                    <div key={col.column_name} className="flex items-baseline justify-between gap-2 text-xs py-0.5 border-b border-surface-border/30">
                      <span className="font-mono text-slate-300 truncate">{col.column_name}</span>
                      <span className="text-slate-600 shrink-0">{String(col.column_type).toLowerCase()}</span>
                    </div>
                  ))}
                </div>
              </Panel>
            </div>
          )
        }}
      </AsyncSection>
    </div>
  )
}
