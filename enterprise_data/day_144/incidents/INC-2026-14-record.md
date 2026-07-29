---
id: INC-2026-14
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-28T09:00:00
---

# Incident Record — INC-2026-14 UPI Lite PSP callback latency increase

**Incident ID:** INC-2026-14  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Lite  ·  **Commander:** Harsh Nanda
**Detected:** 28 May 2026 08:30 IST (morning KPI sweep)

## Summary
A PSP callback latency increase on BHIM degraded UPI Lite. Success Rate at
99.98%, Technical Declines 0.42%,
Response Time p95 666 ms. Customer Complaints
1,378, Merchant Complaints 112.

## Impact
Impact concentrated on the UPI Lite path.
Expected active window: 28 May - 01 Jun.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Lite.
- 08:30 — anomaly flagged by KPI sweep (RPT-D144-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-14.
Permanent fix tracked as DEC-2026-14.

Refs: upi_kpis_month.xlsx, RPT-D144-DAILY, RCA-2026-14, DEC-2026-14, TEAMS-D144-MON
