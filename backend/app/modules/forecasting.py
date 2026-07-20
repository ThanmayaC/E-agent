"""Forecasting Module (SDS §2.2).

Deterministic trend + seasonal forecasts with confidence intervals over
discovered KPI series. ML-admitted forecasts (champion/challenger) come from
the Machine Learning Module; this module is the always-available baseline.
"""
from app.intelligence.forecasting.engine import ForecastEngine

__all__ = ["ForecastEngine"]
