---
id: INC-2026-23
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-23T09:00:00
---

# Incident Record — INC-2026-23 UPI Core merchant decline-rate spike

**Incident ID:** INC-2026-23  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Core  ·  **Commander:** Harsh Nanda
**Detected:** 23 Apr 2026 08:30 IST (morning KPI sweep)

## Summary
A merchant decline-rate spike on PowerPay Utilities, MetroRide degraded UPI Core. Success Rate at
98.55%, Technical Declines 0.37%,
Response Time p95 626 ms. Customer Complaints
1,283, Merchant Complaints 214.

## Impact
Affected merchants: PowerPay Utilities, MetroRide.
Expected active window: 23 Apr - 26 Apr.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Core.
- 08:30 — anomaly flagged by KPI sweep (RPT-D109-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-23.
Permanent fix tracked as DEC-2026-23.

Refs: upi_kpis_month.xlsx, RPT-D109-DAILY, RCA-2026-23, DEC-2026-23, TEAMS-D109-MON
