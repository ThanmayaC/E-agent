"""Document parsing — one text extractor per format.

Every parser is optional-dependency-aware in the same way the data
connectors are: a missing library makes the format report itself
unavailable with an install hint; it never breaks the pipeline.

OCR is a *fallback*, not a stage: it runs only when a PDF page yields no
text layer (a scan) and the optional OCR stack (pytesseract + Pillow) is
installed. A deployment without OCR still parses every born-digital
document; scanned pages are recorded as unparsed rather than invented.
"""
from __future__ import annotations

import csv as csv_module
from dataclasses import dataclass, field
from pathlib import Path

from app.core.logging import get_logger

logger = get_logger(__name__)

try:
    import pdfplumber  # type: ignore
    _PDF_OK = True
except ImportError:
    _PDF_OK = False

try:
    import docx  # type: ignore
    _DOCX_OK = True
except ImportError:
    _DOCX_OK = False

try:
    from pptx import Presentation  # type: ignore
    _PPTX_OK = True
except ImportError:
    _PPTX_OK = False

try:
    import openpyxl  # type: ignore
    _XLSX_OK = True
except ImportError:
    _XLSX_OK = False

try:
    import pytesseract  # type: ignore
    from PIL import Image  # type: ignore  # noqa: F401 — capability probe
    _OCR_OK = True
except ImportError:
    _OCR_OK = False

MAX_TEXT_CHARS = 400_000
MAX_SHEET_ROWS = 500
MAX_CSV_ROWS = 500
TEXT_EXTENSIONS = (".md", ".markdown", ".txt", ".text", ".log", ".rst")


@dataclass
class ParsedDocument:
    """What parsing one document produced."""
    text: str = ""
    pages: int = 0
    parser: str = ""
    ocr_used: bool = False
    warnings: list[str] = field(default_factory=list)

    @property
    def parsed(self) -> bool:
        return bool(self.text.strip())


