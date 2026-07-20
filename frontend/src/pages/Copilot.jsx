import { useRef, useState } from 'react'
import { useParams } from 'react-router-dom'
import { api } from '../api/client'
import { Badge, PageHeader } from '../components/ui'

const SUGGESTIONS = [
  'Why did growth slow?',
  'Which KPI is declining?',
  'Compare the last two periods',
  'Predict next quarter',
  'Explain active users',
  'What is causing cannibalization?',
]

export default function Copilot() {
  const { projectId } = useParams()
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [busy, setBusy] = useState(false)
  const endRef = useRef(null)

  async function send(text) {
    const q = (text ?? input).trim()
    if (!q || busy) return
    setInput('')
    setMessages((m) => [...m, { role: 'user', text: q }])
    setBusy(true)
    try {
      const res = await api.ask(projectId, q)
      setMessages((m) => [...m, { role: 'assistant', ...res }])
    } catch (e) {
      setMessages((m) => [...m, { role: 'assistant', answer: `Error: ${e.message}` }])
    } finally {
      setBusy(false)
      setTimeout(() => endRef.current?.scrollIntoView({ behavior: 'smooth' }), 50)
    }
  }

  return (
    <div className="flex flex-col h-[calc(100vh-6rem)]">
      <PageHeader title="AI Copilot" subtitle="Grounded in your datasets, KPIs, insights and knowledge graph" />
      <div className="flex-1 overflow-y-auto space-y-4 pr-2">
        {messages.length === 0 && (
          <div className="card-pad">
            <div className="h-sub mb-3">Try asking</div>
            <div className="flex flex-wrap gap-2">
              {SUGGESTIONS.map((s) => (
                <button key={s} className="btn-ghost" onClick={() => send(s)}>{s}</button>
              ))}
            </div>
          </div>
        )}
        {messages.map((m, i) =>
          m.role === 'user' ? (
            <div key={i} className="flex justify-end">
              <div className="bg-accent/20 border border-accent/40 rounded-2xl rounded-br-sm px-4 py-2 max-w-xl text-sm text-slate-100">
                {m.text}
              </div>
            </div>
          ) : (
            <div key={i} className="card-pad max-w-3xl">
              <div className="flex items-center gap-2">
                {m.status === 'ok' && m.provider && <Badge tone="accent">AI · {m.provider}{m.model ? ` / ${m.model}` : ''}</Badge>}
                {m.status && m.status !== 'ok' && <Badge tone="warn">{m.status}</Badge>}
                {m.confidence > 0 && <span className="text-[11px] text-slate-600">confidence {Math.round(m.confidence * 100)}%</span>}
              </div>
              <div className="text-sm text-slate-200 whitespace-pre-wrap mt-2">{m.answer}</div>
              {m.cited_facts?.length > 0 && (
                <div className="mt-3 pt-3 border-t border-surface-border">
                  <div className="h-sub mb-1">Cited facts</div>
                  <ul className="text-xs text-slate-500 space-y-1">
                    {m.cited_facts.map((f, j) => <li key={j}>• {f}</li>)}
                  </ul>
                </div>
              )}
              {m.sources?.length > 0 && (
                <div className="mt-3 pt-3 border-t border-surface-border">
                  <div className="h-sub mb-1">Retrieved context</div>
                  <div className="flex flex-wrap gap-2">
                    {m.sources.slice(0, 6).map((s, j) => (
                      <span key={j} className="text-[11px] bg-surface px-2 py-0.5 rounded border border-surface-border text-slate-500">
                        {s.kind}: {s.title}
                      </span>
                    ))}
                  </div>
                </div>
              )}
            </div>
          ),
        )}
        {busy && <div className="text-sm text-slate-500 animate-pulse">Copilot is reasoning…</div>}
        <div ref={endRef} />
      </div>
      <div className="mt-4 flex gap-2">
        <input className="input" placeholder="Ask anything about your data…"
               value={input} onChange={(e) => setInput(e.target.value)}
               onKeyDown={(e) => e.key === 'Enter' && send()} />
        <button className="btn" onClick={() => send()} disabled={busy || !input.trim()}>Send</button>
      </div>
    </div>
  )
}
