// Persistent AI sidebar (V9.0) — always-available AI panel that knows the
// current page and answers with evidence, using the same Enterprise Copilot
// reasoning as the full chat. Floating toggle, docked panel.
import { useEffect, useRef, useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import { api } from '../api/client'
import { Badge } from './ui'

const PAGE_LABEL = {
  '/': 'AI Home', '/assistant': 'Chat', '/files': 'Files', '/search': 'Search',
  '/reports': 'Reports', '/products': 'Products', '/ecosystem': 'Ecosystem',
  '/evolution': 'Evolution', '/decisions': 'Decisions', '/timeline': 'Timeline',
  '/pm-home': 'Dashboard',
}

function pageName(path) {
  if (PAGE_LABEL[path]) return PAGE_LABEL[path]
  const base = '/' + (path.split('/')[1] || '')
  return PAGE_LABEL[base] || 'this page'
}

export default function AISidebar() {
  const [open, setOpen] = useState(false)
  const [msgs, setMsgs] = useState([])
  const [input, setInput] = useState('')
  const [busy, setBusy] = useState(false)
  const [convId, setConvId] = useState('')
  const location = useLocation()
  const nav = useNavigate()
  const endRef = useRef(null)
  const page = pageName(location.pathname)

  useEffect(() => {
    if (open) setTimeout(() => endRef.current?.scrollIntoView({ behavior: 'smooth' }), 50)
  }, [msgs, open])

  async function send(text) {
    const q = (text ?? input).trim()
    if (!q || busy) return
    setInput('')
    setMsgs((m) => [...m, { role: 'user', text: q }])
    setBusy(true)
    try {
      // give the copilot the page context so answers are situation-aware
      const framed = `[Context: user is on the ${page} page] ${q}`
      const res = await api.copilotChat(framed, convId)
      setConvId(res.conversation_id || convId)
      setMsgs((m) => [...m, { role: 'assistant', ...res }])
    } catch (e) {
      setMsgs((m) => [...m, { role: 'assistant', answer: `Could not answer: ${e.message}`, status: 'error' }])
    } finally { setBusy(false) }
  }

  if (!open) {
    return (
      <button onClick={() => setOpen(true)} title="Ask AI about this page"
        className="fixed bottom-5 right-5 z-40 w-12 h-12 rounded-full bg-accent text-white text-xl shadow-lg shadow-black/30 flex items-center justify-center hover:scale-105 transition">
        ✦
      </button>
    )
  }

  return (
    <div className="fixed bottom-5 right-5 z-40 w-[360px] max-w-[calc(100vw-2rem)] h-[560px] max-h-[calc(100vh-2rem)] card shadow-2xl shadow-black/40 flex flex-col">
      <div className="flex items-center gap-2 px-3 py-2.5 border-b border-surface-border">
        <span className="text-accent">✦</span>
        <span className="text-sm font-semibold text-slate-200">AI Assistant</span>
        <Badge tone="default">{page}</Badge>
        <div className="flex-1" />
        <button onClick={() => nav('/assistant')} title="Open full chat"
          className="text-xs text-slate-500 hover:text-accent">⤢</button>
        <button onClick={() => setOpen(false)} title="Close"
          className="text-slate-500 hover:text-slate-200">✕</button>
      </div>

      <div className="flex-1 overflow-y-auto p-3 space-y-3">
        {msgs.length === 0 && (
          <div className="text-xs text-slate-500">
            <p className="mb-2">Ask about <span className="text-slate-300">{page}</span> — or anything across the enterprise.</p>
            <div className="space-y-1">
              {['Explain what I\'m looking at', 'What changed recently?', 'What should we do next?'].map((s) => (
                <button key={s} onClick={() => send(s)}
                  className="block w-full text-left px-2 py-1.5 rounded bg-surface-overlay/50 hover:bg-surface-overlay text-slate-300">
                  {s}
                </button>
              ))}
            </div>
          </div>
        )}
        {msgs.map((m, i) => m.role === 'user' ? (
          <div key={i} className="flex justify-end">
            <div className="bg-accent/15 border border-accent/30 rounded-xl rounded-br-sm px-3 py-1.5 max-w-[85%] text-sm text-slate-100">{m.text}</div>
          </div>
        ) : (
          <div key={i} className="text-sm text-slate-200">
            <div className="whitespace-pre-wrap leading-relaxed">{m.answer}</div>
            {(m.cited_facts || []).length > 0 && (
              <div className="mt-2 pt-2 border-t border-surface-border">
                <div className="text-[11px] text-slate-500 mb-1">Evidence</div>
                <ul className="text-[11px] text-slate-500 space-y-0.5">
                  {m.cited_facts.slice(0, 4).map((f, j) => <li key={j}>• {f}</li>)}
                </ul>
              </div>
            )}
            {m.confidence > 0 && (
              <div className="text-[10px] text-slate-600 mt-1">confidence {Math.round(m.confidence * 100)}%</div>
            )}
          </div>
        ))}
        {busy && <div className="text-xs text-slate-500 animate-pulse">Thinking…</div>}
        <div ref={endRef} />
      </div>

      <form onSubmit={(e) => { e.preventDefault(); send() }} className="p-2.5 border-t border-surface-border flex gap-2">
        <input value={input} onChange={(e) => setInput(e.target.value)}
          placeholder={`Ask about ${page}…`} className="input flex-1 !py-1.5 !text-sm" />
        <button className="btn !px-3 !py-1.5" type="submit" disabled={busy || !input.trim()}>↑</button>
      </form>
    </div>
  )
}
