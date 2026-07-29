---
id: RPT-D129-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-13T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 13 May 2026)

**Report ID:** RPT-D129-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 13 May 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 129 of 206)

## Transaction summary
The rail processed 707.1M UPI transactions on Wednesday — a steady mid-week day — down 15.9M on the same day last week. Success landed at 99.98% and settlement at 99.98%, held back by live issues on TravelGo, InsureWell (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 707.1  (▼0.7 d/d, ▼15.9 w/w, ▼88.8 m/m)
- **Success Rate:** 99.98%  (▲0.35 d/d, ▲0.85 m/m)
- **Settlement Success:** 99.98%  (▲1.09 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.34%  (▼0.01 w/w, ▼0.21 m/m)
- **Business Declines:** 0.22%  (▼0.03 d/d, ▲0.04 w/w, ▼0.02 m/m)
- **Customer Complaints:** 1,178  (▼3 d/d, ▼25 w/w, ▼964 m/m)
- **Merchant Complaints:** 165  (▼30 d/d, ▲40 w/w, ▼69 m/m)
- **Fraud Alerts:** 838  (▲2 d/d, ▼5 w/w, ▼322 m/m)
- **Risk Score:** 23  (▼11 m/m)
- **Response Time:** 604 ms  (▼1 d/d, ▼9 w/w, ▼149 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 230.2 | 99.67% |
| HDFC Bank | 75.6 | 99.42% |
| Bank of Baroda | 54.4 | 99.26% |
| Union Bank of India | 47.7 | 99.63% |
| Axis Bank | 43.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 337.8 | 99.51% | 198 ms |
| Google Pay | 231.2 | 99.35% | 241 ms |
| Paytm | 56.1 | 99.53% | 201 ms |
| Navi | 26.0 | 99.53% | 304 ms |
| SuperMoney | 13.8 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 261.6 |
| Person to Person | 251.0 |
| QR Payments | 67.2 |
| UPI Lite | 33.9 |
| UPI Autopay | 23.3 |

## Failure analysis
- INC-2026-13 — merchant decline-rate spike on TravelGo, InsureWell (day 2 of 5); see RCA-2026-13.

## Recommendations
Stay on the open incident: keep recovery monitoring on TravelGo, InsureWell and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D129-MON) and any meetings/emails on 13 May.

Refs: upi_kpis_month.xlsx, TEAMS-D129-MON, RPT-D128-DAILY, INC-2026-13, RCA-2026-13
