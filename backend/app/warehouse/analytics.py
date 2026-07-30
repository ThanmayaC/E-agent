"""Analytics over raw transactions.

Every metric here is a SQL expression over individual payment rows. There is no
aggregate table to go stale, no nightly job to be behind, and no number that
cannot be re-derived by re-running the same query. A KPI is a *definition*, not
a stored value:

    success_rate = successful attempts / attempts

so when the corpus changes, the KPI changes with it — automatically, and by
exactly as much as the underlying transactions moved.
"""
from __future__ import annotations

from datetime import date, timedelta

from app.core.logging import get_logger
from app.warehouse.engine import Warehouse
from app.warehouse.filters import Filters

logger = get_logger(__name__)

# The metric block reused by nearly every aggregation. Written once so a
# product page, a bank page and an AI answer cannot disagree on definitions.
_METRICS = """
    count(*)                                                    AS attempts,
    count(*) FILTER (WHERE status = 'SUCCESS')                  AS successful,
    count(*) FILTER (WHERE status = 'FAILED')                   AS failed,
    count(*) FILTER (WHERE status = 'PENDING')                  AS pending,
    round(100.0 * count(*) FILTER (WHERE status = 'SUCCESS')
          / nullif(count(*), 0), 3)                             AS success_rate,
    round(100.0 * count(*) FILTER (WHERE failure_bucket = 'technical')
          / nullif(count(*), 0), 3)                             AS technical_decline_pct,
    round(100.0 * count(*) FILTER (WHERE failure_bucket = 'business')
          / nullif(count(*), 0), 3)                             AS business_decline_pct,
    round(100.0 * count(*) FILTER (WHERE failure_bucket = 'risk')
          / nullif(count(*), 0), 3)                             AS risk_decline_pct,
    round(100.0 * count(*) FILTER (WHERE failure_bucket = 'timeout')
          / nullif(count(*), 0), 3)                             AS timeout_pct,
    round(sum(amount_inr) FILTER (WHERE status = 'SUCCESS'), 2) AS value_inr,
    round(avg(amount_inr) FILTER (WHERE status = 'SUCCESS'), 2) AS avg_ticket_inr,
    round(median(amount_inr) FILTER (WHERE status = 'SUCCESS'), 2)
                                                                AS median_ticket_inr,
    count(DISTINCT customer_id)                                 AS active_customers,
    count(DISTINCT merchant_id)                                 AS active_merchants,
    round(quantile_cont(latency_ms, 0.95), 0)                   AS p95_latency_ms,
    round(median(latency_ms), 0)                                AS p50_latency_ms,
    count(*) FILTER (WHERE is_retry)                            AS retries,
    round(100.0 * count(*) FILTER (WHERE is_retry)
          / nullif(count(*), 0), 3)                             AS retry_rate_pct
"""

# Direction and unit metadata for the KPI cards; 'higher' says which way is good.
KPI_META: dict[str, dict] = {
    "attempts": {"label": "Transaction attempts", "unit": "txns", "higher": True},
    "successful": {"label": "Successful transactions", "unit": "txns",
                   "higher": True},
    "success_rate": {"label": "Success rate", "unit": "%", "higher": True},
    "technical_decline_pct": {"label": "Technical declines", "unit": "%",
                              "higher": False},
    "business_decline_pct": {"label": "Business declines", "unit": "%",
                             "higher": False},
    "risk_decline_pct": {"label": "Risk declines", "unit": "%",
                         "higher": False},
    "timeout_pct": {"label": "Timeouts", "unit": "%", "higher": False},
    "value_inr": {"label": "Settled value", "unit": "₹", "higher": True},
    "avg_ticket_inr": {"label": "Average ticket", "unit": "₹", "higher": True},
    "active_customers": {"label": "Active customers", "unit": "users",
                         "higher": True},
    "active_merchants": {"label": "Active merchants", "unit": "merchants",
                         "higher": True},
    "p95_latency_ms": {"label": "p95 latency", "unit": "ms", "higher": False},
    "retry_rate_pct": {"label": "Retry rate", "unit": "%", "higher": False},
}


