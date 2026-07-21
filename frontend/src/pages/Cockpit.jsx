// Executive Cockpit (V2.5) — the flagship homepage. The first thing an
// executive sees is what requires attention: a live pulse of the enterprise,
// the Brain's ranked decisions (each explainable), critical risks, approvals,
// and a one-click "simulate next business day" so the whole autonomous loop
// can be demonstrated on demand. Every number comes from an existing API.
import { useMemo, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { api } from '../api/client'
import { useAsync } from '../components/ui'
import {
  Counter, ExplainPanel, ExportMenu, GlowPanel, Loader, PremiumHeader, Reveal,
  ScoreGauge, Sparkline, Stagger, StaggerItem, StatCard, TrendPill,
} from '../components/premium'
import { SimulateDayButton } from './SimulateDay'

function greeting() {
  const h = new Date().getHours()
  return h < 12 ? 'Good morning' : h < 18 ? 'Good afternoon' : 'Good evening'
}

export default function Cockpit() {
  const [refresh, setRefresh] = useState(0)
  const [ask, setAsk] = useState('')
  const [explain, setExplain] = useState(null)
  const navigate = useNavigate()
  const reload = () => setRefresh((n) => n + 1)

  const ws = useAsync(() => api.managerWorkspace(), [refresh])
  const brief = useAsync(() => api.intelligenceBrief().catch(() => null), [refresh])
  const status = useAsync(() => api.intelligenceStatus().catch(() => null), [refresh])
  const stats = useAsync(() => api.brainStatistics().catch(() => null), [refresh])
  const briefHistory = useAsync(() => api.dailyBriefHistory(14).catch(() => []), [refresh])

  const goAsk = (q) => navigate('/copilot', { state: { ask: q } })
  const decide = (id, s) => api.setIntelligenceDecision(id, s, 'executive', `${s} from Cockpit`).then(reload)

  const health = ws.data?.portfolio_health?.average_health_score
  // Brief-history items don't carry a single health number; derive one per
  // day from the mean of that day's report health scores, for the sparkline.
  const healthSeries = useMemo(
    () => (briefHistory.data || [])
      .map((b) => {
        const scores = (b.important_reports || [])
          .map((r) => r.health_score).filter((n) => typeof n === 'number')
        return scores.length ? scores.reduce((a, c) => a + c, 0) / scores.length : null
      })
      .filter((n) => n != null).reverse(),
    [briefHistory.data])
  const weights = status.data?.ranking_weights

  return (
    <div className="space-y-6">
      <PremiumHeader title="Executive Cockpit" badge="Live"
        subtitle="Your enterprise at a glance — reasoned, ranked, and ready to act.">
        <SimulateDayButton onDone={reload} />
        <ExportMenu filename="executive-cockpit"
          json={{ workspace: ws.data, brief: brief.data, stats: stats.data }} />
      </PremiumHeader>

      {/* Hero: greeting + pulse + ask bar */}
      <Reveal>
        <div className="card-pad grid-backdrop relative overflow-hidden">
          <div className="absolute top-0 right-0 w-72 h-72 bg-accent/10 blur-3xl rounded-full pointer-events-none" />
          <div className="relative flex flex-col lg:flex-row lg:items-center gap-6">
            <div className="shrink-0">
              <HealthDial score={health} series={healthSeries} />
            </div>
            <div className="flex-1 min-w-0">
              <h2 className="text-xl lg:text-2xl font-bold text-slate-100">
                {greeting()}. {(brief.data?.critical_risks?.length ?? 0) > 0
                  ? `${brief.data.critical_risks.length} risk(s) need attention.`
                  : 'The enterprise is steady.'}
              </h2>
              <p className="text-sm text-slate-500 mt-1">
                {status.data?.open ?? 0} open decisions · {(brief.data?.pending_approvals?.length ?? 0)} awaiting approval ·{' '}
                {stats.data?.learning?.events ?? 0} things learned
              </p>
              <form className="mt-4 flex gap-2 max-w-xl"
                onSubmit={(e) => { e.preventDefault(); if (ask.trim()) goAsk(ask.trim()) }}>
                <input className="input !py-2.5" autoFocus placeholder="Ask the Enterprise Brain anything…"
                  value={ask} onChange={(e) => setAsk(e.target.value)} />
                <button className="btn" type="submit" disabled={!ask.trim()}>Ask ✦</button>
              </form>
            </div>
          </div>
        </div>
      </Reveal>

      {/* Pulse strip: the enterprise in six live numbers */}
      <Loader state={ws} skeleton={<div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4 xl:grid-cols-6" />}>
        {(w) => {
          const summary = w.todays_summary || {}
          return (
            <Stagger className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4 xl:grid-cols-6">
              <StaggerItem><StatCard label="Portfolio health" value={health} decimals={0}
                tone={health >= 70 ? 'text-emerald-400' : health >= 50 ? 'text-amber-400' : 'text-rose-400'}
                spark={<Sparkline data={healthSeries} width={150} />} onClick={() => navigate('/portfolio')} /></StaggerItem>
              <StaggerItem><StatCard label="Open decisions" value={status.data?.open ?? 0}
                onClick={() => navigate('/decisions')} /></StaggerItem>
              <StaggerItem><StatCard label="Awaiting approval" value={brief.data?.pending_approvals?.length ?? 0}
                tone="text-amber-400" onClick={() => navigate('/tasks')} /></StaggerItem>
              <StaggerItem><StatCard label="Critical risks" value={brief.data?.critical_risks?.length ?? 0}
                tone="text-rose-400" onClick={() => navigate('/analytics/decisions')} /></StaggerItem>
              <StaggerItem><StatCard label="Open tasks" value={summary.open_action_items ?? 0}
                onClick={() => navigate('/tasks')} /></StaggerItem>
              <StaggerItem><StatCard label="Things learned" value={stats.data?.learning?.events ?? 0}
                onClick={() => navigate('/analytics/knowledge')} /></StaggerItem>
            </Stagger>
          )
        }}
      </Loader>

      {/* Top decisions — each explainable — and recommended actions */}
      <div className="grid gap-5 lg:grid-cols-3">
        <GlowPanel accent className="lg:col-span-2" title="Top decisions"
          action={<Link to="/decisions" className="btn-quiet">All decisions →</Link>}>
          <Loader state={brief} empty="The Brain has nothing urgent to propose."
            skeleton={<div className="space-y-3">{[0, 1, 2].map((i) => <div key={i} className="h-16 rounded-lg bg-surface-overlay/40 animate-pulse" />)}</div>}>
            {(b) => (b.top_decisions || []).length === 0
              ? <div className="text-sm text-slate-500 py-6 text-center">No open decisions right now.</div>
              : (
                <Stagger className="space-y-2.5">
                  {b.top_decisions.slice(0, 5).map((d, i) => (
                    <StaggerItem key={d.decision_id}>
                      <div className="flex items-center gap-3 p-3 rounded-lg bg-surface-overlay/30 hover:bg-surface-overlay/60 transition-colors group">
                        <ScoreGauge score={d.score} size={46} />
                        <div className="min-w-0 flex-1">
                          <div className="text-sm text-slate-200 truncate">
                            <span className={`inline-block px-1.5 py-0.5 rounded text-[10px] font-semibold mr-1.5 ${
                              d.priority <= 2 ? 'bg-rose-500/15 text-rose-400' : 'bg-accent/15 text-accent'}`}>P{d.priority}</span>
                            {d.action}
                          </div>
                          <div className="text-xs text-slate-500 mt-0.5 capitalize">
                            {d.kind} · {Math.round((d.confidence ?? 0) * 100)}% confidence · rank #{i + 1}
                          </div>
                        </div>
                        <div className="shrink-0 flex items-center gap-2 text-xs">
                          <button onClick={() => setExplain({ ...d, rank: i + 1 })}
                            className="text-accent hover:underline whitespace-nowrap">Why?</button>
                          {(d.status === 'proposed' || d.status === 'modified') && (
                            <>
                              <button onClick={() => decide(d.decision_id, 'approved')}
                                className="text-emerald-400 hover:underline">Approve</button>
                              <button onClick={() => decide(d.decision_id, 'rejected')}
                                className="text-slate-500 hover:underline">Reject</button>
                            </>
                          )}
                        </div>
                      </div>
                    </StaggerItem>
                  ))}
                </Stagger>
              )}
          </Loader>
        </GlowPanel>

        <div className="space-y-5">
          <GlowPanel title="Today's brief" action={<Link to="/reports" className="btn-quiet">Full →</Link>}>
            <Loader state={brief} empty="Brief warming up." skeleton={<div className="h-24 rounded bg-surface-overlay/40 animate-pulse" />}>
              {(b) => (
                <div className="space-y-2.5">
                  {(b.recommended_actions || []).slice(0, 3).map((r) => (
                    <div key={r.decision_id} className="text-sm text-slate-300 flex gap-2">
                      <span className="text-accent">▹</span><span className="truncate">{r.action}</span>
                    </div>
                  ))}
                  {(b.recommended_actions || []).length === 0 && <div className="text-sm text-slate-500">No actions pending a call.</div>}
                </div>
              )}
            </Loader>
          </GlowPanel>

          <GlowPanel title="Critical risks" action={<Link to="/notifications" className="btn-quiet">Alerts →</Link>}>
            <Loader state={brief} empty="No open risks." skeleton={<div className="h-16 rounded bg-surface-overlay/40 animate-pulse" />}>
              {(b) => (b.critical_risks || []).length === 0
                ? <div className="text-sm text-slate-500">No open business risks.</div>
                : (
                  <ul className="space-y-2">
                    {b.critical_risks.slice(0, 4).map((r, i) => (
                      <li key={i} className="text-sm text-slate-300 flex gap-2">
                        <span className="text-rose-400 mt-0.5">▲</span><span className="truncate">{r.insight}</span>
                      </li>
                    ))}
                  </ul>
                )}
            </Loader>
          </GlowPanel>
        </div>
      </div>

      {/* Approvals + organizational changes */}
      <div className="grid gap-5 lg:grid-cols-2">
        <GlowPanel title="Pending approvals" action={<Link to="/tasks" className="btn-quiet">All →</Link>}>
          <Loader state={brief} empty="Nothing waiting on you." skeleton={<div className="h-16 rounded bg-surface-overlay/40 animate-pulse" />}>
            {(b) => (b.pending_approvals || []).length === 0
              ? <div className="text-sm text-slate-500">Nothing is waiting on you.</div>
              : (
                <ul className="space-y-2">
                  {b.pending_approvals.slice(0, 5).map((a) => (
                    <li key={a.action_id} className="flex items-center justify-between gap-3 text-sm">
                      <span className="text-slate-300 truncate">{a.title}</span>
                      <span className="shrink-0 space-x-2.5 text-xs">
                        <button onClick={() => api.approveAction(a.action_id, 'executive').then(reload)}
                          className="text-emerald-400 hover:underline">Approve</button>
                        <button onClick={() => api.rejectAction(a.action_id, 'executive', 'from cockpit').then(reload)}
                          className="text-slate-500 hover:underline">Reject</button>
                      </span>
                    </li>
                  ))}
                </ul>
              )}
          </Loader>
        </GlowPanel>

        <GlowPanel title="Recent organizational changes"
          action={<Link to="/timeline" className="btn-quiet">Timeline →</Link>}>
          <Loader state={brief} empty="No recent changes." skeleton={<div className="h-16 rounded bg-surface-overlay/40 animate-pulse" />}>
            {(b) => (
              <ul className="space-y-2">
                {(b.recent_changes || []).slice(0, 6).map((c, i) => (
                  <li key={i} className="text-sm flex items-start gap-2.5">
                    <span className="w-1.5 h-1.5 rounded-full bg-accent mt-1.5 shrink-0" />
                    <div className="min-w-0">
                      <span className="text-slate-300">{c.kind}</span>
                      <span className="text-slate-500 text-xs"> · {c.summary}</span>
                    </div>
                  </li>
                ))}
                {(b.recent_changes || []).length === 0 && <div className="text-sm text-slate-500">Nothing has changed recently.</div>}
              </ul>
            )}
          </Loader>
        </GlowPanel>
      </div>

      {explain && <ExplainPanel decision={explain} weights={weights} onClose={() => setExplain(null)} />}
    </div>
  )
}

function HealthDial({ score, series }) {
  const size = 132
  const r = (size - 14) / 2, c = 2 * Math.PI * r
  const pct = score == null ? 0 : Math.max(0, Math.min(100, score))
  const color = score == null ? '#334155' : score >= 70 ? '#34d399' : score >= 50 ? '#fbbf24' : '#fb7185'
  const rawDelta = series?.length >= 2 ? series[series.length - 1] - series[series.length - 2] : null
  const delta = Number.isFinite(rawDelta) ? Number(rawDelta.toFixed(1)) : null
  return (
    <div className="relative flex flex-col items-center" style={{ width: size }}>
      <div className="relative" style={{ width: size, height: size }}>
        <svg width={size} height={size} className="-rotate-90">
          <circle cx={size / 2} cy={size / 2} r={r} fill="none" strokeWidth="7" className="stroke-surface-overlay" />
          <circle cx={size / 2} cy={size / 2} r={r} fill="none" strokeWidth="7" stroke={color} strokeLinecap="round"
            strokeDasharray={c} strokeDashoffset={c - (c * pct) / 100}
            style={{ transition: 'stroke-dashoffset 900ms cubic-bezier(0.22,1,0.36,1)' }} />
        </svg>
        <div className="absolute inset-0 flex flex-col items-center justify-center">
          <span className="text-3xl font-bold text-slate-100 tabular-nums">
            {score == null ? '—' : <Counter value={score} />}
          </span>
          <span className="text-[10px] uppercase tracking-wider text-slate-500">health</span>
        </div>
      </div>
      {delta != null && <div className="mt-2"><TrendPill change={delta} /></div>}
    </div>
  )
}
