---
id: INC-2026-18
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-24T09:00:00
---

# Incident Record — INC-2026-18 UPI Core fraud / risk spike

**Incident ID:** INC-2026-18  ·  **Severity:** Sev-2  ·  **Status:** Investigating
**Product:** UPI Core  ·  **Commander:** Harsh Nanda
**Detected:** 24 May 2026 08:30 IST (morning KPI sweep)

## Summary
A fraud / risk spike on BHIM degraded UPI Core. Success Rate at
99.63%, Technical Declines 0.33%,
Response Time p95 588 ms. Customer Complaints
1,515, Merchant Complaints 113.

## Impact
Impact concentrated on the UPI Core path.
Expected active window: 24 May - 27 May.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Core.
- 08:30 — anomaly flagged by KPI sweep (RPT-D140-DAILY).
- 09:30 — incident bridge convened; Sev-2 confirmed.

Root cause under investigation — see RCA-2026-18.
Permanent fix tracked as DEC-2026-18.

Refs: upi_kpis_month.xlsx, RPT-D140-DAILY, RCA-2026-18, DEC-2026-18, TEAMS-D140-MON
