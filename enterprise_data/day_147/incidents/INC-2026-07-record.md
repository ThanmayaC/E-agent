---
id: INC-2026-07
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-31T09:00:00
---

# Incident Record — INC-2026-07 UPI Lite X merchant decline-rate spike

**Incident ID:** INC-2026-07  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Lite X  ·  **Commander:** Harsh Nanda
**Detected:** 31 May 2026 08:30 IST (morning KPI sweep)

## Summary
A merchant decline-rate spike on MetroRide, QuickBite degraded UPI Lite X. Success Rate at
99.2%, Technical Declines 0.33%,
Response Time p95 586 ms. Customer Complaints
1,133, Merchant Complaints 178.

## Impact
Affected merchants: MetroRide, QuickBite.
Expected active window: 31 May - 01 Jun.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Lite X.
- 08:30 — anomaly flagged by KPI sweep (RPT-D147-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause being triaged as a short operational issue.

Refs: upi_kpis_month.xlsx, RPT-D147-DAILY, TEAMS-D147-MON
