---
id: RPT-D03-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-24T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 24 Jun 2026)

**Report ID:** RPT-D03-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 24 Jun 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 3 of 180)

## Transaction summary
The rail processed 767.4M UPI transactions on Wednesday — a steady mid-week day — the first day in the window. Success landed at 97.39% and settlement at 99.05%, held back by live issues on Union Bank of India (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 767.4  (▼5.5 d/d, ▲22.5 m/m)
- **Success Rate:** 97.39%  (▼1.96 d/d, ▼2.21 m/m)
- **Settlement Success:** 99.05%  (▼0.51 d/d, ▼0.38 m/m)
- **Technical Declines:** 0.92%  (▲0.47 d/d, ▲0.47 m/m)
- **Business Declines:** 0.2%
- **Customer Complaints:** 3,286  (▲1356 d/d, ▲1344 m/m)
- **Merchant Complaints:** 434  (▲227 d/d, ▲223 m/m)
- **Fraud Alerts:** 1,051  (▼1 d/d)
- **Risk Score:** 31
- **Response Time:** 847 ms  (▲112 d/d, ▲105 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 246.7 | 99.5% |
| HDFC Bank | 84.7 | 99.55% |
| Bank of Baroda | 60.9 | 99.64% |
| Union Bank of India | 52.9 | 97.23% |
| ICICI Bank | 47.3 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 366.1 | 99.14% | 231 ms |
| Google Pay | 250.7 | 99.17% | 316 ms |
| Paytm | 61.9 | 99.06% | 192 ms |
| Navi | 28.3 | 99.17% | 225 ms |
| SuperMoney | 15.0 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 287.8 |
| Person to Person | 272.4 |
| QR Payments | 72.9 |
| UPI Lite | 36.8 |
| UPI Autopay | 25.3 |

## Failure analysis
- INC-2026-01 — bank timeout / 5xx spike on Union Bank of India (day 1 of 4); see RCA-2026-01.

## Recommendations
Stay on the open incident: keep recovery monitoring on Union Bank of India and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D03-MON) and any meetings/emails on 24 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D03-MON, RPT-D02-DAILY, INC-2026-01, RCA-2026-01
