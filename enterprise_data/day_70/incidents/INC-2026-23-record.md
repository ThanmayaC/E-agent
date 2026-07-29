---
id: INC-2026-23
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-30T09:00:00
---

# Incident Record — INC-2026-23 UPI Core PSP callback latency increase

**Incident ID:** INC-2026-23  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Core  ·  **Commander:** Harsh Nanda
**Detected:** 30 Aug 2026 08:30 IST (morning KPI sweep)

## Summary
A PSP callback latency increase on BHIM degraded UPI Core. Success Rate at
99.92%, Technical Declines 0.46%,
Response Time p95 733 ms. Customer Complaints
1,779, Merchant Complaints 147.

## Impact
Impact concentrated on the UPI Core path.
Expected active window: 30 Aug - 31 Aug.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Core.
- 08:30 — anomaly flagged by KPI sweep (RPT-D70-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause being triaged as a short operational issue.

Refs: upi_kpis_month.xlsx, RPT-D70-DAILY, TEAMS-D70-MON
