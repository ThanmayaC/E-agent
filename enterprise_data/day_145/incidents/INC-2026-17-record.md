---
id: INC-2026-17
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-13T09:00:00
---

# Incident Record — INC-2026-17 Merchant Products merchant settlement delay

**Incident ID:** INC-2026-17  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** Merchant Products  ·  **Commander:** Harsh Nanda
**Detected:** 13 Nov 2026 08:30 IST (morning KPI sweep)

## Summary
A merchant settlement delay on IndusInd Bank degraded Merchant Products. Success Rate at
99.79%, Technical Declines 0.26%,
Response Time p95 558 ms. Customer Complaints
1,105, Merchant Complaints 178.

## Impact
Affected merchants: TravelGo, MetroRide, PowerPay Utilities, BharatKart.
Expected active window: 13 Nov - 16 Nov.

## Timeline (day 1)
- 06:25 — first elevated failures on Merchant Products.
- 08:30 — anomaly flagged by KPI sweep (RPT-D145-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-17.
Permanent fix tracked as DEC-2026-17.

Refs: upi_kpis_month.xlsx, RPT-D145-DAILY, RCA-2026-17, DEC-2026-17, TEAMS-D145-MON
