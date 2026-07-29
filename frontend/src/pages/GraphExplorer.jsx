// Interactive Knowledge Graph Explorer (V2.5) — the whole organizational
// brain as a navigable graph. Reads the org-wide node-link payload from
// /knowledge/graph, lets you filter by node kind, search to focus a node,
// and click any node to inspect its relationships (via /knowledge/graph/node).
// Reuses reactflow (already a dependency) — no backend logic here.
import { useCallback, useMemo, useState } from 'react'
import ReactFlow, { Background, Controls, MiniMap } from 'reactflow'
import 'reactflow/dist/style.css'
import { api } from '../api/client'
import { useAsync } from '../components/ui'
import {
  ExportMenu, FilterChips, Loader, PremiumHeader, SearchInput,
} from '../components/premium'

// A colour language per node kind. Only the hue is fixed — it is what carries
// the meaning. The fill is that hue at low alpha and the label uses the
// theme's ink, so the same node reads correctly on both a dark and a light
// canvas instead of being a dark chip stranded on white.
const KIND_HUE = {
  decision: '#c084fc', product: '#38bdf8', concept: '#34d399',
  kpi: '#fbbf24', signal: '#fb7185', rca: '#fb923c',
  sop: '#60a5fa', policy: '#94a3b8', meeting: '#2dd4bf',
  document: '#6b7280', report: '#4f8ef7', project: '#a78bfa',
  insight: '#10b981', recommendation: '#eab308', dataset: '#60a5fa',
  default: '#64748b',
}

const tint = (hex, alpha) => {
  const n = parseInt(hex.slice(1), 16)
  return `rgba(${(n >> 16) & 255}, ${(n >> 8) & 255}, ${n & 255}, ${alpha})`
}

const styleFor = (k) => {
  const hue = KIND_HUE[k] || KIND_HUE.default
  return { br: hue, bg: tint(hue, 0.16), fg: 'var(--text-primary)' }
}

// Deterministic force-free layout: cluster by kind into a ring of clusters,
// then spiral each cluster's nodes. Stable across renders, no physics cost.
function layout(nodes) {
  const byKind = {}
  nodes.forEach((n) => { (byKind[n.kind] || (byKind[n.kind] = [])).push(n) })
  const kinds = Object.keys(byKind)
  const out = []
  const R = 520
  kinds.forEach((kind, ki) => {
    const a = (2 * Math.PI * ki) / kinds.length
    const cx = 640 + R * Math.cos(a), cy = 480 + R * Math.sin(a)
    byKind[kind].forEach((n, i) => {
      const ring = Math.floor(i / 8)
      const per = Math.min(8, byKind[kind].length - ring * 8)
      const aa = (2 * Math.PI * (i % 8)) / per
      const rr = 60 + ring * 78
      out.push({ ...n, x: cx + rr * Math.cos(aa), y: cy + rr * Math.sin(aa) })
    })
  })
  return out
}

export default function GraphExplorer() {
  const state = useAsync(() => api.enterpriseGraph(800), [])
  return (
    <div>
      <PremiumHeader title="Knowledge Graph Explorer" badge="Interactive"
        subtitle="The whole organization as a living graph — entities, documents, decisions, and how they connect.">
        <ExportMenu filename="knowledge-graph" json={state.data} />
      </PremiumHeader>
      <Loader state={state} skeleton={<div className="card" style={{ height: '74vh' }} />}
        empty="The knowledge graph is still forming — ingest data to grow it.">
        {(g) => <Explorer payload={g} />}
      </Loader>
    </div>
  )
}

