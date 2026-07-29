// Files (V9.0) — universal file upload with automatic AI understanding, and
// AI artifact generation. Drag & drop (or pick) any Excel/CSV/PDF/Word/PPT/
// image/ZIP/JSON/XML/TXT; each is understood instantly (type, text, tables,
// entities, dates, KPIs, summary, tags, recommendations, KG links).
import { useEffect, useRef, useState } from 'react'
import { useLocation } from 'react-router-dom'
import { api, fmt } from '../api/client'
import { Badge, PageHeader, Panel, Spinner } from '../components/ui'

const ARTIFACT_KINDS = [
  ['executive_report', 'Executive Report (Word)'],
  ['excel', 'Excel Workbook'],
  ['word', 'Word Document'],
  ['pdf', 'PDF / Printable'],
  ['powerpoint', 'Presentation'],
  ['rca', 'RCA'],
  ['meeting_minutes', 'Meeting Minutes'],
  ['action_items', 'Action Items'],
  ['roadmap', 'Roadmap'],
  ['business_case', 'Business Case'],
  ['email', 'Email Draft'],
]

function Understanding({ d }) {
  if (!d) return null
  const chips = (label, items, tone = 'default') =>
    items?.length ? (
      <div className="flex items-start gap-2 flex-wrap">
        <span className="text-xs text-slate-500 w-20 shrink-0 pt-0.5">{label}</span>
        <div className="flex flex-wrap gap-1">
          {items.map((x, i) => <Badge key={i} tone={tone}>{typeof x === 'object' ? (x.kpi || x.name) : x}</Badge>)}
        </div>
      </div>
    ) : null
  const ents = Object.entries(d.entities || {}).flatMap(([, v]) => v)
  return (
    <div className="space-y-2.5 text-sm">
      <p className="text-slate-300">{d.summary}</p>
      <div className="grid gap-1.5">
        {chips('Type', [d.type], 'info')}
        {chips('Entities', ents, 'accent')}
        {chips('KPIs', (d.kpis || []).map((k) => k.kpi), 'warn')}
        {chips('Dates', (d.dates || []).slice(0, 8))}
        {chips('Tags', d.tags)}
      </div>
      {d.tables?.length > 0 && (
        <div className="text-xs text-slate-500">{d.tables.length} table(s) · {d.metadata?.words} words · {d.metadata?.chunks_for_embedding} chunks</div>
      )}
      {d.recommendations?.length > 0 && (
        <div className="pt-2 border-t border-surface-border">
          <div className="text-xs text-slate-500 mb-1">AI recommendations</div>
          <ul className="text-xs text-slate-400 space-y-1">
            {d.recommendations.map((r, i) => <li key={i}>→ {r}</li>)}
          </ul>
        </div>
      )}
    </div>
  )
}

