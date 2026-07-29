---
id: INC-2026-27
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-25T09:00:00
---

# Incident Record — INC-2026-27 UPI Core PSP callback latency increase

**Incident ID:** INC-2026-27  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Core  ·  **Commander:** Harsh Nanda
**Detected:** 25 Jul 2026 08:30 IST (morning KPI sweep)

## Summary
A PSP callback latency increase on Amazon Pay degraded UPI Core. Success Rate at
99.17%, Technical Declines 0.52%,
Response Time p95 782 ms. Customer Complaints
2,109, Merchant Complaints 178.

## Impact
Impact concentrated on the UPI Core path.
Expected active window: 25 Jul - 29 Jul.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Core.
- 08:30 — anomaly flagged by KPI sweep (RPT-D34-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-27.
Permanent fix tracked as DEC-2026-27.

Refs: upi_kpis_month.xlsx, RPT-D34-DAILY, RCA-2026-27, DEC-2026-27, TEAMS-D34-MON
