---
id: RPT-D54-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-27T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 27 Feb 2026)

**Report ID:** RPT-D54-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 27 Feb 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 54 of 206)

## Transaction summary
The rail processed 821.2M UPI transactions on Friday — a campaign-driven high-volume day — up 132.8M on the same day last week. Success landed at 98.34% and settlement at 98.96%, held back by live issues on Navi (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 821.2  (▲137.0 d/d, ▲132.8 w/w, ▲25.3 m/m)
- **Success Rate:** 98.34%  (▼1.31 d/d, ▼1.2 w/w, ▼0.79 m/m)
- **Settlement Success:** 98.96%  (▼0.26 d/d, ▼0.1 w/w, ▼0.99 m/m)
- **Technical Declines:** 0.5%  (▼0.05 d/d, ▲0.04 w/w, ▼0.05 m/m)
- **Business Declines:** 0.21%  (▼0.03 m/m)
- **Customer Complaints:** 1,810  (▼155 d/d, ▲89 w/w, ▼332 m/m)
- **Merchant Complaints:** 180  (▼1 d/d, ▼7 w/w, ▼54 m/m)
- **Fraud Alerts:** 1,002  (▼14 d/d, ▼26 w/w, ▼158 m/m)
- **Risk Score:** 29  (▼5 m/m)
- **Response Time:** 716 ms  (▼30 d/d, ▲20 w/w, ▼37 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 267.3 | 99.67% |
| HDFC Bank | 87.8 | 99.42% |
| Bank of Baroda | 63.2 | 99.26% |
| Union Bank of India | 55.4 | 99.63% |
| Axis Bank | 50.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 392.3 | 99.51% | 198 ms |
| Google Pay | 268.6 | 99.35% | 241 ms |
| Paytm | 65.1 | 99.53% | 201 ms |
| Navi | 30.2 | 99.32% | 359 ms |
| SuperMoney | 16.0 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 303.8 |
| Person to Person | 291.5 |
| QR Payments | 78.0 |
| UPI Lite | 39.4 |
| UPI Autopay | 27.1 |

## Failure analysis
- INC-2026-22 — PSP callback latency increase on Navi (day 3 of 4); see RCA-2026-22.

## Recommendations
Stay on the open incident: keep recovery monitoring on Navi and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D54-MON) and any meetings/emails on 27 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D54-MON, RPT-D53-DAILY, INC-2026-22, RCA-2026-22
