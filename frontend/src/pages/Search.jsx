// Enterprise Search (V9.0) — one search bar across banks, PSPs, merchants,
// products, features, KPIs, reports, decisions, files and the Knowledge Graph.
import { useEffect, useState } from 'react'
import { useNavigate, useSearchParams } from 'react-router-dom'
import { api } from '../api/client'
import { Badge, PageHeader, Spinner } from '../components/ui'

const TYPE_TONE = {
  bank: 'info', psp: 'accent', merchant: 'success', product: 'success',
  feature: 'warn', kpi: 'warn', report: 'default', decision: 'accent',
  file: 'info',
}

export default function Search() {
  const nav = useNavigate()
  const [params, setParams] = useSearchParams()
  const [q, setQ] = useState(params.get('q') || '')
  const [res, setRes] = useState(null)
  const [busy, setBusy] = useState(false)

  const run = async (query) => {
    const term = (query ?? q).trim()
    if (!term) return
    setBusy(true); setParams({ q: term })
    try { setRes(await api.workspaceSearch(term)) }
    catch { setRes({ results: [], groups: {} }) } finally { setBusy(false) }
  }

  useEffect(() => { if (params.get('q')) run(params.get('q')) }, []) // eslint-disable-line

  const groups = res?.groups || {}

  return (
    <>
      <PageHeader title="Enterprise Search"
        subtitle="Search everything — entities, KPIs, reports, decisions, files and the Knowledge Graph" />
      <form onSubmit={(e) => { e.preventDefault(); run() }} className="flex gap-2 max-w-2xl mb-5">
        <input autoFocus value={q} onChange={(e) => setQ(e.target.value)}
          placeholder="Search banks, PSPs, merchants, products, KPIs, reports, files…"
          className="input flex-1 !py-2.5" />
        <button className="btn !px-6" type="submit" disabled={!q.trim()}>Search</button>
      </form>

      {busy && <Spinner label="Searching the enterprise…" />}
      {!busy && res && (
        res.total === 0 ? (
          <p className="text-sm text-slate-500">No results for “{res.query}”.</p>
        ) : (
          <div className="space-y-5">
            <div className="text-xs text-slate-500">{res.total} results across {Object.keys(groups).length} categories</div>
            {Object.entries(groups).map(([type, items]) => (
              <div key={type}>
                <h3 className="text-xs uppercase tracking-wide text-slate-500 mb-2">{type} ({items.length})</h3>
                <div className="grid gap-2 sm:grid-cols-2">
                  {items.map((r, i) => (
                    <button key={i} onClick={() => r.link && nav(r.link)}
                      className="card-pad text-left card-hover flex items-start gap-3">
                      <Badge tone={TYPE_TONE[type] || 'default'}>{type}</Badge>
                      <span className="min-w-0">
                        <span className="block text-sm text-slate-200 truncate">{r.title}</span>
                        {r.snippet && <span className="block text-xs text-slate-500 truncate">{r.snippet}</span>}
                      </span>
                    </button>
                  ))}
                </div>
              </div>
            ))}
          </div>
        )
      )}
    </>
  )
}
