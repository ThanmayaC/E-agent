// LLM status — whether a model is actually connected, and what it has
// actually done. Every number here comes from recorded calls: the platform
// records provider, model, tokens, and duration after each LLM request, so
// this page cannot show activity that did not happen.
import { api } from '../../api/client'
import {
  AsyncSection, Badge, PageHeader, Panel, PanelEmpty, Stat, useAsync, when,
} from '../../components/ui'

export default function AdminLLM() {
  const state = useAsync(async () => {
    const [workspace, intents, usage, obs] = await Promise.all([
      api.copilotWorkspace().catch(() => null),
      api.copilotIntents().catch(() => null),
      api.opsModelUsage().catch(() => null),
      api.opsObservability().catch(() => null),
    ])
    return { workspace, intents, usage, obs }
  }, [])

  return (
    <>
      <PageHeader title="LLM"
                  subtitle="Provider, model, connection state, and recorded request volume" />
      <AsyncSection state={state} empty="The conversational layer is disabled.">
        {({ workspace, intents, usage, obs }) => {
          const provider = workspace?.provider || {}
          const primary = provider.primary || {}
          const fallback = provider.fallback
          const connected = Boolean(provider.available && primary.provider)
          const summary = usage?.summary || {}
          const calls = summary.calls ?? 0
          const latency = obs?.sections?.processing_latency?.operations?.llm_chat

          if (!connected) return <NotConnected />

          return (
            <div className="space-y-5">
              <div className="grid gap-4 md:grid-cols-4">
                <Stat label="Provider" value={primary.provider} tone="fg-success" />
                <Stat label="Model" value={primary.model || 'auto-selected'} />
                <Stat label="Connection"
                      value={calls > 0 ? 'verified' : 'configured'}
                      tone={calls > 0 ? 'fg-success' : 'fg-warn'}
                      hint={calls > 0
                        ? 'a request has completed against this provider'
                        : 'configured but not yet exercised — ask a question to verify'} />
                <Stat label="Fallback" value={fallback?.provider || 'none'}
                      hint={fallback ? `model ${fallback.model || 'auto'}`
                                     : 'no secondary provider configured'} />
              </div>

              <div className="grid gap-4 md:grid-cols-4">
                <Stat label="Requests" value={calls}
                      hint="recorded since the backend started" />
                <Stat label="Tokens" value={summary.tokens_total ?? 0}
                      hint="prompt + completion, as reported by the provider" />
                <Stat label="Avg latency"
                      value={latency?.avg_ms != null ? `${latency.avg_ms} ms`
                             : summary.avg_duration_ms ? `${summary.avg_duration_ms} ms` : '—'}
                      hint={latency?.samples
                        ? `${latency.samples} call(s) · p95 ${latency.p95_ms} ms`
                        : 'no calls timed yet'} />
                <Stat label="Failures" value={summary.failures ?? 0}
                      tone={(summary.failures ?? 0) > 0 ? 'fg-danger' : 'fg-primary'} />
              </div>

              {calls === 0 && (
                <Panel title="No requests recorded yet">
                  <p className="text-sm fg-muted">
                    A provider is configured, but nothing has called it since this backend
                    started. Ask the assistant a question — the request, its token counts,
                    and its latency will appear here.
                  </p>
                </Panel>
              )}

              <Panel title="Recent requests">
                {(usage?.usage || []).length === 0 ? (
                  <PanelEmpty text="No LLM requests recorded since startup." />
                ) : (
                  <div className="overflow-x-auto">
                    <table className="table-base">
                      <thead>
                        <tr><th>Model</th><th>Status</th><th>Tokens in</th>
                            <th>Tokens out</th><th>Duration</th><th>When</th></tr>
                      </thead>
                      <tbody>
                        {(usage.usage || []).slice(0, 25).map((u, i) => (
                          <tr key={i}>
                            <td className="font-mono text-xs">{u.model || u.provider}</td>
                            <td><Badge tone={u.status === 'ok' ? 'success' : 'danger'}>{u.status}</Badge></td>
                            <td className="tabular-nums text-xs">{u.tokens_in ?? 0}</td>
                            <td className="tabular-nums text-xs">{u.tokens_out ?? 0}</td>
                            <td className="tabular-nums text-xs">{u.duration_ms ?? 0} ms</td>
                            <td className="text-xs">{when(u.at)}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                )}
              </Panel>

              <Panel title="Understanding routes">
                {(intents?.intents || []).length === 0 ? (
                  <PanelEmpty text="Intent vocabulary unavailable." />
                ) : (
                  <div className="flex flex-wrap gap-2">
                    {(intents.intents || []).map((it, i) => (
                      <Badge key={i}>{typeof it === 'string' ? it : it.intent || it.name}</Badge>
                    ))}
                  </div>
                )}
              </Panel>
            </div>
          )
        }}
      </AsyncSection>
    </>
  )
}

// The honest state. No provider means no AI narration — saying so plainly is
// the point, because the deterministic analytics genuinely do still work.
function NotConnected() {
  return (
    <Panel title="No LLM Provider Connected">
      <p className="text-sm fg-warn mb-3">
        No language model is configured or reachable, so the platform cannot narrate
        answers, summaries, or reports. Retrieval, KPIs, forecasts, and every
        deterministic analytic remain fully available — they do not use a model.
      </p>
      <p className="text-sm fg-muted mb-2">To connect one, set these and restart the backend:</p>
      <pre className="text-xs font-mono bg-surface border border-surface-border rounded-lg p-3 overflow-x-auto">
{`EDIP_LLM_PROVIDER=ollama       # or openai | azure-openai | anthropic | gemini | enterprise
EDIP_LLM_MODEL=qwen3:14b       # leave empty to auto-select the first installed Ollama model
EDIP_LLM_BASE_URL=http://localhost:11434
EDIP_LLM_API_KEY=              # required for the hosted providers, not for Ollama`}
      </pre>
      <p className="text-xs fg-muted mt-3">
        Ollama needs no key but must be running locally with a model pulled
        (<span className="font-mono">ollama pull qwen3:14b</span>).
      </p>
    </Panel>
  )
}
