"""Source readers — turning a registered source into tabular extracts.

This layer deliberately contains **no provider code**. Every registered source
is read through a connector that already exists (`app/intelligence/connectors`)
— Excel, CSV, SQL via SQLAlchemy, REST via httpx — because a second way to
read a database is a second thing to keep correct.

The SQL and REST connectors take a JSON *descriptor* file. Sources hold their
secret by reference, so the descriptor is materialized in a temp file at sync
time, containing the resolved credential, and deleted in a ``finally`` — the
credential exists on disk only inside one sync, never in the registry, and
never where an API could serve it.
"""
from __future__ import annotations

import json
import os
import re
import tempfile
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

import pandas as pd

from app.core.logging import get_logger
from app.intelligence.connectors.base import ConnectorNotAvailable, ExtractedTable
from app.sync.registry import SOURCE_KINDS, AuthConfig

logger = get_logger(__name__)

# A document source is a heartbeat catalog scan, not a crawler.
MAX_DOCUMENTS_PER_SOURCE = 2_000


class SourceUnreadable(RuntimeError):
    """The source cannot be read as configured."""


def _records_table(name: str, source_name: str,
                   records: list[dict]) -> ExtractedTable:
    """Wrap reader-built records in the ExtractedTable shape the sync
    engine already consumes."""
    return ExtractedTable(name=name, source_file=source_name,
                          source_sheet=name, header_row=0,
                          df=pd.DataFrame(records))


def _strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", " ", text or "").replace("&nbsp;", " ").strip()


