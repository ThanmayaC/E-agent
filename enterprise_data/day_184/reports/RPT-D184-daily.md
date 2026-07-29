---
id: RPT-D184-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-07T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 07 Jul 2026)

**Report ID:** RPT-D184-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 07 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 184 of 206)

## Transaction summary
The rail processed 756.6M UPI transactions on Tuesday — a steady mid-week day — down 74.9M on the same day last week. Success landed at 99.04% and settlement at 99.98%, held back by live issues on UPI 123Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 756.6  (▲37.9 d/d, ▼74.9 w/w, ▼39.3 m/m)
- **Success Rate:** 99.04%  (▼0.94 d/d, ▼0.58 w/w, ▼0.09 m/m)
- **Settlement Success:** 99.98%  (▲0.3 d/d, ▲0.03 m/m)
- **Technical Declines:** 0.41%  (▲0.13 d/d, ▲0.13 w/w, ▼0.14 m/m)
- **Business Declines:** 0.15%  (▼0.01 w/w, ▼0.09 m/m)
- **Customer Complaints:** 1,181  (▲274 d/d, ▲250 w/w, ▼961 m/m)
- **Merchant Complaints:** 91  (▼1 d/d, ▼2 w/w, ▼143 m/m)
- **Fraud Alerts:** 725  (▼12 d/d, ▼17 w/w, ▼435 m/m)
- **Risk Score:** 19  (▼1 w/w, ▼15 m/m)
- **Response Time:** 584 ms  (▲46 d/d, ▲35 w/w, ▼169 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 246.3 | 99.67% |
| HDFC Bank | 80.9 | 99.42% |
| Bank of Baroda | 58.2 | 99.26% |
| Union Bank of India | 51.0 | 99.63% |
| Axis Bank | 46.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 361.4 | 99.51% | 198 ms |
| Google Pay | 247.4 | 99.35% | 241 ms |
| Paytm | 60.0 | 99.53% | 201 ms |
| Navi | 27.8 | 99.53% | 304 ms |
| SuperMoney | 14.8 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 279.9 |
| Person to Person | 268.6 |
| QR Payments | 71.9 |
| UPI Lite | 36.3 |
| UPI Autopay | 25.0 |

## Failure analysis
- INC-2026-10 — feature-level degradation on UPI 123Pay (day 1 of 5); see RCA-2026-10.

## Recommendations
Stay on the open incident: keep recovery monitoring on UPI 123Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D184-MON) and any meetings/emails on 07 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D184-MON, RPT-D183-DAILY, INC-2026-10, RCA-2026-10
