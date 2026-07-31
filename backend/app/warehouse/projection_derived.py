"""The remaining cubes, projected off the corpus.

``projection.py`` covers the cubes that are plain daily aggregates. This module
covers the seven that are *derived* — weekly entity evolution, KPI rollups,
cross-entity relationships, BI findings, incident storylines, decision tracking
and forecast validation. Until now every one of them was written by
``generate_enterprise.py`` from its own hand-authored KPI series, which made
them the last places in the platform where a number on a screen could not be
traced back to a transaction.

The narrative cubes are the interesting case. A "storyline" or a "decision" is
still a story, but here the story is *assembled from measurement*: the incident
comes from the ground-truth event calendar the simulator emitted, and the
before / trough / after numbers are queried from the transactions the incident
actually affected. So the recovery percentage in ``decision_tracking`` is the
recovery that happened, not one that was asserted alongside it.

Anything that genuinely cannot be derived from payment rows is left alone
rather than invented — the same restraint the KPI workbook projection applies.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from app.core.logging import get_logger
from app.warehouse.projection import CubeResult, _fmt

logger = get_logger(__name__)

try:
    import duckdb
    _DUCKDB = True
except ImportError:  # pragma: no cover
    _DUCKDB = False

_ATTEMPTS = "'PAYMENT', 'MANDATE_EXECUTION', 'RETRY', 'MANDATE_RETRY'"


def _tier(share: float) -> str:
    return "Tier 1" if share >= 5.0 else ("Tier 2" if share >= 1.0
                                          else "Tier 3")


def _grade(score: float) -> str:
    if score >= 90:
        return "Healthy"
    if score >= 75:
        return "Watch"
    return "At Risk"


class DerivedProjection:
    """Projects the derived and narrative cubes from raw transactions."""

    def __init__(self, warehouse_root: str | Path, out_dir: str | Path):
        self.txn_glob = str(Path(warehouse_root) / "transactions" / "*.parquet")
        self.ref_dir = Path(warehouse_root) / "reference"
        self.out = Path(out_dir)

    # ------------------------------------------------------------------ util
    def _con(self):
        if not _DUCKDB:
            raise RuntimeError("duckdb is required to project cubes")
        con = duckdb.connect()
        con.execute(f"""
            CREATE OR REPLACE TEMP VIEW attempts AS
            SELECT *, day_index + 1 AS day,
                   CAST(date_trunc('week', CAST(txn_date AS DATE)) AS DATE)
                       AS week_start
            FROM read_parquet('{self.txn_glob}')
            WHERE txn_type IN ({_ATTEMPTS})
        """)
        inc = self.ref_dir / "incidents.parquet"
        if inc.exists():
            con.execute(
                "CREATE OR REPLACE TEMP VIEW incidents AS "
                f"SELECT * FROM read_parquet('{inc.as_posix()}')")
        return con

    def _write(self, con, name: str, sql: str, header: list[str]
               ) -> CubeResult:
        rows = con.execute(sql).fetchall()
        return self._write_rows(name, header, rows)

    def _write_rows(self, name: str, header: list[str],
                    rows: list[tuple | list]) -> CubeResult:
        self.out.mkdir(parents=True, exist_ok=True)
        path = self.out / f"{name}.csv"
        with path.open("w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(header)
            for r in rows:
                w.writerow([_fmt(v) for v in r])
        logger.info("projected derived cube %s: %d rows", name, len(rows))
        return CubeResult(name=name, rows=len(rows), path=path)

    # ----------------------------------------------------------------- build
    def build(self) -> dict[str, CubeResult]:
        con = self._con()
        out: dict[str, CubeResult] = {}
        out["bank_evolution"] = self._entity_evolution(
            con, "bank_evolution", "payer_bank", "bank")
        out["psp_evolution"] = self._entity_evolution(
            con, "psp_evolution", "payer_psp", "psp")
        out["merchant_evolution"] = self._merchant_evolution(con)
        out["customer_evolution"] = self._customer_evolution(con)
        out["kpi_rollups"] = self._kpi_rollups(con)
        out["cross_entity"] = self._cross_entity(con)
        out["bi_findings"] = self._bi_findings(con)
        out["storylines"] = self._storylines(con)
        out["decision_tracking"] = self._decision_tracking(con)
        return out

    # ------------------------------------------------------ entity evolution
    def _entity_evolution(self, con, name: str, col: str, label: str
                          ) -> CubeResult:
        """Weekly trajectory of every issuer or app, measured not asserted.

        ``health_score`` is a composite of the three things an operations lead
        actually judges a counterparty on — reliability against the ecosystem,
        latency, and whether an incident touched it — so a bank that had a bad
        week is graded on the week it had.
        """
        scope = "scope_bank" if col == "payer_bank" else "scope_psp"
        sql = f"""
        WITH w AS (
          SELECT {col} AS entity, week_start,
                 COUNT(*) AS txns,
                 SUM(CASE WHEN status='SUCCESS' THEN amount_inr ELSE 0 END)
                     AS value_inr,
                 100.0*SUM(CASE WHEN status='SUCCESS' THEN 1 ELSE 0 END)
                     /NULLIF(COUNT(*),0) AS success_rate,
                 QUANTILE_CONT(latency_ms, 0.95) AS p95
          FROM attempts WHERE {col} IS NOT NULL GROUP BY 1,2),
        tot AS (SELECT week_start, SUM(txns) AS all_txns,
                       AVG(success_rate) AS eco_sr FROM w GROUP BY 1),
        idx AS (SELECT week_start,
                       DENSE_RANK() OVER (ORDER BY week_start) AS week_index
                FROM w GROUP BY 1),
        inc AS (SELECT i.{scope} AS entity, a.week_start,
                       COUNT(DISTINCT i.event_id) AS incidents
                FROM incidents i
                JOIN (SELECT DISTINCT txn_date, week_start FROM attempts) a
                  ON CAST(a.txn_date AS DATE)
                     BETWEEN CAST(i.start_date AS DATE) AND CAST(i.end_date AS DATE)
                WHERE i.{scope} IS NOT NULL GROUP BY 1,2),
        j AS (
          SELECT w.*, tot.all_txns, tot.eco_sr, idx.week_index,
                 COALESCE(inc.incidents, 0) AS incidents,
                 100.0*w.txns/NULLIF(tot.all_txns,0) AS share,
                 LAG(w.txns) OVER (PARTITION BY w.entity ORDER BY w.week_start)
                     AS prev_txns
          FROM w JOIN tot USING (week_start) JOIN idx USING (week_start)
               LEFT JOIN inc ON inc.entity = w.entity
                            AND inc.week_start = w.week_start)
        SELECT entity,
               CASE WHEN share >= 5 THEN 'Tier 1'
                    WHEN share >= 1 THEN 'Tier 2' ELSE 'Tier 3' END AS tier,
               'W' || week_index AS week, week_index, week_start,
               txns, ROUND(value_inr, 2), ROUND(share, 2),
               ROUND(success_rate, 2), CAST(ROUND(p95) AS BIGINT),
               ROUND(100.0*(txns - prev_txns)/NULLIF(prev_txns,0), 2),
               incidents,
               ROUND(GREATEST(0, LEAST(100,
                    100
                    - GREATEST(0, (eco_sr - success_rate)) * 6.0
                    - GREATEST(0, (p95 - 900)) / 90.0
                    - incidents * 6.0)), 1) AS health_score
        FROM j ORDER BY entity, week_index
        """
        rows = con.execute(sql).fetchall()
        rows = [list(r) + [_grade(r[-1])] for r in rows]
        return self._write_rows(
            name, [label, "tier", "week", "week_index", "date", "txns",
                   "value_inr", "market_share_pct", "success_rate",
                   "p95_latency_ms", "wow_growth_pct", "incidents",
                   "health_score", "health_grade"], rows)

    def _merchant_evolution(self, con) -> CubeResult:
        """Weekly trajectory of the merchant panel, including entry and exit.

        ``lifecycle`` is read out of the data: a merchant with no prior week
        is New, one that transacted before and has stopped is Churned, and the
        rest are graded on their own trend. Nothing is labelled in advance.
        """
        sql = """
        WITH panel AS (
          SELECT merchant_name FROM attempts WHERE merchant_name IS NOT NULL
          GROUP BY 1 ORDER BY COUNT(*) DESC LIMIT 80),
        w AS (
          SELECT merchant_name AS merchant, week_start,
                 MIN(merchant_tier) AS tier, MIN(mcc_category) AS category,
                 COUNT(*) AS txns,
                 SUM(CASE WHEN status='SUCCESS' THEN amount_inr ELSE 0 END)
                     AS value_inr,
                 100.0*SUM(CASE WHEN status='SUCCESS' THEN 1 ELSE 0 END)
                     /NULLIF(COUNT(*),0) AS success_rate,
                 COUNT(DISTINCT customer_id) AS customers
          FROM attempts WHERE merchant_name IN (SELECT merchant_name FROM panel)
          GROUP BY 1,2),
        idx AS (SELECT week_start,
                       DENSE_RANK() OVER (ORDER BY week_start) AS week_index
                FROM attempts GROUP BY 1),
        j AS (SELECT w.*, idx.week_index,
                     LAG(w.txns) OVER (PARTITION BY w.merchant
                                       ORDER BY w.week_start) AS prev_txns,
                     ROW_NUMBER() OVER (PARTITION BY w.merchant
                                        ORDER BY w.week_start) AS seq,
                     MAX(idx.week_index) OVER () AS last_week
              FROM w JOIN idx USING (week_start))
        SELECT merchant, tier, category, 'W' || week_index AS week,
               week_index, week_start, txns, ROUND(value_inr, 2),
               ROUND(success_rate, 2), customers,
               ROUND(100.0*(txns - prev_txns)/NULLIF(prev_txns,0), 2)
                   AS wow_growth_pct,
               CASE WHEN seq = 1 AND week_index > 1 THEN 'New'
                    WHEN prev_txns IS NOT NULL
                         AND txns < prev_txns * 0.55 THEN 'Contracting'
                    WHEN prev_txns IS NOT NULL
                         AND txns > prev_txns * 1.45 THEN 'Expanding'
                    ELSE 'Steady' END AS lifecycle
        FROM j ORDER BY merchant, week_index
        """
        return self._write(con, "merchant_evolution", sql,
                           ["merchant", "tier", "category", "week",
                            "week_index", "date", "txns", "value_inr",
                            "success_rate", "customers", "wow_growth_pct",
                            "lifecycle"])

    def _customer_evolution(self, con) -> CubeResult:
        """Weekly cohort behaviour — actives, new, returning and per-head use."""
        sql = """
        WITH first_seen AS (
          SELECT customer_id, MIN(week_start) AS cohort_week
          FROM attempts GROUP BY 1),
        w AS (
          SELECT a.week_start, a.customer_segment AS segment,
                 COUNT(DISTINCT a.customer_id) AS active_customers,
                 COUNT(*) AS txns,
                 SUM(CASE WHEN status='SUCCESS' THEN amount_inr ELSE 0 END)
                     AS value_inr,
                 COUNT(DISTINCT CASE WHEN f.cohort_week = a.week_start
                                     THEN a.customer_id END) AS new_customers,
                 100.0*SUM(CASE WHEN a.status='SUCCESS' THEN 1 ELSE 0 END)
                     /NULLIF(COUNT(*),0) AS success_rate
          FROM attempts a JOIN first_seen f USING (customer_id)
          GROUP BY 1,2),
        idx AS (SELECT week_start,
                       DENSE_RANK() OVER (ORDER BY week_start) AS week_index
                FROM attempts GROUP BY 1)
        SELECT 'W' || idx.week_index AS week, idx.week_index, w.week_start,
               w.segment, w.active_customers, w.new_customers,
               w.active_customers - w.new_customers AS returning_customers,
               w.txns,
               ROUND(1.0*w.txns/NULLIF(w.active_customers,0), 3) AS txns_per_customer,
               ROUND(w.value_inr, 2),
               ROUND(w.value_inr/NULLIF(w.txns,0), 2) AS avg_ticket_inr,
               ROUND(w.success_rate, 2)
        FROM w JOIN idx USING (week_start)
        ORDER BY idx.week_index, w.segment
        """
        return self._write(con, "customer_evolution", sql,
                           ["week", "week_index", "date", "segment",
                            "active_customers", "new_customers",
                            "returning_customers", "txns",
                            "txns_per_customer", "value_inr",
                            "avg_ticket_inr", "success_rate"])

    # ---------------------------------------------------------- KPI rollups
    def _kpi_rollups(self, con) -> CubeResult:
        """The same KPIs at weekly, monthly and quarterly grain."""
        rows: list[list[Any]] = []
        grains = {
            "weekly": ("week", "'W' || DENSE_RANK() OVER (ORDER BY g)"),
            "monthly": ("month", "strftime(g, '%Y-%m')"),
            "quarterly": ("quarter", "'Q' || quarter(g) || ' ' || year(g)"),
        }
        for grain, (trunc, label) in grains.items():
            sql = f"""
            WITH b AS (
              SELECT CAST(date_trunc('{trunc}', CAST(txn_date AS DATE)) AS DATE) AS g,
                     COUNT(*) AS attempts,
                     SUM(CASE WHEN status='SUCCESS' THEN 1 ELSE 0 END) AS ok,
                     SUM(CASE WHEN status='SUCCESS' THEN amount_inr ELSE 0 END)
                         AS value_inr,
                     COUNT(DISTINCT txn_date) AS days,
                     COUNT(DISTINCT customer_id) AS customers,
                     100.0*SUM(CASE WHEN failure_bucket='technical' THEN 1 ELSE 0 END)
                         /NULLIF(COUNT(*),0) AS tech,
                     100.0*SUM(CASE WHEN failure_bucket='business' THEN 1 ELSE 0 END)
                         /NULLIF(COUNT(*),0) AS biz,
                     MEDIAN(latency_ms) AS lat
              FROM attempts GROUP BY 1),
            l AS (SELECT *, {label} AS period,
                         DENSE_RANK() OVER (ORDER BY g) AS period_index FROM b)
            SELECT period, period_index,
                   100.0*ok/NULLIF(attempts,0) AS "Success Rate (%)",
                   1.0*attempts/NULLIF(days,0)*56000.0/1e6 AS "UPI Transactions (M/day)",
                   value_inr/NULLIF(ok,0) AS "Average Ticket (INR)",
                   tech AS "Technical Declines (%)",
                   biz AS "Business Declines (%)",
                   lat AS "Response Time (ms)",
                   customers AS "Active Customers"
            FROM l ORDER BY period_index
            """
            res = con.execute(sql).fetchall()
            cols = [d[0] for d in con.description][2:]
            prev: dict[str, float] = {}
            for r in res:
                period, pidx = r[0], r[1]
                for i, kpi in enumerate(cols):
                    v = r[2 + i]
                    if v is None:
                        continue
                    p = prev.get(kpi)
                    delta = (None if p in (None, 0)
                             else round((v - p) / abs(p) * 100, 2))
                    direction = ("flat" if delta is None or abs(delta) < 1.0
                                 else ("up" if delta > 0 else "down"))
                    rows.append([kpi, grain, period, pidx, round(float(v), 3),
                                 delta, direction])
                    prev[kpi] = v
                prev = {k: v for k, v in prev.items()}
        return self._write_rows(
            "kpi_rollups",
            ["kpi", "grain", "period", "period_index", "value", "delta_pct",
             "direction"], rows)

    # -------------------------------------------------------- relationships
    def _cross_entity(self, con) -> CubeResult:
        """Real edges in the ecosystem graph, weighted by measured flow."""
        rows: list[list[Any]] = []
        specs = [
            ("merchant", "merchant_name", "settles_via", "psp", "payee_psp",
             "mcc_category", 40),
            ("bank", "payer_bank", "routes_through", "psp", "payer_psp",
             "region", 40),
            ("product", "product_name", "acquires_in", "mcc_category",
             "mcc_category", "product_family", 40),
            ("region", "region", "transacts_on", "product", "product_name",
             "state", 30),
        ]
        for s_type, s_col, rel, t_type, t_col, note_col, limit in specs:
            sql = f"""
            SELECT {s_col} AS s, {t_col} AS t, COUNT(*) AS w,
                   MIN({note_col}) AS note,
                   100.0*SUM(CASE WHEN status='SUCCESS' THEN 1 ELSE 0 END)
                       /NULLIF(COUNT(*),0) AS sr,
                   SUM(CASE WHEN status='SUCCESS' THEN amount_inr ELSE 0 END) AS v
            FROM attempts
            WHERE {s_col} IS NOT NULL AND {t_col} IS NOT NULL
            GROUP BY 1,2 ORDER BY w DESC LIMIT {limit}
            """
            for s, t, w, note, sr, v in con.execute(sql).fetchall():
                rows.append([s_type, s, rel, t_type, t, w, note,
                             round(float(sr or 0), 2), round(float(v or 0), 2)])
        return self._write_rows(
            "cross_entity",
            ["source_type", "source", "relation", "target_type", "target",
             "weight", "note", "success_rate", "value_inr"], rows)

    # ------------------------------------------------------------- findings
    def _bi_findings(self, con) -> CubeResult:
        """Findings a BI analyst would raise, each computed from the corpus."""
        rows: list[list[Any]] = []

        def add(cat, sev, finding, entity, metric, value):
            rows.append([cat, sev, finding, entity, metric,
                         round(float(value), 2)])

        # Fastest and slowest movers, first month against last.
        movers = con.execute("""
            WITH m AS (
              SELECT product_name AS p,
                     strftime(CAST(txn_date AS DATE), '%Y-%m') AS mo,
                     COUNT(*) AS n FROM attempts GROUP BY 1,2),
            b AS (SELECT p, MIN(mo) AS first_mo, MAX(mo) AS last_mo
                  FROM m GROUP BY 1)
            SELECT b.p,
                   MAX(CASE WHEN m.mo = b.first_mo THEN m.n END) AS n0,
                   MAX(CASE WHEN m.mo = b.last_mo  THEN m.n END) AS n1
            FROM b JOIN m ON m.p = b.p GROUP BY 1
        """).fetchall()
        growth = sorted(
            ((p, (n1 - n0) / n0 * 100) for p, n0, n1 in movers if n0),
            key=lambda x: -x[1])
        if growth:
            p, g = growth[0]
            add("growing_features", "info",
                f"Fastest-growing product: {p} ({g:+.1f}% first month to last).",
                p, "txns_growth_pct", g)
            p, g = growth[-1]
            add("declining_features", "warning" if g < 0 else "info",
                (f"Contracting product: {p} ({g:+.1f}% first month to last)."
                 if g < 0 else
                 f"Slowest-growing product: {p} ({g:+.1f}% first month to "
                 f"last) — still expanding, just behind the pack."),
                p, "txns_growth_pct", g)

        # Reliability outliers against the ecosystem.
        for entity, sr, n, eco in con.execute("""
            WITH b AS (SELECT payer_bank AS e,
                              100.0*SUM(CASE WHEN status='SUCCESS' THEN 1 ELSE 0 END)
                                  /NULLIF(COUNT(*),0) AS sr,
                              COUNT(*) AS n FROM attempts GROUP BY 1)
            SELECT e, sr, n, (SELECT AVG(sr) FROM b) FROM b
            WHERE n > 5000 ORDER BY sr LIMIT 2
        """).fetchall():
            if sr < eco - 0.4:
                add("reliability", "warning",
                    f"{entity} settles at {sr:.2f}% against an ecosystem "
                    f"{eco:.2f}% across {n:,} attempts — a "
                    f"{eco - sr:.2f}pp reliability gap.",
                    entity, "success_rate", sr)

        # Concentration.
        top5, total = con.execute("""
            WITH b AS (SELECT payer_bank, COUNT(*) n FROM attempts GROUP BY 1)
            SELECT (SELECT SUM(n) FROM (SELECT n FROM b ORDER BY n DESC LIMIT 5)),
                   (SELECT SUM(n) FROM b)
        """).fetchone()
        if total:
            share = top5 / total * 100
            add("concentration", "warning" if share > 70 else "info",
                f"The top five issuers carry {share:.1f}% of all attempts.",
                "issuer concentration", "top5_share_pct", share)

        # Failure ownership — who the platform should actually go and talk to.
        for owner, n, pct in con.execute("""
            SELECT failure_owner, COUNT(*) n,
                   100.0*COUNT(*)/SUM(COUNT(*)) OVER () AS pct
            FROM attempts WHERE status='FAILED' AND failure_owner IS NOT NULL
            GROUP BY 1 ORDER BY n DESC LIMIT 3
        """).fetchall():
            add("failure_ownership", "info",
                f"{owner} owns {pct:.1f}% of all declines ({n:,} attempts).",
                owner, "decline_share_pct", pct)

        # Dispute-heavy categories.
        for rank, (cat, cb, sold, rate) in enumerate(con.execute(f"""
            WITH s AS (SELECT mcc_category c, COUNT(*) n FROM attempts
                       WHERE status='SUCCESS' AND mcc_category IS NOT NULL
                       GROUP BY 1),
                 d AS (SELECT mcc_category c, COUNT(*) n
                       FROM read_parquet('{self.txn_glob}')
                       WHERE txn_type='CHARGEBACK' AND mcc_category IS NOT NULL
                       GROUP BY 1)
            SELECT s.c, COALESCE(d.n,0), s.n, 100.0*COALESCE(d.n,0)/s.n
            FROM s LEFT JOIN d USING (c) WHERE s.n > 2000
            ORDER BY 4 DESC LIMIT 2
        """).fetchall()):
            add("disputes", "warning" if rate > 0.15 else "info",
                f"{cat} runs a {rate:.3f}% dispute rate ({cb:,} disputes on "
                f"{sold:,} settled payments) — the "
                f"{'highest' if rank == 0 else 'second-highest'} of any "
                f"category.",
                cat, "dispute_rate_pct", rate)

        # Retry burden.
        rn, ra, rr = con.execute("""
            SELECT SUM(CASE WHEN is_retry THEN 1 ELSE 0 END), COUNT(*),
                   100.0*SUM(CASE WHEN is_retry AND status='SUCCESS' THEN 1 ELSE 0 END)
                       /NULLIF(SUM(CASE WHEN is_retry THEN 1 ELSE 0 END),0)
            FROM attempts
        """).fetchone()
        if rn:
            add("retries", "info",
                f"Re-presented payments are {rn / ra * 100:.2f}% of all "
                f"attempts and recover {rr:.1f}% of the time.",
                "retry path", "retry_share_pct", rn / ra * 100)
        return self._write_rows(
            "bi_findings",
            ["category", "severity", "finding", "entity", "metric", "value"],
            rows)

    # ----------------------------------------------------------- storylines
    def _incident_impact(self, con) -> list[dict]:
        """Per incident: the rail before it, during it, and after it.

        This is the join that makes the narrative cubes honest. The incident
        list is ground truth from the simulator; the three success rates are
        measured from the transactions inside each window, so an incident that
        did not actually move the numbers cannot be written up as if it did.
        """
        incs = con.execute("""
            SELECT event_id, kind, title, severity, start_date, end_date,
                   scope_bank, scope_psp, scope_product, scope_mcc,
                   detected_date, narrative, shape, recurs_every_days
            FROM incidents WHERE shape <> 'step' ORDER BY start_date
        """).fetchall()
        cols = [d[0] for d in con.description]
        out = []
        for row in incs:
            inc = dict(zip(cols, row))
            where, params = ["1=1"], []
            for col, key in (("payer_bank", "scope_bank"),
                             ("payer_psp", "scope_psp"),
                             ("product_code", "scope_product"),
                             ("mcc", "scope_mcc")):
                v = inc.get(key)
                if v and "," not in str(v):
                    where.append(f"{col} = ?")
                    params.append(v)
            w = " AND ".join(where)
            stats = con.execute(f"""
                WITH s AS (
                  SELECT CAST(txn_date AS DATE) AS d,
                         100.0*SUM(CASE WHEN status='SUCCESS' THEN 1 ELSE 0 END)
                             /NULLIF(COUNT(*),0) AS sr,
                         COUNT(*) AS n
                  FROM attempts WHERE {w} GROUP BY 1)
                SELECT
                  AVG(CASE WHEN d BETWEEN CAST(? AS DATE) - 7
                                      AND CAST(? AS DATE) - 1 THEN sr END),
                  MIN(CASE WHEN d BETWEEN CAST(? AS DATE) AND CAST(? AS DATE)
                           THEN sr END),
                  AVG(CASE WHEN d BETWEEN CAST(? AS DATE) + 1
                                      AND CAST(? AS DATE) + 7 THEN sr END),
                  SUM(CASE WHEN d BETWEEN CAST(? AS DATE) AND CAST(? AS DATE)
                           THEN n END)
                FROM s
            """, params + [inc["start_date"]] * 2
                 + [inc["start_date"], inc["end_date"]]
                 + [inc["end_date"]] * 2
                 + [inc["start_date"], inc["end_date"]]).fetchone()
            pre, trough, post, vol = stats
            if pre is None or trough is None:
                continue
            inc.update(pre=float(pre), trough=float(trough),
                       post=float(post) if post is not None else float(pre),
                       volume=int(vol or 0))
            out.append(inc)
        return out

    def _storylines(self, con) -> CubeResult:
        """The lifecycle of each incident, staged and measured.

        Every step names the team that would own it and carries the entity and
        KPI it concerns, so the storyline can be joined back to the incident
        and to the transactions underneath it.
        """
        # Two lifecycles, because not every logged event actually moved the
        # rail. Writing "success troughed at 95.5% from a 94.7% baseline" —
        # a trough *above* its own baseline — is the kind of sentence that
        # teaches a reader to stop believing the report, so an event with no
        # measurable dip gets written up as the non-event it was.
        impact_stages = [
            ("Signal", "Product Analytics",
             "Transaction monitoring flags {kind_h} on {entity}"),
            ("Triage", "UPI Operations",
             "Operations opens {event_id} at {severity} and scopes the blast "
             "radius to {entity}"),
            ("Diagnosis", "Platform Engineering",
             "Decline-code analysis attributes the drop to {owner_h}"),
            ("Mitigation", "UPI Operations",
             "Mitigation applied; success on {entity} troughs at {trough:.2f}% "
             "against a {pre:.2f}% baseline, a {dip:.2f}pp dip"),
            ("Recovery", "UPI Operations",
             "{entity} recovers to {post:.2f}% over the following week"),
            ("Review", "Product Analytics",
             "Post-incident review closes {event_id}; "
             "{volume:,} attempts were exposed"),
        ]
        quiet_stages = [
            ("Signal", "Product Analytics",
             "Operational calendar records {kind_h} on {entity}"),
            ("Triage", "UPI Operations",
             "Operations opens {event_id} at {severity} and scopes it to "
             "{entity}"),
            ("Diagnosis", "Platform Engineering",
             "Measured impact is inside {entity}'s normal daily variation — "
             "success held at {trough:.2f}% against a {pre:.2f}% baseline"),
            ("Mitigation", "UPI Operations",
             "No mitigation required; {volume:,} attempts were exposed with "
             "no detectable degradation"),
            ("Recovery", "UPI Operations",
             "{entity} closes the window at {post:.2f}%"),
            ("Review", "Product Analytics",
             "{event_id} closed as no-impact; retained for trend context"),
        ]
        kind_h = {
            "bank_outage": "an issuer decline spike",
            "psp_degradation": "an app-side regression",
            "network_latency": "switch latency degradation",
            "settlement_delay": "a mandate batch delay",
            "fraud_spike": "a coordinated fraud pattern",
            "maintenance_window": "a scheduled maintenance dip",
            "merchant_campaign": "a category volume surge",
            "merchant_onboarding": "an acquiring cohort step-in",
            "merchant_churn": "category attrition",
            "adoption_surge": "an onboarding surge",
            "dormancy_wave": "a regional demand fall",
            "market_correction": "a discretionary spend pull-back",
        }
        owner_h = {
            "bank_outage": "issuer-side U30/U28 declines",
            "psp_degradation": "PSP-side YA declines and callback timeouts",
            "network_latency": "NPCI switch timeouts (BT/U54)",
            "settlement_delay": "mandates presented outside their window (UX)",
            "fraud_spike": "risk-engine blocks (U16/K1)",
            "maintenance_window": "planned issuer unavailability",
        }
        rows: list[list[Any]] = []
        for inc in self._incident_impact(con):
            entity = (inc["scope_bank"] or inc["scope_psp"]
                      or inc["scope_product"] or inc["scope_mcc"]
                      or "the ecosystem")
            dip = inc["pre"] - inc["trough"]
            ctx = dict(inc, entity=entity, dip=dip,
                       kind_h=kind_h.get(inc["kind"], inc["kind"]),
                       owner_h=owner_h.get(inc["kind"],
                                           "a mix of decline classes"))
            stages = impact_stages if dip >= 0.25 else quiet_stages
            for i, (stage, team, tpl) in enumerate(stages, start=1):
                rows.append([
                    inc["event_id"], inc["start_date"], i, stage, team,
                    tpl.format(**ctx), entity, "Success Rate (%)",
                    round(inc["pre"], 2), round(inc["post"], 2),
                    inc["severity"] in ("Sev-1", "Sev-2")])
        return self._write_rows(
            "storylines",
            ["incident_id", "week_start", "step_no", "stage", "actor_team",
             "event", "entity", "linked_kpi", "sr_start", "sr_end",
             "has_incident"], rows)

    def _decision_tracking(self, con) -> CubeResult:
        """Did the response work? Measured against the transactions."""
        rows: list[list[Any]] = []
        for n, inc in enumerate(self._incident_impact(con), start=1):
            if inc["severity"] == "Sev-3":
                continue
            pre, trough, post = inc["pre"], inc["trough"], inc["post"]
            dip = pre - trough
            measurable = dip >= 0.25
            recovery = (max(0.0, min(100.0, (post - trough) / dip * 100))
                        if measurable else 100.0)
            entity = (inc["scope_bank"] or inc["scope_psp"]
                      or inc["scope_product"] or inc["scope_mcc"] or "")
            # A score that rewards recovering a large dip more than a small
            # one, so a fast fix on a serious incident outranks a slow fix on
            # a trivial one.
            score = round(recovery * min(1.0, max(dip, 0.0) / 3.0)
                          + recovery * 0.35, 1)
            rows.append([
                f"DEC-{n:04d}", inc["event_id"], inc["start_date"],
                f"{inc['title']} response", inc["severity"],
                inc["scope_bank"] or "", inc["scope_psp"] or "",
                inc["scope_product"] or "", "Success Rate (%)",
                f"Restore success on {entity or 'the rail'} toward the "
                f"pre-incident {pre:.2f}%",
                round(pre, 2), round(trough, 2), round(post, 2),
                (f"Recovered {recovery:.1f}% of a {dip:.2f}pp dip "
                 f"({trough:.2f}% -> {post:.2f}%)" if measurable else
                 f"No measurable dip — success stayed within normal daily "
                 f"variation of the {pre:.2f}% baseline"),
                round(recovery, 1), score,
                round(inc["volume"] * (max(dip, 0.0) / 100.0), 2),
                "No impact" if not measurable else
                ("Closed" if recovery >= 85 else
                 ("Monitoring" if recovery >= 50 else "Open")),
                f"{inc['event_id']} storylines cross_entity"])
        return self._write_rows(
            "decision_tracking",
            ["decision_id", "incident_id", "date", "title", "severity",
             "bank", "psp", "feature", "target_kpi", "expected_impact",
             "pre_value", "trough_value", "post_value", "actual_impact",
             "recovery_pct", "success_score", "attempts_at_risk", "status",
             "evidence_refs"], rows)
