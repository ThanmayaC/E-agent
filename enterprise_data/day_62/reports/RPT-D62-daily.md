---
id: RPT-D62-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-07T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 07 Mar 2026)

**Report ID:** RPT-D62-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 07 Mar 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 62 of 206)

## Transaction summary
The rail processed 626.5M UPI transactions on Saturday — a lighter Saturday — down 141.1M on the same day last week. Success landed at 99.89% and settlement at 98.27%, held back by live issues on Bank of Baroda (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 626.5  (▼52.4 d/d, ▼141.1 w/w, ▼169.4 m/m)
- **Success Rate:** 99.89%  (▼0.05 d/d, ▲1.68 w/w, ▲0.76 m/m)
- **Settlement Success:** 98.27%  (▼0.31 d/d, ▼1.35 w/w, ▼1.68 m/m)
- **Technical Declines:** 0.43%  (▼0.01 d/d, ▼0.04 w/w, ▼0.12 m/m)
- **Business Declines:** 0.24%  (▼0.08 d/d, ▼0.06 w/w)
- **Customer Complaints:** 1,744  (▼252 d/d, ▼339 w/w, ▼398 m/m)
- **Merchant Complaints:** 253  (▼55 d/d, ▲76 w/w, ▲19 m/m)
- **Fraud Alerts:** 991  (▼103 d/d, ▼212 w/w, ▼169 m/m)
- **Risk Score:** 28  (▼9 d/d, ▼15 w/w, ▼6 m/m)
- **Response Time:** 674 ms  (▼30 w/w, ▼79 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 203.9 | 99.67% |
| HDFC Bank | 67.0 | 99.42% |
| Bank of Baroda | 48.2 | 98.82% |
| Union Bank of India | 42.3 | 99.63% |
| Axis Bank | 38.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 299.3 | 99.51% | 198 ms |
| Google Pay | 204.9 | 99.35% | 241 ms |
| Paytm | 49.7 | 99.53% | 201 ms |
| Navi | 23.0 | 99.53% | 304 ms |
| SuperMoney | 12.2 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 231.8 |
| Person to Person | 222.4 |
| QR Payments | 59.5 |
| UPI Lite | 30.1 |
| UPI Autopay | 20.7 |

## Failure analysis
- INC-2026-09 — merchant settlement delay on Bank of Baroda (day 2 of 2); see INC-2026-09.

## Recommendations
Stay on the open incident: keep recovery monitoring on Bank of Baroda and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D62-MON) and any meetings/emails on 07 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D62-MON, RPT-D61-DAILY, INC-2026-09
