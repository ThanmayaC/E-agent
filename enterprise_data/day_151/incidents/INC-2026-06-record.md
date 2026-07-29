---
id: INC-2026-06
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-04T09:00:00
---

# Incident Record — INC-2026-06 UPI International bank timeout / 5xx spike

**Incident ID:** INC-2026-06  ·  **Severity:** Sev-2  ·  **Status:** Investigating
**Product:** UPI International  ·  **Commander:** Harsh Nanda
**Detected:** 04 Jun 2026 08:30 IST (morning KPI sweep)

## Summary
A bank timeout / 5xx spike on Punjab National Bank degraded UPI International. Success Rate at
99.21%, Technical Declines 0.63%,
Response Time p95 662 ms. Customer Complaints
1,795, Merchant Complaints 226.

## Impact
Impact concentrated on the UPI International path.
Expected active window: 04 Jun - 06 Jun.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI International.
- 08:30 — anomaly flagged by KPI sweep (RPT-D151-DAILY).
- 09:30 — incident bridge convened; Sev-2 confirmed.

Root cause under investigation — see RCA-2026-06.
Permanent fix tracked as DEC-2026-06.

Refs: upi_kpis_month.xlsx, RPT-D151-DAILY, RCA-2026-06, DEC-2026-06, TEAMS-D151-MON
