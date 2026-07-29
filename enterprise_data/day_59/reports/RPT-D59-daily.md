---
id: RPT-D59-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-04T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 04 Mar 2026)

**Report ID:** RPT-D59-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 04 Mar 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 59 of 206)

## Transaction summary
The rail processed 675.7M UPI transactions on Wednesday — a steady mid-week day — down 149.2M on the same day last week. Success landed at 99.84% and settlement at 99.38%, held back by live issues on Navi (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 675.7  (▼20.9 d/d, ▼149.2 w/w, ▼120.2 m/m)
- **Success Rate:** 99.84%  (▼0.03 d/d, ▲0.55 w/w, ▲0.71 m/m)
- **Settlement Success:** 99.38%  (▼0.6 d/d, ▲0.03 w/w, ▼0.57 m/m)
- **Technical Declines:** 0.44%  (▼0.17 w/w, ▼0.11 m/m)
- **Business Declines:** 0.37%  (▲0.16 d/d, ▲0.1 w/w, ▲0.13 m/m)
- **Customer Complaints:** 2,201  (▲574 d/d, ▼127 w/w, ▲59 m/m)
- **Merchant Complaints:** 174  (▼2 d/d, ▼7 w/w, ▼60 m/m)
- **Fraud Alerts:** 1,325  (▲320 d/d, ▲199 w/w, ▲165 m/m)
- **Risk Score:** 53  (▲25 d/d, ▲16 w/w, ▲19 m/m)
- **Response Time:** 689 ms  (▼98 w/w, ▼64 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 219.9 | 99.67% |
| HDFC Bank | 72.2 | 99.42% |
| Bank of Baroda | 52.0 | 99.26% |
| Union Bank of India | 45.6 | 99.63% |
| Axis Bank | 41.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 322.8 | 99.51% | 198 ms |
| Google Pay | 221.0 | 99.35% | 241 ms |
| Paytm | 53.6 | 99.53% | 201 ms |
| Navi | 24.8 | 98.53% | 790 ms |
| SuperMoney | 13.2 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 250.0 |
| Person to Person | 239.9 |
| QR Payments | 64.2 |
| UPI Lite | 32.4 |
| UPI Autopay | 22.3 |

## Failure analysis
- INC-2026-03 — fraud / risk spike on Navi (day 1 of 3); see RCA-2026-03.

## Recommendations
Stay on the open incident: keep recovery monitoring on Navi and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D59-MON) and any meetings/emails on 04 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D59-MON, RPT-D58-DAILY, INC-2026-03, RCA-2026-03
