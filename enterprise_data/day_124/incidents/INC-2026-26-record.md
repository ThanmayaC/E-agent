---
id: INC-2026-26
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-08T09:00:00
---

# Incident Record — INC-2026-26 Merchant Products merchant settlement delay

**Incident ID:** INC-2026-26  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** Merchant Products  ·  **Commander:** Harsh Nanda
**Detected:** 08 May 2026 08:30 IST (morning KPI sweep)

## Summary
A merchant settlement delay on AU Small Finance Bank degraded Merchant Products. Success Rate at
99.59%, Technical Declines 0.35%,
Response Time p95 605 ms. Customer Complaints
1,355, Merchant Complaints 219.

## Impact
Affected merchants: EduPrime, CityFuel.
Expected active window: 08 May - 11 May.

## Timeline (day 1)
- 06:25 — first elevated failures on Merchant Products.
- 08:30 — anomaly flagged by KPI sweep (RPT-D124-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-26.
Permanent fix tracked as DEC-2026-26.

Refs: upi_kpis_month.xlsx, RPT-D124-DAILY, RCA-2026-26, DEC-2026-26, TEAMS-D124-MON
