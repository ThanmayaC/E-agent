// One business's executive report, rendered for reading, export and — Phase 2
// #16 — interaction: discuss it with the AI, or generate a grounded email from
// it (composed from the report's own summary + reference id, never generic).
import { useMemo, useState } from 'react'
import { Link, useNavigate, useParams } from 'react-router-dom'
import { api } from '../api/client'
import { AsyncSection, PageHeader, useAsync } from '../components/ui'
import MarkdownLite from '../components/MarkdownLite'

// Pull a title and the first substantive paragraph out of the report markdown
// so a generated email is grounded in what the report actually says.
function summarize(md = '') {
  const lines = md.split('\n')
  const title = (lines.find((l) => l.startsWith('# ')) || '').replace(/^#\s*/, '').trim()
  const para = lines.find((l) => l.trim() && !l.startsWith('#') && !l.startsWith('|') && !l.startsWith('-'))
  return { title: title || 'Executive report', summary: (para || '').trim() }
}

export default function ReportView() {
  const { projectId } = useParams()
  const navigate = useNavigate()
  const state = useAsync(() => api.reportMarkdown(projectId), [projectId])
  const [draft, setDraft] = useState(null)
  const [busy, setBusy] = useState(false)

  const meta = useMemo(() => summarize(state.data?.markdown), [state.data])

  function download(md) {
    const blob = new Blob([md], { type: 'text/markdown' })
    const a = document.createElement('a')
    a.href = URL.createObjectURL(blob)
    a.download = `executive-report-${projectId}.md`
    a.click()
    URL.revokeObjectURL(a.href)
  }

  function generateEmail() {
    setBusy(true)
    api.commDraft('management_update', {
      entity: meta.title, recipient_name: 'Leadership',
      summary: meta.summary, evidence: [String(projectId)],
      sender_name: 'Product Operations',
    }).then(setDraft).catch(() => setDraft(null)).finally(() => setBusy(false))
  }

  function discuss() {
    navigate(`/assistant?q=${encodeURIComponent(`Discuss this report: ${meta.title}`)}`)
  }

  return (
    <>
      <div className="text-xs text-slate-500 mb-3">
        <Link to="/reports" className="hover:text-accent">Reports</Link> <span className="mx-1">/</span> Executive report
      </div>
      <AsyncSection state={state} empty="This report is not ready yet — it appears once the analysis completes.">
        {(d) => (
          <>
            <PageHeader title="Executive Report"
                        subtitle="Summary → KPIs → Insights → Root cause → Risks → Forecasts → Recommendations">
              <button className="btn-ghost" onClick={discuss}>💬 Discuss</button>
              <button className="btn-ghost" onClick={generateEmail} disabled={busy}>
                {busy ? 'Drafting…' : '✉ Generate email'}
              </button>
              <button className="btn" onClick={() => download(d.markdown)}>Export .md</button>
            </PageHeader>
            {draft && (
              <div className="card-pad max-w-5xl mb-4 border-accent/40">
                <div className="flex items-center justify-between mb-2">
                  <div className="text-sm font-medium text-slate-200">Draft email (grounded in this report)</div>
                  <button className="btn-quiet" onClick={() => setDraft(null)}>Dismiss</button>
                </div>
                <div className="text-[11px] uppercase tracking-wide text-slate-500">Subject</div>
                <div className="text-sm font-medium text-slate-200 mb-2">{draft.subject}</div>
                <pre className="text-sm text-slate-300 whitespace-pre-wrap font-sans">{draft.body}</pre>
                <div className="text-[11px] text-slate-500 mt-2">Draft only — an actual send goes through approval.</div>
              </div>
            )}
            <div className="card-pad max-w-5xl">
              <MarkdownLite text={d.markdown} />
            </div>
          </>
        )}
      </AsyncSection>
    </>
  )
}
