---
id: INC-2026-26
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-15T09:00:00
---

# Incident Record — INC-2026-26 UPI Autopay fraud / risk spike

**Incident ID:** INC-2026-26  ·  **Severity:** Sev-2  ·  **Status:** Investigating
**Product:** UPI Autopay  ·  **Commander:** Harsh Nanda
**Detected:** 15 Nov 2026 08:30 IST (morning KPI sweep)

## Summary
A fraud / risk spike on FamApp degraded UPI Autopay. Success Rate at
98.57%, Technical Declines 0.26%,
Response Time p95 559 ms. Customer Complaints
1,354, Merchant Complaints 124.

## Impact
Impact concentrated on the UPI Autopay path.
Expected active window: 15 Nov - 17 Nov.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Autopay.
- 08:30 — anomaly flagged by KPI sweep (RPT-D147-DAILY).
- 09:30 — incident bridge convened; Sev-2 confirmed.

Root cause under investigation — see RCA-2026-26.
Permanent fix tracked as DEC-2026-26.

Refs: upi_kpis_month.xlsx, RPT-D147-DAILY, RCA-2026-26, DEC-2026-26, TEAMS-D147-MON
