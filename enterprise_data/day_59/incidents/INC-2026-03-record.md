---
id: INC-2026-03
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-04T09:00:00
---

# Incident Record — INC-2026-03 UPI International fraud / risk spike

**Incident ID:** INC-2026-03  ·  **Severity:** Sev-2  ·  **Status:** Investigating
**Product:** UPI International  ·  **Commander:** Harsh Nanda
**Detected:** 04 Mar 2026 08:30 IST (morning KPI sweep)

## Summary
A fraud / risk spike on Navi degraded UPI International. Success Rate at
99.84%, Technical Declines 0.44%,
Response Time p95 689 ms. Customer Complaints
2,201, Merchant Complaints 174.

## Impact
Impact concentrated on the UPI International path.
Expected active window: 04 Mar - 06 Mar.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI International.
- 08:30 — anomaly flagged by KPI sweep (RPT-D59-DAILY).
- 09:30 — incident bridge convened; Sev-2 confirmed.

Root cause under investigation — see RCA-2026-03.
Permanent fix tracked as DEC-2026-03.

Refs: upi_kpis_month.xlsx, RPT-D59-DAILY, RCA-2026-03, DEC-2026-03, TEAMS-D59-MON
