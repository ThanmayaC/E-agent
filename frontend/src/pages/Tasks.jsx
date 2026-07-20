// Tasks — the executive's work queue: approvals, action items, deadlines,
// and progress. Business tasks only.
import { useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import { api } from '../api/client'
import {
  AsyncSection, Badge, PageHeader, Panel, PanelEmpty, Tabs, useAsync,
} from '../components/ui'

const dueTone = (d) => {
  if (!d) return 'text-slate-600'
  const days = (new Date(d) - Date.now()) / 86400000
  return days < 0 ? 'text-rose-400' : days <= 3 ? 'text-amber-400' : 'text-slate-500'
}

export default function Tasks() {
  const [refresh, setRefresh] = useState(0)
  const [tab, setTab] = useState('open')
  const [title, setTitle] = useState('')
  const [due, setDue] = useState('')
  const [error, setError] = useState('')
  const state = useAsync(async () => {
    const [tasks, ws] = await Promise.all([
      api.managerTasks(),
      api.managerWorkspace().catch(() => null),
    ])
    return { ...tasks, approvals: ws?.pending_approvals || [] }
  }, [refresh])
  const reload = () => setRefresh((n) => n + 1)

  const setStatus = (id, status) => {
    setError('')
    api.setTaskStatus(id, status).then(reload).catch((e) => setError(String(e.message || e)))
  }
  const addTask = (e) => {
    e.preventDefault()
    if (!title.trim()) return
    setError('')
    api.createTask({ title: title.trim(), due_date: due, owner: 'executive' })
      .then(() => { setTitle(''); setDue(''); reload() })
      .catch((err) => setError(String(err.message || err)))
  }
  const actionId = (ref) => ref.replace(/^action:/, '')
  const approve = (ref) => api.approveAction(actionId(ref), 'executive').then(reload)
  const reject = (ref) => api.rejectAction(actionId(ref), 'executive', 'rejected from Tasks').then(reload)

  return (
    <>
      <PageHeader title="Tasks" subtitle="Approvals, action items, and deadlines — everything waiting on you" />
      {error && <div className="card-pad border-rose-500/40 text-rose-300 text-sm mb-4">{error}</div>}
      <AsyncSection state={state} empty="No tasks yet.">
        {({ tasks, stats, approvals }) => (
          <TaskBoard tasks={tasks || []} stats={stats || {}} approvals={approvals}
                     tab={tab} setTab={setTab}
                     title={title} setTitle={setTitle} due={due} setDue={setDue}
                     addTask={addTask} setStatus={setStatus} approve={approve} reject={reject} />
        )}
      </AsyncSection>
    </>
  )
}

function TaskBoard({ tasks, stats, approvals, tab, setTab, title, setTitle, due, setDue, addTask, setStatus, approve, reject }) {
  const byTab = useMemo(() => ({
    open: tasks.filter((t) => t.status === 'pending' || t.status === 'in_progress'),
    suggested: tasks.filter((t) => t.status === 'suggested'),
    completed: tasks.filter((t) => t.status === 'completed'),
    dismissed: tasks.filter((t) => t.status === 'dismissed'),
  }), [tasks])

  const total = (stats.completed || 0) + byTab.open.length
  const progress = total ? Math.round(((stats.completed || 0) / total) * 100) : 0
  const deadlines = byTab.open
    .filter((t) => t.due_date)
    .sort((a, b) => String(a.due_date).localeCompare(String(b.due_date)))

  const tabs = [
    { value: 'open', label: 'Open', count: byTab.open.length },
    { value: 'suggested', label: 'Suggested', count: byTab.suggested.length },
    { value: 'completed', label: 'Completed', count: byTab.completed.length },
    { value: 'dismissed', label: 'Dismissed', count: byTab.dismissed.length },
  ]

  return (
    <div className="space-y-5">
      <div className="grid gap-5 lg:grid-cols-3">
        <Panel title="Approval queue" className="lg:col-span-2">
          {approvals.length === 0 ? <PanelEmpty text="Nothing is waiting for approval." /> : (
            <ul className="space-y-2.5">
              {approvals.map((a) => (
                <li key={a.ref} className="flex items-start justify-between gap-3 text-sm">
                  <div className="min-w-0">
                    <div className="text-slate-200">{a.title}</div>
                    {a.detail && <div className="text-slate-500 text-xs mt-0.5 truncate">{a.detail}</div>}
                  </div>
                  {a.kind === 'action_approval' ? (
                    <span className="shrink-0 space-x-2.5 text-xs">
                      <button onClick={() => approve(a.ref)} className="text-emerald-400 hover:underline">Approve</button>
                      <button onClick={() => reject(a.ref)} className="text-slate-500 hover:underline">Reject</button>
                    </span>
                  ) : (
                    <Link className="text-accent text-xs shrink-0"
                          to={a.kind === 'report_review' ? '/reports' : `/reports/${a.project_id}`}>Open →</Link>
                  )}
                </li>
              ))}
            </ul>
          )}
        </Panel>

        <Panel title="Progress">
          <div className="text-sm text-slate-300 mb-2 tabular-nums">
            {stats.completed || 0} of {total} done · {progress}%
          </div>
          <div className="h-2 rounded bg-surface-overlay overflow-hidden">
            <div className="h-full rounded bg-accent transition-all" style={{ width: `${progress}%` }} />
          </div>
          <div className="h-sub mt-5 mb-2">Deadlines</div>
          {deadlines.length === 0 ? <PanelEmpty text="No dated tasks." /> : (
            <ul className="space-y-1.5">
              {deadlines.slice(0, 5).map((t) => (
                <li key={t.task_id} className="flex justify-between gap-3 text-sm">
                  <span className="text-slate-300 truncate">{t.title}</span>
                  <span className={`text-xs shrink-0 ${dueTone(t.due_date)}`}>{t.due_date}</span>
                </li>
              ))}
            </ul>
          )}
        </Panel>
      </div>

      <section className="card-pad">
        <form className="flex gap-2 mb-4 flex-wrap" onSubmit={addTask}>
          <input className="input flex-1 min-w-[220px]" placeholder="Add a task…"
                 value={title} onChange={(e) => setTitle(e.target.value)} />
          <input className="input !w-40" type="date" value={due} onChange={(e) => setDue(e.target.value)} />
          <button className="btn" type="submit" disabled={!title.trim()}>Add task</button>
        </form>

        <Tabs tabs={tabs} active={tab} onChange={setTab} />
        {byTab[tab].length === 0 ? <PanelEmpty text="Nothing here." /> : (
          <ul className="divide-y divide-surface-border/50">
            {byTab[tab].map((t) => (
              <li key={t.task_id} className="py-2.5 flex items-start justify-between gap-3 text-sm">
                <div className="min-w-0">
                  <div className="text-slate-200">
                    {t.priority && <Badge tone="accent">P{t.priority}</Badge>} {t.title}
                  </div>
                  <div className="text-xs text-slate-500 mt-0.5">
                    {t.detail && <span>{String(t.detail).slice(0, 120)} · </span>}
                    {t.due_date && <span className={dueTone(t.due_date)}>due {t.due_date} · </span>}
                    {t.owner || ''}
                  </div>
                </div>
                <span className="shrink-0 space-x-2.5 text-xs">
                  {tab === 'open' && (
                    <>
                      <button onClick={() => setStatus(t.task_id, 'completed')} className="text-emerald-400 hover:underline">Done ✓</button>
                      <button onClick={() => setStatus(t.task_id, 'dismissed')} className="text-slate-500 hover:underline">Dismiss</button>
                    </>
                  )}
                  {tab === 'suggested' && (
                    <>
                      <button onClick={() => setStatus(t.task_id, 'pending')} className="text-accent hover:underline">Accept</button>
                      <button onClick={() => setStatus(t.task_id, 'dismissed')} className="text-slate-500 hover:underline">Dismiss</button>
                    </>
                  )}
                  {(tab === 'completed' || tab === 'dismissed') && (
                    <button onClick={() => setStatus(t.task_id, 'pending')} className="text-accent hover:underline">Re-open</button>
                  )}
                </span>
              </li>
            ))}
          </ul>
        )}
      </section>
    </div>
  )
}
