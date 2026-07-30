// Shared rendering for one ML pipeline forecast result (the shape returned by
// /intel/ml/forecast and embedded in /intel/products/{code}): forecast chart,
// confidence, supporting factors, most influential features, business reason,
// risks, suggested actions, anomaly detection and EDA. Reused by the ML Engine
// admin console and every per-product / per-node dashboard so a forecast reads
// the same way everywhere in the platform.
import { fmt } from '../api/client'
import { Badge, Panel, PanelEmpty, Stat } from './ui'
import EChart from './EChart'

const TONE = { strong: 'success', moderate: 'warn', weak: 'default' }
const RISK_TONE = { high: 'danger', medium: 'warn', low: 'default' }

export function prettifyKey(key) {
  return String(key).replace(/_/g, ' ').replace(/\bpct\b/, '%').replace(/\binr\b/i, '(INR)')
}

export function ForecastChart({ backtest, forecast, unit, height = 300 }) {
  const history = (backtest?.recent_predictions || []).map((p) => ({
    date: p.date, actual: p.actual, predicted: p.predicted,
  }))
  const dates = [...history.map((h) => h.date), ...forecast.map((f) => f.date)]
  const actualSeries = [...history.map((h) => h.actual), ...forecast.map(() => null)]
  const predictedSeries = [...history.map((h) => h.predicted),
    ...forecast.map((f) => f.forecast)]
  const lower = [...history.map(() => null), ...forecast.map((f) => f.lower_80)]
  const upper = [...history.map(() => null), ...forecast.map((f) => f.upper_80)]

  const option = {
    tooltip: { trigger: 'axis' },
    legend: { data: ['Actual', 'Forecast', '80% interval'], top: 0, textStyle: {} },
    grid: { left: 56, right: 20, top: 40, bottom: 32 },
    xAxis: { type: 'category', data: dates, axisLabel: { rotate: 45, fontSize: 10 } },
    yAxis: { type: 'value', name: unit || '', axisLabel: { fontSize: 10 } },
    series: [
      { name: '80% interval', type: 'line', data: upper, lineStyle: { opacity: 0 },
        stack: 'band', symbol: 'none', areaStyle: { opacity: 0 }, silent: true },
      { name: '80% interval', type: 'line', data: lower.map((v, i) =>
          v == null ? null : v - (upper[i] ?? v)), lineStyle: { opacity: 0 },
        stack: 'band', symbol: 'none', areaStyle: { opacity: 0.14 }, silent: true },
      { name: 'Actual', type: 'line', data: actualSeries, symbol: 'none', smooth: 0.2 },
      { name: 'Forecast', type: 'line', data: predictedSeries, symbol: 'none',
        smooth: 0.2, lineStyle: { type: 'dashed' } },
    ],
  }
  return <EChart option={option} height={height} />
}

/** The complete narrative for one forecast: everything section 7 of the spec
 *  requires — forecast, confidence, supporting factors, influential features,
 *  business reason, risks, suggested actions — plus anomaly detection and EDA.
 *  `d` is a full /intel/ml/forecast response (or a product/node's `.forecast`
 *  field, which is the same shape). Set `compact` to drop the EDA panel and
 *  anomaly table for tighter spaces (e.g. inside a node drawer). */
