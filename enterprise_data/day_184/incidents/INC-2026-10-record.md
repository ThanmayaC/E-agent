---
id: INC-2026-10
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-07T09:00:00
---

# Incident Record — INC-2026-10 UPI 123Pay feature-level degradation

**Incident ID:** INC-2026-10  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI 123Pay  ·  **Commander:** Harsh Nanda
**Detected:** 07 Jul 2026 08:30 IST (morning KPI sweep)

## Summary
A feature-level degradation on UPI 123Pay degraded UPI 123Pay. Success Rate at
99.04%, Technical Declines 0.41%,
Response Time p95 584 ms. Customer Complaints
1,181, Merchant Complaints 91.

## Impact
Impact concentrated on the UPI 123Pay path.
Expected active window: 07 Jul - 11 Jul.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI 123Pay.
- 08:30 — anomaly flagged by KPI sweep (RPT-D184-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-10.
Permanent fix tracked as DEC-2026-10.

Refs: upi_kpis_month.xlsx, RPT-D184-DAILY, RCA-2026-10, DEC-2026-10, TEAMS-D184-MON
