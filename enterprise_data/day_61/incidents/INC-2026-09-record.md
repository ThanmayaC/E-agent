---
id: INC-2026-09
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-06T09:00:00
---

# Incident Record — INC-2026-09 Merchant Products merchant settlement delay

**Incident ID:** INC-2026-09  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** Merchant Products  ·  **Commander:** Harsh Nanda
**Detected:** 06 Mar 2026 08:30 IST (morning KPI sweep)

## Summary
A merchant settlement delay on Bank of Baroda degraded Merchant Products. Success Rate at
99.94%, Technical Declines 0.44%,
Response Time p95 674 ms. Customer Complaints
1,996, Merchant Complaints 308.

## Impact
Affected merchants: GadgetZone, CityFuel, FlixStream, InsureWell.
Expected active window: 06 Mar - 07 Mar.

## Timeline (day 1)
- 06:25 — first elevated failures on Merchant Products.
- 08:30 — anomaly flagged by KPI sweep (RPT-D61-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause being triaged as a short operational issue.

Refs: upi_kpis_month.xlsx, RPT-D61-DAILY, TEAMS-D61-MON
