---
id: INC-2026-10
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-30T09:00:00
---

# Incident Record — INC-2026-10 UPI Lite X bank timeout / 5xx spike

**Incident ID:** INC-2026-10  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Lite X  ·  **Commander:** Harsh Nanda
**Detected:** 30 Oct 2026 08:30 IST (morning KPI sweep)

## Summary
A bank timeout / 5xx spike on Union Bank of India degraded UPI Lite X. Success Rate at
98.48%, Technical Declines 0.44%,
Response Time p95 631 ms. Customer Complaints
1,503, Merchant Complaints 201.

## Impact
Impact concentrated on the UPI Lite X path.
Expected active window: 30 Oct - 31 Oct.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Lite X.
- 08:30 — anomaly flagged by KPI sweep (RPT-D131-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause being triaged as a short operational issue.

Refs: upi_kpis_month.xlsx, RPT-D131-DAILY, TEAMS-D131-MON
