// Report Center — every generated report: review queue, approvals, search,
// filters, and export.
import { useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import { api } from '../api/client'
import {
  AsyncSection, Badge, PageHeader, PanelEmpty, Tabs, healthTone, useAsync,
} from '../components/ui'

const TONE = { draft: 'default', review: 'warn', approved: 'success', rejected: 'danger', archived: 'default' }
const ACTIONS = {
  draft: ['review', 'archived'],
  review: ['approved', 'rejected', 'archived'],
  approved: ['archived'],
  rejected: ['review', 'archived'],
  archived: [],
}
const ACTION_LABEL = { review: 'Send to review', approved: 'Approve', rejected: 'Reject', archived: 'Archive' }

async function exportReport(projectId, title) {
  const d = await api.reportMarkdown(projectId)
  const blob = new Blob([d.markdown], { type: 'text/markdown' })
  const a = document.createElement('a')
  a.href = URL.createObjectURL(blob)
  a.download = `${(title || `report-${projectId}`).replace(/[^\w\- ]+/g, '').trim() || 'report'}.md`
  a.click()
  URL.revokeObjectURL(a.href)
}

export default function ReportCenter() {
  const [refresh, setRefresh] = useState(0)
  const [tab, setTab] = useState('all')
  const [q, setQ] = useState('')
  const [error, setError] = useState('')
  const state = useAsync(() => api.reportReviews(), [refresh])

  const move = (id, status) => {
    setError('')
    api.setReviewStatus(id, status, 'executive')
      .then(() => setRefresh((n) => n + 1))
      .catch((e) => setError(String(e.message || e)))
  }

  return (
    <>
      <PageHeader title="Reports" subtitle="Every generated report — review, approve, and export" />
      {error && <div className="card-pad border-rose-500/40 text-rose-300 text-sm mb-4">{error}</div>}
      <AsyncSection state={state} empty="No reports yet — they appear as soon as an analysis completes.">
        {({ reviews, stats }) => (
          <ReportList reviews={reviews} stats={stats} tab={tab} setTab={setTab} q={q} setQ={setQ} move={move} />
        )}
      </AsyncSection>
    </>
  )
}

function ReportList({ reviews, stats, tab, setTab, q, setQ, move }) {
  const filtered = useMemo(() => {
    let list = reviews
    if (tab === 'pending') list = list.filter((r) => r.status === 'review' || r.status === 'draft')
    else if (tab !== 'all') list = list.filter((r) => r.status === tab)
    const needle = q.trim().toLowerCase()
    if (needle) list = list.filter((r) => (r.title || '').toLowerCase().includes(needle))
    return list
  }, [reviews, tab, q])

  const pending = (stats?.review || 0) + (stats?.draft || 0)
  const tabs = [
    { value: 'all', label: 'All', count: reviews.length },
    { value: 'pending', label: 'Pending review', count: pending },
    { value: 'approved', label: 'Approved', count: stats?.approved || 0 },
    { value: 'rejected', label: 'Rejected', count: stats?.rejected || 0 },
    { value: 'archived', label: 'Archived', count: stats?.archived || 0 },
  ]

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between gap-4 flex-wrap">
        <input className="input max-w-xs" placeholder="Search reports…" value={q} onChange={(e) => setQ(e.target.value)} />
      </div>
      <Tabs tabs={tabs} active={tab} onChange={setTab} />
      {filtered.length === 0 ? <PanelEmpty text="No reports match." /> : (
        <div className="space-y-3">
          {filtered.map((r) => (
            <section key={r.review_id} className="card-pad card-hover">
              <div className="flex items-start justify-between gap-4 flex-wrap">
                <div className="min-w-0">
                  <div className="text-sm text-slate-200 font-medium">
                    <Link className="hover:text-accent" to={`/reports/${r.project_id}`}>{r.title}</Link>{' '}
                    <Badge tone={TONE[r.status]}>{r.status}</Badge>
                  </div>
                  <div className="text-xs text-slate-500 mt-1">
                    {r.health_score != null && (
                      <span className={healthTone(r.health_score)}>health {Math.round(r.health_score)} · </span>
                    )}
                    {(r.history || []).map((h) => `${h.status}${h.by ? ` (${h.by})` : ''}`).join(' → ')}
                  </div>
                </div>
                <div className="flex gap-2 items-center shrink-0">
                  <button onClick={() => exportReport(r.project_id, r.title)}
                          className="px-2.5 py-1 rounded-md text-xs bg-surface-overlay text-slate-300 hover:bg-surface-overlay/70">
                    Export
                  </button>
                  {(ACTIONS[r.status] || []).map((next) => (
                    <button key={next} onClick={() => move(r.review_id, next)}
                            className={`px-2.5 py-1 rounded-md text-xs ${
                              next === 'approved' ? 'bg-emerald-500/15 text-emerald-400 hover:bg-emerald-500/25'
                              : next === 'rejected' ? 'bg-rose-500/15 text-rose-400 hover:bg-rose-500/25'
                              : 'bg-surface-overlay text-slate-300 hover:bg-surface-overlay/70'}`}>
                      {r.status === 'rejected' && next === 'review' ? 'Re-open review' : ACTION_LABEL[next]}
                    </button>
                  ))}
                </div>
              </div>
            </section>
          ))}
        </div>
      )}
    </div>
  )
}
