---
id: RPT-D152-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-05T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 05 Jun 2026)

**Report ID:** RPT-D152-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 05 Jun 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 152 of 206)

## Transaction summary
The rail processed 733.1M UPI transactions on Friday — a steady mid-week day — down 75.8M on the same day last week. Success landed at 98.86% and settlement at 99.97%, held back by live issues on Punjab National Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 733.1  (▼12.7 d/d, ▼75.8 w/w, ▼62.8 m/m)
- **Success Rate:** 98.86%  (▼0.35 d/d, ▼0.76 w/w, ▼0.27 m/m)
- **Settlement Success:** 99.97%  (▲0.47 d/d, ▲0.47 w/w, ▲0.02 m/m)
- **Technical Declines:** 0.51%  (▼0.12 d/d, ▲0.13 w/w, ▼0.04 m/m)
- **Business Declines:** 0.16%  (▼0.01 w/w, ▼0.08 m/m)
- **Customer Complaints:** 1,522  (▼273 d/d, ▲254 w/w, ▼620 m/m)
- **Merchant Complaints:** 182  (▼44 d/d, ▲70 w/w, ▼52 m/m)
- **Fraud Alerts:** 782  (▼5 d/d, ▼18 w/w, ▼378 m/m)
- **Risk Score:** 21  (▼1 w/w, ▼13 m/m)
- **Response Time:** 635 ms  (▼27 d/d, ▲10 w/w, ▼118 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 238.6 | 99.67% |
| HDFC Bank | 78.4 | 99.42% |
| Bank of Baroda | 56.4 | 99.26% |
| Union Bank of India | 49.5 | 99.63% |
| Axis Bank | 45.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 350.2 | 99.51% | 198 ms |
| Google Pay | 239.8 | 99.35% | 241 ms |
| Paytm | 58.2 | 99.53% | 201 ms |
| Navi | 27.0 | 99.53% | 304 ms |
| SuperMoney | 14.3 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 271.2 |
| Person to Person | 260.3 |
| QR Payments | 69.6 |
| UPI Lite | 35.2 |
| UPI Autopay | 24.2 |

## Failure analysis
- INC-2026-06 — bank timeout / 5xx spike on Punjab National Bank (day 2 of 3); see RCA-2026-06.

## Recommendations
Stay on the open incident: keep recovery monitoring on Punjab National Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D152-MON) and any meetings/emails on 05 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D152-MON, RPT-D151-DAILY, INC-2026-06, RCA-2026-06
