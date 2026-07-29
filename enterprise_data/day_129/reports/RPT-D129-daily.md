---
id: RPT-D129-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-28T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 28 Oct 2026)

**Report ID:** RPT-D129-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 28 Oct 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 129 of 180)

## Transaction summary
The rail processed 1068.1M UPI transactions on Wednesday — the month-end surge as salary and bill-pay flows land — up 110.2M on the same day last week. Success landed at 98.41% and settlement at 99.89%, held back by live issues on TravelGo, InsureWell, Union Bank of India (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1068.1  (▲81.6 d/d, ▲110.2 w/w, ▲323.2 m/m)
- **Success Rate:** 98.41%  (▼1.57 d/d, ▼1.57 w/w, ▼1.19 m/m)
- **Settlement Success:** 99.89%  (▲0.17 d/d, ▲0.97 w/w, ▲0.46 m/m)
- **Technical Declines:** 0.32%  (▼0.05 d/d, ▲0.04 w/w, ▼0.13 m/m)
- **Business Declines:** 0.21%  (▲0.06 d/d, ▲0.06 w/w, ▲0.01 m/m)
- **Customer Complaints:** 1,185  (▼134 d/d, ▲81 w/w, ▼757 m/m)
- **Merchant Complaints:** 194  (▲43 d/d, ▲82 w/w, ▼17 m/m)
- **Fraud Alerts:** 758  (▼14 d/d, ▼13 w/w, ▼293 m/m)
- **Risk Score:** 21  (▼10 m/m)
- **Response Time:** 598 ms  (▼19 d/d, ▲16 w/w, ▼144 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 343.4 | 99.5% |
| HDFC Bank | 117.8 | 99.55% |
| Bank of Baroda | 84.7 | 99.64% |
| Union Bank of India | 73.6 | 99.08% |
| ICICI Bank | 65.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 509.6 | 99.14% | 231 ms |
| Google Pay | 348.9 | 99.17% | 316 ms |
| Paytm | 86.2 | 99.06% | 192 ms |
| Navi | 39.4 | 99.17% | 225 ms |
| SuperMoney | 20.8 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 400.5 |
| Person to Person | 379.2 |
| QR Payments | 101.5 |
| UPI Lite | 51.3 |
| UPI Autopay | 35.2 |

## Failure analysis
- INC-2026-05 — bank timeout / 5xx spike on Union Bank of India (day 4 of 5); see RCA-2026-05.
- INC-2026-24 — merchant decline-rate spike on TravelGo, InsureWell (day 1 of 5); see RCA-2026-24.

## Recommendations
Stay on the open incidents: keep recovery monitoring on TravelGo, InsureWell, Union Bank of India and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D129-MON) and any meetings/emails on 28 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D129-MON, RPT-D128-DAILY, INC-2026-05, INC-2026-24, RCA-2026-05, RCA-2026-24
