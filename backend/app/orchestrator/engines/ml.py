"""ML Engine — the trained models, called when a question is theirs.

Anomaly detection, merchant segmentation, merchant risk grading: "is anything
unusual", "which merchants are at risk", "segment the merchant base" are
answered by the warehouse ML modules running over raw transactions, not by
retrieval and not by the LLM. Anomaly detection is scored against the simulator's
incident ledger (a held-out answer key), so the engine can report its own
precision and recall rather than assert it caught everything.

The engine selects which model(s) to run from the question's signals, so a
segmentation question does not needlessly run anomaly detection.
"""
from __future__ import annotations

from app.orchestrator.base import Engine, EngineRequest, EngineResult
from app.orchestrator.engines import _slice
from app.warehouse.ml import segment as segment_mod

_ANOMALY = ("anomaly", "anomalies", "outlier", "unusual", "spike", "strange",
            "irregular", "incident", "outage")
_SEGMENT = ("segment", "segmentation", "cluster", "group merchants", "cohort",
            "archetype")
_RISK = ("churn", "at risk", "at-risk", "leaving", "attrition", "failure",
         "risky", "risk of", "health", "unhealthy", "propensity")


class MLEngine(Engine):
    key = "ml"
    label = "Machine Learning Engine"
    categories = ("ml",)

    def __init__(self, ml_pipeline=None, analytics=None):
        self._ml = ml_pipeline
        self._a = analytics

    def available(self) -> bool:
        return bool(self._ml is not None and self._ml.available)

    def run(self, request: EngineRequest) -> EngineResult:
        res = self._result()
        if not self.available():
            res.status = "unavailable"
            res.ran = False
            res.note = "ML pipeline holds no transaction history"
            return res
        filters, _window = _slice.build_training_filters(request, self._a)
        # The metric the question actually names — a question about
        # transaction *value* must scan value_inr for anomalies, not always
        # success_rate, or the evidence gathered has nothing to do with what
        # was asked.
        target = _slice.pick_target(request)
        text = f" {request.message.lower()} "
        wanted = self._select(text)
        cards: dict[str, dict] = {}
        for name in wanted:
            getattr(self, f"_{name}")(res, cards, filters, target)
        res.detail = {"models_run": list(wanted), "slice": filters.describe(),
                      "target": target, "cards": cards}
        return res

    def _select(self, text: str) -> list[str]:
        picks = []
        if any(k in text for k in _ANOMALY):
            picks.append("anomaly")
        if any(k in text for k in _SEGMENT):
            picks.append("segment")
        if any(k in text for k in _RISK):
            picks.append("risk")
        return picks or ["anomaly", "risk"]

    # ------------------------------------------------------------ anomaly
    def _anomaly(self, res: EngineResult, cards: dict, filters, target: str) -> None:
        r = self._ml.anomaly_scan(filters, target=target)
        if not r.get("available"):
            return
        val = r.get("validation", {})
        cards["anomaly"] = {"validation": val,
                            "days_flagged": r.get("distinct_anomaly_days")}
        if val.get("scored"):
            res.add("ml_anomaly_quality", "ml:anomaly:validation",
                    f"Anomaly detector precision {val.get('precision')}, "
                    f"recall {val.get('recall')}",
                    {"text": (
                        f"The anomaly detector, scanning {target}, caught "
                        f"{val.get('incidents_detected')} of "
                        f"{val.get('incidents_in_ledger')} real incidents in "
                        f"this slice (recall {val.get('recall')}), with precision "
                        f"{val.get('precision')} and F1 {val.get('f1')} — scored "
                        f"against the ground-truth incident ledger.")})
        for a in (r.get("seasonal_anomalies") or [])[:6]:
            res.add("ml_anomaly", f"ml:anomaly:{a.get('date')}:{a.get('metric')}",
                    f"Anomalous {a.get('metric')} on {a.get('date')} "
                    f"({a.get('direction')})",
                    {"text": (
                        f"{a.get('date')}: {a.get('metric')} {a.get('direction')} "
                        f"to {a.get('value')} vs an expected {a.get('expected')} "
                        f"({a.get('deviation_pct')}%, z={a.get('z_score')}, "
                        f"{a.get('severity')}).")})

    # ------------------------------------------------------------ segment
    def _segment(self, res: EngineResult, cards: dict, filters, target: str) -> None:
        r = segment_mod.cluster_merchants(self._a, filters)
        if not r.get("available"):
            return
        cards["segmentation"] = {"k": r.get("k"),
                                 "silhouette": r.get("silhouette"),
                                 "merchants": r.get("merchants_clustered")}
        for s in r.get("clusters", []):
            prof = s.get("profile", {})
            res.add("ml_segment", f"ml:segment:{s.get('cluster_id')}",
                    f"Segment '{s.get('label')}' ({s.get('merchants')} merchants)",
                    {"text": (
                        f"KMeans segment '{s.get('label')}': {s.get('merchants')} "
                        f"merchants ({s.get('share_pct')}% of base), median "
                        f"{int(prof.get('attempts', 0))} txns, success "
                        f"{prof.get('success_rate')}%, avg ticket ₹"
                        f"{prof.get('avg_ticket_inr')}, total settled ₹"
                        f"{int(s.get('total_value_inr', 0)):,}.")})

    # --------------------------------------------------------------- risk
    def _risk(self, res: EngineResult, cards: dict, filters, target: str) -> None:
        r = segment_mod.classify_merchant_health(self._a, filters)
        if not r.get("available"):
            return
        cards["merchant_health"] = {"graded": r.get("graded"),
                                    "distribution": r.get("grade_distribution"),
                                    "peer_median_success":
                                        r.get("peer_median_success")}
        res.add("ml_health_summary", "ml:health:summary",
                f"{r.get('graded')} merchants graded; "
                f"{len(r.get('at_risk', []))} at risk",
                {"text": (
                    f"Merchant health graded for {r.get('graded')} merchants "
                    f"(grade mix {r.get('grade_distribution')}); peer-median "
                    f"success {r.get('peer_median_success')}%.")})
        for m in (r.get("at_risk") or [])[:6]:
            res.add("ml_risk", f"ml:risk:{m.get('merchant_id')}",
                    f"{m.get('merchant_name')} health {m.get('health_score')} "
                    f"(grade {m.get('grade')})",
                    {"text": (
                        f"{m.get('merchant_name')} ({m.get('category')}) graded "
                        f"{m.get('grade')} at health {m.get('health_score')}/100: "
                        f"success {m.get('success_rate')}%, refund rate "
                        f"{m.get('refund_rate')}%. Reasons: "
                        f"{'; '.join(m.get('reasons', []))}.")})
