---
id: INC-2026-25
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-07T09:00:00
---

# Incident Record — INC-2026-25 UPI Lite X PSP callback latency increase

**Incident ID:** INC-2026-25  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Lite X  ·  **Commander:** Harsh Nanda
**Detected:** 07 Nov 2026 08:30 IST (morning KPI sweep)

## Summary
A PSP callback latency increase on BHIM degraded UPI Lite X. Success Rate at
99.65%, Technical Declines 0.35%,
Response Time p95 642 ms. Customer Complaints
1,280, Merchant Complaints 103.

## Impact
Impact concentrated on the UPI Lite X path.
Expected active window: 07 Nov - 11 Nov.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Lite X.
- 08:30 — anomaly flagged by KPI sweep (RPT-D139-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-25.
Permanent fix tracked as DEC-2026-25.

Refs: upi_kpis_month.xlsx, RPT-D139-DAILY, RCA-2026-25, DEC-2026-25, TEAMS-D139-MON
