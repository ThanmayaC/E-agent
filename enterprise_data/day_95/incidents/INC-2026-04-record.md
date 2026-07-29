---
id: INC-2026-04
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-24T09:00:00
---

# Incident Record — INC-2026-04 UPI Credit fraud / risk spike

**Incident ID:** INC-2026-04  ·  **Severity:** Sev-2  ·  **Status:** Investigating
**Product:** UPI Credit  ·  **Commander:** Harsh Nanda
**Detected:** 24 Sep 2026 08:30 IST (morning KPI sweep)

## Summary
A fraud / risk spike on iMobile Pay degraded UPI Credit. Success Rate at
99.71%, Technical Declines 0.32%,
Response Time p95 619 ms. Customer Complaints
1,693, Merchant Complaints 130.

## Impact
Impact concentrated on the UPI Credit path.
Expected active window: 24 Sep - 28 Sep.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Credit.
- 08:30 — anomaly flagged by KPI sweep (RPT-D95-DAILY).
- 09:30 — incident bridge convened; Sev-2 confirmed.

Root cause under investigation — see RCA-2026-04.
Permanent fix tracked as DEC-2026-04.

Refs: upi_kpis_month.xlsx, RPT-D95-DAILY, RCA-2026-04, DEC-2026-04, TEAMS-D95-MON
