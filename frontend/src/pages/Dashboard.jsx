import { useParams, Link } from 'react-router-dom'
import { api, fmt } from '../api/client'
import { AsyncSection, Badge, PageHeader, useAsync } from '../components/ui'
import EChart, { axisStyle, PALETTE, useChartTheme } from '../components/EChart'

function HealthRing({ score }) {
  const theme = useChartTheme()
  const tone = score >= 70 ? theme.palette[1]
    : score >= 45 ? theme.palette[2] : theme.palette[3]
  return (
    <EChart height={170} option={{
      series: [{
        type: 'gauge', startAngle: 220, endAngle: -40, min: 0, max: 100,
        progress: { show: true, width: 12, itemStyle: { color: tone } },
        axisLine: { lineStyle: { width: 12, color: [[1, theme.grid]] } },
        axisTick: { show: false }, splitLine: { show: false }, axisLabel: { show: false },
        pointer: { show: false }, anchor: { show: false },
        detail: { valueAnimation: false, fontSize: 30, color: theme.textStrong,
                  offsetCenter: [0, 0], formatter: '{value}' },
        data: [{ value: score }],
      }],
    }} />
  )
}

function KpiTile({ k }) {
  const tone = k.trend === 'up' ? 'text-emerald-400' : k.trend === 'down' ? 'text-rose-400' : 'text-slate-500'
  return (
    <div className="card-pad">
      <div className="h-sub truncate" title={k.name}>{k.name}</div>
      <div className="flex items-baseline gap-2 mt-2">
        <span className="text-2xl font-bold text-slate-100">{fmt.num(k.current_value)}</span>
        {k.unit === '%' && <span className="text-slate-500 text-sm">%</span>}
      </div>
      <div className={`text-xs mt-1 ${tone}`}>
        {k.growth_pct != null ? `${fmt.pct(k.growth_pct)} vs prev` : 'no prior period'}
      </div>
      {k.sparkline?.length > 1 && (
        <EChart height={54} option={{
          grid: { left: 0, right: 0, top: 4, bottom: 0 },
          xAxis: { type: 'category', show: false, data: k.sparkline_labels },
          yAxis: { type: 'value', show: false, min: 'dataMin' },
          series: [{ type: 'line', data: k.sparkline, showSymbol: false, smooth: true,
                     lineStyle: { width: 2, color: k.trend === 'down' ? '#f87171' : '#4f8ef7' },
                     areaStyle: { opacity: 0.12, color: k.trend === 'down' ? '#f87171' : '#4f8ef7' } }],
          tooltip: { trigger: 'axis' },
        }} />
      )}
    </div>
  )
}

export default function Dashboard() {
  const { projectId } = useParams()
  const report = useAsync(() => api.report(projectId), [projectId])
  const kpis = useAsync(() => api.kpis(projectId), [projectId])

  return (
    <>
      <PageHeader title="Executive Dashboard" subtitle="Auto-generated from your uploaded workbooks" />
      <AsyncSection state={report} empty="Analysis not finished yet — check back shortly.">
        {(r) => (
          <div className="space-y-6">
            <div className="grid lg:grid-cols-3 gap-4">
              <div className="card-pad text-center">
                <div className="h-sub">Overall Health Score</div>
                <HealthRing score={r.executive_summary.overall_health_score} />
              </div>
              <div className="card-pad lg:col-span-2">
                <div className="flex items-center justify-between mb-2">
                  <div className="h-sub">Executive Summary</div>
                  {r.meta.ai.status === 'ok'
                    ? <span className="text-[11px] text-accent">AI · {r.meta.ai.provider}{r.meta.ai.model ? ` / ${r.meta.ai.model}` : ''}</span>
                    : <span className="text-[11px] text-amber-400">AI narrative unavailable</span>}
                </div>
                {r.meta.ai.status === 'ok' ? (
                  <>
                    <p className="text-slate-300 text-sm leading-relaxed">{r.executive_summary.summary}</p>
                    {r.executive_summary.portfolio_health && (
                      <p className="text-slate-400 text-sm mt-2">{r.executive_summary.portfolio_health}</p>
                    )}
                    {r.executive_summary.priority_actions?.length > 0 && (
                      <div className="mt-3">
                        <div className="h-sub mb-1">Priority Actions</div>
                        <ol className="text-sm text-slate-400 space-y-1">
                          {r.executive_summary.priority_actions.slice(0, 4).map((a, i) => (
                            <li key={i}>{i + 1}. {a}</li>
                          ))}
                        </ol>
                      </div>
                    )}
                  </>
                ) : (
                  <p className="text-sm fg-warn">
                    {r.meta.ai.error || 'Configure an LLM provider (EDIP_LLM_PROVIDER) to generate the executive narrative.'}
                    {' '}Deterministic KPIs, signals and forecasts below remain available.
                  </p>
                )}
              </div>
            </div>

            <AsyncSection state={kpis}>
              {(ks) => (
                <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
                  {ks.filter((k) => k.sparkline?.length).slice(0, 8).map((k) => <KpiTile key={k.id} k={k} />)}
                </div>
              )}
            </AsyncSection>

            <div className="grid lg:grid-cols-2 gap-4">
              <div className="card-pad">
                <div className="flex justify-between items-center mb-3">
                  <div className="h-title">Top Insights</div>
                  <Link className="text-xs text-accent" to={`/p/${projectId}/insights`}>view all →</Link>
                </div>
                <div className="space-y-3">
                  {(r.business_insights || []).slice(0, 5).map((i, idx) => (
                    <div key={idx} className="flex gap-3 items-start">
                      <Badge tone="accent">AI</Badge>
                      <div className="text-sm text-slate-300">
                        {i.title}
                        {i.detail && <span className="text-slate-500"> — {i.detail}</span>}
                      </div>
                    </div>
                  ))}
                  {(r.business_insights || []).length === 0 && (
                    <div className="text-sm text-slate-600">AI insights unavailable — see Signals for deterministic facts.</div>
                  )}
                </div>
              </div>
              <div className="card-pad">
                <div className="flex justify-between items-center mb-3">
                  <div className="h-title">Portfolio</div>
                  <Link className="text-xs text-accent" to={`/p/${projectId}/datasets`}>explore →</Link>
                </div>
                <EChart height={230} option={{
                  tooltip: {},
                  xAxis: { type: 'category', ...axisStyle,
                           data: r.dataset_summary.tables.map((t) => t.name), axisLabel: { color: '#64748b', rotate: 20 } },
                  yAxis: { type: 'value', ...axisStyle, name: 'rows' },
                  series: [{ type: 'bar', data: r.dataset_summary.tables.map((t) => t.rows),
                             itemStyle: { color: PALETTE[0], borderRadius: [4, 4, 0, 0] } }],
                }} />
              </div>
            </div>
          </div>
        )}
      </AsyncSection>
    </>
  )
}
