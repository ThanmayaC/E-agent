---
id: RPT-D102-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-16T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 16 Apr 2026)

**Report ID:** RPT-D102-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 16 Apr 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 102 of 206)

## Transaction summary
The rail processed 697.9M UPI transactions on Thursday — a steady mid-week day — down 7.0M on the same day last week. Success landed at 99.66% and settlement at 99.04%, held back by live issues on Kotak Mahindra Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 697.9  (▼11.9 d/d, ▼7.0 w/w, ▼98.0 m/m)
- **Success Rate:** 99.66%  (▲0.41 d/d, ▲1.09 w/w, ▲0.53 m/m)
- **Settlement Success:** 99.04%  (▲0.39 d/d, ▼0.94 w/w, ▼0.91 m/m)
- **Technical Declines:** 0.37%  (▼0.01 d/d, ▼0.08 w/w, ▼0.18 m/m)
- **Business Declines:** 0.22%  (▼0.02 d/d, ▲0.03 w/w, ▼0.02 m/m)
- **Customer Complaints:** 1,440  (▼71 d/d, ▼98 w/w, ▼702 m/m)
- **Merchant Complaints:** 204  (▼45 d/d, ▲34 w/w, ▼30 m/m)
- **Fraud Alerts:** 895  (▼9 d/d, ▼10 w/w, ▼265 m/m)
- **Risk Score:** 25  (▼9 m/m)
- **Response Time:** 634 ms  (▲5 d/d, ▼16 w/w, ▼119 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 227.2 | 99.67% |
| HDFC Bank | 74.6 | 99.42% |
| Bank of Baroda | 53.7 | 99.26% |
| Union Bank of India | 47.1 | 99.63% |
| Axis Bank | 43.0 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 333.4 | 99.51% | 198 ms |
| Google Pay | 228.2 | 99.35% | 241 ms |
| Paytm | 55.4 | 99.53% | 201 ms |
| Navi | 25.7 | 99.53% | 304 ms |
| SuperMoney | 13.6 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 258.2 |
| Person to Person | 247.8 |
| QR Payments | 66.3 |
| UPI Lite | 33.5 |
| UPI Autopay | 23.0 |

## Failure analysis
- INC-2026-20 — merchant settlement delay on Kotak Mahindra Bank (day 2 of 3); see RCA-2026-20.

## Recommendations
Stay on the open incident: keep recovery monitoring on Kotak Mahindra Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D102-MON) and any meetings/emails on 16 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D102-MON, RPT-D101-DAILY, INC-2026-20, RCA-2026-20
