"""The raw-transaction warehouse — the platform's single source of truth.

    parquet corpus  →  Warehouse (DuckDB SQL)  →  TransactionAnalytics  →  MLPipeline

Millions of individual payment rows across every NPCI product live here as
partitioned parquet. Every KPI, chart, forecast and AI answer in the platform is
a query against this layer — there is no aggregate table, no nightly rollup and
no stored dashboard, so any number can always be traced back to the transactions
that produced it.
"""
from app.warehouse.analytics import KPI_META, TransactionAnalytics
from app.warehouse.engine import Warehouse, WarehouseQueryError, get_warehouse
from app.warehouse.filters import Filters, clamp_window

__all__ = ["Warehouse", "WarehouseQueryError", "get_warehouse",
           "TransactionAnalytics", "KPI_META", "Filters", "clamp_window"]
