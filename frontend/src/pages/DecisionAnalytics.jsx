// Decision Analytics (V2.5) — how well the enterprise is deciding. Reads the
// V2.4 decision reports and records (/runtime/intelligence/*) and renders
// effectiveness, lifecycle mix, success-by-kind, and the ranked backlog with
// an explainable-AI panel per decision. Charts via ECharts (existing dep);
// all analytics computed backend-side, just visualized here.
import { useMemo, useState } from 'react'
import { api } from '../api/client'
import { useAsync } from '../components/ui'
import EChart, { axisStyle, PALETTE } from '../components/EChart'
import {
  ExplainPanel, ExportMenu, FilterChips, Loader, PremiumHeader, Reveal,
  ScoreGauge, StatCard, Stagger, StaggerItem,
} from '../components/premium'

const PERIODS = [
  { value: 'daily', label: 'Today' },
  { value: 'weekly', label: 'This week' },
  { value: 'monthly', label: 'This month' },
]

export default function DecisionAnalytics() {
  const [period, setPeriod] = useState('weekly')
  const [explain, setExplain] = useState(null)
  const report = useAsync(() => api.intelligenceReport(period).catch(() => null), [period])
  const status = useAsync(() => api.intelligenceStatus().catch(() => null), [])
  const ranked = useAsync(() => api.intelligenceRecommendations(12).then((r) => r.recommendations).catch(() => []), [])

  const weights = status.data?.ranking_weights

  return (
    <div>
      <PremiumHeader title="Decision Analytics" badge="Intelligence"
        subtitle="How the Enterprise Brain is deciding — volume, effectiveness, and what's worth acting on next.">
        <FilterChips options={PERIODS} active={period} onChange={(v) => setPeriod(v || 'weekly')} allLabel="Today" />
        <ExportMenu filename={`decision-report-${period}`} json={report.data} />
      </PremiumHeader>

      <Loader state={report} empty="No decision activity in this window yet.">
        {(r) => {
          const eff = r.effectiveness || {}
          return (
            <div className="space-y-6">
              <Stagger className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
                <StaggerItem><StatCard label="Decisions" value={r.decisions} /></StaggerItem>
                <StaggerItem><StatCard label="Executed" value={r.executed} tone="text-emerald-400" /></StaggerItem>
                <StaggerItem><StatCard label="Execution rate"
                  value={eff.execution_rate != null ? eff.execution_rate * 100 : null}
                  suffix="%" decimals={0} tone="text-accent" /></StaggerItem>
                <StaggerItem><StatCard label="Open now" value={status.data?.open ?? 0} tone="text-amber-400" /></StaggerItem>
              </Stagger>

              <div className="grid gap-5 lg:grid-cols-2">
                <Reveal>
                  <div className="card-pad">
                    <h2 className="text-sm font-semibold text-slate-200 mb-3">Lifecycle mix</h2>
                    {Object.keys(r.by_status || {}).length === 0
                      ? <Empty />
                      : <EChart height={260} option={statusOption(r.by_status)} />}
                  </div>
                </Reveal>
                <Reveal delay={0.06}>
                  <div className="card-pad">
                    <h2 className="text-sm font-semibold text-slate-200 mb-3">Success rate by decision kind</h2>
                    {Object.keys(eff.success_by_kind || {}).length === 0
                      ? <Empty />
                      : <EChart height={260} option={kindOption(eff.success_by_kind)} />}
                  </div>
                </Reveal>
              </div>

              <Reveal>
                <div className="card-pad">
                  <div className="flex items-center justify-between mb-1">
                    <h2 className="text-sm font-semibold text-slate-200">Effectiveness</h2>
                  </div>
                  <div className="grid gap-4 sm:grid-cols-3 mt-3">
                    <Gauge label="Execution rate" value={eff.execution_rate} />
                    <Gauge label="Approved confidence" value={eff.approval_confidence_avg} />
                    <Gauge label="Rejected confidence" value={eff.rejection_confidence_avg} invert />
                  </div>
                  <p className="text-xs text-slate-500 mt-4">
                    The Brain approves higher-confidence decisions and rejects lower-confidence ones —
                    the gap between these two gauges is the platform's judgment, learned from outcomes.
                  </p>
                </div>
              </Reveal>

              <Reveal>
                <div className="card-pad">
                  <div className="flex items-center justify-between mb-3">
                    <h2 className="text-sm font-semibold text-slate-200">Highest-value decisions right now</h2>
                    <span className="text-xs text-slate-500">Click “Why?” to see the reasoning</span>
                  </div>
                  {(ranked.data || []).length === 0
                    ? <Empty text="No open decisions to rank." />
                    : (
                      <div className="space-y-2">
                        {ranked.data.map((d, i) => (
                          <div key={d.decision_id}
                            className="flex items-center gap-3 p-2.5 rounded-lg bg-surface-overlay/30 hover:bg-surface-overlay/60 transition-colors">
                            <span className="text-xs text-slate-600 w-5 tabular-nums">#{i + 1}</span>
                            <ScoreGauge score={d.score} size={40} />
                            <div className="min-w-0 flex-1">
                              <div className="text-sm text-slate-200 truncate">{d.action}</div>
                              <div className="text-xs text-slate-500 capitalize">{d.kind} · P{d.priority} · {Math.round((d.confidence ?? 0) * 100)}%</div>
                            </div>
                            <button onClick={() => setExplain({ ...d, rank: i + 1 })}
                              className="text-xs text-accent hover:underline shrink-0">Why?</button>
                          </div>
                        ))}
                      </div>
                    )}
                </div>
              </Reveal>
            </div>
          )
        }}
      </Loader>

      {explain && <ExplainPanel decision={explain} weights={weights} onClose={() => setExplain(null)} />}
    </div>
  )
}

