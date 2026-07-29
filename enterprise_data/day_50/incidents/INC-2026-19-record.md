---
id: INC-2026-19
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-23T09:00:00
---

# Incident Record — INC-2026-19 UPI International fraud / risk spike

**Incident ID:** INC-2026-19  ·  **Severity:** Sev-2  ·  **Status:** Investigating
**Product:** UPI International  ·  **Commander:** Harsh Nanda
**Detected:** 23 Feb 2026 08:30 IST (morning KPI sweep)

## Summary
A fraud / risk spike on Google Pay degraded UPI International. Success Rate at
99.36%, Technical Declines 0.46%,
Response Time p95 693 ms. Customer Complaints
2,292, Merchant Complaints 183.

## Impact
Impact concentrated on the UPI International path.
Expected active window: 23 Feb - 25 Feb.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI International.
- 08:30 — anomaly flagged by KPI sweep (RPT-D50-DAILY).
- 09:30 — incident bridge convened; Sev-2 confirmed.

Root cause under investigation — see RCA-2026-19.
Permanent fix tracked as DEC-2026-19.

Refs: upi_kpis_month.xlsx, RPT-D50-DAILY, RCA-2026-19, DEC-2026-19, TEAMS-D50-MON