export function MLForecastPanel({ d, compact = false }) {
  if (!d || d.available === false) {
    return <PanelEmpty text="Not enough history to forecast this slice yet." />
  }
  return (
    <div className="space-y-5">
      <div className="grid gap-4 md:grid-cols-4">
        <Stat label="Backtest MAPE" value={`${d.backtest.mape}%`}
              tone={d.backtest.mape < 10 ? 'fg-success' : 'fg-warn'}
              hint={`${d.backtest.folds} walk-forward fold(s)`} />
        <Stat label="Skill vs naive" value={`${d.backtest.skill_vs_naive}%`}
              hint={`naive MAPE ${d.backtest.naive_mape}%`} />
        <Stat label="80% interval coverage" value={`${d.backtest.coverage_80}%`}
              hint={`R² ${d.backtest.r2}`} />
        <Stat label="Confidence" value={`${d.confidence.score} · ${d.confidence.band}`}
              tone={d.confidence.band === 'high' ? 'fg-success'
                    : d.confidence.band === 'low' ? 'fg-danger' : 'fg-warn'} />
      </div>

      <Panel title={`${d.target_label} — forecast${d.window ? ` (${d.window.start} to ${d.window.end})` : ''}`}>
        <ForecastChart backtest={d.backtest} forecast={d.forecast} unit={d.unit} />
      </Panel>

      <Panel title="Business reason">
        <p className="text-sm fg-primary leading-relaxed">{d.business_reason}</p>
        <p className="text-xs fg-muted mt-2">{d.confidence.interpretation}</p>
      </Panel>

      <div className="grid md:grid-cols-2 gap-4">
        <Panel title="Supporting factors">
          {(d.supporting_factors || []).length === 0 ? <PanelEmpty text="No factors detected." /> : (
            <div className="space-y-2">
              {d.supporting_factors.map((f, i) => (
                <div key={i} className="text-xs border-b border-surface-border/50 pb-2 last:border-0">
                  <div className="flex items-center justify-between gap-2">
                    <span className="fg-primary font-medium capitalize">{f.factor}</span>
                    <Badge tone={TONE[f.strength] || 'default'}>{f.strength}</Badge>
                  </div>
                  <div className="fg-muted mt-0.5">{f.finding}</div>
                  <div className="text-[11px] fg-muted opacity-70 font-mono">{f.evidence}</div>
                </div>
              ))}
            </div>
          )}
        </Panel>

        <Panel title="Most influential features">
          {(d.most_influential_features || []).length === 0 ? <PanelEmpty text="No feature importances." /> : (
            <div className="space-y-2">
              {d.most_influential_features.map((f, i) => (
                <div key={i} className="text-xs">
                  <div className="flex items-center justify-between">
                    <span className="fg-primary">{f.label}</span>
                    <span className="fg-muted tabular-nums">{f.importance_pct}%</span>
                  </div>
                  <div className="h-1.5 rounded-full bg-surface-overlay/60 mt-1 overflow-hidden">
                    <div className="h-full rounded-full bg-[var(--chart-1)]"
                         style={{ width: `${Math.min(100, f.importance_pct)}%` }} />
                  </div>
                </div>
              ))}
            </div>
          )}
        </Panel>
      </div>

      <div className="grid md:grid-cols-2 gap-4">
        <Panel title="Potential risks">
          {(d.potential_risks || []).length === 0 ? <PanelEmpty text="No material risks flagged." /> : (
            <ul className="text-xs fg-muted space-y-1.5 list-disc list-inside">
              {d.potential_risks.map((r, i) => <li key={i}>{r}</li>)}
            </ul>
          )}
        </Panel>
        <Panel title="Suggested actions">
          {(d.suggested_actions || []).length === 0 ? <PanelEmpty text="No actions suggested." /> : (
            <div className="space-y-2">
              {d.suggested_actions.map((a, i) => (
                <div key={i} className="text-xs flex items-start gap-2">
                  <Badge tone={RISK_TONE[a.priority] || 'default'}>{a.priority}</Badge>
                  <div>
                    <div className="fg-primary">{a.action}</div>
                    <div className="fg-muted opacity-70 text-[11px]">{a.trigger}</div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </Panel>
      </div>

      {!compact && (
        <Panel title="Anomaly detection"
               action={d.anomalies?.validation?.scored ? (
                 <span className="text-[11px] fg-muted">
                   precision {d.anomalies.validation.precision} · recall {d.anomalies.validation.recall}
                   {' '}· F1 {d.anomalies.validation.f1} (scored against {d.anomalies.validation.incidents_in_ledger} real incidents)
                 </span>
               ) : null}>
          {(d.anomalies?.multivariate_anomalies || []).length === 0 ? <PanelEmpty text="No anomalies detected in this window." /> : (
            <div className="overflow-x-auto">
              <table className="table-base">
                <thead>
                  <tr><th>Date</th><th>Score</th><th>Primary driver</th><th>Deviation</th></tr>
                </thead>
                <tbody>
                  {d.anomalies.multivariate_anomalies.slice(0, 12).map((a, i) => (
                    <tr key={i}>
                      <td className="text-xs font-mono">{a.date}</td>
                      <td className="text-xs tabular-nums">{a.anomaly_score}</td>
                      <td className="text-xs">{prettifyKey(a.primary_driver)}</td>
                      <td className="text-xs tabular-nums">{a.driver_z > 0 ? '+' : ''}{a.driver_z}σ</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </Panel>
      )}

      {!compact && d.eda && (
        <Panel title="EDA — trend & seasonality">
          <div className="grid md:grid-cols-3 gap-4 text-xs">
            <div>
              <div className="fg-muted mb-1">Trend</div>
              <div className="fg-primary">
                {d.eda.trend?.direction} ({fmt.pct(d.eda.trend?.total_change_pct)} over window,
                R² {d.eda.trend?.r_squared})
              </div>
            </div>
            <div>
              <div className="fg-muted mb-1">Weekly seasonality</div>
              <div className="fg-primary">
                {d.eda.weekly_seasonality?.detected ? 'detected' : 'not detected'}
                {d.eda.weekly_seasonality?.detected &&
                  ` (F=${d.eda.weekly_seasonality.f_statistic}, p=${d.eda.weekly_seasonality.p_value})`}
              </div>
            </div>
            <div>
              <div className="fg-muted mb-1">Distribution</div>
              <div className="fg-primary">
                mean {fmt.num(d.eda.distribution?.mean)}, std {fmt.num(d.eda.distribution?.std)},
                {' '}{d.eda.distribution?.outlier_pct}% outliers
              </div>
            </div>
          </div>
        </Panel>
      )}
    </div>
  )
}
