---
id: INC-2026-09
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-06T09:00:00
---

# Incident Record — INC-2026-09 UPI International fraud / risk spike

**Incident ID:** INC-2026-09  ·  **Severity:** Sev-2  ·  **Status:** Investigating
**Product:** UPI International  ·  **Commander:** Harsh Nanda
**Detected:** 06 Jul 2026 08:30 IST (morning KPI sweep)

## Summary
A fraud / risk spike on YONO SBI degraded UPI International. Success Rate at
99.57%, Technical Declines 0.43%,
Response Time p95 723 ms. Customer Complaints
2,484, Merchant Complaints 196.

## Impact
Impact concentrated on the UPI International path.
Expected active window: 06 Jul - 08 Jul.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI International.
- 08:30 — anomaly flagged by KPI sweep (RPT-D15-DAILY).
- 09:30 — incident bridge convened; Sev-2 confirmed.

Root cause under investigation — see RCA-2026-09.
Permanent fix tracked as DEC-2026-09.

Refs: upi_kpis_month.xlsx, RPT-D15-DAILY, RCA-2026-09, DEC-2026-09, TEAMS-D15-MON
