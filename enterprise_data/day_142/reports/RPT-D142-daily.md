---
id: RPT-D142-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-26T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 26 May 2026)

**Report ID:** RPT-D142-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 26 May 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 142 of 206)

## Transaction summary
The rail processed 722.8M UPI transactions on Tuesday — a steady mid-week day — up 6.8M on the same day last week. Success landed at 98.73% and settlement at 99.98%, held back by live issues on BHIM (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 722.8  (▲18.3 d/d, ▲6.8 w/w, ▼73.1 m/m)
- **Success Rate:** 98.73%  (▼0.29 d/d, ▼1.0 w/w, ▼0.4 m/m)
- **Settlement Success:** 99.98%  (▲0.63 d/d, ▲0.57 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.32%  (▼0.01 w/w, ▼0.23 m/m)
- **Business Declines:** 0.21%  (▼0.04 d/d, ▲0.04 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,244  (▼113 d/d, ▲101 w/w, ▼898 m/m)
- **Merchant Complaints:** 114  (▼3 w/w, ▼120 m/m)
- **Fraud Alerts:** 902  (▼82 d/d, ▲86 w/w, ▼258 m/m)
- **Risk Score:** 28  (▼5 d/d, ▲6 w/w, ▼6 m/m)
- **Response Time:** 588 ms  (▲3 d/d, ▼1 w/w, ▼165 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 235.3 | 99.67% |
| HDFC Bank | 77.3 | 99.42% |
| Bank of Baroda | 55.6 | 99.26% |
| Union Bank of India | 48.8 | 99.63% |
| Axis Bank | 44.5 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 345.2 | 99.51% | 198 ms |
| Google Pay | 236.4 | 99.35% | 241 ms |
| Paytm | 57.3 | 99.53% | 201 ms |
| Navi | 26.6 | 99.53% | 304 ms |
| SuperMoney | 14.1 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 267.4 |
| Person to Person | 256.6 |
| QR Payments | 68.7 |
| UPI Lite | 34.7 |
| UPI Autopay | 23.9 |

## Failure analysis
- INC-2026-18 — fraud / risk spike on BHIM (day 3 of 4); see RCA-2026-18.

## Recommendations
Stay on the open incident: keep recovery monitoring on BHIM and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D142-MON) and any meetings/emails on 26 May.

Refs: upi_kpis_month.xlsx, TEAMS-D142-MON, RPT-D141-DAILY, INC-2026-18, RCA-2026-18
