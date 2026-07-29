---
id: RPT-D13-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-04T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 04 Jul 2026)

**Report ID:** RPT-D13-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 04 Jul 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 13 of 180)

## Transaction summary
The rail processed 696.4M UPI transactions on Saturday — a lighter Saturday — up 30.5M on the same day last week. Success landed at 98.73% and settlement at 99.41%, held back by live issues on Paytm (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 696.4  (▼81.1 d/d, ▲30.5 w/w, ▼48.5 m/m)
- **Success Rate:** 98.73%  (▼1.16 d/d, ▼1.25 w/w, ▼0.87 m/m)
- **Settlement Success:** 99.41%  (▲0.67 d/d, ▼0.57 w/w, ▼0.02 m/m)
- **Technical Declines:** 0.48%  (▼0.06 d/d, ▼0.04 w/w, ▲0.03 m/m)
- **Business Declines:** 0.19%  (▼0.01 w/w, ▼0.01 m/m)
- **Customer Complaints:** 2,021  (▼238 d/d, ▼114 w/w, ▲79 m/m)
- **Merchant Complaints:** 199  (▲1 d/d, ▼41 w/w, ▼12 m/m)
- **Fraud Alerts:** 1,014  (▼9 d/d, ▼13 w/w, ▼37 m/m)
- **Risk Score:** 30  (▼1 m/m)
- **Response Time:** 759 ms  (▼38 d/d, ▲9 w/w, ▲17 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 223.9 | 99.5% |
| HDFC Bank | 76.8 | 99.55% |
| Bank of Baroda | 55.2 | 99.64% |
| Union Bank of India | 48.0 | 99.43% |
| ICICI Bank | 42.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 332.2 | 99.14% | 231 ms |
| Google Pay | 227.5 | 99.17% | 316 ms |
| Paytm | 56.2 | 98.86% | 227 ms |
| Navi | 25.7 | 99.17% | 225 ms |
| SuperMoney | 13.6 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 261.1 |
| Person to Person | 247.2 |
| QR Payments | 66.2 |
| UPI Lite | 33.4 |
| UPI Autopay | 23.0 |

## Failure analysis
- INC-2026-16 — PSP callback latency increase on Paytm (day 3 of 4); see RCA-2026-16.

## Recommendations
Stay on the open incident: keep recovery monitoring on Paytm and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D13-MON) and any meetings/emails on 04 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D13-MON, RPT-D12-DAILY, INC-2026-16, RCA-2026-16
