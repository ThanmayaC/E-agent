---
id: RPT-D35-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-26T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 26 Jul 2026)

**Report ID:** RPT-D35-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 26 Jul 2026  ·  **Day archetype:** Sunday (quiet) · maintenance window
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 35 of 180)

## Transaction summary
The rail processed 662.9M UPI transactions on Sunday — a quiet Sunday with a scheduled maintenance window — up 11.3M on the same day last week. Success landed at 98.52% and settlement at 99.26%, held back by live issues on Amazon Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 662.9  (▼54.4 d/d, ▲11.3 w/w, ▼82.0 m/m)
- **Success Rate:** 98.52%  (▼0.65 d/d, ▼0.52 w/w, ▼1.08 m/m)
- **Settlement Success:** 99.26%  (▲0.3 d/d, ▲0.28 w/w, ▼0.17 m/m)
- **Technical Declines:** 0.48%  (▼0.04 d/d, ▼0.06 w/w, ▲0.03 m/m)
- **Business Declines:** 0.18%  (▼0.01 w/w, ▼0.02 m/m)
- **Customer Complaints:** 1,932  (▼177 d/d, ▼241 w/w, ▼10 m/m)
- **Merchant Complaints:** 176  (▼2 d/d, ▼5 w/w, ▼35 m/m)
- **Fraud Alerts:** 959  (▼17 d/d, ▼19 w/w, ▼92 m/m)
- **Risk Score:** 28  (▼1 w/w, ▼3 m/m)
- **Response Time:** 752 ms  (▼30 d/d, ▼36 w/w, ▲10 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 213.1 | 99.5% |
| HDFC Bank | 73.1 | 99.55% |
| Bank of Baroda | 52.6 | 99.64% |
| Union Bank of India | 45.7 | 99.43% |
| ICICI Bank | 40.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 316.3 | 99.14% | 231 ms |
| Google Pay | 216.5 | 99.17% | 316 ms |
| Paytm | 53.5 | 99.06% | 192 ms |
| Navi | 24.4 | 99.17% | 225 ms |
| SuperMoney | 12.9 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 248.6 |
| Person to Person | 235.3 |
| QR Payments | 63.0 |
| UPI Lite | 31.8 |
| UPI Autopay | 21.9 |

## Failure analysis
- INC-2026-27 — PSP callback latency increase on Amazon Pay (day 2 of 5); see RCA-2026-27.

## Recommendations
Stay on the open incident: keep recovery monitoring on Amazon Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D35-MON) and any meetings/emails on 26 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D35-MON, RPT-D34-DAILY, INC-2026-27, RCA-2026-27
