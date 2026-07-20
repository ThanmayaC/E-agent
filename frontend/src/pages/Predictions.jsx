import { useParams } from 'react-router-dom'
import { api, fmt } from '../api/client'
import { AsyncSection, Badge, PageHeader, useAsync } from '../components/ui'
import EChart, { axisStyle } from '../components/EChart'

export default function Predictions() {
  const { projectId } = useParams()
  const forecasts = useAsync(() => api.predictions(projectId), [projectId])
  const kpis = useAsync(() => api.kpis(projectId), [projectId])

  return (
    <>
      <PageHeader title="Predictive Analytics" subtitle="Trend + seasonality forecasts with confidence intervals" />
      <AsyncSection state={forecasts} empty="No KPI has enough history to forecast.">
        {(fcs) => (
          <AsyncSection state={kpis}>
            {(ks) => (
              <div className="grid lg:grid-cols-2 gap-4">
                {fcs.map((f) => {
                  const kpi = ks.find((k) => k.id === f.kpi_id)
                  const hist = kpi?.sparkline || []
                  const histLabels = kpi?.sparkline_labels || []
                  const labels = [...histLabels, ...f.periods]
                  const pad = new Array(hist.length ? hist.length - 1 : 0).fill(null)
                  const bridge = hist.length ? [hist[hist.length - 1]] : []
                  if (f.status === 'unavailable') {
                    return (
                      <div key={f.kpi_id} className="card-pad">
                        <div className="flex justify-between items-center flex-wrap gap-2">
                          <div className="h-title">{f.kpi_name}</div>
                          <Badge tone="danger">forecast unavailable</Badge>
                        </div>
                        <div className="text-sm text-slate-500 mt-2">
                          This series did not pass forecast validation — no prediction is shown
                          because it would be misleading.
                        </div>
                        {(f.validation || []).map((v) => (
                          <div key={v} className="text-xs text-amber-400/80 mt-1">• {v}</div>
                        ))}
                      </div>
                    )
                  }
                  return (
                    <div key={f.kpi_id} className="card-pad">
                      <div className="flex justify-between items-center flex-wrap gap-2">
                        <div className="h-title">{f.kpi_name}</div>
                        <div className="flex gap-2">
                          <Badge tone="info">{f.method}</Badge>
                          {f.status === 'low_confidence' && <Badge tone="warn">low confidence</Badge>}
                          <Badge tone={f.confidence > 0.6 ? 'success' : 'warn'}>confidence {Math.round(f.confidence * 100)}%</Badge>
                        </div>
                      </div>
                      <div className="text-sm text-slate-500 mt-1">
                        Next period: <span className="text-slate-200 font-medium">{fmt.num(f.values[0])}</span>
                        {' '}(range {fmt.num(f.lower[0])} – {fmt.num(f.upper[0])})
                      </div>
                      {(f.validation || []).map((v) => (
                        <div key={v} className="text-xs text-amber-400/80 mt-1">• {v}</div>
                      ))}
                      <EChart height={240} option={{
                        tooltip: { trigger: 'axis' },
                        xAxis: { type: 'category', ...axisStyle, data: labels },
                        yAxis: { type: 'value', ...axisStyle, min: 'dataMin' },
                        series: [
                          { name: 'history', type: 'line', data: hist, showSymbol: false,
                            lineStyle: { color: '#4f8ef7', width: 2 } },
                          { name: 'forecast', type: 'line', data: [...pad, ...bridge, ...f.values],
                            showSymbol: false, lineStyle: { color: '#fbbf24', width: 2, type: 'dashed' } },
                          { name: 'upper', type: 'line', data: [...pad, ...bridge, ...f.upper],
                            lineStyle: { opacity: 0 }, stack: 'band', symbol: 'none' },
                          { name: 'lower', type: 'line', data: [...pad, ...bridge, ...f.lower],
                            lineStyle: { opacity: 0 }, symbol: 'none',
                            areaStyle: { color: '#fbbf24', opacity: 0.08 } },
                        ],
                      }} />
                    </div>
                  )
                })}
              </div>
            )}
          </AsyncSection>
        )}
      </AsyncSection>
    </>
  )
}
