// Sync — connected sources, synchronization runs, and the organization
// model the platform maintains from them.
import { useState } from 'react'
import { api } from '../../api/client'
import {
  AsyncSection, Badge, ListControls, Notice, PageHeader, Pager, Panel, PanelEmpty,
  Stat, TableWrap, useAsync, usePaged, when,
} from '../../components/ui'

// The source table is filtered and paged rather than rendered whole: this
// deployment reports ~1,000 connected sources, and one row each produced a page
// too large to paint smoothly and impossible to search by eye.
function SourceTable({ sources }) {
  const paged = usePaged(sources, { pageSize: 25, fields: ['name', 'source_id', 'kind', 'connector', 'status'] })
  return (
    <>
      <ListControls paged={paged} placeholder="Filter sources by name, kind or status…" />
      <TableWrap>
        <table className="table-base">
          <thead><tr><th>Source</th><th>Kind</th><th>Status</th><th>Last sync</th></tr></thead>
          <tbody>
            {paged.rows.map((s, i) => (
              <tr key={s.source_id || i}>
                <td className="text-slate-200">{s.name || s.source_id}</td>
                <td className="text-xs font-mono">{s.kind || s.connector || '—'}</td>
                <td>
                  <Badge tone={{ healthy: 'success', connected: 'success', degraded: 'warn', failed: 'danger' }[s.status] || 'default'}>
                    {s.status || 'unknown'}
                  </Badge>
                </td>
                <td className="text-xs">{when(s.last_synced_at || s.last_sync_at)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </TableWrap>
      {paged.matched === 0 && (
        <p className="text-xs text-slate-500 py-3">No source matches “{paged.query}”.</p>
      )}
      <Pager paged={paged} />
    </>
  )
}

export default function AdminSync() {
  const [refresh, setRefresh] = useState(0)
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState('')
  const state = useAsync(async () => {
    const [sources, statusInfo, overview, refreshes] = await Promise.all([
      api.syncSources().catch(() => null),
      api.syncSourcesStatus().catch(() => null),
      api.orgOverview().catch(() => null),
      api.orgRefreshes().catch(() => null),
    ])
    return { sources, statusInfo, overview, refreshes }
  }, [refresh])
  const reload = () => setRefresh((n) => n + 1)

  const syncNow = async () => {
    setBusy(true); setError('')
    try { await api.syncNow() } catch (e) { setError(String(e.message || e)) }
    finally { setBusy(false); reload() }
  }

  return (
    <>
      <PageHeader title="Sync" subtitle="Connected sources and the enterprise model built from them">
        <button className="btn" onClick={syncNow} disabled={busy}>{busy ? 'Synchronizing…' : 'Sync all sources'}</button>
      </PageHeader>
      {error && <div className="mb-4"><Notice tone="danger" onDismiss={() => setError('')}>{error}</Notice></div>}
      <AsyncSection state={state} empty="The synchronization layer is not active.">
        {({ sources, overview, refreshes }) => {
          const sourceList = sources?.sources || (Array.isArray(sources) ? sources : [])
          const refreshList = refreshes?.refreshes || (Array.isArray(refreshes) ? refreshes : [])
          return (
            <div className="space-y-5">
              <div className="grid gap-4 md:grid-cols-4">
                <Stat label="Sources" value={sourceList.length} />
                <Stat label="Entities modeled" value={overview?.entities_total} />
                <Stat label="Freshness" value={overview?.knowledge_freshness?.status || '—'}
                      tone={overview?.knowledge_freshness?.status === 'fresh' ? 'fg-success' : 'fg-warn'} />
                <Stat label="Last update" value={overview?.knowledge_freshness?.last_updated_at
                  ? when(overview.knowledge_freshness.last_updated_at) : '—'} />
              </div>

              <Panel title="Sources" subtitle={`${sourceList.length} registered`}>
                {sourceList.length === 0
                  ? <PanelEmpty text="No sources registered." />
                  : <SourceTable sources={sourceList} />}
              </Panel>

              <div className="grid gap-5 lg:grid-cols-2">
                <Panel title="Entities by kind">
                  {!overview?.by_kind || Object.keys(overview.by_kind).length === 0
                    ? <PanelEmpty text="Nothing modeled yet." />
                    : <div className="grid grid-cols-2 gap-2 text-sm">
                        {Object.entries(overview.by_kind).map(([k, v]) => (
                          <div key={k} className="flex justify-between gap-2">
                            <span className="text-slate-500 capitalize">{k.replace(/_/g, ' ')}</span>
                            <span className="text-slate-200 tabular-nums">{v}</span>
                          </div>
                        ))}
                      </div>}
                </Panel>
                <Panel title="Recent refreshes">
                  {refreshList.length === 0 ? <PanelEmpty text="No refreshes recorded." /> : (
                    <ul className="space-y-2 text-sm">
                      {refreshList.slice(0, 10).map((r, i) => (
                        <li key={i} className="flex justify-between gap-3">
                          <span className="text-slate-300 min-w-0 truncate">{r.source || r.name || r.kind || 'refresh'}</span>
                          <span className="text-slate-500 text-xs shrink-0">{when(r.refreshed_at || r.at || r.finished_at)}</span>
                        </li>
                      ))}
                    </ul>
                  )}
                </Panel>
              </div>
            </div>
          )
        }}
      </AsyncSection>
    </>
  )
}
