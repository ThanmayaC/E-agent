"""Executive Intelligence APIs (V3.1) — the AI Product Head's surface.

Read-only endpoints over the :class:`ExecutiveIntelligence` layer: the daily
executive brief, Monday-morning priorities, ranked recommendations, KPI
intelligence, enhanced/ranked decisions, risks, and the recurring-pattern
memory. Everything is derived from the ingested enterprise — no new data, no
Brain change — and every figure traces to the KPI workbook.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends

from app.api.deps import container
from app.core.container import Container

router = APIRouter(tags=["executive"])


@router.get("/executive")
def executive_status(c: Container = Depends(container)):
    """Is the executive layer live, and how much enterprise does it see?"""
    return c.executive.status()


@router.get("/executive/brief")
def executive_brief(c: Container = Depends(container)):
    """The daily executive brief: business summary, critical events, major
    decisions, risk assessment, products/banks/merchants at risk, customer
    impact, recommended actions, deadlines, priorities, and confidence."""
    return c.executive.executive_brief()


@router.get("/executive/priorities")
def executive_priorities(c: Container = Depends(container)):
    """What the Product Head should prioritize, ranked with reason, impact,
    confidence, and the evidence behind each."""
    return {"priorities": c.executive.priorities()}


@router.get("/executive/recommendations")
def executive_recommendations(c: Container = Depends(container)):
    """Ranked recommendations, each with reason, evidence, business impact,
    confidence, owner, timeline, dependencies, and status."""
    return {"recommendations": c.executive.recommendations()}


@router.get("/executive/kpis")
def executive_kpis(c: Container = Depends(container)):
    """KPI intelligence: composite health scores plus a card per KPI with its
    value, change, trend, why it changed, the cause, and a recommended action."""
    return c.executive.kpi_intelligence()


@router.get("/executive/decisions")
def executive_decisions(c: Container = Depends(container)):
    """Enhanced, ranked decisions: problem, alternatives, reason selected,
    expected/actual impact, affected products/banks/merchants/customers,
    confidence, business value, learning, and an executive-priority rank."""
    return {"decisions": c.executive.decisions()}


@router.get("/executive/risks")
def executive_risks(c: Container = Depends(container)):
    """Top operational risks, banks at risk, products at risk, and merchants
    to follow up — with the evidence and recommended action for each."""
    return c.executive.risks()


@router.get("/executive/patterns")
def executive_patterns(c: Container = Depends(container)):
    """Recurring signals across every week on record — the memory the
    assistant keeps: recurring bank, incident, merchants, KPI, recommendation,
    and repeat-offender banks with a "has this happened before" flag."""
    return c.executive.patterns()


@router.get("/executive/trends")
def executive_trends(c: Container = Depends(container)):
    """Per-KPI {today, yesterday, last_week, last_month, trend} — the shared
    data source for trend rows across Home/Reports/Products."""
    return {"trends": c.executive.trends()}


@router.get("/executive/week-over-week")
def executive_week_over_week(c: Container = Depends(container)):
    """Per-KPI average for the latest week vs. the week before it."""
    return {"comparison": c.executive.week_over_week()}


@router.get("/executive/month-over-month")
def executive_month_over_month(c: Container = Depends(container)):
    """Per-KPI value at month start vs. the latest value."""
    return {"comparison": c.executive.month_over_month()}


@router.get("/executive/reports")
def executive_reports(c: Container = Depends(container)):
    """Every report + RCA, categorised for the Reports hub (Daily/Weekly/
    Monthly/Product/Merchant/Bank/Failure Analysis/Executive), each with a
    summary, key findings, evidence, recommendations, linked decisions,
    related products, and a trend."""
    return {"reports": c.executive.reports()}


# ---------------------------------------------------------------------------
# V7.0 — UPI ecosystem analytics (over the sampled ledger + aggregate cubes).
# ---------------------------------------------------------------------------
@router.get("/executive/ecosystem")
def ecosystem_status(c: Container = Depends(container)):
    """Is the ecosystem layer live, and how many days/cubes does it hold?"""
    return c.ecosystem.status()


@router.get("/executive/ecosystem/overview")
def ecosystem_overview(c: Container = Depends(container)):
    """Period, sampled volume/value, latest daily metrics, and the top
    feature/bank/PSP/city."""
    return c.ecosystem.overview()


@router.get("/executive/ecosystem/features")
def ecosystem_features(c: Container = Depends(container)):
    """Every UPI feature compared: txns, value, avg ticket, success, share, and
    month-over-month growth."""
    return {"features": c.ecosystem.compare_features()}


@router.get("/executive/ecosystem/features/{feature}")
def ecosystem_feature(feature: str, c: Container = Depends(container)):
    """One feature's daily series plus its totals, ticket, success and growth."""
    return c.ecosystem.feature_analytics(feature)


@router.get("/executive/ecosystem/banks")
def ecosystem_banks(c: Container = Depends(container)):
    """Every bank compared: volume, share, average success, growth."""
    return {"banks": c.ecosystem.compare_banks()}


@router.get("/executive/ecosystem/psps")
def ecosystem_psps(c: Container = Depends(container)):
    """Every PSP compared: volume, share, average success, growth."""
    return {"psps": c.ecosystem.compare_psps()}


@router.get("/executive/ecosystem/market-share")
def ecosystem_market_share(c: Container = Depends(container)):
    """Feature/bank/PSP share now and the share trend (first vs last day)."""
    return c.ecosystem.market_share()


@router.get("/executive/ecosystem/growth")
def ecosystem_growth(c: Container = Depends(container)):
    """Growth leaders and laggards across features, banks, PSPs and cities."""
    return c.ecosystem.growth_leaders()


