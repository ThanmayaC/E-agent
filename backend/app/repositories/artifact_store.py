"""Repository for pipeline artifacts.

Artifacts (profiles, KPIs, insights, report, graph, ...) are stored as JSON
documents per project; tabular data lives in the project's DuckDB file.
This keeps the API layer free of any knowledge of how artifacts persist.
"""
from __future__ import annotations

import json
import shutil
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pydantic import BaseModel


class ArtifactStore:
    def __init__(self, projects_dir: Path):
        self._root = projects_dir

    # ------------------------------------------------------------- paths
    def project_dir(self, project_id: str, *, create: bool = True) -> Path:
        """Path to a project directory. ``create=False`` for read paths: a
        lookup must never bring a project into existence (a stray id such as
        ``undefined`` used to leave a permanent ghost directory behind)."""
        d = self._root / project_id
        if create:
            d.mkdir(parents=True, exist_ok=True)
        return d

    def uploads_dir(self, project_id: str) -> Path:
        d = self.project_dir(project_id) / "uploads"
        d.mkdir(exist_ok=True)
        return d

    def duckdb_path(self, project_id: str) -> Path:
        return self.project_dir(project_id) / "analytics.duckdb"

    def vectors_path(self, project_id: str) -> Path:
        return self.project_dir(project_id) / "vectors.json"

    def _artifact_path(self, project_id: str, name: str,
                       *, create: bool = True) -> Path:
        d = self.project_dir(project_id, create=create) / "artifacts"
        if create:
            d.mkdir(parents=True, exist_ok=True)
        return d / f"{name}.json"

    # ---------------------------------------------------------- documents
    def save(self, project_id: str, name: str, payload: Any) -> None:
        data = self._serialize(payload)
        self._artifact_path(project_id, name).write_text(
            json.dumps({"saved_at": datetime.now(timezone.utc).isoformat(), "data": data},
                       ensure_ascii=False, default=str),
            encoding="utf-8",
        )

    def load(self, project_id: str, name: str, default: Any = None) -> Any:
        path = self._artifact_path(project_id, name, create=False)
        if not path.exists():
            return default
        try:
            return json.loads(path.read_text(encoding="utf-8"))["data"]
        except (ValueError, KeyError):
            # a truncated/half-written artifact must not take the caller down
            return default

    def exists(self, project_id: str, name: str) -> bool:
        return self._artifact_path(project_id, name, create=False).exists()

    def list_projects(self) -> list[str]:
        """User-facing project ids. Directories prefixed with ``_`` are
        internal namespaces (``_enterprise``, ``_organization``,
        ``_documents``) and are never projects."""
        if not self._root.exists():
            return []
        return sorted(p.name for p in self._root.iterdir()
                      if p.is_dir() and not p.name.startswith("_"))

    def delete_project(self, project_id: str) -> bool:
        """Remove every artifact a project owns: metadata/state, uploaded
        files, generated datasets (DuckDB), cached analytics, reports,
        embeddings (vector store), knowledge graph, and workflow runs — all of
        which live under the project directory."""
        d = self._root / project_id
        if not d.exists():
            return False
        # transient locks (e.g. an in-flight DuckDB read on Windows) get a
        # short retry before failing
        for attempt in range(3):
            try:
                shutil.rmtree(d)
                return True
            except OSError:
                if attempt == 2:
                    raise
                time.sleep(0.5)
        return True

    @classmethod
    def _serialize(cls, payload: Any) -> Any:
        if isinstance(payload, BaseModel):
            return payload.model_dump(mode="json")
        if isinstance(payload, list):
            return [cls._serialize(p) for p in payload]
        if isinstance(payload, dict):
            return {k: cls._serialize(v) for k, v in payload.items()}
        return payload
