// Settings — business configuration only. Engineering configuration lives
// in the Admin Console.
import { useState } from 'react'
import { Link } from 'react-router-dom'
import { api } from '../api/client'
import {
  getNotifyPrefs, getTheme, isAdmin, setAdmin, setNotifyPref, setTheme,
} from '../lib/prefs'
import { Badge, PageHeader, Panel, PanelEmpty, timeAgo, useAsync } from '../components/ui'

const NOTIFY_KINDS = [
  ['critical_risk', 'Critical business risks'],
  ['portfolio_change', 'Portfolio health changes'],
  ['new_report', 'New reports'],
  ['recommendation', 'New recommendations'],
  ['task_deadline', 'Task deadlines'],
  ['workflow_failure', 'Analyses that need review'],
]

const THEMES = [
  ['midnight', 'Midnight', 'Deep blue-black — the default'],
  ['graphite', 'Graphite', 'Warm neutral dark'],
  ['daylight', 'Daylight', 'Bright light theme (V2.5)'],
]

function Toggle({ on, onChange }) {
  return (
    <button role="switch" aria-checked={on} onClick={() => onChange(!on)}
            className={`w-9 h-5 rounded-full transition-colors relative shrink-0 ${on ? 'bg-accent' : 'bg-surface-overlay'}`}>
      <span className={`absolute top-0.5 w-4 h-4 rounded-full bg-white transition-all ${on ? 'left-[18px]' : 'left-0.5'}`} />
    </button>
  )
}

export default function Settings() {
  const [notify, setNotify] = useState(getNotifyPrefs())
  const [theme, setThemeState] = useState(getTheme())
  const [admin, setAdminState] = useState(isAdmin())

  const org = useAsync(() => api.managerOrganization().catch(() => null), [])
  const provider = useAsync(() => api.copilotWorkspace().catch(() => null), [])
  const integrations = useAsync(() => api.integrations().catch(() => null), [])

  const flipNotify = (kind, on) => setNotify({ ...setNotifyPref(kind, on) })
  const pickTheme = (t) => { setTheme(t); setThemeState(t) }
  const flipAdmin = (on) => { setAdmin(on); setAdminState(on) }

  const orgData = org.data
  const providerInfo = provider.data?.provider || provider.data?.llm || null
  const slots = integrations.data?.integrations || integrations.data?.providers || integrations.data || null

  return (
    <>
      <PageHeader title="Settings" subtitle="Workspace configuration for your organization" />
      <div className="space-y-5 max-w-4xl">
        <Panel title="Organization">
          {!orgData || orgData.status !== 'active' ? (
            <PanelEmpty text="Organization data appears here once a business system is connected." />
          ) : (
            <div className="grid gap-4 sm:grid-cols-3">
              <div>
                <div className="eyebrow">Business entities</div>
                <div className="metric !text-xl mt-1">{orgData.entities_total ?? 0}</div>
              </div>
              <div>
                <div className="eyebrow">Connected systems</div>
                <div className="metric !text-xl mt-1">
                  {orgData.connected_systems?.connected ?? 0}
                  <span className="text-sm text-slate-500"> / {orgData.connected_systems?.total ?? 0}</span>
                </div>
              </div>
              <div>
                <div className="eyebrow">Knowledge freshness</div>
                <div className="mt-2">
                  <Badge tone={orgData.knowledge_freshness?.status === 'fresh' ? 'success' : 'warn'}>
                    {orgData.knowledge_freshness?.status || 'unknown'}
                  </Badge>
                  <span className="text-xs text-slate-500 ml-2">
                    {orgData.knowledge_freshness?.last_updated_at ? `updated ${timeAgo(orgData.knowledge_freshness.last_updated_at)}` : ''}
                  </span>
                </div>
              </div>
            </div>
          )}
        </Panel>

        <Panel title="Users">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-full bg-accent/20 text-accent text-sm font-semibold flex items-center justify-center">E</div>
            <div>
              <div className="text-sm text-slate-200">Executive <Badge tone="accent">you</Badge></div>
              <div className="text-xs text-slate-500">Full workspace access on this device</div>
            </div>
          </div>
          <div className="text-xs text-slate-600 mt-3">
            Team accounts, roles, and sign-in arrive in Version 2.
          </div>
        </Panel>

        <Panel title="Notification preferences">
          <div className="grid gap-2.5 sm:grid-cols-2">
            {NOTIFY_KINDS.map(([kind, label]) => (
              <div key={kind} className="flex items-center justify-between gap-3 text-sm text-slate-300">
                <span>{label}</span>
                <Toggle on={notify[kind] !== false} onChange={(on) => flipNotify(kind, on)} />
              </div>
            ))}
          </div>
          <div className="text-xs text-slate-600 mt-3">Muted kinds are hidden from your Notifications view.</div>
        </Panel>

        <Panel title="AI provider">
          {providerInfo ? (
            <div className="text-sm text-slate-300">
              The AI Copilot and executive briefs run on{' '}
              <span className="text-slate-100 font-medium">
                {providerInfo.provider || providerInfo.name || 'the configured provider'}
              </span>
              {providerInfo.model && <span className="text-slate-500"> ({providerInfo.model})</span>}.
            </div>
          ) : (
            <PanelEmpty text="No AI provider is configured, or the Copilot is turned off." />
          )}
          <div className="text-xs text-slate-600 mt-3">
            Changing the provider is an administrator action — it is configured per environment in the Admin Console → Model status.
          </div>
        </Panel>

        <Panel title="Data sources">
          {Array.isArray(slots) && slots.length > 0 ? (
            <ul className="space-y-2 mb-4">
              {slots.map((s, i) => (
                <li key={i} className="flex items-center justify-between text-sm">
                  <span className="text-slate-300 capitalize">{(s.name || s.kind || '').replace(/_/g, ' ')}</span>
                  <Badge tone={s.available || s.connected ? 'success' : 'default'}>
                    {s.available || s.connected ? 'connected' : s.status || 'available in V2'}
                  </Badge>
                </li>
              ))}
            </ul>
          ) : (
            <div className="text-sm text-slate-500 mb-4">
              Outlook, Teams, SharePoint, document folders, and databases connect in the Admin Console —
              once configured, the platform keeps itself up to date.
            </div>
          )}
          <Link to="/data" className="btn-ghost">Upload business data →</Link>
        </Panel>

        <Panel title="Theme">
          <div className="grid gap-3 sm:grid-cols-2">
            {THEMES.map(([value, name, hint]) => (
              <button key={value} onClick={() => pickTheme(value)}
                      className={`card-pad !p-4 text-left transition-colors ${
                        theme === value ? 'border-accent' : 'hover:border-accent/40'}`}>
                <div className="text-sm text-slate-200 font-medium">{name} {theme === value && <Badge tone="accent">active</Badge>}</div>
                <div className="text-xs text-slate-500 mt-1">{hint}</div>
              </button>
            ))}
          </div>
          <div className="text-xs text-slate-600 mt-3">Two dark themes and a light theme (Daylight) — switch anytime from the header too.</div>
        </Panel>

        <Panel title="Administration">
          <div className="flex items-center justify-between gap-3">
            <div>
              <div className="text-sm text-slate-300">Administrator mode on this device</div>
              <div className="text-xs text-slate-500 mt-0.5">
                Unlocks the Admin Console: runtime, scheduling, synchronization, diagnostics, and model status.
              </div>
            </div>
            <Toggle on={admin} onChange={flipAdmin} />
          </div>
          {admin && <Link to="/admin" className="btn-ghost mt-4">Open Admin Console →</Link>}
        </Panel>
      </div>
    </>
  )
}
