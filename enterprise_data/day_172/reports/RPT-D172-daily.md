---
id: RPT-D172-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-12-10T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 10 Dec 2026)

**Report ID:** RPT-D172-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 10 Dec 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 172 of 180)

## Transaction summary
The rail processed 1052.7M UPI transactions on Thursday — a steady mid-week day — up 26.2M on the same day last week. Success landed at 99.98% and settlement at 99.55%, held back by live issues on Bank of Baroda (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1052.7  (▲16.4 d/d, ▲26.2 w/w, ▲307.8 m/m)
- **Success Rate:** 99.98%  (▲0.38 m/m)
- **Settlement Success:** 99.55%  (▼0.2 d/d, ▲0.07 w/w, ▲0.12 m/m)
- **Technical Declines:** 0.23%  (▼0.01 d/d, ▼0.01 w/w, ▼0.22 m/m)
- **Business Declines:** 0.15%  (▼0.02 d/d, ▲0.02 w/w, ▼0.05 m/m)
- **Customer Complaints:** 927  (▼59 d/d, ▲30 w/w, ▼1015 m/m)
- **Merchant Complaints:** 129  (▼27 d/d, ▲39 w/w, ▼82 m/m)
- **Fraud Alerts:** 692  (▼2 d/d, ▼10 w/w, ▼359 m/m)
- **Risk Score:** 18  (▼13 m/m)
- **Response Time:** 535 ms  (▲1 d/d, ▼3 w/w, ▼207 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 338.5 | 99.5% |
| HDFC Bank | 116.1 | 99.55% |
| Bank of Baroda | 83.5 | 99.19% |
| Union Bank of India | 72.5 | 99.43% |
| ICICI Bank | 64.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 502.2 | 99.14% | 231 ms |
| Google Pay | 343.8 | 99.17% | 316 ms |
| Paytm | 84.9 | 99.06% | 192 ms |
| Navi | 38.8 | 99.17% | 225 ms |
| SuperMoney | 20.5 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 394.8 |
| Person to Person | 373.7 |
| QR Payments | 100.0 |
| UPI Lite | 50.5 |
| UPI Autopay | 34.7 |

## Failure analysis
- INC-2026-15 — merchant settlement delay on Bank of Baroda (day 2 of 4); see RCA-2026-15.

## Recommendations
Stay on the open incident: keep recovery monitoring on Bank of Baroda and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D172-MON) and any meetings/emails on 10 Dec.

Refs: upi_kpis_month.xlsx, TEAMS-D172-MON, RPT-D171-DAILY, INC-2026-15, RCA-2026-15
