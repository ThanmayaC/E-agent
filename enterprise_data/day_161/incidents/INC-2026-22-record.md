---
id: INC-2026-22
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-29T09:00:00
---

# Incident Record — INC-2026-22 UPI Lite X bank timeout / 5xx spike

**Incident ID:** INC-2026-22  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Lite X  ·  **Commander:** Harsh Nanda
**Detected:** 29 Nov 2026 08:30 IST (morning KPI sweep)

## Summary
A bank timeout / 5xx spike on Bank of Baroda degraded UPI Lite X. Success Rate at
98.92%, Technical Declines 0.4%,
Response Time p95 597 ms. Customer Complaints
1,294, Merchant Complaints 153.

## Impact
Impact concentrated on the UPI Lite X path.
Expected active window: 29 Nov - 30 Nov.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Lite X.
- 08:30 — anomaly flagged by KPI sweep (RPT-D161-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause being triaged as a short operational issue.

Refs: upi_kpis_month.xlsx, RPT-D161-DAILY, TEAMS-D161-MON
