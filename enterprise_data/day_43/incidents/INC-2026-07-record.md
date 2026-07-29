---
id: INC-2026-07
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-03T09:00:00
---

# Incident Record — INC-2026-07 Merchant Products merchant settlement delay

**Incident ID:** INC-2026-07  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** Merchant Products  ·  **Commander:** Harsh Nanda
**Detected:** 03 Aug 2026 08:30 IST (morning KPI sweep)

## Summary
A merchant settlement delay on Yes Bank degraded Merchant Products. Success Rate at
98.73%, Technical Declines 0.39%,
Response Time p95 676 ms. Customer Complaints
1,796, Merchant Complaints 302.

## Impact
Affected merchants: FreshBasket, GadgetZone, QuickBite, InsureWell.
Expected active window: 03 Aug - 04 Aug.

## Timeline (day 1)
- 06:25 — first elevated failures on Merchant Products.
- 08:30 — anomaly flagged by KPI sweep (RPT-D43-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause being triaged as a short operational issue.

Refs: upi_kpis_month.xlsx, RPT-D43-DAILY, TEAMS-D43-MON
