---
id: INC-2026-24
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-28T09:00:00
---

# Incident Record — INC-2026-24 UPI Credit merchant decline-rate spike

**Incident ID:** INC-2026-24  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Credit  ·  **Commander:** Harsh Nanda
**Detected:** 28 Oct 2026 08:30 IST (morning KPI sweep)

## Summary
A merchant decline-rate spike on TravelGo, InsureWell degraded UPI Credit. Success Rate at
98.41%, Technical Declines 0.32%,
Response Time p95 598 ms. Customer Complaints
1,185, Merchant Complaints 194.

## Impact
Affected merchants: TravelGo, InsureWell.
Expected active window: 28 Oct - 01 Nov.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Credit.
- 08:30 — anomaly flagged by KPI sweep (RPT-D129-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-24.
Permanent fix tracked as DEC-2026-24.

Refs: upi_kpis_month.xlsx, RPT-D129-DAILY, RCA-2026-24, DEC-2026-24, TEAMS-D129-MON
