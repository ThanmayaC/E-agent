---
id: RPT-D43-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-03T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 03 Aug 2026)

**Report ID:** RPT-D43-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 03 Aug 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 43 of 180)

## Transaction summary
The rail processed 775.9M UPI transactions on Monday — the Monday ramp-up after the weekend — down 16.7M on the same day last week. Success landed at 98.73% and settlement at 99.79%, held back by live issues on Yes Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 775.9  (▲103.9 d/d, ▼16.7 w/w, ▲31.0 m/m)
- **Success Rate:** 98.73%  (▼0.97 d/d, ▼1.24 w/w, ▼0.87 m/m)
- **Settlement Success:** 99.79%  (▼0.19 d/d, ▲0.58 w/w, ▲0.36 m/m)
- **Technical Declines:** 0.39%  (▲0.01 d/d, ▼0.05 w/w, ▼0.06 m/m)
- **Business Declines:** 0.23%  (▲0.05 d/d, ▼0.04 w/w, ▲0.03 m/m)
- **Customer Complaints:** 1,796  (▲203 d/d, ▼355 w/w, ▼146 m/m)
- **Merchant Complaints:** 302  (▲131 d/d, ▼103 w/w, ▲91 m/m)
- **Fraud Alerts:** 938  (▼19 d/d, ▼17 w/w, ▼113 m/m)
- **Risk Score:** 27  (▼1 w/w, ▼4 m/m)
- **Response Time:** 676 ms  (▼3 d/d, ▼50 w/w, ▼66 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 249.5 | 99.5% |
| HDFC Bank | 85.6 | 99.55% |
| Bank of Baroda | 61.5 | 99.64% |
| Union Bank of India | 53.5 | 99.43% |
| ICICI Bank | 47.8 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 370.2 | 99.14% | 231 ms |
| Google Pay | 253.4 | 99.17% | 316 ms |
| Paytm | 62.6 | 99.06% | 192 ms |
| Navi | 28.6 | 99.17% | 225 ms |
| SuperMoney | 15.1 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 291.0 |
| Person to Person | 275.4 |
| QR Payments | 73.7 |
| UPI Lite | 37.2 |
| UPI Autopay | 25.6 |

## Failure analysis
- INC-2026-07 — merchant settlement delay on Yes Bank (day 1 of 2); see INC-2026-07.

## Recommendations
Stay on the open incident: keep recovery monitoring on Yes Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D43-MON) and any meetings/emails on 03 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D43-MON, RPT-D42-DAILY, INC-2026-07
