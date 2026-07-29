---
id: INC-2026-14
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-14T09:00:00
---

# Incident Record — INC-2026-14 UPI Autopay PSP callback latency increase

**Incident ID:** INC-2026-14  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Autopay  ·  **Commander:** Harsh Nanda
**Detected:** 14 Sep 2026 08:30 IST (morning KPI sweep)

## Summary
A PSP callback latency increase on Axis Mobile degraded UPI Autopay. Success Rate at
99.02%, Technical Declines 0.43%,
Response Time p95 707 ms. Customer Complaints
1,651, Merchant Complaints 136.

## Impact
Impact concentrated on the UPI Autopay path.
Expected active window: 14 Sep - 18 Sep.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Autopay.
- 08:30 — anomaly flagged by KPI sweep (RPT-D85-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-14.
Permanent fix tracked as DEC-2026-14.

Refs: upi_kpis_month.xlsx, RPT-D85-DAILY, RCA-2026-14, DEC-2026-14, TEAMS-D85-MON
