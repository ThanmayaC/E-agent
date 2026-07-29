// Reusable BI interactivity: the sort / filter / drill-down pattern shared by
// every entity dashboard (ecosystem features, banks, PSPs, cities, products).
//
// Deliberately data-agnostic — a caller supplies rows plus a column spec and a
// metric spec, and gets Power-BI-style behaviour with no extra fetches: peer
// ranks are computed from the rows already loaded.
import { useMemo, useState } from 'react'
import { PanelEmpty, Badge } from './ui'

/** Sort/filter state for a table, shared between a chart and its table so a
 *  chart click and a row click select the same entity. */
export function useDrilldown(rows, { key = 'name' } = {}) {
  const [selected, setSelected] = useState(null)
  const [filter, setFilter] = useState('')
  const list = rows || []
  return {
    selected, setSelected, filter, setFilter, rows: list,
    /** select by the identifying value (used for chart clicks) */
    selectByName: (value) =>
      setSelected(list.find((r) => r[key] === value) || null),
    close: () => setSelected(null),
  }
}

/** Rank an entity against its peers on one metric. Returns null when the
 *  metric is absent or non-numeric, so callers can skip the row. */
export function peerRank(entity, peers, key, higherBetter = true) {
  const vals = (peers || []).map((p) => p[key]).filter((v) => typeof v === 'number')
  if (!vals.length || typeof entity?.[key] !== 'number') return null
  const better = vals.filter((v) => (higherBetter ? v > entity[key] : v < entity[key])).length
  return { position: better + 1, of: vals.length, pct: Math.round((1 - better / vals.length) * 100) }
}

/** Power-BI-style table: click a header to sort (numeric-aware), click a row
 *  to drill in. `idKey` identifies a row for selection/keying. */
export function CompareTable({
  rows, cols, onRowClick, selected, filter = '', idKey = 'name', defaultSort,
}) {
  const [sortKey, setSortKey] = useState(
    defaultSort || cols.find((c) => c.right)?.key || cols[0].key)
  const [dir, setDir] = useState('desc')

  const view = useMemo(() => {
    const f = filter.trim().toLowerCase()
    const out = (rows || []).filter((r) => !f ||
      cols.some((c) => String(r[c.key] ?? '').toLowerCase().includes(f)))
    out.sort((a, b) => {
      const av = a[sortKey], bv = b[sortKey]
      const cmp = typeof av === 'number' && typeof bv === 'number'
        ? av - bv
        : String(av ?? '').localeCompare(String(bv ?? ''))
      return dir === 'desc' ? -cmp : cmp
    })
    return out
  }, [rows, cols, filter, sortKey, dir])

  if (!rows?.length) return <PanelEmpty text="No data." />
  const toggle = (key) => {
    if (key === sortKey) setDir(dir === 'desc' ? 'asc' : 'desc')
    else { setSortKey(key); setDir('desc') }
  }
  if (!view.length) return <PanelEmpty text="No rows match that filter." />

  return (
    <div className="overflow-x-auto">
      <table className="w-full text-sm">
        <thead>
          <tr className="text-left text-xs uppercase tracking-wide text-slate-500 border-b border-surface-border">
            {cols.map((c) => (
              <th key={c.key} onClick={() => toggle(c.key)}
                  title={`Sort by ${c.label}`}
                  className={`py-2 pr-4 cursor-pointer select-none hover:text-slate-300 ${c.right ? 'text-right' : ''}`}>
                {c.label}
                {sortKey === c.key && <span className="ml-1 text-accent">{dir === 'desc' ? '↓' : '↑'}</span>}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {view.map((r, i) => (
            <tr key={r[idKey] ?? i} onClick={() => onRowClick?.(r)}
                className={`border-b border-surface-border/50 ${onRowClick ? 'cursor-pointer' : ''} ${
                  selected && selected[idKey] === r[idKey]
                    ? 'bg-accent/10' : 'hover:bg-surface-overlay/40'}`}>
              {cols.map((c) => (
                <td key={c.key} className={`py-2 pr-4 tabular-nums ${c.right ? 'text-right' : 'text-slate-200'}`}>
                  {c.render ? c.render(r) : (r[c.key] ?? '—')}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

/** Drill-down drawer: an entity's metrics plus where it ranks among peers.
 *  `metrics` is [label, key, higherBetter, format] tuples. */
export function EntityDrawer({
  entity, peers, label, onClose, metrics = [], idKey = 'name', children,
}) {
  if (!entity) return null
  const shown = metrics.filter(([, k]) => entity[k] != null)
  return (
    <div className="fixed inset-0 z-50 flex justify-end bg-black/50" onClick={onClose}>
      <div className="w-full max-w-md h-full bg-surface-raised border-l border-surface-border overflow-y-auto p-6"
           onClick={(e) => e.stopPropagation()} role="dialog" aria-label={`${label} detail`}>
        <div className="flex items-start justify-between">
          <div>
            <Badge tone="accent">{label}</Badge>
            <h2 className="text-lg font-bold text-slate-100 mt-2">{entity[idKey]}</h2>
          </div>
          <button onClick={onClose} aria-label="Close"
                  className="text-slate-500 hover:text-slate-200">✕</button>
        </div>
        <div className="mt-5 space-y-3">
          {shown.map(([lbl, key, higherBetter = true, format]) => {
            const r = peerRank(entity, peers, key, higherBetter)
            return (
              <div key={key} className="card-pad">
                <div className="flex items-center justify-between">
                  <span className="text-xs uppercase tracking-wide text-slate-500">{lbl}</span>
                  {r && <span className="text-[11px] text-slate-500">#{r.position} of {r.of} · P{r.pct}</span>}
                </div>
                <div className="metric mt-1 text-slate-100">
                  {format ? format(entity[key]) : entity[key]}
                </div>
                {r && (
                  <div className="mt-1.5 h-1.5 rounded bg-surface-overlay overflow-hidden">
                    <div className="h-full bg-accent" style={{ width: `${r.pct}%` }} />
                  </div>
                )}
              </div>
            )
          })}
        </div>
        {children && <div className="mt-5">{children}</div>}
      </div>
    </div>
  )
}

/** Standard hint shown above an interactive table. */
export const DrillHint = () => (
  <div className="text-[11px] text-slate-500 mb-2">
    Click a column to sort · click a row to drill in
  </div>
)

/** Compact filter input for a Panel `action` slot. */
export function FilterInput({ value, onChange, placeholder = 'Filter…' }) {
  return (
    <input className="input !py-1 !text-xs w-40" placeholder={placeholder}
           value={value} onChange={(e) => onChange(e.target.value)} />
  )
}
