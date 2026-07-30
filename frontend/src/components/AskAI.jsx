// A grounded "Ask AI" panel: fires one copilot question through the same
// evidence-gathering + orchestrator + validator pipeline as the Assistant, so
// an AI summary on a product/node page is never a free-floating LLM guess —
// it is validated against the same evidence a chat answer would cite, and if
// that evidence is too thin the copilot says so instead of inventing a story.
import { useState } from 'react'
import { api } from '../api/client'
import { Badge, Panel } from './ui'

export default function AskAI({ question, title = 'AI summary', prompt = 'Ask AI' }) {
  const [state, setState] = useState({ status: 'idle' })

  const run = async () => {
    setState({ status: 'loading' })
    try {
      const res = await api.copilotChat(question)
      setState({ status: 'done', res })
    } catch (e) {
      setState({ status: 'error', error: e?.message || 'The assistant is unavailable.' })
    }
  }

  return (
    <Panel title={title}>
      {state.status === 'idle' && (
        <div className="flex items-center justify-between gap-3">
          <p className="text-xs fg-muted">
            Generates a grounded summary from this product's real analytics, ML and
            knowledge evidence — nothing is written until you ask.
          </p>
          <button className="btn shrink-0" onClick={run}>{prompt}</button>
        </div>
      )}
      {state.status === 'loading' && (
        <div className="text-xs fg-muted animate-pulse">Gathering evidence and reasoning…</div>
      )}
      {state.status === 'error' && (
        <div className="text-xs fg-danger">{state.error}</div>
      )}
      {state.status === 'done' && (
        <div>
          <div className="flex items-center gap-2 flex-wrap mb-2">
            {state.res.status && state.res.status !== 'ok' && (
              <Badge tone="warn">{String(state.res.status).replace(/_/g, ' ')}</Badge>
            )}
            {state.res.confidence > 0 && (
              <span className="text-[11px] fg-muted tabular-nums">
                confidence {Math.round(state.res.confidence * 100)}%
              </span>
            )}
          </div>
          <p className="text-sm fg-primary whitespace-pre-wrap leading-relaxed">{state.res.answer}</p>
          {(state.res.cited_facts || []).length > 0 && (
            <div className="mt-3 pt-3 border-t border-surface-border">
              <div className="text-[11px] uppercase tracking-wide fg-muted mb-1.5">Based on</div>
              <ul className="text-xs fg-muted space-y-1">
                {state.res.cited_facts.slice(0, 6).map((f, i) => <li key={i}>• {f}</li>)}
              </ul>
            </div>
          )}
          {(state.res.limitations || []).length > 0 && (
            <div className="mt-3 text-[11px] fg-muted">{state.res.limitations.join(' · ')}</div>
          )}
          <button className="btn-ghost mt-3 text-xs" onClick={run}>Regenerate</button>
        </div>
      )}
    </Panel>
  )
}
