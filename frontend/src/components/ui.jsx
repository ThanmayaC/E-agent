// Shared UI primitives (ShadCN-style: local, composable, Tailwind-driven)
import { useEffect, useMemo, useState } from 'react'

// The single page header for the whole app. `premium.jsx`'s PremiumHeader is a
// thin animated wrapper over this one, so every surface — executive or admin —
// gets the same title block, badge treatment and action alignment.
export function PageHeader({ title, subtitle, badge, eyebrow, children }) {
  return (
    <header className="flex items-end justify-between gap-4 flex-wrap mb-6 pb-4 border-b border-surface-border/70">
      <div className="min-w-0">
        {eyebrow && <div className="eyebrow mb-1.5">{eyebrow}</div>}
        <div className="flex items-center gap-2.5 flex-wrap">
          <h1 className="h-page">{title}</h1>
          {badge && <span className="chip chip-accent uppercase tracking-wider">{badge}</span>}
        </div>
        {subtitle && <p className="prose-sm mt-1.5 max-w-3xl">{subtitle}</p>}
      </div>
      {children && <div className="flex items-center gap-2 shrink-0">{children}</div>}
    </header>
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
      <span className="w-4 h-4 border-2 border-surface-border border-t-accent rounded-full animate-spin" />
      {label}
    </div>
  )
}

// One empty state, with an optional call to action. Anything that can be empty
// says *why* it is empty and what to do about it — never a bare dash.
export function Empty({ title = 'Nothing here yet', hint, icon = '◌', action }) {
  return (
    <div className="card empty-state">
      <div className="text-2xl text-slate-600 mb-2.5" aria-hidden>{icon}</div>
      <div className="text-slate-300 font-medium">{title}</div>
      {hint && <div className="text-xs text-slate-500 mt-1.5 max-w-sm">{hint}</div>}
      {action && <div className="mt-4">{action}</div>}
    </div>
  )
}

export function ErrorBox({ error, onRetry }) {
  return (
    <div className="card-pad" style={{ borderColor: 'var(--status-danger-fg)' }}>
      <div className="flex items-start gap-3">
        <span className="fg-danger text-sm" aria-hidden>⚠</span>
        <div className="min-w-0 flex-1">
          <div className="text-sm font-medium fg-danger">Couldn’t load this</div>
          <div className="text-xs text-slate-400 mt-1 break-words">{String(error)}</div>
        </div>
        {onRetry && <button className="btn-ghost btn-sm" onClick={onRetry}>Retry</button>}
      </div>
    </div>
  )
}

