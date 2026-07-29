// Decisions — the decision log. A simple table (Decision/Status/Owner/Date/
// Business Impact); clicking a row explains the problem, evidence,
// alternatives considered, why this decision, expected vs. actual outcome,
// and the supporting reports/meetings/RCAs/SOPs.
import { useMemo, useState } from 'react'
import { api } from '../api/client'
import { AsyncSection, Badge, PageHeader, PanelEmpty, Tabs, useAsync, when } from '../components/ui'

const TONE = { proposed: 'warn', approved: 'success', executed: 'success', rejected: 'danger' }

function DecisionDetail({ d, onClose }) {
  return (
    <div className="fixed inset-0 z-50 flex justify-end bg-black/50" onClick={onClose}>
      <div className="w-full max-w-xl h-full bg-surface-raised border-l border-surface-border overflow-y-auto p-6"
           onClick={(e) => e.stopPropagation()}>
        <div className="flex items-start justify-between gap-3">
          <div>
            <Badge tone={TONE[d.status] || 'default'}>{d.status}</Badge>
            <h2 className="text-lg font-bold text-slate-100 mt-2">{d.title}</h2>
            <div className="text-xs text-slate-500 mt-1">
              {d.owner} · {when(d.timestamp)} · rank #{d.rank}
            </div>
          </div>
          <button onClick={onClose} className="text-slate-500 hover:text-slate-200">✕</button>
        </div>

        <section className="mt-5">
          <div className="h-sub mb-1.5">Problem</div>
          <p className="text-sm text-slate-300 leading-relaxed">{d.problem}</p>
        </section>

        <section className="mt-5">
          <div className="h-sub mb-1.5">Evidence</div>
          <ul className="text-xs text-slate-500 space-y-1">
            {(d.evidence || []).map((e) => <li key={e}>• {e}</li>)}
          </ul>
        </section>

        <section className="mt-5">
          <div className="h-sub mb-1.5">Alternatives Considered</div>
          <ul className="text-sm text-slate-300 space-y-1.5 list-disc list-inside">
            {(d.alternatives_considered || []).map((a, i) => <li key={i}>{a}</li>)}
          </ul>
        </section>

        <section className="mt-5">
          <div className="h-sub mb-1.5">Why This Decision</div>
          <p className="text-sm text-slate-300 leading-relaxed">{d.reason_selected}</p>
        </section>

        <div className="grid grid-cols-2 gap-4 mt-5">
          <section>
            <div className="h-sub mb-1.5">Expected Outcome</div>
            <p className="text-sm text-slate-300 leading-relaxed">{d.expected_impact}</p>
          </section>
          <section>
            <div className="h-sub mb-1.5">Actual Outcome</div>
            <p className="text-sm text-slate-300 leading-relaxed">{d.actual_impact}</p>
          </section>
        </div>

        <section className="mt-5">
          <div className="h-sub mb-1.5">Business Value</div>
          <p className="text-sm text-slate-300 leading-relaxed">{d.business_value}</p>
        </section>

        {(d.affected_products?.length > 0 || d.affected_banks?.length > 0 || d.affected_merchants?.length > 0) && (
          <section className="mt-5">
            <div className="h-sub mb-1.5">Related Products / Banks / Merchants</div>
            <div className="flex flex-wrap gap-1.5">
              {(d.affected_products || []).map((x) => <Badge key={x} tone="accent">{x}</Badge>)}
              {(d.affected_banks || []).map((x) => <Badge key={x} tone="info">{x}</Badge>)}
              {(d.affected_merchants || []).map((x) => <Badge key={x}>{x}</Badge>)}
            </div>
          </section>
        )}
      </div>
    </div>
  )
}

export default function Decisions() {
  const [refresh, setRefresh] = useState(0)
  const [tab, setTab] = useState('all')
  const [selected, setSelected] = useState(null)
  const state = useAsync(() => api.executiveDecisions().catch(() => ({ decisions: [] })), [refresh])

  return (
    <>
      <PageHeader title="Decisions" subtitle="Every strategic decision — problem, evidence, alternatives, and outcome" />
      <AsyncSection state={state} empty="No decisions recorded yet.">
        {({ decisions }) => (
          <DecisionTable decisions={decisions || []} tab={tab} setTab={setTab} selected={selected} setSelected={setSelected} />
        )}
      </AsyncSection>
    </>
  )
}

function DecisionTable({ decisions, tab, setTab, selected, setSelected }) {
  const filtered = useMemo(
    () => (tab === 'all' ? decisions : decisions.filter((d) => (d.status || '').toLowerCase() === tab)),
    [decisions, tab],
  )
  const count = (s) => decisions.filter((d) => (d.status || '').toLowerCase() === s).length
  const tabs = [
    { value: 'all', label: 'All', count: decisions.length },
    { value: 'proposed', label: 'Proposed', count: count('proposed') },
    { value: 'approved', label: 'Approved', count: count('approved') },
    { value: 'executed', label: 'Executed', count: count('executed') },
  ]

  return (
    <div className="space-y-4">
      <Tabs tabs={tabs} active={tab} onChange={setTab} />
      {filtered.length === 0 ? <PanelEmpty text="No decisions in this view." /> : (
        <div className="card overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="text-left text-xs text-slate-500 border-b border-surface-border">
                <th className="px-4 py-3 font-medium">Decision</th>
                <th className="px-4 py-3 font-medium">Status</th>
                <th className="px-4 py-3 font-medium">Owner</th>
                <th className="px-4 py-3 font-medium">Date</th>
                <th className="px-4 py-3 font-medium">Business Impact</th>
              </tr>
            </thead>
            <tbody>
              {filtered.map((d) => (
                <tr key={d.decision_id} onClick={() => setSelected(d)}
                    className="border-b border-surface-border/50 last:border-0 hover:bg-surface-overlay/40 cursor-pointer">
                  <td className="px-4 py-3 text-slate-200 max-w-sm truncate">{d.title}</td>
                  <td className="px-4 py-3"><Badge tone={TONE[d.status] || 'default'}>{d.status}</Badge></td>
                  <td className="px-4 py-3 text-slate-400">{d.owner}</td>
                  <td className="px-4 py-3 text-slate-500">{when(d.timestamp)}</td>
                  <td className="px-4 py-3 text-slate-400 tabular-nums">{d.impact?.business ?? '—'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
      {selected && <DecisionDetail d={selected} onClose={() => setSelected(null)} />}
    </div>
  )
}
