---
id: RPT-D131-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-15T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 15 May 2026)

**Report ID:** RPT-D131-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 15 May 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 131 of 206)

## Transaction summary
The rail processed 724.2M UPI transactions on Friday — a steady mid-week day — up 6.3M on the same day last week. Success landed at 99.98% and settlement at 99.98%, held back by live issues on TravelGo, InsureWell (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 724.2  (▲1.0 d/d, ▲6.3 w/w, ▼71.7 m/m)
- **Success Rate:** 99.98%  (▲0.78 d/d, ▲0.39 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.98%  (▲0.28 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.33%  (▼0.01 d/d, ▼0.02 w/w, ▼0.22 m/m)
- **Business Declines:** 0.18%  (▼0.02 d/d, ▼0.05 w/w, ▼0.06 m/m)
- **Customer Complaints:** 1,175  (▲9 d/d, ▼180 w/w, ▼967 m/m)
- **Merchant Complaints:** 132  (▼13 d/d, ▼87 w/w, ▼102 m/m)
- **Fraud Alerts:** 840  (▲6 d/d, ▼3 w/w, ▼320 m/m)
- **Risk Score:** 23  (▼11 m/m)
- **Response Time:** 601 ms  (▲6 d/d, ▼4 w/w, ▼152 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 235.7 | 99.67% |
| HDFC Bank | 77.4 | 99.42% |
| Bank of Baroda | 55.7 | 99.26% |
| Union Bank of India | 48.9 | 99.63% |
| Axis Bank | 44.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 345.9 | 99.51% | 198 ms |
| Google Pay | 236.8 | 99.35% | 241 ms |
| Paytm | 57.4 | 99.53% | 201 ms |
| Navi | 26.6 | 99.53% | 304 ms |
| SuperMoney | 14.1 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 268.0 |
| Person to Person | 257.1 |
| QR Payments | 68.8 |
| UPI Lite | 34.8 |
| UPI Autopay | 23.9 |

## Failure analysis
- INC-2026-13 — merchant decline-rate spike on TravelGo, InsureWell (day 4 of 5); see RCA-2026-13.

## Recommendations
Stay on the open incident: keep recovery monitoring on TravelGo, InsureWell and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D131-MON) and any meetings/emails on 15 May.

Refs: upi_kpis_month.xlsx, TEAMS-D131-MON, RPT-D130-DAILY, INC-2026-13, RCA-2026-13
