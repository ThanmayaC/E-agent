// One business's executive report, rendered for reading and export.
import { Link, useParams } from 'react-router-dom'
import { api } from '../api/client'
import { AsyncSection, PageHeader, useAsync } from '../components/ui'
import MarkdownLite from '../components/MarkdownLite'

export default function ReportView() {
  const { projectId } = useParams()
  const state = useAsync(() => api.reportMarkdown(projectId), [projectId])

  function download(md) {
    const blob = new Blob([md], { type: 'text/markdown' })
    const a = document.createElement('a')
    a.href = URL.createObjectURL(blob)
    a.download = `executive-report-${projectId}.md`
    a.click()
    URL.revokeObjectURL(a.href)
  }

  return (
    <>
      <div className="text-xs text-slate-500 mb-3">
        <Link to="/reports" className="hover:text-accent">Reports</Link> <span className="mx-1">/</span> Executive report
      </div>
      <AsyncSection state={state} empty="This report is not ready yet — it appears once the analysis completes.">
        {(d) => (
          <>
            <PageHeader title="Executive Report"
                        subtitle="Summary → KPIs → Insights → Root cause → Risks → Forecasts → Recommendations">
              <button className="btn" onClick={() => download(d.markdown)}>Export .md</button>
            </PageHeader>
            <div className="card-pad max-w-5xl">
              <MarkdownLite text={d.markdown} />
            </div>
          </>
        )}
      </AsyncSection>
    </>
  )
}
