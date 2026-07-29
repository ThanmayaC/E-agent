---
id: SOP-UPI-RISK-030
type: sop
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-27T16:30:00
---

# SOP-UPI-RISK-030 — Fraud & risk response SOP

**SOP ID:** SOP-UPI-RISK-030  ·  **Owner:** Harsh Nanda
**Applies to:** UPI International and related flows

## Purpose
Standard operating procedure for handling a fraud / risk spike, first codified after
INC-2026-15.

## Procedure
1. Confirm the failure signature on the affected entity (FamApp-class).
2. Apply mitigation (failover / retry tuning / merchant comms as applicable).
3. Open an incident and start recovery monitoring.
4. Draft the RCA and decision; validate recovery in the daily report.

## References
Derived from RCA-2026-15 and decision DEC-2026-15.

Refs: INC-2026-15, RCA-2026-15, DEC-2026-15
