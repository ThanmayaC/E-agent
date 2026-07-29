---
id: INC-2026-20
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-03T09:00:00
---

# Incident Record — INC-2026-20 Merchant Products merchant settlement delay

**Incident ID:** INC-2026-20  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** Merchant Products  ·  **Commander:** Harsh Nanda
**Detected:** 03 Nov 2026 08:30 IST (morning KPI sweep)

## Summary
A merchant settlement delay on Bank of Baroda degraded Merchant Products. Success Rate at
99.21%, Technical Declines 0.27%,
Response Time p95 576 ms. Customer Complaints
1,170, Merchant Complaints 187.

## Impact
Affected merchants: GadgetZone, CityFuel, FlixStream, InsureWell.
Expected active window: 03 Nov - 04 Nov.

## Timeline (day 1)
- 06:25 — first elevated failures on Merchant Products.
- 08:30 — anomaly flagged by KPI sweep (RPT-D135-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause being triaged as a short operational issue.

Refs: upi_kpis_month.xlsx, RPT-D135-DAILY, TEAMS-D135-MON
