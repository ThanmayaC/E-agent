// Enterprise Timeline (V2.5) — one chronological stream of everything the
// organization did: runtime events, things the Brain learned, and decisions
// as they moved through their lifecycle. Merged client-side from existing
// endpoints (/runtime/events, /learning/history, /runtime/intelligence/
// decisions); filterable by category and searchable. No backend logic.
import { useMemo, useState } from 'react'
import { api } from '../api/client'
import { useAsync } from '../components/ui'
import { timeAgo, when } from '../components/ui'
import {
  ExportMenu, FilterChips, Loader, PremiumHeader, Reveal, SearchInput,
} from '../components/premium'

const CATS = {
  decision: { label: 'Decisions', dot: 'bg-purple-400', tone: 'text-purple-300' },
  learning: { label: 'Learning', dot: 'bg-emerald-400', tone: 'text-emerald-300' },
  event: { label: 'Events', dot: 'bg-accent', tone: 'text-accent' },
}

// Map raw records from three sources into one shape the timeline renders.
function normalize({ events, learning, decisions }) {
  const items = []
  for (const e of events || []) {
    items.push({
      id: e.event_id, at: e.created_at, category: 'event', title: e.kind,
      detail: e.source ? `via ${e.source}` : '', meta: e.payload,
    })
  }
  for (const l of learning || []) {
    items.push({
      id: `${l.event}-${l.recorded_at}`, at: l.recorded_at, category: 'learning',
      title: (l.event || '').replace(/_/g, ' '),
      detail: l.details?.action || l.source || '', meta: l.details,
    })
  }
  for (const d of decisions || []) {
    const last = (d.history || [])[d.history.length - 1]
    items.push({
      id: d.decision_id, at: d.updated_at || d.created_at, category: 'decision',
      title: `Decision ${d.status}`, detail: d.action,
      meta: { kind: d.kind, priority: d.priority, by: last?.by },
    })
  }
  return items
    .filter((i) => i.at)
    .sort((a, b) => new Date(b.at) - new Date(a.at))
}

export default function Timeline() {
  const events = useAsync(() => api.runtimeEvents(120).then((r) => r.events).catch(() => []), [])
  const learning = useAsync(() => api.learningHistory(120).catch(() => []), [])
  const decisions = useAsync(() => api.intelligenceDecisions('', 80).then((r) => r.decisions).catch(() => []), [])

  const loading = events.loading || learning.loading || decisions.loading
  const all = useMemo(() => normalize({
    events: events.data, learning: learning.data, decisions: decisions.data,
  }), [events.data, learning.data, decisions.data])

  const [cat, setCat] = useState('')
  const [q, setQ] = useState('')
  const filtered = useMemo(() => {
    const needle = q.trim().toLowerCase()
    return all.filter((i) =>
      (!cat || i.category === cat) &&
      (!needle || `${i.title} ${i.detail}`.toLowerCase().includes(needle)))
  }, [all, cat, q])

  const counts = useMemo(() => Object.keys(CATS).map((value) => ({
    value, label: CATS[value].label, count: all.filter((i) => i.category === value).length,
  })), [all])

  // Group by calendar day for section headers.
  const grouped = useMemo(() => {
    const g = []
    let day = null
    for (const item of filtered) {
      const d = new Date(item.at).toLocaleDateString(undefined, { weekday: 'long', month: 'short', day: 'numeric' })
      if (d !== day) { day = d; g.push({ day: d, items: [] }) }
      g[g.length - 1].items.push(item)
    }
    return g
  }, [filtered])

  return (
    <div>
      <PremiumHeader title="Enterprise Timeline" badge={`${all.length} events`}
        subtitle="Everything the organization did — decisions, learning, and autonomous activity — in one stream.">
        <ExportMenu filename="enterprise-timeline" rows={filtered.map((i) => ({
          time: i.at, category: i.category, title: i.title, detail: i.detail }))} json={all} />
      </PremiumHeader>

      <div className="flex flex-wrap items-center gap-3 mb-5">
        <SearchInput value={q} onChange={setQ} placeholder="Search the timeline…" className="w-64" />
        <FilterChips options={counts} active={cat} onChange={setCat} allLabel={`All (${all.length})`} />
      </div>

      <Loader state={{ loading, error: null, data: loading ? null : filtered }}
        skeleton={<div className="space-y-3">{Array.from({ length: 6 }).map((_, i) => <div key={i} className="h-14 rounded-lg bg-surface-overlay/40 animate-pulse" />)}</div>}
        empty="No activity matches your filters.">
        {() => (
          <div className="relative">
            {grouped.map((group, gi) => (
              <div key={group.day} className="mb-6">
                <div className="sticky top-0 z-10 -mx-1 px-1 py-1.5 bg-surface/80 backdrop-blur text-xs font-semibold text-slate-400 uppercase tracking-wider">
                  {group.day}
                </div>
                <ol className="relative border-l border-surface-border ml-2 mt-2">
                  {group.items.map((item, i) => (
                    <Reveal key={item.id + i} delay={Math.min(gi * 0.02 + i * 0.015, 0.4)}>
                      <TimelineRow item={item} />
                    </Reveal>
                  ))}
                </ol>
              </div>
            ))}
          </div>
        )}
      </Loader>
    </div>
  )
}

function TimelineRow({ item }) {
  const cat = CATS[item.category] || CATS.event
  return (
    <li className="ml-5 mb-3 group">
      <span className={`absolute -left-[6.5px] w-3 h-3 rounded-full ${cat.dot} ring-4 ring-surface`} />
      <div className="card-pad !p-3 card-hover">
        <div className="flex items-center justify-between gap-3">
          <div className="min-w-0 flex-1">
            <div className="flex items-center gap-2">
              <span className={`text-sm font-medium capitalize ${cat.tone}`}>{item.title}</span>
            </div>
            {item.detail && <div className="text-sm text-slate-400 mt-0.5 truncate">{item.detail}</div>}
          </div>
          <div className="shrink-0 text-right">
            <div className="text-xs text-slate-500" title={when(item.at)}>{timeAgo(item.at)}</div>
            {item.meta?.priority && <div className="text-[10px] text-slate-600">P{item.meta.priority}</div>}
          </div>
        </div>
      </div>
    </li>
  )
}
