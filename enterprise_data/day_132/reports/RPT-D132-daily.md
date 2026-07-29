---
id: RPT-D132-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-16T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 16 May 2026)

**Report ID:** RPT-D132-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 16 May 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 132 of 206)

## Transaction summary
The rail processed 643.6M UPI transactions on Saturday — a lighter Saturday — up 3.5M on the same day last week. Success landed at 99.98% and settlement at 99.98%, held back by live issues on TravelGo, InsureWell (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 643.6  (▼80.6 d/d, ▲3.5 w/w, ▼152.3 m/m)
- **Success Rate:** 99.98%  (▲0.36 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.98%  (▲0.1 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.34%  (▲0.01 d/d, ▼0.21 m/m)
- **Business Declines:** 0.18%  (▼0.03 w/w, ▼0.06 m/m)
- **Customer Complaints:** 1,149  (▼26 d/d, ▼139 w/w, ▼993 m/m)
- **Merchant Complaints:** 124  (▼8 d/d, ▼60 w/w, ▼110 m/m)
- **Fraud Alerts:** 824  (▼16 d/d, ▼18 w/w, ▼336 m/m)
- **Risk Score:** 22  (▼1 d/d, ▼1 w/w, ▼12 m/m)
- **Response Time:** 601 ms  (▼2 w/w, ▼152 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 209.5 | 99.67% |
| HDFC Bank | 68.8 | 99.42% |
| Bank of Baroda | 49.5 | 99.26% |
| Union Bank of India | 43.4 | 99.63% |
| Axis Bank | 39.7 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 307.4 | 99.51% | 198 ms |
| Google Pay | 210.5 | 99.35% | 241 ms |
| Paytm | 51.1 | 99.53% | 201 ms |
| Navi | 23.7 | 99.53% | 304 ms |
| SuperMoney | 12.6 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 238.1 |
| Person to Person | 228.5 |
| QR Payments | 61.1 |
| UPI Lite | 30.9 |
| UPI Autopay | 21.2 |

## Failure analysis
- INC-2026-13 — merchant decline-rate spike on TravelGo, InsureWell (day 5 of 5); see RCA-2026-13.

## Recommendations
Stay on the open incident: keep recovery monitoring on TravelGo, InsureWell and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D132-MON) and any meetings/emails on 16 May.

Refs: upi_kpis_month.xlsx, TEAMS-D132-MON, RPT-D131-DAILY, INC-2026-13, RCA-2026-13
