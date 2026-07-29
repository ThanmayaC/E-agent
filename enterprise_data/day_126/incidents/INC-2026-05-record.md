---
id: INC-2026-05
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-25T09:00:00
---

# Incident Record — INC-2026-05 UPI Credit bank timeout / 5xx spike

**Incident ID:** INC-2026-05  ·  **Severity:** Sev-2  ·  **Status:** Investigating
**Product:** UPI Credit  ·  **Commander:** Harsh Nanda
**Detected:** 25 Oct 2026 08:30 IST (morning KPI sweep)

## Summary
A bank timeout / 5xx spike on Union Bank of India degraded UPI Credit. Success Rate at
98.22%, Technical Declines 0.58%,
Response Time p95 682 ms. Customer Complaints
1,831, Merchant Complaints 229.

## Impact
Impact concentrated on the UPI Credit path.
Expected active window: 25 Oct - 29 Oct.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Credit.
- 08:30 — anomaly flagged by KPI sweep (RPT-D126-DAILY).
- 09:30 — incident bridge convened; Sev-2 confirmed.

Root cause under investigation — see RCA-2026-05.
Permanent fix tracked as DEC-2026-05.

Refs: upi_kpis_month.xlsx, RPT-D126-DAILY, RCA-2026-05, DEC-2026-05, TEAMS-D126-MON
