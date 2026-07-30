// Ecosystem — an interactive enterprise intelligence workspace, not another
// dashboard. Products, banks, PSPs and MCC categories are nodes in a real
// transaction-flow graph (edges are weighted by actual attempts/value); every
// node opens a drawer with its own KPIs, trend, neighbours, ML forecast and a
// grounded "Ask AI" summary. A second tab is the MCC Explorer: category ->
// subcategory -> individual MCC code, each with the same live intelligence.
import { useCallback, useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import ReactFlow, { Background, Controls, MiniMap } from 'reactflow'
import 'reactflow/dist/style.css'
import { api, fmt } from '../api/client'
import { Badge, PanelEmpty, Stat, Tabs, useAsync } from '../components/ui'
import { ExportMenu, FilterChips, Loader, PremiumHeader, SearchInput } from '../components/premium'
import DimensionTable from '../components/DimensionTable'
import EChart from '../components/EChart'
import { MLForecastPanel } from '../components/MLForecast'
import AskAI from '../components/AskAI'

const inr = (v) => `₹${fmt.num(v)}`

const TYPE_HUE = { product: '#38bdf8', bank: '#34d399', psp: '#c084fc', mcc_category: '#fbbf24' }
const tint = (hex, alpha) => {
  const n = parseInt(hex.slice(1), 16)
  return `rgba(${(n >> 16) & 255}, ${(n >> 8) & 255}, ${n & 255}, ${alpha})`
}
const styleFor = (t) => {
  const hue = TYPE_HUE[t] || '#64748b'
  return { br: hue, bg: tint(hue, 0.16) }
}

// Deterministic ring-of-clusters layout, same idea as the Knowledge Graph
// explorer: one ring per node type, nodes spiralled within their ring so the
// same graph always renders the same way (no physics jitter between loads).
function layout(nodes) {
  const byType = {}
  nodes.forEach((n) => { (byType[n.type] || (byType[n.type] = [])).push(n) })
  const types = Object.keys(byType)
  const out = []
  const R = 420
  types.forEach((type, ti) => {
    const a = (2 * Math.PI * ti) / types.length
    const cx = 560 + R * Math.cos(a), cy = 400 + R * Math.sin(a)
    byType[type].forEach((n, i) => {
      const ring = Math.floor(i / 8)
      const per = Math.min(8, byType[type].length - ring * 8)
      const aa = (2 * Math.PI * (i % 8)) / per
      const rr = 55 + ring * 75
      out.push({ ...n, x: cx + rr * Math.cos(aa), y: cy + rr * Math.sin(aa) })
    })
  })
  return out
}

function GraphCanvas({ payload, onSelect, selectedId }) {
  const [type, setType] = useState('')
  const [q, setQ] = useState('')

  const typeCounts = useMemo(() => {
    const m = {}
    payload.nodes.forEach((n) => { m[n.type] = (m[n.type] || 0) + 1 })
    return Object.entries(m).map(([value, count]) => ({ value, label: value.replace('_', ' '), count }))
  }, [payload.nodes])

  const maxAttempts = useMemo(
    () => Math.max(1, ...payload.nodes.map((n) => n.attempts || 0)), [payload.nodes])

  const { nodes, edges } = useMemo(() => {
    const needle = q.trim().toLowerCase()
    const keep = payload.nodes.filter((n) =>
      (!type || n.type === type) &&
      (!needle || `${n.label} ${n.node_id}`.toLowerCase().includes(needle)))
    const ids = new Set(keep.map((n) => n.id))
    const positioned = layout(keep)
    return {
      nodes: positioned.map((n) => {
        const s = styleFor(n.type)
        const isSel = selectedId === n.id
        const scale = 0.6 + 0.5 * Math.sqrt((n.attempts || 0) / maxAttempts)
        return {
          id: n.id, position: { x: n.x, y: n.y }, data: { label: n.label },
          style: {
            background: s.bg, color: 'var(--text-primary)',
            border: `${isSel ? 2 : 1}px solid ${isSel ? 'rgb(var(--accent))' : s.br}`,
            borderRadius: 9, fontSize: Math.round(10 * scale), padding: '6px 10px',
            maxWidth: 190, fontWeight: n.type === 'product' ? 600 : 400,
            boxShadow: isSel ? `0 0 0 3px ${s.br}55` : 'none',
          },
        }
      }),
      edges: payload.edges.filter((e) => ids.has(e.source) && ids.has(e.target)).map((e, i) => ({
        id: `${e.source}->${e.target}-${i}`, source: e.source, target: e.target,
        style: { stroke: '#2a3650', strokeWidth: Math.min(4, 0.5 + (e.weight / maxAttempts) * 8) },
      })),
    }
  }, [payload, type, q, selectedId, maxAttempts])

  const onNodeClick = useCallback((_, node) => {
    const n = payload.nodes.find((x) => x.id === node.id)
    if (n) onSelect(n)
  }, [payload.nodes, onSelect])

  return (
    <div className="card overflow-hidden" style={{ height: '70vh' }}>
      <div className="flex flex-wrap items-center gap-3 p-3 border-b border-surface-border">
        <SearchInput value={q} onChange={setQ} placeholder="Find a bank, PSP, product, MCC…" className="w-64" />
        <div className="text-xs text-slate-500">{nodes.length} nodes · {edges.length} flows</div>
      </div>
      <div className="px-3 py-2 border-b border-surface-border overflow-x-auto">
        <FilterChips options={typeCounts} active={type} onChange={setType} allLabel={`All (${payload.nodes.length})`} />
      </div>
      <div style={{ height: 'calc(70vh - 96px)' }}>
        <ReactFlow nodes={nodes} edges={edges} fitView minZoom={0.1}
                   onNodeClick={onNodeClick} proOptions={{ hideAttribution: true }}>
          <Background color="#1a2333" gap={26} />
          <Controls position="bottom-right" />
          <MiniMap pannable zoomable style={{ background: 'rgb(16,19,27)' }}
                   maskColor="rgba(10,12,18,0.7)"
                   nodeColor={(n) => styleFor(payload.nodes.find((x) => x.id === n.id)?.type).br} />
        </ReactFlow>
      </div>
    </div>
  )
}

const NODE_TABS = [
  { value: 'overview', label: 'Overview' },
  { value: 'neighbours', label: 'Relationships' },
  { value: 'forecast', label: 'Forecast' },
  { value: 'ai', label: 'Ask AI' },
]

function NodeDrawer({ node, onClose }) {
  const [tab, setTab] = useState('overview')
  const state = useAsync(() => api.intelNode(node.type, node.node_id), [node.type, node.node_id])
  const s = styleFor(node.type)

  const dailyOption = useMemo(() => {
    if (!state.data?.daily) return null
    return {
      tooltip: { trigger: 'axis' },
      grid: { left: 50, right: 16, top: 16, bottom: 30 },
      xAxis: { type: 'category', data: state.data.daily.map((d) => d.date),
               axisLabel: { rotate: 45, fontSize: 9, interval: Math.floor(state.data.daily.length / 16) } },
      yAxis: { type: 'value', axisLabel: { fontSize: 10 } },
      series: [{ type: 'line', data: state.data.daily.map((d) => d.attempts), symbol: 'none',
                 smooth: 0.15, areaStyle: { opacity: 0.08 } }],
    }
  }, [state.data])

  return (
    <div className="card-pad h-fit lg:max-h-[70vh] overflow-y-auto space-y-3">
      <div className="flex items-start justify-between gap-2">
        <div className="min-w-0">
          <span className="px-2 py-0.5 rounded-md text-[10px] font-semibold capitalize"
                style={{ background: `${s.br}22`, color: s.br }}>{node.type.replace('_', ' ')}</span>
          <h3 className="text-sm font-semibold text-slate-100 mt-1.5 break-words">{node.label}</h3>
          <div className="text-xs text-slate-500 mt-0.5">
            {fmt.num(node.attempts)} attempts · {node.success_rate}% success · {node.share_pct}% share
          </div>
        </div>
        <button onClick={onClose} className="text-slate-500 hover:text-slate-200 text-lg leading-none">×</button>
      </div>

      {node.type === 'product' && (
        <Link to={`/products/${encodeURIComponent(node.node_id)}`} className="btn w-full text-center block">
          Open full product dashboard →
        </Link>
      )}

      <Tabs tabs={NODE_TABS} active={tab} onChange={setTab} />

      <Loader state={state} skeleton={<div className="h-40" />} empty="No intelligence available for this node.">
        {(d) => {
          if (tab === 'overview') {
            return (
              <div className="space-y-3">
                <div className="grid grid-cols-2 gap-2">
                  {(d.kpis || []).slice(0, 6).map((k) => (
                    <Stat key={k.key} label={k.label}
                          value={k.unit === '₹' ? inr(k.value) : k.unit === '%' ? `${k.value}%` : fmt.num(k.value)} />
                  ))}
                </div>
                {dailyOption && <EChart option={dailyOption} height={200} />}
              </div>
            )
          }
          if (tab === 'neighbours') {
            const groups = Object.entries(d.neighbours || {})
            if (groups.length === 0) return <PanelEmpty text="No relationships recorded." />
            return (
              <div className="space-y-3">
                {groups.map(([dim, rows]) => (
                  <DimensionTable key={dim} title={dim.replace('_', ' ')} rows={rows}
                                  nameLabel={dim.replace('_', ' ')} />
                ))}
                {(d.top_mccs || []).length > 0 && (
                  <DimensionTable title="Top MCCs" rows={d.top_mccs} nameLabel="MCC" />
                )}
              </div>
            )
          }
          if (tab === 'forecast') {
            return <MLForecastPanel d={d.forecast} compact />
          }
          return (
            <AskAI title=""
                   question={`Explain ${node.label}'s performance, what is driving it, and any risks or recommendations, using the real transaction data.`} />
          )
        }}
      </Loader>
    </div>
  )
}

function GraphWorkspace() {
  const state = useAsync(() => api.intelGraph(), [])
  const [selected, setSelected] = useState(null)

  return (
    <Loader state={state} skeleton={<div className="card" style={{ height: '70vh' }} />}
            empty="No transactions ingested yet — the ecosystem graph holds no data.">
      {(payload) => (
        <div className="grid gap-4 lg:grid-cols-[1fr_340px]">
          <GraphCanvas payload={payload} selectedId={selected?.id} onSelect={setSelected} />
          {selected ? (
            <NodeDrawer node={selected} onClose={() => setSelected(null)} />
          ) : (
            <div className="card-pad text-sm text-slate-500 h-fit">
              <div className="eyebrow mb-2">Inspector</div>
              Click any bank, PSP, product or MCC category to open its full intelligence —
              KPIs, trend, relationships, forecast, and a grounded AI summary.
            </div>
          )}
        </div>
      )}
    </Loader>
  )
}

// ------------------------------------------------------------- MCC Explorer
function CategoryCard({ c, active, onClick }) {
  return (
    <button onClick={onClick}
            className={`card-pad text-left transition-colors ${active ? 'ring-2 ring-accent' : 'card-hover'}`}>
      <div className="font-medium text-slate-100">{c.name}</div>
      <div className="mt-2 grid grid-cols-2 gap-2 text-xs">
        <div><div className="text-slate-500">Attempts</div><div className="text-slate-200 tabular-nums">{fmt.num(c.attempts)}</div></div>
        <div><div className="text-slate-500">Share</div><div className="text-slate-200 tabular-nums">{c.share_pct}%</div></div>
        <div><div className="text-slate-500">Success</div><div className="text-slate-200 tabular-nums">{c.success_rate}%</div></div>
        <div><div className="text-slate-500">Value</div><div className="text-slate-200 tabular-nums">{inr(c.value_inr)}</div></div>
      </div>
    </button>
  )
}

function McCodeDetail({ code, onClose }) {
  const state = useAsync(() => api.intelMccDetail(code), [code])
  return (
    <Loader state={state} skeleton={<div className="h-40" />} empty="No data for this MCC code.">
      {(d) => (
        <div className="space-y-4">
          <div className="flex items-start justify-between gap-2">
            <div>
              <div className="text-xs text-slate-500 font-mono">{d.mcc}</div>
              <h3 className="text-lg font-semibold text-slate-100">{d.reference?.mcc_name}</h3>
              <div className="text-xs text-slate-500 mt-0.5">
                {d.reference?.category} · {d.reference?.subcategory} · {d.reference?.seasonality} seasonality ·
                {' '}risk index {d.reference?.risk_index}
              </div>
            </div>
            <button onClick={onClose} className="text-slate-500 hover:text-slate-200 text-lg leading-none">×</button>
          </div>
          <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
            {(d.kpis || []).slice(0, 8).map((k) => (
              <Stat key={k.key} label={k.label}
                    value={k.unit === '₹' ? inr(k.value) : k.unit === '%' ? `${k.value}%` : fmt.num(k.value)} />
            ))}
          </div>
          <div className="grid lg:grid-cols-2 gap-4">
            <DimensionTable title="Products" rows={d.products} nameLabel="Product" />
            <DimensionTable title="Banks" rows={d.banks} nameLabel="Bank" />
          </div>
          <div className="grid lg:grid-cols-2 gap-4">
            <DimensionTable title="PSPs" rows={d.psps} nameLabel="PSP" />
            <DimensionTable title="Top merchants" rows={d.merchants} nameLabel="Merchant" />
          </div>
          {(d.adjustments?.by_type || []).length > 0 && (
            <div className="card-pad">
              <div className="h-sub mb-2">Refunds, reversals & chargebacks</div>
              <div className="flex flex-wrap gap-2">
                {d.adjustments.by_type.map((a) => (
                  <Badge key={a.type} tone="default">{a.type}: {a.n} ({inr(a.value_inr)})</Badge>
                ))}
              </div>
            </div>
          )}
          <div>
            <div className="h-sub mb-2">Forecast</div>
            <MLForecastPanel d={d.forecast} compact />
          </div>
          <AskAI title="AI summary"
                 question={`Summarize the ${d.reference?.mcc_name} MCC's performance, risks, and growth using the real transaction data.`} />
        </div>
      )}
    </Loader>
  )
}

function MccExplorer() {
  const state = useAsync(() => api.intelMcc(), [])
  const [category, setCategory] = useState('')
  const [q, setQ] = useState('')
  const [code, setCode] = useState(null)

  return (
    <Loader state={state} skeleton={<div className="h-96" />} empty="No MCC data — the warehouse holds no data.">
      {(d) => {
        const catalog = (d.catalog || []).filter((c) =>
          (!category || c.category === category) &&
          (!q || `${c.mcc} ${c.mcc_name} ${c.subcategory}`.toLowerCase().includes(q.toLowerCase())))
        return (
          <div className="space-y-5">
            <div>
              <div className="h-sub mb-2">Categories</div>
              <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-5">
                {(d.categories || []).map((c) => (
                  <CategoryCard key={c.name} c={c} active={category === c.name}
                                onClick={() => setCategory(category === c.name ? '' : c.name)} />
                ))}
              </div>
            </div>

            <div className="card-pad">
              <div className="flex items-center justify-between gap-3 mb-3">
                <div className="h-sub">Merchant Category Codes ({catalog.length})</div>
                <SearchInput value={q} onChange={setQ} placeholder="Find an MCC…" className="w-56" />
              </div>
              <div className="overflow-x-auto">
                <table className="table-base">
                  <thead>
                    <tr><th>MCC</th><th>Name</th><th>Category</th><th>Subcategory</th><th>Risk</th><th>Seasonality</th></tr>
                  </thead>
                  <tbody>
                    {catalog.map((c) => (
                      <tr key={c.mcc} className="cursor-pointer hover:bg-surface-overlay/40"
                          onClick={() => setCode(c.mcc)}>
                        <td className="text-xs font-mono">{c.mcc}</td>
                        <td className="text-xs">{c.mcc_name}</td>
                        <td className="text-xs">{c.category}</td>
                        <td className="text-xs">{c.subcategory}</td>
                        <td className="text-xs tabular-nums">{c.risk_index}</td>
                        <td className="text-xs">{c.seasonality}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>

            {code && <McCodeDetail code={code} onClose={() => setCode(null)} />}
          </div>
        )
      }}
    </Loader>
  )
}

const VIEWS = [{ value: 'graph', label: 'Graph Workspace' }, { value: 'mcc', label: 'MCC Explorer' }]

export default function EcosystemDashboard() {
  const [view, setView] = useState('graph')
  return (
    <div>
      <PremiumHeader title="Ecosystem" badge="Interactive"
                     subtitle="Banks, PSPs, products and merchant categories as a real transaction-flow graph — explore relationships, open any node's full intelligence, and ask AI, grounded in the raw corpus.">
        <ExportMenu filename="ecosystem" />
      </PremiumHeader>
      <div className="mb-4"><Tabs tabs={VIEWS} active={view} onChange={setView} /></div>
      {view === 'graph' ? <GraphWorkspace /> : <MccExplorer />}
    </div>
  )
}
