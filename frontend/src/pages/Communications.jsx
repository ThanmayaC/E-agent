// Communications (Phase 2 #12/#13) — email as enterprise knowledge.
// Inbox messages arrive already analysed (category, entities, action items,
// decisions, deadlines, risks); an Analyze tab works on pasted email without a
// live provider; a Draft tab composes a grounded email from business context.
import { useState } from 'react'
import { api } from '../api/client'
import {
  AsyncSection, Badge, PageHeader, Tabs, severityTone, useAsync,
} from '../components/ui'

const CAT_TONE = {
  incident: 'danger', escalation: 'danger', risk_compliance: 'warn',
  approval: 'success', settlement: 'info', merchant: 'accent',
  report: 'info', meeting: 'default', general: 'default',
}

function EntityChips({ items = [] }) {
  if (!items.length) return null
  return (
    <div className="flex flex-wrap gap-1 mt-1.5">
      {items.map((e, i) => (
        <span key={i} className="text-[11px] px-1.5 py-0.5 rounded bg-surface-overlay text-slate-400">{e}</span>
      ))}
    </div>
  )
}

function Insight({ m }) {
  const rows = [
    ['Action items', m.action_items], ['Decisions', m.decisions],
    ['Blockers', m.blockers], ['Deadlines', m.deadlines], ['Risks', m.risks],
  ].filter(([, v]) => v && v.length)
  return (
    <div className="card-pad">
      <div className="flex items-center gap-2 flex-wrap">
        <Badge tone={CAT_TONE[m.category] || 'default'}>{(m.category || '').replace('_', ' ')}</Badge>
        <Badge tone={severityTone(m.priority)}>{m.priority} priority</Badge>
        {m.channel && <span className="text-[11px] text-slate-500">via {m.channel}</span>}
      </div>
      {m.subject && <div className="text-sm font-medium text-slate-200 mt-2">{m.subject}</div>}
      {m.sender && <div className="text-xs text-slate-500">{m.sender}{m.received ? ` · ${m.received}` : ''}</div>}
      <EntityChips items={m.entities} />
      {rows.map(([label, vals]) => (
        <div key={label} className="mt-2.5">
          <div className="text-[11px] uppercase tracking-wide text-slate-500">{label}</div>
          <ul className="mt-0.5 space-y-0.5">
            {vals.map((v, i) => <li key={i} className="text-sm text-slate-300">• {v}</li>)}
          </ul>
        </div>
      ))}
    </div>
  )
}

function Inbox() {
  const state = useAsync(() => api.commInbox(), [])
  return (
    <AsyncSection state={state} empty="Inbox is empty.">
      {(d) => !d.available ? (
        <div className="card-pad">
          <div className="text-sm text-slate-300">No email channel is configured yet.</div>
          <div className="text-xs text-slate-500 mt-1">{d.reason}</div>
          <div className="text-xs text-slate-500 mt-3">
            Once configured (Gmail or Outlook), every message is read as enterprise
            knowledge — categorised and linked to the banks, PSPs, products and
            incidents it mentions. Try the <b>Analyze</b> tab to see this on any email now.
          </div>
        </div>
      ) : (
        <div className="space-y-3">
          <div className="text-xs text-slate-500">{d.count} message(s) via {d.provider}</div>
          {d.messages.map((m, i) => <Insight key={m.email_id || i} m={m} />)}
        </div>
      )}
    </AsyncSection>
  )
}

const SAMPLE = `Escalation: PhonePe callback latency on State Bank of India (INC-2026-07)

Team, technical declines on UPI Autopay spiked this morning. Please hold an
incident bridge by EOD today and coordinate with the bank. We decided to fail
over to the backup route. Risk of an SLA breach if not contained.`

function Analyze() {
  const [text, setText] = useState(SAMPLE)
  const [result, setResult] = useState(null)
  const [busy, setBusy] = useState(false)
  const run = () => {
    const lines = text.split('\n')
    setBusy(true)
    api.commAnalyze({ subject: lines[0] || '', body: lines.slice(1).join('\n') })
      .then(setResult).catch(() => setResult(null)).finally(() => setBusy(false))
  }
  return (
    <div className="grid lg:grid-cols-2 gap-4">
      <div className="card-pad">
        <div className="text-sm font-medium text-slate-200 mb-2">Paste an email</div>
        <textarea className="input w-full h-56 font-mono !text-xs" value={text}
                  onChange={(e) => setText(e.target.value)} />
        <button className="btn mt-3" onClick={run} disabled={busy}>
          {busy ? 'Analyzing…' : 'Analyze'}
        </button>
      </div>
      <div>{result ? <Insight m={result} /> : <div className="card-pad text-sm text-slate-500">Extracted signal appears here.</div>}</div>
    </div>
  )
}

