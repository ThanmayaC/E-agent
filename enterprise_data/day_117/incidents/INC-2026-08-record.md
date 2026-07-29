---
id: INC-2026-08
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-16T09:00:00
---

# Incident Record — INC-2026-08 UPI Core PSP callback latency increase

**Incident ID:** INC-2026-08  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Core  ·  **Commander:** Harsh Nanda
**Detected:** 16 Oct 2026 08:30 IST (morning KPI sweep)

## Summary
A PSP callback latency increase on CRED degraded UPI Core. Success Rate at
99.25%, Technical Declines 0.39%,
Response Time p95 675 ms. Customer Complaints
1,459, Merchant Complaints 114.

## Impact
Impact concentrated on the UPI Core path.
Expected active window: 16 Oct - 19 Oct.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Core.
- 08:30 — anomaly flagged by KPI sweep (RPT-D117-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-08.
Permanent fix tracked as DEC-2026-08.

Refs: upi_kpis_month.xlsx, RPT-D117-DAILY, RCA-2026-08, DEC-2026-08, TEAMS-D117-MON
