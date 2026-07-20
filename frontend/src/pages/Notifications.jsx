// Notifications — business signals only: revenue moves, risks, reports
// awaiting approval, deadlines. Muted kinds (Settings → Notifications)
// are filtered out of the view.
import { useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import { api } from '../api/client'
import { getNotifyPrefs } from '../lib/prefs'
import {
  AsyncSection, Badge, PageHeader, PanelEmpty, Tabs, timeAgo, useAsync,
} from '../components/ui'

const KIND_TONE = {
  critical_risk: 'danger', workflow_failure: 'danger', portfolio_change: 'warn',
  new_report: 'info', recommendation: 'accent', task_deadline: 'warn',
}
const KIND_LABEL = {
  critical_risk: 'risk', workflow_failure: 'needs review', portfolio_change: 'health change',
  new_report: 'new report', recommendation: 'recommendation', task_deadline: 'deadline',
}

export default function Notifications() {
  const [refresh, setRefresh] = useState(0)
  const [tab, setTab] = useState('unread')
  const state = useAsync(() => api.managerNotifications(false), [refresh])
  const reload = () => setRefresh((n) => n + 1)
  const prefs = useMemo(getNotifyPrefs, [refresh])

  const markRead = (id) => api.markNotificationRead(id).then(reload)
  const readAll = () => api.markAllNotificationsRead().then(reload)

  return (
    <>
      <PageHeader title="Notifications" subtitle="What changed in the business and what needs your eyes">
        <button className="btn-ghost" onClick={readAll}>Mark all read</button>
      </PageHeader>
      <AsyncSection state={state} empty="No notifications — you are fully caught up.">
        {({ notifications, stats }) => {
          const visible = (notifications || []).filter((n) => prefs[n.kind] !== false)
          const unread = visible.filter((n) => !n.read)
          const list = tab === 'unread' ? unread : visible
          return (
            <>
              <Tabs active={tab} onChange={setTab}
                    tabs={[{ value: 'unread', label: 'Unread', count: stats?.unread ?? unread.length },
                           { value: 'all', label: 'All', count: visible.length }]} />
              {list.length === 0 ? <PanelEmpty text={tab === 'unread' ? 'Nothing unread.' : 'No notifications.'} /> : (
                <div className="space-y-2">
                  {list.map((n) => (
                    <section key={n.notification_id}
                             className={`card px-5 py-3.5 flex items-start gap-3 ${n.read ? 'opacity-60' : ''}`}>
                      <Badge tone={KIND_TONE[n.kind] || 'default'}>{KIND_LABEL[n.kind] || (n.kind || '').replace(/_/g, ' ')}</Badge>
                      <div className="min-w-0 flex-1">
                        <div className={`text-sm ${n.read ? 'text-slate-400' : 'text-slate-200'}`}>{n.title}</div>
                        {n.detail && <div className="text-xs text-slate-500 mt-0.5">{n.detail}</div>}
                        <div className="text-[11px] text-slate-600 mt-1">
                          {timeAgo(n.created_at)}
                          {n.project_id && (
                            <> · <Link to={`/reports/${n.project_id}`} className="hover:text-accent">view report →</Link></>
                          )}
                        </div>
                      </div>
                      {!n.read && (
                        <button onClick={() => markRead(n.notification_id)}
                                className="btn-quiet shrink-0">Mark read</button>
                      )}
                    </section>
                  ))}
                </div>
              )}
            </>
          )
        }}
      </AsyncSection>
    </>
  )
}
