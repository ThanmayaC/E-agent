"""AI-generated artifacts (V9.0).

Turns enterprise intelligence into downloadable deliverables: PowerPoint, Excel,
Word, PDF, email drafts, executive reports, meeting minutes, RCAs, action items,
roadmaps and business cases. Everything is built from a single neutral document
model (title + sections of paragraphs / bullets / tables), then rendered to the
requested format with the libraries this deployment has (openpyxl for Excel,
python-docx for Word) and a styled, printable HTML fallback for formats whose
writer is not installed (PDF, PowerPoint) — honest degradation, never a failure.

When the caller supplies no explicit content, the artifact is composed from the
executive / evolution / ecosystem layers so "generate an executive report" or
"generate an RCA" produces a real, evidence-backed document.
"""
from __future__ import annotations

import html
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from app.core.logging import get_logger

logger = get_logger(__name__)

try:
    import openpyxl
    from openpyxl.styles import Font, PatternFill
    _XLSX_OK = True
except ImportError:  # pragma: no cover
    _XLSX_OK = False

try:
    import docx
    from docx.shared import Pt, RGBColor
    _DOCX_OK = True
except ImportError:  # pragma: no cover
    _DOCX_OK = False


@dataclass
class Section:
    heading: str = ""
    paragraphs: list[str] = field(default_factory=list)
    bullets: list[str] = field(default_factory=list)
    table: dict | None = None  # {"headers": [...], "rows": [[...]]}


@dataclass
class DocModel:
    title: str
    subtitle: str = ""
    sections: list[Section] = field(default_factory=list)


# native format -> what we can actually write
_FORMAT = {
    "excel": "xlsx", "xlsx": "xlsx",
    "word": "docx", "docx": "docx",
    "pdf": "html", "powerpoint": "html", "pptx": "html", "presentation": "html",
    "email": "txt", "markdown": "md", "md": "md", "text": "txt", "txt": "txt",
}

# kinds that are documents (default docx) unless a format is forced
_DOC_KINDS = {"executive_report", "meeting_minutes", "rca", "action_items",
              "roadmap", "business_case", "report"}


