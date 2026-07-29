---
id: INC-2026-12
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-29T09:00:00
---

# Incident Record — INC-2026-12 Merchant Products merchant settlement delay

**Incident ID:** INC-2026-12  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** Merchant Products  ·  **Commander:** Harsh Nanda
**Detected:** 29 Sep 2026 08:30 IST (morning KPI sweep)

## Summary
A merchant settlement delay on State Bank of India degraded Merchant Products. Success Rate at
99.98%, Technical Declines 0.31%,
Response Time p95 611 ms. Customer Complaints
1,377, Merchant Complaints 222.

## Impact
Affected merchants: StyleHub, CityFuel.
Expected active window: 29 Sep - 03 Oct.

## Timeline (day 1)
- 06:25 — first elevated failures on Merchant Products.
- 08:30 — anomaly flagged by KPI sweep (RPT-D100-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-12.
Permanent fix tracked as DEC-2026-12.

Refs: upi_kpis_month.xlsx, RPT-D100-DAILY, RCA-2026-12, DEC-2026-12, TEAMS-D100-MON
