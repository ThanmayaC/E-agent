---
id: RPT-D140-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-24T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 24 May 2026)

**Report ID:** RPT-D140-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 24 May 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 140 of 206)

## Transaction summary
The rail processed 600.3M UPI transactions on Sunday — a quiet Sunday — down 3.5M on the same day last week. Success landed at 99.63% and settlement at 99.43%, held back by live issues on BHIM (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 600.3  (▼49.3 d/d, ▼3.5 w/w, ▼195.6 m/m)
- **Success Rate:** 99.63%  (▲0.73 d/d, ▼0.35 w/w, ▲0.5 m/m)
- **Settlement Success:** 99.43%  (▼0.29 d/d, ▲0.46 w/w, ▼0.52 m/m)
- **Technical Declines:** 0.33%  (▲0.01 d/d, ▼0.22 m/m)
- **Business Declines:** 0.3%  (▲0.1 d/d, ▲0.13 w/w, ▲0.06 m/m)
- **Customer Complaints:** 1,515  (▲306 d/d, ▲368 w/w, ▼627 m/m)
- **Merchant Complaints:** 113  (▼57 d/d, ▼6 w/w, ▼121 m/m)
- **Fraud Alerts:** 1,094  (▲272 d/d, ▲266 w/w, ▼66 m/m)
- **Risk Score:** 41  (▲19 d/d, ▲19 w/w, ▲7 m/m)
- **Response Time:** 588 ms  (▼3 d/d, ▼11 w/w, ▼165 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 195.4 | 99.67% |
| HDFC Bank | 64.2 | 99.42% |
| Bank of Baroda | 46.2 | 99.26% |
| Union Bank of India | 40.5 | 99.63% |
| Axis Bank | 37.0 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 286.7 | 99.51% | 198 ms |
| Google Pay | 196.3 | 99.35% | 241 ms |
| Paytm | 47.6 | 99.53% | 201 ms |
| Navi | 22.1 | 99.53% | 304 ms |
| SuperMoney | 11.7 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 222.1 |
| Person to Person | 213.1 |
| QR Payments | 57.0 |
| UPI Lite | 28.8 |
| UPI Autopay | 19.8 |

## Failure analysis
- INC-2026-18 — fraud / risk spike on BHIM (day 1 of 4); see RCA-2026-18.

## Recommendations
Stay on the open incident: keep recovery monitoring on BHIM and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D140-MON) and any meetings/emails on 24 May.

Refs: upi_kpis_month.xlsx, TEAMS-D140-MON, RPT-D139-DAILY, INC-2026-18, RCA-2026-18
