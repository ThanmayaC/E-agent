import { useParams } from 'react-router-dom'
import { api, fmt } from '../api/client'
import { AsyncSection, Badge, PageHeader, useAsync } from '../components/ui'
import EChart, { axisStyle } from '../components/EChart'

export default function KPIs() {
  const { projectId } = useParams()
  const state = useAsync(() => api.kpis(projectId), [projectId])

  return (
    <>
      <PageHeader title="KPI Analysis" subtitle="Discovered automatically — no KPI configuration" />
      <AsyncSection state={state}>
        {(kpis) => (
          <div className="space-y-4">
            {kpis.map((k) => (
              <div key={k.id} className="card-pad grid lg:grid-cols-3 gap-4 items-center">
                <div>
                  <div className="flex items-center gap-2 flex-wrap">
                    <span className="font-semibold text-slate-100">{k.name}</span>
                    <Badge tone={k.trend === 'up' ? 'success' : k.trend === 'down' ? 'danger' : 'default'}>{k.trend}</Badge>
                  </div>
                  <div className="font-mono text-xs text-slate-600 mt-1">{k.expression}</div>
                  <div className="flex gap-6 mt-3 text-sm">
                    <div><div className="h-sub">Current</div><div className="text-xl font-bold text-slate-100">{fmt.num(k.current_value)}{k.unit === '%' && '%'}</div></div>
                    <div><div className="h-sub">Previous</div><div className="text-xl text-slate-400">{fmt.num(k.previous_value)}</div></div>
                    <div><div className="h-sub">Growth</div>
                      <div className={`text-xl ${k.growth_pct > 0 ? 'text-emerald-400' : k.growth_pct < 0 ? 'text-rose-400' : 'text-slate-400'}`}>
                        {fmt.pct(k.growth_pct)}
                      </div>
                    </div>
                    {k.forecast_next != null && (
                      <div><div className="h-sub">Forecast next</div>
                        <div className="text-xl text-sky-400">{fmt.num(k.forecast_next)}</div></div>
                    )}
                  </div>
                </div>
                <div className="lg:col-span-2">
                  {k.sparkline?.length > 1 ? (
                    <EChart height={160} option={{
                      tooltip: { trigger: 'axis' },
                      xAxis: { type: 'category', ...axisStyle, data: k.sparkline_labels },
                      yAxis: { type: 'value', ...axisStyle, min: 'dataMin' },
                      series: [{ type: 'line', data: k.sparkline, showSymbol: false, smooth: true,
                                 lineStyle: { color: k.trend === 'down' ? '#f87171' : '#4f8ef7', width: 2 },
                                 areaStyle: { opacity: 0.1 } }],
                    }} />
                  ) : (
                    <div className="text-sm text-slate-600 text-center">No time series available for this KPI</div>
                  )}
                </div>
              </div>
            ))}
          </div>
        )}
      </AsyncSection>
    </>
  )
}