class DocumentParser:
    """Extracts plain text from every supported document format."""

    def __init__(self, ocr_enabled: bool = True):
        self._ocr_enabled = ocr_enabled

    # ------------------------------------------------------------ catalogue
    @staticmethod
    def formats() -> list[dict]:
        """What this deployment can parse, and what an admin must install
        to parse more."""
        return [
            {"format": "pdf", "extensions": [".pdf"], "available": _PDF_OK,
             "requires": "" if _PDF_OK else "pip install pdfplumber"},
            {"format": "docx", "extensions": [".docx"], "available": _DOCX_OK,
             "requires": "" if _DOCX_OK else "pip install python-docx"},
            {"format": "pptx", "extensions": [".pptx"], "available": _PPTX_OK,
             "requires": "" if _PPTX_OK else "pip install python-pptx"},
            {"format": "excel", "extensions": [".xlsx", ".xlsm"],
             "available": _XLSX_OK,
             "requires": "" if _XLSX_OK else "pip install openpyxl"},
            {"format": "csv", "extensions": [".csv", ".tsv"],
             "available": True, "requires": ""},
            {"format": "text", "extensions": list(TEXT_EXTENSIONS),
             "available": True, "requires": ""},
            {"format": "ocr", "extensions": [".pdf (scanned pages)"],
             "available": _OCR_OK,
             "requires": "" if _OCR_OK
             else "pip install pytesseract pillow (plus the tesseract binary)"},
        ]

    @classmethod
    def supported_extensions(cls) -> tuple[str, ...]:
        return (".pdf", ".docx", ".pptx", ".xlsx", ".xlsm", ".csv", ".tsv",
                *TEXT_EXTENSIONS)

    def can_parse(self, path: Path) -> bool:
        return path.suffix.lower() in self.supported_extensions()

    # ---------------------------------------------------------------- parse
    def parse(self, path: Path) -> ParsedDocument:
        """Parse one document. Never raises: an unparseable document is a
        ParsedDocument with warnings, because one broken file must not stop
        the folder it lives in."""
        suffix = path.suffix.lower()
        try:
            if suffix == ".pdf":
                return self._parse_pdf(path)
            if suffix == ".docx":
                return self._parse_docx(path)
            if suffix == ".pptx":
                return self._parse_pptx(path)
            if suffix in (".xlsx", ".xlsm"):
                return self._parse_excel(path)
            if suffix in (".csv", ".tsv"):
                return self._parse_csv(path)
            if suffix in TEXT_EXTENSIONS:
                return self._parse_text(path)
            return ParsedDocument(warnings=[f"unsupported format: {suffix}"])
        except Exception as exc:  # noqa: BLE001 — degrade per document
            logger.exception("Parsing failed for %s", path.name)
            return ParsedDocument(parser=suffix.lstrip("."),
                                  warnings=[f"parse failed: {exc}"[:200]])

    # ------------------------------------------------------------- formats
    def _parse_pdf(self, path: Path) -> ParsedDocument:
        if not _PDF_OK:
            return ParsedDocument(
                parser="pdf", warnings=["pdfplumber is not installed"])
        parsed = ParsedDocument(parser="pdf")
        texts: list[str] = []
        with pdfplumber.open(path) as pdf:
            parsed.pages = len(pdf.pages)
            for page in pdf.pages:
                text = (page.extract_text() or "").strip()
                if not text and self._ocr_enabled and _OCR_OK:
                    text = self._ocr_page(page)
                    if text:
                        parsed.ocr_used = True
                if text:
                    texts.append(text)
        parsed.text = "\n\n".join(texts)[:MAX_TEXT_CHARS]
        if not parsed.text and not _OCR_OK:
            parsed.warnings.append(
                "no text layer found; OCR stack not installed")
        return parsed

    @staticmethod
    def _ocr_page(page) -> str:
        """OCR one scanned PDF page. Best effort — a page that resists OCR
        is skipped, not fatal."""
        try:
            image = page.to_image(resolution=200).original
            return (pytesseract.image_to_string(image) or "").strip()
        except Exception:  # noqa: BLE001
            logger.warning("OCR failed for a page", exc_info=True)
            return ""

    @staticmethod
    def _parse_docx(path: Path) -> ParsedDocument:
        if not _DOCX_OK:
            return ParsedDocument(
                parser="docx", warnings=["python-docx is not installed"])
        document = docx.Document(str(path))
        parts = [p.text.strip() for p in document.paragraphs if p.text.strip()]
        for table in document.tables:
            for row in table.rows:
                cells = [c.text.strip() for c in row.cells if c.text.strip()]
                if cells:
                    parts.append(" | ".join(cells))
        return ParsedDocument(text="\n\n".join(parts)[:MAX_TEXT_CHARS],
                              pages=len(parts), parser="docx")

    @staticmethod
    def _parse_pptx(path: Path) -> ParsedDocument:
        if not _PPTX_OK:
            return ParsedDocument(
                parser="pptx", warnings=["python-pptx is not installed"])
        presentation = Presentation(str(path))
        slides: list[str] = []
        for number, slide in enumerate(presentation.slides, start=1):
            texts = [shape.text.strip() for shape in slide.shapes
                     if getattr(shape, "has_text_frame", False)
                     and shape.text.strip()]
            notes = ""
            if slide.has_notes_slide and slide.notes_slide.notes_text_frame:
                notes = slide.notes_slide.notes_text_frame.text.strip()
            body = "\n".join(texts + ([f"Notes: {notes}"] if notes else []))
            if body:
                slides.append(f"[Slide {number}]\n{body}")
        return ParsedDocument(text="\n\n".join(slides)[:MAX_TEXT_CHARS],
                              pages=len(presentation.slides), parser="pptx")

    @staticmethod
    def _parse_excel(path: Path) -> ParsedDocument:
        if not _XLSX_OK:
            return ParsedDocument(
                parser="excel", warnings=["openpyxl is not installed"])
        workbook = openpyxl.load_workbook(path, read_only=True, data_only=True)
        sheets: list[str] = []
        try:
            for sheet in workbook.worksheets:
                lines = []
                for row in sheet.iter_rows(max_row=MAX_SHEET_ROWS,
                                           values_only=True):
                    cells = [str(v).strip() for v in row
                             if v is not None and str(v).strip()]
                    if cells:
                        lines.append(" | ".join(cells))
                if lines:
                    sheets.append(f"[Sheet {sheet.title}]\n" + "\n".join(lines))
        finally:
            workbook.close()
        return ParsedDocument(text="\n\n".join(sheets)[:MAX_TEXT_CHARS],
                              pages=len(sheets), parser="excel")

    @staticmethod
    def _parse_csv(path: Path) -> ParsedDocument:
        delimiter = "\t" if path.suffix.lower() == ".tsv" else ","
        lines: list[str] = []
        with path.open("r", encoding="utf-8", errors="replace",
                       newline="") as handle:
            for i, row in enumerate(csv_module.reader(handle,
                                                      delimiter=delimiter)):
                if i >= MAX_CSV_ROWS:
                    break
                cells = [c.strip() for c in row if c.strip()]
                if cells:
                    lines.append(" | ".join(cells))
        return ParsedDocument(text="\n".join(lines)[:MAX_TEXT_CHARS],
                              pages=1, parser="csv")

    @staticmethod
    def _parse_text(path: Path) -> ParsedDocument:
        text = path.read_text(encoding="utf-8", errors="replace")
        return ParsedDocument(text=text[:MAX_TEXT_CHARS], pages=1,
                              parser="text")
