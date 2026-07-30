import { Navigate, Route, Routes } from 'react-router-dom'
import ExecLayout from './components/ExecLayout'
import AdminLayout from './components/AdminLayout'

// Executive Workspace — business surfaces only. Every route below is reachable
// from the rail in ExecLayout or from the header; nothing is mounted that the
// user cannot navigate to.
import AIHome from './pages/AIHome'
import Files from './pages/Files'
import Search from './pages/Search'
import ReportsHub from './pages/ReportsHub'
import Products from './pages/Products'
import ProductSummary from './pages/ProductSummary'
import EcosystemDashboard from './pages/EcosystemDashboard'
import Evolution from './pages/Evolution'
import Intelligence from './pages/Intelligence'
import ReportView from './pages/ReportView'
import AIAssistant from './pages/AIAssistant'
import Communications from './pages/Communications'
import Timeline from './pages/Timeline'
import Tasks from './pages/Tasks'
import Decisions from './pages/Decisions'
import Notifications from './pages/Notifications'
import Settings from './pages/Settings'
import Projects from './pages/Projects'

// Admin Console — engineering surfaces, administrators only. Every route here
// maps to a real subsystem in AdminLayout's NAV.
import AdminOverview from './pages/admin/AdminOverview'
import AdminRuntime from './pages/admin/AdminRuntime'
import AdminBrain from './pages/admin/AdminBrain'
import AdminJobs from './pages/admin/AdminJobs'
import AdminConnectors from './pages/admin/AdminConnectors'
import AdminSync from './pages/admin/AdminSync'
import AdminDiagnostics from './pages/admin/AdminDiagnostics'
import AdminModels from './pages/admin/AdminModels'
import AdminLLM from './pages/admin/AdminLLM'
import AdminWarehouse from './pages/admin/AdminWarehouse'
import GraphExplorer from './pages/GraphExplorer'

export default function App() {
  return (
    <Routes>
      {/* Executive Workspace — the production experience */}
      <Route element={<ExecLayout />}>
        <Route path="/" element={<AIHome />} />
        <Route path="/files" element={<Files />} />
        <Route path="/search" element={<Search />} />
        <Route path="/reports" element={<ReportsHub />} />
        <Route path="/reports/:projectId" element={<ReportView />} />
        <Route path="/products" element={<Products />} />
        <Route path="/products/:productId" element={<ProductSummary />} />
        <Route path="/ecosystem" element={<EcosystemDashboard />} />
        <Route path="/evolution" element={<Evolution />} />
        <Route path="/intelligence" element={<Intelligence />} />
        <Route path="/decisions" element={<Decisions />} />
        <Route path="/assistant" element={<AIAssistant />} />
        <Route path="/communications" element={<Communications />} />
        <Route path="/timeline" element={<Timeline />} />
        <Route path="/tasks" element={<Tasks />} />
        <Route path="/notifications" element={<Notifications />} />
        <Route path="/settings" element={<Settings />} />
        <Route path="/data" element={<Projects />} />
      </Route>

      {/* Admin Console — engineering surfaces, administrators only */}
      <Route path="/admin" element={<AdminLayout />}>
        <Route index element={<AdminOverview />} />
        <Route path="warehouse" element={<AdminWarehouse />} />
        <Route path="models" element={<AdminModels />} />
        <Route path="brain" element={<AdminBrain />} />
        <Route path="graph" element={<GraphExplorer />} />
        <Route path="llm" element={<AdminLLM />} />
        <Route path="data-sources" element={<AdminConnectors />} />
        <Route path="sync" element={<AdminSync />} />
        <Route path="runtime" element={<AdminRuntime />} />
        <Route path="jobs" element={<AdminJobs />} />
        <Route path="diagnostics" element={<AdminDiagnostics />} />
      </Route>

      {/* Legacy routes kept as redirects so old links still resolve.
          `/p/*` was a per-project analyst workbench (datasets, schema, KPIs,
          insights, predictions, quality, …). It had no inbound link from any
          nav — only its own internal one — and every surface in it now has a
          live equivalent: the warehouse and graph under Admin, the numbers
          under Analytics and Evolution, the write-up under /reports/:id. The
          shell and its sixteen pages are gone; the URLs land on the report
          list, which is what the workbench was reached for. */}
      <Route path="/p/:projectId/*" element={<Navigate to="/reports" replace />} />
      <Route path="/pm-home" element={<Navigate to="/" replace />} />
      <Route path="/autonomy" element={<Navigate to="/admin/runtime" replace />} />
      <Route path="/reviews" element={<Navigate to="/reports" replace />} />
      <Route path="/projects" element={<Navigate to="/data" replace />} />
      <Route path="/workspace" element={<Navigate to="/" replace />} />
      <Route path="/brief" element={<Navigate to="/" replace />} />
      <Route path="/dashboard" element={<Navigate to="/" replace />} />
      <Route path="/portfolio" element={<Navigate to="/products" replace />} />
      <Route path="/portfolio/product/:productId" element={<Navigate to="/products" replace />} />
      <Route path="/copilot" element={<Navigate to="/assistant" replace />} />
      <Route path="/graph" element={<Navigate to="/admin/graph" replace />} />
      <Route path="/analytics/decisions" element={<Navigate to="/admin" replace />} />
      <Route path="/analytics/workflows" element={<Navigate to="/admin/jobs" replace />} />
      <Route path="/analytics/agents" element={<Navigate to="/admin" replace />} />
      <Route path="/analytics/knowledge" element={<Navigate to="/admin/graph" replace />} />
      <Route path="*" element={<Navigate to="/" />} />
    </Routes>
  )
}
