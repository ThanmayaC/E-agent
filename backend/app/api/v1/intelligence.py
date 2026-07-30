"""Enterprise Intelligence APIs (V11) — the raw-transaction platform surface.

Every endpoint here answers from the transaction warehouse: analytics is SQL
over individual payments, ML is the backtested pipeline over the leak-free daily
frame, the product dashboards and ecosystem graph are compositions of those
queries, and the admin subsystem metrics are the real runtime state of each
layer. Nothing is precomputed and nothing is mocked — a number returned here can
always be traced to the transactions that produced it.

    /intel/analytics/*   KPIs, series, dimensions, failures, cohorts, geography
    /intel/ml/*          forecast, EDA, anomalies, segmentation, merchant health
    /intel/products/*    per-product intelligence dashboards
    /intel/ecosystem/*   the interactive graph + node intelligence
    /intel/mcc/*         the MCC explorer
    /intel/admin/*       real subsystem runtime metrics for the console
"""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query

from app.api.deps import container
from app.core.container import Container
from app.warehouse.filters import Filters

router = APIRouter(prefix="/intel", tags=["enterprise intelligence"])


# --------------------------------------------------------------- dependencies
def slice_filters(
    start: str | None = Query(None), end: str | None = Query(None),
    last_days: int | None = Query(None),
    product: str | None = Query(None), product_family: str | None = Query(None),
    payment_type: str | None = Query(None),
    bank: str | None = Query(None), psp: str | None = Query(None),
    mcc: str | None = Query(None), mcc_category: str | None = Query(None),
    mcc_subcategory: str | None = Query(None),
    merchant: str | None = Query(None), region: str | None = Query(None),
    state: str | None = Query(None), city: str | None = Query(None),
    segment: str | None = Query(None), channel: str | None = Query(None),
) -> Filters:
    return Filters.from_query(
        start=start, end=end, last_days=last_days, product=product,
        product_family=product_family, payment_type=payment_type, bank=bank,
        psp=psp, mcc=mcc, mcc_category=mcc_category,
        mcc_subcategory=mcc_subcategory, merchant=merchant, region=region,
        state=state, city=city, segment=segment, channel=channel)


def _analytics(c: Container):
    a = getattr(c, "tx_analytics", None)
    if a is None or not a.available:
        raise HTTPException(503, "transaction warehouse is not available; "
                                 "generate the corpus first")
    return a


def _ml(c: Container):
    m = getattr(c, "ml_pipeline", None)
    if m is None or not m.available:
        raise HTTPException(503, "ML pipeline is not available")
    return m


# -------------------------------------------------------------------- status
@router.get("/status")
def intel_status(c: Container = Depends(container)):
    """Is the warehouse live, and what does it hold?"""
    wh = getattr(c, "warehouse", None)
    if wh is None:
        return {"available": False}
    return {"available": wh.available, "warehouse": wh.status(),
            "corpus_window": (getattr(c, "tx_analytics").corpus_window()
                              if wh.available else None)}


# ----------------------------------------------------------------- analytics
@router.get("/analytics/kpis")
def analytics_kpis(c: Container = Depends(container),
                   f: Filters = Depends(slice_filters)):
    a = _analytics(c)
    return {"kpis": a.kpis(f), "window": a.resolve(f).describe()}


@router.get("/analytics/series")
def analytics_series(c: Container = Depends(container),
                     f: Filters = Depends(slice_filters)):
    a = _analytics(c)
    return {"daily": a.daily_series(f)}


@router.get("/analytics/monthly")
def analytics_monthly(c: Container = Depends(container),
                      f: Filters = Depends(slice_filters)):
    return {"monthly": _analytics(c).monthly_series(f)}


@router.get("/analytics/profile")
def analytics_profile(c: Container = Depends(container),
                      f: Filters = Depends(slice_filters)):
    a = _analytics(c)
    return {"hourly": a.hourly_profile(f), "weekday": a.weekday_profile(f)}


@router.get("/analytics/dimension/{dimension}")
def analytics_dimension(dimension: str, limit: int = Query(50, le=500),
                        c: Container = Depends(container),
                        f: Filters = Depends(slice_filters)):
    a = _analytics(c)
    try:
        return {"dimension": dimension,
                "rows": a.by_dimension(f, dimension, limit=limit)}
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc


