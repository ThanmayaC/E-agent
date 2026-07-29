---
id: RPT-D60-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-20T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 20 Aug 2026)

**Report ID:** RPT-D60-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 20 Aug 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 60 of 180)

## Transaction summary
The rail processed 828.9M UPI transactions on Thursday — a steady mid-week day — down 2.6M on the same day last week. Success landed at 99.8% and settlement at 98.99%, held back by live issues on ICICI Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 828.9  (▼8.7 d/d, ▼2.6 w/w, ▲84.0 m/m)
- **Success Rate:** 99.8%  (▲1.0 d/d, ▲0.46 w/w, ▲0.2 m/m)
- **Settlement Success:** 98.99%  (▼0.36 d/d, ▼0.02 w/w, ▼0.44 m/m)
- **Technical Declines:** 0.36%  (▼0.01 w/w, ▼0.09 m/m)
- **Business Declines:** 0.19%  (▼0.01 d/d, ▲0.02 w/w, ▼0.01 m/m)
- **Customer Complaints:** 1,513  (▼85 d/d, ▼6 w/w, ▼429 m/m)
- **Merchant Complaints:** 185  (▼41 d/d, ▲25 w/w, ▼26 m/m)
- **Fraud Alerts:** 900  (▼11 d/d, ▼15 w/w, ▼151 m/m)
- **Risk Score:** 26  (▼5 m/m)
- **Response Time:** 657 ms  (▼2 d/d, ▼15 w/w, ▼85 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 266.5 | 99.5% |
| HDFC Bank | 91.4 | 99.55% |
| Bank of Baroda | 65.7 | 99.64% |
| Union Bank of India | 57.1 | 99.43% |
| ICICI Bank | 51.1 | 99.05% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 395.5 | 99.14% | 231 ms |
| Google Pay | 270.7 | 99.17% | 316 ms |
| Paytm | 66.9 | 99.06% | 192 ms |
| Navi | 30.5 | 99.17% | 225 ms |
| SuperMoney | 16.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 310.8 |
| Person to Person | 294.3 |
| QR Payments | 78.7 |
| UPI Lite | 39.8 |
| UPI Autopay | 27.4 |

## Failure analysis
- INC-2026-03 — merchant settlement delay on ICICI Bank (day 4 of 4); see RCA-2026-03.

## Recommendations
Stay on the open incident: keep recovery monitoring on ICICI Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D60-MON) and any meetings/emails on 20 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D60-MON, RPT-D59-DAILY, INC-2026-03, RCA-2026-03
