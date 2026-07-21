const BASE = import.meta.env.VITE_API_URL || ''

async function request(path, options = {}) {
  const res = await fetch(`${BASE}/api/v1${path}`, {
    headers: options.body instanceof FormData ? {} : { 'Content-Type': 'application/json' },
    ...options,
  })
  if (!res.ok) {
    const detail = await res.json().catch(() => ({}))
    throw new Error(detail.detail || `${res.status} ${res.statusText}`)
  }
  if (res.status === 204) return null
  return res.json()
}

export const api = {
  listProjects: () => request('/projects'),
  createProject: (name) => request('/projects', { method: 'POST', body: JSON.stringify({ name }) }),
  getProject: (id) => request(`/projects/${id}`),
  deleteProject: (id) => request(`/projects/${id}`, { method: 'DELETE' }),
  // XHR instead of fetch so callers can observe real upload progress
  uploadFiles: (id, files, onProgress) =>
    new Promise((resolve, reject) => {
      const form = new FormData()
      for (const f of files) form.append('files', f)
      const xhr = new XMLHttpRequest()
      xhr.open('POST', `${BASE}/api/v1/projects/${id}/files`)
      if (onProgress) {
        xhr.upload.onprogress = (e) => {
          if (e.lengthComputable) onProgress(Math.round((e.loaded / e.total) * 100))
        }
      }
      xhr.onload = () => {
        let body = {}
        try { body = JSON.parse(xhr.responseText) } catch { /* non-JSON error body */ }
        if (xhr.status >= 200 && xhr.status < 300) resolve(body)
        else reject(new Error(body.detail || `${xhr.status} ${xhr.statusText}`))
      }
      xhr.onerror = () => reject(new Error('Network error during upload'))
      xhr.send(form)
    }),
  analyze: (id) => request(`/projects/${id}/analyze`, { method: 'POST' }),
  status: (id) => request(`/projects/${id}/status`),
  clarifications: (id) => request(`/projects/${id}/clarifications`),
  answerClarifications: (id, answers) =>
    request(`/projects/${id}/clarifications`, { method: 'POST', body: JSON.stringify({ answers }) }),
  datasets: (id) => request(`/projects/${id}/datasets`),
  preview: (id, ds) => request(`/projects/${id}/datasets/${ds}/preview`),
  semantics: (id) => request(`/projects/${id}/semantics`),
  relationships: (id) => request(`/projects/${id}/relationships`),
  graph: (id) => request(`/projects/${id}/graph`),
  kpis: (id) => request(`/projects/${id}/kpis`),
  signals: (id) => request(`/projects/${id}/signals`),
  aiReport: (id) => request(`/projects/${id}/ai-report`),
  context: (id) => request(`/projects/${id}/context`),
  insights: (id) => request(`/projects/${id}/insights`),
  predictions: (id) => request(`/projects/${id}/predictions`),
  recommendations: (id) => request(`/projects/${id}/recommendations`),
  quality: (id) => request(`/projects/${id}/quality`),
  breakdowns: (id) => request(`/projects/${id}/breakdowns`),
  report: (id) => request(`/projects/${id}/report`),
  reportMarkdown: (id) => request(`/projects/${id}/report/markdown`),
  ask: (id, question) => request(`/projects/${id}/copilot/chat`, { method: 'POST', body: JSON.stringify({ question }) }),
  query: (id, sql) => request(`/projects/${id}/query`, { method: 'POST', body: JSON.stringify({ sql }) }),
  // Enterprise knowledge (org-wide, persistent)
  knowledge: () => request('/knowledge'),
  knowledgeSearch: (q) => request(`/knowledge/search?q=${encodeURIComponent(q)}`),
  // V2.5 Executive Experience — org-wide graph, relationships, learning stream
  enterpriseGraph: (limit = 800) => request(`/knowledge/graph?limit=${limit}`),
  enterpriseGraphNode: (id) => request(`/knowledge/graph/node?id=${encodeURIComponent(id)}`),
  enterpriseGraphSearch: (q) => request(`/knowledge/graph/search?q=${encodeURIComponent(q)}`),
  enterpriseRelationships: (kind = '', limit = 400) =>
    request(`/knowledge/relationships?limit=${limit}${kind ? `&kind=${encodeURIComponent(kind)}` : ''}`),
  learningHistory: (limit = 200) => request(`/learning/history?limit=${limit}`),
  addTerm: (term, definition, aliases = []) =>
    request('/knowledge/terms', { method: 'POST', body: JSON.stringify({ term, definition, aliases }) }),
  addRule: (rule, scope = 'global') =>
    request('/knowledge/rules', { method: 'POST', body: JSON.stringify({ rule, scope }) }),
  addClarification: (question, answer, project_id = '') =>
    request('/knowledge/clarifications', { method: 'POST', body: JSON.stringify({ question, answer, project_id }) }),
  // Platform introspection + workflows
  platformAgents: () => request('/platform/agents'),
  platformTools: () => request('/platform/tools'),
  platformConnectors: () => request('/platform/connectors'),
  platformWorkflows: () => request('/platform/workflows'),
  workflowRuns: (id) => request(`/projects/${id}/workflow-runs`),
  workflowSchedules: (id) => request(`/projects/${id}/workflow-schedules`),
  addWorkflowSchedule: (id, workflow, cadence) =>
    request(`/projects/${id}/workflow-schedules`, { method: 'POST', body: JSON.stringify({ workflow, cadence }) }),
  // Executive Workspace (Manager Module)
  managerDashboard: () => request('/manager/dashboard'),
  managerWorkspace: () => request('/manager/workspace'),
  dailyBrief: (regenerate = false) => request(`/manager/daily-brief${regenerate ? '?regenerate=true' : ''}`),
  managerTasks: (status = '') => request(`/manager/tasks${status ? `?status=${status}` : ''}`),
  createTask: (payload) => request('/manager/tasks', { method: 'POST', body: JSON.stringify(payload) }),
  setTaskStatus: (id, status) =>
    request(`/manager/tasks/${id}`, { method: 'PATCH', body: JSON.stringify({ status }) }),
  managerDecisions: () => request('/manager/decisions'),
  recordDecision: (payload) => request('/manager/decisions', { method: 'POST', body: JSON.stringify(payload) }),
  setDecisionStatus: (id, status, by = '') =>
    request(`/manager/decisions/${id}`, { method: 'PATCH', body: JSON.stringify({ status, by }) }),
  managerNotifications: (unread = false) => request(`/manager/notifications${unread ? '?unread=true' : ''}`),
  markNotificationRead: (id) => request(`/manager/notifications/${id}/read`, { method: 'POST' }),
  markAllNotificationsRead: () => request('/manager/notifications/read-all', { method: 'POST' }),
  reportReviews: (status = '') => request(`/manager/reports${status ? `?status=${status}` : ''}`),
  setReviewStatus: (id, status, by = '', note = '') =>
    request(`/manager/reports/${id}/status`, { method: 'POST', body: JSON.stringify({ status, by, note }) }),
  managerPortfolio: () => request('/manager/portfolio'),
  integrations: () => request('/manager/integrations'),
  // Enterprise Brain (technical status — Admin only)
  brainStatus: () => request('/brain/status'),
  brainStatistics: () => request('/brain/statistics'),
  // Autonomous execution layer (Runtime Dashboard)
  runtimeStatus: () => request('/runtime'),
  runtimeActivity: (limit = 20) => request(`/runtime/activity?limit=${limit}`),
  runtimeJobs: () => request('/runtime/jobs'),
  runJob: (name) => request(`/runtime/jobs/${name}/run`, { method: 'POST' }),
  setJobEnabled: (name, enabled) =>
    request(`/runtime/jobs/${name}`, { method: 'PATCH', body: JSON.stringify({ enabled }) }),
  runtimeEvents: (limit = 50) => request(`/runtime/events?limit=${limit}`),
  runtimeActions: (status = '') => request(`/runtime/actions${status ? `?status=${status}` : ''}`),
  runtimeQueue: () => request('/runtime/queue'),
  approveAction: (id, by = '') =>
    request(`/runtime/actions/${id}/approve`, { method: 'POST', body: JSON.stringify({ by }) }),
  rejectAction: (id, by = '', reason = '') =>
    request(`/runtime/actions/${id}/reject`, { method: 'POST', body: JSON.stringify({ by, reason }) }),
  runtimeGoals: () => request('/runtime/goals'),
  createGoal: (payload) => request('/runtime/goals', { method: 'POST', body: JSON.stringify(payload) }),
  runtimeMetrics: () => request('/runtime/metrics'),
  runtimeTriggers: () => request('/runtime/triggers'),
  runtimeDecisions: () => request('/runtime/decisions'),
  startScheduler: () => request('/runtime/scheduler/start', { method: 'POST' }),
  stopScheduler: () => request('/runtime/scheduler/stop', { method: 'POST' }),
  runtimeExecutions: (limit = 50) => request(`/runtime/executions?limit=${limit}`),
  // V2.4 Decision Intelligence — the Brain deciding, not just informing
  intelligenceBrief: () => request('/runtime/intelligence/brief'),
  intelligenceStatus: () => request('/runtime/intelligence'),
  intelligenceDecisions: (status = '', limit = 50) =>
    request(`/runtime/intelligence/decisions?limit=${limit}${status ? `&status=${status}` : ''}`),
  intelligenceRecommendations: (limit = 5) => request(`/runtime/intelligence/recommendations?limit=${limit}`),
  intelligenceSignals: (limit = 50) => request(`/runtime/intelligence/signals?limit=${limit}`),
  setIntelligenceDecision: (id, status, by = '', note = '') =>
    request(`/runtime/intelligence/decisions/${id}`, { method: 'PATCH', body: JSON.stringify({ status, by, note }) }),
  proposeDecision: (payload) =>
    request('/runtime/intelligence/decisions', { method: 'POST', body: JSON.stringify(payload) }),
  intelligenceReport: (period = 'daily') => request(`/runtime/intelligence/reports/${period}`),
  intelligenceObserve: () => request('/runtime/intelligence/observe', { method: 'POST' }),
  // Enterprise Copilot (organization-wide conversational surface)
  copilotChat: (message, conversation_id = '') =>
    request('/copilot/chat', { method: 'POST', body: JSON.stringify({ message, conversation_id }) }),
  copilotWorkspace: () => request('/copilot'),
  copilotSuggestions: (limit = 6) => request(`/copilot/suggestions?limit=${limit}`),
  copilotIntents: () => request('/copilot/intents'),
  copilotConversations: () => request('/copilot/conversations'),
  copilotConversation: (id) => request(`/copilot/conversations/${id}`),
  deleteCopilotConversation: (id) => request(`/copilot/conversations/${id}`, { method: 'DELETE' }),
  pinCopilotConversation: (id, pinned) =>
    request(`/copilot/conversations/${id}`, { method: 'PATCH', body: JSON.stringify({ pinned }) }),
  // Executive views over the organization and the product portfolio
  managerProducts: () => request('/manager/products'),
  managerProductReviews: (limit = 6) => request(`/manager/product-reviews?limit=${limit}`),
  managerOrganization: () => request('/manager/organization'),
  managerSearch: (q, limit = 12) => request(`/manager/search?q=${encodeURIComponent(q)}&limit=${limit}`),
  dailyBriefHistory: (limit = 14) => request(`/manager/daily-brief/history?limit=${limit}`),
  productOverview: () => request('/product'),
  productPortfolio: () => request('/product/portfolio'),
  productHealth: () => request('/product/health'),
  productGrowth: (product_id = '') => request(`/product/growth${product_id ? `?product_id=${encodeURIComponent(product_id)}` : ''}`),
  productReviewsFor: (product_id = '', limit = 20) =>
    request(`/product/reviews?limit=${limit}${product_id ? `&product_id=${encodeURIComponent(product_id)}` : ''}`),
  productRecommendations: (product_id = '', status = '') =>
    request(`/product/recommendations?limit=100${product_id ? `&product_id=${encodeURIComponent(product_id)}` : ''}${status ? `&status=${status}` : ''}`),
  productCatalogItem: (product_id) => request(`/product/catalog/${product_id}`),
  // V2: autonomous operations
  overnightSummary: (hours = 16) => request(`/manager/overnight?hours=${hours}`),
  editAction: (id, changes, by = '') =>
    request(`/runtime/actions/${id}`, { method: 'PATCH', body: JSON.stringify({ ...changes, by }) }),
  documentsStatus: () => request('/documents/status'),
  documentsList: (category = '', limit = 100) =>
    request(`/documents?limit=${limit}${category ? `&category=${category}` : ''}`),
  documentVersions: (id) => request(`/documents/${id}/versions`),
  registerSource: (payload) => request('/sources', { method: 'POST', body: JSON.stringify(payload) }),
  // Organization synchronization (Admin Console)
  syncSources: () => request('/sources'),
  syncSourcesStatus: () => request('/sources/status'),
  syncNow: () => request('/sources/sync', { method: 'POST' }),
  orgOverview: () => request('/organization'),
  orgRefreshes: () => request('/organization/refreshes'),
  // V2.1: Enterprise Connector Framework (Admin Console only — managers
  // never configure a data source and never see these surfaces)
  connectorsOverview: () => request('/connectors'),
  connectorCatalogue: () => request('/connectors/catalogue'),
  connectorSources: (kind = '', health = '') =>
    request(`/connectors/sources?${new URLSearchParams({ kind, health })}`),
  connectorSource: (id) => request(`/connectors/sources/${id}`),
  registerConnector: (payload) =>
    request('/connectors/sources', { method: 'POST', body: JSON.stringify(payload) }),
  updateConnector: (id, changes) =>
    request(`/connectors/sources/${id}`, { method: 'PATCH', body: JSON.stringify(changes) }),
  deleteConnector: (id) => request(`/connectors/sources/${id}`, { method: 'DELETE' }),
  testConnector: (id) => request(`/connectors/sources/${id}/test`, { method: 'POST' }),
  discoverConnector: (id) => request(`/connectors/sources/${id}/discover`, { method: 'POST' }),
  syncConnector: (id, full = false) =>
    request(`/connectors/sources/${id}/sync?full=${full}`, { method: 'POST' }),
  syncAllConnectors: (full = false) =>
    request(`/connectors/sync?full=${full}`, { method: 'POST' }),
  connectorRuns: (id = '', limit = 50) =>
    request(`/connectors/runs?limit=${limit}${id ? `&connector_id=${id}` : ''}`),
  connectorFailures: (id = '', limit = 50) =>
    request(`/connectors/failures?limit=${limit}${id ? `&connector_id=${id}` : ''}`),
  connectorPackages: (id = '', limit = 100) =>
    request(`/connectors/packages?limit=${limit}${id ? `&connector_id=${id}` : ''}`),
  // V2.2: Enterprise AI Operating Layer (Admin Console only)
  opsObservability: () => request('/ops/observability'),
  opsAgents: (capability = '') =>
    request(`/ops/agents${capability ? `?capability=${capability}` : ''}`),
  opsRunAgent: (id, payload = {}) =>
    request(`/ops/agents/${id}/run`, { method: 'POST', body: JSON.stringify(payload) }),
  opsTools: () => request('/ops/tools'),
  opsPrompts: (domain = '') =>
    request(`/ops/prompts${domain ? `?domain=${domain}` : ''}`),
  opsPrompt: (id) => request(`/ops/prompts/${encodeURIComponent(id)}`),
  opsEvaluation: () => request('/ops/evaluation'),
  opsEvaluationHistory: (decision = '', limit = 50) =>
    request(`/ops/evaluation/history?limit=${limit}${decision ? `&decision=${decision}` : ''}`),
  opsGovernance: () => request('/ops/governance'),
  opsAuditLog: (limit = 100) => request(`/ops/governance/audit?limit=${limit}`),
  opsModelUsage: () => request('/ops/governance/model-usage'),
  opsAssignRole: (principal, role) =>
    request('/ops/governance/assign', { method: 'POST', body: JSON.stringify({ principal, role }) }),
  opsMemoryLifecycle: () => request('/ops/memory/lifecycle'),
  opsWorkflows: () => request('/ops/workflows'),
  opsRunWorkflow: (id) => request(`/ops/workflows/${id}/run`, { method: 'POST' }),
}

export const fmt = {
  num: (v) => {
    if (v === null || v === undefined) return '—'
    const n = Number(v)
    if (Number.isNaN(n)) return String(v)
    if (Math.abs(n) >= 1e6) return `${(n / 1e6).toFixed(2)}M`
    if (Math.abs(n) >= 1e3) return n.toLocaleString(undefined, { maximumFractionDigits: 0 })
    return n.toLocaleString(undefined, { maximumFractionDigits: 2 })
  },
  pct: (v) => (v === null || v === undefined ? '—' : `${v > 0 ? '+' : ''}${Number(v).toFixed(1)}%`),
}
