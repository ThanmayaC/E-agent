# Executive Experience (Production UI)

The frontend is a production-grade executive workspace. Business users see
business workflows only; every engineering surface lives behind an Admin
Console. No new backend modules were added — every screen consumes existing
REST APIs (`/api/v1/manager/*`, `/api/v1/product/*`, `/api/v1/projects/*`,
`/api/v1/brain/*`, `/api/v1/runtime/*`, `/api/v1/sync/*`, `/api/v1/platform/*`).

## Design principles

- **Business language only.** The executive surfaces never mention runtime,
  scheduler, jobs, event bus, brain, knowledge graph, sync engine, action
  queue, or internal APIs. Those words exist only inside `/admin`.
- **Dark mode first**, minimal, responsive — visual direction drawn from
  Microsoft Fabric / Power BI / Copilot, Notion, Linear, GitHub Enterprise.
- **No duplicated business logic.** The UI renders what the APIs return;
  approvals, briefs, health scores, and recommendations are computed by the
  backend.
- **Backwards compatible.** The per-project analyst workbench keeps its
  original URLs under `/p/:projectId/*`, and legacy routes redirect
  (`/brief → /dashboard`, `/autonomy → /admin/runtime`, `/reviews → /reports`,
  `/projects → /data`).

## Executive Workspace (what a manager sees)

| Route | Page | Purpose |
| --- | --- | --- |
| `/` | Home | Welcome surface with a natural-language ask box that hands off to the Copilot |
| `/dashboard` | Executive Dashboard | Landing view: Today's Summary, AI Executive Brief, Critical Alerts, Portfolio Health, Top Opportunities, Products At Risk, Pending Approvals (approve/reject inline), Recent Reports, Recommended Actions, Upcoming Deadlines |
| `/portfolio` | Portfolio | Products as executive cards — health score, growth, risk, revenue, trend, recommendations |
| `/portfolio/product/:id` | Product Summary | Executive summary opened from a card |
| `/reports` | Report Center | Generated / pending-review / approved reports, search, filters, export |
| `/reports/:projectId` | Report View | A single executive report |
| `/copilot` | AI Copilot | Primary conversational interface ("Why is Autopay growth slowing?", "Prepare today's executive brief", "What should I focus on today?") — uses the existing Copilot APIs |
| `/tasks` | Tasks | Business tasks: action items, deadlines, progress |
| `/decisions` | Decisions | Approval queue and strategic decision log |
| `/notifications` | Notifications | Business signals only (revenue moves, risks, reports awaiting approval, deadlines); kinds muted in Settings are hidden |
| `/settings` | Settings | Organization, users, notification preferences, AI provider, data sources, theme, administrator switch |
| `/data` | Data | Upload and manage business data (projects) |

Shell: `frontend/src/components/ExecLayout.jsx` — left navigation limited to
the routes above, plus organization-wide search. The Admin Console link
appears only when administrator mode is enabled.

## Admin Console (`/admin`)

Every engineering screen moved here: Overview, Runtime, Brain, Scheduler,
Jobs, Sync, Knowledge, Logs, Diagnostics, Model status, plus a link to the
per-project data workbench.

Access is gated by an administrator switch (Settings → Administration).
`AdminLayout` renders a lock screen for non-admins. The backend has no user
model yet, so the role is a client-side device preference
(`frontend/src/lib/prefs.js`, `localStorage`) — real accounts/roles arrive
with the V2 user model.

## Preferences

Kept per-device in `localStorage` (`frontend/src/lib/prefs.js`):

- `edip.theme` — `midnight` (default) or `graphite`; applied before first
  paint via `data-theme` on `<html>`.
- `edip.admin` — administrator mode toggle.
- `edip.notify-prefs` — per-kind notification muting, respected by the
  Notifications page.

## Build

```bash
cd frontend && npm run build   # vite production build — run after every major change
```
