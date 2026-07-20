// Logs — event bus history and scheduler executions.
import { useState } from 'react'
import { api } from '../../api/client'
import {
  AsyncSection, Badge, PageHeader, Panel, PanelEmpty, Tabs, useAsync, when,
} from '../../components/ui'

const statusTone = { completed: 'success', running: 'info', failed: 'danger' }

export default function AdminLogs() {
  const [tab, setTab] = useState('events')
  const state = useAsync(async () => {
    const [events, executions] = await Promise.all([
      api.runtimeEvents(100).catch(() => null),
      api.runtimeExecutions(100).catch(() => null),
    ])
    return { events, executions }
  }, [])

  return (
    <>
      <PageHeader title="Logs" subtitle="Event bus history and job execution records" />
      <AsyncSection state={state} empty="No log data.">
        {({ events, executions }) => {
          const eventList = events?.events || []
          const execList = executions?.executions || (Array.isArray(executions) ? executions : [])
          return (
            <>
              <Tabs active={tab} onChange={setTab}
                    tabs={[{ value: 'events', label: 'Events', count: eventList.length },
                           { value: 'executions', label: 'Executions', count: execList.length }]} />
              {tab === 'events' ? (
                <Panel title="Event bus">
                  {eventList.length === 0 ? <PanelEmpty text="No events." /> : (
                    <ul className="space-y-1.5 text-sm font-mono">
                      {eventList.map((e, i) => (
                        <li key={e.event_id || i} className="flex justify-between gap-3 py-1 px-2 rounded hover:bg-surface-overlay/40">
                          <span className="min-w-0 truncate">
                            <span className="text-accent text-xs">{e.kind}</span>{' '}
                            <span className="text-slate-400 text-xs">{e.project_id || ''}</span>{' '}
                            <span className="text-slate-500 text-xs">{typeof e.payload === 'object' ? JSON.stringify(e.payload).slice(0, 100) : String(e.detail || '')}</span>
                          </span>
                          <span className="text-slate-600 text-xs shrink-0">{when(e.at || e.emitted_at || e.created_at)}</span>
                        </li>
                      ))}
                    </ul>
                  )}
                </Panel>
              ) : (
                <Panel title="Job executions">
                  {execList.length === 0 ? <PanelEmpty text="No executions." /> : (
                    <ul className="space-y-1.5 text-sm">
                      {execList.map((e, i) => (
                        <li key={e.execution_id || i} className="flex justify-between gap-3 py-1 px-2 rounded hover:bg-surface-overlay/40">
                          <span className="min-w-0 truncate">
                            <Badge tone={statusTone[e.status] || 'default'}>{e.status}</Badge>{' '}
                            <span className="font-mono text-xs text-slate-300">{e.job}</span>
                            {e.error && <span className="text-rose-400 text-xs ml-2">{String(e.error).slice(0, 100)}</span>}
                          </span>
                          <span className="text-slate-600 text-xs shrink-0">{when(e.started_at)}</span>
                        </li>
                      ))}
                    </ul>
                  )}
                </Panel>
              )}
            </>
          )
        }}
      </AsyncSection>
    </>
  )
}
