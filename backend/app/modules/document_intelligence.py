"""Document Intelligence Module (SDS §2.1) — status: partial.

Implemented: table extraction from PDF (pdfplumber) and Word (python-docx)
documents via the Observation Module's connector contract.

SDS scope still open: document understanding beyond tables — narrative
sections, contracts, semantic document search. Those capabilities land
here, reusing the connector extracts as input.
"""
from app.intelligence.connectors.pdf import PDFConnector
from app.intelligence.connectors.word import WordConnector

__all__ = ["PDFConnector", "WordConnector"]
