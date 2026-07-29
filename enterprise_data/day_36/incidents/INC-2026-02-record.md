---
id: INC-2026-02
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-27T09:00:00
---

# Incident Record — INC-2026-02 Merchant Products merchant settlement delay

**Incident ID:** INC-2026-02  ·  **Severity:** Sev-2  ·  **Status:** Investigating
**Product:** Merchant Products  ·  **Commander:** Harsh Nanda
**Detected:** 27 Jul 2026 08:30 IST (morning KPI sweep)

## Summary
A merchant settlement delay on Axis Bank degraded Merchant Products. Success Rate at
99.97%, Technical Declines 0.44%,
Response Time p95 726 ms. Customer Complaints
2,151, Merchant Complaints 405.

## Impact
Affected merchants: CityFuel, InsureWell, QuickBite.
Expected active window: 27 Jul - 29 Jul.

## Timeline (day 1)
- 06:25 — first elevated failures on Merchant Products.
- 08:30 — anomaly flagged by KPI sweep (RPT-D36-DAILY).
- 09:30 — incident bridge convened; Sev-2 confirmed.

Root cause under investigation — see RCA-2026-02.
Permanent fix tracked as DEC-2026-02.

Refs: upi_kpis_month.xlsx, RPT-D36-DAILY, RCA-2026-02, DEC-2026-02, TEAMS-D36-MON