const Empty = ({ text = 'Nothing to chart yet.' }) => (
  <div className="h-[260px] flex items-center justify-center text-sm text-slate-600">{text}</div>
)

function Gauge({ label, value, invert }) {
  const v = value == null ? null : Number(value)
  return (
    <div className="flex items-center gap-3 bg-surface-overlay/30 rounded-lg p-3">
      <ScoreGauge score={v == null ? 0 : v} size={54} />
      <div>
        <div className="text-sm text-slate-200">{v == null ? '—' : v.toFixed(2)}</div>
        <div className="text-xs text-slate-500">{label}</div>
      </div>
    </div>
  )
}

const STATUS_COLORS = {
  proposed: '#4f8ef7', modified: '#a78bfa', approved: '#34d399',
  executed: '#22c55e', rejected: '#fb7185', expired: '#94a3b8', cancelled: '#64748b',
}

function statusOption(byStatus) {
  return {
    tooltip: { trigger: 'item' },
    legend: { bottom: 0, textStyle: { color: '#94a3b8', fontSize: 11 } },
    series: [{
      type: 'pie', radius: ['48%', '72%'], center: ['50%', '44%'],
      itemStyle: { borderColor: 'rgb(16,19,27)', borderWidth: 2 },
      label: { color: '#cbd5e1', fontSize: 11 },
      data: Object.entries(byStatus).map(([name, value]) => ({
        name, value, itemStyle: { color: STATUS_COLORS[name] || '#64748b' } })),
    }],
  }
}

function kindOption(successByKind) {
  const entries = Object.entries(successByKind).sort((a, b) => b[1] - a[1])
  return {
    grid: { left: 110, right: 24, top: 12, bottom: 24 },
    tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
    xAxis: { type: 'value', max: 1, ...axisStyle },
    yAxis: { type: 'category', data: entries.map((e) => e[0]).reverse(), ...axisStyle,
      axisLabel: { color: '#94a3b8', fontSize: 11 } },
    series: [{
      type: 'bar', barWidth: 14,
      data: entries.map((e) => e[1]).reverse(),
      itemStyle: {
        borderRadius: [0, 4, 4, 0],
        color: (p) => (p.value >= 0.6 ? '#34d399' : p.value >= 0.4 ? '#fbbf24' : '#fb7185'),
      },
      label: { show: true, position: 'right', color: '#94a3b8', fontSize: 10,
        formatter: (p) => p.value.toFixed(2) },
    }],
  }
}
