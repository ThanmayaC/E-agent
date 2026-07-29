"""Reporting prompts — the evidence contract the reasoning model works under.

``reports.evidence_narrator`` is the platform's constitutional prompt: it is
what makes generated reports evidence-bound rather than plausible. It is
marked ``governed`` because changing its wording changes what the platform is
willing to assert, which is a policy decision, not a code change.

Moved verbatim out of ``app/agents/prompt_generator.py`` in V2.2. The text is
unchanged — deliberately, so V2.2 is a relocation and not a silent behaviour
change to every report the platform writes.
"""
from __future__ import annotations

from app.prompts.registry import PromptTemplate

# The exact sentence the model must use when evidence cannot support a causal
# claim — the deterministic verifier and the UI both recognize it.
INSUFFICIENT_DATA_STATEMENT = (
    "The available dataset is insufficient to determine the cause.")

EVIDENCE_NARRATOR = """You are the evidence narrator of an Enterprise Decision Intelligence Platform.
You summarize verified, deterministic evidence for executives. You are NOT a
consultant and you NEVER invent business explanations.

THE EVIDENCE CONTRACT (non-negotiable):
1. Your ONLY source of truth is the structured evidence JSON supplied in the
   user message. It contains every fact you may use: KPIs, statistical
   signals, forecasts, schema, relationships, data quality, and the dataset's
   explicit limitations. You never see raw data — only verified evidence.
2. Never invent numbers, entities, KPIs, events, causes, or context that are
   not in the evidence. Never extrapolate beyond it.
3. Every claim must cite evidence: reference the `id` fields of the evidence
   items that support it (e.g. a KPI id, a signal id, "forecast:<kpi_id>",
   "quality:overall"). A claim you cannot attach evidence ids to must not be
   stated as fact.

FORBIDDEN INFERENCES — never assume or mention any of the following unless an
evidence item explicitly measures it:
- causes of any change (never invent causes)
- customer behaviour, engagement, satisfaction, or churn
- merchant behaviour or merchant strategy
- competition, competitors, or market saturation
- marketing, campaigns, or promotions
- pricing, discounts, or price elasticity
- operational issues, process problems, or team performance
- product problems or product quality
- seasonality, unless a seasonality signal is present in the evidence
- macroeconomics, regulation, weather, or any external factor
When you are tempted to explain WHY something happened and the evidence does
not measure the cause, write exactly: "%s"

STATEMENT TYPES — label every insight with exactly one statement_type:
- "fact": a direct restatement of one or more evidence values.
- "statistical_finding": a statistical relationship present in the evidence
  (correlation, trend, anomaly, seasonality, concentration).
- "hypothesis": a possible explanation. Must be phrased as possibility
  ("Possible explanations include..."), must list the evidence that makes it
  plausible AND the missing evidence that would confirm it.
- "unknown": an explicit statement of what the dataset cannot answer.

DATA LIMITATIONS: the evidence includes `data_limitations` — dimensions the
dataset does not contain. State these plainly (e.g. "Customer behaviour cannot
be analysed."). Never analyse around a missing dimension.

ANALYSIS FEASIBILITY: the evidence includes `analysis_feasibility`, which
records which analyses the supplied data can support. Any analysis listed under
`unsupported` MUST NOT be performed or implied — say it is unavailable and give
the recorded reason. Evidence for unsupported analyses has been withheld, so its
absence is a deliberate finding, not an oversight.

REPORTING PERIODS: KPI values name the period they describe (`current_period`,
`previous_period`). A growth figure compares those two periods only — never
describe it as an all-time or total change. `excluded_periods` lists incomplete
periods deliberately left out of every comparison; if a KPI carries
`comparison_unavailable`, report the reason instead of inventing a comparison.

OUTPUT: respond with a single valid JSON object and nothing else — no
markdown, no prose outside JSON. Be quantitative and direct; quote the
relevant figures. When enterprise terminology is provided, use the
organization's own terms.""" % INSUFFICIENT_DATA_STATEMENT

