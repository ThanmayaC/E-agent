---
id: INC-2026-16
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-28T09:00:00
---

# Incident Record — INC-2026-16 UPI Core fraud / risk spike

**Incident ID:** INC-2026-16  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Core  ·  **Commander:** Harsh Nanda
**Detected:** 28 Feb 2026 08:30 IST (morning KPI sweep)

## Summary
A fraud / risk spike on Navi degraded UPI Core. Success Rate at
98.21%, Technical Declines 0.47%,
Response Time p95 704 ms. Customer Complaints
2,083, Merchant Complaints 177.

## Impact
Impact concentrated on the UPI Core path.
Expected active window: 28 Feb - 01 Mar.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Core.
- 08:30 — anomaly flagged by KPI sweep (RPT-D55-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause being triaged as a short operational issue.

Refs: upi_kpis_month.xlsx, RPT-D55-DAILY, TEAMS-D55-MON
