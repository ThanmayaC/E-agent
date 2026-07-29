"""AI file understanding (V9.0).

Given any uploaded file, produce a structured understanding of it with no manual
preprocessing: detect the type, extract text / tables / entities / dates / KPIs,
generate a summary, tags and metadata, and surface recommendations. Text formats
are extracted in full; formats that need an unavailable library (scanned PDFs
without OCR, images without a vision model) degrade honestly to metadata rather
than inventing content.

It reuses the platform's :class:`DocumentParser` for docx/xlsx/csv/text and adds
pypdf for PDFs and native JSON / XML / ZIP / image handling. Entities and KPIs
are matched against the enterprise's own vocabulary (banks, PSPs, merchants,
products, KPI names) so an uploaded file connects to the Knowledge Graph.
"""
from __future__ import annotations

import io
import json
import re
import zipfile
from datetime import datetime
from pathlib import Path

from app.core.logging import get_logger
from app.documents.parser import DocumentParser

logger = get_logger(__name__)

try:
    import pypdf  # type: ignore
    _PYPDF_OK = True
except ImportError:  # pragma: no cover
    _PYPDF_OK = False

# Canonical UPI KPI vocabulary (matches the executive/ecosystem layers).
KPI_TERMS = [
    "success rate", "settlement", "technical decline", "business decline",
    "transactions", "merchant adoption", "upi lite", "autopay", "fraud",
    "complaints", "response time", "latency", "risk score", "market share",
    "revenue", "gmv", "churn", "retention", "adoption", "downtime",
]

TYPE_BY_EXT = {
    ".xlsx": "excel", ".xlsm": "excel", ".xls": "excel",
    ".csv": "csv", ".tsv": "csv",
    ".pdf": "pdf", ".docx": "word", ".doc": "word",
    ".pptx": "powerpoint", ".ppt": "powerpoint",
    ".png": "image", ".jpg": "image", ".jpeg": "image", ".gif": "image",
    ".webp": "image", ".bmp": "image", ".svg": "image",
    ".zip": "archive", ".json": "json", ".xml": "xml",
    ".txt": "text", ".md": "text", ".markdown": "text", ".log": "text",
}

_DATE_RE = re.compile(
    r"\b(\d{4}-\d{2}-\d{2}|\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|"
    r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2},?\s*\d{0,4})\b")
_MONEY_RE = re.compile(r"(?:₹|Rs\.?|INR)\s?[\d,]+(?:\.\d+)?\s?(?:cr|crore|lakh|k|M|bn)?",
                       re.IGNORECASE)
_PCT_RE = re.compile(r"\b\d{1,3}(?:\.\d+)?\s?%")
_EMAIL_RE = re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b")
_NUM_RE = re.compile(r"-?\d[\d,]*(?:\.\d+)?")


