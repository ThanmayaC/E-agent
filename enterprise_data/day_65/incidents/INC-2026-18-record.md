---
id: INC-2026-18
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-25T09:00:00
---

# Incident Record — INC-2026-18 UPI Autopay merchant decline-rate spike

**Incident ID:** INC-2026-18  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Autopay  ·  **Commander:** Harsh Nanda
**Detected:** 25 Aug 2026 08:30 IST (morning KPI sweep)

## Summary
A merchant decline-rate spike on MetroRide, QuickBite degraded UPI Autopay. Success Rate at
98.95%, Technical Declines 0.36%,
Response Time p95 652 ms. Customer Complaints
1,437, Merchant Complaints 242.

## Impact
Affected merchants: MetroRide, QuickBite.
Expected active window: 25 Aug - 26 Aug.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Autopay.
- 08:30 — anomaly flagged by KPI sweep (RPT-D65-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause being triaged as a short operational issue.

Refs: upi_kpis_month.xlsx, RPT-D65-DAILY, TEAMS-D65-MON
