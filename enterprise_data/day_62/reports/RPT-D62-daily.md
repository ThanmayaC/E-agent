---
id: RPT-D62-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-22T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 22 Aug 2026)

**Report ID:** RPT-D62-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 22 Aug 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 62 of 180)

## Transaction summary
The rail processed 754.5M UPI transactions on Saturday — a lighter Saturday — up 8.9M on the same day last week. Success landed at 99.98% and settlement at 99.98%, held back by live issues on Collect Requests (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 754.5  (▼278.8 d/d, ▲8.9 w/w, ▲9.6 m/m)
- **Success Rate:** 99.98%  (▲1.05 d/d, ▲0.29 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.55 m/m)
- **Technical Declines:** 0.46%  (▼0.07 d/d, ▲0.09 w/w, ▲0.01 m/m)
- **Business Declines:** 0.17%  (▼0.01 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,746  (▼152 d/d, ▲233 w/w, ▼196 m/m)
- **Merchant Complaints:** 153  (▼2 d/d, ▼6 w/w, ▼58 m/m)
- **Fraud Alerts:** 910  (▲10 d/d, ▼7 w/w, ▼141 m/m)
- **Risk Score:** 25  (▼1 d/d, ▼1 w/w, ▼6 m/m)
- **Response Time:** 686 ms  (▼12 d/d, ▲19 w/w, ▼56 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 242.6 | 99.5% |
| HDFC Bank | 83.2 | 99.55% |
| Bank of Baroda | 59.8 | 99.64% |
| Union Bank of India | 52.0 | 99.43% |
| ICICI Bank | 46.5 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 360.0 | 99.14% | 231 ms |
| Google Pay | 246.4 | 99.17% | 316 ms |
| Paytm | 60.9 | 99.06% | 192 ms |
| Navi | 27.8 | 99.17% | 225 ms |
| SuperMoney | 14.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 282.9 |
| Person to Person | 267.8 |
| QR Payments | 71.7 |
| UPI Lite | 36.2 |
| UPI Autopay | 24.9 |

## Failure analysis
- INC-2026-28 — feature-level degradation on Collect Requests (day 2 of 3); see RCA-2026-28.

## Recommendations
Stay on the open incident: keep recovery monitoring on Collect Requests and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D62-MON) and any meetings/emails on 22 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D62-MON, RPT-D61-DAILY, INC-2026-28, RCA-2026-28
