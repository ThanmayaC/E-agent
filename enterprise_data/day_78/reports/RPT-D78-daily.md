---
id: RPT-D78-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-23T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 23 Mar 2026)

**Report ID:** RPT-D78-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 23 Mar 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 78 of 206)

## Transaction summary
The rail processed 675.9M UPI transactions on Monday — the Monday ramp-up after the weekend — down 4.9M on the same day last week. Success landed at 98.71% and settlement at 99.66%, held back by live issues on BHIM, YONO SBI (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 675.9  (▲119.1 d/d, ▼4.9 w/w, ▼120.0 m/m)
- **Success Rate:** 98.71%  (▼0.92 d/d, ▼0.7 w/w, ▼0.42 m/m)
- **Settlement Success:** 99.66%  (▼0.08 d/d, ▲0.29 w/w, ▼0.29 m/m)
- **Technical Declines:** 0.59%  (▲0.09 d/d, ▲0.17 w/w, ▲0.04 m/m)
- **Business Declines:** 0.2%  (▼0.04 m/m)
- **Customer Complaints:** 2,049  (▲306 d/d, ▲495 w/w, ▼93 m/m)
- **Merchant Complaints:** 158  (▼1 d/d, ▼5 w/w, ▼76 m/m)
- **Fraud Alerts:** 953  (▲3 d/d, ▼9 w/w, ▼207 m/m)
- **Risk Score:** 26  (▼1 d/d, ▼1 w/w, ▼8 m/m)
- **Response Time:** 768 ms  (▲51 d/d, ▲103 w/w, ▲15 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 220.0 | 99.67% |
| HDFC Bank | 72.3 | 99.42% |
| Bank of Baroda | 52.0 | 99.26% |
| Union Bank of India | 45.6 | 99.63% |
| Axis Bank | 41.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 322.8 | 99.51% | 198 ms |
| Google Pay | 221.0 | 99.35% | 241 ms |
| Paytm | 53.6 | 99.53% | 201 ms |
| Navi | 24.9 | 99.53% | 304 ms |
| SuperMoney | 13.2 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 250.1 |
| Person to Person | 239.9 |
| QR Payments | 64.2 |
| UPI Lite | 32.4 |
| UPI Autopay | 22.3 |

## Failure analysis
- INC-2026-17 — PSP callback latency increase on YONO SBI (day 3 of 3); see RCA-2026-17.
- INC-2026-12 — PSP callback latency increase on BHIM (day 1 of 2); see INC-2026-12.

## Recommendations
Stay on the open incidents: keep recovery monitoring on BHIM, YONO SBI and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D78-MON) and any meetings/emails on 23 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D78-MON, RPT-D77-DAILY, INC-2026-17, INC-2026-12, RCA-2026-17
