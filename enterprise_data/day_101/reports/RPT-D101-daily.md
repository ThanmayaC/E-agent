---
id: RPT-D101-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-30T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 30 Sep 2026)

**Report ID:** RPT-D101-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 30 Sep 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 101 of 180)

## Transaction summary
The rail processed 1005.4M UPI transactions on Wednesday — the month-end surge as salary and bill-pay flows land — up 104.0M on the same day last week. Success landed at 99.98% and settlement at 98.84%, held back by live issues on State Bank of India (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1005.4  (▼24.3 d/d, ▲104.0 w/w, ▲260.5 m/m)
- **Success Rate:** 99.98%  (▲0.38 m/m)
- **Settlement Success:** 98.84%  (▼1.14 w/w, ▼0.59 m/m)
- **Technical Declines:** 0.31%  (▼0.01 w/w, ▼0.14 m/m)
- **Business Declines:** 0.19%  (▼0.01 d/d, ▲0.03 w/w, ▼0.01 m/m)
- **Customer Complaints:** 1,305  (▼72 d/d, ▲54 w/w, ▼637 m/m)
- **Merchant Complaints:** 187  (▼35 d/d, ▲58 w/w, ▼24 m/m)
- **Fraud Alerts:** 824  (▼2 d/d, ▼7 w/w, ▼227 m/m)
- **Risk Score:** 23  (▼8 m/m)
- **Response Time:** 616 ms  (▲5 d/d, ▼6 w/w, ▼126 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 323.3 | 99.05% |
| HDFC Bank | 110.9 | 99.55% |
| Bank of Baroda | 79.7 | 99.64% |
| Union Bank of India | 69.3 | 99.43% |
| ICICI Bank | 62.0 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 479.7 | 99.14% | 231 ms |
| Google Pay | 328.4 | 99.17% | 316 ms |
| Paytm | 81.1 | 99.06% | 192 ms |
| Navi | 37.1 | 99.17% | 225 ms |
| SuperMoney | 19.6 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 377.0 |
| Person to Person | 356.9 |
| QR Payments | 95.5 |
| UPI Lite | 48.3 |
| UPI Autopay | 33.2 |

## Failure analysis
- INC-2026-12 — merchant settlement delay on State Bank of India (day 2 of 5); see RCA-2026-12.

## Recommendations
Stay on the open incident: keep recovery monitoring on State Bank of India and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D101-MON) and any meetings/emails on 30 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D101-MON, RPT-D100-DAILY, INC-2026-12, RCA-2026-12
