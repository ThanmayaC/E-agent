---
id: RPT-D185-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-08T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 08 Jul 2026)

**Report ID:** RPT-D185-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 08 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 185 of 206)

## Transaction summary
The rail processed 742.8M UPI transactions on Wednesday — a steady mid-week day — down 9.7M on the same day last week. Success landed at 99.01% and settlement at 99.67%, held back by live issues on UPI 123Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 742.8  (▼13.8 d/d, ▼9.7 w/w, ▼53.1 m/m)
- **Success Rate:** 99.01%  (▼0.03 d/d, ▼0.48 w/w, ▼0.12 m/m)
- **Settlement Success:** 99.67%  (▼0.31 d/d, ▼0.31 w/w, ▼0.28 m/m)
- **Technical Declines:** 0.35%  (▼0.06 d/d, ▲0.07 w/w, ▼0.2 m/m)
- **Business Declines:** 0.15%  (▼0.01 w/w, ▼0.09 m/m)
- **Customer Complaints:** 1,069  (▼112 d/d, ▲143 w/w, ▼1073 m/m)
- **Merchant Complaints:** 91  (▼4 w/w, ▼143 m/m)
- **Fraud Alerts:** 729  (▲4 d/d, ▼4 w/w, ▼431 m/m)
- **Risk Score:** 19  (▼15 m/m)
- **Response Time:** 559 ms  (▼25 d/d, ▲15 w/w, ▼194 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 241.8 | 99.67% |
| HDFC Bank | 79.4 | 99.42% |
| Bank of Baroda | 57.2 | 99.26% |
| Union Bank of India | 50.1 | 99.63% |
| Axis Bank | 45.8 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 354.8 | 99.51% | 198 ms |
| Google Pay | 242.9 | 99.35% | 241 ms |
| Paytm | 58.9 | 99.53% | 201 ms |
| Navi | 27.3 | 99.53% | 304 ms |
| SuperMoney | 14.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 274.8 |
| Person to Person | 263.7 |
| QR Payments | 70.6 |
| UPI Lite | 35.7 |
| UPI Autopay | 24.5 |

## Failure analysis
- INC-2026-10 — feature-level degradation on UPI 123Pay (day 2 of 5); see RCA-2026-10.

## Recommendations
Stay on the open incident: keep recovery monitoring on UPI 123Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D185-MON) and any meetings/emails on 08 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D185-MON, RPT-D184-DAILY, INC-2026-10, RCA-2026-10
