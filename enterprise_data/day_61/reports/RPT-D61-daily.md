---
id: RPT-D61-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-06T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 06 Mar 2026)

**Report ID:** RPT-D61-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 06 Mar 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 61 of 206)

## Transaction summary
The rail processed 678.9M UPI transactions on Friday — a steady mid-week day — down 142.3M on the same day last week. Success landed at 99.94% and settlement at 98.58%, held back by live issues on Bank of Baroda, Navi (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 678.9  (▼14.6 d/d, ▼142.3 w/w, ▼117.0 m/m)
- **Success Rate:** 99.94%  (▲1.69 d/d, ▲1.6 w/w, ▲0.81 m/m)
- **Settlement Success:** 98.58%  (▼1.4 d/d, ▼0.38 w/w, ▼1.37 m/m)
- **Technical Declines:** 0.44%  (▼0.06 w/w, ▼0.11 m/m)
- **Business Declines:** 0.32%  (▲0.01 d/d, ▲0.11 w/w, ▲0.08 m/m)
- **Customer Complaints:** 1,996  (▲29 d/d, ▲186 w/w, ▼146 m/m)
- **Merchant Complaints:** 308  (▲136 d/d, ▲128 w/w, ▲74 m/m)
- **Fraud Alerts:** 1,094  (▼119 d/d, ▲92 w/w, ▼66 m/m)
- **Risk Score:** 37  (▼6 d/d, ▲8 w/w, ▲3 m/m)
- **Response Time:** 674 ms  (▼13 d/d, ▼42 w/w, ▼79 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 221.0 | 99.67% |
| HDFC Bank | 72.6 | 99.42% |
| Bank of Baroda | 52.2 | 98.54% |
| Union Bank of India | 45.8 | 99.63% |
| Axis Bank | 41.8 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 324.3 | 99.51% | 198 ms |
| Google Pay | 222.0 | 99.35% | 241 ms |
| Paytm | 53.9 | 99.53% | 201 ms |
| Navi | 25.0 | 99.19% | 469 ms |
| SuperMoney | 13.2 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 251.2 |
| Person to Person | 241.0 |
| QR Payments | 64.5 |
| UPI Lite | 32.6 |
| UPI Autopay | 22.4 |

## Failure analysis
- INC-2026-03 — fraud / risk spike on Navi (day 3 of 3); see RCA-2026-03.
- INC-2026-09 — merchant settlement delay on Bank of Baroda (day 1 of 2); see INC-2026-09.

## Recommendations
Stay on the open incidents: keep recovery monitoring on Bank of Baroda, Navi and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D61-MON) and any meetings/emails on 06 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D61-MON, RPT-D60-DAILY, INC-2026-03, INC-2026-09, RCA-2026-03
