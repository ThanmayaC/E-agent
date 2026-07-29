---
id: RPT-D52-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-25T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 25 Feb 2026)

**Report ID:** RPT-D52-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 25 Feb 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 52 of 206)

## Transaction summary
The rail processed 824.9M UPI transactions on Wednesday — a campaign-driven high-volume day — up 141.7M on the same day last week. Success landed at 99.29% and settlement at 99.35%, held back by live issues on Google Pay, Navi (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 824.9  (▼5.1 d/d, ▲141.7 w/w, ▲29.0 m/m)
- **Success Rate:** 99.29%  (▼0.12 w/w, ▲0.16 m/m)
- **Settlement Success:** 99.35%  (▼0.63 d/d, ▼0.54 w/w, ▼0.6 m/m)
- **Technical Declines:** 0.61%  (▲0.16 d/d, ▲0.14 w/w, ▲0.06 m/m)
- **Business Declines:** 0.27%  (▼0.04 d/d, ▲0.05 w/w, ▲0.03 m/m)
- **Customer Complaints:** 2,328  (▲272 d/d, ▲567 w/w, ▲186 m/m)
- **Merchant Complaints:** 181  (▼6 w/w, ▼53 m/m)
- **Fraud Alerts:** 1,126  (▼108 d/d, ▲94 w/w, ▼34 m/m)
- **Risk Score:** 37  (▼7 d/d, ▲8 w/w, ▲3 m/m)
- **Response Time:** 787 ms  (▲91 d/d, ▲87 w/w, ▲34 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 268.5 | 99.67% |
| HDFC Bank | 88.2 | 99.42% |
| Bank of Baroda | 63.5 | 99.26% |
| Union Bank of India | 55.6 | 99.63% |
| Axis Bank | 50.8 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 394.0 | 99.51% | 198 ms |
| Google Pay | 269.8 | 99.01% | 372 ms |
| Paytm | 65.4 | 99.53% | 201 ms |
| Navi | 30.3 | 98.93% | 468 ms |
| SuperMoney | 16.1 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 305.2 |
| Person to Person | 292.8 |
| QR Payments | 78.4 |
| UPI Lite | 39.6 |
| UPI Autopay | 27.2 |

## Failure analysis
- INC-2026-19 — fraud / risk spike on Google Pay (day 3 of 3); see RCA-2026-19.
- INC-2026-22 — PSP callback latency increase on Navi (day 1 of 4); see RCA-2026-22.

## Recommendations
Stay on the open incidents: keep recovery monitoring on Google Pay, Navi and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D52-MON) and any meetings/emails on 25 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D52-MON, RPT-D51-DAILY, INC-2026-19, INC-2026-22, RCA-2026-19, RCA-2026-22
