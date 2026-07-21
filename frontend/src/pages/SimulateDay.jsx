// "Simulate Next Business Day" (V2.5 demo mode) — a one-click way to watch
// the whole autonomous loop run and see what changed. It orchestrates
// existing runtime endpoints only (no new backend): observe the org, run the
// daily cycle, and re-read the decision brief, narrating each step as it
// goes. Perfect for a live demo of the Enterprise Brain deciding on its own.
import { useState } from 'react'
import { AnimatePresence, motion } from 'framer-motion'
import { api } from '../api/client'
import { ease } from '../components/premium'

const STEPS = [
  { key: 'observe', label: 'Scanning the organization for signals',
    run: () => api.intelligenceObserve() },
  { key: 'cycle', label: 'Running the autonomous daily cycle',
    run: () => api.runJob('daily_cycle') },
  { key: 'decisions', label: 'Refreshing decision intelligence',
    run: () => api.intelligenceStatus() },
  { key: 'brief', label: 'Composing the executive brief',
    run: () => api.intelligenceBrief() },
]

export function SimulateDayButton({ onDone }) {
  const [open, setOpen] = useState(false)
  return (
    <>
      <button className="btn" onClick={() => setOpen(true)}>
        <span className="opacity-80">▷</span> Simulate next business day
      </button>
      <AnimatePresence>
        {open && <SimulateModal onClose={() => setOpen(false)} onDone={onDone} />}
      </AnimatePresence>
    </>
  )
}

function SimulateModal({ onClose, onDone }) {
  const [state, setState] = useState(STEPS.map(() => 'pending'))
  const [running, setRunning] = useState(false)
  const [done, setDone] = useState(false)
  const [summary, setSummary] = useState(null)

  async function run() {
    setRunning(true); setDone(false)
    const next = STEPS.map(() => 'pending')
    const results = {}
    for (let i = 0; i < STEPS.length; i++) {
      next[i] = 'running'; setState([...next])
      try {
        results[STEPS[i].key] = await STEPS[i].run()
        next[i] = 'done'
      } catch {
        next[i] = 'error'
      }
      setState([...next])
    }
    const observe = results.observe || {}
    const signals = Object.values(observe).reduce(
      (n, v) => n + (v && typeof v === 'object' && 'signals' in v ? v.signals : 0), 0)
    setSummary({
      signals,
      expired: observe.expired ?? 0,
      open: results.decisions?.open ?? 0,
      decisions: results.decisions?.decisions ?? 0,
      top: (results.brief?.top_decisions || []).slice(0, 3),
    })
    setRunning(false); setDone(true)
    onDone && onDone()
  }

  return (
    <motion.div className="fixed inset-0 z-[70] flex items-center justify-center p-4"
      initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
      <div className="absolute inset-0 bg-black/70 backdrop-blur-sm" onClick={running ? undefined : onClose} />
      <motion.div className="relative w-full max-w-lg card-pad"
        initial={{ scale: 0.94, y: 16, opacity: 0 }} animate={{ scale: 1, y: 0, opacity: 1 }}
        exit={{ scale: 0.94, opacity: 0 }} transition={{ duration: 0.35, ease }}>
        <div className="flex items-start justify-between gap-3 mb-1">
          <div>
            <div className="text-[11px] uppercase tracking-[0.14em] text-accent font-semibold">Demo mode</div>
            <h3 className="text-lg font-bold text-slate-100 mt-0.5">Simulate the next business day</h3>
          </div>
          {!running && <button onClick={onClose} className="text-slate-500 hover:text-slate-200 text-xl leading-none">×</button>}
        </div>
        <p className="text-sm text-slate-500 mb-5">
          Fast-forward the enterprise: the agent observes, runs its daily cycle, decides, and re-briefs you —
          all through the same APIs it uses on its own heartbeat.
        </p>

        <div className="space-y-2.5 mb-5">
          {STEPS.map((s, i) => (
            <div key={s.key} className="flex items-center gap-3">
              <StepIcon status={state[i]} />
              <span className={`text-sm ${
                state[i] === 'done' ? 'text-slate-300' : state[i] === 'running' ? 'text-slate-100'
                  : state[i] === 'error' ? 'text-rose-400' : 'text-slate-500'}`}>{s.label}</span>
            </div>
          ))}
        </div>

        <AnimatePresence>
          {done && summary && (
            <motion.div className="rounded-lg bg-surface-overlay/40 p-4 mb-5"
              initial={{ opacity: 0, height: 0 }} animate={{ opacity: 1, height: 'auto' }}>
              <div className="grid grid-cols-3 gap-3 text-center mb-3">
                <Result label="New signals" value={summary.signals} />
                <Result label="Open decisions" value={summary.open} />
                <Result label="Expired" value={summary.expired} />
              </div>
              {summary.top.length > 0 && (
                <>
                  <div className="eyebrow mb-1.5">Now on the executive's desk</div>
                  <ul className="space-y-1">
                    {summary.top.map((d) => (
                      <li key={d.decision_id} className="text-xs text-slate-400 truncate">▹ {d.action}</li>
                    ))}
                  </ul>
                </>
              )}
            </motion.div>
          )}
        </AnimatePresence>

        <div className="flex justify-end gap-2">
          {!running && !done && <button className="btn-ghost" onClick={onClose}>Cancel</button>}
          {!done
            ? <button className="btn" onClick={run} disabled={running}>{running ? 'Simulating…' : 'Run simulation'}</button>
            : <button className="btn" onClick={onClose}>Done</button>}
        </div>
      </motion.div>
    </motion.div>
  )
}

function StepIcon({ status }) {
  if (status === 'done') return <span className="w-5 h-5 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-xs">✓</span>
  if (status === 'error') return <span className="w-5 h-5 rounded-full bg-rose-500/20 text-rose-400 flex items-center justify-center text-xs">!</span>
  if (status === 'running') return <span className="w-5 h-5 rounded-full border-2 border-slate-600 border-t-accent animate-spin" />
  return <span className="w-5 h-5 rounded-full border border-surface-border" />
}

function Result({ label, value }) {
  return (
    <div>
      <div className="text-2xl font-bold text-slate-100 tabular-nums">{value}</div>
      <div className="text-[10px] uppercase tracking-wide text-slate-500">{label}</div>
    </div>
  )
}
