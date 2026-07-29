"""Enterprise AI Workspace (V9.0) — the facade the AI-first UI talks to.

Ties together universal file upload + AI understanding, unified enterprise
search, artifact generation, the conversational home feed and the workspace
(pins / saved prompts / bookmarks). It adds no new intelligence of its own — it
orchestrates the layers the platform already has (Copilot, Executive, Ecosystem,
Evolution, Knowledge Graph) behind one surface. If a layer is unavailable the
corresponding section degrades to empty, never an error.
"""
from __future__ import annotations

import json
import re
import time
from pathlib import Path

from app.analyst.cache import SemanticCache
from app.core.logging import get_logger
from app.workspace.artifacts import ArtifactGenerator
from app.workspace.search import EnterpriseSearch
from app.workspace.understanding import FileUnderstanding

logger = get_logger(__name__)

_SUPPORTED = {".xlsx", ".xlsm", ".xls", ".csv", ".tsv", ".pdf", ".docx", ".doc",
              ".pptx", ".ppt", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp",
              ".svg", ".zip", ".json", ".xml", ".txt", ".md", ".markdown", ".log"}


class Workspace:
    def __init__(self, container, base_dir: Path):
        self._c = container
        self._dir = Path(base_dir)
        self._uploads = self._dir / "uploads"
        self._understanding = self._dir / "understanding"
        self._artifacts_dir = self._dir / "artifacts"
        for d in (self._uploads, self._understanding, self._artifacts_dir):
            d.mkdir(parents=True, exist_ok=True)
        self._meta_path = self._dir / "meta.json"
        self._search = EnterpriseSearch(container)
        self._artifacts = ArtifactGenerator(container, self._artifacts_dir)
        self._search_cache = SemanticCache(ttl=90.0, capacity=256)

    # ------------------------------------------------------------ capability
    @staticmethod
    def supported_extensions() -> list[str]:
        return sorted(_SUPPORTED)

    def accepts(self, filename: str) -> bool:
        return Path(filename or "").suffix.lower() in _SUPPORTED

    def status(self) -> dict:
        return {"available": True,
                "files": len(list(self._understanding.glob("*.json"))),
                "artifacts": len(list(self._artifacts_dir.glob("*"))),
                "supported_extensions": self.supported_extensions(),
                "artifact_kinds": self._artifacts.kinds()}

    # ------------------------------------------------------------- vocabulary
    def _vocab(self) -> dict:
        v = {"banks": [], "psps": [], "merchants": [], "products": [],
             "features": []}
        eco = getattr(self._c, "ecosystem", None)
        evo = getattr(self._c, "evolution", None)
        try:
            if eco and eco.available:
                v["banks"] = [r["name"] for r in eco.compare_banks()]
                v["psps"] = [r["name"] for r in eco.compare_psps()]
                v["features"] = [r["name"] for r in eco.compare_features()]
            if evo and evo.available:
                v["merchants"] = [r["merchant"] for r in
                                  evo.merchants().get("merchants", [])]
                v["products"] = [r["product"] for r in
                                 evo.products().get("products", [])]
        except Exception:  # noqa: BLE001
            logger.exception("workspace vocab build failed")
        return v

    # ---------------------------------------------------------------- uploads
    def save_upload(self, filename: str, content: bytes) -> dict:
        safe = re.sub(r"[^0-9a-zA-Z._ -]", "_", filename or "upload")
        fid = f"{int(time.time() * 1000)}-{abs(hash(safe)) % 10000:04d}"
        path = self._uploads / f"{fid}__{safe}"
        path.write_bytes(content)
        result = self.understand(fid)
        return result

    def understand(self, fid: str) -> dict:
        path = self._upload_path(fid)
        if not path:
            return {"error": "file not found", "id": fid}
        fu = FileUnderstanding(self._vocab())
        result = fu.understand(path)
        result["id"] = fid
        # display name without the internal "{id}__" storage prefix
        result["file"] = path.name.split("__", 1)[-1]
        result["stored_path"] = str(path)
        self._link_to_graph(result)
        (self._understanding / f"{fid}.json").write_text(
            json.dumps(result, ensure_ascii=False), encoding="utf-8")
        return result

    def _upload_path(self, fid: str) -> Path | None:
        for p in self._uploads.glob(f"{fid}__*"):
            return p
        return None

    def list_files(self) -> list[dict]:
        out = []
        for p in sorted(self._understanding.glob("*.json"),
                        key=lambda x: x.stat().st_mtime, reverse=True):
            try:
                d = json.loads(p.read_text(encoding="utf-8"))
            except Exception:  # noqa: BLE001
                continue
            out.append({k: d.get(k) for k in
                        ("id", "file", "type", "size_bytes", "summary",
                         "tags", "understood_at", "entities")})
        return out

    def get_file(self, fid: str) -> dict:
        p = self._understanding / f"{fid}.json"
        if not p.exists():
            return {"error": "not found", "id": fid}
        return json.loads(p.read_text(encoding="utf-8"))

    def delete_file(self, fid: str) -> dict:
        removed = False
        for p in (self._understanding / f"{fid}.json", self._upload_path(fid)):
            if p and p.exists():
                p.unlink(); removed = True
        return {"deleted": removed, "id": fid}

    def _link_to_graph(self, result: dict) -> None:
        """Best-effort: record the file as a Knowledge-Graph node linked to the
        entities it mentions. Never fails the upload."""
        graph = getattr(self._c, "enterprise_graph", None)
        if not graph or not hasattr(graph, "batch"):
            return
        try:
            with graph.batch() as b:  # type: ignore[attr-defined]
                node_id = f"file:{result['id']}"
                add = getattr(b, "add_node", None) or getattr(b, "node", None)
                relate = getattr(b, "relate", None) or getattr(b, "_relate", None)
                if add:
                    add(node_id, label=result["file"], type="file")
                if relate:
                    for link in result.get("kg_links", []):
                        relate(node_id, f"{link['type']}:{link['name']}",
                               "mentions")
        except Exception:  # noqa: BLE001
            logger.debug("workspace KG link skipped", exc_info=True)

    # ----------------------------------------------------------------- search
    def search(self, query: str, limit: int = 40) -> dict:
        cache_key = f"{query}::{limit}"
        cached = self._search_cache.get(cache_key)
        if cached is not None:
            return {**cached, "cached": True}
        result = self._search.search(query, limit)
        self._search_cache.set(cache_key, result)
        # continuous learning: remember what people search for
        learn = getattr(self._c, "learning_store", None)
        if learn:
            try:
                learn.record_question(query)
            except Exception:  # noqa: BLE001
                pass
        return result

    def cache_stats(self) -> dict:
        return self._search_cache.stats()

    # -------------------------------------------------------------- artifacts
    def generate_artifact(self, kind: str, title: str = "", prompt: str = "",
                          sections: list | None = None, fmt: str = "") -> dict:
        return self._artifacts.generate(kind, title=title or None,
                                        prompt=prompt or None,
                                        sections=sections, fmt=fmt or None)

    def list_artifacts(self) -> list[dict]:
        out = []
        for p in sorted(self._artifacts_dir.glob("*"),
                        key=lambda x: x.stat().st_mtime, reverse=True):
            if p.is_file():
                out.append({"file": p.name, "bytes": p.stat().st_size,
                            "download_url": f"/api/v1/workspace/artifacts/{p.name}"})
        return out

    def artifact_path(self, name: str) -> Path | None:
        safe = Path(name).name
        p = self._artifacts_dir / safe
        return p if p.exists() else None

    # -------------------------------------------------- pins / saved / meta
    def _meta(self) -> dict:
        if self._meta_path.exists():
            try:
                return json.loads(self._meta_path.read_text(encoding="utf-8"))
            except Exception:  # noqa: BLE001
                pass
        return {"pins": [], "saved_prompts": [], "saved_queries": [],
                "bookmarks": [], "collections": []}

    def _write_meta(self, meta: dict) -> None:
        self._meta_path.write_text(json.dumps(meta, ensure_ascii=False),
                                   encoding="utf-8")

    def pins(self) -> dict:
        return self._meta()

    def add_pin(self, bucket: str, item: dict) -> dict:
        meta = self._meta()
        bucket = bucket if bucket in meta else "pins"
        item = {**item, "id": f"{int(time.time() * 1000)}"}
        meta[bucket].insert(0, item)
        meta[bucket] = meta[bucket][:100]
        self._write_meta(meta)
        return item

    def remove_pin(self, bucket: str, item_id: str) -> dict:
        meta = self._meta()
        if bucket in meta:
            meta[bucket] = [x for x in meta[bucket] if x.get("id") != item_id]
            self._write_meta(meta)
        return {"removed": item_id, "bucket": bucket}

    # ------------------------------------------------------------------ home
    def home(self) -> dict:
        feed = {"available": True}
        cop = getattr(self._c, "copilot_layer", None)
        # recent conversations (a fast store read). NOTE: we deliberately do NOT
        # call copilot.suggested_questions() here — it can invoke the LLM and
        # would block the home feed; the suggestions below are instant and the
        # frontend also carries fallbacks.
        try:
            if cop:
                feed["recent_conversations"] = cop.conversations.conversations(
                    limit=8)
        except Exception:  # noqa: BLE001
            feed["recent_conversations"] = []
        feed.setdefault("recent_conversations", [])
        feed["suggestions"] = [
            "What happened across UPI this month?",
            "Why did transaction value change?",
            "Which banks are improving?",
            "Which PSP is losing market share?",
            "Generate an executive report.",
            "Summarize the latest incident and its RCA.",
        ]
        # recent files
        feed["recent_files"] = self.list_files()[:8]
        # recent reports — deliberately NOT via executive.reports(); on the
        # 180-day corpus that call parses every report/RCA and is too slow for
        # the home feed. Surface report categories from the fast reader instead.
        feed["recent_reports"] = self._recent_reports()
        # recommendations
        try:
            evo = getattr(self._c, "evolution", None)
            feed["recommendations"] = (evo.decisions().get("top_value", [])[:4]
                                       if evo and evo.available else [])
        except Exception:  # noqa: BLE001
            feed["recommendations"] = []
        # pinned items + saved
        meta = self._meta()
        feed["pinned"] = meta.get("pins", [])[:8]
        feed["saved_prompts"] = meta.get("saved_prompts", [])[:8]
        feed["recent_artifacts"] = self.list_artifacts()[:6]
        return feed

    def _recent_reports(self) -> list[dict]:
        """Fast, filesystem-only listing of the most recent report artifacts
        (no markdown parsing) from the generated corpus."""
        try:
            base = self._c.settings.enterprise_data_dir
        except Exception:  # noqa: BLE001
            return []
        try:
            paths = sorted(base.glob("day_*/reports/*.md"),
                           key=lambda p: p.stat().st_mtime, reverse=True)[:6]
            out = []
            for p in paths:
                stem = p.stem
                cat = ("Monthly" if "MONTHLY" in stem.upper()
                       else "Weekly" if "W" in stem.upper() and "WEEK" in stem.upper()
                       else "Daily")
                out.append({"title": stem.replace("-", " "), "category": cat})
            return out
        except Exception:  # noqa: BLE001
            return []

    # --------------------------------------------------------------- context
    def context(self, page: str = "", extra: dict | None = None) -> dict:
        """What the AI sidebar knows about the user's current situation."""
        return {"page": page, "extra": extra or {},
                "enterprise": {
                    "ecosystem_available": bool(getattr(getattr(self._c,
                        "ecosystem", None), "available", False)),
                    "evolution_available": bool(getattr(getattr(self._c,
                        "evolution", None), "available", False))},
                "files_in_workspace": len(list(
                    self._understanding.glob("*.json")))}
