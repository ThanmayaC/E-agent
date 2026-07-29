// Documents — the V2 Document Intelligence pipeline: what has been
// ingested, parsed, chunked, and versioned, and which formats this
// deployment can parse.
import { useState } from 'react'
import { api } from '../../api/client'
import {
  AsyncSection, Badge, PageHeader, Panel, PanelEmpty, Spinner, Stat, Tabs,
  useAsync, when,
} from '../../components/ui'

const CATEGORIES = [
  ['', 'All'], ['sop', 'SOPs'], ['rca', 'RCAs'], ['policy', 'Policies'],
  ['meeting', 'Meetings'], ['product_document', 'Product docs'],
  ['document', 'Other'],
]

export default function AdminDocuments() {
  const [category, setCategory] = useState('')
  const state = useAsync(async () => {
    const [status, list, rag] = await Promise.all([
      api.documentsStatus().catch(() => null),
      api.documentsList(category).catch(() => null),
      api.ragDiagnostics().catch(() => null),
    ])
    return { status, list, rag }
  }, [category])

  return (
    <>
      <PageHeader title="Documents & Enterprise RAG"
                  subtitle="Document Intelligence: detection, parsing, OCR, chunking, embeddings, retrieval" />
      <AsyncSection state={state}
                    empty="Document Intelligence is disabled in this deployment.">
        {({ status, list, rag }) => {
          const documents = list?.documents || []
          return (
            <div className="space-y-5">
              <div className="grid gap-4 md:grid-cols-4">
                <Stat label="Documents" value={status?.documents ?? 0} />
                <Stat label="Parsed" value={status?.parsed ?? 0} />
                <Stat label="Chunks embedded" value={status?.chunks ?? 0} />
                <Stat label="Versions tracked" value={status?.versions ?? 0} />
              </div>

              <RagPanel rag={rag} />

              <Panel title="Parser availability">
                <div className="grid gap-2 sm:grid-cols-2 lg:grid-cols-4 text-sm">
                  {(status?.formats || []).map((f) => (
                    <div key={f.format} className="flex items-center justify-between gap-2">
                      <span className="text-slate-300 uppercase text-xs font-mono">{f.format}</span>
                      <Badge tone={f.available ? 'success' : 'default'}>
                        {f.available ? 'available' : 'not installed'}
                      </Badge>
                    </div>
                  ))}
                </div>
                {(status?.formats || []).some((f) => !f.available) && (
                  <div className="text-xs text-slate-600 mt-3">
                    {(status.formats || []).filter((f) => !f.available && f.requires)
                      .map((f) => `${f.format}: ${f.requires}`).join(' · ')}
                  </div>
                )}
              </Panel>

              <Tabs active={category} onChange={setCategory}
                    tabs={CATEGORIES.map(([value, label]) => ({
                      value, label,
                      count: value === '' ? (status?.documents ?? 0)
                        : (status?.by_category?.[value] ?? 0),
                    }))} />

              <Panel title="Ingested documents">
                {documents.length === 0 ? <PanelEmpty text="No documents in this view — register a document source under Sync." /> : (
                  <div className="overflow-x-auto">
                    <table className="table-base">
                      <thead>
                        <tr><th>Document</th><th>Category</th><th>Source</th>
                            <th>Version</th><th>Parsed</th><th>Chunks</th><th>Updated</th></tr>
                      </thead>
                      <tbody>
                        {documents.map((d) => (
                          <tr key={d.document_id}>
                            <td className="text-slate-200">{d.name}</td>
                            <td><Badge tone="accent">{d.category.replace(/_/g, ' ')}</Badge></td>
                            <td className="text-xs">{d.source}</td>
                            <td className="tabular-nums">v{d.version}</td>
                            <td>
                              <Badge tone={d.parsed ? 'success' : 'warn'}>
                                {d.parsed ? (d.ocr_used ? 'ocr' : d.parser || 'yes') : 'no'}
                              </Badge>
                            </td>
                            <td className="tabular-nums">{d.chunks}</td>
                            <td className="text-xs">{when(d.updated_at)}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                )}
              </Panel>
            </div>
          )
        }}
      </AsyncSection>
    </>
  )
}

// Enterprise RAG diagnostics. Every figure is read live from the retrieval
// layer — vector count from the vector store itself, timing from recorded
// retrievals — and the panel states plainly when retrieval is not usable
// rather than showing a reassuring zero.
function RagPanel({ rag }) {
  if (!rag) {
    return (
      <Panel title="Enterprise RAG">
        <PanelEmpty text="Retrieval diagnostics are unavailable — the documents API did not respond." />
      </Panel>
    )
  }

  const r = rag.retrieval || {}
  const timing = rag.timing || {}
  const vectors = r.vectors ?? 0
  const indexed = rag.documents_indexed ?? 0
  const usable = vectors > 0 && r.embedder_available && r.vector_store_available

  return (
    <Panel title="Enterprise RAG">
      {!usable && (
        <div className="text-sm fg-warn mb-4">
          {r.reason
            || (indexed === 0
              ? 'No documents are indexed, so retrieval has nothing to search. Register a document source and synchronize it.'
              : 'Documents are indexed but no vectors exist — run a synchronization to embed them.')}
        </div>
      )}

      <div className="grid gap-4 md:grid-cols-4">
        <Stat label="Documents indexed" value={indexed} />
        <Stat label="Chunks embedded" value={rag.chunks_embedded ?? 0} />
        <Stat label="Vectors stored" value={vectors}
              tone={vectors > 0 ? 'fg-primary' : 'fg-warn'}
              hint={r.dimensions ? `${r.dimensions} dimensions · ${r.backend} store` : r.backend} />
        <Stat label="Avg retrieval"
              value={timing.avg_ms != null ? `${timing.avg_ms} ms` : '—'}
              hint={timing.samples
                ? `${timing.samples} search(es) · p95 ${timing.p95_ms} ms`
                : 'no retrieval has run since startup'} />
      </div>

      <div className="mt-4 flex items-center gap-2 flex-wrap">
        <span className="text-xs fg-muted">Embedding model</span>
        <Badge tone={r.semantic ? 'success' : 'warn'}>{r.embedding_model}</Badge>
        <span className="text-xs fg-muted">
          {r.semantic
            ? 'sentence-transformers model — retrieval is semantic.'
            : 'Built-in feature-hash embedding, not a trained semantic model: retrieval matches shared terms and n-grams, not meaning. Set EDIP_EMBEDDING_MODEL to a sentence-transformers model for semantic retrieval.'}
        </span>
      </div>

      <RetrievalTest disabled={!usable} />
    </Panel>
  )
}

// A live query against the same retrieval path the copilot uses. This is the
// only honest way to answer "is RAG working" — run it and show what came back.
function RetrievalTest({ disabled }) {
  const [q, setQ] = useState('')
  const [result, setResult] = useState(null)
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState('')

  const run = async (event) => {
    event.preventDefault()
    if (!q.trim()) return
    setBusy(true); setError(''); setResult(null)
    try {
      setResult(await api.documentsSearch(q, 5))
    } catch (e) {
      setError(String(e.message || e))
    } finally {
      setBusy(false)
    }
  }

  return (
    <div className="mt-5 pt-4 border-t border-surface-border">
      <div className="h-sub mb-2">Test retrieval</div>
      <form className="flex gap-2" onSubmit={run}>
        <input className="input flex-1" value={q} disabled={disabled}
               placeholder="e.g. Why did UPI Autopay success dip?"
               onChange={(e) => setQ(e.target.value)} />
        <button className="btn" type="submit" disabled={busy || disabled || !q.trim()}>
          {busy ? 'Retrieving…' : 'Retrieve'}
        </button>
      </form>

      {disabled && (
        <div className="text-xs fg-muted mt-2">
          Retrieval is unavailable until documents are indexed and embedded.
        </div>
      )}
      {error && <div className="text-sm fg-danger mt-3">{error}</div>}
      {busy && <Spinner label="Running retrieval…" />}

      {result && (
        <div className="mt-4">
          <div className="text-xs fg-muted mb-2">
            {result.count} chunk(s) retrieved in {result.took_ms} ms
          </div>
          {result.count === 0 ? (
            <PanelEmpty text="Nothing matched — retrieval ran but found no relevant chunk." />
          ) : (
            <ul className="space-y-3">
              {result.results.map((hit, i) => (
                <li key={i} className="card-pad">
                  <div className="flex items-center justify-between gap-2 mb-1.5">
                    <span className="text-sm fg-primary truncate">
                      {hit.document || hit.title || hit.id}
                    </span>
                    <span className="flex items-center gap-2 shrink-0">
                      {hit.category && <Badge tone="accent">{String(hit.category).replace(/_/g, ' ')}</Badge>}
                      <Badge tone={hit.score >= 0.5 ? 'success' : hit.score >= 0.25 ? 'warn' : 'default'}>
                        {Number(hit.score ?? 0).toFixed(3)}
                      </Badge>
                    </span>
                  </div>
                  <p className="text-xs fg-muted line-clamp-3">
                    {(hit.text || '').slice(0, 400) || '(no text on this chunk)'}
                  </p>
                </li>
              ))}
            </ul>
          )}
        </div>
      )}
    </div>
  )
}
