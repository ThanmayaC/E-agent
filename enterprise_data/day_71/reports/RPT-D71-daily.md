---
id: RPT-D71-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-31T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 31 Aug 2026)

**Report ID:** RPT-D71-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 31 Aug 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 71 of 180)

## Transaction summary
The rail processed 956.8M UPI transactions on Monday — the month-end surge as salary and bill-pay flows land — up 132.6M on the same day last week. Success landed at 99.98% and settlement at 99.98%, held back by live issues on BHIM (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 956.8  (▲15.6 d/d, ▲132.6 w/w, ▲211.9 m/m)
- **Success Rate:** 99.98%  (▲0.06 d/d, ▲1.07 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.67 d/d, ▲0.55 m/m)
- **Technical Declines:** 0.42%  (▼0.04 d/d, ▲0.07 w/w, ▼0.03 m/m)
- **Business Declines:** 0.17%  (▼0.03 m/m)
- **Customer Complaints:** 1,633  (▼146 d/d, ▲198 w/w, ▼309 m/m)
- **Merchant Complaints:** 145  (▼2 d/d, ▼5 w/w, ▼66 m/m)
- **Fraud Alerts:** 883  (▼3 d/d, ▼6 w/w, ▼168 m/m)
- **Risk Score:** 25  (▼6 m/m)
- **Response Time:** 698 ms  (▼35 d/d, ▲43 w/w, ▼44 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 307.6 | 99.5% |
| HDFC Bank | 105.6 | 99.55% |
| Bank of Baroda | 75.9 | 99.64% |
| Union Bank of India | 65.9 | 99.43% |
| ICICI Bank | 59.0 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 456.5 | 99.14% | 231 ms |
| Google Pay | 312.5 | 99.17% | 316 ms |
| Paytm | 77.2 | 99.06% | 192 ms |
| Navi | 35.3 | 99.17% | 225 ms |
| SuperMoney | 18.6 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 358.8 |
| Person to Person | 339.7 |
| QR Payments | 90.9 |
| UPI Lite | 45.9 |
| UPI Autopay | 31.6 |

## Failure analysis
- INC-2026-23 — PSP callback latency increase on BHIM (day 2 of 2); see INC-2026-23.

## Recommendations
Stay on the open incident: keep recovery monitoring on BHIM and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D71-MON) and any meetings/emails on 31 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D71-MON, RPT-D70-DAILY, INC-2026-23
