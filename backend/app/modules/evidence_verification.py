"""Evidence Verification Module (SDS §2.9).

The control-plane system of record: typed evidence extraction from the
business context, the append-only Evidence Ledger (runs, node events,
evidence records, AI statements with citations and verdicts, report
versions, audit log). The deterministic verifier agent node that scores
statement verdicts is built by the Supervisor/orchestration layer and reads
from this ledger.
"""
from app.evidence.extract import content_hash, extract_evidence
from app.evidence.ledger import EvidenceLedger

__all__ = ["content_hash", "extract_evidence", "EvidenceLedger"]
