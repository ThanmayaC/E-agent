// Desktop shell (EnterpriseAI.exe) injects the Core origin + per-launch bearer
// token as window.__CORE__ before any app code runs. In the browser dev/web
// build it is undefined and we fall back to the Vite proxy / VITE_API_URL with
// no token (the web Core does not require one).
const CORE = (typeof window !== 'undefined' && window.__CORE__) || null
const BASE = (CORE && CORE.url) || import.meta.env.VITE_API_URL || ''
const AUTH_HEADERS = CORE && CORE.token ? { Authorization: `Bearer ${CORE.token}` } : {}

// Default request ceiling. A hung backend (e.g. a slow local model retrying)
// must never leave the UI waiting forever — the request aborts and the caller's
// catch/finally runs, so loading indicators always clear. Override per call with
// options.timeoutMs (the copilot uses a longer one).
const DEFAULT_TIMEOUT_MS = 60000

async function request(path, options = {}) {
  const { timeoutMs = DEFAULT_TIMEOUT_MS, ...opts } = options
  const contentType = opts.body instanceof FormData ? {} : { 'Content-Type': 'application/json' }
  const controller = new AbortController()
  const timer = setTimeout(() => controller.abort(), timeoutMs)
  let res
  try {
    res = await fetch(`${BASE}/api/v1${path}`, {
      ...opts,
      signal: opts.signal || controller.signal,
      headers: { ...contentType, ...AUTH_HEADERS, ...(opts.headers || {}) },
    })
  } catch (e) {
    if (e.name === 'AbortError') {
      throw new Error(`Request timed out after ${Math.round(timeoutMs / 1000)}s — the server did not respond in time.`)
    }
    throw e
  } finally {
    clearTimeout(timer)
  }
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
  // V3.1 Executive Intelligence — the AI Product Head layer
  executiveStatus: () => request('/executive'),
  executiveBrief: () => request('/executive/brief'),
  executivePriorities: () => request('/executive/priorities'),
  executiveRecommendations: () => request('/executive/recommendations'),
  executiveKpis: () => request('/executive/kpis'),
  executiveDecisions: () => request('/executive/decisions'),
  executiveRisks: () => request('/executive/risks'),
  executivePatterns: () => request('/executive/patterns'),
  executiveTrends: () => request('/executive/trends'),
  executiveWeekOverWeek: () => request('/executive/week-over-week'),
  executiveMonthOverMonth: () => request('/executive/month-over-month'),
  executiveReports: () => request('/executive/reports'),
  // V7.0 UPI Ecosystem analytics (over the sampled ledger + aggregate cubes)
  ecosystemStatus: () => request('/executive/ecosystem'),
  ecosystemOverview: () => request('/executive/ecosystem/overview'),
  ecosystemFeatures: () => request('/executive/ecosystem/features'),
  ecosystemFeature: (feature) => request(`/executive/ecosystem/features/${encodeURIComponent(feature)}`),
  ecosystemBanks: () => request('/executive/ecosystem/banks'),
  ecosystemPsps: () => request('/executive/ecosystem/psps'),
  ecosystemMarketShare: () => request('/executive/ecosystem/market-share'),
  ecosystemGrowth: () => request('/executive/ecosystem/growth'),
  ecosystemCities: () => request('/executive/ecosystem/cities'),
  ecosystemHourly: () => request('/executive/ecosystem/hourly'),
  ecosystemMix: () => request('/executive/ecosystem/mix'),
  ecosystemAnomalies: () => request('/executive/ecosystem/anomalies'),
  ecosystemForecasts: () => request('/executive/ecosystem/forecasts'),
  ecosystemKpis: () => request('/executive/ecosystem/kpis'),
  // V8.0 six-month evolution — the continuously-evolving digital twin
  evolutionStatus: () => request('/executive/evolution'),
  evolutionOverview: () => request('/executive/evolution/overview'),
  evolutionCustomers: () => request('/executive/evolution/customers'),
  evolutionMerchants: () => request('/executive/evolution/merchants'),
  evolutionMerchant: (name) => request(`/executive/evolution/merchants/${encodeURIComponent(name)}`),
  evolutionBanks: () => request('/executive/evolution/banks'),
  evolutionPsps: () => request('/executive/evolution/psps'),
  evolutionProducts: () => request('/executive/evolution/products'),
  evolutionProduct: (name) => request(`/executive/evolution/products/${encodeURIComponent(name)}`),
  evolutionFeatures: () => request('/executive/evolution/features'),
  evolutionTrends: (grain = 'monthly') => request(`/executive/evolution/trends?grain=${grain}`),
  evolutionTrend: (kpi) => request(`/executive/evolution/trends/${encodeURIComponent(kpi)}`),
  evolutionForecastAccuracy: () => request('/executive/evolution/forecast-accuracy'),
  evolutionForecast: (kpi) => request(`/executive/evolution/forecast/${encodeURIComponent(kpi)}`),
  evolutionDecisions: () => request('/executive/evolution/decisions'),
  evolutionDecision: (id) => request(`/executive/evolution/decisions/${encodeURIComponent(id)}`),
  evolutionCrossEntity: (entity = '') => request(`/executive/evolution/cross-entity${entity ? `?entity=${encodeURIComponent(entity)}` : ''}`),
  evolutionStories: () => request('/executive/evolution/stories'),
  evolutionStory: (week) => request(`/executive/evolution/stories/${week}`),
  evolutionAsk: (q) => request(`/executive/evolution/ask?q=${encodeURIComponent(q)}`),
  // V9.0 AI Workspace — universal upload+understanding, unified search, artifacts
  workspaceStatus: () => request('/workspace'),
  workspaceHome: () => request('/workspace/home'),
  workspaceUpload: (files) => {
    const form = new FormData()
    for (const f of files) form.append('files', f)
    return request('/workspace/upload', { method: 'POST', body: form })
  },
  workspaceFiles: () => request('/workspace/files'),
  workspaceFile: (id) => request(`/workspace/files/${id}`),
  deleteWorkspaceFile: (id) => request(`/workspace/files/${id}`, { method: 'DELETE' }),
  workspaceSearch: (q, limit = 40) => request(`/workspace/search?q=${encodeURIComponent(q)}&limit=${limit}`),
  generateArtifact: (payload) => request('/workspace/artifacts', { method: 'POST', body: JSON.stringify(payload) }),
  workspaceArtifacts: () => request('/workspace/artifacts'),
  workspacePins: () => request('/workspace/pins'),
  addWorkspacePin: (bucket, item) => request('/workspace/pins', { method: 'POST', body: JSON.stringify({ bucket, item }) }),
  removeWorkspacePin: (bucket, id) => request(`/workspace/pins/${bucket}/${id}`, { method: 'DELETE' }),
  workspaceContext: (page = '') => request(`/workspace/context?page=${encodeURIComponent(page)}`),
  artifactUrl: (name) => `${BASE}/api/v1/workspace/artifacts/${name}`,
  // V10.0 analyst layer — ML models, insights, continuous learning, cache
  mlStatus: () => request('/ml'),
  mlModels: () => request('/ml/models'),
  mlForecast: (kpi = 'Success Rate (%)', horizon = 30) => request(`/ml/forecast?kpi=${encodeURIComponent(kpi)}&horizon=${horizon}`),
  mlAnomalies: () => request('/ml/anomalies'),
  mlSegments: (k = 4) => request(`/ml/segments?k=${k}`),
  mlChurn: () => request('/ml/churn'),
  mlFailure: () => request('/ml/failure'),
  insights: (limit = 12) => request(`/insights?limit=${limit}`),
  learningStats: () => request('/learning'),
  sendFeedback: (ref, action, kind = 'recommendation', meta = {}) =>
    request('/learning/feedback', { method: 'POST', body: JSON.stringify({ kind, ref, action, meta }) }),
  cacheStats: () => request('/cache'),
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
    // Longer ceiling than the default: a local model may legitimately take a
    // while, but it is still bounded so the UI always recovers.
    request('/copilot/chat', { method: 'POST', body: JSON.stringify({ message, conversation_id }), timeoutMs: 150000 }),
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
  // Phase 2 — Communications: email as enterprise knowledge
  commProviders: () => request('/communication/providers'),
  commInbox: (provider = '', folder = 'inbox', top = 25) =>
    request(`/communication/inbox?folder=${encodeURIComponent(folder)}&top=${top}${provider ? `&provider=${encodeURIComponent(provider)}` : ''}`),
  commSearch: (q, provider = '', top = 25) =>
    request(`/communication/search?q=${encodeURIComponent(q)}&top=${top}${provider ? `&provider=${encodeURIComponent(provider)}` : ''}`),
  commAnalyze: (email) => request('/communication/analyze', { method: 'POST', body: JSON.stringify(email) }),
  commDraft: (kind, context) => request('/communication/draft', { method: 'POST', body: JSON.stringify({ kind, context }) }),
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
  // Enterprise RAG diagnostics + live retrieval test
  ragDiagnostics: () => request('/documents/rag'),
  documentsSearch: (q, limit = 8) =>
    request(`/documents/search?q=${encodeURIComponent(q)}&limit=${limit}`),
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

  // ── Enterprise Intelligence (V11) — the raw-transaction warehouse surface.
  // Every method below answers from individual payments: analytics is SQL over
  // transactions, ML is the backtested pipeline, and the product / ecosystem /
  // MCC / admin views are compositions of those. `q` is a slice object
  // ({ product, bank, psp, mcc, last_days, start, end, ... }); see Filters.
  intelStatus: () => request('/intel/status'),
  intelKpis: (q) => request(`/intel/analytics/kpis${qs(q)}`),
  intelSeries: (q) => request(`/intel/analytics/series${qs(q)}`),
  intelMonthly: (q) => request(`/intel/analytics/monthly${qs(q)}`),
  intelProfile: (q) => request(`/intel/analytics/profile${qs(q)}`),
  intelDimension: (dim, q) => request(`/intel/analytics/dimension/${dim}${qs(q)}`),
  intelDimensionSeries: (dim, q) =>
    request(`/intel/analytics/dimension/${dim}/series${qs(q)}`),
  intelFailures: (q) => request(`/intel/analytics/failures${qs(q)}`),
  intelRetry: (q) => request(`/intel/analytics/retry${qs(q)}`),
  intelAdjustments: (q) => request(`/intel/analytics/adjustments${qs(q)}`),
  intelCustomers: (q) => request(`/intel/analytics/customers${qs(q)}`),
  intelCohorts: (q) => request(`/intel/analytics/cohorts${qs(q)}`),
  intelConcentration: (q) => request(`/intel/analytics/concentration${qs(q)}`),
  intelGeography: (q) => request(`/intel/analytics/geography${qs(q)}`),
  intelMandates: (q) => request(`/intel/analytics/mandates${qs(q)}`),
  intelIncidents: (q) => request(`/intel/analytics/incidents${qs(q)}`),
  // ML
  intelForecast: (q) => request(`/intel/ml/forecast${qs(q)}`),
  intelEda: (q) => request(`/intel/ml/eda${qs(q)}`),
  intelAnomalies: (q) => request(`/intel/ml/anomalies${qs(q)}`),
  intelSegments: (q) => request(`/intel/ml/segments${qs(q)}`),
  intelMerchantHealth: (q) => request(`/intel/ml/merchant-health${qs(q)}`),
  intelForecastable: () => request('/intel/ml/forecastable'),
  // Products
  intelProducts: (q) => request(`/intel/products${qs(q)}`),
  intelProduct: (code, q) =>
    request(`/intel/products/${encodeURIComponent(code)}${qs(q)}`),
  // Ecosystem + MCC
  intelGraph: (q) => request(`/intel/ecosystem/graph${qs(q)}`),
  intelNode: (type, id, q) =>
    request(`/intel/ecosystem/node/${type}/${encodeURIComponent(id)}${qs(q)}`),
  intelMcc: (q) => request(`/intel/mcc${qs(q)}`),
  intelMccDetail: (code, q) =>
    request(`/intel/mcc/${encodeURIComponent(code)}${qs(q)}`),
  // Admin
  intelSubsystems: () => request('/intel/admin/subsystems'),
  intelAdminWarehouse: () => request('/intel/admin/warehouse'),
}

// Build a query string from a slice object, dropping empty values.
function qs(q) {
  if (!q) return ''
  const parts = Object.entries(q)
    .filter(([, v]) => v !== null && v !== undefined && v !== '')
    .map(([k, v]) => `${encodeURIComponent(k)}=${encodeURIComponent(v)}`)
  return parts.length ? `?${parts.join('&')}` : ''
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
