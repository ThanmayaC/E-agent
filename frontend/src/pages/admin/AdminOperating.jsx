// Enterprise AI Operating Layer — the operational view of the platform's
// agents, tools, prompts, evaluation, governance, memory lifecycle, and
// workflows. Admin-only, and composed entirely from the layers' own status
// surfaces. The Executive Workspace never shows any of this.
import { useState } from 'react'
import { api } from '../../api/client'
import {
  AsyncSection, Badge, PageHeader, Panel, PanelEmpty, Stat, Tabs, useAsync,
  when,
} from '../../components/ui'

const VERDICT_TONE = {
  healthy: 'success', degraded: 'warn', unhealthy: 'danger', unknown: 'default',
}

const STATE_TONE = {
  healthy: 'success', current: 'success', ready: 'success', accept: 'success',
  degraded: 'warn', aging: 'warn', catalogue: 'default', unknown: 'default',
  unavailable: 'danger', unhealthy: 'danger', stale: 'danger', reject: 'danger',
}

const TABS = [
  ['overview', 'Overview'], ['agents', 'Agents'], ['tools', 'Tools'],
  ['prompts', 'Prompts'], ['evaluation', 'Evaluation'],
  ['governance', 'Governance'], ['workflows', 'Workflows'],
  ['memory', 'Memory'],
]

export default function AdminOperating() {
  const [tab, setTab] = useState('overview')
  const [refresh, setRefresh] = useState(0)
  const reload = () => setRefresh((n) => n + 1)

  const state = useAsync(async () => {
    const [obs, agents, tools, prompts, evaluation, governance, workflows,
           memory, usage] = await Promise.all([
      api.opsObservability().catch(() => null),
      api.opsAgents().catch(() => null),
      api.opsTools().catch(() => null),
      api.opsPrompts().catch(() => null),
      api.opsEvaluation().catch(() => null),
      api.opsGovernance().catch(() => null),
      api.opsWorkflows().catch(() => null),
      api.opsMemoryLifecycle().catch(() => null),
      api.opsModelUsage().catch(() => null),
    ])
    return { obs, agents, tools, prompts, evaluation, governance, workflows,
             memory, usage }
  }, [refresh])

  return (
    <>
      <PageHeader title="AI Operating Layer"
                  subtitle="Agents, tools, prompts, evaluation, governance, and memory — the operational layers around the Enterprise Brain">
        <button className="btn-ghost" onClick={reload}>Refresh</button>
      </PageHeader>

      <AsyncSection state={state} empty="The operating layer is not available.">
        {(data) => (
          <div className="space-y-5">
            <Tabs active={tab} onChange={setTab}
                  tabs={TABS.map(([value, label]) => ({ value, label }))} />
            {tab === 'overview' && <Overview {...data} />}
            {tab === 'agents' && <Agents data={data.agents} onRun={reload} />}
            {tab === 'tools' && <Tools data={data.tools} />}
            {tab === 'prompts' && <Prompts data={data.prompts} />}
            {tab === 'evaluation' && <Evaluation data={data.evaluation} />}
            {tab === 'governance' && <Governance data={data.governance} usage={data.usage} />}
            {tab === 'workflows' && <Workflows data={data.workflows} onRun={reload} />}
            {tab === 'memory' && <Memory data={data.memory} />}
          </div>
        )}
      </AsyncSection>
    </>
  )
}