def _pct_change(now, prior) -> float | None:
    if now is None or prior in (None, 0):
        return None
    try:
        return round(100.0 * (float(now) - float(prior)) / abs(float(prior)), 2)
    except (TypeError, ValueError, ZeroDivisionError):
        return None


class TransactionAnalytics:
    """Read-only analytics surface. Stateless — everything is a query."""

    def __init__(self, warehouse: Warehouse):
        self.wh = warehouse

    # ------------------------------------------------------------- corpus
    @property
    def available(self) -> bool:
        return self.wh.available

    def corpus_window(self) -> tuple[str, str]:
        row = self.wh.one(
            "SELECT min(txn_date) AS a, max(txn_date) AS b FROM txn",
            label="corpus.window")
        return (str(row.get("a") or ""), str(row.get("b") or ""))

    def resolve(self, f: Filters) -> Filters:
        """Fill in a concrete window so prior-period maths is well defined."""
        start, end = self.corpus_window()
        if not start:
            return f
        out = f
        if f.last_days:
            e = date.fromisoformat(end)
            out = out.with_(
                start=str(max(date.fromisoformat(start),
                              e - timedelta(days=f.last_days - 1))),
                end=end, last_days=None)
        if not out.start:
            out = out.with_(start=start)
        if not out.end:
            out = out.with_(end=end)
        return out

    def _prior(self, f: Filters) -> Filters:
        """The equally long window immediately before this one."""
        try:
            s, e = date.fromisoformat(f.start), date.fromisoformat(f.end)
        except (TypeError, ValueError):
            return f
        span = (e - s).days + 1
        return f.with_(start=str(s - timedelta(days=span)),
                       end=str(s - timedelta(days=1)))

    # ------------------------------------------------------------ headline
    def summary(self, f: Filters) -> dict:
        """Base metrics for a slice, with the previous period alongside."""
        f = self.resolve(f)
        where, params = f.where()
        now = self.wh.one(
            f"SELECT {_METRICS} FROM attempts WHERE {where}", params,
            label="analytics.summary")
        pf = self._prior(f)
        pw, pp = pf.where()
        prior = self.wh.one(
            f"SELECT {_METRICS} FROM attempts WHERE {pw}", pp,
            label="analytics.summary.prior")
        return {"window": {"start": f.start, "end": f.end},
                "prior_window": {"start": pf.start, "end": pf.end},
                "filters": f.describe(), "current": now, "prior": prior}

    def kpis(self, f: Filters) -> list[dict]:
        """KPI cards — value, prior value, change and direction, all derived."""
        s = self.summary(f)
        cur, prior = s["current"], s["prior"]
        out = []
        for key, meta in KPI_META.items():
            v, p = cur.get(key), prior.get(key)
            change = _pct_change(v, p)
            good = None
            if change is not None:
                good = (change >= 0) if meta["higher"] else (change <= 0)
            out.append({
                "key": key, "label": meta["label"], "unit": meta["unit"],
                "value": v, "prior": p, "change_pct": change,
                "direction": "up" if (change or 0) > 0 else
                             ("down" if (change or 0) < 0 else "flat"),
                "is_good": good, "higher_is_better": meta["higher"],
            })
        out.extend(self._adjustment_kpis(f))
        return out

    def _adjustment_kpis(self, f: Filters) -> list[dict]:
        f = self.resolve(f)
        where, params = f.where()
        row = self.wh.one(f"""
            SELECT
              count(*) FILTER (WHERE txn_type = 'REFUND')     AS refunds,
              count(*) FILTER (WHERE txn_type = 'REVERSAL')   AS reversals,
              count(*) FILTER (WHERE txn_type = 'CHARGEBACK') AS chargebacks,
              round(abs(sum(amount_inr) FILTER (WHERE txn_type = 'REFUND')), 2)
                                                              AS refund_value
            FROM adjustments WHERE {where}""", params,
            label="analytics.adjustments")
        settled = self.wh.scalar(
            f"SELECT count(*) FROM settled WHERE {where}", params, default=0) or 1
        return [
            {"key": "refund_rate_pct", "label": "Refund rate", "unit": "%",
             "value": round(100.0 * (row.get("refunds") or 0) / settled, 3),
             "prior": None, "change_pct": None, "direction": "flat",
             "is_good": None, "higher_is_better": False},
            {"key": "chargeback_rate_pct", "label": "Chargeback rate",
             "unit": "%",
             "value": round(100.0 * (row.get("chargebacks") or 0) / settled, 4),
             "prior": None, "change_pct": None, "direction": "flat",
             "is_good": None, "higher_is_better": False},
            {"key": "reversals", "label": "Auto-reversals", "unit": "txns",
             "value": row.get("reversals") or 0, "prior": None,
             "change_pct": None, "direction": "flat", "is_good": None,
             "higher_is_better": False},
        ]

    # -------------------------------------------------------------- series
    def daily_series(self, f: Filters) -> list[dict]:
        """The per-day fact table — the input to every chart and every model."""
        f = self.resolve(f)
        where, params = f.where()
        return self.wh.query(f"""
            SELECT txn_date AS date, any_value(day_of_week) AS day_of_week,
                   any_value(is_weekend) AS is_weekend,
                   any_value(is_holiday) AS is_holiday,
                   any_value(calendar_event) AS calendar_event,
                   {_METRICS}
            FROM attempts WHERE {where}
            GROUP BY txn_date ORDER BY txn_date""", params,
            label="analytics.daily_series")

    def monthly_series(self, f: Filters) -> list[dict]:
        f = self.resolve(f)
        where, params = f.where()
        return self.wh.query(f"""
            SELECT strftime(CAST(txn_date AS DATE), '%Y-%m') AS month,
                   count(DISTINCT txn_date) AS days, {_METRICS}
            FROM attempts WHERE {where}
            GROUP BY 1 ORDER BY 1""", params, label="analytics.monthly")

    def hourly_profile(self, f: Filters) -> list[dict]:
        f = self.resolve(f)
        where, params = f.where()
        return self.wh.query(f"""
            SELECT hour, count(*) AS attempts,
                   round(100.0 * count(*) FILTER (WHERE status='SUCCESS')
                         / nullif(count(*),0), 2) AS success_rate,
                   round(sum(amount_inr) FILTER (WHERE status='SUCCESS'), 0)
                        AS value_inr,
                   round(quantile_cont(latency_ms, 0.95), 0) AS p95_latency_ms
            FROM attempts WHERE {where}
            GROUP BY hour ORDER BY hour""", params, label="analytics.hourly")

    def weekday_profile(self, f: Filters) -> list[dict]:
        f = self.resolve(f)
        where, params = f.where()
        return self.wh.query(f"""
            SELECT day_of_week,
                   round(avg(n), 0) AS avg_attempts,
                   round(avg(sr), 3) AS avg_success_rate,
                   round(avg(v), 0) AS avg_value_inr
            FROM (
              SELECT txn_date, any_value(day_of_week) AS day_of_week,
                     count(*) AS n,
                     100.0*count(*) FILTER (WHERE status='SUCCESS')
                        / nullif(count(*),0) AS sr,
                     sum(amount_inr) FILTER (WHERE status='SUCCESS') AS v
              FROM attempts WHERE {where} GROUP BY txn_date)
            GROUP BY day_of_week ORDER BY day_of_week""", params,
            label="analytics.weekday")

    # ---------------------------------------------------------- dimensions
    _DIM_SQL = {
        "product": "product_code", "product_name": "product_name",
        "family": "product_family", "bank": "payer_bank",
        "payee_bank": "payee_bank", "psp": "payer_psp",
        "payee_psp": "payee_psp", "mcc": "mcc", "mcc_category": "mcc_category",
        "mcc_subcategory": "mcc_subcategory", "merchant": "merchant_id",
        "merchant_name": "merchant_name", "region": "region", "state": "state",
        "city": "city", "segment": "customer_segment", "device": "device",
        "channel": "channel", "payment_type": "payment_type",
        "merchant_tier": "merchant_tier", "failure_code": "failure_code",
    }

    def by_dimension(self, f: Filters, dimension: str, *, limit: int = 50,
                     with_growth: bool = True) -> list[dict]:
        """Rank a dimension by volume, with share and period-over-period growth
        computed from the same raw rows."""
        col = self._DIM_SQL.get(dimension)
        if not col:
            raise ValueError(f"unknown dimension: {dimension}")
        f = self.resolve(f)
        where, params = f.where()
        rows = self.wh.query(f"""
            SELECT {col} AS name, {_METRICS}
            FROM attempts WHERE {where} AND {col} IS NOT NULL
            GROUP BY {col} ORDER BY attempts DESC LIMIT {int(limit)}""",
            params, label=f"analytics.dim.{dimension}")
        total = self.wh.scalar(
            f"SELECT count(*) FROM attempts WHERE {where} AND {col} IS NOT NULL",
            params, default=0) or 1
        prior_map: dict[str, dict] = {}
        if with_growth:
            pf = self._prior(f)
            pw, pp = pf.where()
            prior_map = {str(r["name"]): r for r in self.wh.query(f"""
                SELECT {col} AS name, count(*) AS attempts,
                       sum(amount_inr) FILTER (WHERE status='SUCCESS') AS value_inr,
                       100.0*count(*) FILTER (WHERE status='SUCCESS')
                            / nullif(count(*),0) AS success_rate
                FROM attempts WHERE {pw} AND {col} IS NOT NULL
                GROUP BY {col}""", pp, label=f"analytics.dim.{dimension}.prior")}
        for r in rows:
            key = str(r["name"])
            r["share_pct"] = round(100.0 * (r["attempts"] or 0) / total, 3)
            p = prior_map.get(key)
            r["prior_attempts"] = p["attempts"] if p else None
            r["growth_pct"] = _pct_change(r["attempts"],
                                          p["attempts"] if p else None)
            r["value_growth_pct"] = _pct_change(
                r["value_inr"], p["value_inr"] if p else None)
            r["success_rate_delta_pp"] = (
                round(float(r["success_rate"] or 0) - float(p["success_rate"] or 0), 3)
                if p and p.get("success_rate") is not None
                and r.get("success_rate") is not None else None)
        return rows

    def dimension_series(self, f: Filters, dimension: str, *,
                         top: int = 8) -> dict:
        """Daily series for the top N members of a dimension — the shape a
        multi-line comparison chart needs."""
        col = self._DIM_SQL.get(dimension)
        if not col:
            raise ValueError(f"unknown dimension: {dimension}")
        f = self.resolve(f)
        leaders = [str(r["name"]) for r in
                   self.by_dimension(f, dimension, limit=top,
                                     with_growth=False)]
        if not leaders:
            return {"dimension": dimension, "members": [], "series": []}
        where, params = f.where()
        marks = ", ".join("?" for _ in leaders)
        rows = self.wh.query(f"""
            SELECT txn_date AS date, {col} AS name, count(*) AS attempts,
                   round(100.0*count(*) FILTER (WHERE status='SUCCESS')
                         / nullif(count(*),0), 3) AS success_rate,
                   round(sum(amount_inr) FILTER (WHERE status='SUCCESS'), 0)
                        AS value_inr
            FROM attempts WHERE {where} AND {col} IN ({marks})
            GROUP BY 1, 2 ORDER BY 1, 2""", params + leaders,
            label=f"analytics.dimseries.{dimension}")
        return {"dimension": dimension, "members": leaders, "series": rows}

    # ------------------------------------------------------------ failures
    def failure_analysis(self, f: Filters) -> dict:
        f = self.resolve(f)
        where, params = f.where()
        by_code = self.wh.query(f"""
            SELECT failure_code AS code, any_value(failure_reason) AS reason,
                   any_value(failure_bucket) AS bucket,
                   any_value(failure_owner) AS owner,
                   any_value(retryable) AS retryable,
                   count(*) AS failures,
                   round(100.0 * count(*) / nullif(sum(count(*)) OVER (), 0), 2)
                        AS share_pct,
                   round(avg(amount_inr), 0) AS avg_amount_inr
            FROM attempts WHERE {where} AND status = 'FAILED'
            GROUP BY failure_code ORDER BY failures DESC""", params,
            label="analytics.failures.code")
        by_owner = self.wh.query(f"""
            SELECT failure_owner AS owner, count(*) AS failures,
                   round(100.0 * count(*) / nullif(sum(count(*)) OVER (), 0), 2)
                        AS share_pct
            FROM attempts WHERE {where} AND status = 'FAILED'
            GROUP BY failure_owner ORDER BY failures DESC""", params,
            label="analytics.failures.owner")
        by_bank = self.wh.query(f"""
            SELECT payer_bank AS bank, count(*) AS attempts,
                   count(*) FILTER (WHERE status='FAILED') AS failures,
                   round(100.0 * count(*) FILTER (WHERE status='FAILED')
                         / nullif(count(*),0), 3) AS failure_rate_pct,
                   round(100.0 * count(*) FILTER (WHERE failure_bucket='technical')
                         / nullif(count(*),0), 3) AS technical_pct
            FROM attempts WHERE {where}
            GROUP BY payer_bank HAVING count(*) > 200
            ORDER BY failure_rate_pct DESC""", params,
            label="analytics.failures.bank")
        trend = self.wh.query(f"""
            SELECT txn_date AS date, failure_bucket AS bucket, count(*) AS n
            FROM attempts WHERE {where} AND status = 'FAILED'
            GROUP BY 1, 2 ORDER BY 1""", params, label="analytics.failures.trend")
        return {"by_code": by_code, "by_owner": by_owner,
                "by_bank": by_bank, "trend": trend,
                "window": {"start": f.start, "end": f.end}}

    def retry_recovery(self, f: Filters) -> dict:
        """How much revenue the retry path actually recovers."""
        f = self.resolve(f)
        where, params = f.where()
        row = self.wh.one(f"""
            SELECT count(*) AS retry_attempts,
                   count(*) FILTER (WHERE status='SUCCESS') AS recovered,
                   round(100.0 * count(*) FILTER (WHERE status='SUCCESS')
                         / nullif(count(*),0), 2) AS recovery_rate_pct,
                   round(sum(amount_inr) FILTER (WHERE status='SUCCESS'), 0)
                        AS recovered_value_inr
            FROM attempts WHERE {where} AND is_retry""", params,
            label="analytics.retry")
        by_product = self.wh.query(f"""
            SELECT product_code AS product, count(*) AS retry_attempts,
                   round(100.0 * count(*) FILTER (WHERE status='SUCCESS')
                         / nullif(count(*),0), 2) AS recovery_rate_pct
            FROM attempts WHERE {where} AND is_retry
            GROUP BY product_code ORDER BY retry_attempts DESC""", params,
            label="analytics.retry.product")
        return {**row, "by_product": by_product}

    def adjustments(self, f: Filters) -> dict:
        """Refunds, auto-reversals and chargebacks — the money that flows back."""
        f = self.resolve(f)
        where, params = f.where()
        by_type = self.wh.query(f"""
            SELECT txn_type AS type, count(*) AS n,
                   round(abs(sum(amount_inr)), 2) AS value_inr,
                   round(abs(avg(amount_inr)), 2) AS avg_value_inr
            FROM adjustments WHERE {where} GROUP BY 1 ORDER BY n DESC""",
            params, label="analytics.adjust.type")
        by_mcc = self.wh.query(f"""
            SELECT mcc, any_value(mcc_subcategory) AS subcategory,
                   count(*) FILTER (WHERE txn_type='REFUND') AS refunds,
                   count(*) FILTER (WHERE txn_type='CHARGEBACK') AS chargebacks,
                   round(abs(sum(amount_inr)), 0) AS value_inr
            FROM adjustments WHERE {where} AND mcc IS NOT NULL
            GROUP BY mcc ORDER BY value_inr DESC LIMIT 20""", params,
            label="analytics.adjust.mcc")
        trend = self.wh.query(f"""
            SELECT txn_date AS date, txn_type AS type, count(*) AS n
            FROM adjustments WHERE {where} GROUP BY 1,2 ORDER BY 1""", params,
            label="analytics.adjust.trend")
        return {"by_type": by_type, "by_mcc": by_mcc, "trend": trend}

    # ------------------------------------------------------------ customers
    def customer_activity(self, f: Filters) -> list[dict]:
        """New / returning / reactivated customers per day, straight from the
        first- and last-seen dates in the transaction stream."""
        f = self.resolve(f)
        where, params = f.where()
        return self.wh.query(f"""
            WITH t AS (
              SELECT customer_id, txn_date,
                     min(txn_date) OVER (PARTITION BY customer_id) AS first_seen,
                     lag(txn_date) OVER (PARTITION BY customer_id
                                         ORDER BY txn_date) AS prev_date
              FROM (SELECT DISTINCT customer_id, txn_date
                    FROM attempts WHERE {where})
            )
            SELECT txn_date AS date,
                   count(*) AS active_customers,
                   count(*) FILTER (WHERE txn_date = first_seen) AS new_customers,
                   count(*) FILTER (WHERE prev_date IS NOT NULL
                                    AND date_diff('day', CAST(prev_date AS DATE),
                                                  CAST(txn_date AS DATE)) > 21)
                        AS reactivated,
                   count(*) FILTER (WHERE prev_date IS NOT NULL
                                    AND date_diff('day', CAST(prev_date AS DATE),
                                                  CAST(txn_date AS DATE)) <= 21)
                        AS returning
            FROM t GROUP BY txn_date ORDER BY txn_date""", params,
            label="analytics.customer_activity")

    def cohort_retention(self, f: Filters, *, periods: int = 6) -> dict:
        """Monthly acquisition cohorts and their month-on-month retention."""
        f = self.resolve(f)
        where, params = f.where()
        rows = self.wh.query(f"""
            WITH first_txn AS (
              SELECT customer_id, min(txn_date) AS first_date
              FROM attempts WHERE {where} GROUP BY customer_id
            ), acts AS (
              SELECT DISTINCT a.customer_id,
                     strftime(CAST(ft.first_date AS DATE), '%Y-%m') AS cohort,
                     date_diff('month', date_trunc('month', CAST(ft.first_date AS DATE)),
                               date_trunc('month', CAST(a.txn_date AS DATE)))
                          AS period,
                     strftime(CAST(a.txn_date AS DATE), '%Y-%m') AS active_month
              FROM attempts a JOIN first_txn ft USING (customer_id)
              WHERE {where}
            )
            SELECT cohort, period, count(DISTINCT customer_id) AS customers
            FROM acts WHERE period BETWEEN 0 AND {int(periods)}
            GROUP BY cohort, period ORDER BY cohort, period""",
            params * 2,   # the slice predicate appears in both CTEs
            label="analytics.cohorts")
        sizes = {r["cohort"]: r["customers"] for r in rows if r["period"] == 0}
        for r in rows:
            base = sizes.get(r["cohort"]) or 0
            r["retention_pct"] = round(100.0 * r["customers"] / base, 2) \
                if base else None
        return {"cohorts": rows, "sizes": sizes}

    def customer_behaviour(self, f: Filters) -> dict:
        f = self.resolve(f)
        where, params = f.where()
        by_segment = self.wh.query(f"""
            SELECT customer_segment AS segment, count(*) AS attempts,
                   count(DISTINCT customer_id) AS customers,
                   round(count(*) * 1.0 / nullif(count(DISTINCT customer_id),0), 2)
                        AS txns_per_customer,
                   round(avg(amount_inr) FILTER (WHERE status='SUCCESS'), 0)
                        AS avg_ticket_inr,
                   round(100.0*count(*) FILTER (WHERE status='SUCCESS')
                         / nullif(count(*),0), 2) AS success_rate,
                   round(sum(amount_inr) FILTER (WHERE status='SUCCESS'), 0)
                        AS value_inr
            FROM attempts WHERE {where}
            GROUP BY 1 ORDER BY attempts DESC""", params,
            label="analytics.behaviour.segment")
        frequency = self.wh.query(f"""
            SELECT bucket, count(*) AS customers FROM (
              SELECT customer_id,
                CASE WHEN n = 1 THEN '1'
                     WHEN n <= 3 THEN '2-3'
                     WHEN n <= 10 THEN '4-10'
                     WHEN n <= 30 THEN '11-30'
                     WHEN n <= 100 THEN '31-100'
                     ELSE '100+' END AS bucket
              FROM (SELECT customer_id, count(*) AS n FROM attempts
                    WHERE {where} GROUP BY customer_id))
            GROUP BY bucket ORDER BY customers DESC""", params,
            label="analytics.behaviour.frequency")
        products_per_customer = self.wh.query(f"""
            SELECT products_used, count(*) AS customers FROM (
              SELECT customer_id, count(DISTINCT product_code) AS products_used
              FROM attempts WHERE {where} GROUP BY customer_id)
            GROUP BY 1 ORDER BY 1""", params, label="analytics.behaviour.cross")
        return {"by_segment": by_segment, "frequency": frequency,
                "products_per_customer": products_per_customer}

    def concentration(self, f: Filters, dimension: str = "merchant") -> dict:
        """Pareto: what share of volume the top 1 / 5 / 10 / 20 % carry."""
        col = self._DIM_SQL.get(dimension, "merchant_id")
        f = self.resolve(f)
        where, params = f.where()
        row = self.wh.one(f"""
            WITH e AS (
              SELECT {col} AS name, count(*) AS n
              FROM attempts WHERE {where} AND {col} IS NOT NULL GROUP BY 1
            ), r AS (
              SELECT name, n, row_number() OVER (ORDER BY n DESC) AS rk,
                     count(*) OVER () AS total_entities,
                     sum(n) OVER () AS total_n
              FROM e
            )
            SELECT any_value(total_entities) AS entities,
                   round(100.0*sum(n) FILTER (WHERE rk <= greatest(1, total_entities/100))
                         / nullif(any_value(total_n),0), 2) AS top_1pct_share,
                   round(100.0*sum(n) FILTER (WHERE rk <= greatest(1, total_entities/20))
                         / nullif(any_value(total_n),0), 2) AS top_5pct_share,
                   round(100.0*sum(n) FILTER (WHERE rk <= greatest(1, total_entities/10))
                         / nullif(any_value(total_n),0), 2) AS top_10pct_share,
                   round(100.0*sum(n) FILTER (WHERE rk <= greatest(1, total_entities/5))
                         / nullif(any_value(total_n),0), 2) AS top_20pct_share
            FROM r""", params, label=f"analytics.concentration.{dimension}")
        return {"dimension": dimension, **row}

    # -------------------------------------------------------------- mandates
    def mandate_analytics(self, f: Filters) -> dict:
        """The AutoPay book: lifecycle flow, execution quality and churn."""
        f = self.resolve(f)
        where, params = f.where()
        ev_where = where.replace("txn_date", "event_date")
        lifecycle = self.wh.query(f"""
            SELECT event, count(*) AS n, count(DISTINCT mandate_id) AS mandates
            FROM dim_mandate_events
            WHERE event_date BETWEEN ? AND ?
            GROUP BY event ORDER BY n DESC""", [f.start, f.end],
            label="analytics.mandate.lifecycle")
        daily = self.wh.query("""
            SELECT event_date AS date,
                   count(*) FILTER (WHERE event='MANDATE_CREATED')  AS created,
                   count(*) FILTER (WHERE event='MANDATE_EXECUTED') AS executed,
                   count(*) FILTER (WHERE event='MANDATE_FAILED')   AS failed,
                   count(*) FILTER (WHERE event='MANDATE_RETRY')    AS retried,
                   count(*) FILTER (WHERE event='MANDATE_REVOKED')  AS revoked,
                   count(*) FILTER (WHERE event='MANDATE_PAUSED')   AS paused,
                   count(*) FILTER (WHERE event='MANDATE_CANCELLED') AS cancelled
            FROM dim_mandate_events WHERE event_date BETWEEN ? AND ?
            GROUP BY event_date ORDER BY event_date""", [f.start, f.end],
            label="analytics.mandate.daily")
        by_purpose = self.wh.query("""
            SELECT purpose, any_value(category) AS category, frequency,
                   count(*) FILTER (WHERE event IN ('MANDATE_EXECUTED',
                                                    'MANDATE_FAILED')) AS executions,
                   round(100.0*count(*) FILTER (WHERE event='MANDATE_EXECUTED')
                         / nullif(count(*) FILTER (WHERE event IN
                              ('MANDATE_EXECUTED','MANDATE_FAILED')),0), 2)
                        AS execution_success_pct,
                   round(avg(amount_inr) FILTER (WHERE event='MANDATE_EXECUTED'), 0)
                        AS avg_amount_inr
            FROM dim_mandate_events WHERE event_date BETWEEN ? AND ?
            GROUP BY purpose, frequency
            HAVING executions > 0 ORDER BY executions DESC""",
            [f.start, f.end], label="analytics.mandate.purpose")
        book = self.wh.one("""
            SELECT count(*) AS total_mandates,
                   count(*) FILTER (WHERE status='ACTIVE')    AS active,
                   count(*) FILTER (WHERE status='PAUSED')    AS paused,
                   count(*) FILTER (WHERE status='REVOKED')   AS revoked,
                   count(*) FILTER (WHERE status='CANCELLED') AS cancelled,
                   count(*) FILTER (WHERE status='EXPIRED')   AS expired,
                   round(sum(amount_inr) FILTER (WHERE status='ACTIVE'), 0)
                        AS active_committed_inr
            FROM dim_mandates""", label="analytics.mandate.book")
        failures = self.wh.query("""
            SELECT failure_code, count(*) AS n
            FROM dim_mandate_events
            WHERE event='MANDATE_FAILED' AND failure_code IS NOT NULL
              AND event_date BETWEEN ? AND ?
            GROUP BY 1 ORDER BY n DESC LIMIT 10""", [f.start, f.end],
            label="analytics.mandate.failures")
        return {"book": book, "lifecycle": lifecycle, "daily": daily,
                "by_purpose": by_purpose, "failure_codes": failures,
                "window": {"start": f.start, "end": f.end}}

    # -------------------------------------------------------------- geography
    def geography(self, f: Filters) -> dict:
        f = self.resolve(f)
        where, params = f.where()
        by_region = self.by_dimension(f, "region", limit=10)
        by_state = self.by_dimension(f, "state", limit=40)
        by_city = self.by_dimension(f, "city", limit=40)
        tiers = self.wh.query(f"""
            SELECT city_tier, count(*) AS attempts,
                   round(100.0*count(*) FILTER (WHERE status='SUCCESS')
                         / nullif(count(*),0), 2) AS success_rate,
                   round(avg(amount_inr) FILTER (WHERE status='SUCCESS'), 0)
                        AS avg_ticket_inr
            FROM attempts WHERE {where} GROUP BY 1 ORDER BY 1""", params,
            label="analytics.geo.tier")
        return {"regions": by_region, "states": by_state, "cities": by_city,
                "city_tiers": tiers}

    # ------------------------------------------------------------- incidents
    def incidents(self, f: Filters | None = None) -> list[dict]:
        """The ground-truth event calendar — used to score anomaly detection."""
        if not self.wh.available:
            return []
        if f and f.start and f.end:
            return self.wh.query(
                "SELECT * FROM dim_incidents WHERE end_date >= ? "
                "AND start_date <= ? ORDER BY start_date DESC",
                [f.start, f.end], label="analytics.incidents")
        return self.wh.query(
            "SELECT * FROM dim_incidents ORDER BY start_date DESC",
            label="analytics.incidents.all")

    def calendar(self, f: Filters) -> list[dict]:
        f = self.resolve(f)
        return self.wh.query(
            "SELECT * FROM dim_calendar WHERE date BETWEEN ? AND ? "
            "ORDER BY date", [f.start, f.end], label="analytics.calendar")

    # ------------------------------------------------------------ reference
    def products(self) -> list[dict]:
        return self.wh.query("SELECT * FROM dim_products ORDER BY product_code",
                             label="ref.products")

    def mccs(self) -> list[dict]:
        return self.wh.query("SELECT * FROM dim_mcc ORDER BY mcc",
                             label="ref.mcc")

    def banks(self) -> list[dict]:
        return self.wh.query("SELECT * FROM dim_banks ORDER BY share DESC",
                             label="ref.banks")

    def psps(self) -> list[dict]:
        return self.wh.query("SELECT * FROM dim_psps ORDER BY share DESC",
                             label="ref.psps")
