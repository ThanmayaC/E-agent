---
id: RPT-D31-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-04T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 04 Feb 2026)

**Report ID:** RPT-D31-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 04 Feb 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 31 of 206)

## Transaction summary
The rail processed 665.4M UPI transactions on Wednesday — a steady mid-week day — down 94.1M on the same day last week. Success landed at 98.61% and settlement at 99.98%, held back by live issues on HDFC MobileBanking (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 665.4  (▼4.6 d/d, ▼94.1 w/w, ▼130.5 m/m)
- **Success Rate:** 98.61%  (▼0.93 d/d, ▼0.94 w/w, ▼0.52 m/m)
- **Settlement Success:** 99.98%  (▲0.63 d/d, ▲0.29 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.49%  (▼0.01 d/d, ▼0.02 w/w, ▼0.06 m/m)
- **Business Declines:** 0.39%  (▲0.17 d/d, ▲0.1 w/w, ▲0.15 m/m)
- **Customer Complaints:** 2,525  (▲664 d/d, ▲355 w/w, ▲383 m/m)
- **Merchant Complaints:** 203  (▲1 d/d, ▼7 w/w, ▼31 m/m)
- **Fraud Alerts:** 1,419  (▲339 d/d, ▲200 w/w, ▲259 m/m)
- **Risk Score:** 57  (▲26 d/d, ▲16 w/w, ▲23 m/m)
- **Response Time:** 716 ms  (▲2 d/d, ▼12 w/w, ▼37 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 216.6 | 99.67% |
| HDFC Bank | 71.1 | 99.42% |
| Bank of Baroda | 51.2 | 99.26% |
| Union Bank of India | 44.9 | 99.63% |
| Axis Bank | 41.0 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 317.8 | 99.51% | 198 ms |
| Google Pay | 217.6 | 99.35% | 241 ms |
| Paytm | 52.8 | 99.53% | 201 ms |
| Navi | 24.5 | 99.53% | 304 ms |
| SuperMoney | 13.0 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 246.2 |
| Person to Person | 236.2 |
| QR Payments | 63.2 |
| UPI Lite | 31.9 |
| UPI Autopay | 22.0 |

## Failure analysis
- INC-2026-02 — fraud / risk spike on HDFC MobileBanking (day 1 of 5); see RCA-2026-02.

## Recommendations
Stay on the open incident: keep recovery monitoring on HDFC MobileBanking and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D31-MON) and any meetings/emails on 04 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D31-MON, RPT-D30-DAILY, INC-2026-02, RCA-2026-02
