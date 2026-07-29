---
id: SOP-UPI-RISK-030
type: sop
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-07T16:30:00
---

# SOP-UPI-RISK-030 — Fraud & risk response SOP

**SOP ID:** SOP-UPI-RISK-030  ·  **Owner:** Harsh Nanda
**Applies to:** UPI International and related flows

## Purpose
Standard operating procedure for handling a fraud / risk spike, first codified after
INC-2026-09.

## Procedure
1. Confirm the failure signature on the affected entity (YONO SBI-class).
2. Apply mitigation (failover / retry tuning / merchant comms as applicable).
3. Open an incident and start recovery monitoring.
4. Draft the RCA and decision; validate recovery in the daily report.

## References
Derived from RCA-2026-09 and decision DEC-2026-09.

Refs: INC-2026-09, RCA-2026-09, DEC-2026-09
