---
id: INC-2026-08
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-07T09:00:00
---

# Incident Record — INC-2026-08 UPI Core fraud / risk spike

**Incident ID:** INC-2026-08  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Core  ·  **Commander:** Harsh Nanda
**Detected:** 07 Feb 2026 08:30 IST (morning KPI sweep)

## Summary
A fraud / risk spike on WhatsApp Pay degraded UPI Core. Success Rate at
98.87%, Technical Declines 0.49%,
Response Time p95 716 ms. Customer Complaints
2,330, Merchant Complaints 199.

## Impact
Impact concentrated on the UPI Core path.
Expected active window: 07 Feb - 11 Feb.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Core.
- 08:30 — anomaly flagged by KPI sweep (RPT-D34-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-08.
Permanent fix tracked as DEC-2026-08.

Refs: upi_kpis_month.xlsx, RPT-D34-DAILY, RCA-2026-08, DEC-2026-08, TEAMS-D34-MON