class SourceReader:
    """Reads a registered source into `ExtractedTable`s via the connectors."""

    def __init__(self, connectors, max_rows: int = 200_000):
        self._connectors = connectors
        self._max_rows = max_rows

    def read(self, source: dict, auth: AuthConfig) -> list[ExtractedTable]:
        spec = SOURCE_KINDS[source["kind"]]
        if spec.capability != "native":
            raise SourceUnreadable(
                f"{spec.title} is not readable yet: {spec.unavailable_reason}")
        if spec.connector == "sql":
            return self._read_sql(source, auth)
        if spec.connector == "api":
            return self._read_api(source, auth)
        if spec.connector == "documents":
            return self._read_documents(source)
        if spec.connector == "graph":
            return self._read_graph(source, auth)
        return self._read_files(source)

    # ------------------------------------------------------------- files
    def _read_files(self, source: dict) -> list[ExtractedTable]:
        """CSV/Excel: ``location`` is a file or a directory of files."""
        path = Path(source["location"]).expanduser()
        if not path.exists():
            raise SourceUnreadable(f"path does not exist: {path}")
        paths = sorted(p for p in path.iterdir()
                       if p.is_file()) if path.is_dir() else [path]
        tables: list[ExtractedTable] = []
        for file_path in paths:
            try:
                connector = self._connectors.for_file(file_path)
            except ConnectorNotAvailable:
                continue  # a directory may hold files this source does not own
            tables.extend(connector.extract(file_path).tables)
        if not tables:
            raise SourceUnreadable(f"no readable tables found at {path}")
        return tables

    # -------------------------------------------------- documents (V2)
    def _read_documents(self, source: dict) -> list[ExtractedTable]:
        """Document folders (SOPs, RCAs, policies, meeting notes, OneDrive-
        synced directories): the extract is a *catalog* — one record per
        document with its content hash, so the sync engine's fingerprint
        diff detects new, updated, and removed documents. Parsing is
        Document Intelligence's job, downstream of the delta."""
        from app.documents.parser import DocumentParser
        from app.documents.pipeline import file_content_hash

        root = Path(source["location"]).expanduser()
        if not root.exists() or not root.is_dir():
            raise SourceUnreadable(f"document folder does not exist: {root}")
        extensions = set(DocumentParser.supported_extensions())
        records: list[dict] = []
        for path in sorted(root.rglob("*")):
            if not path.is_file() or path.suffix.lower() not in extensions:
                continue
            if path.name.startswith("~$"):  # Office lock files
                continue
            try:
                stat = path.stat()
                records.append({
                    "id": path.relative_to(root).as_posix(),
                    "name": path.name,
                    "extension": path.suffix.lower(),
                    "path": str(path),
                    "size": stat.st_size,
                    "modified_at": datetime.fromtimestamp(
                        stat.st_mtime, tz=timezone.utc).isoformat(),
                    "content_hash": file_content_hash(path),
                })
            except OSError as exc:
                logger.warning("Skipping unreadable document %s: %s",
                               path.name, exc)
            if len(records) >= MAX_DOCUMENTS_PER_SOURCE:
                break
        if not records:
            raise SourceUnreadable(f"no supported documents found in {root}")
        return [_records_table("documents", source["name"], records)]

    # ---------------------------------------------- Microsoft Graph (V2)
    def _read_graph(self, source: dict, auth: AuthConfig) -> list[ExtractedTable]:
        """Microsoft 365 through Graph: Outlook mail and Teams messages
        arrive as communications tables; SharePoint drives arrive as a
        document catalog with pre-authenticated download URLs."""
        from app.communication.graph import GraphClient

        client = GraphClient(auth.require(source["name"]))
        options = source.get("options") or {}
        kind = source["kind"]
        try:
            if kind == "outlook":
                return [self._graph_outlook(client, options, source)]
            if kind == "teams":
                return [self._graph_teams(client, options, source)]
            if kind == "sharepoint":
                return [self._graph_sharepoint(client, options, source)]
        except SourceUnreadable:
            raise
        except Exception as exc:  # noqa: BLE001 — Graph errors are readable text
            raise SourceUnreadable(f"Microsoft Graph read failed: {exc}")
        raise SourceUnreadable(f"unsupported Graph source kind: {kind}")

    @staticmethod
    def _graph_outlook(client, options: dict, source: dict) -> ExtractedTable:
        mailbox = options.get("mailbox", "")
        base = f"/users/{mailbox}" if mailbox else "/me"
        messages = client.get_all(
            f"{base}/messages",
            params={"$top": 50, "$select": "id,subject,from,toRecipients,"
                    "receivedDateTime,bodyPreview,importance,isRead"},
            limit=int(options.get("limit", 200)))
        records = [{
            "id": m.get("id", ""),
            "subject": m.get("subject", ""),
            "from": ((m.get("from") or {}).get("emailAddress") or {})
            .get("address", ""),
            "received_at": m.get("receivedDateTime", ""),
            "preview": (m.get("bodyPreview") or "")[:500],
            "importance": m.get("importance", ""),
            "read": bool(m.get("isRead")),
        } for m in messages]
        if not records:
            raise SourceUnreadable("mailbox returned no messages")
        return _records_table("emails", source["name"], records)

    @staticmethod
    def _graph_teams(client, options: dict, source: dict) -> ExtractedTable:
        team_id = options.get("team_id", "")
        channel_id = options.get("channel_id", "")
        if not team_id or not channel_id:
            raise SourceUnreadable(
                "a Teams source needs options {'team_id': ..., "
                "'channel_id': ...}")
        messages = client.get_all(
            f"/teams/{team_id}/channels/{channel_id}/messages",
            params={"$top": 50}, limit=int(options.get("limit", 200)))
        records = [{
            "id": m.get("id", ""),
            "author": ((m.get("from") or {}).get("user") or {})
            .get("displayName", ""),
            "created_at": m.get("createdDateTime", ""),
            "text": _strip_html((m.get("body") or {}).get("content", ""))[:800],
            "importance": m.get("importance", ""),
        } for m in messages if (m.get("body") or {}).get("content")]
        if not records:
            raise SourceUnreadable("channel returned no messages")
        return _records_table("messages", source["name"], records)

    @staticmethod
    def _graph_sharepoint(client, options: dict, source: dict) -> ExtractedTable:
        drive_id = options.get("drive_id", "")
        if drive_id:
            base = f"/drives/{drive_id}"
        else:
            site_id = options.get("site_id", "")
            if not site_id:
                raise SourceUnreadable(
                    "a SharePoint source needs options {'drive_id': ...} or "
                    "{'site_id': ...}")
            base = f"/sites/{site_id}/drive"
        folder = options.get("folder", "")
        path = (f"{base}/root:/{folder.strip('/')}:/children" if folder
                else f"{base}/root/children")
        items = client.get_all(path, params={"$top": 100},
                               limit=int(options.get("limit", 500)))
        records = [{
            "id": item.get("id", ""),
            "name": item.get("name", ""),
            "extension": Path(item.get("name", "")).suffix.lower(),
            "size": int(item.get("size") or 0),
            "modified_at": item.get("lastModifiedDateTime", ""),
            "content_hash": ((item.get("file") or {}).get("hashes") or {})
            .get("quickXorHash") or item.get("eTag", ""),
            "download_url": item.get("@microsoft.graph.downloadUrl", ""),
            "web_url": item.get("webUrl", ""),
        } for item in items if "file" in item]
        if not records:
            raise SourceUnreadable("drive returned no files")
        return _records_table("documents", source["name"], records)

    # --------------------------------------------------------------- sql
    def _read_sql(self, source: dict, auth: AuthConfig) -> list[ExtractedTable]:
        url = auth.require(source["name"])
        options = source.get("options") or {}
        descriptor = {"url": url}
        if options.get("tables"):
            descriptor["tables"] = options["tables"]
        with _descriptor_file(descriptor, ".sqlsource.json") as path:
            return self._extract_with("sql", path)

    # --------------------------------------------------------------- api
    def _read_api(self, source: dict, auth: AuthConfig) -> list[ExtractedTable]:
        options = source.get("options") or {}
        descriptor: dict[str, Any] = {
            "url": source["location"],
            "name": options.get("name") or source["name"],
        }
        if options.get("records_path"):
            descriptor["records_path"] = options["records_path"]
        token = auth.resolved()
        if token:
            header = options.get("auth_header", "Authorization")
            scheme = options.get("auth_scheme", "Bearer")
            descriptor["headers"] = {header: f"{scheme} {token}".strip()}
        with _descriptor_file(descriptor, ".apisource.json") as path:
            return self._extract_with("api", path)

    def _extract_with(self, connector_name: str, path: Path
                      ) -> list[ExtractedTable]:
        connector = next((c for c in self._connectors.all()
                          if c.name == connector_name), None)
        if connector is None:
            raise SourceUnreadable(f"connector '{connector_name}' is not "
                                   f"registered in this deployment")
        if not connector.available:
            raise SourceUnreadable(
                f"connector '{connector_name}' is unavailable: "
                f"{connector.unavailable_reason}")
        return connector.extract(path).tables


@contextmanager
def _descriptor_file(descriptor: dict, suffix: str) -> Iterator[Path]:
    """Write a connector descriptor holding a resolved credential, and remove
    it as soon as the read finishes — success or failure."""
    handle = tempfile.NamedTemporaryFile(
        mode="w", suffix=suffix, delete=False, encoding="utf-8")
    try:
        json.dump(descriptor, handle)
        handle.close()
        path = Path(handle.name)
        try:
            os.chmod(path, 0o600)  # best-effort; a no-op on some platforms
        except OSError:
            pass
        yield path
    finally:
        try:
            Path(handle.name).unlink(missing_ok=True)
        except OSError:  # noqa: PERF203 — cleanup must never mask the real error
            logger.warning("Could not remove temporary descriptor %s",
                           handle.name)
