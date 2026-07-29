---
id: INC-2026-03
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-17T09:00:00
---

# Incident Record — INC-2026-03 Merchant Products merchant settlement delay

**Incident ID:** INC-2026-03  ·  **Severity:** Sev-2  ·  **Status:** Investigating
**Product:** Merchant Products  ·  **Commander:** Harsh Nanda
**Detected:** 17 Aug 2026 08:30 IST (morning KPI sweep)

## Summary
A merchant settlement delay on ICICI Bank degraded Merchant Products. Success Rate at
99.57%, Technical Declines 0.36%,
Response Time p95 666 ms. Customer Complaints
1,814, Merchant Complaints 363.

## Impact
Affected merchants: CityFuel, QuickBite.
Expected active window: 17 Aug - 20 Aug.

## Timeline (day 1)
- 06:25 — first elevated failures on Merchant Products.
- 08:30 — anomaly flagged by KPI sweep (RPT-D57-DAILY).
- 09:30 — incident bridge convened; Sev-2 confirmed.

Root cause under investigation — see RCA-2026-03.
Permanent fix tracked as DEC-2026-03.

Refs: upi_kpis_month.xlsx, RPT-D57-DAILY, RCA-2026-03, DEC-2026-03, TEAMS-D57-MON
