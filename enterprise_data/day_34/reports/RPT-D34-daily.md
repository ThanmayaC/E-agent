---
id: RPT-D34-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-25T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 25 Jul 2026)

**Report ID:** RPT-D34-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 25 Jul 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 34 of 180)

## Transaction summary
The rail processed 717.3M UPI transactions on Saturday — a lighter Saturday — up 0.7M on the same day last week. Success landed at 99.17% and settlement at 98.96%, held back by live issues on Amazon Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 717.3  (▼97.9 d/d, ▲0.7 w/w, ▼27.6 m/m)
- **Success Rate:** 99.17%  (▼0.26 d/d, ▼0.63 w/w, ▼0.43 m/m)
- **Settlement Success:** 98.96%  (▲0.13 d/d, ▼0.1 w/w, ▼0.47 m/m)
- **Technical Declines:** 0.52%  (▲0.12 d/d, ▲0.11 w/w, ▲0.07 m/m)
- **Business Declines:** 0.18%  (▼0.01 w/w, ▼0.02 m/m)
- **Customer Complaints:** 2,109  (▲427 d/d, ▲370 w/w, ▲167 m/m)
- **Merchant Complaints:** 178  (▼4 w/w, ▼33 m/m)
- **Fraud Alerts:** 976  (▲7 d/d, ▼4 w/w, ▼75 m/m)
- **Risk Score:** 28  (▼1 w/w, ▼3 m/m)
- **Response Time:** 782 ms  (▲86 d/d, ▲76 w/w, ▲40 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 230.6 | 99.5% |
| HDFC Bank | 79.1 | 99.55% |
| Bank of Baroda | 56.9 | 99.64% |
| Union Bank of India | 49.4 | 99.43% |
| ICICI Bank | 44.2 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 342.2 | 99.14% | 231 ms |
| Google Pay | 234.3 | 99.17% | 316 ms |
| Paytm | 57.9 | 99.06% | 192 ms |
| Navi | 26.4 | 99.17% | 225 ms |
| SuperMoney | 14.0 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 269.0 |
| Person to Person | 254.6 |
| QR Payments | 68.1 |
| UPI Lite | 34.4 |
| UPI Autopay | 23.7 |

## Failure analysis
- INC-2026-27 — PSP callback latency increase on Amazon Pay (day 1 of 5); see RCA-2026-27.

## Recommendations
Stay on the open incident: keep recovery monitoring on Amazon Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D34-MON) and any meetings/emails on 25 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D34-MON, RPT-D33-DAILY, INC-2026-27, RCA-2026-27
