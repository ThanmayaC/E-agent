// V2.5 Executive Experience — premium shared primitives.
//
// A small, composable design language layered on the existing tokens
// (surface-*, accent, slate) so every new surface reads as one system:
// motion, skeleton loaders, animated numerals, sparklines, an explainable-AI
// panel, export, and search/filter controls. No backend logic lives here —
// these are presentation primitives the dashboards compose.
import { useEffect, useMemo, useRef, useState } from 'react'
import { AnimatePresence, motion } from 'framer-motion'

// --------------------------------------------------------------- motion
// One easing/limit vocabulary, so entrances feel deliberate, never busy.
export const ease = [0.22, 1, 0.36, 1]

export function Reveal({ children, delay = 0, y = 12, className = '' }) {
  return (
    <motion.div className={className}
      initial={{ opacity: 0, y }} animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.45, ease, delay }}>
      {children}
    </motion.div>
  )
}

// Staggered grid/list container — children animate in sequence.
export function Stagger({ children, className = '', gap = 0.05 }) {
  return (
    <motion.div className={className} initial="hidden" animate="show"
      variants={{ hidden: {}, show: { transition: { staggerChildren: gap } } }}>
      {children}
    </motion.div>
  )
}

export function StaggerItem({ children, className = '', y = 14 }) {
  return (
    <motion.div className={className}
      variants={{ hidden: { opacity: 0, y }, show: { opacity: 1, y: 0 } }}
      transition={{ duration: 0.4, ease }}>
      {children}
    </motion.div>
  )
}

// ------------------------------------------------------- loading states
// Shimmering skeletons that mirror the shape of what's loading, so the page
// never jumps when data arrives.
export function Skeleton({ className = '' }) {
  return <div className={`animate-pulse rounded-md bg-surface-overlay/70 ${className}`} />
}

export function SkeletonCard({ lines = 3 }) {
  return (
    <div className="card-pad space-y-3">
      <Skeleton className="h-3 w-24" />
      <Skeleton className="h-8 w-20" />
      {Array.from({ length: lines }).map((_, i) => (
        <Skeleton key={i} className="h-3" style={{ width: `${90 - i * 15}%` }} />
      ))}
    </div>
  )
}

export function SkeletonGrid({ count = 4 }) {
  return (
    <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
      {Array.from({ length: count }).map((_, i) => <SkeletonCard key={i} lines={2} />)}
    </div>
  )
}

// Async gate with premium skeletons instead of a bare spinner.
export function Loader({ state, skeleton, children, empty = 'Nothing here yet.' }) {
  if (state.loading) return skeleton || <SkeletonGrid />
  if (state.error) {
    return (
      <div className="card-pad border-rose-500/40 text-rose-300 text-sm">
        {String(state.error.message || state.error)}
      </div>
    )
  }
  const d = state.data
  const isEmpty = !d || (Array.isArray(d) && d.length === 0)
  if (isEmpty) return <div className="card-pad text-center py-12 text-slate-500 text-sm">{empty}</div>
  return children(d)
}

// ------------------------------------------------------- animated value
// Counts up to the target so KPIs feel alive on first paint.
export function Counter({ value, decimals = 0, prefix = '', suffix = '', className = '' }) {
  const [display, setDisplay] = useState(0)
  const raf = useRef(null)
  useEffect(() => {
    const target = Number(value) || 0
    const start = performance.now()
    const from = 0
    const tick = (now) => {
      const t = Math.min(1, (now - start) / 700)
      const eased = 1 - Math.pow(1 - t, 3)
      setDisplay(from + (target - from) * eased)
      if (t < 1) raf.current = requestAnimationFrame(tick)
    }
    raf.current = requestAnimationFrame(tick)
    return () => cancelAnimationFrame(raf.current)
  }, [value])
  return (
    <span className={`tabular-nums ${className}`}>
      {prefix}{display.toLocaleString(undefined, {
        minimumFractionDigits: decimals, maximumFractionDigits: decimals })}{suffix}
    </span>
  )
}

// A premium stat tile: eyebrow label, animated value, trend, optional spark.
export function StatCard({ label, value, decimals = 0, prefix = '', suffix = '',
                          tone = 'text-slate-100', delta, spark, hint, onClick }) {
  return (
    <div onClick={onClick}
      className={`card-pad relative overflow-hidden group ${onClick ? 'cursor-pointer card-hover' : ''}`}>
      <div className="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-accent/40 to-transparent opacity-0 group-hover:opacity-100 transition-opacity" />
      <div className="eyebrow">{label}</div>
      <div className={`metric mt-1.5 ${tone}`}>
        {value == null ? '—' : <Counter value={value} decimals={decimals} prefix={prefix} suffix={suffix} />}
      </div>
      <div className="flex items-center gap-2 mt-1">
        {delta != null && <TrendPill change={delta} />}
        {hint && <span className="text-xs text-slate-500">{hint}</span>}
      </div>
      {spark && <div className="mt-3">{spark}</div>}
    </div>
  )
}

