---
id: INC-2026-16
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-02T09:00:00
---

# Incident Record — INC-2026-16 UPI Lite X PSP callback latency increase

**Incident ID:** INC-2026-16  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Lite X  ·  **Commander:** Harsh Nanda
**Detected:** 02 Jul 2026 08:30 IST (morning KPI sweep)

## Summary
A PSP callback latency increase on Paytm degraded UPI Lite X. Success Rate at
98.08%, Technical Declines 0.63%,
Response Time p95 854 ms. Customer Complaints
2,519, Merchant Complaints 200.

## Impact
Impact concentrated on the UPI Lite X path.
Expected active window: 02 Jul - 05 Jul.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Lite X.
- 08:30 — anomaly flagged by KPI sweep (RPT-D11-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-16.
Permanent fix tracked as DEC-2026-16.

Refs: upi_kpis_month.xlsx, RPT-D11-DAILY, RCA-2026-16, DEC-2026-16, TEAMS-D11-MON
