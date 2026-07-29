// Knowledge Growth (V2.5) — how the Enterprise Brain is getting smarter over
// time. Reads /brain/statistics and /learning/history to show the shape of
// what the organization knows, the composition of its knowledge graph, and a
// cumulative curve of everything it has learned. All figures come from the
// Brain's own statistics — visualized here, computed there.
import { useMemo } from 'react'
import { api } from '../api/client'
import { useAsync } from '../components/ui'
import { timeAgo } from '../components/ui'
import EChart, { axisStyle, PALETTE } from '../components/EChart'
import {
  ExportMenu, Loader, PremiumHeader, Reveal, Sparkline, StatCard,
  Stagger, StaggerItem,
} from '../components/premium'

export default function KnowledgeGrowth() {
  const stats = useAsync(() => api.brainStatistics().catch(() => null), [])
  const history = useAsync(() => api.learningHistory(200).catch(() => []), [])

  return (
    <div>
      <PremiumHeader title="Knowledge Growth" badge="Enterprise Brain"
        subtitle="How the organization's intelligence compounds — what it knows, how it connects, and what it keeps learning.">
        <ExportMenu filename="knowledge-growth" json={{ statistics: stats.data, learning: history.data }} />
      </PremiumHeader>

      <Loader state={stats} empty="The Brain has not learned anything yet.">
        {(s) => {
          const k = s.knowledge || {}
          const g = s.graph || {}
          const learnSeries = cumulative(history.data || [])
          return (
            <div className="space-y-6">
              <Stagger className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
                <StaggerItem><StatCard label="Things learned" value={s.learning?.events ?? 0}
                  tone="fg-success" spark={<Sparkline data={learnSeries.map((p) => p.v)} width={150} stroke="#34d399" />} /></StaggerItem>
                <StaggerItem><StatCard label="Graph nodes" value={g.node_count ?? 0} /></StaggerItem>
                <StaggerItem><StatCard label="Graph connections" value={g.edge_count ?? 0} /></StaggerItem>
                <StaggerItem><StatCard label="Decisions remembered" value={k.decisions ?? 0} tone="text-accent" /></StaggerItem>
              </Stagger>

              <div className="grid gap-5 lg:grid-cols-3">
                <Reveal className="lg:col-span-2">
                  <div className="card-pad">
                    <h2 className="text-sm font-semibold text-slate-200 mb-3">Cumulative learning</h2>
                    {learnSeries.length < 2
                      ? <ChartEmpty text="Not enough history yet." />
                      : <EChart height={280} option={growthOption(learnSeries)} />}
                  </div>
                </Reveal>
                <Reveal delay={0.06}>
                  <div className="card-pad">
                    <h2 className="text-sm font-semibold text-slate-200 mb-3">Knowledge graph composition</h2>
                    {Object.keys(g.node_kinds || {}).length === 0
                      ? <ChartEmpty text="No nodes yet." />
                      : <EChart height={280} option={kindsOption(g.node_kinds)} />}
                  </div>
                </Reveal>
              </div>

              <div className="grid gap-5 lg:grid-cols-2">
                <Reveal>
                  <div className="card-pad">
                    <h2 className="text-sm font-semibold text-slate-200 mb-3">What the Brain holds</h2>
                    <div className="grid grid-cols-2 gap-3">
                      {KNOWLEDGE_ROWS.map(([key, label]) => (
                        <div key={key} className="flex items-center justify-between bg-surface-overlay/30 rounded-lg px-3 py-2">
                          <span className="text-sm text-slate-400">{label}</span>
                          <span className="text-sm font-semibold text-slate-100 tabular-nums">{k[key] ?? 0}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                </Reveal>

                <Reveal delay={0.06}>
                  <div className="card-pad">
                    <h2 className="text-sm font-semibold text-slate-200 mb-3">Latest things learned</h2>
                    <Loader state={history} skeleton={<div className="h-40 rounded bg-surface-overlay/40 animate-pulse" />}
                      empty="No learning events yet.">
                      {(h) => (
                        <ol className="space-y-2 max-h-64 overflow-y-auto">
                          {[...h].reverse().slice(0, 14).map((e, i) => (
                            <li key={i} className="flex items-start gap-2.5 text-sm">
                              <span className="mt-1.5 w-1.5 h-1.5 rounded-full bg-emerald-400 shrink-0" />
                              <div className="min-w-0 flex-1">
                                <span className="text-slate-300 capitalize">{(e.event || '').replace(/_/g, ' ')}</span>
                                <span className="text-xs text-slate-500"> · {e.source}</span>
                                <div className="text-[11px] text-slate-600">{timeAgo(e.recorded_at)}</div>
                              </div>
                            </li>
                          ))}
                        </ol>
                      )}
                    </Loader>
                  </div>
                </Reveal>
              </div>
            </div>
          )
        }}
      </Loader>
    </div>
  )
}

const KNOWLEDGE_ROWS = [
  ['terminology', 'Terminology'], ['entity_definitions', 'Entities'],
  ['business_rules', 'Business rules'], ['clarifications', 'Clarifications'],
  ['report_history', 'Reports'], ['insights', 'Insights'],
  ['recommendations', 'Recommendations'], ['strategic_insights', 'Strategic insights'],
]

const ChartEmpty = ({ text }) => (
  <div className="h-[280px] flex items-center justify-center text-sm text-slate-600">{text}</div>
)

// Build a cumulative count of learning events over time from the history.
function cumulative(history) {
  const sorted = [...history]
    .filter((e) => e.recorded_at)
    .sort((a, b) => new Date(a.recorded_at) - new Date(b.recorded_at))
  return sorted.map((e, i) => ({ t: e.recorded_at, v: i + 1 }))
}

function growthOption(series) {
  return {
    grid: { left: 40, right: 20, top: 20, bottom: 32 },
    tooltip: { trigger: 'axis' },
    xAxis: {
      type: 'category', boundaryGap: false,
      data: series.map((p) => new Date(p.t).toLocaleDateString(undefined, { month: 'short', day: 'numeric' })),
      ...axisStyle, axisLabel: { color: '#64748b', fontSize: 10, showMaxLabel: true },
    },
    yAxis: { type: 'value', ...axisStyle },
    series: [{
      type: 'line', smooth: true, symbol: 'none', data: series.map((p) => p.v),
      lineStyle: { width: 2.5, color: '#34d399' },
      areaStyle: { color: { type: 'linear', x: 0, y: 0, x2: 0, y2: 1,
        colorStops: [{ offset: 0, color: 'rgba(52,211,153,0.3)' }, { offset: 1, color: 'rgba(52,211,153,0)' }] } },
    }],
  }
}

function kindsOption(nodeKinds) {
  const entries = Object.entries(nodeKinds).sort((a, b) => b[1] - a[1])
  return {
    tooltip: { trigger: 'item' },
    series: [{
      type: 'pie', radius: ['40%', '70%'], center: ['50%', '50%'],
      itemStyle: { borderColor: 'rgb(16,19,27)', borderWidth: 2 },
      label: { color: '#94a3b8', fontSize: 10, formatter: '{b}' },
      data: entries.map(([name, value], i) => ({ name, value,
        itemStyle: { color: PALETTE[i % PALETTE.length] } })),
    }],
  }
}
