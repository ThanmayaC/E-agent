"""Analyst-layer APIs (V10.0) — multi-level intelligence surface.

Exposes the Layer-2 ML models (each prediction tagged model+version+confidence+
features), the multi-layer insight engine (explains WHY), the continuous-learning
feedback store, and the retrieval/cache stats. Read-only except feedback, which
writes only to the learning store.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from app.api.deps import container
from app.core.container import Container

router = APIRouter(tags=["analyst"])


def _ml(c: Container):
    ml = getattr(c, "ml", None)
    if ml is None:
        raise HTTPException(503, "The ML layer is not available")
    return ml


# ------------------------------------------------------------------ ML layer
@router.get("/ml")
def ml_status(c: Container = Depends(container)):
    return _ml(c).status()


@router.get("/ml/models")
def ml_models(c: Container = Depends(container)):
    """Model cards for every trained model (explainability index)."""
    return _ml(c).models()


@router.get("/ml/forecast")
def ml_forecast(kpi: str = "Success Rate (%)", horizon: int = 30,
                c: Container = Depends(container)):
    return _ml(c).forecast(kpi, horizon)


@router.get("/ml/anomalies")
def ml_anomalies(c: Container = Depends(container)):
    return _ml(c).anomalies()


@router.get("/ml/segments")
def ml_segments(k: int = 4, c: Container = Depends(container)):
    return _ml(c).segment_merchants(k)


@router.get("/ml/churn")
def ml_churn(c: Container = Depends(container)):
    return _ml(c).churn_merchants()


@router.get("/ml/failure")
def ml_failure(c: Container = Depends(container)):
    return _ml(c).failure_banks()


# ------------------------------------------------------------- insights
@router.get("/insights")
def insights(limit: int = 12, c: Container = Depends(container)):
    """WHY-first insights composed from deterministic + ML + graph layers."""
    eng = getattr(c, "insight_engine", None)
    if eng is None:
        raise HTTPException(503, "The insight engine is not available")
    return eng.insights(limit)


# ------------------------------------------------------- continuous learning
class Feedback(BaseModel):
    kind: str = Field("recommendation")
    ref: str = Field(...)
    action: str = Field(...)  # accepted / rejected / applied / dismissed ...
    meta: dict | None = None


@router.get("/learning")
def learning_stats(c: Container = Depends(container)):
    ls = getattr(c, "learning_store", None)
    if ls is None:
        raise HTTPException(503, "The learning store is not available")
    return ls.stats()


@router.post("/learning/feedback", status_code=201)
def learning_feedback(body: Feedback, c: Container = Depends(container)):
    ls = getattr(c, "learning_store", None)
    if ls is None:
        raise HTTPException(503, "The learning store is not available")
    return ls.record_feedback(body.kind, body.ref, body.action, body.meta)


# -------------------------------------------------------------- cache stats
@router.get("/cache")
def cache_stats(c: Container = Depends(container)):
    ws = getattr(c, "workspace", None)
    return {"search_cache": ws.cache_stats() if ws else {}}
