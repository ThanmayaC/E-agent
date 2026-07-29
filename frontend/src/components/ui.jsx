// Shared UI primitives (ShadCN-style: local, composable, Tailwind-driven)
import { useEffect, useState } from 'react'

export function PageHeader({ title, subtitle, children }) {
  return (
    <div className="flex items-end justify-between mb-6 gap-4 flex-wrap">
      <div>
        <h1 className="text-2xl font-bold text-slate-100">{title}</h1>
        {subtitle && <p className="text-sm text-slate-500 mt-1">{subtitle}</p>}
      </div>
      {children}
    </div>
  )
}

export function Badge({ tone = 'default', children }) {
  const tones = {
    default: 'chip-neutral',
    success: 'chip-success',
    danger: 'chip-danger',
    warn: 'chip-warn',
    info: 'chip-info',
    ai: 'chip-ai',
    accent: 'chip-accent',
  }
  return (
    <span className={`chip ${tones[tone] || tones.default}`}>
      {children}
    </span>
  )
}

export const severityTone = (s) =>
  ({ critical: 'danger', high: 'danger', medium: 'warn', low: 'info', info: 'default' }[s] || 'default')

export function Spinner({ label = 'Loading…' }) {
  return (
    <div className="flex items-center gap-3 text-slate-500 text-sm py-12 justify-center">
      <span className="w-4 h-4 border-2 border-slate-600 border-t-accent rounded-full animate-spin" />
      {label}
    </div>
  )
}

export function Empty({ title = 'Nothing here yet', hint }) {
  return (
    <div className="card-pad text-center py-14">
      <div className="text-slate-400 font-medium">{title}</div>
      {hint && <div className="text-sm text-slate-600 mt-1">{hint}</div>}
    </div>
  )
}

export function ErrorBox({ error }) {
  return <div className="card-pad border-rose-500/40 text-rose-300 text-sm">{String(error)}</div>
}

export function useAsync(fn, deps) {
  const [state, setState] = useState({ loading: true, data: null, error: null })
  useEffect(() => {
    let live = true
    setState({ loading: true, data: null, error: null })
    fn()
      .then((data) => live && setState({ loading: false, data, error: null }))
      .catch((error) => live && setState({ loading: false, data: null, error }))
    return () => { live = false }
  }, deps) // eslint-disable-line react-hooks/exhaustive-deps
  return state
}

export function AsyncSection({ state, children, empty = 'No data — run an analysis first.' }) {
  if (state.loading) return <Spinner />
  if (state.error) return <ErrorBox error={state.error.message || state.error} />
  const isEmpty = !state.data || (Array.isArray(state.data) && state.data.length === 0)
  if (isEmpty) return <Empty title={empty} />
  return children(state.data)
}

// ---------------------------------------------------------------------------
// Executive design language: metric stats, health rings, trends, panels.

export const healthTone = (h) =>
  h == null ? 'fg-muted' : h >= 70 ? 'fg-success' : h >= 50 ? 'fg-warn' : 'fg-danger'

export function Stat({ label, value, tone = 'fg-primary', hint }) {
  // Guard: React throws if a value is an object/array. Coerce non-primitives to
  // a count/string so one bad field can never blank the page.
  const shown = value == null ? '—'
    : Array.isArray(value) ? value.length
    : typeof value === 'object' ? JSON.stringify(value)
    : value
  return (
    <div className="card-pad">
      <div className="eyebrow">{label}</div>
      <div className={`metric mt-1.5 ${tone}`}>{shown}</div>
      {hint && <div className="text-xs text-slate-500 mt-1">{hint}</div>}
    </div>
  )
}

export function Panel({ title, action, children, className = '' }) {
  return (
    <section className={`card-pad ${className}`}>
      <div className="flex items-center justify-between mb-3 gap-3">
        <h2 className="text-sm font-semibold text-slate-200">{title}</h2>
        {action}
      </div>
      {children}
    </section>
  )
}

export const PanelEmpty = ({ text }) => <div className="text-sm text-slate-600">{text}</div>

// Signature element: the health ring. One glance — score, band, motion-free.
export function HealthRing({ score, size = 56, label }) {
  const r = (size - 8) / 2
  const c = 2 * Math.PI * r
  const pct = score == null ? 0 : Math.max(0, Math.min(100, score))
  const stroke = score == null ? '#334155' : score >= 70 ? '#34d399' : score >= 50 ? '#fbbf24' : '#fb7185'
  return (
    <div className="relative inline-flex items-center justify-center shrink-0" style={{ width: size, height: size }}>
      <svg width={size} height={size} className="-rotate-90">
        <circle cx={size / 2} cy={size / 2} r={r} fill="none" strokeWidth="4" className="stroke-surface-overlay" />
        <circle cx={size / 2} cy={size / 2} r={r} fill="none" strokeWidth="4" stroke={stroke}
                strokeLinecap="round" strokeDasharray={c} strokeDashoffset={c - (c * pct) / 100}
                style={{ transition: 'stroke-dashoffset 600ms ease' }} />
      </svg>
      <div className="absolute inset-0 flex flex-col items-center justify-center">
        <span className={`font-semibold tabular-nums ${size >= 72 ? 'text-lg' : 'text-sm'} ${healthTone(score)}`}>
          {score == null ? '—' : Math.round(score)}
        </span>
        {label && <span className="text-[9px] uppercase tracking-wide text-slate-500">{label}</span>}
      </div>
    </div>
  )
}

export function Trend({ change, suffix = '' }) {
  if (change == null) return <span className="text-xs text-slate-600">no trend</span>
  const up = change > 0
  const flat = change === 0
  return (
    <span className={`inline-flex items-center gap-1 text-xs font-medium tabular-nums ${
      flat ? 'text-slate-500' : up ? 'text-emerald-400' : 'text-rose-400'}`}>
      {flat ? '→' : up ? '↑' : '↓'} {up ? '+' : ''}{Number(change).toFixed(1)}{suffix}
    </span>
  )
}

export function Tabs({ tabs, active, onChange }) {
  return (
    <div className="flex gap-1 border-b border-surface-border mb-4 overflow-x-auto">
      {tabs.map((t) => (
        <button key={t.value} onClick={() => onChange(t.value)}
                className={`px-3 py-2 text-sm whitespace-nowrap border-b-2 -mb-px transition-colors ${
                  active === t.value
                    ? 'border-accent text-slate-100'
                    : 'border-transparent text-slate-500 hover:text-slate-300'}`}>
          {t.label}{t.count != null && <span className="ml-1.5 text-xs text-slate-500 tabular-nums">{t.count}</span>}
        </button>
      ))}
    </div>
  )
}

export const when = (iso) =>
  iso ? new Date(iso).toLocaleString(undefined, { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' }) : '—'

export function timeAgo(iso) {
  if (!iso) return '—'
  const secs = Math.max(0, (Date.now() - new Date(iso)) / 1000)
  if (secs < 60) return 'just now'
  if (secs < 3600) return `${Math.floor(secs / 60)}m ago`
  if (secs < 86400) return `${Math.floor(secs / 3600)}h ago`
  return `${Math.floor(secs / 86400)}d ago`
}
