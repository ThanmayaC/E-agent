import { Badge } from './ui'

// Shows where narrative came from: which LLM, or why it's unavailable.
export function AIStatus({ status, provider, model, error }) {
  if (status === 'ok') {
    return (
      <div className="flex items-center gap-2">
        <Badge tone="accent">AI · {provider}{model ? ` / ${model}` : ''}</Badge>
      </div>
    )
  }
  return (
    <div className="card-pad border-amber-500/40 text-sm fg-warn">
      <div className="font-medium mb-1">AI reasoning {status === 'failed' ? 'failed' : 'unavailable'}</div>
      <div className="text-xs mt-1 fg-warn">{error || 'Configure EDIP_LLM_PROVIDER (ollama, openai, azure-openai, anthropic, gemini, enterprise).'}</div>
      <div className="text-xs mt-1 fg-muted">Deterministic analytics (KPIs, signals, forecasts, quality) remain available.</div>
    </div>
  )
}
