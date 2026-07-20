import { useEffect, useRef, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { motion } from 'framer-motion'
import { api } from '../api/client'
import { Badge, Spinner } from '../components/ui'

const STAGE_LABELS = {
  file_discovery: 'File Discovery', worksheet_discovery: 'Worksheet Discovery',
  schema_discovery: 'Schema Discovery', column_profiling: 'Column Profiling',
  business_meaning: 'Business Meaning', deduplication: 'Duplicate Detection',
  relationship_detection: 'Relationships', time_series_detection: 'Time Series',
  kpi_discovery: 'KPI Discovery', data_quality: 'Data Quality',
  semantic_layer: 'Business Glossary', knowledge_graph: 'Relationship Mapping',
  embeddings: 'Search Indexing', analytics: 'Analytics', signals: 'Statistical Signals',
  predictions: 'Predictions', confidence_assessment: 'Confidence Assessment',
  business_context: 'Building Business Context', ai_reasoning: 'AI Reasoning',
  report: 'Executive Report',
}

const CATEGORY_LABELS = {
  entity_understanding: 'Entities', metric_understanding: 'Metrics',
  time_understanding: 'Time', business_meaning: 'Business Meaning',
  relationship_understanding: 'Relationships', dimension_understanding: 'Dimensions',
  schema_completeness: 'Schema', data_quality: 'Quality',
}

function analysisDuration(p) {
  const starts = (p.stages || []).map((s) => s.started_at).filter(Boolean).sort()
  const ends = (p.stages || []).map((s) => s.finished_at).filter(Boolean).sort()
  if (!starts.length || !ends.length) return null
  const secs = (new Date(ends[ends.length - 1]) - new Date(starts[0])) / 1000
  if (!(secs >= 0)) return null
  return secs < 60 ? `${Math.round(secs)}s` : `${Math.floor(secs / 60)}m ${Math.round(secs % 60)}s`
}

const confTone = (v) => (v >= 0.7 ? 'success' : v >= 0.5 ? 'warn' : 'danger')

export default function Projects() {
  const [projects, setProjects] = useState(null)
  const [name, setName] = useState('')
  const [files, setFiles] = useState([])
  const [busy, setBusy] = useState(false)
  const [uploadPct, setUploadPct] = useState(null)
  const [active, setActive] = useState(null) // { projectId, stages, status }
  const [clarify, setClarify] = useState(null) // understanding assessment while paused
  const [answers, setAnswers] = useState({})   // question_id -> answer
  const [resuming, setResuming] = useState(false)
  const [confirmDelete, setConfirmDelete] = useState(null) // project_id pending confirmation
  const [deleting, setDeleting] = useState(null)
  const [error, setError] = useState(null)
  const navigate = useNavigate()
  const pollRef = useRef(null)
  const clarifyFetchedRef = useRef(false)

  const refresh = () => api.listProjects().then(setProjects).catch((e) => setError(e.message))
  useEffect(() => { refresh(); return () => clearInterval(pollRef.current) }, [])

  function poll(projectId) {
    clearInterval(pollRef.current)
    pollRef.current = setInterval(async () => {
      const s = await api.status(projectId)
      setActive({ projectId, ...s })
      if (s.status === 'awaiting_clarification' && !clarifyFetchedRef.current) {
        clarifyFetchedRef.current = true
        setResuming(false)
        api.clarifications(projectId).then(setClarify).catch(() => { clarifyFetchedRef.current = false })
      }
      if (s.status === 'ready') {
        clearInterval(pollRef.current)
        navigate(`/reports/${projectId}`)
      }
      if (s.status === 'failed') clearInterval(pollRef.current)
    }, 1200)
  }

  async function launch() {
    if (!name.trim() || files.length === 0) return
    setBusy(true); setError(null); setClarify(null); setAnswers({})
    clarifyFetchedRef.current = false
    try {
      const project = await api.createProject(name.trim())
      setUploadPct(0)
      await api.uploadFiles(project.project_id, files, setUploadPct)
      await api.analyze(project.project_id)
      setActive({ projectId: project.project_id, status: 'analyzing', stages: [] })
      poll(project.project_id)
    } catch (e) {
      setError(e.message)
    } finally {
      setBusy(false)
      setUploadPct(null)
    }
  }

  async function removeProject(projectId) {
    setDeleting(projectId); setError(null)
    try {
      await api.deleteProject(projectId)
      if (active?.projectId === projectId) {
        clearInterval(pollRef.current)
        setActive(null); setClarify(null)
      }
      await refresh()
    } catch (e) {
      setError(e.message)
    } finally {
      setDeleting(null); setConfirmDelete(null)
    }
  }

  async function submitAnswers() {
    const payload = Object.entries(answers)
      .filter(([, v]) => v && v.trim())
      .map(([question_id, answer]) => ({ question_id, answer: answer.trim() }))
    if (!payload.length) return
    setError(null)
    try {
      await api.answerClarifications(active.projectId, payload)
      setClarify(null); setAnswers({}); setResuming(true)
      clarifyFetchedRef.current = false
      poll(active.projectId) // analysis resumes automatically on the backend
    } catch (e) {
      setError(e.message)
    }
  }

  function openProject(p) {
    if (p.status === 'awaiting_clarification') {
      setActive({ projectId: p.project_id, status: p.status, stages: p.stages || [] })
      clarifyFetchedRef.current = true
      api.clarifications(p.project_id).then(setClarify).catch(() => { clarifyFetchedRef.current = false })
      poll(p.project_id)
    } else {
      navigate(`/reports/${p.project_id}`)
    }
  }

  return (
    <div className="max-w-4xl mx-auto py-12 px-6">
      <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }}>
        <h1 className="text-3xl font-bold text-slate-100 tracking-tight">Business data</h1>
        <p className="text-slate-500 mt-2 max-w-2xl">
          Upload any Excel files — 1 or 1,000. The platform understands the business meaning,
          relationships, and KPIs automatically, then delivers insights, forecasts, and an
          executive report. No mapping. No configuration.
        </p>
      </motion.div>

      <div className="card-pad mt-8 space-y-4">
        <div className="h-sub">New analysis</div>
        <input className="input" placeholder="Project name, e.g. Q3 Payments Portfolio"
               value={name} onChange={(e) => setName(e.target.value)} />
        <label className="block border-2 border-dashed border-surface-border rounded-xl p-8 text-center cursor-pointer hover:border-accent/60 transition-colors">
          <input type="file" multiple accept=".xlsx,.xlsm,.xls,.csv" className="hidden"
                 onChange={(e) => setFiles([...e.target.files])} />
          <div className="text-slate-300 font-medium">
            {files.length ? `${files.length} file(s) selected` : 'Drop Excel files or click to browse'}
          </div>
          <div className="text-xs text-slate-600 mt-1">.xlsx · .xlsm · .xls · .csv — multiple sheets, merged cells, messy headers all welcome</div>
          {files.length > 0 && (
            <div className="mt-3 flex flex-wrap gap-2 justify-center">
              {files.map((f) => <Badge key={f.name} tone="accent">{f.name}</Badge>)}
            </div>
          )}
        </label>
        <button className="btn" disabled={busy || !name.trim() || !files.length} onClick={launch}>
          {busy ? (uploadPct != null && uploadPct < 100 ? `Uploading ${uploadPct}%…` : 'Starting…') : 'Upload & Analyze'}
        </button>
        {uploadPct != null && (
          <div>
            <div className="flex justify-between text-xs text-slate-500 mb-1">
              <span>{uploadPct < 100 ? `Uploading ${files.length} file(s)` : 'Upload complete — starting analysis'}</span>
              <span>{uploadPct}%</span>
            </div>
            <div className="h-1.5 rounded bg-surface-border overflow-hidden">
              <div className="h-full rounded bg-accent transition-all" style={{ width: `${uploadPct}%` }} />
            </div>
          </div>
        )}
        {error && <div className="text-sm text-rose-400">{error}</div>}
      </div>

      {active && (
        <div className="card-pad mt-6">
          <div className="flex items-center justify-between mb-4">
            <div className="h-title">Automatic understanding pipeline</div>
            <Badge tone={active.status === 'failed' ? 'danger' : active.status === 'awaiting_clarification' ? 'warn' : 'accent'}>
              {resuming && active.status === 'analyzing' ? 'resuming analysis' : active.status}
            </Badge>
          </div>
          <div className="grid grid-cols-2 md:grid-cols-3 gap-2">
            {(active.stages || []).map((s) => (
              <div key={s.stage} className="flex items-center gap-2 text-sm py-1">
                <span className={
                  s.status === 'completed' ? 'text-emerald-400' :
                  s.status === 'running' ? 'text-accent animate-pulse' :
                  s.status === 'failed' ? 'text-rose-400' : 'text-slate-600'
                }>
                  {s.status === 'completed' ? '●' : s.status === 'running' ? '◐' : s.status === 'failed' ? '✕' : '○'}
                </span>
                <span className={s.status === 'pending' ? 'text-slate-600' : 'text-slate-300'}>
                  {STAGE_LABELS[s.stage] || s.stage}
                </span>
              </div>
            ))}
          </div>
        </div>
      )}

      {active && active.status === 'awaiting_clarification' && clarify && (
        <div className="card-pad mt-6 border border-amber-500/30">
          <div className="flex items-center justify-between mb-2">
            <div className="h-title">I need your help to understand this data</div>
            <Badge tone="warn">confidence {Math.round((clarify.confidence || 0) * 100)}%</Badge>
          </div>
          <p className="text-sm text-slate-400 mb-4">{clarify.explanation}</p>

          {clarify.categories && (
            <div className="grid grid-cols-2 md:grid-cols-4 gap-2 mb-5">
              {Object.entries(clarify.categories).map(([k, v]) => (
                <div key={k} className="text-xs">
                  <div className="flex justify-between text-slate-500 mb-1">
                    <span>{CATEGORY_LABELS[k] || k}</span><span>{Math.round(v * 100)}%</span>
                  </div>
                  <div className="h-1.5 rounded bg-surface-border overflow-hidden">
                    <div className={`h-full rounded ${v >= 0.55 ? 'bg-emerald-500' : 'bg-amber-500'}`}
                         style={{ width: `${Math.round(v * 100)}%` }} />
                  </div>
                </div>
              ))}
            </div>
          )}

          <div className="space-y-5">
            {(clarify.questions || []).filter((q) => !q.answered).map((q) => (
              <div key={q.id}>
                <div className="text-sm text-slate-200 mb-2">{q.question}</div>
                {(q.options || []).length > 0 && (
                  <div className="flex flex-wrap gap-2 mb-2">
                    {q.options.map((o) => (
                      <button key={o.value} type="button" title={o.detail}
                              onClick={() => setAnswers((a) => ({ ...a, [q.id]: o.value }))}
                              className={`px-3 py-1.5 rounded-lg border text-xs transition-colors ${
                                answers[q.id] === o.value
                                  ? 'border-accent bg-accent/15 text-accent'
                                  : 'border-surface-border text-slate-300 hover:border-accent/50'}`}>
                        <span className="font-medium">{o.value}</span>
                        {o.detail && <span className="text-slate-500 ml-1.5">{o.detail}</span>}
                      </button>
                    ))}
                  </div>
                )}
                <input className="input text-sm" placeholder="Or type your answer…"
                       value={(q.options || []).some((o) => o.value === answers[q.id]) ? '' : (answers[q.id] || '')}
                       onChange={(e) => setAnswers((a) => ({ ...a, [q.id]: e.target.value }))} />
              </div>
            ))}
          </div>

          <button className="btn mt-5" onClick={submitAnswers}
                  disabled={!Object.values(answers).some((v) => v && v.trim())}>
            Submit answers & resume analysis
          </button>
          <div className="text-xs text-slate-600 mt-2">
            Answers are stored in enterprise knowledge — equivalent datasets will never ask again.
          </div>
        </div>
      )}

      <div className="mt-10">
        <div className="h-sub mb-3">Recent projects</div>
        {!projects ? <Spinner /> : projects.length === 0 ? (
          <div className="text-sm text-slate-600">No projects yet.</div>
        ) : (
          <div className="grid md:grid-cols-2 gap-3">
            {projects.map((p) => {
              const duration = analysisDuration(p)
              return (
                <div key={p.project_id} role="button" tabIndex={0} onClick={() => openProject(p)}
                     onKeyDown={(e) => e.key === 'Enter' && openProject(p)}
                     className="card-pad text-left hover:border-accent/50 transition-colors cursor-pointer">
                  <div className="flex items-center justify-between gap-2">
                    <div className="font-medium text-slate-200 truncate">{p.name}</div>
                    <div className="flex items-center gap-2 shrink-0">
                      {p.report_confidence != null && (
                        <Badge tone={confTone(p.report_confidence)}>
                          confidence {Math.round(p.report_confidence * 100)}%
                        </Badge>
                      )}
                      <Badge tone={p.status === 'ready' ? 'success' : p.status === 'failed' ? 'danger' : 'warn'}>
                        {p.status === 'awaiting_clarification' ? 'needs your input' : p.status}
                      </Badge>
                      <button title="Delete project"
                              onClick={(e) => { e.stopPropagation(); setConfirmDelete(p.project_id) }}
                              className="w-6 h-6 rounded flex items-center justify-center text-slate-600 hover:text-rose-400 hover:bg-rose-500/10 transition-colors">
                        ✕
                      </button>
                    </div>
                  </div>
                  <div className="text-xs text-slate-600 mt-1">
                    {p.files?.length || 0} file(s) · {new Date(p.created_at).toLocaleString()}
                    {duration && <> · analysis {duration}</>}
                  </div>
                  {p.report_generated_at && (
                    <div className="text-xs text-slate-600 mt-0.5">
                      report v{p.report_version || 1} · {new Date(p.report_generated_at).toLocaleString()}
                    </div>
                  )}
                  {confirmDelete === p.project_id && (
                    <div className="mt-3 p-3 rounded-lg border border-rose-500/30 bg-rose-500/5"
                         onClick={(e) => e.stopPropagation()}>
                      <div className="text-sm text-slate-300">
                        Delete <span className="font-medium">{p.name}</span> and all its data
                        (uploads, datasets, analytics, reports, embeddings, knowledge graph)?
                        This cannot be undone.
                      </div>
                      <div className="flex gap-2 mt-2">
                        <button className="px-3 py-1.5 rounded-lg bg-rose-500/20 text-rose-300 text-xs font-medium hover:bg-rose-500/30 transition-colors"
                                disabled={deleting === p.project_id}
                                onClick={() => removeProject(p.project_id)}>
                          {deleting === p.project_id ? 'Deleting…' : 'Delete permanently'}
                        </button>
                        <button className="px-3 py-1.5 rounded-lg border border-surface-border text-slate-400 text-xs hover:border-accent/50 transition-colors"
                                onClick={() => setConfirmDelete(null)}>
                          Cancel
                        </button>
                      </div>
                    </div>
                  )}
                </div>
              )
            })}
          </div>
        )}
      </div>
    </div>
  )
}
