import { useParams } from 'react-router-dom'
import { motion } from 'framer-motion'
import { api } from '../api/client'
import { AsyncSection, Badge, PageHeader, severityTone, useAsync } from '../components/ui'
import { AIStatus } from '../components/AIBadge'

const SIGNAL_TONE = {
  trend: 'info', anomaly: 'danger', seasonality: 'accent',
  concentration: 'warn', correlation: 'success', inverse_correlation: 'danger',
}

// every AI statement is labelled: FACT / STATISTICAL / HYPOTHESIS / UNKNOWN
const STATEMENT_TONE = { fact: 'success', statistical_finding: 'info', hypothesis: 'warn', unknown: 'default' }
const STATEMENT_LABEL = { fact: 'FACT', statistical_finding: 'STATISTICAL', hypothesis: 'HYPOTHESIS', unknown: 'UNKNOWN' }

function StatementBadges({ x }) {
  if (!x.statement_type && !x.verification) return null
  return (
    <span className="inline-flex gap-1.5 mr-2 align-middle">
      {x.statement_type && (
        <Badge tone={STATEMENT_TONE[x.statement_type] || 'default'}>
          {STATEMENT_LABEL[x.statement_type] || x.statement_type}
        </Badge>
      )}
      {x.verification === 'evidence_verified' && <Badge tone="success">✓ evidence</Badge>}
      {x.verification === 'unverified' && <Badge tone="warn">unverified</Badge>}
    </span>
  )
}

function EvidenceIds({ ids }) {
  if (!ids?.length) return null
  return (
    <div className="flex gap-1.5 flex-wrap mt-1">
      {ids.map((e) => (
        <span key={e} className="text-[11px] font-mono bg-surface px-1.5 py-0.5 rounded border border-surface-border text-slate-500">
          {e}
        </span>
      ))}
    </div>
  )
}

function AIList({ title, subtitle, items, render }) {
  if (!items?.length) return null
  return (
    <div className="card-pad">
      <div className="h-title mb-1">{title}</div>
      {subtitle && <div className="text-xs text-slate-500 mb-3">{subtitle}</div>}
      <div className="space-y-3">{items.map((x, i) => render(x, i))}</div>
    </div>
  )
}

