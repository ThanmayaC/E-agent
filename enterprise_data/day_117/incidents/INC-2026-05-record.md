---
id: INC-2026-05
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-01T09:00:00
---

# Incident Record — INC-2026-05 Merchant Products merchant settlement delay

**Incident ID:** INC-2026-05  ·  **Severity:** Sev-2  ·  **Status:** Investigating
**Product:** Merchant Products  ·  **Commander:** Harsh Nanda
**Detected:** 01 May 2026 08:30 IST (morning KPI sweep)

## Summary
A merchant settlement delay on Union Bank of India degraded Merchant Products. Success Rate at
99.98%, Technical Declines 0.36%,
Response Time p95 611 ms. Customer Complaints
1,478, Merchant Complaints 294.

## Impact
Affected merchants: FlixStream, DailyMart, InsureWell, PowerPay Utilities.
Expected active window: 01 May - 03 May.

## Timeline (day 1)
- 06:25 — first elevated failures on Merchant Products.
- 08:30 — anomaly flagged by KPI sweep (RPT-D117-DAILY).
- 09:30 — incident bridge convened; Sev-2 confirmed.

Root cause under investigation — see RCA-2026-05.
Permanent fix tracked as DEC-2026-05.

Refs: upi_kpis_month.xlsx, RPT-D117-DAILY, RCA-2026-05, DEC-2026-05, TEAMS-D117-MON
