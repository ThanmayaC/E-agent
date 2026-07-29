---
id: RPT-D05-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-09T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 09 Jan 2026)

**Report ID:** RPT-D05-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 09 Jan 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 5 of 206)

## Transaction summary
The rail processed 658.6M UPI transactions on Friday — a steady mid-week day — the first day in the window. Success landed at 98.72% and settlement at 98.86%, held back by live issues on Punjab National Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 658.6  (▲15.5 d/d, ▼137.3 m/m)
- **Success Rate:** 98.72%  (▼1.26 d/d, ▼0.41 m/m)
- **Settlement Success:** 98.86%  (▼1.12 d/d, ▼1.09 m/m)
- **Technical Declines:** 1.11%  (▲0.56 d/d, ▲0.56 m/m)
- **Business Declines:** 0.24%
- **Customer Complaints:** 3,596  (▲1465 d/d, ▲1454 m/m)
- **Merchant Complaints:** 482  (▲251 d/d, ▲248 m/m)
- **Fraud Alerts:** 1,149  (▲14 d/d, ▼11 m/m)
- **Risk Score:** 34
- **Response Time:** 878 ms  (▲128 d/d, ▲125 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 214.4 | 99.67% |
| HDFC Bank | 70.4 | 99.42% |
| Bank of Baroda | 50.7 | 99.26% |
| Union Bank of India | 44.4 | 99.63% |
| Axis Bank | 40.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 314.6 | 99.51% | 198 ms |
| Google Pay | 215.4 | 99.35% | 241 ms |
| Paytm | 52.2 | 99.53% | 201 ms |
| Navi | 24.2 | 99.53% | 304 ms |
| SuperMoney | 12.8 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 243.7 |
| Person to Person | 233.8 |
| QR Payments | 62.6 |
| UPI Lite | 31.6 |
| UPI Autopay | 21.7 |

## Failure analysis
- INC-2026-01 — bank timeout / 5xx spike on Punjab National Bank (day 1 of 4); see RCA-2026-01.

## Recommendations
Stay on the open incident: keep recovery monitoring on Punjab National Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D05-MON) and any meetings/emails on 09 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D05-MON, RPT-D04-DAILY, INC-2026-01, RCA-2026-01
