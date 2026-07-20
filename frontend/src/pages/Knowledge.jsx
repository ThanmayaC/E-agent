import { useState } from 'react'
import { api } from '../api/client'
import { AsyncSection, Badge, Empty, PageHeader, useAsync } from '../components/ui'

// Knowledge Explorer — browse and grow the enterprise's persistent knowledge:
// terminology, business rules, and clarifications. Everything taught here is
// injected into future AI reasoning, so the platform gets smarter over time.
export default function Knowledge() {
  const [refresh, setRefresh] = useState(0)
  const state = useAsync(() => api.knowledge(), [refresh])
  const bump = () => setRefresh((n) => n + 1)

  return (
    <>
      <PageHeader
        title="Knowledge Explorer"
        subtitle="Organization-wide memory: terminology, rules, clarifications, and history the AI learns from"
      />
      <div className="space-y-5">
        <div className="grid lg:grid-cols-2 gap-5">
          <TeachTermCard onSaved={bump} />
          <TeachRuleCard onSaved={bump} />
        </div>
        <AsyncSection state={state} empty="No enterprise knowledge yet — teach a term or rule above.">
          {(k) => <KnowledgeSections k={k} />}
        </AsyncSection>
      </div>
    </>
  )
}

function TeachTermCard({ onSaved }) {
  const [term, setTerm] = useState('')
  const [definition, setDefinition] = useState('')
  const [aliases, setAliases] = useState('')
  const [busy, setBusy] = useState(false)
  const submit = async (e) => {
    e.preventDefault()
    if (!term.trim() || !definition.trim()) return
    setBusy(true)
    try {
      await api.addTerm(term.trim(), definition.trim(),
        aliases.split(',').map((a) => a.trim()).filter(Boolean))
      setTerm(''); setDefinition(''); setAliases('')
      onSaved()
    } finally { setBusy(false) }
  }
  return (
    <form onSubmit={submit} className="card-pad space-y-3">
      <div className="h-title">Teach a business term</div>
      <input className="input w-full" placeholder="Term (e.g. GMV)" value={term}
             onChange={(e) => setTerm(e.target.value)} />
      <input className="input w-full" placeholder="Definition" value={definition}
             onChange={(e) => setDefinition(e.target.value)} />
      <input className="input w-full" placeholder="Aliases, comma-separated (optional)" value={aliases}
             onChange={(e) => setAliases(e.target.value)} />
      <button className="btn" disabled={busy || !term.trim() || !definition.trim()}>
        {busy ? 'Saving…' : 'Add to enterprise knowledge'}
      </button>
    </form>
  )
}

function TeachRuleCard({ onSaved }) {
  const [rule, setRule] = useState('')
  const [busy, setBusy] = useState(false)
  const submit = async (e) => {
    e.preventDefault()
    if (!rule.trim()) return
    setBusy(true)
    try {
      await api.addRule(rule.trim())
      setRule('')
      onSaved()
    } finally { setBusy(false) }
  }
  return (
    <form onSubmit={submit} className="card-pad space-y-3">
      <div className="h-title">Teach a business rule</div>
      <textarea className="input w-full h-[104px] resize-none"
                placeholder='e.g. "Fiscal year starts in April" or "Exclude test merchants from revenue"'
                value={rule} onChange={(e) => setRule(e.target.value)} />
      <button className="btn" disabled={busy || !rule.trim()}>
        {busy ? 'Saving…' : 'Add rule'}
      </button>
    </form>
  )
}

function KnowledgeSections({ k }) {
  const terms = Object.values(k.terminology || {})
  const rules = k.business_rules || []
  const clarifications = k.clarifications || []
  const reports = k.report_history || []
  return (
    <div className="space-y-5">
      <div className="card-pad">
        <div className="h-title mb-3">Terminology <Badge>{terms.length}</Badge></div>
        {terms.length === 0 ? <Empty title="No terms taught yet" /> : (
          <table className="table-base">
            <thead><tr><th>Term</th><th>Definition</th><th>Aliases</th><th>Added</th></tr></thead>
            <tbody>
              {terms.map((t) => (
                <tr key={t.term}>
                  <td className="text-slate-200 font-medium">{t.term}</td>
                  <td className="text-slate-400">{t.definition}</td>
                  <td className="text-slate-500">{(t.aliases || []).join(', ') || '—'}</td>
                  <td className="text-slate-500 text-xs">{t.added_at ? new Date(t.added_at).toLocaleDateString() : '—'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>

      <div className="grid lg:grid-cols-2 gap-5">
        <div className="card-pad">
          <div className="h-title mb-3">Business rules <Badge>{rules.length}</Badge></div>
          {rules.length === 0 ? <Empty title="No rules yet" /> : (
            <ul className="space-y-2 text-sm">
              {rules.map((r, i) => (
                <li key={i} className="flex justify-between gap-3 py-1.5 px-2 rounded hover:bg-surface-overlay/40">
                  <span className="text-slate-300">{r.rule}</span>
                  <Badge>{r.scope}</Badge>
                </li>
              ))}
            </ul>
          )}
        </div>
        <div className="card-pad">
          <div className="h-title mb-3">Clarifications learned <Badge>{clarifications.length}</Badge></div>
          {clarifications.length === 0 ? (
            <Empty title="None yet" hint="Answers you give to AI clarification questions are remembered here and never asked again." />
          ) : (
            <ul className="space-y-3 text-sm">
              {clarifications.map((c, i) => (
                <li key={i} className="border-l-2 border-accent/40 pl-3">
                  <div className="text-slate-400">{c.question}</div>
                  <div className="text-slate-200 mt-0.5">{c.answer}</div>
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>

      <div className="card-pad">
        <div className="h-title mb-3">Report history <Badge>{reports.length}</Badge></div>
        {reports.length === 0 ? <Empty title="No reports recorded yet" /> : (
          <table className="table-base">
            <thead><tr><th>Project</th><th>Title</th><th>Health score</th><th>Generated</th></tr></thead>
            <tbody>
              {reports.slice().reverse().map((r, i) => (
                <tr key={i}>
                  <td className="font-mono text-xs text-slate-400">{r.project_id}</td>
                  <td className="text-slate-200">{r.title}</td>
                  <td>{Number(r.health_score).toFixed(0)}</td>
                  <td className="text-slate-500 text-xs">{new Date(r.generated_at).toLocaleString()}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  )
}
