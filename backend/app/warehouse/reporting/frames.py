"""One pass over the corpus that yields every frame the daily reports need.

The naive way to write 206 daily reports is to run twenty queries per day. That
is four thousand round trips, and — worse — it makes it possible for two
sections of the same report to disagree, because each ran its own query with
its own filter.

Instead this module runs a dozen queries *once*, each grouped by date and one
dimension, and hands back pandas frames the report slices per day. Every number
in every report therefore comes from the same scan of the same rows, and the
whole run costs one pass.

Only raw transactions are read. There is no aggregate table anywhere in this
path — the frames are computed here and thrown away.
"""
from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from app.warehouse.engine import Warehouse

# Attempts on the rail, excluding money-back rows which are counted separately.
_ATTEMPTS = "attempts"


@dataclass
class ReportFrames:
    daily: pd.DataFrame
    by_product: pd.DataFrame
    by_bank: pd.DataFrame
    by_psp: pd.DataFrame
    by_category: pd.DataFrame
    by_region: pd.DataFrame
    by_segment: pd.DataFrame
    by_merchant: pd.DataFrame
    failures: pd.DataFrame
    hourly: pd.DataFrame
    incidents: list[dict]
    calendar: pd.DataFrame

    @property
    def dates(self) -> list[str]:
        return list(self.daily["txn_date"])


_DIM_SQL = """
SELECT txn_date,
       {col} AS entity,
       COUNT(*)                                                AS attempts,
       SUM(CASE WHEN status = 'SUCCESS' THEN 1 ELSE 0 END)      AS successes,
       100.0 * SUM(CASE WHEN status = 'SUCCESS' THEN 1 ELSE 0 END)
             / NULLIF(COUNT(*), 0)                              AS success_rate,
       SUM(CASE WHEN status = 'SUCCESS' THEN amount_inr ELSE 0 END)
                                                                AS value_inr,
       COUNT(DISTINCT customer_id)                              AS customers
FROM attempts
WHERE {col} IS NOT NULL
GROUP BY 1, 2
"""


def _dim(wh: Warehouse, col: str) -> pd.DataFrame:
    df = wh.df(_DIM_SQL.format(col=col))
    return df.rename(columns={"entity": col})


