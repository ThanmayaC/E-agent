// AI Home (V9.0) — the AI-first conversational workspace landing. A large
// prompt box, suggested prompts, recent conversations, recent files, recent
// reports, recommendations and pinned items. The prompt routes into the
// Enterprise Chat (/assistant), which answers with evidence.
import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { api } from '../api/client'
import { Badge, Spinner } from '../components/ui'

const FALLBACK_PROMPTS = [
  'What happened across UPI this month?',
  'Why did transaction value change?',
  'Which banks are improving?',
  'Generate an executive report.',
  'Which decision generated the most business value?',
  'Summarize the latest incident and its RCA.',
]

function Section({ title, action, children }) {
  return (
    <div className="card overflow-hidden">
      <div className="flex items-center justify-between px-4 py-2.5 border-b border-surface-border">
        <h2 className="text-sm font-semibold text-slate-200">{title}</h2>
        {action}
      </div>
      <div className="p-3">{children}</div>
    </div>
  )
}

export default function AIHome() {
  const nav = useNavigate()
  const [input, setInput] = useState('')
  const [feed, setFeed] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    api.workspaceHome().then(setFeed).catch(() => setFeed({})).finally(() => setLoading(false))
  }, [])

  const ask = (q) => {
    const question = (q ?? input).trim()
    if (!question) return
    nav('/assistant', { state: { ask: question } })
  }

  const prompts = (feed?.suggestions?.length ? feed.suggestions : FALLBACK_PROMPTS).slice(0, 6)
  const convos = feed?.recent_conversations || []
  const files = feed?.recent_files || []
  const reports = feed?.recent_reports || []
  const recs = feed?.recommendations || []
  const pinned = feed?.pinned || []
  const artifacts = feed?.recent_artifacts || []

  return (
    <div className="max-w-6xl mx-auto">
      {/* Hero prompt */}
      <div className="pt-6 pb-8 text-center">
        <div className="text-3xl mb-2 text-accent">✦</div>
        <h1 className="text-2xl font-bold text-slate-100 tracking-tight">Enterprise AI Workspace</h1>
        <p className="text-sm text-slate-500 mt-1.5">
          Ask anything across the UPI ecosystem — grounded in the Knowledge Graph, six-month history, reports and your files.
        </p>
        <form onSubmit={(e) => { e.preventDefault(); ask() }}
          className="mt-5 max-w-2xl mx-auto flex gap-2">
          <input autoFocus value={input} onChange={(e) => setInput(e.target.value)}
            placeholder="Ask, analyze, compare, or generate…"
            className="input flex-1 !py-3 !text-base" />
          <button className="btn !px-6" type="submit" disabled={!input.trim()}>Ask</button>
        </form>
        <div className="mt-4 flex flex-wrap gap-1.5 justify-center">
          {prompts.map((p) => (
            <button key={p} onClick={() => ask(p)}
              className="px-3 py-1.5 rounded-full text-xs bg-surface-overlay/60 text-slate-400 hover:text-slate-100 hover:bg-surface-overlay border border-surface-border">
              {p}
            </button>
          ))}
        </div>
      </div>

      {loading ? <Spinner label="Loading your workspace…" /> : (
        <div className="grid gap-4 lg:grid-cols-2 pb-8">
          <Section title="Recent conversations"
            action={<button className="text-xs text-accent" onClick={() => nav('/assistant')}>Open chat →</button>}>
            {convos.length === 0 ? <p className="text-xs text-slate-600 px-1 py-2">No conversations yet — ask something above.</p> : (
              <ul className="space-y-1">
                {convos.slice(0, 6).map((c) => (
                  <li key={c.conversation_id}>
                    <button onClick={() => nav('/assistant', { state: { open: c.conversation_id } })}
                      className="w-full text-left px-2 py-1.5 rounded hover:bg-surface-overlay/50 text-sm text-slate-300 truncate">
                      {c.pinned && '★ '}{c.title || 'Untitled'}
                    </button>
                  </li>
                ))}
              </ul>
            )}
          </Section>

          <Section title="Recent files"
            action={<button className="text-xs text-accent" onClick={() => nav('/files')}>Upload / view →</button>}>
            {files.length === 0 ? <p className="text-xs text-slate-600 px-1 py-2">No files yet — drop files on the Files page for instant AI understanding.</p> : (
              <ul className="space-y-1">
                {files.slice(0, 6).map((f) => (
                  <li key={f.id}>
                    <button onClick={() => nav('/files', { state: { open: f.id } })}
                      className="w-full text-left px-2 py-1.5 rounded hover:bg-surface-overlay/50 text-sm text-slate-300 flex items-center gap-2">
                      <Badge tone="info">{f.type}</Badge>
                      <span className="truncate flex-1">{f.file}</span>
                    </button>
                  </li>
                ))}
              </ul>
            )}
          </Section>

          <Section title="Recent reports"
            action={<button className="text-xs text-accent" onClick={() => nav('/reports')}>All reports →</button>}>
            {reports.length === 0 ? <p className="text-xs text-slate-600 px-1 py-2">No reports available.</p> : (
              <ul className="space-y-1">
                {reports.slice(0, 6).map((r, i) => (
                  <li key={i} className="px-2 py-1.5 text-sm text-slate-300 flex items-center gap-2">
                    <Badge tone="default">{r.category || 'report'}</Badge>
                    <span className="truncate">{r.title || r.id}</span>
                  </li>
                ))}
              </ul>
            )}
          </Section>

          <Section title="Recommendations"
            action={<button className="text-xs text-accent" onClick={() => nav('/evolution')}>Evolution →</button>}>
            {recs.length === 0 ? <p className="text-xs text-slate-600 px-1 py-2">No recommendations yet.</p> : (
              <ul className="space-y-1.5">
                {recs.slice(0, 4).map((r, i) => (
                  <li key={i} className="px-2 py-1.5 text-sm text-slate-300">
                    <span className="text-accent">→</span> {r.title || r.decision_id}
                    {r.business_value_cr != null && <span className="text-xs text-slate-500"> · ₹{r.business_value_cr}cr</span>}
                  </li>
                ))}
              </ul>
            )}
          </Section>

          {(pinned.length > 0 || artifacts.length > 0) && (
            <Section title="Pinned & generated">
              <div className="flex flex-wrap gap-2">
                {pinned.map((p) => (
                  <button key={p.id} onClick={() => p.link && nav(p.link)}
                    className="text-xs bg-surface px-2.5 py-1 rounded border border-surface-border text-slate-300 hover:border-accent/50">
                    📌 {p.title}
                  </button>
                ))}
                {artifacts.map((a) => (
                  <a key={a.file} href={api.artifactUrl(a.file)} target="_blank" rel="noreferrer"
                    className="text-xs bg-surface px-2.5 py-1 rounded border border-surface-border text-slate-300 hover:border-accent/50">
                    ⬇ {a.file}
                  </a>
                ))}
              </div>
            </Section>
          )}
        </div>
      )}
    </div>
  )
}
