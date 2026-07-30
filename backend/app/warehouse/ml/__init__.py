"""The machine-learning layer over the raw transaction warehouse.

    features → eda → forecast → anomaly / segment → insight → pipeline

Every model reads the leak-free daily frame built from raw transactions and
returns not just a number but the evidence, confidence and recommendation that
make it a decision. `MLPipeline` is the single entry point.
"""
from app.warehouse.ml.pipeline import FORECASTABLE, MLPipeline

__all__ = ["MLPipeline", "FORECASTABLE"]
