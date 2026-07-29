---
id: INC-2026-01
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-09T09:00:00
---

# Incident Record — INC-2026-01 UPI Core bank timeout / 5xx spike

**Incident ID:** INC-2026-01  ·  **Severity:** Sev-2  ·  **Status:** Investigating
**Product:** UPI Core  ·  **Commander:** Harsh Nanda
**Detected:** 09 Jan 2026 08:30 IST (morning KPI sweep)

## Summary
A bank timeout / 5xx spike on Punjab National Bank degraded UPI Core. Success Rate at
98.72%, Technical Declines 1.11%,
Response Time p95 878 ms. Customer Complaints
3,596, Merchant Complaints 482.

## Impact
Impact concentrated on the UPI Core path.
Expected active window: 09 Jan - 12 Jan.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Core.
- 08:30 — anomaly flagged by KPI sweep (RPT-D05-DAILY).
- 09:30 — incident bridge convened; Sev-2 confirmed.

Root cause under investigation — see RCA-2026-01.
Permanent fix tracked as DEC-2026-01.

Refs: upi_kpis_month.xlsx, RPT-D05-DAILY, RCA-2026-01, DEC-2026-01, TEAMS-D05-MON
