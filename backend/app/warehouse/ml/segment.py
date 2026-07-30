"""Unsupervised segmentation and rule-grounded classification.

Clustering here is descriptive, not decorative: merchants are grouped by
behaviour derived from their own transactions (ticket size, success, growth,
refund propensity, activity cadence), and each cluster is given a name and a
plain-language profile from its centroid so a product manager can act on it.

Classification is deliberately transparent — a merchant's health grade is a
scored rubric over measured facts, not a black box, because a risk label that
cannot be explained cannot be trusted.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

try:
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import silhouette_score
    _SKLEARN = True
except ImportError:  # pragma: no cover
    _SKLEARN = False

_CLUSTER_FEATURES = ["attempts", "success_rate", "avg_ticket_inr",
                     "refund_rate", "active_days", "customers", "value_inr"]


def _merchant_frame(analytics, filters) -> pd.DataFrame:
    """Per-merchant behavioural facts, straight from the transaction rows."""
    f = analytics.resolve(filters)
    where, params = f.where()
    sql = f"""
        WITH m AS (
          SELECT merchant_id,
                 any_value(merchant_name) AS merchant_name,
                 any_value(mcc_category) AS category,
                 any_value(merchant_tier) AS tier,
                 count(*) AS attempts,
                 count(DISTINCT txn_date) AS active_days,
                 count(DISTINCT customer_id) AS customers,
                 100.0*count(*) FILTER (WHERE status='SUCCESS')
                    / nullif(count(*),0) AS success_rate,
                 avg(amount_inr) FILTER (WHERE status='SUCCESS') AS avg_ticket_inr,
                 sum(amount_inr) FILTER (WHERE status='SUCCESS') AS value_inr
          FROM attempts WHERE {where} AND merchant_id IS NOT NULL
          GROUP BY merchant_id HAVING count(*) >= 30
        ), r AS (
          SELECT merchant_id,
                 count(*) FILTER (WHERE txn_type='REFUND') AS refunds,
                 count(*) FILTER (WHERE txn_type='CHARGEBACK') AS chargebacks
          FROM adjustments WHERE {where} GROUP BY merchant_id
        )
        SELECT m.*, coalesce(r.refunds,0) AS refunds,
               coalesce(r.chargebacks,0) AS chargebacks,
               100.0*coalesce(r.refunds,0)/nullif(m.attempts,0) AS refund_rate
        FROM m LEFT JOIN r USING (merchant_id)
    """
    return analytics.wh.df(sql, params * 2)


def cluster_merchants(analytics, filters, *, k: int | None = None,
                      max_merchants: int = 4000) -> dict:
    """Behavioural archetypes over the merchant base."""
    if not _SKLEARN:
        return {"available": False, "reason": "sklearn unavailable"}
    df = _merchant_frame(analytics, filters)
    if df.empty or len(df) < 20:
        return {"available": False, "reason": "not enough active merchants"}
    df = df.sample(min(len(df), max_merchants), random_state=7) \
        if len(df) > max_merchants else df
    feats = [c for c in _CLUSTER_FEATURES if c in df.columns]
    X = df[feats].fillna(0.0).to_numpy(float)
    # Log-compress the heavy-tailed magnitude features before scaling.
    for j, c in enumerate(feats):
        if c in ("attempts", "value_inr", "avg_ticket_inr", "customers"):
            X[:, j] = np.log1p(np.clip(X[:, j], 0, None))
    Xs = StandardScaler().fit_transform(X)

    best = None
    for kk in ([k] if k else range(3, 7)):
        if kk >= len(df):
            continue
        km = KMeans(n_clusters=kk, n_init=10, random_state=7).fit(Xs)
        try:
            sil = silhouette_score(Xs, km.labels_) if kk > 1 else -1
        except ValueError:
            sil = -1
        if best is None or sil > best[0]:
            best = (sil, kk, km)
    if best is None:
        return {"available": False, "reason": "clustering failed"}
    sil, kk, km = best
    df = df.copy()
    df["cluster"] = km.labels_

    clusters = []
    for cid in range(kk):
        seg = df[df["cluster"] == cid]
        if seg.empty:
            continue
        profile = {c: round(float(seg[c].median()), 2)
                   for c in feats if c in seg}
        clusters.append({
            "cluster_id": int(cid),
            "label": _name_cluster(profile, df, feats),
            "merchants": int(len(seg)),
            "share_pct": round(100 * len(seg) / len(df), 1),
            "profile": profile,
            "total_value_inr": round(float(seg["value_inr"].sum()), 0),
            "example_merchants": seg.nlargest(5, "attempts")[
                "merchant_name"].tolist()})
    clusters.sort(key=lambda c: c["total_value_inr"], reverse=True)
    return {"available": True, "k": kk,
            "silhouette": round(float(sil), 3),
            "merchants_clustered": int(len(df)),
            "features": feats, "clusters": clusters}


def _name_cluster(profile: dict, df: pd.DataFrame, feats: list[str]) -> str:
    """A human archetype name from where the centroid sits versus the base."""
    med = {c: float(df[c].median()) for c in feats}
    big = profile.get("attempts", 0) > med.get("attempts", 0)
    high_ticket = profile.get("avg_ticket_inr", 0) > med.get("avg_ticket_inr", 0)
    weak = profile.get("success_rate", 100) < med.get("success_rate", 100) - 1
    refundy = profile.get("refund_rate", 0) > max(1.0, med.get("refund_rate", 0) * 1.5)
    if refundy:
        return "High-refund / disputed"
    if weak:
        return "Struggling — low success"
    if big and high_ticket:
        return "High-value anchors"
    if big and not high_ticket:
        return "High-frequency low-ticket"
    if high_ticket:
        return "Premium occasional"
    return "Long-tail steady"


def classify_merchant_health(analytics, filters, *, limit: int = 200) -> dict:
    """A transparent 0-100 health grade per top merchant, with the reasons."""
    df = _merchant_frame(analytics, filters)
    if df.empty:
        return {"available": False}
    df = df.nlargest(min(limit, len(df)), "attempts").copy()
    base_success = float(df["success_rate"].median())
    graded = []
    for _, m in df.iterrows():
        score, reasons = 100.0, []
        sr = float(m["success_rate"] or 0)
        if sr < base_success - 3:
            pen = min(35, (base_success - sr) * 4)
            score -= pen
            reasons.append(f"success {sr:.1f}% is {base_success - sr:.1f}pp "
                           f"below peer median")
        rr = float(m["refund_rate"] or 0)
        if rr > 4:
            score -= min(25, (rr - 4) * 3)
            reasons.append(f"refund rate {rr:.1f}% elevated")
        if int(m["chargebacks"] or 0) > 0:
            score -= min(20, int(m["chargebacks"]) * 2)
            reasons.append(f"{int(m['chargebacks'])} chargebacks")
        if reasons == []:
            reasons.append("stable, no risk signals")
        score = max(0.0, min(100.0, score))
        grade = ("A" if score >= 85 else "B" if score >= 70 else
                 "C" if score >= 55 else "D" if score >= 40 else "E")
        graded.append({
            "merchant_id": m["merchant_id"],
            "merchant_name": m["merchant_name"],
            "category": m.get("category"),
            "tier": m.get("tier"),
            "attempts": int(m["attempts"]),
            "success_rate": round(sr, 2),
            "refund_rate": round(rr, 2),
            "health_score": round(score, 1),
            "grade": grade,
            "reasons": reasons})
    graded.sort(key=lambda r: r["health_score"])
    dist: dict[str, int] = {}
    for g in graded:
        dist[g["grade"]] = dist.get(g["grade"], 0) + 1
    return {"available": True, "graded": len(graded),
            "grade_distribution": dist,
            "peer_median_success": round(base_success, 2),
            "at_risk": [g for g in graded if g["grade"] in ("D", "E")][:25],
            "merchants": graded}
