---
id: INC-2026-13
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-30T09:00:00
---

# Incident Record — INC-2026-13 UPI Core PSP callback latency increase

**Incident ID:** INC-2026-13  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Core  ·  **Commander:** Harsh Nanda
**Detected:** 30 Jun 2026 08:30 IST (morning KPI sweep)

## Summary
A PSP callback latency increase on YONO SBI degraded UPI Core. Success Rate at
99.72%, Technical Declines 0.58%,
Response Time p95 826 ms. Customer Complaints
2,390, Merchant Complaints 200.

## Impact
Impact concentrated on the UPI Core path.
Expected active window: 30 Jun - 03 Jul.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Core.
- 08:30 — anomaly flagged by KPI sweep (RPT-D09-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-13.
Permanent fix tracked as DEC-2026-13.

Refs: upi_kpis_month.xlsx, RPT-D09-DAILY, RCA-2026-13, DEC-2026-13, TEAMS-D09-MON
