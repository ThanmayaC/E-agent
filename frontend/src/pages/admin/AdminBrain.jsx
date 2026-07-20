// Brain — technical status of the Enterprise Brain: state, checks,
// knowledge statistics, and learning history.
import { api } from '../../api/client'
import { AsyncSection, Badge, PageHeader, Panel, Stat, useAsync } from '../../components/ui'

export default function AdminBrain() {
  const state = useAsync(async () => {
    const [status, stats] = await Promise.all([api.brainStatus(), api.brainStatistics()])
    return { status, stats }
  }, [])

  return (
    <>
      <PageHeader title="Enterprise Brain" subtitle="Learning state, storage statistics, and subsystem checks" />
      <AsyncSection state={state} empty="Brain status unavailable.">
        {({ status, stats }) => (
          <div className="space-y-5">
            <div className="grid gap-4 md:grid-cols-4">
              <Stat label="State" value={status.state}
                    tone={status.state === 'ready' ? 'text-emerald-400' : 'text-amber-400'} />
              <Stat label="Knowledge entries"
                    value={Object.values(stats.knowledge || {}).reduce((a, b) => a + b, 0)} />
              <Stat label="Graph"
                    value={`${stats.graph?.node_count ?? 0} / ${stats.graph?.edge_count ?? 0}`}
                    hint={`nodes / edges (${stats.graph?.neo4j || 'in-memory'})`} />
              <Stat label="Learning events" value={stats.learning?.events ?? 0}
                    hint={`${stats.clarifications?.answered ?? 0} clarifications learned`} />
            </div>

            <Panel title="Subsystem checks">
              <div className="grid md:grid-cols-3 gap-1 text-sm">
                {Object.entries(status.checks || {}).map(([name, check]) => (
                  <div key={name} className="flex justify-between py-1.5 px-2 rounded hover:bg-surface-overlay/40">
                    <span className="text-slate-400 font-mono text-xs">{name}</span>
                    <Badge tone={check.ok ? 'success' : 'danger'}>{check.ok ? 'ok' : 'failed'}</Badge>
                  </div>
                ))}
              </div>
            </Panel>

            <Panel title="Knowledge by kind">
              <div className="grid grid-cols-2 md:grid-cols-4 gap-3 text-sm">
                {Object.entries(stats.knowledge || {}).map(([k, v]) => (
                  <div key={k} className="flex justify-between gap-2">
                    <span className="text-slate-500 font-mono text-xs">{k}</span>
                    <span className="text-slate-200 tabular-nums">{v}</span>
                  </div>
                ))}
              </div>
            </Panel>
          </div>
        )}
      </AsyncSection>
    </>
  )
}
