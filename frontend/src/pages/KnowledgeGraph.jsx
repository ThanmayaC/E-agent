import { useMemo, useState } from 'react'
import { useParams } from 'react-router-dom'
import ReactFlow, { Background, Controls, MiniMap } from 'reactflow'
import 'reactflow/dist/style.css'
import { api } from '../api/client'
import { AsyncSection, Badge, PageHeader, useAsync } from '../components/ui'

// The hue carries the node's kind; the fill is that hue at low alpha and the
// label uses the theme's ink, so nodes read correctly on a light canvas too.
const KIND_HUE = {
  dataset: '#4f8ef7', concept: '#34d399', kpi: '#fbbf24',
  signal: '#f87171', column: '#64748b',
}

const tint = (hex, alpha) => {
  const n = parseInt(hex.slice(1), 16)
  return `rgba(${(n >> 16) & 255}, ${(n >> 8) & 255}, ${n & 255}, ${alpha})`
}

const KIND_STYLE = Object.fromEntries(
  Object.entries(KIND_HUE).map(([kind, hue]) => [kind, {
    background: tint(hue, 0.16),
    border: `1px solid ${hue}`,
    color: 'var(--text-primary)',
  }]))

function layout(nodes) {
  // simple concentric layout by kind ring
  const rings = { dataset: 0, concept: 1, kpi: 2, signal: 3, column: 4 }
  const byRing = {}
  nodes.forEach((n) => { (byRing[rings[n.kind] ?? 4] ||= []).push(n) })
  const out = []
  Object.entries(byRing).forEach(([ring, ns]) => {
    const radius = 160 + Number(ring) * 190
    ns.forEach((n, i) => {
      const angle = (2 * Math.PI * i) / ns.length
      out.push({ ...n, x: 600 + radius * Math.cos(angle), y: 450 + radius * Math.sin(angle) })
    })
  })
  return out
}

export default function KnowledgeGraph() {
  const { projectId } = useParams()
  const state = useAsync(() => api.graph(projectId), [projectId])
  const [showColumns, setShowColumns] = useState(false)

  return (
    <>
      <PageHeader title="Knowledge Graph" subtitle="Entities, concepts, KPIs and statistical signals — connected automatically">
        <button className="btn-ghost" onClick={() => setShowColumns((v) => !v)}>
          {showColumns ? 'Hide columns' : 'Show columns'}
        </button>
      </PageHeader>
      <AsyncSection state={state}>
        {(g) => <GraphCanvas payload={g} showColumns={showColumns} />}
      </AsyncSection>
    </>
  )
}

function GraphCanvas({ payload, showColumns }) {
  const { nodes, edges } = useMemo(() => {
    const keep = payload.nodes.filter((n) => showColumns || n.kind !== 'column')
    const ids = new Set(keep.map((n) => n.id))
    const positioned = layout(keep)
    return {
      nodes: positioned.map((n) => ({
        id: n.id,
        position: { x: n.x, y: n.y },
        data: { label: n.label },
        style: { ...KIND_STYLE[n.kind], borderRadius: 10, fontSize: 11, padding: 6, maxWidth: 170 },
      })),
      edges: payload.edges
        .filter((e) => ids.has(e.source) && ids.has(e.target))
        .map((e) => ({
          id: e.id, source: e.source, target: e.target,
          label: e.kind === 'joins' ? e.label : undefined,
          animated: e.kind === 'joins',
          style: { stroke: '#334155' },
          labelStyle: { fill: '#64748b', fontSize: 9 },
          labelBgStyle: { fill: '#0b0f17' },
        })),
    }
  }, [payload, showColumns])

  return (
    <div className="card" style={{ height: '72vh' }}>
      <div className="flex gap-3 p-3 border-b border-surface-border text-xs">
        <Badge tone="accent">datasets {payload.stats.datasets}</Badge>
        <Badge tone="success">concepts {payload.stats.concepts}</Badge>
        <Badge>nodes {payload.stats.node_count}</Badge>
        <Badge>edges {payload.stats.edge_count}</Badge>
      </div>
      <ReactFlow nodes={nodes} edges={edges} fitView proOptions={{ hideAttribution: true }}>
        <Background color="#1a2333" gap={24} />
        <Controls position="bottom-right" />
        <MiniMap pannable zoomable style={{ background: '#111827' }} maskColor="rgba(11,15,23,0.7)" />
      </ReactFlow>
    </div>
  )
}
