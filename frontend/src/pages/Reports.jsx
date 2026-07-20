import { useParams } from 'react-router-dom'
import { api } from '../api/client'
import { AsyncSection, PageHeader, useAsync } from '../components/ui'
import MarkdownLite from '../components/MarkdownLite'

export default function Reports() {
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
      <AsyncSection state={state}>
        {(d) => (
          <>
            <PageHeader title="Executive Report"
                        subtitle="Fixed structure, every time: Summary → KPIs → Insights → Root Cause → Risks → Forecasts → Recommendations">
              <button className="btn" onClick={() => download(d.markdown)}>Download .md</button>
            </PageHeader>
            <div className="card-pad prose-report max-w-5xl">
              <MarkdownLite text={d.markdown} />
            </div>
          </>
        )}
      </AsyncSection>
    </>
  )
}