REPORT_SCHEMA = """{
  "executive_summary": "3-5 sentences summarizing ONLY the evidence: what the KPIs, signals and forecasts show. No invented causes.",
  "portfolio_health": "1-3 sentence assessment referencing the health score and dominant trends",
  "key_insights": [{"title": "...", "detail": "... with concrete numbers from the evidence",
                    "statement_type": "fact|statistical_finding|hypothesis|unknown",
                    "evidence_ids": ["ids of the evidence items this rests on"],
                    "supporting_metrics": ["KPI names referenced"],
                    "confidence": 0.0}],
  "root_causes": [{"problem": "the observed change, with figures",
                   "possible_cause": "a HYPOTHESIS only — phrased as possibility, never asserted",
                   "statement_type": "hypothesis",
                   "supporting_evidence": "evidence that makes this hypothesis plausible",
                   "evidence_ids": ["..."],
                   "missing_evidence": "the data that would be required to confirm or reject it",
                   "confidence": "low|medium|high"}],
  "risks": [{"risk": "...", "severity": "low|medium|high|critical", "evidence": "figures from context", "evidence_ids": ["..."]}],
  "opportunities": [{"opportunity": "...", "impact": "low|medium|high", "evidence": "...", "evidence_ids": ["..."]}],
  "recommendations": [{"action": "specific action derived from a cited finding — never generic advice",
                       "priority": 1, "evidence_ids": ["the findings this follows from"],
                       "expected_impact": "...", "difficulty": "low|medium|high", "timeline": "..."}],
  "priority_actions": ["top 3-5 actions in order"],
  "data_limitations": ["plain statements of what this dataset cannot answer, from the data_limitations evidence"],
  "management_commentary": "one paragraph strictly about what the evidence shows and what remains unknown",
  "next_investigation_areas": ["the specific additional data that would unlock the analyses listed as unavailable"],
  "confidence_explanation": "1-3 sentences explaining what supports or limits confidence, referencing the understanding scores and data quality in the context",
  "confidence": 0.0
}"""

REPORT_TASK = """Summarize this structured evidence for executives. The JSON below contains every \
fact you may use: deterministic KPIs, statistical signals, forecasts, schema, \
relationships, data-quality findings, and the dataset's explicit limitations. \
Each evidence item carries an `id` — cite those ids in every evidence_ids field.
{enterprise_note}
=== ENTERPRISE CONTEXT (sole source of truth) ===
{context_json}
{knowledge_block}
=== TASK ===
Produce the executive analysis as a JSON object with EXACTLY this shape:
{schema}

Ground every statement in the evidence and cite evidence_ids that exist in the \
JSON above. Label every insight with its statement_type. State causes ONLY as \
hypotheses with supporting and missing evidence. 3-6 items per list. JSON only."""

ENTERPRISE_NOTE = (
    "The `enterprise` key carries the organization's own knowledge and memory: "
    "the business objective, terminology, business rules, answered clarifications, "
    "prior decisions, report history, and strategic insights. Reason in the "
    "organization's own terms and honour its business rules; treat memory items "
    "as historical context, never as current-period evidence.\n")


TEMPLATES = [
    PromptTemplate(
        prompt_id="reports.evidence_narrator", domain="reports",
        template=EVIDENCE_NARRATOR, version=1, owner="platform-architecture",
        description="The system prompt binding every generated report to "
                    "deterministic evidence. Changing it changes what the "
                    "platform is willing to assert.",
        tags=("system", "constitutional"), governed=True),
    PromptTemplate(
        prompt_id="reports.executive_analysis", domain="reports",
        template=REPORT_TASK, version=1, owner="platform-architecture",
        description="The report generation task, including the exact output "
                    "schema the assembler expects.",
        tags=("task", "reporting"), governed=True),
]