@router.get("/analytics/dimension/{dimension}/series")
def analytics_dimension_series(dimension: str, top: int = Query(8, le=20),
                               c: Container = Depends(container),
                               f: Filters = Depends(slice_filters)):
    a = _analytics(c)
    try:
        return a.dimension_series(f, dimension, top=top)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc


@router.get("/analytics/failures")
def analytics_failures(c: Container = Depends(container),
                       f: Filters = Depends(slice_filters)):
    return _analytics(c).failure_analysis(f)


@router.get("/analytics/retry")
def analytics_retry(c: Container = Depends(container),
                    f: Filters = Depends(slice_filters)):
    return _analytics(c).retry_recovery(f)


@router.get("/analytics/adjustments")
def analytics_adjustments(c: Container = Depends(container),
                          f: Filters = Depends(slice_filters)):
    return _analytics(c).adjustments(f)


@router.get("/analytics/customers")
def analytics_customers(c: Container = Depends(container),
                        f: Filters = Depends(slice_filters)):
    a = _analytics(c)
    return {"activity": a.customer_activity(f),
            "behaviour": a.customer_behaviour(f)}


@router.get("/analytics/cohorts")
def analytics_cohorts(c: Container = Depends(container),
                      f: Filters = Depends(slice_filters)):
    return _analytics(c).cohort_retention(f)


@router.get("/analytics/concentration")
def analytics_concentration(dimension: str = Query("merchant"),
                            c: Container = Depends(container),
                            f: Filters = Depends(slice_filters)):
    return _analytics(c).concentration(f, dimension)


@router.get("/analytics/geography")
def analytics_geography(c: Container = Depends(container),
                        f: Filters = Depends(slice_filters)):
    return _analytics(c).geography(f)


@router.get("/analytics/mandates")
def analytics_mandates(c: Container = Depends(container),
                       f: Filters = Depends(slice_filters)):
    return _analytics(c).mandate_analytics(f)


@router.get("/analytics/incidents")
def analytics_incidents(c: Container = Depends(container),
                        f: Filters = Depends(slice_filters)):
    return {"incidents": _analytics(c).incidents(f)}


# ------------------------------------------------------------------------ ml
@router.get("/ml/forecast")
def ml_forecast(target: str = Query("attempts"), horizon: int = Query(14, le=60),
                full: bool = Query(True),
                c: Container = Depends(container),
                f: Filters = Depends(slice_filters)):
    m = _ml(c)
    if full:
        return m.run(f, target=target, horizon=horizon)
    return m.forecast_only(f, target=target, horizon=horizon)


@router.get("/ml/eda")
def ml_eda(target: str = Query("attempts"),
           c: Container = Depends(container),
           f: Filters = Depends(slice_filters)):
    return _ml(c).eda_only(f, target=target)


@router.get("/ml/anomalies")
def ml_anomalies(target: str = Query("success_rate"),
                 c: Container = Depends(container),
                 f: Filters = Depends(slice_filters)):
    return _ml(c).anomaly_scan(f, target=target)


@router.get("/ml/segments")
def ml_segments(c: Container = Depends(container),
                f: Filters = Depends(slice_filters)):
    from app.warehouse.ml import segment as seg
    return seg.cluster_merchants(_analytics(c), f)


@router.get("/ml/merchant-health")
def ml_merchant_health(limit: int = Query(200, le=1000),
                       c: Container = Depends(container),
                       f: Filters = Depends(slice_filters)):
    from app.warehouse.ml import segment as seg
    return seg.classify_merchant_health(_analytics(c), f, limit=limit)


@router.get("/ml/forecastable")
def ml_forecastable():
    from app.warehouse.ml import FORECASTABLE
    return {"targets": list(FORECASTABLE)}


# ------------------------------------------------------------------ products
@router.get("/products")
def products_overview(c: Container = Depends(container),
                      f: Filters = Depends(slice_filters)):
    """Every NPCI product with its headline metrics — the Products landing grid.
    All values derived from raw transactions over the window."""
    a = _analytics(c)
    catalog = {p["product_code"]: p for p in a.products()}
    rows = a.by_dimension(f, "product", limit=50)
    for r in rows:
        meta = catalog.get(r["name"], {})
        r["product_code"] = r["name"]
        r["product_name"] = meta.get("product_name", r["name"])
        r["product_family"] = meta.get("product_family")
    return {"products": rows, "window": a.resolve(f).describe()}


