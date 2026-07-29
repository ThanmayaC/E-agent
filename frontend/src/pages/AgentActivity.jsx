// Agent Activity (V2.5) — the enterprise's agent workforce and what it has
// been doing. Reads the agent catalogue (/ops/agents) and the runtime's own
// event/execution records (/runtime/activity, /runtime/events) to show who's
// registered, their role toward the Brain, and a live feed of autonomous
// activity. No backend logic — a lens over existing records.
import { useEffect, useMemo, useState } from 'react'
import { api } from '../api/client'
import { useAsync } from '../components/ui'
import { timeAgo } from '../components/ui'
import {
  ExportMenu, FilterChips, Loader, PremiumHeader, Reveal, SearchInput,
  StatCard, Stagger, StaggerItem,
} from '../components/premium'

const ROLE_TONE = {
  produces: 'text-emerald-400 bg-emerald-500/10',
  consumes: 'text-accent bg-accent/10',
  updates: 'text-purple-400 bg-purple-500/10',
  observes: 'text-amber-400 bg-amber-500/10',
}

export default function AgentActivity() {
  const [tick, setTick] = useState(0)
  useEffect(() => {
    const id = setInterval(() => setTick((n) => n + 1), 8000)
    return () => clearInterval(id)
  }, [])

  const agents = useAsync(() => api.opsAgents().then((r) => r.agents || []).catch(() => []), [])
  const events = useAsync(() => api.runtimeEvents(80).then((r) => r).catch(() => ({ events: [], stats: {} })), [tick])
  const activity = useAsync(() => api.runtimeActivity(20), [tick])

  const [q, setQ] = useState('')
  const [role, setRole] = useState('')

  const roleCounts = useMemo(() => {
    const m = {}
    ;(agents.data || []).forEach((a) => { const r = a.brain_role || 'other'; m[r] = (m[r] || 0) + 1 })
    return Object.entries(m).map(([value, count]) => ({ value, label: value, count }))
  }, [agents.data])

  const filteredAgents = useMemo(() => {
    const needle = q.trim().toLowerCase()
    return (agents.data || []).filter((a) =>
      (!role || (a.brain_role || 'other') === role) &&
      (!needle || `${a.name} ${a.description}`.toLowerCase().includes(needle)))
  }, [agents.data, q, role])

  // Job activity from the event stream: JobStarted/JobCompleted/JobFailed.
  const jobFeed = useMemo(() => (events.data?.events || [])
    .filter((e) => e.kind?.startsWith('Job') || e.source?.includes('scheduler'))
    .slice(0, 12), [events.data])

  const byKind = events.data?.stats?.by_kind || {}
  const jobsCompleted = byKind.JobCompleted || 0
  const jobsFailed = byKind.JobFailed || 0

  return (
    <div>
      <PremiumHeader title="Agent Activity" badge="Workforce"
        subtitle="The specialized agents running the enterprise, their role toward the Brain, and live autonomous activity.">
        <ExportMenu filename="agent-activity" json={agents.data}
          rows={(agents.data || []).map((a) => ({ id: a.id, name: a.name,
            role: a.brain_role, policy: a.execution_policy, approval: a.approval_policy }))} />
      </PremiumHeader>

      <Stagger className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4 mb-6">
        <StaggerItem><StatCard label="Registered agents" value={(agents.data || []).length} /></StaggerItem>
        <StaggerItem><StatCard label="Events published" value={events.data?.stats?.published ?? 0} /></StaggerItem>
        <StaggerItem><StatCard label="Jobs completed" value={jobsCompleted} tone="fg-success" /></StaggerItem>
        <StaggerItem><StatCard label="Jobs failed" value={jobsFailed}
          tone={jobsFailed ? 'fg-danger' : 'fg-primary'} /></StaggerItem>
      </Stagger>

      <div className="grid gap-5 lg:grid-cols-3">
        <div className="lg:col-span-2">
          <div className="flex flex-wrap items-center gap-3 mb-3">
            <SearchInput value={q} onChange={setQ} placeholder="Find an agent…" className="w-56" />
            <FilterChips options={roleCounts} active={role} onChange={setRole}
              allLabel={`All (${(agents.data || []).length})`} />
          </div>
          <Loader state={agents} skeleton={<div className="grid sm:grid-cols-2 gap-4">{[0, 1, 2, 3].map((i) => <div key={i} className="h-28 rounded-xl bg-surface-overlay/40 animate-pulse" />)}</div>}
            empty="No agents registered.">
            {() => (
              <Stagger className="grid sm:grid-cols-2 gap-4">
                {filteredAgents.map((a) => (
                  <StaggerItem key={a.id}>
                    <div className="card-pad card-hover h-full">
                      <div className="flex items-start justify-between gap-2 mb-1.5">
                        <h3 className="text-sm font-semibold text-slate-100">{a.name}</h3>
                        {a.brain_role && (
                          <span className={`px-2 py-0.5 rounded-md text-[10px] font-medium capitalize shrink-0 ${ROLE_TONE[a.brain_role] || 'text-slate-400 bg-surface-overlay'}`}>
                            {a.brain_role}
                          </span>
                        )}
                      </div>
                      <p className="text-xs text-slate-500 leading-relaxed line-clamp-3">{a.description}</p>
                      <div className="flex flex-wrap gap-1.5 mt-3">
                        <Tag>{(a.execution_policy || 'on_demand').replace(/_/g, ' ')}</Tag>
                        {a.approval_policy && a.approval_policy !== 'none' && <Tag tone="amber">needs approval</Tag>}
                        {(a.capabilities || []).slice(0, 2).map((c) => <Tag key={c}>{c}</Tag>)}
                      </div>
                    </div>
                  </StaggerItem>
                ))}
                {filteredAgents.length === 0 && <div className="text-sm text-slate-500 py-6">No agents match.</div>}
              </Stagger>
            )}
          </Loader>
        </div>

        <div>
          <h2 className="text-sm font-semibold text-slate-200 mb-3 flex items-center gap-2">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" /> Live activity
          </h2>
          <div className="card-pad max-h-[600px] overflow-y-auto">
            {jobFeed.length === 0
              ? <div className="text-sm text-slate-500">Waiting for activity…</div>
              : (
                <ol className="space-y-2.5">
                  {jobFeed.map((e, i) => (
                    <Reveal key={e.event_id + i} delay={i * 0.02}>
                      <li className="flex items-start gap-2.5 text-sm">
                        <span className={`mt-1.5 w-1.5 h-1.5 rounded-full shrink-0 ${
                          e.kind === 'JobFailed' ? 'bg-rose-400' : e.kind === 'JobCompleted' ? 'bg-emerald-400' : 'bg-accent'}`} />
                        <div className="min-w-0 flex-1">
                          <div className="text-slate-300 truncate">
                            {(e.payload?.job || e.kind).replace(/_/g, ' ')}
                          </div>
                          <div className="text-[11px] text-slate-500">{e.kind.replace('Job', '')} · {timeAgo(e.created_at)}</div>
                        </div>
                      </li>
                    </Reveal>
                  ))}
                </ol>
              )}
          </div>
        </div>
      </div>
    </div>
  )
}

function Tag({ children, tone }) {
  return (
    <span className={`px-1.5 py-0.5 rounded text-[10px] capitalize ${
      tone === 'amber' ? 'bg-amber-500/10 text-amber-400' : 'bg-surface-overlay text-slate-400'}`}>
      {children}
    </span>
  )
}