export function TrendPill({ change, suffix = '' }) {
  if (change == null) return null
  const up = change > 0, flat = change === 0
  return (
    <span className={`inline-flex items-center gap-1 text-xs font-medium tabular-nums px-1.5 py-0.5 rounded-md ${
      flat ? 'text-slate-400 bg-surface-overlay'
        : up ? 'text-emerald-400 bg-emerald-500/10' : 'text-rose-400 bg-rose-500/10'}`}>
      {flat ? '→' : up ? '↑' : '↓'} {up ? '+' : ''}{Number(change).toFixed(1)}{suffix}
    </span>
  )
}

// ------------------------------------------------------------ sparkline
// Dependency-free inline SVG spark — for stat cards and dense tables.
export function Sparkline({ data = [], width = 120, height = 32, stroke = '#4f8ef7', fill = true }) {
  const pts = useMemo(() => {
    const nums = data.map(Number).filter((n) => !Number.isNaN(n))
    if (nums.length < 2) return null
    const min = Math.min(...nums), max = Math.max(...nums)
    const span = max - min || 1
    const step = width / (nums.length - 1)
    return nums.map((n, i) => [i * step, height - ((n - min) / span) * (height - 4) - 2])
  }, [data, width, height])
  if (!pts) return <div style={{ width, height }} className="flex items-center text-[10px] text-slate-600">—</div>
  const line = pts.map((p, i) => `${i ? 'L' : 'M'}${p[0].toFixed(1)},${p[1].toFixed(1)}`).join(' ')
  const area = `${line} L${width},${height} L0,${height} Z`
  const id = useMemo(() => `sg${Math.random().toString(36).slice(2, 8)}`, [])
  return (
    <svg width={width} height={height} className="overflow-visible">
      {fill && (
        <>
          <defs>
            <linearGradient id={id} x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor={stroke} stopOpacity="0.28" />
              <stop offset="100%" stopColor={stroke} stopOpacity="0" />
            </linearGradient>
          </defs>
          <path d={area} fill={`url(#${id})`} />
        </>
      )}
      <path d={line} fill="none" stroke={stroke} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  )
}

// -------------------------------------------------- explainable AI panel
// Every recommendation the platform makes can be opened up: the reasoning,
// the ranked factors behind its score, the evidence it cited, and the
// confidence it carried. This is the "why" surface the milestone asks for.
const FACTOR_LABEL = {
  impact: 'Business impact', urgency: 'Urgency', confidence: 'Confidence',
  evidence: 'Evidence strength', history: 'Historical success', risk: 'Risk',
  strategic: 'Strategic importance',
}

export function ExplainPanel({ decision, weights, onClose }) {
  if (!decision) return null
  const factors = decision.factors || {}
  const entries = Object.entries(factors)
    .sort((a, b) => (weights?.[b[0]] ?? 0) * b[1] - (weights?.[a[0]] ?? 0) * a[1])
  return (
    <AnimatePresence>
      <motion.div className="fixed inset-0 z-[60] flex justify-end"
        initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
        <div className="absolute inset-0 bg-black/60 backdrop-blur-sm" onClick={onClose} />
        <motion.aside
          className="relative w-full max-w-md h-full bg-surface-raised border-l border-surface-border overflow-y-auto"
          initial={{ x: 40, opacity: 0.6 }} animate={{ x: 0, opacity: 1 }} exit={{ x: 40, opacity: 0 }}
          transition={{ duration: 0.35, ease }}>
          <div className="sticky top-0 bg-surface-raised/95 backdrop-blur border-b border-surface-border px-5 py-4 flex items-start justify-between gap-3">
            <div>
              <div className="text-[11px] uppercase tracking-[0.14em] text-accent font-semibold">Why this recommendation</div>
              <h3 className="text-sm font-semibold text-slate-100 mt-1">{decision.action}</h3>
            </div>
            <button onClick={onClose} className="text-slate-500 hover:text-slate-200 text-lg leading-none">×</button>
          </div>
          <div className="p-5 space-y-5">
            {decision.score != null && (
              <div className="flex items-center gap-4">
                <ScoreGauge score={decision.score} />
                <div className="text-sm text-slate-400">
                  Ranked <span className="text-slate-100 font-semibold">#{decision.rank ?? '—'}</span> by a weighted
                  blend of seven factors. Higher is more worth your attention.
                </div>
              </div>
            )}
            <Section title="Reasoning">
              <p className="text-sm text-slate-300 leading-relaxed">{decision.reasoning || '—'}</p>
            </Section>
            {entries.length > 0 && (
              <Section title="Factor breakdown">
                <div className="space-y-2.5">
                  {entries.map(([k, v]) => (
                    <FactorBar key={k} label={FACTOR_LABEL[k] || k} value={v} weight={weights?.[k]} />
                  ))}
                </div>
              </Section>
            )}
            <div className="grid grid-cols-2 gap-3">
              <MiniFact label="Confidence" value={`${Math.round((decision.confidence ?? 0) * 100)}%`} />
              <MiniFact label="Priority" value={`P${decision.priority ?? '—'}`} />
              <MiniFact label="Kind" value={decision.kind || '—'} />
              <MiniFact label="Status" value={decision.status || '—'} />
            </div>
            {(decision.evidence_ids || []).length > 0 && (
              <Section title={`Evidence (${decision.evidence_ids.length})`}>
                <ul className="space-y-1">
                  {decision.evidence_ids.map((e, i) => (
                    <li key={i} className="text-xs text-slate-400 font-mono bg-surface-overlay/50 rounded px-2 py-1 truncate">{e}</li>
                  ))}
                </ul>
              </Section>
            )}
            {(decision.affected_teams?.length > 0 || decision.affected_products?.length > 0) && (
              <Section title="Affects">
                <div className="flex flex-wrap gap-1.5">
                  {(decision.affected_products || []).map((p) => (
                    <span key={p} className="px-2 py-0.5 rounded-md text-[11px] bg-accent/15 text-accent">{p}</span>
                  ))}
                  {(decision.affected_teams || []).map((t) => (
                    <span key={t} className="px-2 py-0.5 rounded-md text-[11px] bg-surface-overlay text-slate-300">{t}</span>
                  ))}
                </div>
              </Section>
            )}
          </div>
        </motion.aside>
      </motion.div>
    </AnimatePresence>
  )
}

