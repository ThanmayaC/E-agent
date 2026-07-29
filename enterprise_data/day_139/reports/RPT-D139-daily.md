---
id: RPT-D139-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-23T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 23 May 2026)

**Report ID:** RPT-D139-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 23 May 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 139 of 206)

## Transaction summary
The rail processed 649.6M UPI transactions on Saturday — a lighter Saturday — up 6.0M on the same day last week. Success landed at 98.9% and settlement at 99.72%, held back by live issues on ICICI Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 649.6  (▼59.2 d/d, ▲6.0 w/w, ▼146.3 m/m)
- **Success Rate:** 98.9%  (▼0.33 d/d, ▼1.08 w/w, ▼0.23 m/m)
- **Settlement Success:** 99.72%  (▼0.17 d/d, ▼0.26 w/w, ▼0.23 m/m)
- **Technical Declines:** 0.32%  (▼0.01 d/d, ▼0.02 w/w, ▼0.23 m/m)
- **Business Declines:** 0.2%  (▼0.02 d/d, ▲0.02 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,209  (▼51 d/d, ▲60 w/w, ▼933 m/m)
- **Merchant Complaints:** 170  (▼36 d/d, ▲46 w/w, ▼64 m/m)
- **Fraud Alerts:** 822  (▼2 w/w, ▼338 m/m)
- **Risk Score:** 22  (▼12 m/m)
- **Response Time:** 591 ms  (▼2 d/d, ▼10 w/w, ▼162 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 211.4 | 99.67% |
| HDFC Bank | 69.5 | 99.42% |
| Bank of Baroda | 50.0 | 99.26% |
| Union Bank of India | 43.8 | 99.63% |
| Axis Bank | 40.0 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 310.3 | 99.51% | 198 ms |
| Google Pay | 212.4 | 99.35% | 241 ms |
| Paytm | 51.5 | 99.53% | 201 ms |
| Navi | 23.9 | 99.53% | 304 ms |
| SuperMoney | 12.7 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 240.4 |
| Person to Person | 230.6 |
| QR Payments | 61.7 |
| UPI Lite | 31.2 |
| UPI Autopay | 21.4 |

## Failure analysis
- INC-2026-25 — merchant settlement delay on ICICI Bank (day 2 of 2); see INC-2026-25.

## Recommendations
Stay on the open incident: keep recovery monitoring on ICICI Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D139-MON) and any meetings/emails on 23 May.

Refs: upi_kpis_month.xlsx, TEAMS-D139-MON, RPT-D138-DAILY, INC-2026-25
