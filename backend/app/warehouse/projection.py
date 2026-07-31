"""Cube projection — the day-wise analytics cubes, derived from the corpus.

Why this module exists
----------------------
The platform used to contain *two independent transaction simulators*:

1. ``warehouse/generator`` — emits raw transaction rows. No KPI is asserted;
   success rate, ticket size, growth and seasonality are all emergent from
   per-transaction outcomes. This feeds Analytics, Products and the ML pipeline
   through DuckDB.
2. ``generate_enterprise.py::Ledger`` — sampled ~10k rows/day and then
   *reconciled them to an asserted KPI series* (``n_success = round(N * sr/100)``
   where ``sr`` came from a hand-authored KPI engine). It rolled those rows up
   into ``enterprise_data/master/analytics/*.csv``, which Ecosystem, Evolution,
   the executive surfaces and ~30 other modules read.

The second one has the causality backwards: the KPI produced the transactions
rather than the transactions producing the KPI. Worse, its KPI engine knew
nothing about the incidents the warehouse simulates, so the two sources
disagreed about the same business days — measured at **r = +0.20** on daily
success rate and **+0.23** on volume across the 206-day window. On 2026-01-28
the Analytics page reported 95.17% success while the Ecosystem page reported
99.55%: same company, same day, same product, two answers.

This module removes the second source. Every cube below is now a SQL aggregate
over the raw corpus, so the numbers on every page reconcile by construction and
an incident visible in Analytics is visible in Evolution too.

What is *not* projected here
----------------------------
The narrative and model-output cubes (``storylines``, ``bi_findings``,
``decision_tracking``, ``forecasts``, ``forecast_validation``,
``product_lifecycle``, ``*_evolution``) are downstream interpretations rather
than aggregates of the ledger. They are left to their existing producer; see
``docs/AUDIT_2026-07-30.md`` for the follow-up plan.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

from app.core.logging import get_logger

logger = get_logger(__name__)

try:
    import duckdb
    _DUCKDB = True
except ImportError:  # pragma: no cover - duckdb is a hard dependency in prod
    _DUCKDB = False

# Rows that represent a payment *attempt* on the rail. Refunds, reversals and
# chargebacks move money back and must never inflate an attempt count or dilute
# a success rate — the same split the warehouse engine uses.
ATTEMPT_TYPES = ("PAYMENT", "MANDATE_EXECUTION", "RETRY", "MANDATE_RETRY")

# The corpus is a fixed-rate sample of the national network, not the whole of
# it. This factor lifts sampled attempts to the NPCI-scale headline figure and
# is the *only* place that scaling is applied.
#
# Calibrated so the corpus mean (13,131.8 attempts/day) maps onto the ~697.4 M
# attempts/day the platform reports for the window. That keeps the headline
# number continuous across this change — only its day-to-day *shape* becomes
# evidence-derived. Recalibrate this if the corpus size changes materially:
#   NATIONAL_SCALE_M_PER_TXN = target_national_mean_M / corpus_mean_attempts
NATIONAL_SCALE_M_PER_TXN = 0.053108

# ``merchant_daily`` is a dashboard input, and the ecosystem layer loads every
# cube fully into memory at startup. The corpus carries 2,400 merchants, so an
# unbounded projection would be ~293k rows (95x the previous cube) held
# resident for a panel that ranks the top handful. Per-merchant deep-dives go
# to the warehouse directly via /intel rather than through this cube.
TOP_MERCHANTS = 50

_ATTEMPTS = ", ".join(f"'{t}'" for t in ATTEMPT_TYPES)


@dataclass
class CubeResult:
    name: str
    rows: int
    path: Path


class CubeProjection:
    """Rebuilds the day-wise analytics cubes from the transaction corpus."""

    def __init__(self, warehouse_root: str | Path, out_dir: str | Path):
        self.txn_glob = str(Path(warehouse_root) / "transactions" / "*.parquet")
        self.ref_dir = Path(warehouse_root) / "reference"
        self.out = Path(out_dir)

    # ------------------------------------------------------------------ util
    def _con(self):
        if not _DUCKDB:
            raise RuntimeError(
                "duckdb is required to project the analytics cubes")
        return duckdb.connect()

    def _write(self, con, name: str, sql: str,
               header: list[str]) -> CubeResult:
        rows = con.execute(sql).fetchall()
        self.out.mkdir(parents=True, exist_ok=True)
        path = self.out / f"{name}.csv"
        with path.open("w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(header)
            for r in rows:
                w.writerow([_fmt(v) for v in r])
        logger.info("projected cube %s: %d rows", name, len(rows))
        return CubeResult(name=name, rows=len(rows), path=path)

    # ----------------------------------------------------------------- build
    def build(self) -> dict[str, CubeResult]:
        con = self._con()
        t, att = self.txn_glob, _ATTEMPTS
        out: dict[str, CubeResult] = {}

        # A single scan feeding every daily cube. day_index is 0-based in the
        # corpus and 1-based in the published cubes, so it is shifted once here
        # rather than in each consumer.
        con.execute(f"""
            CREATE OR REPLACE TEMP VIEW attempts AS
            SELECT *, day_index + 1 AS day
            FROM read_parquet('{t}')
            WHERE txn_type IN ({att})
        """)
        con.execute(f"""
            CREATE OR REPLACE TEMP VIEW adjustments AS
            SELECT *, day_index + 1 AS day
            FROM read_parquet('{t}')
            WHERE txn_type NOT IN ({att})
        """)

        out["daily_metrics"] = self._daily_metrics(con)
        out["bank_daily"] = self._entity_daily(
            con, "bank_daily", "payer_bank", "bank")
        out["psp_daily"] = self._entity_daily(
            con, "psp_daily", "payer_psp", "psp")
        out["feature_daily"] = self._entity_daily(
            con, "feature_daily", "product_name", "feature")
        out["merchant_daily"] = self._merchant_daily(con)
        out["city_daily"] = self._city_daily(con)
        out["hourly_distribution"] = self._hourly(con)
        out["transaction_mix"] = self._mix(con)
        out["customer_activity"] = self._customer_activity(con)
        out["kpi_rolling"] = self._kpi_rolling(con)
        out["trends"] = self._trends(con)
        out["product_lifecycle"] = self._product_lifecycle(con)
        out["feature_adoption"] = self._feature_adoption(con)
        con.close()
        return out

    # ------------------------------------------------- product × month cubes
    _LIFECYCLE_SQL = """
        WITH m AS (
          SELECT {group_col} AS name,
                 strftime(txn_date::DATE, '%b %Y') AS month_label,
                 date_trunc('month', txn_date::DATE) AS month_start,
                 count(*) AS txns,
                 sum(amount_inr) AS value_inr,
                 count(DISTINCT customer_id) AS customers,
                 count(DISTINCT merchant_id) AS merchants,
                 100.0 * sum(CASE WHEN status='SUCCESS' THEN 1 ELSE 0 END)
                       / count(*) AS success_rate
          FROM attempts WHERE {group_col} IS NOT NULL
          GROUP BY 1, 2, 3
        ),
        tot AS (
          SELECT month_start, sum(txns) AS all_txns, sum(value_inr) AS all_value
          FROM m GROUP BY 1
        ),
        idx AS (
          SELECT month_start,
                 dense_rank() OVER (ORDER BY month_start) AS month_index
          FROM (SELECT DISTINCT month_start FROM m)
        ),
        j AS (
          SELECT m.*, idx.month_index,
                 100.0 * m.txns / nullif(tot.all_txns, 0) AS share_pct,
                 100.0 * m.value_inr / nullif(tot.all_value, 0) AS rev_pct,
                 lag(m.txns) OVER (PARTITION BY m.name ORDER BY m.month_start)
                     AS prev_txns
          FROM m JOIN tot USING (month_start) JOIN idx USING (month_start)
        )
        SELECT * FROM j ORDER BY name, month_index
    """

    @staticmethod
    def _stage(share_pct: float, mom: float | None) -> str:
        """Lifecycle stage read off the numbers, not assigned by hand.

        The previous cube carried a stage label written by the generator; here
        it is a function of the product's own measured share and momentum, so a
        product that stops growing stops being called "Growth".
        """
        if mom is None:
            return "New"
        if mom >= 25:
            return "Hypergrowth"
        if mom >= 8:
            return "Growth"
        if mom <= -8:
            return "Decline"
        return "Saturation" if share_pct >= 10 else "Mature"

    def _lifecycle_rows(self, con, group_col: str) -> list[list]:
        rows = con.execute(
            self._LIFECYCLE_SQL.format(group_col=group_col)).fetchall()
        cols = [d[0] for d in con.description]
        out = []
        for r in rows:
            d = dict(zip(cols, r))
            prev = d.get("prev_txns")
            mom = (round(100.0 * (d["txns"] - prev) / prev, 2)
                   if prev else None)
            out.append([
                d["name"], d["month_label"], d["month_index"], d["txns"],
                round(d["value_inr"], 2),
                round(d["value_inr"] / d["txns"], 2) if d["txns"] else 0,
                round(d["success_rate"], 2), round(d["share_pct"], 2),
                round(d["rev_pct"], 2), d["customers"], d["merchants"],
                mom, self._stage(d["share_pct"], mom)])
        return out

    def _product_lifecycle(self, con) -> CubeResult:
        rows = self._lifecycle_rows(con, "product_name")
        return self._rows_to_csv(
            "product_lifecycle", rows,
            ["product", "month", "month_index", "txns", "value_inr",
             "avg_ticket_inr", "success_rate", "market_share_pct",
             "revenue_contribution_pct", "customers", "merchants",
             "mom_growth_pct", "lifecycle_stage"])

    def _feature_adoption(self, con) -> CubeResult:
        # Same shape, keyed by payment type — "feature" in this platform's
        # vocabulary is how a payment was initiated (QR, intent, collect),
        # which is the payment_type column rather than the product.
        rows = self._lifecycle_rows(con, "payment_type")
        return self._rows_to_csv(
            "feature_adoption", rows,
            ["feature", "month", "month_index", "txns", "value_inr",
             "avg_ticket_inr", "avg_success_rate", "share_pct",
             "revenue_contribution_pct", "adopters", "merchants",
             "mom_growth_pct", "stage"])

    def _rows_to_csv(self, name: str, rows: list[list],
                     header: list[str]) -> CubeResult:
        self.out.mkdir(parents=True, exist_ok=True)
        path = self.out / f"{name}.csv"
        with path.open("w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(header)
            for r in rows:
                w.writerow(["" if v is None else _fmt(v) for v in r])
        logger.info("projected cube %s: %d rows", name, len(rows))
        return CubeResult(name=name, rows=len(rows), path=path)

    # --------------------------------------------------------- daily metrics
    def _daily_metrics(self, con) -> CubeResult:
        """The spine cube: one row per day, every field an aggregate.

        ``archetype`` used to be a label the KPI engine stamped on the day in
        advance. Here it is *read back* out of the corpus — an incident that
        actually depressed success rate produces an incident archetype, so the
        label and the numbers can never contradict each other.
        """
        sql = f"""
        WITH d AS (
          SELECT day, txn_date,
                 -- min() rather than any_value(): these columns are constant
                 -- within a day, but any_value() picks whichever row the
                 -- parallel scan reached first and so is not reproducible.
                 min(is_weekend)      AS is_weekend,
                 min(is_holiday)      AS is_holiday,
                 min(calendar_event)  AS calendar_event,
                 min(day_of_week)     AS dow,
                 count(*)                   AS attempts,
                 sum(amount_inr)            AS value_inr,
                 count(DISTINCT customer_id) AS active_customers,
                 100.0 * sum(CASE WHEN status='SUCCESS' THEN 1 ELSE 0 END)
                       / count(*)           AS success_rate,
                 -- A timeout is an infrastructure failure, so it belongs with
                 -- the technical declines rather than in its own column.
                 100.0 * sum(CASE WHEN failure_bucket IN ('technical','timeout')
                                  THEN 1 ELSE 0 END) / count(*) AS tech_pct,
                 100.0 * sum(CASE WHEN failure_bucket='business'
                                  THEN 1 ELSE 0 END) / count(*) AS biz_pct,
                 -- Risk declines are policy rejections (fraud rules, velocity
                 -- limits), not faults and not the customer's balance. They had
                 -- no column in the previous schema and were silently dropped,
                 -- so the decline splits never summed to the day.
                 100.0 * sum(CASE WHEN failure_bucket='risk'
                                  THEN 1 ELSE 0 END) / count(*) AS risk_pct,
                 100.0 * sum(CASE WHEN status='PENDING' THEN 1 ELSE 0 END)
                       / count(*)           AS pending_pct
          FROM attempts GROUP BY day, txn_date
        ),
        pk AS (
          SELECT day, hour, count(*) n,
                 row_number() OVER (PARTITION BY day
                                    ORDER BY count(*) DESC, hour) rk
          FROM attempts GROUP BY day, hour
        ),
        med AS (SELECT median(attempts) m FROM d)
        SELECT d.day, d.txn_date,
               CASE
                 -- Evidence-derived. Order matters: the most decision-relevant
                 -- fact about a day wins the label.
                 WHEN d.success_rate < 97.5 THEN 'Incident-affected day'
                 WHEN d.attempts > (SELECT m FROM med) * 1.25
                      THEN 'High-volume campaign day'
                 WHEN d.calendar_event IS NOT NULL
                      THEN 'Calendar event: ' || d.calendar_event
                 WHEN d.dow = 6 THEN 'Sunday (quiet)'
                 WHEN d.dow = 5 THEN 'Saturday (lighter)'
                 WHEN d.dow = 0 THEN 'Monday (ramp-up)'
                 WHEN dayofmonth(d.txn_date::DATE) >= 26
                      OR dayofmonth(d.txn_date::DATE) <= 3
                      THEN 'Month-end peak'
                 ELSE 'Weekday (steady)'
               END AS archetype,
               d.attempts, round(d.value_inr, 2),
               round(d.value_inr / nullif(d.attempts, 0), 2),
               round(d.success_rate, 2), round(d.tech_pct, 2),
               round(d.biz_pct, 2), round(d.pending_pct, 2),
               (SELECT hour FROM pk WHERE pk.day = d.day AND pk.rk = 1),
               round(d.attempts * {NATIONAL_SCALE_M_PER_TXN}, 1),
               d.active_customers, round(d.risk_pct, 2)
        FROM d ORDER BY d.day
        """
        # risk_decline_pct is appended rather than inserted: consumers read
        # these cubes with csv.DictReader, so a new trailing column is additive
        # and existing readers are unaffected.
        return self._write(con, "daily_metrics", sql, [
            "day", "date", "archetype", "sample_txns", "sample_value_inr",
            "avg_ticket_inr", "success_rate", "technical_decline_pct",
            "business_decline_pct", "pending_pct", "peak_hour",
            "volume_millions", "active_customers_sample", "risk_decline_pct"])

    # ------------------------------------------------------- entity × day
    def _entity_daily(self, con, name: str, column: str,
                      label: str) -> CubeResult:
        sql = f"""
        SELECT {column} AS entity, day, count(*) AS txns,
               round(sum(amount_inr), 2) AS value,
               round(100.0 * sum(CASE WHEN status='SUCCESS' THEN 1 ELSE 0 END)
                     / count(*), 2) AS success_rate
        FROM attempts WHERE {column} IS NOT NULL
        GROUP BY 1, 2 ORDER BY 1, 2
        """
        return self._write(con, name, sql,
                           [label, "day", "txns", "value", "success_rate"])

    def _merchant_daily(self, con) -> CubeResult:
        """Top-``TOP_MERCHANTS`` merchants by window volume, per day.

        Bounded on purpose — see the constant. The cut is taken on total
        attempts across the whole window rather than per day, so a merchant
        does not flicker in and out of the series and week-over-week
        comparisons stay on a stable panel.
        """
        sql = f"""
        WITH top AS (
          SELECT merchant_name FROM attempts WHERE merchant_name IS NOT NULL
          GROUP BY 1 ORDER BY count(*) DESC, merchant_name LIMIT {TOP_MERCHANTS}
        )
        SELECT a.merchant_name, a.day, count(*) AS txns,
               round(sum(a.amount_inr), 2) AS value,
               min(a.mcc_category) AS category,
               round(100.0 * sum(CASE WHEN a.status='SUCCESS' THEN 1 ELSE 0 END)
                     / count(*), 2) AS success_rate
        FROM attempts a JOIN top ON top.merchant_name = a.merchant_name
        GROUP BY 1, 2 ORDER BY 1, 2
        """
        return self._write(con, "merchant_daily", sql,
                           ["merchant", "day", "txns", "value", "category",
                            "success_rate"])

    def _city_daily(self, con) -> CubeResult:
        sql = """
        SELECT city, day, count(*) AS txns, round(sum(amount_inr), 2) AS value,
               min(state) AS state
        FROM attempts WHERE city IS NOT NULL
        GROUP BY 1, 2 ORDER BY 1, 2
        """
        return self._write(con, "city_daily", sql,
                           ["city", "day", "txns", "value", "state"])

    # ------------------------------------------------------------ profiles
    def _hourly(self, con) -> CubeResult:
        return self._write(
            con, "hourly_distribution",
            "SELECT hour, count(*) FROM attempts GROUP BY 1 ORDER BY 1",
            ["hour", "sample_txns"])

    def _mix(self, con) -> CubeResult:
        return self._write(
            con, "transaction_mix",
            """SELECT payment_type, count(*), round(sum(amount_inr), 2)
               FROM attempts GROUP BY 1 ORDER BY 2 DESC""",
            ["payment_type", "sample_txns", "sample_value_inr"])

    def _customer_activity(self, con) -> CubeResult:
        """Distinct actives per day, plus the cumulative reach of the corpus.

        ``cumulative_customers_seen`` is a running count of *first* appearances,
        which is what makes the series monotonic — computing it as a windowed
        distinct over all prior days would be O(n^2) on the corpus.
        """
        sql = """
        WITH first_seen AS (
          SELECT customer_id, min(day) AS first_day
          FROM attempts GROUP BY 1
        ),
        new_per_day AS (
          SELECT first_day AS day, count(*) AS new_customers
          FROM first_seen GROUP BY 1
        ),
        d AS (
          SELECT day, min(txn_date) AS txn_date,
                 count(DISTINCT customer_id) AS actives, count(*) AS txns
          FROM attempts GROUP BY day
        )
        SELECT d.day, d.txn_date, d.actives,
               sum(coalesce(n.new_customers, 0))
                 OVER (ORDER BY d.day ROWS UNBOUNDED PRECEDING),
               round(d.txns * 1.0 / nullif(d.actives, 0), 2)
        FROM d LEFT JOIN new_per_day n ON n.day = d.day
        ORDER BY d.day
        """
        return self._write(con, "customer_activity", sql,
                           ["day", "date", "active_customers_sample",
                            "cumulative_customers_seen", "avg_txns_per_active"])

    # -------------------------------------------------------------- rolling
    def _kpi_rolling(self, con) -> CubeResult:
        """30- and 90-day trailing means for the headline KPIs.

        Windows are expanding until they fill, which is why day 1 equals its own
        raw value rather than being null — consumers plot this series from day 1.
        """
        sql = f"""
        WITH d AS (
          SELECT day, min(txn_date) AS txn_date, count(*) AS attempts,
                 sum(amount_inr) AS value_inr,
                 100.0 * sum(CASE WHEN status='SUCCESS' THEN 1 ELSE 0 END)
                       / count(*) AS success_rate
          FROM attempts GROUP BY day
        ),
        k AS (
          SELECT 'UPI Transactions (M/day)' AS kpi, day, txn_date,
                 round(attempts * {NATIONAL_SCALE_M_PER_TXN}, 2) AS value FROM d
          UNION ALL SELECT 'Success Rate (%)', day, txn_date,
                 round(success_rate, 2) FROM d
          UNION ALL SELECT 'Average Ticket (INR)', day, txn_date,
                 round(value_inr / nullif(attempts, 0), 2) FROM d
          UNION ALL SELECT 'Transaction Value (INR)', day, txn_date,
                 round(value_inr, 2) FROM d
        )
        SELECT kpi, day, txn_date, value,
               round(avg(value) OVER (PARTITION BY kpi ORDER BY day
                     ROWS BETWEEN 29 PRECEDING AND CURRENT ROW), 2),
               round(avg(value) OVER (PARTITION BY kpi ORDER BY day
                     ROWS BETWEEN 89 PRECEDING AND CURRENT ROW), 2)
        FROM k ORDER BY kpi, day
        """
        return self._write(con, "kpi_rolling", sql,
                           ["kpi", "day", "date", "value", "rolling_30",
                            "rolling_90"])

    # --------------------------------------------------------------- trends
    def _trends(self, con) -> CubeResult:
        """The most widely consumed cube — ~30 modules read it.

        One row per series with the comparison window every executive surface
        asks for. ``forecast_next``/``forecast_7d`` are a trailing-drift
        projection, deliberately simple and deliberately labelled: the real
        forecasting lives in the ML pipeline, and a naive baseline here is
        honest about being one.
        """
        sql = """
        WITH base AS (
          SELECT 'total::sample_txns' AS series, day, count(*)::DOUBLE AS v
          FROM attempts GROUP BY day
          UNION ALL SELECT 'total::sample_value_inr', day, sum(amount_inr)
          FROM attempts GROUP BY day
          UNION ALL SELECT 'total::success_rate', day,
                 100.0*sum(CASE WHEN status='SUCCESS' THEN 1 ELSE 0 END)/count(*)
          FROM attempts GROUP BY day
          UNION ALL SELECT 'total::avg_ticket_inr', day,
                 sum(amount_inr)/nullif(count(*),0) FROM attempts GROUP BY day
          UNION ALL SELECT 'feature::' || product_name, day, count(*)::DOUBLE
          FROM attempts GROUP BY product_name, day
          UNION ALL SELECT 'bank::' || payer_bank, day, count(*)::DOUBLE
          FROM attempts GROUP BY payer_bank, day
          UNION ALL SELECT 'psp::' || payer_psp, day, count(*)::DOUBLE
          FROM attempts GROUP BY payer_psp, day
          UNION ALL SELECT 'city::' || city, day, count(*)::DOUBLE
          FROM attempts GROUP BY city, day
        ),
        span AS (SELECT max(day) AS last_day FROM base),
        agg AS (
          SELECT series,
            max(CASE WHEN day = (SELECT last_day FROM span) THEN v END) AS today,
            max(CASE WHEN day = (SELECT last_day FROM span)-1 THEN v END) AS yesterday,
            avg(CASE WHEN day >  (SELECT last_day FROM span)-7  THEN v END) AS last_7d,
            avg(CASE WHEN day >  (SELECT last_day FROM span)-30 THEN v END) AS last_30d,
            avg(CASE WHEN day >  (SELECT last_day FROM span)-14
                      AND day <= (SELECT last_day FROM span)-7 THEN v END) AS prev_7d,
            sum(CASE WHEN day >  (SELECT last_day FROM span)-30 THEN v END) AS mtd,
            avg(v) AS ma_all,
            avg(CASE WHEN day <= 7 THEN v END) AS first_7d
          FROM base GROUP BY series
        )
        SELECT series, round(today,2), round(yesterday,2), round(last_7d,2),
               round(last_30d,2),
               round(100.0*(last_7d-prev_7d)/nullif(abs(prev_7d),0), 2),
               round(mtd,2), round(last_7d,2), round(ma_all,2),
               round(100.0*(last_7d-first_7d)/nullif(abs(first_7d),0), 2),
               -- naive drift: last week's level carried forward by its own
               -- week-over-week slope, clamped to one week of extrapolation
               round(last_7d + (last_7d-prev_7d)/7.0, 2),
               round(7.0*last_7d + (last_7d-prev_7d), 2)
        FROM agg ORDER BY series
        """
        return self._write(con, "trends", sql, [
            "series", "today", "yesterday", "last_7d", "last_30d",
            "wow_change", "mtd", "ma_7d", "ma_all", "growth_pct",
            "forecast_next", "forecast_7d"])


def _fmt(v: Any) -> Any:
    if isinstance(v, date):
        return v.isoformat()
    if v is None:
        return ""
    return v


# ---------------------------------------------------------------------------
# The KPI workbook.
#
# ``master/upi_kpis_month.xlsx`` is the source ``EnterpriseReader`` loads for
# the executive KPI surfaces (/executive/trends, /executive/kpis,
# week-over-week, month-over-month, the brief and report trend rows). It was
# written by the same asserted-KPI engine that produced the old cubes and
# carried the same disagreement with the corpus (r = +0.20 on success rate).
#
# Only the rows a transaction can actually answer are rewritten. Metrics owned
# by other subsystems — complaints, fraud alerts, adoption counts, risk score —
# are left exactly as they are, because inventing them from payment rows would
# replace an honest external number with a fabricated one.
KPI_FROM_CORPUS: dict[str, str] = {
    "UPI Transactions (M/day)": "volume_m",
    "Success Rate (%)": "success_rate",
    "Technical Declines (%)": "technical_pct",
    "Business Declines (%)": "business_pct",
    "Response Time (ms)": "latency_ms",
    "Active Banks": "active_banks",
    "Active PSPs": "active_psps",
}


def corpus_kpi_series(warehouse_root: str | Path) -> dict[str, list[float]]:
    """Daily series for every corpus-derivable KPI, ordered by date."""
    if not _DUCKDB:
        raise RuntimeError("duckdb is required to project KPI series")
    txns = str(Path(warehouse_root) / "transactions" / "*.parquet")
    con = duckdb.connect()
    rows = con.execute(f"""
        SELECT txn_date,
               count(*)                                       AS attempts,
               100.0*sum(CASE WHEN status='SUCCESS' THEN 1 ELSE 0 END)
                    /count(*)                                 AS success_rate,
               100.0*sum(CASE WHEN failure_bucket IN ('technical','timeout')
                              THEN 1 ELSE 0 END)/count(*)     AS technical_pct,
               100.0*sum(CASE WHEN failure_bucket='business'
                              THEN 1 ELSE 0 END)/count(*)     AS business_pct,
               avg(latency_ms)                                AS latency_ms,
               count(DISTINCT payer_bank)                     AS active_banks,
               count(DISTINCT payer_psp)                      AS active_psps
        FROM read_parquet('{txns}')
        WHERE txn_type IN ({_ATTEMPTS})
        GROUP BY 1 ORDER BY 1
    """).fetchall()
    con.close()
    return {
        "volume_m": [round(r[1] * NATIONAL_SCALE_M_PER_TXN, 1) for r in rows],
        "success_rate": [round(r[2], 2) for r in rows],
        "technical_pct": [round(r[3], 2) for r in rows],
        "business_pct": [round(r[4], 2) for r in rows],
        "latency_ms": [int(round(r[5])) for r in rows],
        "active_banks": [int(r[6]) for r in rows],
        "active_psps": [int(r[7]) for r in rows],
    }


def project_kpi_workbook(warehouse_root: str | Path,
                         workbook: str | Path) -> dict[str, int]:
    """Rewrite the corpus-derivable KPI rows of the month workbook in place.

    Returns {kpi: days_written}. Rows outside :data:`KPI_FROM_CORPUS` and every
    other sheet are untouched, so this is additive to the workbook rather than a
    regeneration of it.
    """
    try:
        import openpyxl
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError("openpyxl is required to project the KPI workbook"
                           ) from exc

    path = Path(workbook)
    series = corpus_kpi_series(warehouse_root)
    wb = openpyxl.load_workbook(path)
    if "Monthly KPIs" not in wb.sheetnames:
        raise RuntimeError(f"{path.name} has no 'Monthly KPIs' sheet")
    ws = wb["Monthly KPIs"]

    written: dict[str, int] = {}
    for row in ws.iter_rows(min_row=2):
        name = row[0].value
        key = KPI_FROM_CORPUS.get(str(name) if name is not None else "")
        if not key:
            continue
        values = series[key]
        # Column 0 is the KPI name and column 1 its unit; the daily series
        # starts at column 2 and must not be allowed to run past the columns
        # the sheet actually has.
        span = min(len(values), len(row) - 2)
        for i in range(span):
            row[2 + i].value = values[i]
        written[str(name)] = span
    wb.save(path)
    logger.info("projected %d KPI rows in %s", len(written), path.name)
    return written
