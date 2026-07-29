---
id: RPT-D53-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-26T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 26 Feb 2026)

**Report ID:** RPT-D53-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 26 Feb 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 53 of 206)

## Transaction summary
The rail processed 684.2M UPI transactions on Thursday — a steady mid-week day — up 17.5M on the same day last week. Success landed at 99.65% and settlement at 99.22%, held back by live issues on Navi (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 684.2  (▼140.7 d/d, ▲17.5 w/w, ▼111.7 m/m)
- **Success Rate:** 99.65%  (▲0.36 d/d, ▲0.5 w/w, ▲0.52 m/m)
- **Settlement Success:** 99.22%  (▼0.13 d/d, ▼0.76 w/w, ▼0.73 m/m)
- **Technical Declines:** 0.55%  (▼0.06 d/d, ▲0.09 w/w)
- **Business Declines:** 0.21%  (▼0.06 d/d, ▼0.03 m/m)
- **Customer Complaints:** 1,965  (▼363 d/d, ▲236 w/w, ▼177 m/m)
- **Merchant Complaints:** 181  (▼5 w/w, ▼53 m/m)
- **Fraud Alerts:** 1,016  (▼110 d/d, ▼4 w/w, ▼144 m/m)
- **Risk Score:** 29  (▼8 d/d, ▼1 w/w, ▼5 m/m)
- **Response Time:** 746 ms  (▼41 d/d, ▲52 w/w, ▼7 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 222.7 | 99.67% |
| HDFC Bank | 73.2 | 99.42% |
| Bank of Baroda | 52.7 | 99.26% |
| Union Bank of India | 46.2 | 99.63% |
| Axis Bank | 42.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 326.8 | 99.51% | 198 ms |
| Google Pay | 223.8 | 99.35% | 241 ms |
| Paytm | 54.3 | 99.53% | 201 ms |
| Navi | 25.2 | 99.15% | 405 ms |
| SuperMoney | 13.3 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 253.2 |
| Person to Person | 242.9 |
| QR Payments | 65.0 |
| UPI Lite | 32.8 |
| UPI Autopay | 22.6 |

## Failure analysis
- INC-2026-22 — PSP callback latency increase on Navi (day 2 of 4); see RCA-2026-22.

## Recommendations
Stay on the open incident: keep recovery monitoring on Navi and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D53-MON) and any meetings/emails on 26 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D53-MON, RPT-D52-DAILY, INC-2026-22, RCA-2026-22
