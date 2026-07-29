---
id: INC-2026-15
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-26T09:00:00
---

# Incident Record — INC-2026-15 UPI International fraud / risk spike

**Incident ID:** INC-2026-15  ·  **Severity:** Sev-2  ·  **Status:** Investigating
**Product:** UPI International  ·  **Commander:** Harsh Nanda
**Detected:** 26 Jan 2026 08:30 IST (morning KPI sweep)

## Summary
A fraud / risk spike on FamApp degraded UPI International. Success Rate at
98.09%, Technical Declines 0.51%,
Response Time p95 728 ms. Customer Complaints
2,609, Merchant Complaints 209.

## Impact
Impact concentrated on the UPI International path.
Expected active window: 26 Jan - 28 Jan.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI International.
- 08:30 — anomaly flagged by KPI sweep (RPT-D22-DAILY).
- 09:30 — incident bridge convened; Sev-2 confirmed.

Root cause under investigation — see RCA-2026-15.
Permanent fix tracked as DEC-2026-15.

Refs: upi_kpis_month.xlsx, RPT-D22-DAILY, RCA-2026-15, DEC-2026-15, TEAMS-D22-MON
