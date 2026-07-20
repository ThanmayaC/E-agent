// Admin overview — one screen of platform vitals with links into each area.
import { Link } from 'react-router-dom'
import { api } from '../../api/client'
import { AsyncSection, Badge, PageHeader, Panel, Stat, useAsync } from '../../components/ui'

export default function AdminOverview() {
  const state = useAsync(async () => {
    const [runtime, brain, queue] = await Promise.all([
      api.runtimeStatus().catch(() => null),
      api.brainStatus().catch(() => null),
      api.runtimeQueue().catch(() => null),
    ])
    return { runtime, brain, queue }
  }, [])

  return (
    <>
      <PageHeader title="Admin Console" subtitle="Platform internals: runtime, learning, synchronization, and diagnostics" />
      <AsyncSection state={state} empty="The platform is not reachable.">
        {({ runtime, brain, queue }) => (
          <div className="space-y-5">
            <div className="grid gap-4 md:grid-cols-4">
              <Stat label="Autonomy runtime" value={runtime?.autonomy ?? 'unavailable'}
                    tone={runtime?.running ? 'text-emerald-400' : 'text-slate-400'} />
              <Stat label="Enterprise Brain" value={brain?.state ?? 'unavailable'}
                    tone={brain?.state === 'ready' ? 'text-emerald-400' : 'text-amber-400'} />
              <Stat label="Jobs enabled" value={runtime?.scheduler?.jobs_enabled} />
              <Stat label="Actions pending approval" value={queue?.pending_approval ?? runtime?.queue?.pending_approval}
                    tone="text-amber-400" />
            </div>
            <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
              {[
                ['/admin/runtime', 'Runtime', 'Autonomy status, action queue, goals, triggers, metrics'],
                ['/admin/brain', 'Brain', 'Learning state, knowledge statistics, memory'],
                ['/admin/scheduler', 'Scheduler', 'Heartbeat control, degraded jobs, trigger rules'],
                ['/admin/jobs', 'Jobs', 'Scheduled job registry, manual runs, execution history'],
                ['/admin/sync', 'Sync', 'Connected sources, synchronization runs, organization model'],
                ['/admin/knowledge', 'Knowledge', 'Terminology, business rules, learned clarifications'],
                ['/admin/logs', 'Logs', 'Event bus history and job executions'],
                ['/admin/diagnostics', 'Diagnostics', 'Health checks, agents, tools, connectors'],
                ['/admin/models', 'Model status', 'LLM provider, model, and availability'],
              ].map(([to, title, desc]) => (
                <Link key={to} to={to} className="card-pad card-hover block">
                  <div className="text-sm font-semibold text-slate-200">{title}</div>
                  <div className="text-xs text-slate-500 mt-1">{desc}</div>
                </Link>
              ))}
            </div>
            <Panel title="Degraded jobs">
              {(runtime?.scheduler?.degraded_jobs || []).length === 0
                ? <div className="text-sm text-slate-600">None — all scheduled jobs are healthy.</div>
                : <div className="flex gap-2 flex-wrap">
                    {runtime.scheduler.degraded_jobs.map((j) => <Badge key={j} tone="danger">{j}</Badge>)}
                  </div>}
            </Panel>
          </div>
        )}
      </AsyncSection>
    </>
  )
}