class FileUnderstanding:
    """Turns a saved file into a structured understanding dict."""

    def __init__(self, vocab: dict | None = None):
        # vocab: {"banks": [...], "psps": [...], "merchants": [...],
        #         "products": [...], "features": [...]}
        self._vocab = vocab or {}
        self._parser = DocumentParser()

    # ------------------------------------------------------------- public
    def understand(self, path: Path) -> dict:
        path = Path(path)
        ext = path.suffix.lower()
        ftype = TYPE_BY_EXT.get(ext, "unknown")
        size = path.stat().st_size if path.exists() else 0
        text, tables, extra = self._extract(path, ext, ftype)
        text = text or ""
        entities = self._entities(text)
        dates = self._dedupe(_DATE_RE.findall(text))[:25]
        kpis = self._kpis(text)
        money = self._dedupe(_MONEY_RE.findall(text))[:25]
        percentages = self._dedupe(_PCT_RE.findall(text))[:25]
        emails = self._dedupe(_EMAIL_RE.findall(text))[:25]
        summary = self._summary(text, ftype, tables)
        tags = self._tags(ftype, entities, kpis, text)
        recommendations = self._recommendations(text, kpis, entities, ftype)
        words = len(text.split())
        return {
            "file": path.name,
            "type": ftype,
            "extension": ext,
            "size_bytes": size,
            "understood_at": datetime.now().isoformat(timespec="seconds"),
            "metadata": {
                "words": words,
                "characters": len(text),
                "tables": len(tables),
                "chunks_for_embedding": max(1, words // 220) if words else 0,
                **extra,
            },
            "summary": summary,
            "text_excerpt": text[:2000],
            "tables": tables[:10],
            "entities": entities,
            "dates": dates,
            "kpis": kpis,
            "money": money,
            "percentages": percentages,
            "emails": emails,
            "tags": tags,
            "recommendations": recommendations,
            "kg_links": self._kg_links(entities),
        }

    # --------------------------------------------------------- extraction
    def _extract(self, path: Path, ext: str, ftype: str):
        """Return (text, tables, extra_metadata)."""
        try:
            if ftype == "pdf":
                return self._pdf(path)
            if ftype == "json":
                return self._json(path)
            if ftype == "xml":
                return self._xml(path)
            if ftype == "archive":
                return self._zip(path)
            if ftype == "image":
                return ("", [], {"note": "image stored; no vision model "
                                 "available for chart/figure extraction",
                                 "vision_available": False})
            if ftype in ("excel", "csv"):
                return self._tabular(path)
            # docx / pptx / text via the shared parser
            parsed = self._parser.parse(path)
            return (parsed.text, [], {"pages": parsed.pages,
                                      "parser": parsed.parser,
                                      "warnings": parsed.warnings})
        except Exception as exc:  # noqa: BLE001 — never break on one file
            logger.exception("understanding extraction failed for %s", path.name)
            return ("", [], {"error": str(exc)[:200]})

    def _pdf(self, path: Path):
        parsed = self._parser.parse(path)
        if parsed.parsed:
            return (parsed.text, [], {"pages": parsed.pages, "parser": "pdfplumber"})
        if _PYPDF_OK:
            reader = pypdf.PdfReader(str(path))
            text = "\n\n".join((pg.extract_text() or "") for pg in reader.pages)
            return (text[:400_000], [],
                    {"pages": len(reader.pages), "parser": "pypdf"})
        return ("", [], {"parser": "pdf",
                         "warnings": ["no PDF text extractor available"]})

    def _tabular(self, path: Path):
        parsed = self._parser.parse(path)
        tables = self._tables_from_text(parsed.text)
        return (parsed.text, tables, {"parser": parsed.parser,
                                      "warnings": parsed.warnings})

    @staticmethod
    def _tables_from_text(text: str) -> list[dict]:
        """Best-effort table capture: the parser renders sheets/CSVs as lines;
        capture header + a few sample rows for preview."""
        tables: list[dict] = []
        block: list[str] = []
        for line in text.splitlines():
            if "|" in line or "\t" in line or line.count(",") >= 2:
                block.append(line)
            elif block:
                if len(block) >= 2:
                    tables.append({"rows": len(block),
                                   "preview": block[:6]})
                block = []
        if len(block) >= 2:
            tables.append({"rows": len(block), "preview": block[:6]})
        return tables

    def _json(self, path: Path):
        raw = path.read_text(encoding="utf-8", errors="ignore")[:400_000]
        try:
            obj = json.loads(raw)
            keys = list(obj.keys()) if isinstance(obj, dict) else []
            n = len(obj) if isinstance(obj, (list, dict)) else 1
            return (json.dumps(obj, indent=2)[:400_000], [],
                    {"json_keys": keys[:40], "json_items": n})
        except Exception:  # noqa: BLE001
            return (raw, [], {"warnings": ["invalid JSON; treated as text"]})

    def _xml(self, path: Path):
        raw = path.read_text(encoding="utf-8", errors="ignore")[:400_000]
        tags = self._dedupe(re.findall(r"<([A-Za-z_][\w.-]*)", raw))[:40]
        return (raw, [], {"xml_tags": tags})

    def _zip(self, path: Path):
        members: list[str] = []
        texts: list[str] = []
        try:
            with zipfile.ZipFile(path) as zf:
                for info in zf.infolist()[:200]:
                    members.append(info.filename)
                    ext = Path(info.filename).suffix.lower()
                    if ext in (".txt", ".md", ".csv", ".json", ".xml") and info.file_size < 500_000:
                        with zf.open(info) as fh:
                            texts.append(f"# {info.filename}\n" +
                                         fh.read().decode("utf-8", "ignore"))
        except Exception as exc:  # noqa: BLE001
            return ("", [], {"error": f"zip read failed: {exc}"[:200]})
        return ("\n\n".join(texts)[:400_000], [],
                {"archive_members": members[:60], "member_count": len(members)})

    # ----------------------------------------------------------- analysis
    def _entities(self, text: str) -> dict:
        low = text.lower()
        found: dict[str, list[str]] = {}
        for kind in ("banks", "psps", "merchants", "products", "features"):
            hits = [name for name in self._vocab.get(kind, [])
                    if name and name.lower() in low]
            if hits:
                found[kind] = self._dedupe(hits)[:20]
        return found

    def _kpis(self, text: str) -> list[dict]:
        out: list[dict] = []
        low = text.lower()
        for term in KPI_TERMS:
            idx = low.find(term)
            if idx == -1:
                continue
            window = text[max(0, idx - 40):idx + len(term) + 60]
            nums = _NUM_RE.findall(window)
            out.append({"kpi": term,
                        "values": self._dedupe(nums)[:4]})
        # de-dup by kpi term
        seen, uniq = set(), []
        for k in out:
            if k["kpi"] not in seen:
                seen.add(k["kpi"])
                uniq.append(k)
        return uniq[:15]

    def _summary(self, text: str, ftype: str, tables: list) -> str:
        text = (text or "").strip()
        if not text:
            return (f"{ftype.title()} file — no extractable text "
                    f"(stored for reference).")
        sentences = re.split(r"(?<=[.!?])\s+", text.replace("\n", " "))
        sentences = [s.strip() for s in sentences if len(s.strip()) > 30]
        if not sentences:
            head = " ".join(text.split()[:60])
            return head + ("…" if len(text) > len(head) else "")
        # extractive: rank sentences by keyword density (entities + KPI terms)
        vocab_terms = [t for lst in self._vocab.values() for t in lst]
        keywords = [k.lower() for k in KPI_TERMS + vocab_terms]

        def score(s: str) -> int:
            sl = s.lower()
            return sum(1 for k in keywords if k in sl) + (1 if any(
                ch.isdigit() for ch in s) else 0)
        ranked = sorted(sentences[:200], key=score, reverse=True)
        top = ranked[:4] if any(score(s) for s in sentences[:200]) else sentences[:3]
        # keep original order for readability
        top_set = set(top)
        ordered = [s for s in sentences if s in top_set][:4]
        summary = " ".join(ordered)
        return summary[:800] + ("…" if len(summary) > 800 else "")

    def _tags(self, ftype: str, entities: dict, kpis: list, text: str) -> list[str]:
        tags = [ftype]
        for kind, names in entities.items():
            tags.append(kind)
            tags.extend(names[:3])
        tags.extend(k["kpi"] for k in kpis[:4])
        low = text.lower()
        for topic in ("incident", "rca", "settlement", "fraud", "forecast",
                      "roadmap", "quarterly", "monthly", "board", "compliance"):
            if topic in low:
                tags.append(topic)
        return self._dedupe(tags)[:16]

    def _recommendations(self, text: str, kpis: list, entities: dict,
                         ftype: str) -> list[str]:
        recs: list[str] = []
        low = text.lower()
        if any(w in low for w in ("decline", "drop", "decrease", "dip", "fell",
                                  "down ", "outage", "failure")):
            recs.append("Contains adverse signals — cross-check against the "
                        "ecosystem anomalies and open a follow-up review.")
        if "incident" in low or "rca" in low:
            recs.append("Incident/RCA content — link to related decisions and "
                        "confirm the remediation SOP is current.")
        if entities.get("banks"):
            recs.append(f"References banks ({', '.join(entities['banks'][:3])}) "
                        "— compare with bank evolution / market-share trends.")
        if entities.get("merchants"):
            recs.append("Merchant data present — reconcile with merchant "
                        "lifecycle and settlement health.")
        if ftype in ("excel", "csv"):
            recs.append("Tabular data — ask the AI to summarise, find anomalies, "
                        "or compare it with another file.")
        if not recs:
            recs.append("Ask the AI to summarise this file, extract action items, "
                        "or generate an executive report from it.")
        return recs[:5]

    def _kg_links(self, entities: dict) -> list[dict]:
        links = []
        for kind, names in entities.items():
            for n in names:
                links.append({"type": kind[:-1] if kind.endswith("s") else kind,
                              "name": n})
        return links[:30]

    @staticmethod
    def _dedupe(items: list[str]) -> list[str]:
        seen, out = set(), []
        for it in items:
            key = it.strip()
            if key and key.lower() not in seen:
                seen.add(key.lower())
                out.append(key)
        return out