function Section({ title, children }) {
  return (
    <div>
      <div className="eyebrow mb-2">{title}</div>
      {children}
    </div>
  )
}

function MiniFact({ label, value }) {
  return (
    <div className="bg-surface-overlay/40 rounded-lg px-3 py-2">
      <div className="text-[10px] uppercase tracking-wide text-slate-500">{label}</div>
      <div className="text-sm text-slate-200 mt-0.5 capitalize">{value}</div>
    </div>
  )
}

function FactorBar({ label, value, weight }) {
  const pct = Math.max(0, Math.min(1, Number(value) || 0)) * 100
  return (
    <div>
      <div className="flex justify-between text-xs mb-1">
        <span className="text-slate-400">{label}{weight != null && <span className="text-slate-600"> · w{weight}</span>}</span>
        <span className="text-slate-300 tabular-nums">{(Number(value) || 0).toFixed(2)}</span>
      </div>
      <div className="h-1.5 rounded-full bg-surface-overlay overflow-hidden">
        <motion.div className="h-full rounded-full bg-gradient-to-r from-accent/70 to-accent"
          initial={{ width: 0 }} animate={{ width: `${pct}%` }} transition={{ duration: 0.6, ease }} />
      </div>
    </div>
  )
}

export function ScoreGauge({ score, size = 64 }) {
  const pct = Math.max(0, Math.min(1, Number(score) || 0))
  const r = (size - 8) / 2, c = 2 * Math.PI * r
  const color = pct >= 0.66 ? '#f87171' : pct >= 0.4 ? '#fbbf24' : '#34d399'
  return (
    <div className="relative shrink-0" style={{ width: size, height: size }}>
      <svg width={size} height={size} className="-rotate-90">
        <circle cx={size / 2} cy={size / 2} r={r} fill="none" strokeWidth="5" className="stroke-surface-overlay" />
        <motion.circle cx={size / 2} cy={size / 2} r={r} fill="none" strokeWidth="5" stroke={color}
          strokeLinecap="round" strokeDasharray={c}
          initial={{ strokeDashoffset: c }} animate={{ strokeDashoffset: c - c * pct }}
          transition={{ duration: 0.8, ease }} />
      </svg>
      <div className="absolute inset-0 flex items-center justify-center text-sm font-semibold text-slate-100 tabular-nums">
        {(pct).toFixed(2)}
      </div>
    </div>
  )
}

// ------------------------------------------------------- search / filter
export function SearchInput({ value, onChange, placeholder = 'Search…', className = '' }) {
  return (
    <div className={`relative ${className}`}>
      <span className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-500 text-sm pointer-events-none">⌕</span>
      <input className="input !pl-8" placeholder={placeholder} value={value}
             onChange={(e) => onChange(e.target.value)} />
      {value && (
        <button onClick={() => onChange('')}
                className="absolute right-2.5 top-1/2 -translate-y-1/2 text-slate-500 hover:text-slate-300 text-sm">×</button>
      )}
    </div>
  )
}

