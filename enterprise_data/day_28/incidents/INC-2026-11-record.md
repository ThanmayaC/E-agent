---
id: INC-2026-11
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-19T09:00:00
---

# Incident Record — INC-2026-11 UPI Credit PSP callback latency increase

**Incident ID:** INC-2026-11  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Credit  ·  **Commander:** Harsh Nanda
**Detected:** 19 Jul 2026 08:30 IST (morning KPI sweep)

## Summary
A PSP callback latency increase on CRED degraded UPI Credit. Success Rate at
99.04%, Technical Declines 0.54%,
Response Time p95 788 ms. Customer Complaints
2,173, Merchant Complaints 181.

## Impact
Impact concentrated on the UPI Credit path.
Expected active window: 19 Jul - 20 Jul.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Credit.
- 08:30 — anomaly flagged by KPI sweep (RPT-D28-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause being triaged as a short operational issue.

Refs: upi_kpis_month.xlsx, RPT-D28-DAILY, TEAMS-D28-MON
