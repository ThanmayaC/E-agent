---
id: RPT-D08-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-12T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 12 Jan 2026)

**Report ID:** RPT-D08-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 12 Jan 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 8 of 206)

## Transaction summary
The rail processed 644.3M UPI transactions on Monday — the Monday ramp-up after the weekend — down 151.6M on the same day last week. Success landed at 98.78% and settlement at 99.98%, held back by live issues on Punjab National Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 644.3  (▲105.1 d/d, ▼151.6 w/w, ▼151.6 m/m)
- **Success Rate:** 98.78%  (▼0.91 d/d, ▼0.35 w/w, ▼0.35 m/m)
- **Settlement Success:** 99.98%  (▲0.75 d/d, ▲0.03 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.63%  (▼0.09 d/d, ▲0.08 w/w, ▲0.08 m/m)
- **Business Declines:** 0.24%
- **Customer Complaints:** 2,291  (▼305 d/d, ▲149 w/w, ▲149 m/m)
- **Merchant Complaints:** 268  (▼45 d/d, ▲34 w/w, ▲34 m/m)
- **Fraud Alerts:** 1,128  (▲5 d/d, ▼32 w/w, ▼32 m/m)
- **Risk Score:** 34  (▲1 d/d)
- **Response Time:** 764 ms  (▼27 d/d, ▲11 w/w, ▲11 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 209.7 | 99.67% |
| HDFC Bank | 68.9 | 99.42% |
| Bank of Baroda | 49.6 | 99.26% |
| Union Bank of India | 43.5 | 99.63% |
| Axis Bank | 39.7 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 307.8 | 99.51% | 198 ms |
| Google Pay | 210.7 | 99.35% | 241 ms |
| Paytm | 51.1 | 99.53% | 201 ms |
| Navi | 23.7 | 99.53% | 304 ms |
| SuperMoney | 12.6 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 238.4 |
| Person to Person | 228.7 |
| QR Payments | 61.2 |
| UPI Lite | 30.9 |
| UPI Autopay | 21.3 |

## Failure analysis
- INC-2026-01 — bank timeout / 5xx spike on Punjab National Bank (day 4 of 4); see RCA-2026-01.

## Recommendations
Stay on the open incident: keep recovery monitoring on Punjab National Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D08-MON) and any meetings/emails on 12 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D08-MON, RPT-D07-DAILY, INC-2026-01, RCA-2026-01
