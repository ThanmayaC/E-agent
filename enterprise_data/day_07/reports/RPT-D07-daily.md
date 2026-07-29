---
id: RPT-D07-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-11T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 11 Jan 2026)

**Report ID:** RPT-D07-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 11 Jan 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 7 of 206)

## Transaction summary
The rail processed 539.2M UPI transactions on Sunday — a quiet Sunday — the first day in the window. Success landed at 99.69% and settlement at 99.23%, held back by live issues on Punjab National Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 539.2  (▼50.7 d/d, ▼256.7 m/m)
- **Success Rate:** 99.69%  (▲0.87 d/d, ▲0.56 m/m)
- **Settlement Success:** 99.23%  (▼0.75 d/d, ▼0.72 m/m)
- **Technical Declines:** 0.72%  (▼0.16 d/d, ▲0.17 m/m)
- **Business Declines:** 0.24%
- **Customer Complaints:** 2,596  (▼387 d/d, ▲454 m/m)
- **Merchant Complaints:** 313  (▼76 d/d, ▲79 m/m)
- **Fraud Alerts:** 1,123  (▼16 d/d, ▼37 m/m)
- **Risk Score:** 33  (▼1 d/d, ▼1 m/m)
- **Response Time:** 791 ms  (▼37 d/d, ▲38 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 175.5 | 99.67% |
| HDFC Bank | 57.6 | 99.42% |
| Bank of Baroda | 41.5 | 99.26% |
| Union Bank of India | 36.4 | 99.63% |
| Axis Bank | 33.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 257.6 | 99.51% | 198 ms |
| Google Pay | 176.3 | 99.35% | 241 ms |
| Paytm | 42.8 | 99.53% | 201 ms |
| Navi | 19.8 | 99.53% | 304 ms |
| SuperMoney | 10.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 199.5 |
| Person to Person | 191.4 |
| QR Payments | 51.2 |
| UPI Lite | 25.9 |
| UPI Autopay | 17.8 |

## Failure analysis
- INC-2026-01 — bank timeout / 5xx spike on Punjab National Bank (day 3 of 4); see RCA-2026-01.

## Recommendations
Stay on the open incident: keep recovery monitoring on Punjab National Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D07-MON) and any meetings/emails on 11 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D07-MON, RPT-D06-DAILY, INC-2026-01, RCA-2026-01
