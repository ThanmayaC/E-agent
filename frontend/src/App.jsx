import { Navigate, Route, Routes, useParams } from 'react-router-dom'
import ExecLayout from './components/ExecLayout'
import AdminLayout from './components/AdminLayout'
import Layout from './components/Layout'

// Executive Workspace — business surfaces only
import Home from './pages/Home'
import ExecutiveDashboard from './pages/ExecutiveDashboard'
import Portfolio from './pages/Portfolio'
import ProductSummary from './pages/ProductSummary'
import ReportCenter from './pages/ReportCenter'
import ReportView from './pages/ReportView'
import EnterpriseCopilot from './pages/EnterpriseCopilot'
import Tasks from './pages/Tasks'
import Decisions from './pages/Decisions'
import Notifications from './pages/Notifications'
import Settings from './pages/Settings'
import Projects from './pages/Projects'

// Admin Console — engineering surfaces, administrators only
import AdminOverview from './pages/admin/AdminOverview'
import AdminRuntime from './pages/admin/AdminRuntime'
import AdminBrain from './pages/admin/AdminBrain'
import AdminScheduler from './pages/admin/AdminScheduler'
import AdminJobs from './pages/admin/AdminJobs'
import AdminConnectors from './pages/admin/AdminConnectors'
import AdminOperating from './pages/admin/AdminOperating'
import AdminSync from './pages/admin/AdminSync'
import AdminDocuments from './pages/admin/AdminDocuments'
import AdminLogs from './pages/admin/AdminLogs'
import AdminDiagnostics from './pages/admin/AdminDiagnostics'
import AdminModels from './pages/admin/AdminModels'
import Knowledge from './pages/Knowledge'

// Per-project analyst workbench (backwards compatible, linked from Admin)
import Dashboard from './pages/Dashboard'
import Datasets from './pages/Datasets'
import SchemaExplorer from './pages/SchemaExplorer'
import Relationships from './pages/Relationships'
import KnowledgeGraph from './pages/KnowledgeGraph'
import Analytics from './pages/Analytics'
import KPIs from './pages/KPIs'
import Insights from './pages/Insights'
import Predictions from './pages/Predictions'
import Recommendations from './pages/Recommendations'
import Copilot from './pages/Copilot'
import Reports from './pages/Reports'
import DataQuality from './pages/DataQuality'
import Workflows from './pages/Workflows'
import Admin from './pages/Admin'

function ProjectShell() {
  const { projectId } = useParams()
  return (
    <Layout projectId={projectId}>
      <Routes>
        <Route index element={<Dashboard />} />
        <Route path="datasets" element={<Datasets />} />
        <Route path="schema" element={<SchemaExplorer />} />
        <Route path="relationships" element={<Relationships />} />
        <Route path="graph" element={<KnowledgeGraph />} />
        <Route path="analytics" element={<Analytics />} />
        <Route path="kpis" element={<KPIs />} />
        <Route path="insights" element={<Insights />} />
        <Route path="predictions" element={<Predictions />} />
        <Route path="recommendations" element={<Recommendations />} />
        <Route path="copilot" element={<Copilot />} />
        <Route path="reports" element={<Reports />} />
        <Route path="quality" element={<DataQuality />} />
        <Route path="knowledge" element={<Knowledge />} />
        <Route path="workflows" element={<Workflows />} />
        <Route path="admin" element={<Admin />} />
      </Routes>
    </Layout>
  )
}

export default function App() {
  return (
    <Routes>
      {/* Executive Workspace — the production experience */}
      <Route element={<ExecLayout />}>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<ExecutiveDashboard />} />
        <Route path="/portfolio" element={<Portfolio />} />
        <Route path="/portfolio/product/:productId" element={<ProductSummary />} />
        <Route path="/reports" element={<ReportCenter />} />
        <Route path="/reports/:projectId" element={<ReportView />} />
        <Route path="/copilot" element={<EnterpriseCopilot />} />
        <Route path="/tasks" element={<Tasks />} />
        <Route path="/notifications" element={<Notifications />} />
        <Route path="/decisions" element={<Decisions />} />
        <Route path="/settings" element={<Settings />} />
        <Route path="/data" element={<Projects />} />
      </Route>

      {/* Admin Console — engineering surfaces, administrators only */}
      <Route path="/admin" element={<AdminLayout />}>
        <Route index element={<AdminOverview />} />
        <Route path="runtime" element={<AdminRuntime />} />
        <Route path="brain" element={<AdminBrain />} />
        <Route path="scheduler" element={<AdminScheduler />} />
        <Route path="jobs" element={<AdminJobs />} />
        <Route path="operating" element={<AdminOperating />} />
        <Route path="data-sources" element={<AdminConnectors />} />
        <Route path="sync" element={<AdminSync />} />
        <Route path="documents" element={<AdminDocuments />} />
        <Route path="knowledge" element={<Knowledge />} />
        <Route path="logs" element={<AdminLogs />} />
        <Route path="diagnostics" element={<AdminDiagnostics />} />
        <Route path="models" element={<AdminModels />} />
      </Route>

      {/* Per-project analyst workbench (unchanged URLs) */}
      <Route path="/p/:projectId/*" element={<ProjectShell />} />

      {/* Legacy routes from the developer workspace */}
      <Route path="/brief" element={<Navigate to="/dashboard" replace />} />
      <Route path="/autonomy" element={<Navigate to="/admin/runtime" replace />} />
      <Route path="/reviews" element={<Navigate to="/reports" replace />} />
      <Route path="/projects" element={<Navigate to="/data" replace />} />
      <Route path="*" element={<Navigate to="/" />} />
    </Routes>
  )
}