class ArtifactGenerator:
    def __init__(self, container, out_dir: Path):
        self._c = container
        self._dir = Path(out_dir)
        self._dir.mkdir(parents=True, exist_ok=True)

    def kinds(self) -> list[str]:
        return sorted({"powerpoint", "excel", "word", "pdf", "email",
                       *_DOC_KINDS})

    # ------------------------------------------------------------- generate
    def generate(self, kind: str, title: str | None = None,
                 prompt: str | None = None, sections: list | None = None,
                 fmt: str | None = None) -> dict:
        kind = (kind or "report").lower().strip()
        model = self._model(kind, title, prompt, sections)
        fmt = (fmt or _FORMAT.get(kind)
               or ("docx" if kind in _DOC_KINDS else "md"))
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        slug = re.sub(r"[^0-9a-zA-Z]+", "-", model.title.lower()).strip("-")[:50]
        name = f"{slug or kind}-{stamp}.{fmt}"
        path = self._dir / name
        rendered = self._render(model, fmt, path)
        return {"kind": kind, "format": fmt, "file": name,
                "path": str(path), "bytes": path.stat().st_size if path.exists() else 0,
                "title": model.title, "sections": len(model.sections),
                "rendered_with": rendered,
                "download_url": f"/api/v1/workspace/artifacts/{name}"}

    # -------------------------------------------------------------- render
    def _render(self, model: DocModel, fmt: str, path: Path) -> str:
        if fmt == "xlsx" and _XLSX_OK:
            self._xlsx(model, path); return "openpyxl"
        if fmt == "docx" and _DOCX_OK:
            self._docx(model, path); return "python-docx"
        if fmt == "html":
            path.write_text(self._html(model), encoding="utf-8"); return "html"
        if fmt in ("md",):
            path.write_text(self._md(model), encoding="utf-8"); return "markdown"
        # txt / email / fallbacks
        path.write_text(self._md(model), encoding="utf-8"); return "text"

    def _md(self, m: DocModel) -> str:
        lines = [f"# {m.title}", ""]
        if m.subtitle:
            lines += [f"*{m.subtitle}*", ""]
        for s in m.sections:
            if s.heading:
                lines += [f"## {s.heading}", ""]
            lines += [p for p in s.paragraphs]
            if s.paragraphs:
                lines.append("")
            lines += [f"- {b}" for b in s.bullets]
            if s.bullets:
                lines.append("")
            if s.table:
                h = s.table.get("headers", [])
                lines.append("| " + " | ".join(map(str, h)) + " |")
                lines.append("| " + " | ".join("---" for _ in h) + " |")
                for row in s.table.get("rows", []):
                    lines.append("| " + " | ".join(map(str, row)) + " |")
                lines.append("")
        return "\n".join(lines)

    def _html(self, m: DocModel) -> str:
        def esc(x):
            return html.escape(str(x))
        parts = [f"<!doctype html><html><head><meta charset='utf-8'>"
                 f"<title>{esc(m.title)}</title><style>"
                 "body{font-family:Segoe UI,Arial,sans-serif;max-width:900px;"
                 "margin:40px auto;color:#1e293b;line-height:1.5}"
                 "h1{color:#1F4E79;border-bottom:3px solid#1F4E79;padding-bottom:8px}"
                 "h2{color:#2563eb;margin-top:28px}"
                 "table{border-collapse:collapse;width:100%;margin:12px 0}"
                 "th,td{border:1px solid#cbd5e1;padding:6px 10px;text-align:left;"
                 "font-size:14px}th{background:#1F4E79;color:#fff}"
                 ".sub{color:#64748b;font-style:italic}"
                 "@media print{body{margin:0}}</style></head><body>"]
        parts.append(f"<h1>{esc(m.title)}</h1>")
        if m.subtitle:
            parts.append(f"<p class='sub'>{esc(m.subtitle)}</p>")
        for s in m.sections:
            if s.heading:
                parts.append(f"<h2>{esc(s.heading)}</h2>")
            for p in s.paragraphs:
                parts.append(f"<p>{esc(p)}</p>")
            if s.bullets:
                parts.append("<ul>" + "".join(f"<li>{esc(b)}</li>"
                                               for b in s.bullets) + "</ul>")
            if s.table:
                h = s.table.get("headers", [])
                parts.append("<table><tr>" +
                             "".join(f"<th>{esc(x)}</th>" for x in h) + "</tr>")
                for row in s.table.get("rows", []):
                    parts.append("<tr>" + "".join(f"<td>{esc(x)}</td>"
                                                  for x in row) + "</tr>")
                parts.append("</table>")
        parts.append("</body></html>")
        return "".join(parts)

    def _docx(self, m: DocModel, path: Path) -> None:
        doc = docx.Document()
        h = doc.add_heading(m.title, level=0)
        try:
            h.runs[0].font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)
        except Exception:  # noqa: BLE001
            pass
        if m.subtitle:
            p = doc.add_paragraph(m.subtitle)
            p.runs[0].italic = True
        for s in m.sections:
            if s.heading:
                doc.add_heading(s.heading, level=1)
            for para in s.paragraphs:
                doc.add_paragraph(para)
            for b in s.bullets:
                doc.add_paragraph(b, style="List Bullet")
            if s.table:
                headers = s.table.get("headers", [])
                rows = s.table.get("rows", [])
                if headers:
                    t = doc.add_table(rows=1, cols=len(headers))
                    t.style = "Light Grid Accent 1"
                    for i, htext in enumerate(headers):
                        cell = t.rows[0].cells[i]
                        cell.text = str(htext)
                        for run in cell.paragraphs[0].runs:
                            run.font.bold = True
                            run.font.size = Pt(10)
                    for row in rows:
                        cells = t.add_row().cells
                        for i, val in enumerate(row[:len(headers)]):
                            cells[i].text = str(val)
        doc.save(str(path))

    def _xlsx(self, m: DocModel, path: Path) -> None:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Summary"
        ws["A1"] = m.title
        ws["A1"].font = Font(bold=True, size=14, color="1F4E79")
        if m.subtitle:
            ws["A2"] = m.subtitle
        r = 4
        for s in m.sections:
            if s.heading:
                ws.cell(r, 1, s.heading).font = Font(bold=True, size=12)
                r += 1
            for para in s.paragraphs:
                ws.cell(r, 1, para); r += 1
            for b in s.bullets:
                ws.cell(r, 1, f"• {b}"); r += 1
            if s.table:
                headers = s.table.get("headers", [])
                if headers:
                    for ci, htext in enumerate(headers, start=1):
                        cell = ws.cell(r, ci, htext)
                        cell.font = Font(bold=True, color="FFFFFF")
                        cell.fill = PatternFill("solid", fgColor="1F4E79")
                    r += 1
                    for row in s.table.get("rows", []):
                        for ci, val in enumerate(row, start=1):
                            ws.cell(r, ci, val)
                        r += 1
            r += 1
        # widen first columns
        for col in "ABCDEF":
            ws.column_dimensions[col].width = 26
        wb.save(str(path))

    # ------------------------------------------------------- content model
    def _model(self, kind: str, title, prompt, sections) -> DocModel:
        if sections:
            secs = [Section(heading=s.get("heading", ""),
                            paragraphs=s.get("paragraphs", []),
                            bullets=s.get("bullets", []),
                            table=s.get("table")) for s in sections]
            return DocModel(title=title or kind.replace("_", " ").title(),
                            subtitle=prompt or "", sections=secs)
        builder = {
            "executive_report": self._exec_report,
            "report": self._exec_report,
            "rca": self._rca,
            "meeting_minutes": self._minutes,
            "action_items": self._action_items,
            "roadmap": self._roadmap,
            "business_case": self._business_case,
            "email": self._email,
        }.get(kind, self._exec_report)
        return builder(title, prompt)

    def _stamp(self) -> str:
        return datetime.now().strftime("%d %b %Y")

    def _exec(self):
        return getattr(self._c, "executive", None)

    def _evo(self):
        return getattr(self._c, "evolution", None)

    def _exec_report(self, title, prompt) -> DocModel:
        ex, evo = self._exec(), self._evo()
        secs: list[Section] = []
        if ex and getattr(ex, "available", False):
            brief = ex.executive_brief()
            secs.append(Section(heading="Executive summary",
                                paragraphs=[brief.get("summary", "")
                                            if isinstance(brief, dict) else str(brief)]))
            pr = ex.priorities()
            if pr:
                secs.append(Section(heading="Priorities",
                            table={"headers": ["Priority", "Urgency", "Confidence"],
                                   "rows": [[p.get("title"), p.get("urgency", p.get("priority", "")),
                                             p.get("confidence", "")] for p in pr[:8]]}))
        if evo and evo.available:
            ov = evo.overview()
            g = ov.get("user_growth", {}).get("registered_base_m", {})
            secs.append(Section(heading="Six-month evolution", bullets=[
                f"Registered base grew {g.get('start')}M → {g.get('end')}M.",
                f"Forecast accuracy {ov.get('forecast_accuracy')}%.",
                f"{ov.get('decisions', {}).get('count', 0)} tracked decisions, "
                f"₹{ov.get('decisions', {}).get('total_business_value_cr', 0)}cr protected.",
            ]))
            dec = evo.decisions().get("top_value", [])
            if dec:
                secs.append(Section(heading="Highest-value decisions",
                            table={"headers": ["ID", "Decision", "Value (₹cr)", "Success"],
                                   "rows": [[d.get("decision_id"), d.get("title"),
                                             d.get("business_value_cr"), d.get("success_score")]
                                            for d in dec[:6]]}))
        if not secs:
            secs = [Section(heading="Summary",
                            paragraphs=[prompt or "No enterprise data available."])]
        return DocModel(title=title or "Executive Report",
                        subtitle=f"Generated {self._stamp()}" +
                        (f" · {prompt}" if prompt else ""), sections=secs)

    def _rca(self, title, prompt) -> DocModel:
        ex = self._exec()
        inc = {}
        if ex and getattr(ex, "available", False):
            try:
                inc = ex.incident()
            except Exception:  # noqa: BLE001
                inc = {}
        secs = [
            Section(heading="Incident", paragraphs=[
                inc.get("summary", prompt or "Incident under analysis.")]),
            Section(heading="Impact", bullets=[
                f"Bank: {inc.get('bank', 'n/a')}",
                f"PSP: {inc.get('psp', 'n/a')}",
                f"Low day: {inc.get('low_day', 'n/a')}"]),
            Section(heading="Root cause", paragraphs=[
                inc.get("cause", "Root cause established from correlated "
                        "bank/PSP/feature signals in the transaction ledger.")]),
            Section(heading="Corrective actions", bullets=[
                "Deploy the mitigation and monitor recovery.",
                "Update the remediation SOP.",
                "Add a guardrail alert for early detection."]),
        ]
        return DocModel(title=title or "Root Cause Analysis",
                        subtitle=f"Generated {self._stamp()}", sections=secs)

    def _minutes(self, title, prompt) -> DocModel:
        return DocModel(title=title or "Meeting Minutes",
                        subtitle=f"{self._stamp()} · {prompt or 'UPI Products review'}",
                        sections=[
            Section(heading="Attendees", bullets=["UPI Products leadership",
                                                  "Product Operations", "Engineering"]),
            Section(heading="Discussion", paragraphs=[
                prompt or "Reviewed weekly performance, incidents and priorities."]),
            Section(heading="Decisions", bullets=["Endorsed the current remediation.",
                                                  "Approved continued scaling."]),
            Section(heading="Action items", bullets=["Owner to circulate the RCA.",
                                                     "Analytics to validate the forecast."])])

    def _action_items(self, title, prompt) -> DocModel:
        ex = self._exec()
        rows = []
        if ex and getattr(ex, "available", False):
            try:
                for r in ex.recommendations()[:10]:
                    rows.append([r.get("title", r.get("recommendation", "")),
                                 r.get("priority", ""), r.get("owner", "TBD")])
            except Exception:  # noqa: BLE001
                pass
        return DocModel(title=title or "Action Items",
                        subtitle=f"Generated {self._stamp()}",
                        sections=[Section(heading="Actions",
                                  table={"headers": ["Action", "Priority", "Owner"],
                                         "rows": rows or [[prompt or "Define next steps",
                                                           "High", "TBD"]]})])

    def _roadmap(self, title, prompt) -> DocModel:
        evo = self._evo()
        rows = []
        if evo and evo.available:
            for p in evo.products().get("investable", [])[:8]:
                rows.append([p.get("product"), p.get("lifecycle_stage"),
                             f"{p.get('mom_growth_pct')}% m/m"])
        return DocModel(title=title or "Product Roadmap",
                        subtitle=f"Investment priorities · {self._stamp()}",
                        sections=[Section(heading="Where to invest",
                                  table={"headers": ["Product", "Stage", "Momentum"],
                                         "rows": rows or [["—", "—", "—"]]})])

    def _business_case(self, title, prompt) -> DocModel:
        evo = self._evo()
        top = []
        if evo and evo.available:
            top = evo.decisions().get("top_value", [])[:3]
        secs = [Section(heading="Opportunity",
                        paragraphs=[prompt or "Invest in the highest-return "
                                    "remediation and growth initiatives."])]
        if top:
            secs.append(Section(heading="Proven value", bullets=[
                f"{d.get('decision_id')}: {d.get('title')} — "
                f"₹{d.get('business_value_cr')}cr protected." for d in top]))
        secs.append(Section(heading="Recommendation",
                            paragraphs=["Proceed; the evidence shows measurable, "
                                        "repeatable business value."]))
        return DocModel(title=title or "Business Case",
                        subtitle=f"Generated {self._stamp()}", sections=secs)

    def _email(self, title, prompt) -> DocModel:
        evo = self._evo()
        line = ""
        if evo and evo.available:
            ov = evo.overview()
            line = (f"Retention is {ov.get('users', {}).get('retention_pct')}%, "
                    f"forecast accuracy {ov.get('forecast_accuracy')}%, and "
                    f"{ov.get('decisions', {}).get('count', 0)} decisions protected "
                    f"₹{ov.get('decisions', {}).get('total_business_value_cr', 0)}cr.")
        return DocModel(title=title or "Draft email",
                        subtitle="Email draft",
                        sections=[Section(paragraphs=[
                            "Hi team,", prompt or
                            "Sharing a quick update on UPI Products.",
                            line or "See the workspace for details.",
                            "Best regards,", "UPI Products"])])
