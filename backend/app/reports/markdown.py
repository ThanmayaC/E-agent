"""Render the executive report as Markdown.

Narrative sections are inserted verbatim from the AI reasoning output;
fact tables are rendered from deterministic analytics. No template narrative.
"""
from jinja2 import Template

_TEMPLATE = Template("""# Executive Report — {{ r.meta.project }}
_Generated {{ r.meta.generated_at }} · structure v{{ r.meta.structure_version }} · narrative: {{ r.meta.ai.provider or 'unavailable' }}{% if r.meta.ai.model %} ({{ r.meta.ai.model }}){% endif %}_

## 1. Executive Summary
**Overall Health Score: {{ r.executive_summary.overall_health_score }}/100** _(deterministic metric)_
{% set hb = r.executive_summary.health_score_breakdown %}{% if hb and hb.formula %}
_Formula: `{{ hb.formula }}`_
{% for c in hb.components %}- {{ c.component.replace('_',' ') }}: {{ c.value }} → **{{ '%+.2f' % c.contribution }}** _({{ c.detail }})_
{% endfor %}{% if hb.clamped %}
> ⚠ {{ hb.clamp_note }}
{% endif %}{% endif %}

{% if r.meta.ai.status == 'ok' %}{{ r.executive_summary.summary }}

**Portfolio health:** {{ r.executive_summary.portfolio_health }}

### Priority Actions
{% for a in r.executive_summary.priority_actions %}{{ loop.index }}. {{ a }}
{% endfor %}
{% else %}> AI narrative unavailable: {{ r.meta.ai.error }}
{% endif %}

## 2. Analysis Feasibility
_What the supplied data can actually support. Decided before any analysis ran;
anything marked unsupported was withheld from the reasoning model entirely._
{% set f = r.analysis_feasibility %}{% if f and f.checks %}
Datasets: {{ f.datasets }} · Reporting grain: {{ f.grain }} · Periods observed: {{ f.periods_observed }} · **Complete periods: {{ f.complete_periods }}**
{% if f.excluded_partial_periods %}
**Excluded incomplete periods** — present in the data, but not comparable:

| Period | Coverage | Rows | Why excluded |
|---|---|---|---|
{% for p in f.excluded_partial_periods %}| {{ p.period }} | {{ p.coverage_pct }}% | {{ p.rows }} | {{ p.reason }} |
{% endfor %}{% endif %}

| Analysis | Supported | Requires | Observed | Reason if unavailable |
|---|---|---|---|---|
{% for c in f.checks %}| {{ c.analysis.replace('_',' ') }} | {{ '✅' if c.supported else '❌' }}{% if c.qualified %} ⚠{% endif %} | {{ c.requirement }} | {{ c.observed }} | {{ c.reason or '—' }} |
{% endfor %}
{% else %}_Feasibility was not assessed for this report._
{% endif %}

## 3. Management Summary
Datasets: {{ r.management_summary.portfolio_overview.datasets }} · Rows: {{ '{:,}'.format(r.management_summary.portfolio_overview.total_rows) }} · KPIs: {{ r.management_summary.portfolio_overview.kpis_tracked }} · Entities: {{ r.management_summary.portfolio_overview.entities | join(', ') }}

| KPI | Current | Previous | Growth | Trend |
|---|---|---|---|---|
{% for k in r.management_summary.overall_kpis %}| {{ k.name }} | {{ k.current }} | {{ k.previous if k.previous is not none else '—' }} | {{ '%+.1f%%' % k.growth_pct if k.growth_pct is not none else '—' }} | {{ k.trend }} |
{% endfor %}

## 4. Dataset Summary
Quality score: **{{ r.dataset_summary.quality_score }}/100** · Semantic confidence: {{ r.dataset_summary.avg_semantic_confidence }} · Relationships: {{ r.dataset_summary.relationships }}

| Table | Rows | Columns | Entity | Kind | Grain |
|---|---|---|---|---|---|
{% for t in r.dataset_summary.tables %}| {{ t.name }} | {{ '{:,}'.format(t.rows) }} | {{ t.columns }} | {{ t.entity }} | {{ t.kind }} | {{ t.time_grain or '—' }} |
{% endfor %}
{% set ex = r.calculation_provenance.excluded_columns %}{% if ex %}
**Columns excluded from KPIs** — numeric, but not additive quantities:

| Column | Read as | Why it is not a KPI |
|---|---|---|
{% for c in ex %}| `{{ c.column }}` | {{ c.inferred_type }} | {{ c.reason }} |
{% endfor %}{% endif %}

## 5. KPI Analysis
_Every value names the period it describes. Comparisons are like-for-like:
only complete periods are used._

| KPI | Expression | Basis | Current | Period | vs Previous | Growth | Forecast next |
|---|---|---|---|---|---|---|---|
{% for k in r.kpi_analysis %}| {{ k.name }} | `{{ k.expression }}` | {{ k.calculation.source if k.calculation else '—' }} | {{ k.current }} | {{ k.current_period or 'all rows' }} | {{ k.previous if k.previous is not none else '—' }}{% if k.previous_period %} ({{ k.previous_period }}){% endif %} | {{ '%+.1f%%' % k.growth_pct if k.growth_pct is not none else '—' }} | {{ k.forecast.next if k.forecast else '—' }} |
{% endfor %}
{% for k in r.kpi_analysis %}{% if k.comparison_unavailable_reason %}
> **{{ k.name }}** — no period comparison: {{ k.comparison_unavailable_reason }}
{% endif %}{% endfor %}

## 6. Business Insights (AI)
{% for i in r.business_insights %}- {% if i.statement_type %}`{{ i.statement_type | upper }}` {% endif %}**{{ i.title }}**{% if i.detail %} — {{ i.detail }}{% endif %}{% if i.confidence %} _(confidence {{ '%.0f%%' % (i.confidence * 100) }})_{% endif %}{% if i.evidence_ids %}
  Evidence: {{ i.evidence_ids | join(', ') }}{% endif %}
{% else %}- AI narrative unavailable.
{% endfor %}

## 7. Root Cause Hypotheses (AI)
_Causes are never asserted — each entry is a labelled hypothesis with its supporting and missing evidence._
{% for x in r.root_cause_analysis %}- **Observed:** {{ x.problem }}{% if x.possible_cause or x.cause %}
  **Possible cause (hypothesis):** {{ x.possible_cause or x.cause }}{% endif %}{% if x.supporting_evidence or x.evidence %}
  **Supporting evidence:** {{ x.supporting_evidence or x.evidence }}{% endif %}{% if x.missing_evidence %}
  **Missing evidence:** {{ x.missing_evidence }}{% endif %}{% if x.confidence %}
  **Confidence:** {{ x.confidence }}{% endif %}
{% else %}- AI narrative unavailable.
{% endfor %}

## 8. Opportunity Analysis (AI)
{% for o in r.opportunity_analysis %}- {{ o.opportunity }}{% if o.impact %} _(impact: {{ o.impact }})_{% endif %}
{% else %}- AI narrative unavailable.
{% endfor %}

## 9. Risk Analysis (AI)
{% for x in r.risk_analysis %}- {{ x.risk }}{% if x.severity %} _(severity: {{ x.severity }})_{% endif %}
{% else %}- AI narrative unavailable.
{% endfor %}

## 10. Predictive Analytics
| KPI | Status | Next Period | Range | Confidence |
|---|---|---|---|---|
{% for f in r.predictive_analytics.next_month %}| {{ f.kpi }} | {{ 'forecast unavailable' if f.status == 'unavailable' else ('low confidence' if f.status == 'low_confidence' else 'ok') }} | {{ f.expected if f.expected is not none else '—' }} | {{ f.range or '—' }} | {{ '%.0f%%' % (f.confidence * 100) }} |
{% endfor %}

## 11. Recommendations (AI)
_Grounded in cited evidence — see `evidence_ids` in the report JSON._
{% if r.recommendations %}| P | Action | Impact | Difficulty | Timeline | Evidence |
|---|---|---|---|---|---|
{% for x in r.recommendations %}| {{ x.priority or '—' }} | {{ x.action }} | {{ x.expected_impact or '—' }} | {{ x.difficulty or '—' }} | {{ x.timeline or '—' }} | {{ x.evidence_ids | join(', ') if x.evidence_ids else '—' }} |
{% endfor %}{% else %}AI narrative unavailable.
{% endif %}

### Rule-derived recommendations (deterministic)
{% for x in r.deterministic_recommendations %}- **P{{ x.priority }}** {{ x.action }} _(trigger: {{ x.trigger }})_
{% else %}- No deterministic findings triggered a recommendation.
{% endfor %}

## 12. Management Commentary (AI)
{% if r.executive_summary.management_commentary %}{{ r.executive_summary.management_commentary }}{% else %}AI narrative unavailable.{% endif %}

## 13. Next Investigation Areas (AI)
{% for a in r.next_investigation_areas %}- {{ a }}
{% else %}- AI narrative unavailable.
{% endfor %}

## 14. Confidence
{% if r.report_confidence and r.report_confidence.overall is not none %}**Overall (deterministic): {{ '%.0f%%' % (r.report_confidence.overall * 100) }}** — formula: `{{ r.report_confidence.formula }}`
{% endif %}{% if r.confidence_explanation %}{{ r.confidence_explanation }}{% else %}AI narrative unavailable.{% endif %}

## 15. Data Limitations
{% set d = r.data_limitations.deterministic if r.data_limitations else none %}{% if d %}{% if d.available_dimension_detail %}**Analysable dimensions** — present in this data:

{% for a in d.available_dimension_detail %}- **{{ a.dimension }}** — from {{ a.backed_by | join(', ') if a.backed_by else 'detected columns' }}
{% endfor %}
{% endif %}**Not analysable:**

{% for m in d.missing_dimensions %}- {{ m.impact }}
{% endfor %}
Observed history: {{ d.observed_history_periods }} complete period(s).
{% else %}- Not assessed.
{% endif %}

## 16. Calculation & Provenance
_Every number above, traced to its formula and inputs._
{% set cp = r.calculation_provenance %}{% if cp and cp.kpis %}
| Metric | Formula | Source | Periods used | Rows | Excluded |
|---|---|---|---|---|---|
{% for k in cp.kpis %}| {{ k.name }} | `{{ k.expression }}` | {{ k.source }}{% if k.time_column %} over `{{ k.time_column }}`{% endif %} | {{ k.current_period }}{% if k.previous_period and k.previous_period != 'n/a' %} vs {{ k.previous_period }}{% endif %} ({{ k.complete_periods }} complete {{ k.period_grain }}) | {{ '{:,}'.format(k.contributing_rows) }} | {% if k.excluded_periods %}{% for e in k.excluded_periods %}{{ e.period }}{% if not loop.last %}, {% endif %}{% endfor %}{% else %}none{% endif %} |
{% endfor %}
**Growth formula:** `(current - previous) / abs(previous) * 100`, computed only
between two complete periods of the same grain.
{% if cp.health_score and cp.health_score.formula %}
**Health score:** `{{ cp.health_score.formula }}`
{% endif %}{% if cp.confidence and cp.confidence.formula %}
**Report confidence:** `{{ cp.confidence.formula }}`
{% endif %}{% else %}_No metric provenance recorded._
{% endif %}

## 17. Appendix
Deterministic signals, schemas, relationships, data-quality detail and the full
business context sent to the model are available via the API (`/report` JSON).
""")


def render_markdown(report: dict) -> str:
    return _TEMPLATE.render(r=_Obj(report))


class _Obj(dict):
    """dict with attribute access for Jinja convenience."""
    def __getattr__(self, item):
        v = self.get(item)
        if isinstance(v, dict):
            return _Obj(v)
        if isinstance(v, list):
            return [_Obj(x) if isinstance(x, dict) else x for x in v]
        return v
