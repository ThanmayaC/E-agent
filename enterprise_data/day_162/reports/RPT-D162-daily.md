---
id: RPT-D162-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-30T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 30 Nov 2026)

**Report ID:** RPT-D162-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 30 Nov 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 162 of 180)

## Transaction summary
The rail processed 1258.2M UPI transactions on Monday — a campaign-driven high-volume day — up 269.5M on the same day last week. Success landed at 99.98% and settlement at 99.98%, held back by live issues on Bank of Baroda (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1258.2  (▲121.0 d/d, ▲269.5 w/w, ▲513.3 m/m)
- **Success Rate:** 99.98%  (▲1.06 d/d, ▲0.08 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.91 d/d, ▲0.55 m/m)
- **Technical Declines:** 0.34%  (▼0.06 d/d, ▲0.09 w/w, ▼0.11 m/m)
- **Business Declines:** 0.13%  (▼0.01 w/w, ▼0.07 m/m)
- **Customer Complaints:** 1,149  (▼145 d/d, ▲174 w/w, ▼793 m/m)
- **Merchant Complaints:** 129  (▼24 d/d, ▲35 w/w, ▼82 m/m)
- **Fraud Alerts:** 697  (▼11 d/d, ▼35 w/w, ▼354 m/m)
- **Risk Score:** 19  (▼1 w/w, ▼12 m/m)
- **Response Time:** 576 ms  (▼21 d/d, ▲23 w/w, ▼166 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 404.5 | 99.5% |
| HDFC Bank | 138.8 | 99.55% |
| Bank of Baroda | 99.8 | 99.19% |
| Union Bank of India | 86.7 | 99.43% |
| ICICI Bank | 77.6 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 600.3 | 99.14% | 231 ms |
| Google Pay | 411.0 | 99.17% | 316 ms |
| Paytm | 101.5 | 99.06% | 192 ms |
| Navi | 46.4 | 99.17% | 225 ms |
| SuperMoney | 24.5 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 471.8 |
| Person to Person | 446.7 |
| QR Payments | 119.5 |
| UPI Lite | 60.4 |
| UPI Autopay | 41.5 |

## Failure analysis
- INC-2026-22 — bank timeout / 5xx spike on Bank of Baroda (day 2 of 2); see INC-2026-22.

## Recommendations
Stay on the open incident: keep recovery monitoring on Bank of Baroda and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D162-MON) and any meetings/emails on 30 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D162-MON, RPT-D161-DAILY, INC-2026-22
