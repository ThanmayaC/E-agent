// Model status — the configured LLM provider and how the conversational
// layer is behaving.
import { api } from '../../api/client'
import {
  AsyncSection, Badge, PageHeader, Panel, PanelEmpty, Stat, useAsync,
} from '../../components/ui'

export default function AdminModels() {
  const state = useAsync(async () => {
    const [workspace, intents] = await Promise.all([
      api.copilotWorkspace().catch(() => null),
      api.copilotIntents().catch(() => null),
    ])
    return { workspace, intents }
  }, [])

  return (
    <>
      <PageHeader title="Model status" subtitle="LLM provider, model, and the copilot's understanding routes" />
      <AsyncSection state={state} empty="The conversational layer is disabled.">
        {({ workspace, intents }) => {
          const provider = workspace?.provider || workspace?.llm || {}
          const stats = workspace?.stats || workspace?.conversations_stats || {}
          return (
            <div className="space-y-5">
              <div className="grid gap-4 md:grid-cols-4">
                <Stat label="Provider" value={provider.provider || provider.name || 'not configured'}
                      tone={provider.provider ? 'text-emerald-400' : 'text-slate-400'} />
                <Stat label="Model" value={provider.model || '—'} />
                <Stat label="Conversations" value={stats.total ?? stats.conversations ?? '—'} />
                <Stat label="Copilot" value={workspace ? 'enabled' : 'disabled'}
                      tone={workspace ? 'text-emerald-400' : 'text-rose-400'} />
              </div>

              <Panel title="Understanding routes">
                {(intents?.intents || []).length === 0 ? (
                  <PanelEmpty text="Intent vocabulary unavailable." />
                ) : (
                  <div className="flex flex-wrap gap-2">
                    {intents.intents.map((it, i) => (
                      <Badge key={i}>{typeof it === 'string' ? it : it.intent || it.name}</Badge>
                    ))}
                  </div>
                )}
              </Panel>

              <Panel title="Configuration">
                <p className="text-sm text-slate-400">
                  The provider, embedding model, and vector backend are configured per environment through{' '}
                  <span className="font-mono text-xs text-slate-300">EDIP_*</span> variables — see{' '}
                  <span className="font-mono text-xs text-slate-300">docs/INSTALLATION.md</span>. Restart the backend after changing them.
                </p>
              </Panel>
            </div>
          )
        }}
      </AsyncSection>
    </>
  )
}
