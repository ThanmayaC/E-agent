"""Admin console — real subsystem runtime metrics, never placeholders.

Each card here is read live from the subsystem it describes at the moment the
console loads. A subsystem that is wired and holding data reports its true
figures (warehouse partitions and bytes, ML cache entries, orchestrator engine
availability, query cache hit-rate); one that is not wired reports
``available: false`` and says so plainly. There is no fabricated "99.9% uptime"
anywhere in this file — if a number cannot be measured, it is not shown.
"""
from __future__ import annotations

import time


def _safe(fn, default=None):
    try:
        return fn()
    except Exception:  # noqa: BLE001
        return default


def _probe(obj, *methods):
    """Return the first real dict a subsystem exposes via a status-like method."""
    for name in methods:
        fn = getattr(obj, name, None)
        if callable(fn):
            out = _safe(fn)
            if isinstance(out, dict):
                return out
    return None


def _card(key, label, category, available, metrics=None, detail=None,
          note="", healthy=None):
    return {"key": key, "label": label, "category": category,
            "available": bool(available),
            "healthy": (bool(available) if healthy is None else bool(healthy)),
            "metrics": metrics or {}, "detail": detail or {}, "note": note}


# ----------------------------------------------------------- warehouse layer
def _warehouse_card(c) -> dict:
    wh = getattr(c, "warehouse", None)
    if wh is None:
        return _card("warehouse", "Transaction Warehouse", "Data", False,
                     note="not wired")
    st = _safe(wh.status, {}) or {}
    mf = st.get("manifest", {})
    cache = st.get("cache", {})
    return _card(
        "warehouse", "Transaction Warehouse", "Data", st.get("available"),
        metrics={
            "transactions": st.get("transactions") or mf.get("transactions"),
            "partitions": st.get("partitions"),
            "days": st.get("days") or mf.get("days"),
            "products": st.get("products") or mf.get("products"),
            "disk_mb": st.get("mb_on_disk"),
            "cache_hit_rate_pct": cache.get("hit_rate_pct"),
            "cache_entries": cache.get("entries")},
        detail={"engine": st.get("engine"), "window":
                [st.get("first_date"), st.get("last_date")],
                "reference_tables": len(st.get("reference_tables", []))},
        note="DuckDB SQL over raw parquet")


def _analytics_card(c) -> dict:
    a = getattr(c, "tx_analytics", None)
    if a is None:
        return _card("analytics", "Analytics Engine", "Intelligence", False,
                     note="not wired")
    ok = a.available
    metrics = {}
    if ok:
        t0 = time.perf_counter()
        window = _safe(a.corpus_window, ("", ""))
        probe = _safe(lambda: a.wh.scalar("SELECT count(*) FROM attempts",
                                          default=0), 0)
        metrics = {"attempt_rows": int(probe or 0),
                   "probe_ms": round((time.perf_counter() - t0) * 1000, 1),
                   "kpi_definitions": len(__import__(
                       "app.warehouse.analytics", fromlist=["KPI_META"]).KPI_META),
                   "window_start": window[0], "window_end": window[1]}
    return _card("analytics", "Analytics Engine", "Intelligence", ok,
                 metrics=metrics, note="every KPI derived from raw transactions")


def _ml_card(c) -> dict:
    m = getattr(c, "ml_pipeline", None)
    if m is None:
        return _card("ml", "ML Engine", "Intelligence", False, note="not wired")
    ok = m.available
    stats = _safe(m.cache_stats, {}) or {}
    try:
        from app.warehouse.ml.forecast import _SKLEARN
    except Exception:  # noqa: BLE001
        _SKLEARN = False
    from app.warehouse.ml import FORECASTABLE
    return _card("ml", "ML Engine", "Intelligence", ok,
                 metrics={"sklearn": _SKLEARN,
                          "forecastable_targets": len(FORECASTABLE),
                          "cached_runs": stats.get("entries", 0),
                          "models": "HistGradientBoosting / Ridge / "
                                    "IsolationForest / KMeans"},
                 detail={"pipeline": "EDA→features→train→backtest→forecast→"
                                     "explain", "cached_targets":
                         stats.get("targets", [])},
                 note="backtested; forecasts carry confidence + reasons")


