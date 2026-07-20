"""Product Intelligence & Strategic Decision APIs.

The Enterprise Product Manager's surface: the catalogue, product health,
reviews, strategic recommendations, portfolio intelligence, scenarios, KPI
intelligence, and executive strategy briefs. APIs only — no business logic
lives in this module.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field

from app.api.deps import container
from app.core.container import Container

router = APIRouter(tags=["product"])


def _product(c: Container):
    if c.product is None:
        raise HTTPException(
            status_code=503,
            detail="The product intelligence layer is disabled")
    return c.product


# --------------------------------------------------------------- overview
@router.get("/product")
def product_overview(c: Container = Depends(container)):
    """The executive product view: portfolio position, top products, what
    needs attention, open recommendations."""
    return _product(c).overview()


@router.get("/product/strategy")
def strategy(c: Container = Depends(container)):
    """The strategic picture: portfolio intelligence plus the executive
    strategy brief that explains it."""
    layer = _product(c)
    return {"portfolio": layer.portfolio.evaluate(),
            "recommendations": layer.strategy.recommendations(status="open",
                                                              limit=20),
            "brief_kinds": layer.briefs.kinds()}


# ---------------------------------------------------------------- catalog
class ProductCreate(BaseModel):
    name: str
    owner: str = ""
    description: str = ""
    business_unit: str = ""
    lifecycle: str = ""
    status: str = "active"
    dependencies: list[str] = Field(default_factory=list)
    project_id: str = ""


@router.get("/product/catalog")
def catalog(status: str = "", lifecycle: str = "", owner: str = "",
            business_unit: str = "", c: Container = Depends(container)):
    """Every enterprise product with its identity, owner, KPIs, and the
    merchants, customers, and reports it touches."""
    layer = _product(c)
    return {"products": layer.catalog.products(status=status,
                                               lifecycle=lifecycle,
                                               owner=owner,
                                               business_unit=business_unit),
            "stats": layer.catalog.stats()}


@router.post("/product/catalog", status_code=201)
def register_product(body: ProductCreate, c: Container = Depends(container)):
    """Register a product. Products are also discovered automatically from
    the organizational model — this is for the ones the business knows about
    before the data does."""
    try:
        product, _ = _product(c).catalog.upsert(
            body.name, owner=body.owner, description=body.description,
            business_unit=body.business_unit, lifecycle=body.lifecycle,
            status=body.status, dependencies=body.dependencies,
            source="manual", project_id=body.project_id)
        return product
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))


@router.post("/product/catalog/sync")
def sync_catalog(c: Container = Depends(container)):
    """Rebuild the catalogue from the organizational model and reattach every
    product's KPIs, reports, and relationships."""
    return _product(c).build_catalog()


@router.get("/product/catalog/{product_id:path}")
def product_detail(product_id: str, c: Container = Depends(container)):
    """One product: its record, health, latest review, and open work."""
    layer = _product(c)
    found = layer.catalog.get(product_id)
    if found is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"product": found,
            "health": layer.health.health(product_id),
            "review": layer.reviews.latest(product_id),
            "recommendations": layer.strategy.recommendations(
                product_id=product_id, status="open"),
            "kpi_alerts": layer.kpis.alerts(product_id=product_id, limit=10)}


class Lifecycle(BaseModel):
    lifecycle: str


@router.patch("/product/catalog/{product_id:path}")
def set_lifecycle(product_id: str, body: Lifecycle,
                  c: Container = Depends(container)):
    layer = _product(c)
    if layer.catalog.get(product_id) is None:
        raise HTTPException(status_code=404, detail="Product not found")
    try:
        return layer.catalog.set_lifecycle(product_id, body.lifecycle)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))


# ----------------------------------------------------------------- health
@router.get("/product/health")
def health(c: Container = Depends(container)):
    """Every product's health, with the reasons and evidence behind each
    score."""
    layer = _product(c)
    records = layer.health.all_health()
    return {"health": records,
            "scored": sum(1 for r in records
                          if r["health_score"] is not None),
            "unscored": [r["product"] for r in records
                         if r["health_score"] is None]}


@router.post("/product/health/evaluate")
def evaluate_health(product_id: str = "", c: Container = Depends(container)):
    """Re-score now, instead of waiting for the heartbeat."""
    layer = _product(c)
    if product_id:
        if layer.catalog.get(product_id) is None:
            raise HTTPException(status_code=404, detail="Product not found")
        return layer.health.evaluate(product_id)
    return layer.health.evaluate_all()


# ----------------------------------------------------------------- growth
@router.get("/product/growth")
def growth(kind: str = "", product_id: str = "",
           limit: int = Query(50, ge=1, le=200),
           c: Container = Depends(container)):
    """Growth intelligence: opportunities, decline, trends, cannibalization,
    cross-sell, gaps, expansion — each citing its evidence."""
    layer = _product(c)
    if kind or product_id:
        return {"findings": layer.growth.findings(kind=kind,
                                                  product_id=product_id,
                                                  limit=limit)}
    return layer.growth.analyse()


