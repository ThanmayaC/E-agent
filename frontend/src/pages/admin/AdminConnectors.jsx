// Enterprise Data Sources — the Connector Framework's administration
// surface. Administrators register a source once here; the Runtime keeps it
// synchronized from then on. This page is deliberately Admin-only: the
// Executive Workspace receives fresh reports and insights and is never asked
// to know that a connector exists.
import { useState } from 'react'
import { api } from '../../api/client'
import {
  AsyncSection, Badge, PageHeader, Panel, PanelEmpty, Stat, useAsync, when,
} from '../../components/ui'

const CADENCES = ['startup', '15m', 'hourly', 'daily', 'weekly', 'manual']

const HEALTH_TONE = {
  healthy: 'success', degraded: 'warn', unreachable: 'danger',
  unconfigured: 'warn', disconnected: 'default', unknown: 'default',
}

const STATUS_TONE = {
  completed: 'success', degraded: 'warn', failed: 'danger', skipped: 'default',
}

const blank = {
  name: '', kind: 'folder', location: '', cadence: 'hourly', description: '',
  auth: { kind: 'none', ref: '' }, options: '',
}

// The platform holds sources in two registries — this framework's own, and
// the Synchronization Layer's (where document folders and the enterprise
// corpus live). Both are real; only the former is administered from here.
const originHint = (byOrigin) => {
  if (!byOrigin) return ''
  const own = byOrigin.connector_framework ?? 0
  const sync = byOrigin.sync_layer ?? 0
  if (!sync) return 'all managed by the connector framework'
  return `${own} connector · ${sync} synchronization layer`
}

