// Decisions — the strategic decision log: propose, approve, implement,
// and keep the record of why.
import { useMemo, useState } from 'react'
import { api } from '../api/client'
import {
  AsyncSection, Badge, PageHeader, PanelEmpty, Tabs, useAsync, when,
} from '../components/ui'

const TONE = { proposed: 'warn', approved: 'success', rejected: 'danger', implemented: 'info', superseded: 'default' }
const NEXT = {
  proposed: [['approved', 'Approve'], ['rejected', 'Reject']],
  approved: [['implemented', 'Mark implemented'], ['superseded', 'Supersede']],
  rejected: [['proposed', 'Re-propose']],
  implemented: [],
  superseded: [],
}

export default function Decisions() {
  const [refresh, setRefresh] = useState(0)
  const [tab, setTab] = useState('all')
  const [form, setForm] = useState({ decision: '', impact: '', context: '' })
  const [error, setError] = useState('')
  const state = useAsync(() => api.managerDecisions(), [refresh])
  const reload = () => setRefresh((n) => n + 1)

  const move = (id, status) => {
    setError('')
    api.setDecisionStatus(id, status, 'executive').then(reload).catch((e) => setError(String(e.message || e)))
  }
  const record = (e) => {
    e.preventDefault()
    if (!form.decision.trim()) return
    setError('')
    api.recordDecision({ ...form, decision: form.decision.trim(), owner: 'executive' })
      .then(() => { setForm({ decision: '', impact: '', context: '' }); reload() })
      .catch((err) => setError(String(err.message || err)))
  }

  return (
    <>
      <PageHeader title="Decisions" subtitle="Strategic decisions with their status, impact, and history" />
      {error && <div className="card-pad border-rose-500/40 text-rose-300 text-sm mb-4">{error}</div>}
      <AsyncSection state={state} empty="No decisions recorded yet.">
        {({ decisions, stats }) => (
          <DecisionList decisions={decisions || []} stats={stats || {}} tab={tab} setTab={setTab}
                        form={form} setForm={setForm} record={record} move={move} />
        )}
      </AsyncSection>
    </>
  )
}

function DecisionList({ decisions, stats, tab, setTab, form, setForm, record, move }) {
  const filtered = useMemo(
    () => (tab === 'all' ? decisions : decisions.filter((d) => d.status === tab)),
    [decisions, tab],
  )
  const tabs = [
    { value: 'all', label: 'All', count: decisions.length },
    { value: 'proposed', label: 'Awaiting decision', count: stats.proposed || 0 },
    { value: 'approved', label: 'Approved', count: stats.approved || 0 },
    { value: 'implemented', label: 'Implemented', count: stats.implemented || 0 },
  ]

  return (
    <div className="space-y-5">
      <section className="card-pad">
        <div className="h-sub mb-3">Record a decision</div>
        <form className="grid gap-2 md:grid-cols-[2fr,1fr,1fr,auto]" onSubmit={record}>
          <input className="input" placeholder="The decision, e.g. Expand Autopay to SME merchants"
                 value={form.decision} onChange={(e) => setForm((f) => ({ ...f, decision: e.target.value }))} />
          <input className="input" placeholder="Expected impact (optional)"
                 value={form.impact} onChange={(e) => setForm((f) => ({ ...f, impact: e.target.value }))} />
          <input className="input" placeholder="Context (optional)"
                 value={form.context} onChange={(e) => setForm((f) => ({ ...f, context: e.target.value }))} />
          <button className="btn" type="submit" disabled={!form.decision.trim()}>Record</button>
        </form>
      </section>

      <Tabs tabs={tabs} active={tab} onChange={setTab} />
      {filtered.length === 0 ? <PanelEmpty text="No decisions in this view." /> : (
        <div className="space-y-3">
          {filtered.map((d) => (
            <section key={d.decision_id} className="card-pad">
              <div className="flex items-start justify-between gap-4 flex-wrap">
                <div className="min-w-0">
                  <div className="text-sm text-slate-200 font-medium">
                    <Badge tone={TONE[d.status] || 'default'}>{d.status}</Badge> {d.decision}
                  </div>
                  <div className="text-xs text-slate-500 mt-1.5 space-x-2">
                    {d.owner && <span>owner: {d.owner}</span>}
                    {d.impact && <span>· impact: {d.impact}</span>}
                    {d.context && <span>· {d.context}</span>}
                    {(d.recorded_at || d.created_at) && <span>· {when(d.recorded_at || d.created_at)}</span>}
                  </div>
                </div>
                <div className="flex gap-2 shrink-0">
                  {(NEXT[d.status] || []).map(([status, label]) => (
                    <button key={status} onClick={() => move(d.decision_id, status)}
                            className={`px-2.5 py-1 rounded-md text-xs ${
                              status === 'approved' ? 'bg-emerald-500/15 text-emerald-400 hover:bg-emerald-500/25'
                              : status === 'rejected' ? 'bg-rose-500/15 text-rose-400 hover:bg-rose-500/25'
                              : 'bg-surface-overlay text-slate-300 hover:bg-surface-overlay/70'}`}>
                      {label}
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