// Inline banner for the result of an action — the "saved", "failed", "queued"
// line that pages were each hand-rolling with hardcoded rose/emerald classes.
// Driving it from the status tokens is what makes it legible on paper as well
// as on near-black.
export function Notice({ tone = 'info', children, onDismiss }) {
  if (!children) return null
  return (
    <div className="rounded-lg px-3.5 py-2.5 text-sm flex items-start gap-2.5"
         style={{ color: `var(--status-${tone}-fg)`, background: `var(--status-${tone}-bg)` }}>
      <span aria-hidden className="shrink-0 leading-5">
        {tone === 'danger' ? '⚠' : tone === 'success' ? '✓' : tone === 'warn' ? '!' : 'ℹ'}
      </span>
      <div className="min-w-0 flex-1 break-words">{children}</div>
      {onDismiss && (
        <button onClick={onDismiss} aria-label="Dismiss" className="shrink-0 opacity-60 hover:opacity-100">✕</button>
      )}
    </div>
  )
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

// The stat tile. Shares its exact shape with premium.jsx's StatCard (which adds
// a count-up animation on top), so a page mixing the two still looks uniform.
export function Stat({ label, value, tone = 'fg-primary', hint, delta, onClick }) {
  // Guard: React throws if a value is an object/array. Coerce non-primitives to
  // a count/string so one bad field can never blank the page.
  const shown = value == null ? '—'
    : Array.isArray(value) ? value.length
    : typeof value === 'object' ? JSON.stringify(value)
    : value
  return (
    <div onClick={onClick} role={onClick ? 'button' : undefined} tabIndex={onClick ? 0 : undefined}
         onKeyDown={onClick ? (e) => e.key === 'Enter' && onClick() : undefined}
         className={`card-pad ${onClick ? 'cursor-pointer card-hover' : ''}`}>
      <div className="eyebrow">{label}</div>
      <div className={`metric mt-1.5 ${tone}`}>{shown}</div>
      {(hint || delta != null) && (
        <div className="flex items-center gap-2 mt-1">
          {delta != null && <Trend change={delta} />}
          {hint && <span className="text-xs text-slate-500">{hint}</span>}
        </div>
      )}
    </div>
  )
}

// The panel. `premium.jsx`'s GlowPanel delegates here so both names render the
// same box; `accent` promotes one panel per screen as the focal point.
export function Panel({ title, subtitle, action, children, className = '', accent = false, footer }) {
  return (
    <section className={`card-pad relative ${accent ? 'border-accent/30' : ''} ${className}`}>
      {accent && (
        <div className="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-accent/50 to-transparent pointer-events-none" />
      )}
      {(title || action) && (
        <div className="flex items-start justify-between gap-3 mb-3">
          <div className="min-w-0">
            {title && <h2 className="h-panel">{title}</h2>}
            {subtitle && <p className="text-xs text-slate-500 mt-0.5">{subtitle}</p>}
          </div>
          {action && <div className="shrink-0">{action}</div>}
        </div>
      )}
      {children}
      {footer && <div className="mt-4 pt-3 border-t border-surface-border/60 text-xs text-slate-500">{footer}</div>}
    </section>
  )
}

// Wraps a wide table so it scrolls inside its own box instead of pushing the
// page sideways — the single most common layout break on narrow screens.
export function TableWrap({ children, maxHeight }) {
  return (
    <div className="scroll-x" style={maxHeight ? { maxHeight, overflowY: 'auto' } : undefined}>
      {children}
    </div>
  )
}

// ---------------------------------------------------------------------------
// Filtering + paging for long lists.
//
// Several admin surfaces render one row per record with no cap. With ~1,000
// connected sources that is a quarter of a megabyte of DOM on a single page —
// slow to paint, impossible to scan, and unsearchable. Anything that can return
// an unbounded list should go through this hook.

export function usePaged(rows, { pageSize = 25, fields } = {}) {
  const [query, setQuery] = useState('')
  const [page, setPage] = useState(0)
  const list = rows || []

  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase()
    if (!q) return list
    const pick = (r) => (fields ? fields.map((f) => r?.[f]) : Object.values(r || {}))
    return list.filter((r) => pick(r).some((v) =>
      v != null && typeof v !== 'object' && String(v).toLowerCase().includes(q)))
  }, [list, query, fields])

  const pages = Math.max(1, Math.ceil(filtered.length / pageSize))
  const current = Math.min(page, pages - 1)
  const slice = useMemo(
    () => filtered.slice(current * pageSize, current * pageSize + pageSize),
    [filtered, current, pageSize])

  // A new query has to reset to the first page, or filtering while deep in the
  // list silently shows nothing.
  const setSearch = (v) => { setQuery(v); setPage(0) }

  return { rows: slice, query, setSearch, page: current, pages,
           total: list.length, matched: filtered.length, setPage }
}

export function ListControls({ paged, placeholder = 'Filter…', children }) {
  const { query, setSearch, total, matched } = paged
  return (
    <div className="flex items-center gap-2.5 flex-wrap mb-3">
      <input className="input !py-1.5 max-w-xs" placeholder={placeholder}
             value={query} onChange={(e) => setSearch(e.target.value)} />
      <span className="text-xs text-slate-500 num">
        {matched === total ? `${total} total` : `${matched} of ${total}`}
      </span>
      <div className="flex-1" />
      {children}
    </div>
  )
}

export function Pager({ paged }) {
  const { page, pages, setPage } = paged
  if (pages <= 1) return null
  return (
    <div className="flex items-center justify-between gap-3 mt-3 pt-3 border-t border-surface-border/60">
      <button className="btn-ghost btn-sm" disabled={page === 0} onClick={() => setPage(page - 1)}>
        ← Prev
      </button>
      <span className="text-xs text-slate-500 num">Page {page + 1} of {pages}</span>
      <button className="btn-ghost btn-sm" disabled={page >= pages - 1} onClick={() => setPage(page + 1)}>
        Next →
      </button>
    </div>
  )
}

export const PanelEmpty = ({ text }) => <div className="text-sm text-slate-600">{text}</div>

// Signature element: the health ring. One glance — score, band, motion-free.
export function HealthRing({ score, size = 56, label }) {
  const r = (size - 8) / 2
  const c = 2 * Math.PI * r
  const pct = score == null ? 0 : Math.max(0, Math.min(100, score))
  // Read the status tokens rather than hardcoding hex, so the ring darkens with
  // the rest of the palette on the light theme instead of glowing.
  const stroke = score == null ? 'var(--status-neutral-fg)'
    : score >= 70 ? 'var(--status-success-fg)'
    : score >= 50 ? 'var(--status-warn-fg)'
    : 'var(--status-danger-fg)'
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
      flat ? 'fg-muted' : up ? 'fg-success' : 'fg-danger'}`}>
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