function Explorer({ payload }) {
  const [kind, setKind] = useState('')
  const [q, setQ] = useState('')
  const [selected, setSelected] = useState(null)

  const kindCounts = useMemo(() => {
    const m = {}
    payload.nodes.forEach((n) => { m[n.kind] = (m[n.kind] || 0) + 1 })
    return Object.entries(m).sort((a, b) => b[1] - a[1])
      .map(([value, count]) => ({ value, label: value, count }))
  }, [payload.nodes])

  const { nodes, edges } = useMemo(() => {
    const needle = q.trim().toLowerCase()
    const keep = payload.nodes.filter((n) =>
      (!kind || n.kind === kind) &&
      (!needle || `${n.id} ${n.label || ''}`.toLowerCase().includes(needle)))
    const ids = new Set(keep.map((n) => n.id))
    const positioned = layout(keep)
    return {
      nodes: positioned.map((n) => {
        const s = styleFor(n.kind)
        const isSel = selected?.id === n.id
        return {
          id: n.id, position: { x: n.x, y: n.y }, data: { label: n.label || n.id },
          style: {
            background: s.bg, color: s.fg,
            border: `${isSel ? 2 : 1}px solid ${isSel ? 'rgb(var(--accent))' : s.br}`,
            borderRadius: 9, fontSize: 11, padding: '6px 9px', maxWidth: 180,
            boxShadow: isSel ? `0 0 0 3px ${s.br}55` : 'none',
          },
        }
      }),
      edges: payload.edges.filter((e) => ids.has(e.source) && ids.has(e.target)).map((e) => ({
        id: e.id, source: e.source, target: e.target, label: e.kind,
        animated: ['affects', 'implements', 'creates'].includes(e.kind),
        style: { stroke: '#2a3650' }, labelStyle: { fill: '#64748b', fontSize: 8 },
        labelBgStyle: { fill: 'rgb(16,19,27)' },
      })),
    }
  }, [payload, kind, q, selected])

  const onNodeClick = useCallback((_, node) => {
    api.enterpriseGraphNode(node.id).then((r) => setSelected({ id: node.id, ...r })).catch(() => {})
  }, [])

  return (
    <div className="grid gap-4 lg:grid-cols-[1fr_320px]">
      <div className="card overflow-hidden" style={{ height: '74vh' }}>
        <div className="flex flex-wrap items-center gap-3 p-3 border-b border-surface-border">
          <SearchInput value={q} onChange={setQ} placeholder="Find a node…" className="w-56" />
          <div className="text-xs text-slate-500">
            {nodes.length} nodes · {edges.length} edges
          </div>
        </div>
        <div className="px-3 py-2 border-b border-surface-border overflow-x-auto">
          <FilterChips options={kindCounts} active={kind} onChange={setKind} allLabel={`All (${payload.nodes.length})`} />
        </div>
        <div style={{ height: 'calc(74vh - 96px)' }}>
          <ReactFlow nodes={nodes} edges={edges} fitView minZoom={0.1}
            onNodeClick={onNodeClick} proOptions={{ hideAttribution: true }}>
            <Background color="#1a2333" gap={26} />
            <Controls position="bottom-right" />
            <MiniMap pannable zoomable style={{ background: 'rgb(16,19,27)' }}
              maskColor="rgba(10,12,18,0.7)"
              nodeColor={(n) => styleFor(payload.nodes.find((x) => x.id === n.id)?.kind).br} />
          </ReactFlow>
        </div>
      </div>

      <NodeInspector node={selected} onClose={() => setSelected(null)} onPick={(id) =>
        api.enterpriseGraphNode(id).then((r) => setSelected({ id, ...r })).catch(() => {})} />
    </div>
  )
}

function NodeInspector({ node, onClose, onPick }) {
  if (!node?.node) {
    return (
      <div className="card-pad text-sm text-slate-500 h-fit">
        <div className="eyebrow mb-2">Inspector</div>
        Click any node to explore its relationships across the enterprise.
      </div>
    )
  }
  const s = styleFor(node.node.kind)
  return (
    <div className="card-pad h-fit lg:max-h-[74vh] overflow-y-auto">
      <div className="flex items-start justify-between gap-2 mb-3">
        <div className="min-w-0">
          <span className="px-2 py-0.5 rounded-md text-[10px] font-semibold capitalize"
            style={{ background: `${s.br}22`, color: s.br }}>{node.node.kind}</span>
          <h3 className="text-sm font-semibold text-slate-100 mt-1.5 break-words">{node.node.label || node.id}</h3>
        </div>
        <button onClick={onClose} className="text-slate-500 hover:text-slate-200 text-lg leading-none">×</button>
      </div>
      {node.node.projects?.length > 0 && (
        <div className="mb-3 text-xs text-slate-500">
          Seen in {node.node.projects.length} project(s)
        </div>
      )}
      <div className="eyebrow mb-2">Relationships ({node.relations?.length || 0})</div>
      {(node.relations || []).length === 0
        ? <div className="text-sm text-slate-500">No connections recorded.</div>
        : (
          <ul className="space-y-1.5">
            {node.relations.map((rel, i) => (
              <li key={i}>
                <button onClick={() => onPick(rel.node.id)}
                  className="w-full text-left p-2 rounded-lg hover:bg-surface-overlay/60 transition-colors group">
                  <div className="flex items-center gap-2 text-xs">
                    <span className="text-slate-500">{rel.direction === 'out' ? '→' : '←'}</span>
                    <span className="px-1.5 py-0.5 rounded bg-surface-overlay text-slate-400 capitalize">{rel.kind}</span>
                  </div>
                  <div className="text-sm text-slate-300 group-hover:text-slate-100 mt-1 truncate">
                    {rel.node.label || rel.node.id}
                  </div>
                </button>
              </li>
            ))}
          </ul>
        )}
    </div>
  )
}