@router.get("/products/{product_code}")
def product_dashboard(product_code: str, horizon: int = Query(14, le=60),
                      c: Container = Depends(container),
                      f: Filters = Depends(slice_filters)):
    """The complete Product Intelligence Dashboard for one product — overview,
    trends, banks, PSPs, merchants, MCCs, failures, forecast, recommendations,
    all from this product's raw transactions."""
    a = _analytics(c)
    pf = f.with_(product=product_code)
    catalog = {p["product_code"]: p for p in a.products()}
    meta = catalog.get(product_code)
    if meta is None:
        raise HTTPException(404, f"unknown product: {product_code}")
    m = getattr(c, "ml_pipeline", None)
    forecast = None
    if m is not None and m.available:
        forecast = m.run(pf, target="attempts", horizon=horizon)
    return {
        "product": meta,
        "window": a.resolve(pf).describe(),
        "kpis": a.kpis(pf),
        "daily": a.daily_series(pf),
        "monthly": a.monthly_series(pf),
        "banks": a.by_dimension(pf, "bank", limit=15),
        "psps": a.by_dimension(pf, "psp", limit=15),
        "top_merchants": a.by_dimension(pf, "merchant_name", limit=15),
        "top_mccs": a.by_dimension(pf, "mcc_subcategory", limit=15),
        "segments": a.by_dimension(pf, "segment", limit=10),
        "failures": a.failure_analysis(pf),
        "forecast": forecast,
    }


# ----------------------------------------------------------------- ecosystem
@router.get("/ecosystem/graph")
def ecosystem_graph(c: Container = Depends(container),
                    f: Filters = Depends(slice_filters)):
    """Nodes (products, banks, PSPs, MCC categories) and the weighted edges of
    transaction flow between them — the interactive graph's backbone."""
    from app.warehouse.ecosystem import build_graph
    return build_graph(_analytics(c), f)


@router.get("/ecosystem/node/{node_type}/{node_id}")
def ecosystem_node(node_type: str, node_id: str,
                   c: Container = Depends(container),
                   f: Filters = Depends(slice_filters)):
    """Full intelligence for one node: details, neighbours, trend, forecast and
    recommendations — the drawer that opens when a node is clicked."""
    from app.warehouse.ecosystem import node_detail
    m = getattr(c, "ml_pipeline", None)
    try:
        return node_detail(_analytics(c), m, f, node_type, node_id)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc


# ----------------------------------------------------------------------- mcc
@router.get("/mcc")
def mcc_explorer(c: Container = Depends(container),
                 f: Filters = Depends(slice_filters)):
    """The MCC Explorer landing view: every category with distribution, value,
    success and growth — all from raw transactions."""
    from app.warehouse.ecosystem import mcc_overview
    return mcc_overview(_analytics(c), f)


@router.get("/mcc/{mcc_code}")
def mcc_detail(mcc_code: str, c: Container = Depends(container),
               f: Filters = Depends(slice_filters)):
    from app.warehouse.ecosystem import mcc_detail as _mcc_detail
    m = getattr(c, "ml_pipeline", None)
    return _mcc_detail(_analytics(c), m, f, mcc_code)


# --------------------------------------------------------------------- admin
@router.get("/admin/subsystems")
def admin_subsystems(c: Container = Depends(container)):
    """Real runtime metrics for every platform subsystem — the Admin console.
    No placeholders: each figure is read live from the subsystem it describes."""
    from app.warehouse.admin import subsystem_report
    return subsystem_report(c)


@router.get("/admin/warehouse")
def admin_warehouse(c: Container = Depends(container)):
    wh = getattr(c, "warehouse", None)
    if wh is None:
        raise HTTPException(503, "warehouse not wired")
    return {"status": wh.status(), "tables": wh.table_profile(),
            "recent_queries": wh.recent_queries(), "schema": wh.schema("txn")}
