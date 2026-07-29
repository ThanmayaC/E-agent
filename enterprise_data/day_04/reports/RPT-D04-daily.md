---
id: RPT-D04-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-25T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 25 Jun 2026)

**Report ID:** RPT-D04-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 25 Jun 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 4 of 180)

## Transaction summary
The rail processed 931.5M UPI transactions on Thursday — a campaign-driven high-volume day — the first day in the window. Success landed at 99.35% and settlement at 99.06%, held back by live issues on Union Bank of India (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 931.5  (▲164.1 d/d, ▲186.6 m/m)
- **Success Rate:** 99.35%  (▲1.96 d/d, ▼0.25 m/m)
- **Settlement Success:** 99.06%  (▲0.01 d/d, ▼0.37 m/m)
- **Technical Declines:** 0.74%  (▼0.18 d/d, ▲0.29 m/m)
- **Business Declines:** 0.2%
- **Customer Complaints:** 2,755  (▼531 d/d, ▲813 m/m)
- **Merchant Complaints:** 349  (▼85 d/d, ▲138 m/m)
- **Fraud Alerts:** 1,036  (▼15 d/d, ▼15 m/m)
- **Risk Score:** 30  (▼1 d/d, ▼1 m/m)
- **Response Time:** 801 ms  (▼46 d/d, ▲59 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 299.5 | 99.5% |
| HDFC Bank | 102.8 | 99.55% |
| Bank of Baroda | 73.9 | 99.64% |
| Union Bank of India | 64.2 | 98.07% |
| ICICI Bank | 57.4 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 444.4 | 99.14% | 231 ms |
| Google Pay | 304.3 | 99.17% | 316 ms |
| Paytm | 75.1 | 99.06% | 192 ms |
| Navi | 34.3 | 99.17% | 225 ms |
| SuperMoney | 18.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 349.3 |
| Person to Person | 330.7 |
| QR Payments | 88.5 |
| UPI Lite | 44.7 |
| UPI Autopay | 30.7 |

## Failure analysis
- INC-2026-01 — bank timeout / 5xx spike on Union Bank of India (day 2 of 4); see RCA-2026-01.

## Recommendations
Stay on the open incident: keep recovery monitoring on Union Bank of India and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D04-MON) and any meetings/emails on 25 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D04-MON, RPT-D03-DAILY, INC-2026-01, RCA-2026-01
