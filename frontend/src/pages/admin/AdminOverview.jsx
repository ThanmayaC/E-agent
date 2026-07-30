// Admin Console — the subsystem console. Every card here is a real platform
// subsystem, and every number is read live from that subsystem when the page
// loads (see /intel/admin/subsystems). There are no placeholders: a subsystem
// that is not wired says so, and one that is reports its true runtime state.
import { Link } from 'react-router-dom'
import { api, fmt } from '../../api/client'
import { AsyncSection, Badge, PageHeader, useAsync } from '../../components/ui'

const GROUP_ORDER = ['Data', 'Intelligence', 'Integration', 'Operations']

// A subsystem whose card should deep-link to its own admin page.
const LINKS = {
  warehouse: '/admin/warehouse',
  analytics: '/admin/warehouse',
  ml: '/admin/models',
  runtime: '/admin/runtime',
  brain: '/admin/brain',
  knowledge_graph: '/admin/graph',
  llm: '/admin/llm',
  connectors: '/admin/data-sources',
  sync: '/admin/sync',
  workflows: '/admin/jobs',
}

const prettyKey = (k) => k.replace(/_/g, ' ').replace(/\bpct\b/, '%')

function MetricRow({ label, value }) {
  let shown = value
  if (typeof value === 'number') shown = fmt.num(value)
  else if (typeof value === 'boolean') shown = value ? 'yes' : 'no'
  else if (value === null || value === undefined || value === '') shown = '—'
  return (
    <div className="flex items-baseline justify-between gap-3 text-xs py-0.5">
      <span className="text-slate-500 truncate">{prettyKey(label)}</span>
      <span className="text-slate-200 font-mono tabular-nums shrink-0">{String(shown)}</span>
    </div>
  )
}

function SubsystemCard({ s }) {
  const link = LINKS[s.key]
  const metrics = Object.entries(s.metrics || {}).filter(
    ([, v]) => v !== null && v !== undefined && v !== '')
  const body = (
    <div className={`card-pad h-full ${link ? 'card-hover' : ''}`}>
      <div className="flex items-start justify-between gap-2">
        <div className="min-w-0">
          <div className="font-medium text-slate-100 truncate">{s.label}</div>
          <div className="text-[11px] text-slate-500 mt-0.5">{s.category}</div>
        </div>
        <Badge tone={s.available ? (s.healthy ? 'success' : 'warn') : 'danger'}>
          {s.available ? (s.healthy ? 'live' : 'degraded') : 'offline'}
        </Badge>
      </div>
      {metrics.length > 0 ? (
        <div className="mt-3 pt-3 border-t border-surface-border/60">
          {metrics.slice(0, 7).map(([k, v]) => <MetricRow key={k} label={k} value={v} />)}
        </div>
      ) : (
        <p className="text-xs text-slate-500 mt-3">{s.note || 'No metrics exposed.'}</p>
      )}
      {s.note && metrics.length > 0 && (
        <p className="text-[11px] text-slate-600 mt-2 leading-snug">{s.note}</p>
      )}
    </div>
  )
  return link ? <Link to={link} className="block">{body}</Link> : body
}

export default function AdminOverview() {
  const state = useAsync(() => api.intelSubsystems(), [])
  return (
    <div className="space-y-6">
      <PageHeader
        title="Subsystem Console"
        subtitle="Every platform subsystem with its live runtime state — read directly from the source, never cached or mocked."
      />
      <AsyncSection state={state}>
        {(data) => {
          const groups = data.groups || {}
          const order = [...GROUP_ORDER,
            ...Object.keys(groups).filter((g) => !GROUP_ORDER.includes(g))]
          return (
            <div className="space-y-6">
              <div className="flex flex-wrap items-center gap-3 text-sm">
                <Badge tone="success">{data.summary.available} live</Badge>
                {data.summary.unavailable > 0 &&
                  <Badge tone="danger">{data.summary.unavailable} offline</Badge>}
                <span className="text-slate-500">
                  {data.summary.total} subsystems · refreshed {String(data.generated_at).replace('T', ' ')}
                </span>
              </div>
              {order.filter((g) => groups[g]?.length).map((g) => (
                <div key={g}>
                  <div className="text-[11px] uppercase tracking-wider text-slate-500 mb-2">{g}</div>
                  <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
                    {groups[g].map((s) => <SubsystemCard key={s.key} s={s} />)}
                  </div>
                </div>
              ))}
            </div>
          )
        }}
      </AsyncSection>
    </div>
  )
}
