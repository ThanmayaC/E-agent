---
id: RPT-D119-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-03T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 03 May 2026)

**Report ID:** RPT-D119-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 03 May 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 119 of 206)

## Transaction summary
The rail processed 584.7M UPI transactions on Sunday — a quiet Sunday — down 3.1M on the same day last week. Success landed at 99.98% and settlement at 98.7%, held back by live issues on Union Bank of India (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 584.7  (▼50.3 d/d, ▼3.1 w/w, ▼211.2 m/m)
- **Success Rate:** 99.98%  (▲0.28 w/w, ▲0.85 m/m)
- **Settlement Success:** 98.7%  (▼0.97 d/d, ▼1.28 w/w, ▼1.25 m/m)
- **Technical Declines:** 0.35%  (▼0.01 w/w, ▼0.2 m/m)
- **Business Declines:** 0.21%  (▼0.02 d/d, ▲0.02 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,304  (▼74 d/d, ▲23 w/w, ▼838 m/m)
- **Merchant Complaints:** 183  (▼49 d/d, ▲39 w/w, ▼51 m/m)
- **Fraud Alerts:** 850  (▼16 d/d, ▼24 w/w, ▼310 m/m)
- **Risk Score:** 23  (▼1 w/w, ▼11 m/m)
- **Response Time:** 617 ms  (▲6 d/d, ▼2 w/w, ▼136 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 190.3 | 99.67% |
| HDFC Bank | 62.5 | 99.42% |
| Bank of Baroda | 45.0 | 99.26% |
| Union Bank of India | 39.4 | 98.88% |
| Axis Bank | 36.0 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 279.3 | 99.51% | 198 ms |
| Google Pay | 191.2 | 99.35% | 241 ms |
| Paytm | 46.4 | 99.53% | 201 ms |
| Navi | 21.5 | 99.53% | 304 ms |
| SuperMoney | 11.4 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 216.3 |
| Person to Person | 207.6 |
| QR Payments | 55.5 |
| UPI Lite | 28.1 |
| UPI Autopay | 19.3 |

## Failure analysis
- INC-2026-05 — merchant settlement delay on Union Bank of India (day 3 of 3); see RCA-2026-05.

## Recommendations
Stay on the open incident: keep recovery monitoring on Union Bank of India and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D119-MON) and any meetings/emails on 03 May.

Refs: upi_kpis_month.xlsx, TEAMS-D119-MON, RPT-D118-DAILY, INC-2026-05, RCA-2026-05