@router.get("/executive/ecosystem/cities")
def ecosystem_cities(c: Container = Depends(container)):
    """Cities ranked by sampled volume and value."""
    return {"cities": c.ecosystem.city_trends()}


@router.get("/executive/ecosystem/hourly")
def ecosystem_hourly(c: Container = Depends(container)):
    """Hourly transaction distribution across the month (sampled)."""
    return {"hourly": c.ecosystem.hourly_distribution()}


@router.get("/executive/ecosystem/mix")
def ecosystem_mix(c: Container = Depends(container)):
    """Transaction mix by payment type, with share."""
    return {"mix": c.ecosystem.transaction_mix()}


@router.get("/executive/ecosystem/anomalies")
def ecosystem_anomalies(c: Container = Depends(container)):
    """Business-intelligence signals: anomalies, high-risk banks, share loss,
    declining features."""
    return {"anomalies": c.ecosystem.anomalies(),
            "findings": c.ecosystem.bi_findings()}


@router.get("/executive/ecosystem/forecasts")
def ecosystem_forecasts(c: Container = Depends(container)):
    """Directional next-period forecasts for headline metrics and features."""
    return {"forecasts": c.ecosystem.forecasts()}


@router.get("/executive/ecosystem/kpis")
def ecosystem_kpis(c: Container = Depends(container)):
    """Compact ecosystem dashboard: latest metrics, headline trends, top
    entities, and growth leaders."""
    return c.ecosystem.executive_kpis()


# ---------------------------------------------------------------------------
# V8.0 — six-month evolution: entity lifecycle, multi-granularity trends,
# rolling windows, forecast validation, decision tracking, cross-entity links,
# storylines, and the executive workspace Q&A.
# ---------------------------------------------------------------------------
@router.get("/executive/evolution")
def evolution_status(c: Container = Depends(container)):
    """Is the six-month digital twin live, and how large are its cubes?"""
    return c.evolution.status()


@router.get("/executive/evolution/overview")
def evolution_overview(c: Container = Depends(container)):
    """Compact evolution dashboard: user base, entity movers, decisions."""
    return c.evolution.overview()


@router.get("/executive/evolution/customers")
def evolution_customers(c: Container = Depends(container)):
    """User-base lifecycle: DAU/WAU/MAU, retention, churn, power vs dormant."""
    return c.evolution.customers()


@router.get("/executive/evolution/merchants")
def evolution_merchants(c: Container = Depends(container)):
    """Merchant lifecycle: health, stage, growth, retention, churn, status."""
    return c.evolution.merchants()


@router.get("/executive/evolution/merchants/{name}")
def evolution_merchant(name: str, c: Container = Depends(container)):
    return c.evolution.merchant(name)


@router.get("/executive/evolution/banks")
def evolution_banks(c: Container = Depends(container)):
    """Bank evolution + competition: share movement, latency, incidents."""
    return c.evolution.banks()


@router.get("/executive/evolution/psps")
def evolution_psps(c: Container = Depends(container)):
    """PSP competition: market-share gainers and losers, satisfaction."""
    return c.evolution.psps()


@router.get("/executive/evolution/products")
def evolution_products(c: Container = Depends(container)):
    """Product lifecycle: stage, adoption, mix, revenue, market share."""
    return c.evolution.products()


@router.get("/executive/evolution/products/{name}")
def evolution_product(name: str, c: Container = Depends(container)):
    return c.evolution.product(name)


@router.get("/executive/evolution/features")
def evolution_features(c: Container = Depends(container)):
    """Feature adoption journey and saturation."""
    return c.evolution.feature_adoption()


@router.get("/executive/evolution/trends")
def evolution_trends(grain: str = "monthly", c: Container = Depends(container)):
    """KPI roll-ups at weekly / monthly / quarterly granularity."""
    return c.evolution.trends(grain)


@router.get("/executive/evolution/trends/{kpi}")
def evolution_trend(kpi: str, c: Container = Depends(container)):
    """One KPI across every granularity plus its rolling 30/90-day windows."""
    return c.evolution.trend(kpi)


@router.get("/executive/evolution/forecast-accuracy")
def evolution_forecast_accuracy(c: Container = Depends(container)):
    """Backtested forecast validation: predicted vs realised."""
    return c.evolution.forecast_accuracy()


@router.get("/executive/evolution/forecast/{kpi}")
def evolution_forecast(kpi: str, c: Container = Depends(container)):
    """Forward 30-day forecast band + backtest for one KPI."""
    return c.evolution.forecast(kpi)


@router.get("/executive/evolution/decisions")
def evolution_decisions(c: Container = Depends(container)):
    """Executive decision tracking: expected vs actual impact, business value."""
    return c.evolution.decisions()


@router.get("/executive/evolution/decisions/{decision_id}")
def evolution_decision(decision_id: str, c: Container = Depends(container)):
    return c.evolution.decision(decision_id)


@router.get("/executive/evolution/cross-entity")
def evolution_cross_entity(entity: str | None = None,
                           c: Container = Depends(container)):
    """Cross-entity relationships (merchant↔PSP↔bank, feature↔product…)."""
    return c.evolution.cross_entity(entity)


@router.get("/executive/evolution/stories")
def evolution_stories(c: Container = Depends(container)):
    """The connected weekly storyline across the six months."""
    return c.evolution.stories()


@router.get("/executive/evolution/stories/{week}")
def evolution_story(week: int, c: Container = Depends(container)):
    return c.evolution.story(week)


@router.get("/executive/evolution/ask")
def evolution_ask(q: str = "", c: Container = Depends(container)):
    """Executive workspace Q&A over the six-month history."""
    return c.evolution.ask(q)
