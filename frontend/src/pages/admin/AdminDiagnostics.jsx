// Diagnostics — platform health checks plus the agent, tool, and
// connector registries.
import { api } from '../../api/client'
import {
  AsyncSection, Badge, PageHeader, Panel, PanelEmpty, useAsync,
} from '../../components/ui'

export default function AdminDiagnostics() {
  const state = useAsync(async () => {
    const [brain, agents, tools, connectors, workflows] = await Promise.all([
      api.brainStatus().catch(() => null),
      api.platformAgents().catch(() => null),
      api.platformTools().catch(() => null),
      api.platformConnectors().catch(() => null),
      api.platformWorkflows().catch(() => null),
    ])
    return { brain, agents, tools, connectors, workflows }
  }, [])

  const listOf = (d, key) => d?.[key] || (Array.isArray(d) ? d : [])

  return (
    <>
      <PageHeader title="Diagnostics" subtitle="Health checks and the platform's registered capabilities" />
      <AsyncSection state={state} empty="Diagnostics unavailable.">
        {({ brain, agents, tools, connectors, workflows }) => (
          <div className="space-y-5">
            <Panel title={<>Health checks {brain?.state && <Badge tone={brain.state === 'ready' ? 'success' : 'warn'}>{brain.state}</Badge>}</>}>
              {!brain?.checks ? <PanelEmpty text="No checks reported." /> : (
                <div className="grid md:grid-cols-3 gap-1 text-sm">
                  {Object.entries(brain.checks).map(([name, check]) => (
                    <div key={name} className="flex justify-between py-1.5 px-2 rounded hover:bg-surface-overlay/40">
                      <span className="text-slate-400 font-mono text-xs">{name}</span>
                      <Badge tone={check.ok ? 'success' : 'danger'}>{check.ok ? 'ok' : 'failed'}</Badge>
                    </div>
                  ))}
                </div>
              )}
            </Panel>

            <div className="grid gap-5 lg:grid-cols-2">
              {[['Agents', listOf(agents, 'agents')], ['Tools', listOf(tools, 'tools')],
                ['Connectors', listOf(connectors, 'connectors')], ['Workflows', listOf(workflows, 'workflows')]].map(([title, list]) => (
                <Panel key={title} title={`${title} (${list.length})`}>
                  {list.length === 0 ? <PanelEmpty text={`No ${title.toLowerCase()} registered.`} /> : (
                    <ul className="space-y-1.5 text-sm">
                      {list.map((item, i) => (
                        <li key={item.name || i} className="flex justify-between gap-3 py-1 px-2 rounded hover:bg-surface-overlay/40">
                          <span className="min-w-0">
                            <span className="font-mono text-xs text-slate-200">{item.name || item.id}</span>
                            {item.description && <span className="text-slate-500 text-xs ml-2">{String(item.description).slice(0, 90)}</span>}
                          </span>
                          {'available' in item && (
                            <Badge tone={item.available ? 'success' : 'default'}>{item.available ? 'available' : 'off'}</Badge>
                          )}
                        </li>
                      ))}
                    </ul>
                  )}
                </Panel>
              ))}
            </div>
          </div>
        )}
      </AsyncSection>
    </>
  )
}