export default function AdminConnectors() {
  const [refresh, setRefresh] = useState(0)
  const [busy, setBusy] = useState('')
  const [error, setError] = useState('')
  const [notice, setNotice] = useState('')
  const [form, setForm] = useState(blank)
  const [showForm, setShowForm] = useState(false)

  const state = useAsync(async () => {
    const [overview, sources, runs, failures] = await Promise.all([
      api.connectorsOverview().catch(() => null),
      api.connectorSources().catch(() => null),
      api.connectorRuns('', 20).catch(() => null),
      api.connectorFailures('', 10).catch(() => null),
    ])
    return { overview, sources, runs, failures }
  }, [refresh])

  const reload = () => setRefresh((n) => n + 1)

  const act = async (label, fn) => {
    setBusy(label); setError(''); setNotice('')
    try {
      const result = await fn()
      if (result?.ok === false) setError(result.detail || 'Connection failed')
      else if (result?.detail) setNotice(result.detail)
      else if (result?.status) setNotice(`Sync ${result.status} — ${result.packages ?? 0} package(s)`)
      else if (result?.count !== undefined) setNotice(`Discovered ${result.count} item(s)`)
    } catch (e) {
      setError(String(e.message || e))
    } finally {
      setBusy(''); reload()
    }
  }

  const submit = async (event) => {
    event.preventDefault()
    let options = {}
    if (form.options.trim()) {
      try { options = JSON.parse(form.options) }
      catch { setError('Options must be valid JSON'); return }
    }
    await act('register', () => api.registerConnector({
      name: form.name, kind: form.kind, location: form.location,
      cadence: form.cadence, description: form.description,
      auth: form.auth, options,
    }))
    setForm(blank); setShowForm(false)
  }

  return (
    <>
      <PageHeader title="Enterprise Data Sources"
                  subtitle="Configure a source once — the Runtime synchronizes it from then on">
        <button className="btn-ghost" onClick={() => setShowForm((s) => !s)}>
          {showForm ? 'Cancel' : 'Register source'}
        </button>
        <button className="btn" disabled={busy === 'sync-all'}
                onClick={() => act('sync-all', () => api.syncAllConnectors())}>
          {busy === 'sync-all' ? 'Synchronizing…' : 'Sync all'}
        </button>
      </PageHeader>

      {error && <div className="card-pad border-rose-500/40 text-rose-300 text-sm mb-4">{error}</div>}
      {notice && <div className="card-pad border-emerald-500/40 text-emerald-300 text-sm mb-4">{notice}</div>}

      <AsyncSection state={state}
                    empty="The Enterprise Connector Framework is disabled in this deployment.">
        {({ overview, sources, runs, failures }) => {
          const list = sources?.sources || []
          const status = overview?.sources || sources?.status || {}
          const catalogue = overview?.catalogue || []
          const available = catalogue.filter((c) => c.available)
          const runList = runs?.runs || []
          const failureList = failures?.failures || []

          return (
            <div className="space-y-5">
              <div className="grid gap-4 md:grid-cols-4">
                <Stat label="Data sources" value={status.total ?? 0}
                      hint={originHint(status.by_origin)} />
                <Stat label="Healthy" value={status.healthy ?? 0}
                      tone="fg-success" />
                <Stat label="Need attention" value={status.needs_attention ?? 0}
                      tone={(status.needs_attention ?? 0) > 0 ? 'fg-warn' : 'fg-primary'} />
                <Stat label="Records ingested" value={status.items_total ?? 0}
                      hint="across every connected source" />
              </div>

              {showForm && (
                <Panel title="Register an enterprise data source">
                  <form className="grid gap-3 md:grid-cols-2" onSubmit={submit}>
                    <label className="text-sm">
                      <span className="text-slate-500 text-xs block mb-1">Name</span>
                      <input className="input w-full" required value={form.name}
                             onChange={(e) => setForm({ ...form, name: e.target.value })} />
                    </label>
                    <label className="text-sm">
                      <span className="text-slate-500 text-xs block mb-1">Connector</span>
                      <select className="input w-full" value={form.kind}
                              onChange={(e) => setForm({ ...form, kind: e.target.value })}>
                        {available.map((c) => (
                          <option key={c.kind} value={c.kind}>{c.title}</option>
                        ))}
                      </select>
                    </label>
                    <label className="text-sm md:col-span-2">
                      <span className="text-slate-500 text-xs block mb-1">
                        Location — folder path, file path, or host. Never a credentialed URL.
                      </span>
                      <input className="input w-full" value={form.location}
                             onChange={(e) => setForm({ ...form, location: e.target.value })} />
                    </label>
                    <label className="text-sm">
                      <span className="text-slate-500 text-xs block mb-1">Refresh cadence</span>
                      <select className="input w-full" value={form.cadence}
                              onChange={(e) => setForm({ ...form, cadence: e.target.value })}>
                        {CADENCES.map((c) => <option key={c} value={c}>{c}</option>)}
                      </select>
                    </label>
                    <label className="text-sm">
                      <span className="text-slate-500 text-xs block mb-1">
                        Credential reference — an environment variable name
                      </span>
                      <input className="input w-full" placeholder="EDIP_WAREHOUSE_URL"
                             value={form.auth.ref}
                             onChange={(e) => setForm({
                               ...form,
                               auth: { kind: e.target.value ? 'env' : 'none', ref: e.target.value },
                             })} />
                    </label>
                    <label className="text-sm md:col-span-2">
                      <span className="text-slate-500 text-xs block mb-1">
                        Options (JSON) — e.g. {'{"category": "sop", "recursive": true}'}
                      </span>
                      <input className="input w-full font-mono text-xs" value={form.options}
                             onChange={(e) => setForm({ ...form, options: e.target.value })} />
                    </label>
                    <div className="md:col-span-2 flex gap-2">
                      <button className="btn" type="submit" disabled={busy === 'register'}>
                        {busy === 'register' ? 'Registering…' : 'Register'}
                      </button>
                      <span className="text-xs text-slate-600 self-center">
                        The platform never stores credentials — only the variable name.
                      </span>
                    </div>
                  </form>
                </Panel>
              )}

              <Panel title="Connected sources">
                {list.length === 0 ? <PanelEmpty text="No data sources registered yet." /> : (
                  <div className="overflow-x-auto">
                    <table className="table-base">
                      <thead>
                        <tr>
                          <th>Source</th><th>Connector</th><th>Health</th>
                          <th>Last sync</th><th>Items</th><th>Actions</th>
                        </tr>
                      </thead>
                      <tbody>
                        {list.map((s) => (
                          <tr key={s.connector_id}>
                            <td>
                              <div className="text-slate-200">{s.name}</div>
                              <div className="text-[11px] text-slate-600 truncate max-w-[240px]">
                                {s.location || s.description || '—'}
                              </div>
                            </td>
                            <td className="text-xs font-mono">
                              {s.kind}
                              {s.origin === 'sync_layer' && (
                                <div className="mt-1"><Badge>sync layer</Badge></div>
                              )}
                            </td>
                            <td>
                              <Badge tone={HEALTH_TONE[s.health] || 'default'}>
                                {s.enabled ? s.health : 'disabled'}
                              </Badge>
                              {s.health_detail && (
                                <div className="text-[11px] text-slate-600 mt-1 max-w-[220px] truncate">
                                  {s.health_detail}
                                </div>
                              )}
                            </td>
                            <td className="text-xs">
                              {when(s.last_synced_at)}
                              <div className="text-[11px] text-slate-600">{s.cadence}</div>
                            </td>
                            <td className="text-xs tabular-nums">{s.items_total ?? 0}</td>
                            <td>
                              {s.read_only ? (
                                <span className="text-[11px] fg-muted">
                                  Managed under Sync — administered there, not here.
                                </span>
                              ) : (
                              <div className="flex flex-wrap gap-1">
                                <button className="btn-ghost text-xs px-2 py-1"
                                        disabled={busy === `test-${s.connector_id}`}
                                        onClick={() => act(`test-${s.connector_id}`,
                                          () => api.testConnector(s.connector_id))}>
                                  Test
                                </button>
                                <button className="btn-ghost text-xs px-2 py-1"
                                        disabled={busy === `disc-${s.connector_id}`}
                                        onClick={() => act(`disc-${s.connector_id}`,
                                          () => api.discoverConnector(s.connector_id))}>
                                  Discover
                                </button>
                                <button className="btn-ghost text-xs px-2 py-1"
                                        disabled={busy === `sync-${s.connector_id}`}
                                        onClick={() => act(`sync-${s.connector_id}`,
                                          () => api.syncConnector(s.connector_id))}>
                                  Sync
                                </button>
                                <button className="btn-ghost text-xs px-2 py-1"
                                        onClick={() => act(`toggle-${s.connector_id}`,
                                          () => api.updateConnector(s.connector_id,
                                            { enabled: !s.enabled }))}>
                                  {s.enabled ? 'Disable' : 'Enable'}
                                </button>
                                <button className="btn-ghost text-xs px-2 py-1 fg-danger"
                                        onClick={() => act(`del-${s.connector_id}`,
                                          () => api.deleteConnector(s.connector_id))}>
                                  Delete
                                </button>
                              </div>
                              )}
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                )}
              </Panel>

              <div className="grid gap-5 lg:grid-cols-2">
                <Panel title="Recent synchronizations">
                  {runList.length === 0 ? <PanelEmpty text="No synchronizations recorded." /> : (
                    <ul className="space-y-2 text-sm">
                      {runList.map((r) => (
                        <li key={r.run_id} className="flex items-center justify-between gap-3">
                          <span className="text-slate-300 min-w-0 truncate">{r.connector}</span>
                          <span className="flex items-center gap-2 shrink-0">
                            <span className="text-[11px] text-slate-600">
                              {r.mode} · {r.packages ?? 0} pkg
                            </span>
                            <Badge tone={STATUS_TONE[r.status] || 'default'}>{r.status}</Badge>
                            <span className="text-[11px] text-slate-600">{when(r.finished_at)}</span>
                          </span>
                        </li>
                      ))}
                    </ul>
                  )}
                </Panel>

                <Panel title="Failures">
                  {failureList.length === 0
                    ? <PanelEmpty text="No failures — every source is synchronizing." />
                    : (
                      <ul className="space-y-2 text-sm">
                        {failureList.map((f) => (
                          <li key={f.failure_id}>
                            <div className="flex justify-between gap-2">
                              <span className="text-slate-300">{f.connector}</span>
                              <span className="text-[11px] text-slate-600">{when(f.at)}</span>
                            </div>
                            <div className="text-[11px] text-rose-300/80 mt-0.5">{f.error}</div>
                          </li>
                        ))}
                      </ul>
                    )}
                </Panel>
              </div>

              <Panel title="Connector catalogue">
                <div className="grid gap-2 sm:grid-cols-2 lg:grid-cols-3 text-sm">
                  {catalogue.map((c) => (
                    <div key={c.kind} className="flex items-start justify-between gap-2">
                      <div className="min-w-0">
                        <div className="text-slate-300">{c.title || c.kind}</div>
                        <div className="text-[11px] text-slate-600 truncate">
                          {c.description || c.unavailable_reason || '—'}
                        </div>
                      </div>
                      <Badge tone={c.available ? 'success' : 'default'}>
                        {c.available ? 'available' : 'planned'}
                      </Badge>
                    </div>
                  ))}
                </div>
              </Panel>
            </div>
          )
        }}
      </AsyncSection>
    </>
  )
}
