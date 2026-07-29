---
id: INC-2026-22
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-25T09:00:00
---

# Incident Record — INC-2026-22 UPI Credit PSP callback latency increase

**Incident ID:** INC-2026-22  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Credit  ·  **Commander:** Harsh Nanda
**Detected:** 25 Feb 2026 08:30 IST (morning KPI sweep)

## Summary
A PSP callback latency increase on Navi degraded UPI Credit. Success Rate at
99.29%, Technical Declines 0.61%,
Response Time p95 787 ms. Customer Complaints
2,328, Merchant Complaints 181.

## Impact
Impact concentrated on the UPI Credit path.
Expected active window: 25 Feb - 28 Feb.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Credit.
- 08:30 — anomaly flagged by KPI sweep (RPT-D52-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-22.
Permanent fix tracked as DEC-2026-22.

Refs: upi_kpis_month.xlsx, RPT-D52-DAILY, RCA-2026-22, DEC-2026-22, TEAMS-D52-MON
