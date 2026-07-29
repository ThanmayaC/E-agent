---
id: INC-2026-04
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-06T09:00:00
---

# Incident Record — INC-2026-04 UPI Core bank timeout / 5xx spike

**Incident ID:** INC-2026-04  ·  **Severity:** Sev-2  ·  **Status:** Investigating
**Product:** UPI Core  ·  **Commander:** Harsh Nanda
**Detected:** 06 Apr 2026 08:30 IST (morning KPI sweep)

## Summary
A bank timeout / 5xx spike on State Bank of India degraded UPI Core. Success Rate at
98.17%, Technical Declines 0.8%,
Response Time p95 751 ms. Customer Complaints
2,365, Merchant Complaints 308.

## Impact
Impact concentrated on the UPI Core path.
Expected active window: 06 Apr - 09 Apr.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Core.
- 08:30 — anomaly flagged by KPI sweep (RPT-D92-DAILY).
- 09:30 — incident bridge convened; Sev-2 confirmed.

Root cause under investigation — see RCA-2026-04.
Permanent fix tracked as DEC-2026-04.

Refs: upi_kpis_month.xlsx, RPT-D92-DAILY, RCA-2026-04, DEC-2026-04, TEAMS-D92-MON
