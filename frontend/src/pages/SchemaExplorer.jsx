import { useMemo, useState } from 'react'
import { useParams } from 'react-router-dom'
import {
  flexRender, getCoreRowModel, getFilteredRowModel, getSortedRowModel, useReactTable,
} from '@tanstack/react-table'
import { api } from '../api/client'
import { AsyncSection, Badge, PageHeader, useAsync } from '../components/ui'

const roleTone = { primary_key: 'accent', foreign_key: 'info', measure: 'success', time_dimension: 'warn', dimension: 'default' }

export default function SchemaExplorer() {
  const { projectId } = useParams()
  const state = useAsync(() => api.semantics(projectId), [projectId])
  const [filter, setFilter] = useState('')

  const columns = useMemo(() => [
    { header: 'Dataset', accessorKey: 'dataset_id',
      cell: (c) => <span className="font-mono text-xs text-slate-500">{c.getValue()}</span> },
    { header: 'Column', accessorKey: 'column',
      cell: (c) => <span className="text-slate-200">{c.getValue()}</span> },
    { header: 'Business Concept', accessorKey: 'concept',
      cell: (c) => <Badge tone={c.getValue() === 'Unknown' ? 'default' : 'accent'}>{c.getValue()}</Badge> },
    { header: 'Canonical', accessorKey: 'canonical_name' },
    { header: 'Type', accessorKey: 'semantic_type' },
    { header: 'Role', accessorKey: 'role',
      cell: (c) => <Badge tone={roleTone[c.getValue()] || 'default'}>{c.getValue().replace('_', ' ')}</Badge> },
    { header: 'Confidence', accessorKey: 'confidence',
      cell: (c) => `${Math.round(c.getValue() * 100)}%` },
  ], [])

  return (
    <>
      <PageHeader title="Schema Explorer"
                  subtitle="Every column mapped to a business concept — inferred, never configured">
        <input className="input max-w-xs" placeholder="Filter columns…" value={filter}
               onChange={(e) => setFilter(e.target.value)} />
      </PageHeader>
      <AsyncSection state={state}>
        {(rows) => <SchemaTable rows={rows} columns={columns} filter={filter} />}
      </AsyncSection>
    </>
  )
}

function SchemaTable({ rows, columns, filter }) {
  const table = useReactTable({
    data: rows, columns,
    state: { globalFilter: filter },
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
  })
  return (
    <div className="card overflow-auto max-h-[75vh]">
      <table className="table-base">
        <thead>
          {table.getHeaderGroups().map((hg) => (
            <tr key={hg.id}>
              {hg.headers.map((h) => (
                <th key={h.id} onClick={h.column.getToggleSortingHandler()} className="cursor-pointer select-none">
                  {flexRender(h.column.columnDef.header, h.getContext())}
                  {{ asc: ' ↑', desc: ' ↓' }[h.column.getIsSorted()] ?? ''}
                </th>
              ))}
            </tr>
          ))}
        </thead>
        <tbody>
          {table.getRowModel().rows.map((r) => (
            <tr key={r.id} className="hover:bg-surface-overlay/40">
              {r.getVisibleCells().map((c) => <td key={c.id}>{flexRender(c.column.columnDef.cell, c.getContext())}</td>)}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
