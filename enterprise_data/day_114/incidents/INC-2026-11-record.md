---
id: INC-2026-11
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-28T09:00:00
---

# Incident Record — INC-2026-11 UPI Lite bank timeout / 5xx spike

**Incident ID:** INC-2026-11  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Lite  ·  **Commander:** Harsh Nanda
**Detected:** 28 Apr 2026 08:30 IST (morning KPI sweep)

## Summary
A bank timeout / 5xx spike on Bank of Baroda degraded UPI Lite. Success Rate at
99.9%, Technical Declines 0.58%,
Response Time p95 678 ms. Customer Complaints
1,802, Merchant Complaints 218.

## Impact
Impact concentrated on the UPI Lite path.
Expected active window: 28 Apr - 29 Apr.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Lite.
- 08:30 — anomaly flagged by KPI sweep (RPT-D114-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause being triaged as a short operational issue.

Refs: upi_kpis_month.xlsx, RPT-D114-DAILY, TEAMS-D114-MON
