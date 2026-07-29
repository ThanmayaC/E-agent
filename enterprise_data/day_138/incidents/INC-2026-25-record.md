---
id: INC-2026-25
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-22T09:00:00
---

# Incident Record — INC-2026-25 Merchant Products merchant settlement delay

**Incident ID:** INC-2026-25  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** Merchant Products  ·  **Commander:** Harsh Nanda
**Detected:** 22 May 2026 08:30 IST (morning KPI sweep)

## Summary
A merchant settlement delay on ICICI Bank degraded Merchant Products. Success Rate at
99.23%, Technical Declines 0.33%,
Response Time p95 593 ms. Customer Complaints
1,260, Merchant Complaints 206.

## Impact
Affected merchants: BharatKart, FlixStream, PowerPay Utilities, FreshBasket.
Expected active window: 22 May - 23 May.

## Timeline (day 1)
- 06:25 — first elevated failures on Merchant Products.
- 08:30 — anomaly flagged by KPI sweep (RPT-D138-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause being triaged as a short operational issue.

Refs: upi_kpis_month.xlsx, RPT-D138-DAILY, TEAMS-D138-MON
