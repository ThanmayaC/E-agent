---
id: RPT-D131-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-30T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 30 Oct 2026)

**Report ID:** RPT-D131-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 30 Oct 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 131 of 180)

## Transaction summary
The rail processed 1089.9M UPI transactions on Friday — the month-end surge as salary and bill-pay flows land — up 137.3M on the same day last week. Success landed at 98.48% and settlement at 99.64%, held back by live issues on TravelGo, InsureWell, Union Bank of India (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1089.9  (▲1.1 d/d, ▲137.3 w/w, ▲345.0 m/m)
- **Success Rate:** 98.48%  (▼1.17 d/d, ▼1.5 w/w, ▼1.12 m/m)
- **Settlement Success:** 99.64%  (▼0.34 d/d, ▲0.13 w/w, ▲0.21 m/m)
- **Technical Declines:** 0.44%  (▲0.15 d/d, ▲0.16 w/w, ▼0.01 m/m)
- **Business Declines:** 0.16%  (▼0.02 d/d, ▲0.01 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,503  (▲380 d/d, ▲416 w/w, ▼439 m/m)
- **Merchant Complaints:** 201  (▲44 d/d, ▲91 w/w, ▼10 m/m)
- **Fraud Alerts:** 765  (▲5 d/d, ▼5 w/w, ▼286 m/m)
- **Risk Score:** 21  (▼10 m/m)
- **Response Time:** 631 ms  (▲49 d/d, ▲46 w/w, ▼111 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 350.4 | 99.5% |
| HDFC Bank | 120.2 | 99.55% |
| Bank of Baroda | 86.4 | 99.64% |
| Union Bank of India | 75.1 | 98.71% |
| ICICI Bank | 67.2 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 520.0 | 99.14% | 231 ms |
| Google Pay | 356.0 | 99.17% | 316 ms |
| Paytm | 87.9 | 99.06% | 192 ms |
| Navi | 40.2 | 99.17% | 225 ms |
| SuperMoney | 21.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 408.7 |
| Person to Person | 386.9 |
| QR Payments | 103.5 |
| UPI Lite | 52.3 |
| UPI Autopay | 36.0 |

## Failure analysis
- INC-2026-24 — merchant decline-rate spike on TravelGo, InsureWell (day 3 of 5); see RCA-2026-24.
- INC-2026-10 — bank timeout / 5xx spike on Union Bank of India (day 1 of 2); see INC-2026-10.

## Recommendations
Stay on the open incidents: keep recovery monitoring on TravelGo, InsureWell, Union Bank of India and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D131-MON) and any meetings/emails on 30 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D131-MON, RPT-D130-DAILY, INC-2026-24, INC-2026-10, RCA-2026-24
