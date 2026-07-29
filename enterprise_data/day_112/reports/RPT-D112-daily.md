---
id: RPT-D112-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-26T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 26 Apr 2026)

**Report ID:** RPT-D112-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 26 Apr 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 112 of 206)

## Transaction summary
The rail processed 587.8M UPI transactions on Sunday — a quiet Sunday — down 1.8M on the same day last week. Success landed at 99.7% and settlement at 99.98%, held back by live issues on PowerPay Utilities, MetroRide (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 587.8  (▼63.5 d/d, ▼1.8 w/w, ▼208.1 m/m)
- **Success Rate:** 99.7%  (▲1.1 d/d, ▲0.29 w/w, ▲0.57 m/m)
- **Settlement Success:** 99.98%  (▲0.07 d/d, ▲1.2 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.36%  (▼0.01 w/w, ▼0.19 m/m)
- **Business Declines:** 0.19%  (▼0.02 d/d, ▲0.01 w/w, ▼0.05 m/m)
- **Customer Complaints:** 1,281  (▼6 d/d, ▼24 w/w, ▼861 m/m)
- **Merchant Complaints:** 144  (▼16 d/d, ▲6 w/w, ▼90 m/m)
- **Fraud Alerts:** 874  (▼5 d/d, ▼18 w/w, ▼286 m/m)
- **Risk Score:** 24  (▼10 m/m)
- **Response Time:** 619 ms  (▼2 d/d, ▼6 w/w, ▼134 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 191.3 | 99.67% |
| HDFC Bank | 62.8 | 99.42% |
| Bank of Baroda | 45.2 | 99.26% |
| Union Bank of India | 39.7 | 99.63% |
| Axis Bank | 36.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 280.8 | 99.51% | 198 ms |
| Google Pay | 192.2 | 99.35% | 241 ms |
| Paytm | 46.6 | 99.53% | 201 ms |
| Navi | 21.6 | 99.53% | 304 ms |
| SuperMoney | 11.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 217.5 |
| Person to Person | 208.7 |
| QR Payments | 55.8 |
| UPI Lite | 28.2 |
| UPI Autopay | 19.4 |

## Failure analysis
- INC-2026-23 — merchant decline-rate spike on PowerPay Utilities, MetroRide (day 4 of 4); see RCA-2026-23.

## Recommendations
Stay on the open incident: keep recovery monitoring on PowerPay Utilities, MetroRide and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D112-MON) and any meetings/emails on 26 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D112-MON, RPT-D111-DAILY, INC-2026-23, RCA-2026-23
