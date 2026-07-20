// Documents — the V2 Document Intelligence pipeline: what has been
// ingested, parsed, chunked, and versioned, and which formats this
// deployment can parse.
import { useState } from 'react'
import { api } from '../../api/client'
import {
  AsyncSection, Badge, PageHeader, Panel, PanelEmpty, Stat, Tabs, useAsync,
  when,
} from '../../components/ui'

const CATEGORIES = [
  ['', 'All'], ['sop', 'SOPs'], ['rca', 'RCAs'], ['policy', 'Policies'],
  ['meeting', 'Meetings'], ['product_document', 'Product docs'],
  ['document', 'Other'],
]

export default function AdminDocuments() {
  const [category, setCategory] = useState('')
  const state = useAsync(async () => {
    const [status, list] = await Promise.all([
      api.documentsStatus().catch(() => null),
      api.documentsList(category).catch(() => null),
    ])
    return { status, list }
  }, [category])

  return (
    <>
      <PageHeader title="Documents"
                  subtitle="Document Intelligence: detection, parsing, OCR, chunking, embeddings, versions" />
      <AsyncSection state={state}
                    empty="Document Intelligence is disabled in this deployment.">
        {({ status, list }) => {
          const documents = list?.documents || []
          return (
            <div className="space-y-5">
              <div className="grid gap-4 md:grid-cols-4">
                <Stat label="Documents" value={status?.documents ?? 0} />
                <Stat label="Parsed" value={status?.parsed ?? 0} />
                <Stat label="Chunks embedded" value={status?.chunks ?? 0} />
                <Stat label="Versions tracked" value={status?.versions ?? 0} />
              </div>

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
