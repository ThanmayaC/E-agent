"""Model Registry (03-ml-platform.md §3) — versions, stages, signatures, cards.

Project-scoped file registry: each registered version persists the fitted
model bundle (model + its FeatureEngineer, so inference replays the exact
training transformations) via joblib, next to a model card. Stage
transitions follow None → Staging → Production → Archived; promotion to
Production always requires a named human approver (the approval interrupt of
02 §6.4 — governance is not optional).

MLflow is an optional adapter: when the library is installed and a tracking
URI is configured the run is mirrored there; its absence is a recorded,
normal state, never a failure. The relational control-plane record stays in
the Evidence Ledger (``EvidenceLedger.register_model``), written by the
Training Pipeline.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

import joblib

from app.core.logging import get_logger
from app.ml.features import FeatureEngineer

logger = get_logger(__name__)

STAGES = ("None", "Staging", "Production", "Archived")


@dataclass
class RegisteredModel:
    name: str
    version: int
    stage: str
    card: dict
    path: str


class ModelRegistry:
    def __init__(self, project_dir: Path, mlflow_uri: str = ""):
        self._dir = Path(project_dir) / "models"
        self._dir.mkdir(parents=True, exist_ok=True)
        self._mlflow_uri = mlflow_uri

    # ------------------------------------------------------------- register
    def register(self, name: str, model, engineer: FeatureEngineer, *,
                 task: str, family: str, metrics: dict,
                 selection_trace: dict, reference_stats: dict | None = None,
                 limitations: list[str] | None = None) -> RegisteredModel:
        version = self.latest_version(name) + 1
        vdir = self._dir / name / f"v{version}"
        vdir.mkdir(parents=True, exist_ok=True)
        joblib.dump({"model": model, "engineer": engineer}, vdir / "model.joblib")
        card = {
            "name": name, "version": version, "stage": "Staging",
            "task": task, "family": family,
            "signature": {"inputs": engineer.input_columns,
                          "features": engineer.feature_names},
            "metrics": metrics,
            "selection_trace": selection_trace,
            "reference_stats": reference_stats or {},
            "limitations": limitations or [],
            "explainability": (selection_trace.get("explanation") or {}).get("method"),
            "mlflow": self._mirror_to_mlflow(name, version, metrics),
            "registered_at": datetime.now(UTC).isoformat(),
            "approvals": [],
        }
        (vdir / "card.json").write_text(
            json.dumps(card, ensure_ascii=False, default=str), encoding="utf-8")
        logger.info("registered model %s v%d (%s)", name, version, family)
        return RegisteredModel(name=name, version=version, stage="Staging",
                               card=card, path=str(vdir))

    # ------------------------------------------------------------ lifecycle
    def promote(self, name: str, version: int, stage: str,
                approved_by: str = "") -> dict:
        """Stage transition. Production requires a named approver — every
        transition is appended to the card's approval record."""
        if stage not in STAGES:
            raise ValueError(f"unknown stage '{stage}' (valid: {STAGES})")
        if stage == "Production" and not approved_by:
            raise PermissionError(
                "promotion to Production requires human approval "
                "(pass approved_by=<user>)")
        card = self._card_path(name, version)
        data = json.loads(card.read_text(encoding="utf-8"))
        data["approvals"].append({
            "from": data["stage"], "to": stage, "by": approved_by or "system",
            "at": datetime.now(UTC).isoformat()})
        data["stage"] = stage
        if stage == "Production":  # a single Production version per name
            for other in self.list(name):
                if other["version"] != version and other["stage"] == "Production":
                    self.promote(name, other["version"], "Archived",
                                 approved_by=approved_by)
        card.write_text(json.dumps(data, ensure_ascii=False, default=str),
                        encoding="utf-8")
        return data

    # ----------------------------------------------------------------- load
    def load(self, name: str, version: int | None = None,
             stage: str | None = None) -> tuple[object, FeatureEngineer, dict]:
        """Load (model, engineer, card). Default: Production if one exists,
        else the latest version."""
        if version is None:
            cards = self.list(name)
            if not cards:
                raise FileNotFoundError(f"no registered versions of '{name}'")
            wanted = stage or "Production"
            staged = [c for c in cards if c["stage"] == wanted]
            version = (staged or cards)[0]["version"]
        vdir = self._dir / name / f"v{version}"
        bundle = joblib.load(vdir / "model.joblib")
        card = json.loads((vdir / "card.json").read_text(encoding="utf-8"))
        return bundle["model"], bundle["engineer"], card

    # ---------------------------------------------------------------- query
    def latest_version(self, name: str) -> int:
        d = self._dir / name
        if not d.exists():
            return 0
        return max((int(p.name[1:]) for p in d.iterdir()
                    if p.is_dir() and p.name.startswith("v")), default=0)

    def list(self, name: str | None = None) -> list[dict]:
        cards = []
        for card in sorted(self._dir.glob("*/v*/card.json")):
            data = json.loads(card.read_text(encoding="utf-8"))
            if name is None or data["name"] == name:
                cards.append(data)
        cards.sort(key=lambda c: (c["name"], -c["version"]))
        return cards

    # ------------------------------------------------------------ internals
    def _card_path(self, name: str, version: int) -> Path:
        p = self._dir / name / f"v{version}" / "card.json"
        if not p.exists():
            raise FileNotFoundError(f"model {name} v{version} is not registered")
        return p

    def _mirror_to_mlflow(self, name: str, version: int, metrics: dict) -> str:
        if not self._mlflow_uri:
            return "unavailable: no tracking URI configured"
        try:
            import mlflow  # type: ignore
        except ImportError:
            return "unavailable: mlflow not installed (lite profile)"
        try:
            mlflow.set_tracking_uri(self._mlflow_uri)
            with mlflow.start_run(run_name=f"{name}-v{version}"):
                mlflow.log_metrics({k: v for k, v in metrics.items()
                                    if isinstance(v, (int, float))})
            return f"mirrored: {self._mlflow_uri}"
        except Exception as exc:  # tracking outage never blocks registration
            return f"unavailable: {str(exc)[:120]}"
