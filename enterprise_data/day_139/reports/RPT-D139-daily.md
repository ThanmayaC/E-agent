---
id: RPT-D139-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-07T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 07 Nov 2026)

**Report ID:** RPT-D139-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 07 Nov 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 139 of 180)

## Transaction summary
The rail processed 890.2M UPI transactions on Saturday — a lighter Saturday — down 183.9M on the same day last week. Success landed at 99.65% and settlement at 99.62%, held back by live issues on BHIM (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 890.2  (▼308.4 d/d, ▼183.9 w/w, ▲145.3 m/m)
- **Success Rate:** 99.65%  (▼0.24 d/d, ▼0.33 w/w, ▲0.05 m/m)
- **Settlement Success:** 99.62%  (▼0.36 d/d, ▲0.68 w/w, ▲0.19 m/m)
- **Technical Declines:** 0.35%  (▲0.08 d/d, ▼0.03 w/w, ▼0.1 m/m)
- **Business Declines:** 0.14%  (▼0.01 w/w, ▼0.06 m/m)
- **Customer Complaints:** 1,280  (▲255 d/d, ▼55 w/w, ▼662 m/m)
- **Merchant Complaints:** 103  (▲1 d/d, ▼57 w/w, ▼108 m/m)
- **Fraud Alerts:** 745  (▼2 d/d, ▼15 w/w, ▼306 m/m)
- **Risk Score:** 20  (▼11 m/m)
- **Response Time:** 642 ms  (▲72 d/d, ▲30 w/w, ▼100 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 286.2 | 99.5% |
| HDFC Bank | 98.2 | 99.55% |
| Bank of Baroda | 70.6 | 99.64% |
| Union Bank of India | 61.3 | 99.43% |
| ICICI Bank | 54.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 424.7 | 99.14% | 231 ms |
| Google Pay | 290.8 | 99.17% | 316 ms |
| Paytm | 71.8 | 99.06% | 192 ms |
| Navi | 32.8 | 99.17% | 225 ms |
| SuperMoney | 17.3 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 333.8 |
| Person to Person | 316.0 |
| QR Payments | 84.6 |
| UPI Lite | 42.7 |
| UPI Autopay | 29.4 |

## Failure analysis
- INC-2026-25 — PSP callback latency increase on BHIM (day 1 of 5); see RCA-2026-25.

## Recommendations
Stay on the open incident: keep recovery monitoring on BHIM and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D139-MON) and any meetings/emails on 07 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D139-MON, RPT-D138-DAILY, INC-2026-25, RCA-2026-25