# ---------------------------------------------------------------- reviews
@router.get("/product/reviews")
def reviews(product_id: str = "", limit: int = Query(20, ge=1, le=100),
            c: Container = Depends(container)):
    return {"reviews": _product(c).reviews.reviews(product_id=product_id,
                                                   limit=limit)}


@router.post("/product/reviews", status_code=201)
def generate_review(product_id: str = "", register: bool = False,
                    c: Container = Depends(container)):
    """Generate a structured product review. ``register=true`` puts it into
    the executive's existing Report Review Center for approval."""
    layer = _product(c)
    if not product_id:
        return layer.reviews.review_all()
    if layer.catalog.get(product_id) is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return layer.reviews.review(product_id, register=register)


# -------------------------------------------------------- recommendations
@router.get("/product/recommendations")
def recommendations(product_id: str = "", play: str = "", status: str = "",
                    limit: int = Query(100, ge=1, le=500),
                    c: Container = Depends(container)):
    """Strategic recommendations, each with business impact, confidence,
    evidence, priority, effort, and dependencies."""
    layer = _product(c)
    return {"recommendations": layer.strategy.recommendations(
                product_id=product_id, play=play, status=status, limit=limit),
            "stats": layer.strategy.stats()}


@router.post("/product/recommendations")
def generate_recommendations(route: bool = True,
                             c: Container = Depends(container)):
    """Re-derive recommendations from current evidence. ``route`` hands each
    to the Decision Engine, which applies the existing approval policy."""
    return _product(c).strategy.generate(route=route)


class RecommendationStatus(BaseModel):
    status: str


@router.patch("/product/recommendations/{recommendation_id}")
def set_recommendation_status(recommendation_id: str,
                              body: RecommendationStatus,
                              c: Container = Depends(container)):
    try:
        updated = _product(c).strategy.set_status(recommendation_id,
                                                  body.status)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    if updated is None:
        raise HTTPException(status_code=404, detail="Recommendation not found")
    return updated


# -------------------------------------------------------------- portfolio
@router.get("/product/portfolio")
def portfolio(c: Container = Depends(container)):
    """Portfolio intelligence: health, risk, growth, ranking, investment
    priority, top opportunities and risks."""
    return _product(c).portfolio.evaluate()


# -------------------------------------------------------------- scenarios
class Scenario(BaseModel):
    lever: str
    change_pct: float
    product_id: str = ""
    question: str = ""


@router.get("/product/scenarios")
def scenarios(limit: int = Query(20, ge=1, le=100),
              c: Container = Depends(container)):
    """Past scenarios, and the levers that can be asked about."""
    layer = _product(c)
    return {"scenarios": layer.scenarios.scenarios(limit),
            "levers": layer.scenarios.levers()}


@router.post("/product/scenarios", status_code=201)
def simulate(body: Scenario, c: Container = Depends(container)):
    """"What happens if…" — projected from the platform's own KPIs and
    forecasts, with the assumptions stated and confidence inherited from the
    underlying forecast."""
    try:
        return _product(c).scenarios.simulate(
            body.lever, body.change_pct, product_id=body.product_id,
            question=body.question)
    except KeyError:
        raise HTTPException(status_code=404, detail="Product not found")
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))


# ------------------------------------------------------------------- KPIs
@router.get("/product/kpis")
def kpis(c: Container = Depends(container)):
    """Business, growth, operational, and portfolio KPIs, with any alerts."""
    layer = _product(c)
    return {**layer.kpis.overview(), "thresholds": layer.kpis.thresholds()}


@router.post("/product/kpis/monitor")
def monitor_kpis(c: Container = Depends(container)):
    """Check thresholds now and raise any work that is due."""
    return _product(c).kpis.monitor()


class Threshold(BaseModel):
    kpi: str
    warning: float
    critical: float
    direction: str = "higher_is_better"
    category: str = ""


@router.post("/product/kpis/thresholds", status_code=201)
def set_threshold(body: Threshold, c: Container = Depends(container)):
    """Give one KPI its own threshold rule — configuration, not a deploy."""
    try:
        return _product(c).kpis.set_threshold(
            body.kpi, body.warning, body.critical, direction=body.direction,
            category=body.category)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))


@router.get("/product/kpis/alerts")
def kpi_alerts(severity: str = "", product_id: str = "",
               limit: int = Query(50, ge=1, le=200),
               c: Container = Depends(container)):
    return {"alerts": _product(c).kpis.alerts(severity=severity,
                                              product_id=product_id,
                                              limit=limit)}


# ----------------------------------------------------------------- briefs
@router.get("/product/briefs")
def briefs(kind: str = "", limit: int = Query(20, ge=1, le=100),
           c: Container = Depends(container)):
    layer = _product(c)
    return {"briefs": layer.briefs.briefs(kind=kind, limit=limit),
            "kinds": layer.briefs.kinds()}


@router.post("/product/briefs/{kind}", status_code=201)
def generate_brief(kind: str, c: Container = Depends(container)):
    """Generate an executive brief: board_brief, monthly_review,
    quarterly_strategy, risk_summary, growth_summary, or decision_pack."""
    try:
        return _product(c).briefs.generate(kind)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
