// Minimal dependency-free markdown renderer (headings, tables, bold, lists)
export default function MarkdownLite({ text }) {
  const blocks = []
  const lines = (text || '').split('\n')
  let table = null
  const flush = () => { if (table) { blocks.push({ type: 'table', rows: table }); table = null } }

  for (const line of lines) {
    if (line.trim().startsWith('|')) {
      const cells = line.split('|').slice(1, -1).map((c) => c.trim())
      if (cells.every((c) => /^[-\s:]*$/.test(c))) continue
      table = table || []
      table.push(cells)
      continue
    }
    flush()
    blocks.push({ type: 'line', text: line })
  }
  flush()

  const inline = (s) =>
    s.split(/(\*\*[^*]+\*\*|`[^`]+`|_[^_]+_)/g).map((part, i) => {
      if (part.startsWith('**')) return <strong key={i} className="text-slate-100">{part.slice(2, -2)}</strong>
      if (part.startsWith('`')) return <code key={i} className="font-mono text-xs bg-surface px-1 rounded text-sky-300">{part.slice(1, -1)}</code>
      if (part.startsWith('_') && part.endsWith('_') && part.length > 2) return <em key={i} className="text-slate-500">{part.slice(1, -1)}</em>
      return part
    })

  return (
    <div className="space-y-1 text-sm text-slate-300">
      {blocks.map((b, i) => {
        if (b.type === 'table') {
          const [head, ...rows] = b.rows
          return (
            <div key={i} className="overflow-auto my-3 card">
              <table className="table-base">
                <thead><tr>{head.map((c, j) => <th key={j}>{c}</th>)}</tr></thead>
                <tbody>{rows.map((r, j) => <tr key={j}>{r.map((c, k) => <td key={k}>{inline(c)}</td>)}</tr>)}</tbody>
              </table>
            </div>
          )
        }
        const t = b.text
        if (t.startsWith('# ')) return <h1 key={i} className="text-2xl font-bold text-slate-100 pt-2">{inline(t.slice(2))}</h1>
        if (t.startsWith('## ')) return <h2 key={i} className="text-lg font-semibold text-slate-100 pt-5 border-t border-surface-border mt-4">{inline(t.slice(3))}</h2>
        if (t.startsWith('### ')) return <h3 key={i} className="text-sm font-semibold text-accent pt-3">{inline(t.slice(4))}</h3>
        if (t.startsWith('- ')) return <div key={i} className="pl-4 text-slate-400">• {inline(t.slice(2))}</div>
        if (!t.trim()) return <div key={i} className="h-1" />
        return <p key={i} className="text-slate-400">{inline(t)}</p>
      })}
    </div>
  )
}
