// ML Engine — the sklearn pipeline over the raw transaction warehouse:
// EDA -> feature engineering -> training -> backtest -> forecast -> reason
// generation -> confidence -> business recommendations. Every number here is
// a live run against the real corpus, not a stored model card.
import { useState } from 'react'
import { api } from '../../api/client'
import { AsyncSection, PageHeader, useAsync } from '../../components/ui'
import { MLForecastPanel, prettifyKey } from '../../components/MLForecast'

export default function AdminModels() {
  const [target, setTarget] = useState('attempts')
  const [horizon, setHorizon] = useState(14)

  const targets = useAsync(() => api.intelForecastable(), [])
  const state = useAsync(
    () => api.intelForecast({ target, horizon, full: true }),
    [target, horizon],
  )

  return (
    <div className="space-y-5">
      <PageHeader
        title="ML Engine"
        subtitle="Raw transactions -> EDA -> feature engineering -> training -> backtest -> forecast -> reason generation -> confidence -> business recommendations. Nothing here is precomputed." />

      <div className="flex flex-wrap items-center gap-3">
        <label className="text-xs text-slate-500 flex items-center gap-2">
          Target
          <select className="input" value={target}
                  onChange={(e) => setTarget(e.target.value)}>
            {(targets.data?.targets || [target]).map((t) => (
              <option key={t} value={t}>{prettifyKey(t)}</option>
            ))}
          </select>
        </label>
        <label className="text-xs text-slate-500 flex items-center gap-2">
          Horizon (days)
          <select className="input" value={horizon}
                  onChange={(e) => setHorizon(Number(e.target.value))}>
            {[7, 14, 30, 60].map((h) => <option key={h} value={h}>{h}</option>)}
          </select>
        </label>
        {state.data && (
          <span className="text-[11px] text-slate-600">
            {state.data.model} · {state.data.observations} day(s) trained ·
            {' '}{state.data.runtime_ms} ms
          </span>
        )}
      </div>

      <AsyncSection state={state} empty="ML pipeline unavailable — the transaction warehouse holds no data.">
        {(d) => <MLForecastPanel d={d} />}
      </AsyncSection>
    </div>
  )
}
