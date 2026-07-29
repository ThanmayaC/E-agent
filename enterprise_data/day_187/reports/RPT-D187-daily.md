---
id: RPT-D187-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-10T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 10 Jul 2026)

**Report ID:** RPT-D187-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 10 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 187 of 206)

## Transaction summary
The rail processed 750.3M UPI transactions on Friday — a steady mid-week day — up 3.6M on the same day last week. Success landed at 99.63% and settlement at 99.31%, held back by live issues on UPI 123Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 750.3  (▼153.5 d/d, ▲3.6 w/w, ▼45.6 m/m)
- **Success Rate:** 99.63%  (▼0.35 d/d, ▼0.35 w/w, ▲0.5 m/m)
- **Settlement Success:** 99.31%  (▼0.03 d/d, ▼0.67 w/w, ▼0.64 m/m)
- **Technical Declines:** 0.29%  (▼0.02 d/d, ▲0.01 w/w, ▼0.26 m/m)
- **Business Declines:** 0.15%  (▼0.09 m/m)
- **Customer Complaints:** 941  (▼58 d/d, ▲20 w/w, ▼1201 m/m)
- **Merchant Complaints:** 89  (▼1 d/d, ▼5 w/w, ▼145 m/m)
- **Fraud Alerts:** 730  (▲8 d/d, ▼7 w/w, ▼430 m/m)
- **Risk Score:** 19  (▼15 m/m)
- **Response Time:** 544 ms  (▼7 d/d, ▼4 w/w, ▼209 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 244.2 | 99.67% |
| HDFC Bank | 80.2 | 99.42% |
| Bank of Baroda | 57.7 | 99.26% |
| Union Bank of India | 50.6 | 99.63% |
| Axis Bank | 46.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 358.4 | 99.51% | 198 ms |
| Google Pay | 245.4 | 99.35% | 241 ms |
| Paytm | 59.5 | 99.53% | 201 ms |
| Navi | 27.6 | 99.53% | 304 ms |
| SuperMoney | 14.6 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 277.6 |
| Person to Person | 266.4 |
| QR Payments | 71.3 |
| UPI Lite | 36.0 |
| UPI Autopay | 24.8 |

## Failure analysis
- INC-2026-10 — feature-level degradation on UPI 123Pay (day 4 of 5); see RCA-2026-10.

## Recommendations
Stay on the open incident: keep recovery monitoring on UPI 123Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D187-MON) and any meetings/emails on 10 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D187-MON, RPT-D186-DAILY, INC-2026-10, RCA-2026-10
