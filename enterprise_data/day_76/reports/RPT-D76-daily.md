---
id: RPT-D76-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-21T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 21 Mar 2026)

**Report ID:** RPT-D76-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 21 Mar 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 76 of 206)

## Transaction summary
The rail processed 611.6M UPI transactions on Saturday — a lighter Saturday — down 16.2M on the same day last week. Success landed at 98.4% and settlement at 99.64%, held back by live issues on YONO SBI (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 611.6  (▼86.8 d/d, ▼16.2 w/w, ▼184.3 m/m)
- **Success Rate:** 98.4%  (▼1.55 d/d, ▼1.58 w/w, ▼0.73 m/m)
- **Settlement Success:** 99.64%  (▼0.34 d/d, ▲0.01 w/w, ▼0.31 m/m)
- **Technical Declines:** 0.55%  (▲0.14 d/d, ▲0.13 w/w)
- **Business Declines:** 0.2%  (▼0.04 m/m)
- **Customer Complaints:** 1,931  (▲400 d/d, ▲382 w/w, ▼211 m/m)
- **Merchant Complaints:** 158  (▼3 d/d, ▼8 w/w, ▼76 m/m)
- **Fraud Alerts:** 953  (▲5 d/d, ▼25 w/w, ▼207 m/m)
- **Risk Score:** 27  (▼1 w/w, ▼7 m/m)
- **Response Time:** 747 ms  (▲79 d/d, ▲80 w/w, ▼6 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 199.1 | 99.67% |
| HDFC Bank | 65.4 | 99.42% |
| Bank of Baroda | 47.1 | 99.26% |
| Union Bank of India | 41.3 | 99.63% |
| Axis Bank | 37.7 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 292.1 | 99.51% | 198 ms |
| Google Pay | 200.0 | 99.35% | 241 ms |
| Paytm | 48.5 | 99.53% | 201 ms |
| Navi | 22.5 | 99.53% | 304 ms |
| SuperMoney | 11.9 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 226.3 |
| Person to Person | 217.1 |
| QR Payments | 58.1 |
| UPI Lite | 29.4 |
| UPI Autopay | 20.2 |

## Failure analysis
- INC-2026-17 — PSP callback latency increase on YONO SBI (day 1 of 3); see RCA-2026-17.

## Recommendations
Stay on the open incident: keep recovery monitoring on YONO SBI and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D76-MON) and any meetings/emails on 21 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D76-MON, RPT-D75-DAILY, INC-2026-17, RCA-2026-17
