---
id: INC-2026-15
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-12-09T09:00:00
---

# Incident Record — INC-2026-15 Merchant Products merchant settlement delay

**Incident ID:** INC-2026-15  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** Merchant Products  ·  **Commander:** Harsh Nanda
**Detected:** 09 Dec 2026 08:30 IST (morning KPI sweep)

## Summary
A merchant settlement delay on Bank of Baroda degraded Merchant Products. Success Rate at
99.98%, Technical Declines 0.24%,
Response Time p95 534 ms. Customer Complaints
986, Merchant Complaints 156.

## Impact
Affected merchants: DailyMart, FlixStream.
Expected active window: 09 Dec - 12 Dec.

## Timeline (day 1)
- 06:25 — first elevated failures on Merchant Products.
- 08:30 — anomaly flagged by KPI sweep (RPT-D171-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-15.
Permanent fix tracked as DEC-2026-15.

Refs: upi_kpis_month.xlsx, RPT-D171-DAILY, RCA-2026-15, DEC-2026-15, TEAMS-D171-MON