function Overview({ obs, agents, tools, prompts, evaluation, workflows }) {
  const verdict = obs?.verdict || {}
  return (
    <div className="space-y-5">
      <Panel title="Platform health">
        <div className="flex items-center gap-3 mb-4">
          <Badge tone={VERDICT_TONE[verdict.state] || 'default'}>
            {(verdict.state || 'unknown').toUpperCase()}
          </Badge>
          <span className="text-sm text-slate-500">
            {verdict.concerns?.length ? `${verdict.concerns.length} concern(s)` : 'No active concerns'}
          </span>
        </div>
        {verdict.concerns?.length > 0 && (
          <ul className="space-y-1 text-sm">
            {verdict.concerns.map((c, i) => (
              <li key={i} className={c.startsWith('critical:') ? 'text-rose-300' : 'text-amber-300'}>
                {c}
              </li>
            ))}
          </ul>
        )}
      </Panel>
      <div className="grid gap-4 md:grid-cols-4">
        <Stat label="Agents" value={agents?.status?.total ?? '—'}
              hint={`${agents?.status?.executable ?? 0} executable`} />
        <Stat label="Tools" value={tools?.status?.total ?? '—'}
              hint={`${tools?.status?.available ?? 0} available`} />
        <Stat label="Prompts" value={prompts?.status?.total ?? '—'}
              hint={`${prompts?.status?.governed ?? 0} governed`} />
        <Stat label="Workflows" value={workflows?.status?.total ?? '—'}
              hint={`${workflows?.status?.available ?? 0} runnable`} />
      </div>
      <div className="grid gap-4 md:grid-cols-2">
        <Stat label="Outputs evaluated" value={evaluation?.status?.evaluated ?? 0}
              hint={evaluation?.status?.acceptance_rate != null
                ? `${Math.round(evaluation.status.acceptance_rate * 100)}% accepted` : 'no data yet'} />
        <Stat label="Latency tracked ops"
              value={Object.keys(obs?.sections?.processing_latency?.operations || {}).length} />
      </div>
    </div>
  )
}

