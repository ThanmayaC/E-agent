// A sortable/filterable breakdown table for one dimension (bank, PSP,
// merchant, MCC, segment...) of real transaction rows — shared by the Product
// Intelligence Dashboards, the Ecosystem node drawer, and the MCC Explorer so
// every "top N" table in the platform behaves and reads identically.
import { fmt } from '../api/client'
import { Panel, PanelEmpty } from './ui'
import { CompareTable, DrillHint, FilterInput, useDrilldown } from './drilldown'

const inr = (v) => `₹${fmt.num(v)}`

export default function DimensionTable({ title, rows, nameLabel = 'Name', action }) {
  const d = useDrilldown(rows, { key: 'name' })
  if (!rows?.length) {
    return <Panel title={title} action={action}><PanelEmpty text="Not applicable for this slice." /></Panel>
  }
  return (
    <Panel title={title}
           action={action || <FilterInput value={d.filter} onChange={d.setFilter} placeholder="Filter…" />}>
      <DrillHint />
      <CompareTable rows={d.rows} idKey="name" filter={d.filter} selected={d.selected}
                    onRowClick={d.setSelected} defaultSort="attempts"
                    cols={[
                      { key: 'name', label: nameLabel },
                      { key: 'attempts', label: 'Attempts', right: true, render: (r) => fmt.num(r.attempts) },
                      { key: 'success_rate', label: 'Success %', right: true },
                      { key: 'value_inr', label: 'Value', right: true, render: (r) => inr(r.value_inr) },
                      { key: 'share_pct', label: 'Share %', right: true },
                    ]} />
    </Panel>
  )
}
