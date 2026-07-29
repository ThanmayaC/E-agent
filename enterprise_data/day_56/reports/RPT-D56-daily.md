---
id: RPT-D56-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-01T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 01 Mar 2026)

**Report ID:** RPT-D56-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 01 Mar 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 56 of 206)

## Transaction summary
The rail processed 567.0M UPI transactions on Sunday — a quiet Sunday — up 3.0M on the same day last week. Success landed at 98.4% and settlement at 98.79%, held back by live issues on Navi (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 567.0  (▼200.6 d/d, ▲3.0 w/w, ▼228.9 m/m)
- **Success Rate:** 98.4%  (▲0.19 d/d, ▼1.21 w/w, ▼0.73 m/m)
- **Settlement Success:** 98.79%  (▼0.83 d/d, ▲0.16 w/w, ▼1.16 m/m)
- **Technical Declines:** 0.45%  (▼0.02 d/d, ▼0.01 w/w, ▼0.1 m/m)
- **Business Declines:** 0.27%  (▼0.03 d/d, ▲0.06 w/w, ▲0.03 m/m)
- **Customer Complaints:** 1,878  (▼205 d/d, ▲179 w/w, ▼264 m/m)
- **Merchant Complaints:** 178  (▲1 d/d, ▼6 w/w, ▼56 m/m)
- **Fraud Alerts:** 1,131  (▼72 d/d, ▲105 w/w, ▼29 m/m)
- **Risk Score:** 38  (▼5 d/d, ▲9 w/w, ▲4 m/m)
- **Response Time:** 683 ms  (▼21 d/d, ▼10 w/w, ▼70 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 184.6 | 99.67% |
| HDFC Bank | 60.6 | 99.42% |
| Bank of Baroda | 43.6 | 99.26% |
| Union Bank of India | 38.3 | 99.63% |
| Axis Bank | 34.9 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 270.8 | 99.51% | 198 ms |
| Google Pay | 185.4 | 99.35% | 241 ms |
| Paytm | 45.0 | 99.53% | 201 ms |
| Navi | 20.8 | 99.15% | 405 ms |
| SuperMoney | 11.1 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 209.8 |
| Person to Person | 201.3 |
| QR Payments | 53.9 |
| UPI Lite | 27.2 |
| UPI Autopay | 18.7 |

## Failure analysis
- INC-2026-16 — fraud / risk spike on Navi (day 2 of 2); see INC-2026-16.

## Recommendations
Stay on the open incident: keep recovery monitoring on Navi and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D56-MON) and any meetings/emails on 01 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D56-MON, RPT-D55-DAILY, INC-2026-16
