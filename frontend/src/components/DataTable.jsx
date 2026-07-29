// Reusable enterprise-grade interactive table + drill-down drawer.
// - DataTable: sortable columns (numeric-aware), filter, click-to-drill rows.
// - DrillDrawer: an entity's metric set plus where it ranks among peers
//   (percentile), computed from the rows already loaded — real data, no fetch.
// Both are config-driven so every dashboard (banks, PSPs, features, cities,
// products, merchants) reuses the same behaviour.
import { useState } from 'react'
import { Badge } from './ui'

export function DataTable({ rows, cols, onRowClick, selected, filterPlaceholder = 'Filter…', showFilter = true }) {
  const [sortKey, setSortKey] = useState(cols.find((c) => c.right)?.key || cols[0].key)
  const [dir, setDir] = useState('desc')
  const [filter, setFilter] = useState('')
  if (!rows?.length) return <div className="text-sm text-slate-600">No data.</div>

  const toggle = (key) => {
    if (key === sortKey) setDir(dir === 'desc' ? 'asc' : 'desc')
    else { setSortKey(key); setDir('desc') }
  }
  const f = filter.trim().toLowerCase()
  const nameKey = cols[0].key
  let view = f ? rows.filter((r) => String(r[nameKey] ?? r.name ?? '').toLowerCase().includes(f)) : rows.slice()
  view.sort((a, b) => {
    const av = a[sortKey], bv = b[sortKey]
    const cmp = (typeof av === 'number' && typeof bv === 'number')
      ? av - bv : String(av ?? '').localeCompare(String(bv ?? ''))
    return dir === 'desc' ? -cmp : cmp
  })

  return (
    <div>
      {showFilter && (
        <div className="flex items-center justify-between mb-2">
          <div className="text-[11px] text-slate-500">Click a column to sort · click a row to drill in</div>
          <input className="input !py-1 !text-xs w-44" placeholder={filterPlaceholder}
                 value={filter} onChange={(e) => setFilter(e.target.value)} />
        </div>
      )}
      <div className="overflow-x-auto">
        <table className="w-full text-sm">
          <thead>
            <tr className="text-left text-xs uppercase tracking-wide text-slate-500 border-b border-surface-border">
              {cols.map((c) => (
                <th key={c.key} onClick={() => toggle(c.key)}
                    className={`py-2 pr-4 cursor-pointer select-none hover:text-slate-300 ${c.right ? 'text-right' : ''}`}>
                  {c.label}{sortKey === c.key && <span className="ml-1 text-accent">{dir === 'desc' ? '↓' : '↑'}</span>}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {view.map((r, i) => (
              <tr key={r[nameKey] || r.name || i} onClick={() => onRowClick?.(r)}
                  className={`border-b border-surface-border/50 ${onRowClick ? 'cursor-pointer' : ''} ${
                    selected && (selected[nameKey] || selected.name) === (r[nameKey] || r.name)
                      ? 'bg-accent/10' : 'hover:bg-surface-overlay/40'}`}>
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
    </div>
  )
}

// metrics: [{ label, key, higherBetter=true, format=(v)=>v }]
export function DrillDrawer({ entity, peers, label, metrics, nameKey = 'name', onClose }) {
  if (!entity) return null
  const rank = (key, higherBetter) => {
    const vals = (peers || []).map((p) => p[key]).filter((v) => typeof v === 'number')
    if (!vals.length || typeof entity[key] !== 'number') return null
    const better = vals.filter((v) => (higherBetter ? v > entity[key] : v < entity[key])).length
    return { position: better + 1, of: vals.length, pct: Math.round((1 - better / vals.length) * 100) }
  }
  const shown = (metrics || []).filter((m) => entity[m.key] != null)
  return (
    <div className="fixed inset-0 z-50 flex justify-end bg-black/50" onClick={onClose}>
      <div className="w-full max-w-md h-full bg-surface-raised border-l border-surface-border overflow-y-auto p-6"
           onClick={(e) => e.stopPropagation()}>
        <div className="flex items-start justify-between">
          <div>
            <Badge tone="accent">{label}</Badge>
            <h2 className="text-lg font-bold text-slate-100 mt-2">{entity[nameKey] || entity.name}</h2>
          </div>
          <button onClick={onClose} className="text-slate-500 hover:text-slate-200">✕</button>
        </div>
        <div className="mt-5 space-y-3">
          {shown.map((m) => {
            const r = rank(m.key, m.higherBetter !== false)
            const val = m.format ? m.format(entity[m.key]) : entity[m.key]
            return (
              <div key={m.key} className="card-pad">
                <div className="flex items-center justify-between">
                  <span className="text-xs uppercase tracking-wide text-slate-500">{m.label}</span>
                  {r && <span className="text-[11px] text-slate-500">#{r.position} of {r.of} · P{r.pct}</span>}
                </div>
                <div className="metric mt-1 text-slate-100">{val}</div>
                {r && (
                  <div className="mt-1.5 h-1.5 rounded bg-surface-overlay overflow-hidden">
                    <div className="h-full bg-accent" style={{ width: `${r.pct}%` }} />
                  </div>
                )}
              </div>
            )
          })}
        </div>
      </div>
    </div>
  )
}
