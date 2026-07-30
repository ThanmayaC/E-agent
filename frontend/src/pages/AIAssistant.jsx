// AI Assistant — the Product Manager's primary interface, continuing to use
// the Enterprise Brain / copilot reasoning underneath. Instead of an empty
// chat window, the landing state shows suggested questions grounded in the
// five-week enterprise history (comparisons, trends, focus areas).
import { useEffect, useRef, useState } from 'react'
import { Link, useLocation } from 'react-router-dom'
import { api } from '../api/client'
import { Badge, Spinner } from '../components/ui'

// Staged progress while the copilot works, so the user sees the pipeline
// advancing (these stages run in this order in the backend) with elapsed time,
// instead of an indefinite "working…". Purely a status indicator — it never
// blocks; the request itself is bounded by the client timeout.
const STAGES = [
  [0, 'Initializing'],
  [1, 'Building context'],
  [3, 'Retrieving evidence'],
  [6, 'Calling AI'],
  [20, 'Generating report'],
]

function WorkingIndicator() {
  const [elapsed, setElapsed] = useState(0)
  useEffect(() => {
    const t0 = Date.now()
    const id = setInterval(() => setElapsed(Math.floor((Date.now() - t0) / 1000)), 500)
    return () => clearInterval(id)
  }, [])
  const stage = STAGES.filter(([s]) => s <= elapsed).slice(-1)[0]?.[1] || 'Working'
  return (
    <div className="text-sm text-slate-500 flex items-center gap-2">
      <span className="animate-pulse">●</span>
      <span>{stage}…</span>
      <span className="text-xs text-slate-600 tabular-nums">{elapsed}s</span>
    </div>
  )
}

const SUGGESTED_QUESTIONS = [
  'What happened this week?',
  'Compare this week with last week.',
  'Compare this month with last month.',
  'Which products need attention?',
  'Which banks require follow-up?',
  'Which merchants are affected?',
  "Generate today's executive summary.",
  "Summarize this week's executive review.",
  'What changed this month?',
  'Show growth opportunities.',
  "Predict next week's focus areas.",
]

// Phase 14 — the execution graph, shown on demand. Turns the black-box answer
// into an auditable one: which engines ran, the SQL an analytics query issued,
// the ML/forecast model called, the documents retrieved, and the timings.
const ENGINE_ICON = {
  analytics: '📊', knowledge: '📚', ml: '🧠', forecast: '📈',
  recommendation: '🎯', report: '📄',
}
const STATUS_TONE = { ok: 'success', empty: 'warn', unavailable: 'default', error: 'danger' }

function EngineDetail({ engine }) {
  const d = engine.detail || {}
  if (engine.engine === 'analytics' && d.sql) {
    return (
      <div className="mt-1">
        {d.window?.label && <div className="text-[10px] text-slate-500">window: {d.window.label} · {d.rows_scanned} rows</div>}
        <code className="block text-[10px] text-emerald-300/80 bg-black/30 rounded px-2 py-1 mt-1 overflow-x-auto whitespace-pre">{d.sql}</code>
      </div>
    )
  }
  if (engine.engine === 'ml' && d.models_run) {
    return <div className="text-[10px] text-slate-500 mt-1">models: {(d.models_run || []).join(', ') || '—'}</div>
  }
  if (engine.engine === 'forecast') {
    return <div className="text-[10px] text-slate-500 mt-1">model: {d.model} · horizon {d.horizon_days}d · {(d.kpis || []).join(', ')}</div>
  }
  if (engine.engine === 'knowledge') {
    return <div className="text-[10px] text-slate-500 mt-1">retrieved {d.documents_retrieved || 0} passage(s){d.titles?.length ? ` · ${d.titles.slice(0, 2).join('; ')}` : ''}</div>
  }
  if (d.titles?.length) return <div className="text-[10px] text-slate-500 mt-1">{d.titles.slice(0, 3).join(' · ')}</div>
  return null
}

