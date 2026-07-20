"""Schema Intelligence Module (SDS §2.1).

Structural discovery without predefined mappings: column/table profiling
(types, identifiers, currencies, PK candidates, measures vs dimensions,
facts vs dimension tables) and time-series structure detection.
"""
from app.intelligence.profiling.profiler import ColumnProfiler
from app.intelligence.timeseries.detector import TimeSeriesDetector

__all__ = ["ColumnProfiler", "TimeSeriesDetector"]
