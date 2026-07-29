---
id: RPT-D77-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-22T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 22 Mar 2026)

**Report ID:** RPT-D77-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 22 Mar 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 77 of 206)

## Transaction summary
The rail processed 556.8M UPI transactions on Sunday — a quiet Sunday — down 8.6M on the same day last week. Success landed at 99.63% and settlement at 99.74%, held back by live issues on YONO SBI (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 556.8  (▼54.8 d/d, ▼8.6 w/w, ▼239.1 m/m)
- **Success Rate:** 99.63%  (▲1.23 d/d, ▲1.13 w/w, ▲0.5 m/m)
- **Settlement Success:** 99.74%  (▲0.1 d/d, ▼0.24 w/w, ▼0.21 m/m)
- **Technical Declines:** 0.5%  (▼0.05 d/d, ▲0.08 w/w, ▼0.05 m/m)
- **Business Declines:** 0.2%  (▼0.04 m/m)
- **Customer Complaints:** 1,743  (▼188 d/d, ▲196 w/w, ▼399 m/m)
- **Merchant Complaints:** 159  (▲1 d/d, ▼5 w/w, ▼75 m/m)
- **Fraud Alerts:** 950  (▼3 d/d, ▼21 w/w, ▼210 m/m)
- **Risk Score:** 27  (▼7 m/m)
- **Response Time:** 717 ms  (▼30 d/d, ▲44 w/w, ▼36 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 181.2 | 99.67% |
| HDFC Bank | 59.5 | 99.42% |
| Bank of Baroda | 42.9 | 99.26% |
| Union Bank of India | 37.6 | 99.63% |
| Axis Bank | 34.3 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 266.0 | 99.51% | 198 ms |
| Google Pay | 182.1 | 99.35% | 241 ms |
| Paytm | 44.2 | 99.53% | 201 ms |
| Navi | 20.5 | 99.53% | 304 ms |
| SuperMoney | 10.9 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 206.0 |
| Person to Person | 197.7 |
| QR Payments | 52.9 |
| UPI Lite | 26.7 |
| UPI Autopay | 18.4 |

## Failure analysis
- INC-2026-17 — PSP callback latency increase on YONO SBI (day 2 of 3); see RCA-2026-17.

## Recommendations
Stay on the open incident: keep recovery monitoring on YONO SBI and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D77-MON) and any meetings/emails on 22 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D77-MON, RPT-D76-DAILY, INC-2026-17, RCA-2026-17