export default function Files() {
  const location = useLocation()
  const [files, setFiles] = useState([])
  const [open, setOpen] = useState(null)
  const [detail, setDetail] = useState(null)
  const [busy, setBusy] = useState(false)
  const [drag, setDrag] = useState(false)
  const [artifacts, setArtifacts] = useState([])
  const [gen, setGen] = useState({ kind: 'executive_report', title: '', prompt: '' })
  const [genBusy, setGenBusy] = useState(false)
  const inputRef = useRef(null)

  const refresh = () => {
    api.workspaceFiles().then((d) => setFiles(d.files || [])).catch(() => {})
    api.workspaceArtifacts().then((d) => setArtifacts(d.artifacts || [])).catch(() => {})
  }
  useEffect(() => { refresh() }, [])
  useEffect(() => { if (location.state?.open) openFile(location.state.open) }, []) // eslint-disable-line

  async function upload(fileList) {
    if (!fileList?.length) return
    setBusy(true)
    try {
      const res = await api.workspaceUpload(fileList)
      refresh()
      if (res.understood?.length) openDetail(res.understood[0])
    } catch (e) { alert(`Upload failed: ${e.message}`) } finally { setBusy(false) }
  }

  const openDetail = (d) => { setOpen(d.id); setDetail(d) }
  async function openFile(id) {
    setOpen(id); setDetail(null)
    try { setDetail(await api.workspaceFile(id)) } catch { /* ignore */ }
  }
  const del = async (id, e) => {
    e.stopPropagation()
    await api.deleteWorkspaceFile(id); if (open === id) { setOpen(null); setDetail(null) }; refresh()
  }

  async function generate() {
    setGenBusy(true)
    try {
      const res = await api.generateArtifact(gen)
      refresh()
      window.open(api.artifactUrl(res.file), '_blank')
    } catch (e) { alert(`Generation failed: ${e.message}`) } finally { setGenBusy(false) }
  }

  return (
    <>
      <PageHeader title="Files & Artifacts"
        subtitle="Drop any file for instant AI understanding — or generate a report, deck, spreadsheet or RCA from enterprise data" />

      <div className="grid gap-4 lg:grid-cols-3">
        <div className="lg:col-span-2 space-y-4">
          {/* Dropzone */}
          <div
            onDragOver={(e) => { e.preventDefault(); setDrag(true) }}
            onDragLeave={() => setDrag(false)}
            onDrop={(e) => { e.preventDefault(); setDrag(false); upload(e.dataTransfer.files) }}
            onClick={() => inputRef.current?.click()}
            className={`card border-2 border-dashed rounded-xl p-8 text-center cursor-pointer transition ${drag ? 'border-accent bg-accent/5' : 'border-surface-border hover:border-accent/50'}`}>
            <input ref={inputRef} type="file" multiple hidden
              onChange={(e) => upload(e.target.files)} />
            <div className="text-3xl mb-2">📎</div>
            <div className="text-slate-200 font-medium">Drag & drop files here, or click to browse</div>
            <div className="text-xs text-slate-500 mt-1.5">
              Excel · CSV · PDF · Word · PowerPoint · Images · ZIP · JSON · XML · TXT — multiple files supported
            </div>
            {busy && <div className="mt-3"><Spinner label="Understanding your files…" /></div>}
          </div>

          {/* File list + detail */}
          <Panel title={`Your files (${files.length})`}>
            {files.length === 0 ? <p className="text-xs text-slate-600 py-2">No files yet.</p> : (
              <div className="space-y-1.5">
                {files.map((f) => (
                  <div key={f.id}>
                    <div onClick={() => (open === f.id ? setOpen(null) : openFile(f.id))}
                      className="flex items-center gap-2 px-2 py-2 rounded-lg hover:bg-surface-overlay/50 cursor-pointer">
                      <Badge tone="info">{f.type}</Badge>
                      <span className="flex-1 truncate text-sm text-slate-200">{f.file}</span>
                      <span className="text-xs text-slate-600 tabular-nums">{fmt.num(f.size_bytes)} B</span>
                      <button onClick={(e) => del(f.id, e)} className="text-xs text-slate-600 hover:text-rose-400">✕</button>
                    </div>
                    {open === f.id && (
                      <div className="ml-2 pl-4 border-l border-surface-border py-2">
                        {detail ? <Understanding d={detail} /> : <Spinner label="Loading…" />}
                      </div>
                    )}
                  </div>
                ))}
              </div>
            )}
          </Panel>
        </div>

        {/* Artifact generator */}
        <div className="space-y-4">
          <Panel title="Generate an artifact">
            <div className="space-y-2.5">
              <select value={gen.kind} onChange={(e) => setGen({ ...gen, kind: e.target.value })}
                className="input w-full !py-2 text-sm">
                {ARTIFACT_KINDS.map(([v, l]) => <option key={v} value={v}>{l}</option>)}
              </select>
              <input value={gen.title} onChange={(e) => setGen({ ...gen, title: e.target.value })}
                placeholder="Title (optional)" className="input w-full !py-2 text-sm" />
              <textarea value={gen.prompt} onChange={(e) => setGen({ ...gen, prompt: e.target.value })}
                placeholder="What should it cover? (optional)" rows={3}
                className="input w-full !py-2 text-sm resize-none" />
              <button onClick={generate} disabled={genBusy} className="btn w-full justify-center">
                {genBusy ? 'Generating…' : 'Generate & download'}
              </button>
              <p className="text-[11px] text-slate-600">
                Composed from live executive, evolution & ecosystem data when no content is supplied.
              </p>
            </div>
          </Panel>

          <Panel title={`Generated (${artifacts.length})`}>
            {artifacts.length === 0 ? <p className="text-xs text-slate-600 py-2">Nothing generated yet.</p> : (
              <ul className="space-y-1">
                {artifacts.map((a) => (
                  <li key={a.file}>
                    <a href={api.artifactUrl(a.file)} target="_blank" rel="noreferrer"
                      className="flex items-center gap-2 px-2 py-1.5 rounded hover:bg-surface-overlay/50 text-sm text-slate-300">
                      <span>⬇</span><span className="truncate flex-1">{a.file}</span>
                      <span className="text-xs text-slate-600">{fmt.num(a.bytes)} B</span>
                    </a>
                  </li>
                ))}
              </ul>
            )}
          </Panel>
        </div>
      </div>
    </>
  )
}
