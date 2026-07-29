---
id: INC-2026-28
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-21T09:00:00
---

# Incident Record — INC-2026-28 UPI Core feature-level degradation

**Incident ID:** INC-2026-28  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Core  ·  **Commander:** Harsh Nanda
**Detected:** 21 Aug 2026 08:30 IST (morning KPI sweep)

## Summary
A feature-level degradation on Collect Requests degraded UPI Core. Success Rate at
98.93%, Technical Declines 0.53%,
Response Time p95 698 ms. Customer Complaints
1,898, Merchant Complaints 155.

## Impact
Impact concentrated on the UPI Core path.
Expected active window: 21 Aug - 23 Aug.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Core.
- 08:30 — anomaly flagged by KPI sweep (RPT-D61-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-28.
Permanent fix tracked as DEC-2026-28.

Refs: upi_kpis_month.xlsx, RPT-D61-DAILY, RCA-2026-28, DEC-2026-28, TEAMS-D61-MON