function Agents({ data, onRun }) {
  const [busy, setBusy] = useState('')
  const agents = data?.agents || []
  const run = async (id) => {
    setBusy(id)
    try { await api.opsRunAgent(id, { goal: 'manual run' }) } catch { /* surfaced via reload */ }
    finally { setBusy(''); onRun() }
  }
  return (
    <Panel title={`Agents — ${data?.status?.total ?? 0} registered, ${data?.status?.executable ?? 0} executable`}>
      <div className="overflow-x-auto">
        <table className="table-base">
          <thead><tr><th>Agent</th><th>Capabilities</th><th>Brain role</th><th>Policy</th><th>Health</th><th></th></tr></thead>
          <tbody>
            {agents.map((a) => (
              <tr key={a.id}>
                <td className="text-slate-200">{a.name}
                  <div className="text-[11px] text-slate-600 truncate max-w-[240px]">{a.description}</div></td>
                <td className="text-xs">{(a.capabilities || []).join(', ')}</td>
                <td><Badge tone="default">{a.brain_role}</Badge></td>
                <td className="text-xs text-slate-500">{a.execution_policy}<br />{a.approval_policy}</td>
                <td><Badge tone={STATE_TONE[a.health?.state] || 'default'}>{a.health?.state}</Badge>
                  {a.health?.runs > 0 && <span className="text-[11px] text-slate-600 ml-1">{a.health.runs} runs</span>}</td>
                <td>{a.executable && a.execution_policy !== 'on_demand' && (
                  <button className="btn-ghost text-xs px-2 py-1" disabled={busy === a.id}
                          onClick={() => run(a.id)}>{busy === a.id ? '…' : 'Run'}</button>)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </Panel>
  )
}

function Tools({ data }) {
  const tools = data?.tools || []
  return (
    <Panel title={`Tools — ${data?.status?.total ?? 0} registered`}>
      <div className="overflow-x-auto">
        <table className="table-base">
          <thead><tr><th>Tool</th><th>Capability</th><th>Permissions</th><th>Status</th><th>Calls</th></tr></thead>
          <tbody>
            {tools.map((t) => (
              <tr key={t.id}>
                <td className="text-slate-200 font-mono text-xs">{t.id}</td>
                <td><Badge tone="default">{t.capability}</Badge></td>
                <td className="text-[11px] text-slate-500">{(t.permissions || []).join(', ')}</td>
                <td><Badge tone={t.available ? STATE_TONE[t.execution_status?.status] || 'success' : 'danger'}>
                  {t.available ? t.execution_status?.status : 'unavailable'}</Badge></td>
                <td className="text-xs tabular-nums">{t.execution_status?.calls ?? 0}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </Panel>
  )
}

function Prompts({ data }) {
  const prompts = data?.prompts || []
  const byDomain = {}
  for (const p of prompts) (byDomain[p.domain] ||= []).push(p)
  return (
    <div className="space-y-4">
      <div className="grid gap-4 md:grid-cols-3">
        <Stat label="Prompts" value={data?.status?.total ?? 0} />
        <Stat label="Governed" value={data?.status?.governed ?? 0}
              hint="compliance-owned wording" />
        <Stat label="Owners" value={(data?.status?.owners || []).length} />
      </div>
      {Object.entries(byDomain).map(([domain, list]) => (
        <Panel key={domain} title={domain}>
          <ul className="space-y-1.5 text-sm">
            {list.map((p) => (
              <li key={p.id} className="flex items-center justify-between gap-2">
                <span className="font-mono text-xs text-slate-300">{p.id}</span>
                <span className="flex items-center gap-2">
                  {p.governed && <Badge tone="warn">governed</Badge>}
                  <span className="text-[11px] text-slate-600">v{p.version} · {p.owner}</span>
                </span>
              </li>
            ))}
          </ul>
        </Panel>
      ))}
    </div>
  )
}

function Evaluation({ data }) {
  const s = data?.status || {}
  return (
    <div className="space-y-4">
      <div className="grid gap-4 md:grid-cols-4">
        <Stat label="Enabled" value={s.enabled ? 'yes' : 'no'}
              tone={s.enabled ? 'fg-success' : 'fg-muted'} />
        <Stat label="Evaluators" value={s.evaluators ?? 0} />
        <Stat label="Evaluated" value={s.evaluated ?? 0} />
        <Stat label="Acceptance"
              value={s.acceptance_rate != null ? `${Math.round(s.acceptance_rate * 100)}%` : '—'} />
      </div>
      <Panel title="Evaluators">
        <div className="grid gap-2 sm:grid-cols-2 text-sm">
          {(data?.evaluators || []).map((e) => (
            <div key={e.name} className="flex items-start justify-between gap-2">
              <div className="min-w-0">
                <div className="text-slate-300">{e.name}</div>
                <div className="text-[11px] text-slate-600 truncate">{e.description}</div>
              </div>
              <span className="text-[11px] text-slate-500 shrink-0">
                ≥{e.threshold} → {e.on_failure}</span>
            </div>
          ))}
        </div>
      </Panel>
    </div>
  )
}

function Governance({ data, usage }) {
  if (!data) return <PanelEmpty text="Governance is disabled." />
  return (
    <div className="space-y-4">
      <div className="grid gap-4 md:grid-cols-4">
        <Stat label="Governance" value={data.enabled ? 'on' : 'off'}
              tone={data.enabled ? 'fg-success' : 'fg-warn'} />
        <Stat label="Roles" value={(data.roles || []).length} />
        <Stat label="Audit entries" value={data.audit_entries ?? 0} />
        <Stat label="LLM calls" value={usage?.summary?.calls ?? 0}
              hint={`${usage?.summary?.tokens_total ?? 0} tokens`} />
      </div>
      <Panel title="Roles and permissions">
        <div className="space-y-2">
          {(data.roles || []).map((r) => (
            <div key={r.name} className="text-sm">
              <span className="text-slate-200 font-medium">{r.name}</span>
              <div className="text-[11px] text-slate-500 mt-0.5">{(r.permissions || []).join(' · ')}</div>
            </div>
          ))}
        </div>
      </Panel>
      <Panel title="Security policy">
        <div className="grid grid-cols-2 gap-2 text-sm">
          {Object.entries(data.security_policy || {}).map(([k, v]) => (
            <div key={k} className="flex items-center justify-between gap-2">
              <span className="text-slate-500 text-xs">{k.replace(/_/g, ' ')}</span>
              <Badge tone={v ? 'success' : 'danger'}>{v ? 'yes' : 'no'}</Badge>
            </div>
          ))}
        </div>
      </Panel>
      <Panel title="Retention policy">
        <div className="grid grid-cols-2 gap-2 text-sm">
          {Object.entries(data.retention_days || {}).map(([k, v]) => (
            <div key={k} className="flex justify-between gap-2">
              <span className="text-slate-500 capitalize">{k.replace(/_/g, ' ')}</span>
              <span className="text-slate-300 tabular-nums">{v === 0 ? 'never' : `${v} days`}</span>
            </div>
          ))}
        </div>
      </Panel>
    </div>
  )
}

function Workflows({ data, onRun }) {
  const [busy, setBusy] = useState('')
  const workflows = data?.workflows || []
  const run = async (id) => {
    setBusy(id)
    try { await api.opsRunWorkflow(id) } catch { /* surfaced via reload */ }
    finally { setBusy(''); onRun() }
  }
  return (
    <Panel title={`Autonomous workflows — ${data?.status?.total ?? 0} declared, ${data?.status?.available ?? 0} runnable`}>
      <div className="overflow-x-auto">
        <table className="table-base">
          <thead><tr><th>Workflow</th><th>Trigger</th><th>Agents</th><th>Approval</th><th>Status</th><th></th></tr></thead>
          <tbody>
            {workflows.map((w) => (
              <tr key={w.id}>
                <td className="text-slate-200">{w.name}
                  <div className="text-[11px] text-slate-600 truncate max-w-[240px]">{w.description}</div></td>
                <td className="text-xs">{w.trigger}<div className="text-[11px] text-slate-600">{w.schedule || w.event}</div></td>
                <td className="text-[11px] text-slate-500">{(w.agents || []).join(', ') || '—'}</td>
                <td><Badge tone={w.approval_policy === 'none' ? 'default' : 'warn'}>{w.approval_policy}</Badge></td>
                <td><Badge tone={w.available ? 'success' : 'default'}>{w.available ? 'runnable' : 'planned'}</Badge></td>
                <td>{w.available && (
                  <button className="btn-ghost text-xs px-2 py-1" disabled={busy === w.id}
                          onClick={() => run(w.id)}>{busy === w.id ? '…' : 'Run'}</button>)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </Panel>
  )
}

function Memory({ data }) {
  if (!data) return <PanelEmpty text="Memory lifecycle is not available." />
  return (
    <div className="space-y-4">
      <div className="grid gap-4 md:grid-cols-3">
        <Stat label="Knowledge items" value={data.total_items ?? 0} />
        <Stat label="Stale items" value={data.stale_items ?? 0}
              tone={(data.stale_items ?? 0) > 0 ? 'fg-warn' : 'fg-primary'} />
        <Stat label="Archived events" value={data.archived_events ?? 0} />
      </div>
      <Panel title="Knowledge freshness">
        <div className="overflow-x-auto">
          <table className="table-base">
            <thead><tr><th>Class</th><th>State</th><th>Items</th><th>Stale</th><th>Last updated</th></tr></thead>
            <tbody>
              {(data.freshness || []).map((f) => (
                <tr key={f.class}>
                  <td className="text-slate-200 capitalize">{f.class}</td>
                  <td><Badge tone={STATE_TONE[f.state] || 'default'}>{f.state}</Badge></td>
                  <td className="text-xs tabular-nums">{f.items}</td>
                  <td className="text-xs tabular-nums">{f.stale_items}</td>
                  <td className="text-xs">{f.last_updated_at ? when(f.last_updated_at) : '—'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </Panel>
    </div>
  )
}
