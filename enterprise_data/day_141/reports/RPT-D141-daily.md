---
id: RPT-D141-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-25T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 25 May 2026)

**Report ID:** RPT-D141-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 25 May 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 141 of 206)

## Transaction summary
The rail processed 704.5M UPI transactions on Monday — the Monday ramp-up after the weekend — up 11.0M on the same day last week. Success landed at 99.02% and settlement at 99.35%, held back by live issues on BHIM (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 704.5  (▲104.2 d/d, ▲11.0 w/w, ▼91.4 m/m)
- **Success Rate:** 99.02%  (▼0.61 d/d, ▲0.12 w/w, ▼0.11 m/m)
- **Settlement Success:** 99.35%  (▼0.08 d/d, ▲0.38 w/w, ▼0.6 m/m)
- **Technical Declines:** 0.32%  (▼0.01 d/d, ▼0.01 w/w, ▼0.23 m/m)
- **Business Declines:** 0.25%  (▼0.05 d/d, ▲0.08 w/w, ▲0.01 m/m)
- **Customer Complaints:** 1,357  (▼158 d/d, ▲215 w/w, ▼785 m/m)
- **Merchant Complaints:** 114  (▲1 d/d, ▼4 w/w, ▼120 m/m)
- **Fraud Alerts:** 984  (▼110 d/d, ▲154 w/w, ▼176 m/m)
- **Risk Score:** 33  (▼8 d/d, ▲11 w/w, ▼1 m/m)
- **Response Time:** 585 ms  (▼3 d/d, ▼12 w/w, ▼168 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 229.3 | 99.67% |
| HDFC Bank | 75.3 | 99.42% |
| Bank of Baroda | 54.2 | 99.26% |
| Union Bank of India | 47.5 | 99.63% |
| Axis Bank | 43.4 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 336.5 | 99.51% | 198 ms |
| Google Pay | 230.4 | 99.35% | 241 ms |
| Paytm | 55.9 | 99.53% | 201 ms |
| Navi | 25.9 | 99.53% | 304 ms |
| SuperMoney | 13.7 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 260.7 |
| Person to Person | 250.1 |
| QR Payments | 66.9 |
| UPI Lite | 33.8 |
| UPI Autopay | 23.2 |

## Failure analysis
- INC-2026-18 — fraud / risk spike on BHIM (day 2 of 4); see RCA-2026-18.

## Recommendations
Stay on the open incident: keep recovery monitoring on BHIM and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D141-MON) and any meetings/emails on 25 May.

Refs: upi_kpis_month.xlsx, TEAMS-D141-MON, RPT-D140-DAILY, INC-2026-18, RCA-2026-18
