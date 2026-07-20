"""Extract typed evidence records from the business context.

The business context (BusinessContextBuilder) is already the single source of
truth the LLM reasons over, and every citable item in it carries an `id`.
This module walks the known sections and produces ledger records — one per
citable fact — with the correct kind and producer. A final recursive sweep
catches any id-bearing item a future context section adds, so new evidence
kinds degrade to `fact` instead of silently escaping the ledger.
"""
from __future__ import annotations

import hashlib
import json
from typing import Any

# (context section path, kind, producer)
SECTIONS: list[tuple[str, str, str]] = [
    ("kpis", "kpi", "quant.kpi"),
    ("forecast", "forecast", "quant.forecast"),
    ("anomalies", "signal", "quant.signals"),
    ("correlations", "signal", "quant.signals"),
    ("cannibalization", "signal", "quant.signals"),
]


def content_hash(payload: dict) -> str:
    return hashlib.sha1(
        json.dumps(payload, sort_keys=True, default=str).encode()).hexdigest()[:40]


def extract_evidence(context: dict[str, Any]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    seen: set[str] = set()

    def add(item: dict, kind: str, producer: str) -> None:
        eid = item.get("id")
        if not isinstance(eid, str) or not eid or eid in seen:
            return
        seen.add(eid)
        records.append({"evidence_id": eid, "kind": kind, "producer": producer,
                        "payload": item, "content_hash": content_hash(item)})

    for section, kind, producer in SECTIONS:
        for item in context.get(section) or []:
            if isinstance(item, dict):
                add(item, kind, producer)

    growth = context.get("growth") or {}
    for key in ("trends", "seasonality"):
        for item in growth.get(key) or []:
            if isinstance(item, dict):
                add(item, "signal", "quant.signals")
    metrics = context.get("executive_metrics") or {}
    for item in metrics.get("concentration_signals") or []:
        if isinstance(item, dict):
            add(item, "signal", "quant.signals")

    quality = context.get("quality") or {}
    if isinstance(quality, dict) and quality.get("id"):
        add(quality, "quality", "quality.engine")
        for issue in quality.get("worst_issues") or []:
            if isinstance(issue, dict):
                add(issue, "quality", "quality.engine")

    limitations = context.get("data_limitations")
    if isinstance(limitations, dict):
        add({"id": "limitations:dataset", **limitations},
            "limitation", "context.limitations")

    # sweep: any remaining id-bearing dict anywhere in the context
    def sweep(node: Any) -> None:
        if isinstance(node, dict):
            if isinstance(node.get("id"), str):
                add(node, "fact", "context")
            for v in node.values():
                sweep(v)
        elif isinstance(node, list):
            for v in node:
                sweep(v)

    sweep(context)
    return records
