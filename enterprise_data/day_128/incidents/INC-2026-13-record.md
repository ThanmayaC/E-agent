---
id: INC-2026-13
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-12T09:00:00
---

# Incident Record — INC-2026-13 UPI Credit merchant decline-rate spike

**Incident ID:** INC-2026-13  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Credit  ·  **Commander:** Harsh Nanda
**Detected:** 12 May 2026 08:30 IST (morning KPI sweep)

## Summary
A merchant decline-rate spike on TravelGo, InsureWell degraded UPI Credit. Success Rate at
99.63%, Technical Declines 0.34%,
Response Time p95 605 ms. Customer Complaints
1,181, Merchant Complaints 195.

## Impact
Affected merchants: TravelGo, InsureWell.
Expected active window: 12 May - 16 May.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Credit.
- 08:30 — anomaly flagged by KPI sweep (RPT-D128-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-13.
Permanent fix tracked as DEC-2026-13.

Refs: upi_kpis_month.xlsx, RPT-D128-DAILY, RCA-2026-13, DEC-2026-13, TEAMS-D128-MON
