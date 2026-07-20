"""Enterprise Brain — the continuously evolving organizational intelligence
layer.

The Brain is NOT the LLM. It is the composition of the deterministic SDS
modules — Knowledge, Memory, Data/Schema Intelligence, Analytics, ML, Deep
Learning, Evidence Verification — plus the Prompt Engine. The LLM is only
one consumer of what the Brain produces.

Components:
- ``EnterpriseBrain``          — runtime: startup verification, the
  continuous learning pipeline, status and statistics.
- ``EnterpriseContextBuilder`` — the one unified Enterprise Context the
  Prompt Engine consumes (never raw data).
"""
from app.brain.brain import EnterpriseBrain
from app.brain.context import EnterpriseContextBuilder

__all__ = ["EnterpriseBrain", "EnterpriseContextBuilder"]
