---
id: RPT-D22-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-26T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 26 Jan 2026)

**Report ID:** RPT-D22-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 26 Jan 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 22 of 206)

## Transaction summary
The rail processed 663.3M UPI transactions on Monday — the Monday ramp-up after the weekend — up 20.1M on the same day last week. Success landed at 98.09% and settlement at 99.98%, held back by live issues on FamApp (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 663.3  (▲110.2 d/d, ▲20.1 w/w, ▼132.6 m/m)
- **Success Rate:** 98.09%  (▼0.7 d/d, ▼0.69 w/w, ▼1.04 m/m)
- **Settlement Success:** 99.98%  (▲0.63 d/d, ▲0.5 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.51%  (▼0.01 w/w, ▼0.04 m/m)
- **Business Declines:** 0.4%  (▲0.17 d/d, ▲0.17 w/w, ▲0.16 m/m)
- **Customer Complaints:** 2,609  (▲668 d/d, ▲577 w/w, ▲467 m/m)
- **Merchant Complaints:** 209  (▼5 d/d, ▼11 w/w, ▼25 m/m)
- **Fraud Alerts:** 1,455  (▲358 d/d, ▲352 w/w, ▲295 m/m)
- **Risk Score:** 59  (▲27 d/d, ▲26 w/w, ▲25 m/m)
- **Response Time:** 728 ms  (▼1 d/d, ▼13 w/w, ▼25 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 215.9 | 99.67% |
| HDFC Bank | 70.9 | 99.42% |
| Bank of Baroda | 51.0 | 99.26% |
| Union Bank of India | 44.7 | 99.63% |
| Axis Bank | 40.9 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 316.8 | 99.51% | 198 ms |
| Google Pay | 216.9 | 99.35% | 241 ms |
| Paytm | 52.6 | 99.53% | 201 ms |
| Navi | 24.4 | 99.53% | 304 ms |
| SuperMoney | 12.9 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 245.4 |
| Person to Person | 235.5 |
| QR Payments | 63.0 |
| UPI Lite | 31.8 |
| UPI Autopay | 21.9 |

## Failure analysis
- INC-2026-15 — fraud / risk spike on FamApp (day 1 of 3); see RCA-2026-15.

## Recommendations
Stay on the open incident: keep recovery monitoring on FamApp and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D22-MON) and any meetings/emails on 26 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D22-MON, RPT-D21-DAILY, INC-2026-15, RCA-2026-15
