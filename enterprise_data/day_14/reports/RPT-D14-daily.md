---
id: RPT-D14-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-05T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 05 Jul 2026)

**Report ID:** RPT-D14-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 05 Jul 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 14 of 180)

## Transaction summary
The rail processed 620.7M UPI transactions on Sunday — a quiet Sunday — down 228.8M on the same day last week. Success landed at 98.63% and settlement at 99.98%, held back by live issues on Paytm (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 620.7  (▼75.7 d/d, ▼228.8 w/w, ▼124.2 m/m)
- **Success Rate:** 98.63%  (▼0.1 d/d, ▼1.35 w/w, ▼0.97 m/m)
- **Settlement Success:** 99.98%  (▲0.57 d/d, ▲0.55 m/m)
- **Technical Declines:** 0.45%  (▼0.03 d/d, ▲0.01 w/w)
- **Business Declines:** 0.19%  (▼0.01 w/w, ▼0.01 m/m)
- **Customer Complaints:** 1,912  (▼109 d/d, ▲7 w/w, ▼30 m/m)
- **Merchant Complaints:** 198  (▼1 d/d, ▼6 w/w, ▼13 m/m)
- **Fraud Alerts:** 1,018  (▲4 d/d, ▼18 w/w, ▼33 m/m)
- **Risk Score:** 30  (▼1 w/w, ▼1 m/m)
- **Response Time:** 734 ms  (▼25 d/d, ▲4 w/w, ▼8 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 199.6 | 99.5% |
| HDFC Bank | 68.5 | 99.55% |
| Bank of Baroda | 49.2 | 99.64% |
| Union Bank of India | 42.8 | 99.43% |
| ICICI Bank | 38.3 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 296.1 | 99.14% | 231 ms |
| Google Pay | 202.7 | 99.17% | 316 ms |
| Paytm | 50.1 | 98.96% | 208 ms |
| Navi | 22.9 | 99.17% | 225 ms |
| SuperMoney | 12.1 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 232.8 |
| Person to Person | 220.3 |
| QR Payments | 59.0 |
| UPI Lite | 29.8 |
| UPI Autopay | 20.5 |

## Failure analysis
- INC-2026-16 — PSP callback latency increase on Paytm (day 4 of 4); see RCA-2026-16.

## Recommendations
Stay on the open incident: keep recovery monitoring on Paytm and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D14-MON) and any meetings/emails on 05 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D14-MON, RPT-D13-DAILY, INC-2026-16, RCA-2026-16
