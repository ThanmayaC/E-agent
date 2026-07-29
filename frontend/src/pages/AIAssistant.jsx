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
              <button title={c.pinned ? 'Unpin' : 'Pin'} className="opacity-0 group-hover:opacity-100 text-xs text-slate-500 hover:text-amber-400"
                      onClick={(e) => { e.stopPropagation(); pinThread(c.conversation_id, !c.pinned) }}>★</button>
              <button title="Delete" className="opacity-0 group-hover:opacity-100 text-xs text-slate-500 hover:text-rose-400"
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