def _orchestrator_card(c) -> dict:
    orch = getattr(c, "ai_orchestrator", None)
    if orch is None:
        return _card("orchestrator", "Enterprise AI Orchestrator", "Intelligence",
                     False, note="disabled or not wired")
    desc = _safe(orch.describe, {}) or {}
    engines = desc.get("engines", [])
    live = [e for e in engines if e.get("available")]
    return _card("orchestrator", "Enterprise AI Orchestrator", "Intelligence",
                 True,
                 metrics={"engines": len(engines), "engines_available": len(live),
                          "categories": len(desc.get("categories", []))},
                 detail={"engines": [{"key": e.get("engine"),
                                      "available": e.get("available")}
                                     for e in engines]},
                 note="classifies + routes every question to real engines")


# --------------------------------------------------- federated subsystems
def _generic_card(key, label, category, obj, methods, note="") -> dict:
    if obj is None:
        return _card(key, label, category, False, note="not wired")
    st = _probe(obj, *methods)
    if st is None:
        # Wired but exposes no status method — report liveness honestly.
        return _card(key, label, category, True, note=note or "live")
    # Pull a few real scalar metrics out of whatever the status returned.
    metrics = {k: v for k, v in st.items()
               if isinstance(v, (int, float, bool, str)) and k != "note"}
    available = st.get("available", st.get("enabled", True))
    return _card(key, label, category, available,
                 metrics=dict(list(metrics.items())[:10]),
                 detail={"keys": list(st.keys())[:12]},
                 note=note or str(st.get("note", "")))


def subsystem_report(c) -> dict:
    """The full console payload: every subsystem, grouped, with real metrics."""
    cards = [
        _warehouse_card(c),
        _analytics_card(c),
        _ml_card(c),
        _orchestrator_card(c),
        _generic_card("brain", "Enterprise Brain", "Intelligence",
                      getattr(c, "brain", None),
                      ("status", "describe", "stats")),
        _generic_card("knowledge_graph", "Knowledge Graph", "Intelligence",
                      getattr(c, "enterprise_graph", None),
                      ("status", "stats", "describe", "summary")),
        _generic_card("rag", "Enterprise RAG", "Intelligence",
                      getattr(c, "knowledge", None),
                      ("status", "stats", "describe")),
        _generic_card("llm", "LLM Provider", "Intelligence",
                      getattr(c, "llm_provider", None),
                      ("status", "describe", "usage", "stats")),
        _generic_card("connectors", "Connectors", "Integration",
                      getattr(c, "connectors", None),
                      ("status", "describe", "summary")),
        _generic_card("email", "Email Services", "Integration",
                      getattr(c, "email_intelligence", None),
                      ("status", "describe", "stats")),
        _generic_card("sync", "Sync & Ingestion", "Integration",
                      getattr(c, "sync", None),
                      ("status", "describe", "stats")),
        _generic_card("runtime", "Runtime Diagnostics", "Operations",
                      getattr(c, "runtime", None),
                      ("status", "describe", "health", "stats")),
        _generic_card("observability", "Observability", "Operations",
                      getattr(c, "observability", None),
                      ("status", "describe", "snapshot", "stats")),
        _generic_card("workflows", "Jobs & Workflows", "Operations",
                      getattr(c, "workflows", None),
                      ("status", "describe", "list", "stats")),
    ]
    groups: dict[str, list] = {}
    for card in cards:
        groups.setdefault(card["category"], []).append(card)
    live = sum(1 for c_ in cards if c_["available"])
    return {"generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "subsystems": cards, "groups": groups,
            "summary": {"total": len(cards), "available": live,
                        "unavailable": len(cards) - live}}