function Draft() {
  const [form, setForm] = useState({
    kind: 'incident_escalation', entity: 'UPI Autopay', recipient_name: 'Ops team',
    summary: 'Success rate dipped to 98.7% during the morning peak.',
    metrics: 'Success: 98.7%\nTechnical declines: 1.2%',
    actions: 'Hold incident bridge\nFail over to backup route',
    evidence: 'INC-2026-07, RPT-D07-DAILY', sender_name: 'Priya Nair',
    sender_title: 'Product Operations',
  })
  const [draft, setDraft] = useState(null)
  const [busy, setBusy] = useState(false)
  const set = (k) => (e) => setForm({ ...form, [k]: e.target.value })
  const run = () => {
    setBusy(true)
    api.commDraft(form.kind, {
      entity: form.entity, recipient_name: form.recipient_name, summary: form.summary,
      metrics: form.metrics.split('\n').filter(Boolean),
      actions: form.actions.split('\n').filter(Boolean),
      evidence: form.evidence.split(',').map((s) => s.trim()).filter(Boolean),
      sender_name: form.sender_name, sender_title: form.sender_title,
    }).then(setDraft).catch(() => setDraft(null)).finally(() => setBusy(false))
  }
  const KINDS = ['incident_escalation', 'merchant_followup', 'management_update',
    'risk_notification', 'weekly_status', 'meeting_followup']
  return (
    <div className="grid lg:grid-cols-2 gap-4">
      <div className="card-pad space-y-2.5">
        <div className="text-sm font-medium text-slate-200">Draft from business context</div>
        <select className="input w-full" value={form.kind} onChange={set('kind')}>
          {KINDS.map((k) => <option key={k} value={k}>{k.replace(/_/g, ' ')}</option>)}
        </select>
        <input className="input w-full" placeholder="Entity" value={form.entity} onChange={set('entity')} />
        <input className="input w-full" placeholder="Recipient" value={form.recipient_name} onChange={set('recipient_name')} />
        <textarea className="input w-full h-14" placeholder="Summary" value={form.summary} onChange={set('summary')} />
        <textarea className="input w-full h-14" placeholder="Metrics (one per line)" value={form.metrics} onChange={set('metrics')} />
        <textarea className="input w-full h-14" placeholder="Actions (one per line)" value={form.actions} onChange={set('actions')} />
        <input className="input w-full" placeholder="Evidence (comma separated)" value={form.evidence} onChange={set('evidence')} />
        <button className="btn" onClick={run} disabled={busy}>{busy ? 'Drafting…' : 'Generate draft'}</button>
      </div>
      <div className="card-pad">
        {draft ? (
          <>
            <div className="text-[11px] uppercase tracking-wide text-slate-500">Subject</div>
            <div className="text-sm font-medium text-slate-200 mb-2">{draft.subject}</div>
            <pre className="text-sm text-slate-300 whitespace-pre-wrap font-sans">{draft.body}</pre>
            {draft.grounded_in?.length > 0 && (
              <div className="text-xs text-slate-500 mt-3">Grounded in: {draft.grounded_in.join(', ')}</div>
            )}
            <div className="text-[11px] text-slate-500 mt-2">Draft only — an actual send goes through approval.</div>
          </>
        ) : <div className="text-sm text-slate-500">The grounded draft appears here.</div>}
      </div>
    </div>
  )
}

export default function Communications() {
  const [tab, setTab] = useState('inbox')
  const providers = useAsync(() => api.commProviders(), [])
  return (
    <>
      <PageHeader title="Communications" subtitle="Email as enterprise knowledge — read, analysed, drafted from real business context" />
      <AsyncSection state={providers} empty="">
        {(d) => {
          const channels = (d.providers || []).filter((p) => ['email', 'messaging'].includes(p.kind))
          return (
            <div className="flex flex-wrap gap-2 mb-4">
              {channels.map((p, i) => (
                <span key={i} className="inline-flex items-center gap-1.5 text-xs px-2.5 py-1 rounded-lg bg-surface-raised border border-surface-border">
                  <span className={`w-1.5 h-1.5 rounded-full ${p.available ? 'bg-emerald-400' : 'bg-slate-500'}`} />
                  {p.name} <span className="text-slate-500">{p.available ? 'connected' : 'not configured'}</span>
                </span>
              ))}
            </div>
          )
        }}
      </AsyncSection>
      <Tabs active={tab} onChange={setTab}
            tabs={[{ value: 'inbox', label: 'Inbox' }, { value: 'analyze', label: 'Analyze' }, { value: 'draft', label: 'Draft' }]} />
      <div className="mt-4">
        {tab === 'inbox' && <Inbox />}
        {tab === 'analyze' && <Analyze />}
        {tab === 'draft' && <Draft />}
      </div>
    </>
  )
}