export default function Insights() {
  const { projectId } = useParams()
  const ai = useAsync(() => api.insights(projectId), [projectId])
  const signals = useAsync(() => api.signals(projectId), [projectId])

  return (
    <>
      <PageHeader title="Business Insights"
                  subtitle="Narrative reasoned by the LLM from deterministic analytics — never templated" />
      <AsyncSection state={ai} empty="Analysis not finished yet.">
        {(a) => (
          <div className="space-y-4">
            <AIStatus status={a.status} provider={a.provider} model={a.model} error={a.error} />
            {a.status === 'ok' && (
              <div className="grid lg:grid-cols-2 gap-4">
                <AIList title="Key Insights"
                        subtitle="Each statement is labelled and verified against the deterministic evidence it cites"
                        items={a.key_insights} render={(x, i) => (
                  <motion.div key={i} initial={{ opacity: 0, y: 6 }} animate={{ opacity: 1, y: 0 }}
                              transition={{ delay: i * 0.04 }}>
                    <div className="font-medium text-slate-100"><StatementBadges x={x} />{x.title}</div>
                    {x.detail && <div className="text-sm text-slate-400 mt-0.5">{x.detail}</div>}
                    <EvidenceIds ids={x.evidence_ids} />
                    {x.confidence != null && (
                      <div className="text-xs text-slate-600 mt-1">confidence {Math.round(x.confidence * 100)}%</div>
                    )}
                  </motion.div>
                )} />
                <AIList title="Root Cause Hypotheses"
                        subtitle="Causes are never asserted — each is a hypothesis with supporting and missing evidence"
                        items={a.root_causes} render={(x, i) => (
                  <div key={i}>
                    <div className="font-medium text-slate-100"><StatementBadges x={x} />{x.problem}</div>
                    {(x.possible_cause || x.cause) && (
                      <div className="text-sm text-slate-400 mt-0.5">Possible cause: {x.possible_cause || x.cause}</div>
                    )}
                    {(x.supporting_evidence || x.evidence) && (
                      <div className="text-xs text-sky-400/80 mt-0.5">Supporting evidence: {x.supporting_evidence || x.evidence}</div>
                    )}
                    {x.missing_evidence && (
                      <div className="text-xs text-amber-400/80 mt-0.5">Missing evidence: {x.missing_evidence}</div>
                    )}
                    <EvidenceIds ids={x.evidence_ids} />
                    {x.confidence != null && (
                      <div className="text-xs text-slate-600 mt-1">
                        confidence {typeof x.confidence === 'number' ? `${Math.round(x.confidence * 100)}%` : x.confidence}
                      </div>
                    )}
                  </div>
                )} />
                <AIList title="Risks" items={a.risks} render={(x, i) => (
                  <div key={i}>
                    <div className="flex items-start gap-2">
                      {x.severity && <Badge tone={severityTone(x.severity)}>{x.severity}</Badge>}
                      {x.verification === 'unverified' && <Badge tone="warn">unverified</Badge>}
                      <div className="text-sm text-slate-300">{x.risk}{x.evidence ? ` — ${x.evidence}` : ''}</div>
                    </div>
                    <EvidenceIds ids={x.evidence_ids} />
                  </div>
                )} />
                <AIList title="Opportunities" items={a.opportunities} render={(x, i) => (
                  <div key={i}>
                    <div className="flex items-start gap-2">
                      {x.impact && <Badge tone="success">{x.impact}</Badge>}
                      {x.verification === 'unverified' && <Badge tone="warn">unverified</Badge>}
                      <div className="text-sm text-slate-300">{x.opportunity}{x.evidence ? ` — ${x.evidence}` : ''}</div>
                    </div>
                    <EvidenceIds ids={x.evidence_ids} />
                  </div>
                )} />
                {a.data_limitations?.length > 0 && (
                  <AIList title="Data Limitations"
                          subtitle="What this dataset cannot answer"
                          items={a.data_limitations} render={(x, i) => (
                    <div key={i} className="text-sm text-slate-400">• {typeof x === 'string' ? x : JSON.stringify(x)}</div>
                  )} />
                )}
              </div>
            )}

            <AsyncSection state={signals} empty="No statistical signals detected.">
              {(sigs) => (
                <div className="card overflow-auto">
                  <div className="px-4 pt-4">
                    <div className="h-title">Deterministic Signals</div>
                    <div className="text-xs text-slate-500 mb-2">
                      The statistical facts the AI reasons over — computed without any LLM
                    </div>
                  </div>
                  <table className="table-base">
                    <thead><tr><th>Signal</th><th>KPI / Target</th><th>Statistics</th><th>Strength</th></tr></thead>
                    <tbody>
                      {sigs.map((s) => (
                        <tr key={s.id} className="hover:bg-surface-overlay/40">
                          <td><Badge tone={SIGNAL_TONE[s.kind] || 'default'}>{s.kind.replace('_', ' ')}</Badge></td>
                          <td className="text-slate-200">{s.kpi_name || s.stats.dataset || '—'}</td>
                          <td>
                            <div className="flex gap-1.5 flex-wrap max-w-2xl">
                              {Object.entries(s.stats).map(([k, v]) => (
                                <span key={k} className="text-[11px] font-mono bg-surface px-1.5 py-0.5 rounded border border-surface-border text-slate-500">
                                  {k}={String(v)}
                                </span>
                              ))}
                            </div>
                          </td>
                          <td>
                            <div className="w-16 h-1.5 bg-surface-overlay rounded-full">
                              <div className="h-full bg-accent rounded-full" style={{ width: `${s.strength * 100}%` }} />
                            </div>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}
            </AsyncSection>
          </div>
        )}
      </AsyncSection>
    </>
  )
}
