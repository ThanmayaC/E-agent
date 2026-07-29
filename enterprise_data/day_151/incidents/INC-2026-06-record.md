---
id: INC-2026-06
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-19T09:00:00
---

# Incident Record — INC-2026-06 UPI Credit fraud / risk spike

**Incident ID:** INC-2026-06  ·  **Severity:** Sev-2  ·  **Status:** Investigating
**Product:** UPI Credit  ·  **Commander:** Harsh Nanda
**Detected:** 19 Nov 2026 08:30 IST (morning KPI sweep)

## Summary
A fraud / risk spike on HDFC MobileBanking degraded UPI Credit. Success Rate at
99.92%, Technical Declines 0.25%,
Response Time p95 561 ms. Customer Complaints
1,288, Merchant Complaints 96.

## Impact
Impact concentrated on the UPI Credit path.
Expected active window: 19 Nov - 23 Nov.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Credit.
- 08:30 — anomaly flagged by KPI sweep (RPT-D151-DAILY).
- 09:30 — incident bridge convened; Sev-2 confirmed.

Root cause under investigation — see RCA-2026-06.
Permanent fix tracked as DEC-2026-06.

Refs: upi_kpis_month.xlsx, RPT-D151-DAILY, RCA-2026-06, DEC-2026-06, TEAMS-D151-MON