def load_frames(wh: Warehouse, *, merchant_top: int = 60) -> ReportFrames:
    """Every frame the report set needs, in one pass over the corpus."""
    daily = wh.df("""
        WITH a AS (
          SELECT txn_date,
                 COUNT(*)                                          AS attempts,
                 SUM(CASE WHEN status='SUCCESS' THEN 1 ELSE 0 END)  AS successes,
                 SUM(CASE WHEN status='FAILED'  THEN 1 ELSE 0 END)  AS failures,
                 SUM(CASE WHEN status='PENDING' THEN 1 ELSE 0 END)  AS pending,
                 SUM(CASE WHEN status='SUCCESS' THEN amount_inr ELSE 0 END)
                                                                    AS value_inr,
                 SUM(CASE WHEN is_retry THEN 1 ELSE 0 END)          AS retries,
                 SUM(CASE WHEN is_retry AND status='SUCCESS'
                          THEN 1 ELSE 0 END)                        AS retry_wins,
                 COUNT(DISTINCT customer_id)                        AS customers,
                 COUNT(DISTINCT merchant_id)                        AS merchants,
                 COUNT(DISTINCT payer_bank)                         AS banks,
                 QUANTILE_CONT(latency_ms, 0.95)                    AS latency_p95,
                 MEDIAN(latency_ms)                                 AS latency_p50,
                 SUM(CASE WHEN failure_bucket='technical' THEN 1 ELSE 0 END)
                                                                    AS f_technical,
                 SUM(CASE WHEN failure_bucket='business'  THEN 1 ELSE 0 END)
                                                                    AS f_business,
                 SUM(CASE WHEN failure_bucket='risk'      THEN 1 ELSE 0 END)
                                                                    AS f_risk,
                 SUM(CASE WHEN failure_bucket='timeout'   THEN 1 ELSE 0 END)
                                                                    AS f_timeout
          FROM attempts GROUP BY 1),
        adj AS (
          SELECT txn_date,
                 SUM(CASE WHEN txn_type='REFUND'     THEN 1 ELSE 0 END) AS refunds,
                 SUM(CASE WHEN txn_type='REVERSAL'   THEN 1 ELSE 0 END) AS reversals,
                 SUM(CASE WHEN txn_type='CHARGEBACK' THEN 1 ELSE 0 END) AS chargebacks,
                 SUM(ABS(amount_inr))                                   AS adj_value_inr
          FROM adjustments GROUP BY 1)
        SELECT a.*,
               COALESCE(adj.refunds, 0)       AS refunds,
               COALESCE(adj.reversals, 0)     AS reversals,
               COALESCE(adj.chargebacks, 0)   AS chargebacks,
               COALESCE(adj.adj_value_inr, 0) AS adj_value_inr
        FROM a LEFT JOIN adj USING (txn_date)
        ORDER BY txn_date
    """)
    daily["success_rate"] = daily["successes"] / daily["attempts"] * 100
    daily["avg_ticket"] = daily["value_inr"] / daily["successes"].replace(0, pd.NA)
    daily["retry_share"] = daily["retries"] / daily["attempts"] * 100
    daily["retry_recovery_pct"] = (
        daily["retry_wins"] / daily["retries"].replace(0, pd.NA) * 100)
    for b in ("technical", "business", "risk", "timeout"):
        daily[f"{b}_pct"] = daily[f"f_{b}"] / daily["attempts"] * 100
    # Same weekday a week ago — the only honest comparison in a business with
    # a hard weekly cycle, so every reported measure gets one.
    for col in ("attempts", "successes", "success_rate", "value_inr",
                "avg_ticket", "technical_pct", "business_pct", "risk_pct",
                "timeout_pct", "retry_share", "latency_p95", "customers",
                "merchants", "refunds", "reversals", "chargebacks"):
        daily[f"{col}_w1"] = daily[col].shift(7)

    failures = wh.df("""
        SELECT txn_date, failure_code,
               MIN(failure_reason) AS failure_reason,
               MIN(failure_bucket) AS failure_bucket,
               MIN(failure_owner)  AS failure_owner,
               COUNT(*)            AS n
        FROM attempts
        WHERE status = 'FAILED' AND failure_code IS NOT NULL
        GROUP BY 1, 2
    """)
    if not failures.empty:
        totals = daily.set_index("txn_date")["attempts"]
        failures["rate_pct"] = (
            failures["n"] / failures["txn_date"].map(totals) * 100)

    # Merchants are capped to a stable panel: an unbounded per-day merchant
    # frame is hundreds of thousands of rows and the report only ever names a
    # handful. A fixed panel also stops merchants flickering in and out of the
    # narrative between days for purely sampling reasons.
    panel = wh.df(f"""
        SELECT merchant_name FROM attempts
        WHERE merchant_name IS NOT NULL
        GROUP BY 1 ORDER BY COUNT(*) DESC LIMIT {int(merchant_top)}
    """)
    names = ", ".join(f"'{n}'" for n in panel["merchant_name"]) or "''"
    by_merchant = wh.df(f"""
        SELECT txn_date, merchant_name AS merchant, merchant_tier,
               MIN(mcc_category) AS mcc_category,
               COUNT(*) AS attempts,
               100.0 * SUM(CASE WHEN status='SUCCESS' THEN 1 ELSE 0 END)
                     / NULLIF(COUNT(*), 0) AS success_rate,
               SUM(CASE WHEN status='SUCCESS' THEN amount_inr ELSE 0 END)
                     AS value_inr
        FROM attempts WHERE merchant_name IN ({names})
        GROUP BY 1, 2, 3
    """)

    hourly = wh.df("""
        SELECT txn_date, hour, COUNT(*) AS attempts,
               100.0 * SUM(CASE WHEN status='SUCCESS' THEN 1 ELSE 0 END)
                     / NULLIF(COUNT(*), 0) AS success_rate
        FROM attempts GROUP BY 1, 2
    """)

    return ReportFrames(
        daily=daily,
        by_product=_dim(wh, "product_name"),
        by_bank=_dim(wh, "payer_bank"),
        by_psp=_dim(wh, "payer_psp"),
        by_category=_dim(wh, "mcc_category"),
        by_region=_dim(wh, "region"),
        by_segment=_dim(wh, "customer_segment"),
        by_merchant=by_merchant,
        failures=failures,
        hourly=hourly,
        incidents=wh.query("SELECT * FROM dim_incidents ORDER BY start_date"),
        calendar=wh.df("SELECT * FROM dim_calendar ORDER BY date"),
    )