function OrchestrationPanel({ orch }) {
  const [open, setOpen] = useState(false)
  if (!orch || orch.enabled === false) return null
  const cls = orch.classification || {}
  const engines = orch.engines || []
  const graph = orch.graph || []
  return (
    <div className="mt-3 pt-3 border-t border-surface-border">
      <button onClick={() => setOpen((o) => !o)}
              className="text-[11px] text-slate-500 hover:text-accent flex items-center gap-1.5">
        <span>{open ? '▾' : '▸'}</span> How this was answered
        <span className="text-slate-600">· {(orch.engines_run || []).length || engines.filter((e) => e.status === 'ok').length} engine(s) · {Math.round(orch.latency_ms || 0)}ms</span>
      </button>
      {open && (
        <div className="mt-2 space-y-3">
          {/* classification */}
          <div className="flex flex-wrap items-center gap-1.5">
            <span className="text-[10px] text-slate-600">intent</span>
            <Badge tone="default">{cls.intent}</Badge>
            <span className="text-[10px] text-slate-600 ml-1">route</span>
            {(cls.categories || []).map((c) => <Badge key={c} tone="accent">{ENGINE_ICON[c] || ''} {c}</Badge>)}
            {cls.hybrid && <Badge tone="info">hybrid</Badge>}
            {cls.time_range?.label && <span className="text-[10px] text-slate-500">🗓 {cls.time_range.label}</span>}
            {(cls.kpi_hints || []).map((k) => <span key={k} className="text-[10px] text-slate-500">· {k}</span>)}
          </div>
          {/* execution graph */}
          {graph.length > 0 && (
            <div className="flex flex-wrap items-center gap-1 text-[10px] text-slate-500">
              {graph.map((n, i) => (
                <span key={n.node} className="flex items-center gap-1">
                  <span className="bg-surface border border-surface-border rounded px-1.5 py-0.5">{n.label}</span>
                  {i < graph.length - 1 && <span className="text-slate-700">→</span>}
                </span>
              ))}
              <span className="text-slate-700">→</span>
              <span className="bg-surface border border-surface-border rounded px-1.5 py-0.5">LLM</span>
            </div>
          )}
          {/* engines */}
          <div className="space-y-2">
            {engines.map((e) => (
              <div key={e.engine} className="bg-surface/60 rounded border border-surface-border px-2.5 py-1.5">
                <div className="flex items-center gap-2 flex-wrap">
                  <span className="text-xs text-slate-300">{ENGINE_ICON[e.engine] || '•'} {e.label}</span>
                  <Badge tone={STATUS_TONE[e.status] || 'default'}>{e.status}</Badge>
                  <span className="text-[10px] text-slate-600 tabular-nums">{Math.round(e.latency_ms || 0)}ms · {e.evidence_count} evidence</span>
                </div>
                <EngineDetail engine={e} />
                {e.note && e.status !== 'ok' && <div className="text-[10px] text-slate-600 mt-1">{e.note}</div>}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}

function AnswerCard({ m }) {
  const actions = m.recommended_actions || []
  const steps = m.next_steps || []
  const reports = m.related_reports || []
  return (
    <div className="card-pad max-w-3xl">
      <div className="flex items-center gap-2 flex-wrap">
        <Badge tone="accent">✦ Assistant</Badge>
        {m.status && m.status !== 'ok' && <Badge tone="warn">{m.status.replace(/_/g, ' ')}</Badge>}
        {m.confidence > 0 && (
          <span className="text-[11px] text-slate-600 tabular-nums">confidence {Math.round(m.confidence * 100)}%</span>
        )}
      </div>
      <div className="text-sm text-slate-200 whitespace-pre-wrap mt-2 leading-relaxed">{m.answer}</div>

      {(m.cited_facts || []).length > 0 && (
        <div className="mt-3 pt-3 border-t border-surface-border">
          <div className="h-sub mb-1.5">Based on</div>
          <ul className="text-xs text-slate-500 space-y-1">
            {m.cited_facts.slice(0, 6).map((f, j) => <li key={j}>• {f}</li>)}
          </ul>
        </div>
      )}

      {(actions.length > 0 || steps.length > 0) && (
        <div className="mt-3 pt-3 border-t border-surface-border">
          <div className="h-sub mb-1.5">Suggested next moves</div>
          <ul className="text-xs text-slate-400 space-y-1">
            {actions.slice(0, 4).map((a, j) => (
              <li key={`a${j}`}>
                → {a.action}{a.product && <span className="text-slate-600"> · {a.product}</span>}
                {a.impact && <span className="text-slate-600"> · impact: {a.impact}</span>}
              </li>
            ))}
            {steps.slice(0, 3).map((s, j) => <li key={`s${j}`}>→ {typeof s === 'string' ? s : s.step || s.action}</li>)}
          </ul>
        </div>
      )}

      {reports.length > 0 && (
        <div className="mt-3 pt-3 border-t border-surface-border flex flex-wrap gap-2">
          {reports.slice(0, 4).map((r, j) => (
            <Link key={j} to={r.project_id ? `/reports/${r.project_id}` : '/reports'}
                  className="text-[11px] bg-surface px-2 py-1 rounded border border-surface-border text-slate-400 hover:text-accent hover:border-accent/50">
              ▣ {r.title || 'Report'}
            </Link>
          ))}
        </div>
      )}

      {(m.limitations || []).length > 0 && (
        <div className="mt-3 text-[11px] text-slate-600">{m.limitations.join(' · ')}</div>
      )}

      <OrchestrationPanel orch={m.orchestration} />
    </div>
  )
}

export default function AIAssistant() {
  const location = useLocation()
  const [conversations, setConversations] = useState([])
  const [conversationId, setConversationId] = useState('')
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [busy, setBusy] = useState(false)
  const [unavailable, setUnavailable] = useState(false)
  const [loadingThread, setLoadingThread] = useState(false)
  const endRef = useRef(null)
  const askedRef = useRef(false)

  const refreshConversations = () =>
    api.copilotConversations()
      .then((d) => setConversations(d.conversations || []))
      .catch((e) => { if (String(e.message).includes('disabled')) setUnavailable(true) })

  useEffect(() => { refreshConversations() }, [])

  // A question handed over from Home ("Ask AI") fires immediately.
  useEffect(() => {
    const q = location.state?.ask
    if (q && !askedRef.current) { askedRef.current = true; send(q) }
  }, []) // eslint-disable-line react-hooks/exhaustive-deps

  async function openThread(id) {
    setLoadingThread(true)
    setConversationId(id)
    try {
      const d = await api.copilotConversation(id)
      setMessages((d.messages || []).map((m) =>
        m.role === 'user'
          ? { role: 'user', text: m.content || m.message || m.text }
          : { role: 'assistant', answer: m.content || m.answer || '', ...(m.meta || {}) }))
    } catch { setMessages([]) } finally { setLoadingThread(false) }
  }

  function newThread() {
    setConversationId('')
    setMessages([])
  }

  async function send(text) {
    const q = (text ?? input).trim()
    if (!q || busy) return
    setInput('')
    setMessages((m) => [...m, { role: 'user', text: q }])
    setBusy(true)
    try {
      const res = await api.copilotChat(q, conversationId)
      setConversationId(res.conversation_id || conversationId)
      setMessages((m) => [...m, { role: 'assistant', ...res }])
      refreshConversations()
    } catch (e) {
      if (String(e.message).includes('disabled')) setUnavailable(true)
      setMessages((m) => [...m, { role: 'assistant', answer: `I could not answer that: ${e.message}`, status: 'error' }])
    } finally {
      setBusy(false)
      setTimeout(() => endRef.current?.scrollIntoView({ behavior: 'smooth' }), 50)
    }
  }

  const removeThread = (id) =>
    api.deleteCopilotConversation(id).then(() => {
      if (id === conversationId) newThread()
      refreshConversations()
    })
  const pinThread = (id, pinned) => api.pinCopilotConversation(id, pinned).then(refreshConversations)

  if (unavailable) {
    return (
      <div className="card-pad max-w-xl mx-auto mt-16 text-center py-12">
        <div className="text-2xl mb-3">✦</div>
        <div className="text-slate-200 font-medium">The AI Assistant is turned off for this workspace</div>
        <div className="text-sm text-slate-500 mt-2">
          An administrator can enable it under Admin → AI provider.
        </div>
      </div>
    )
  }

  return (
    <div className="flex gap-6 h-[calc(100vh-8.5rem)]">
      <aside className="w-60 shrink-0 hidden xl:flex flex-col card overflow-hidden">
        <div className="p-3 border-b border-surface-border">
          <button className="btn w-full justify-center !py-1.5 !text-xs" onClick={newThread}>New conversation</button>
        </div>
        <div className="flex-1 overflow-y-auto py-1">
          {conversations.length === 0 && <div className="px-4 py-3 text-xs text-slate-600">No conversations yet.</div>}
          {conversations.map((c) => (
            <div key={c.conversation_id}
                 className={`group px-3 py-2 mx-1 my-0.5 rounded-lg cursor-pointer text-sm flex items-center gap-2 ${
                   c.conversation_id === conversationId ? 'bg-surface-overlay text-slate-100' : 'text-slate-400 hover:bg-surface-overlay/50'}`}
                 onClick={() => openThread(c.conversation_id)}>
              <span className="flex-1 truncate">{c.pinned && '★ '}{c.title || 'Untitled'}</span>
              <button title={c.pinned ? 'Unpin' : 'Pin'} className="opacity-0 group-hover:opacity-100 text-xs text-slate-500 hv-warn"
                      onClick={(e) => { e.stopPropagation(); pinThread(c.conversation_id, !c.pinned) }}>★</button>
              <button title="Delete" className="opacity-0 group-hover:opacity-100 text-xs text-slate-500 hv-danger"
                      onClick={(e) => { e.stopPropagation(); removeThread(c.conversation_id) }}>✕</button>
            </div>
          ))}
        </div>
      </aside>

      <div className="flex-1 min-w-0 flex flex-col">
        <div className="flex-1 overflow-y-auto space-y-4 pr-1">
          {loadingThread && <Spinner label="Opening conversation…" />}
          {!loadingThread && messages.length === 0 && (
            <div className="max-w-2xl mx-auto pt-10 text-center">
              <div className="text-3xl mb-3 text-accent">✦</div>
              <h1 className="text-xl font-bold text-slate-100 tracking-tight">Ask the AI Assistant</h1>
              <p className="text-sm text-slate-500 mt-2">
                Answers are grounded in five weeks of reports, decisions, and enterprise history — with evidence shown.
              </p>
              <div className="mt-6 grid gap-2 sm:grid-cols-2">
                {SUGGESTED_QUESTIONS.map((s) => (
                  <button key={s} onClick={() => send(s)}
                          className="card-pad card-hover !p-3.5 text-left text-sm text-slate-300">
                    {s}
                  </button>
                ))}
              </div>
            </div>
          )}
          {messages.map((m, i) =>
            m.role === 'user' ? (
              <div key={i} className="flex justify-end">
                <div className="bg-accent/15 border border-accent/30 rounded-2xl rounded-br-sm px-4 py-2 max-w-xl text-sm text-slate-100">
                  {m.text}
                </div>
              </div>
            ) : (
              <AnswerCard key={i} m={m} />
            ))}
          {busy && <WorkingIndicator />}
          <div ref={endRef} />
        </div>
        <form className="mt-4 flex gap-2" onSubmit={(e) => { e.preventDefault(); send() }}>
          <input className="input" placeholder="Ask about products, banks, merchants, reports, or decisions…"
                 value={input} onChange={(e) => setInput(e.target.value)} />
          <button className="btn" type="submit" disabled={busy || !input.trim()}>Ask</button>
        </form>
      </div>
    </div>
  )
}
