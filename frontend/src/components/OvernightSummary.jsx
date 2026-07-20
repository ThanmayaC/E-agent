// Overnight Summary (V2) — what the platform did autonomously: workflows
// completed, actions executed, drafts awaiting approval (approve / edit /
// reject inline), new reports and notifications since the cutoff.
import { useState } from 'react'
import { api } from '../api/client'
import { Badge, Panel, PanelEmpty, timeAgo, useAsync } from './ui'

const KIND_LABEL = {
  send_email: 'email draft', send_message: 'Teams draft',
  create_meeting: 'meeting', update_business_rule: 'rule change',
  execute_automation: 'automation', generate_report: 'report',
}

function DraftEditor({ action, onDone, onCancel }) {
  const payload = action.payload || {}
  const isEmail = action.kind === 'send_email'
  const [to, setTo] = useState((payload.to || []).join(', '))
  const [subject, setSubject] = useState(payload.subject || '')
  const [text, setText] = useState(isEmail ? (payload.body || '') : (payload.text || ''))
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState('')

  const save = async () => {
    setSaving(true)
    setError('')
    try {
      const changes = isEmail
        ? { payload: { to: to.split(',').map((s) => s.trim()).filter(Boolean), subject, body: text } }
        : { payload: { text } }
      await api.editAction(action.action_id, changes, 'executive')
      onDone()
    } catch (e) {
      setError(String(e.message || e))
      setSaving(false)
    }
  }

  return (
    <div className="mt-3 space-y-2 border-t border-surface-border pt-3">
      {isEmail && (
        <>
          <input className="input !py-1.5 text-sm" placeholder="Recipients, comma-separated"
                 value={to} onChange={(e) => setTo(e.target.value)} />
          <input className="input !py-1.5 text-sm" placeholder="Subject"
                 value={subject} onChange={(e) => setSubject(e.target.value)} />
        </>
      )}
      <textarea className="input text-sm h-28" value={text}
                onChange={(e) => setText(e.target.value)} />
      {error && <div className="text-xs text-rose-400">{error}</div>}
      <div className="flex gap-2">
        <button onClick={save} disabled={saving} className="btn !py-1 !text-xs">
          {saving ? 'Saving…' : 'Save changes'}
        </button>
        <button onClick={onCancel} className="btn-ghost !py-1 !text-xs">Cancel</button>
      </div>
    </div>
  )
}

function DraftRow({ action, reload }) {
  const [editing, setEditing] = useState(false)
  const approve = () => api.approveAction(action.action_id, 'executive').then(reload)
  const reject = () => api.rejectAction(action.action_id, 'executive', 'rejected from overnight summary').then(reload)
  const payload = action.payload || {}
  const preview = payload.body || payload.text || action.detail || ''

  return (
    <li className="py-2.5 first:pt-0 last:pb-0">
      <div className="flex items-start justify-between gap-3 text-sm">
        <div className="min-w-0">
          <div className="text-slate-200">
            <Badge tone="warn">{KIND_LABEL[action.kind] || action.kind.replace(/_/g, ' ')}</Badge>{' '}
            {action.title}
          </div>
          {preview && !editing && (
            <div className="text-xs text-slate-500 mt-1 line-clamp-2 whitespace-pre-line">{preview}</div>
          )}
        </div>
        <span className="shrink-0 space-x-2.5 text-xs">
          <button onClick={approve} className="text-emerald-400 hover:underline">Approve</button>
          <button onClick={() => setEditing((v) => !v)} className="text-accent hover:underline">
            {editing ? 'Close' : 'Edit'}
          </button>
          <button onClick={reject} className="text-slate-500 hover:underline">Reject</button>
        </span>
      </div>
      {editing && <DraftEditor action={action} onDone={() => { setEditing(false); reload() }}
                               onCancel={() => setEditing(false)} />}
    </li>
  )
}

export default function OvernightSummary() {
  const [refresh, setRefresh] = useState(0)
  const state = useAsync(() => api.overnightSummary(), [refresh])
  const reload = () => setRefresh((n) => n + 1)

  if (state.loading || state.error || !state.data) return null
  const s = state.data
  const totals = s.totals || {}
  const quiet = !totals.workflows && !totals.actions_executed
    && !totals.awaiting_approval && !totals.reports

  return (
    <Panel title="Overnight summary"
           action={<span className="text-xs text-slate-600">last {s.hours}h · autonomous</span>}>
      {quiet ? (
        <PanelEmpty text="A quiet night — nothing ran, nothing is waiting on you." />
      ) : (
        <div className="grid gap-5 lg:grid-cols-2">
          <div>
            <div className="h-sub mb-2">
              Awaiting your approval
              {totals.awaiting_approval > 0 && (
                <span className="ml-2 text-amber-400">{totals.awaiting_approval}</span>
              )}
            </div>
            {(s.awaiting_approval || []).length === 0
              ? <PanelEmpty text="Nothing to approve." />
              : <ul className="divide-y divide-surface-border">
                  {s.awaiting_approval.map((a) => (
                    <DraftRow key={a.action_id} action={a} reload={reload} />
                  ))}
                </ul>}
          </div>
          <div className="space-y-4">
            <div>
              <div className="h-sub mb-2">Completed while you were away</div>
              {(s.workflows_completed || []).length === 0 && (s.actions_executed || []).length === 0
                ? <PanelEmpty text="No autonomous work in this window." />
                : <ul className="space-y-1.5 text-sm text-slate-300">
                    {(s.workflows_completed || []).slice(0, 5).map((w, i) => (
                      <li key={`w${i}`} className="flex justify-between gap-3">
                        <span className="truncate">{w.workflow.replace(/_/g, ' ')}</span>
                        <span className="text-xs text-slate-600 shrink-0">
                          {w.status} {w.finished_at && `· ${timeAgo(w.finished_at)}`}
                        </span>
                      </li>
                    ))}
                    {(s.actions_executed || []).slice(0, 4).map((a, i) => (
                      <li key={`a${i}`} className="flex justify-between gap-3">
                        <span className="truncate">{a.title}</span>
                        <span className="text-xs text-slate-600 shrink-0">{timeAgo(a.executed_at)}</span>
                      </li>
                    ))}
                  </ul>}
            </div>
            {(s.new_reports || []).length > 0 && (
              <div>
                <div className="h-sub mb-2">New reports</div>
                <ul className="space-y-1.5 text-sm text-slate-300">
                  {s.new_reports.slice(0, 4).map((r, i) => (
                    <li key={i} className="truncate">{r.title}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        </div>
      )}
    </Panel>
  )
}
