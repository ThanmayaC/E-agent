---
id: INC-2026-20
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-15T09:00:00
---

# Incident Record — INC-2026-20 Merchant Products merchant settlement delay

**Incident ID:** INC-2026-20  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** Merchant Products  ·  **Commander:** Harsh Nanda
**Detected:** 15 Apr 2026 08:30 IST (morning KPI sweep)

## Summary
A merchant settlement delay on Kotak Mahindra Bank degraded Merchant Products. Success Rate at
99.25%, Technical Declines 0.38%,
Response Time p95 629 ms. Customer Complaints
1,511, Merchant Complaints 249.

## Impact
Affected merchants: MetroRide, QuickBite, InsureWell, CityFuel.
Expected active window: 15 Apr - 17 Apr.

## Timeline (day 1)
- 06:25 — first elevated failures on Merchant Products.
- 08:30 — anomaly flagged by KPI sweep (RPT-D101-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-20.
Permanent fix tracked as DEC-2026-20.

Refs: upi_kpis_month.xlsx, RPT-D101-DAILY, RCA-2026-20, DEC-2026-20, TEAMS-D101-MON