export function FilterChips({ options, active, onChange, allLabel = 'All' }) {
  return (
    <div className="flex flex-wrap gap-1.5">
      <Chip active={!active} onClick={() => onChange('')}>{allLabel}</Chip>
      {options.map((o) => {
        const value = typeof o === 'string' ? o : o.value
        const label = typeof o === 'string' ? o : o.label
        const count = typeof o === 'object' ? o.count : undefined
        return (
          <Chip key={value} active={active === value} onClick={() => onChange(value)}>
            {label}{count != null && <span className="ml-1 opacity-60 tabular-nums">{count}</span>}
          </Chip>
        )
      })}
    </div>
  )
}

function Chip({ active, onClick, children }) {
  return (
    <button onClick={onClick}
      className={`px-2.5 py-1 rounded-full text-xs font-medium border transition-colors capitalize ${
        active ? 'bg-accent/15 border-accent/50 text-accent'
          : 'border-surface-border text-slate-400 hover:text-slate-200 hover:border-slate-500'}`}>
      {children}
    </button>
  )
}

// ---------------------------------------------------------------- export
// Client-side export only — no backend involvement. JSON and CSV download
// from data already on the page; "Print / PDF" uses the browser's print
// dialog against a print stylesheet.
export function download(filename, text, type = 'application/json') {
  const blob = new Blob([text], { type })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url; a.download = filename
  document.body.appendChild(a); a.click(); a.remove()
  URL.revokeObjectURL(url)
}

export function toCSV(rows) {
  if (!rows || !rows.length) return ''
  const cols = [...new Set(rows.flatMap((r) => Object.keys(r)))]
  const esc = (v) => {
    const s = v == null ? '' : typeof v === 'object' ? JSON.stringify(v) : String(v)
    return /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s
  }
  return [cols.join(','), ...rows.map((r) => cols.map((c) => esc(r[c])).join(','))].join('\n')
}

export function ExportMenu({ filename = 'export', json, rows, onPrint }) {
  const [open, setOpen] = useState(false)
  const ref = useRef(null)
  useEffect(() => {
    const close = (e) => { if (ref.current && !ref.current.contains(e.target)) setOpen(false) }
    document.addEventListener('mousedown', close)
    return () => document.removeEventListener('mousedown', close)
  }, [])
  return (
    <div ref={ref} className="relative">
      <button className="btn-ghost" onClick={() => setOpen((v) => !v)}>
        <span className="opacity-70">↓</span> Export
      </button>
      <AnimatePresence>
        {open && (
          <motion.div className="absolute right-0 top-full mt-1.5 w-44 card shadow-2xl shadow-black/40 z-50 py-1"
            initial={{ opacity: 0, y: -6 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -6 }}
            transition={{ duration: 0.15 }}>
            {json !== undefined && (
              <MenuItem onClick={() => { download(`${filename}.json`, JSON.stringify(json, null, 2)); setOpen(false) }}>
                Download JSON
              </MenuItem>
            )}
            {rows !== undefined && (
              <MenuItem onClick={() => { download(`${filename}.csv`, toCSV(rows), 'text/csv'); setOpen(false) }}>
                Download CSV
              </MenuItem>
            )}
            <MenuItem onClick={() => { (onPrint || window.print)(); setOpen(false) }}>
              Print / Save as PDF
            </MenuItem>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  )
}

function MenuItem({ onClick, children }) {
  return (
    <button onClick={onClick}
      className="w-full text-left px-3 py-2 text-sm text-slate-300 hover:bg-surface-overlay hover:text-slate-100 transition-colors">
      {children}
    </button>
  )
}

// ---------------------------------------------------------- page header
export function PremiumHeader({ title, subtitle, badge, children }) {
  return (
    <Reveal className="flex items-end justify-between mb-6 gap-4 flex-wrap">
      <div>
        <div className="flex items-center gap-2.5">
          <h1 className="text-2xl font-bold text-slate-100 tracking-tight">{title}</h1>
          {badge && <span className="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-accent/15 text-accent uppercase tracking-wider">{badge}</span>}
        </div>
        {subtitle && <p className="text-sm text-slate-500 mt-1">{subtitle}</p>}
      </div>
      {children && <div className="flex items-center gap-2">{children}</div>}
    </Reveal>
  )
}

// A soft-glow panel used for the flagship cockpit sections.
export function GlowPanel({ title, action, children, className = '', accent = false }) {
  return (
    <section className={`card-pad relative ${accent ? 'border-accent/30' : ''} ${className}`}>
      {accent && <div className="absolute -inset-px rounded-xl bg-gradient-to-b from-accent/10 to-transparent pointer-events-none -z-10" />}
      {(title || action) && (
        <div className="flex items-center justify-between mb-3 gap-3">
          {title && <h2 className="text-sm font-semibold text-slate-200">{title}</h2>}
          {action}
        </div>
      )}
      {children}
    </section>
  )
}
