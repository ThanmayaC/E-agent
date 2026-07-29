---
id: RPT-D28-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-19T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 19 Jul 2026)

**Report ID:** RPT-D28-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 19 Jul 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 28 of 180)

## Transaction summary
The rail processed 651.6M UPI transactions on Sunday — a quiet Sunday — up 16.7M on the same day last week. Success landed at 99.04% and settlement at 98.98%, held back by live issues on CRED (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 651.6  (▼65.0 d/d, ▲16.7 w/w, ▼93.3 m/m)
- **Success Rate:** 99.04%  (▼0.76 d/d, ▲0.1 w/w, ▼0.56 m/m)
- **Settlement Success:** 98.98%  (▼0.08 d/d, ▼1.0 w/w, ▼0.45 m/m)
- **Technical Declines:** 0.54%  (▲0.13 d/d, ▲0.13 w/w, ▲0.09 m/m)
- **Business Declines:** 0.19%  (▼0.01 m/m)
- **Customer Complaints:** 2,173  (▲434 d/d, ▲382 w/w, ▲231 m/m)
- **Merchant Complaints:** 181  (▼1 d/d, ▼8 w/w, ▼30 m/m)
- **Fraud Alerts:** 978  (▼2 d/d, ▼13 w/w, ▼73 m/m)
- **Risk Score:** 29  (▼2 m/m)
- **Response Time:** 788 ms  (▲82 d/d, ▲74 w/w, ▲46 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 209.5 | 99.5% |
| HDFC Bank | 71.9 | 99.55% |
| Bank of Baroda | 51.7 | 99.64% |
| Union Bank of India | 44.9 | 99.43% |
| ICICI Bank | 40.2 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 310.9 | 99.14% | 231 ms |
| Google Pay | 212.8 | 99.17% | 316 ms |
| Paytm | 52.6 | 99.06% | 192 ms |
| Navi | 24.0 | 99.17% | 225 ms |
| SuperMoney | 12.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 244.4 |
| Person to Person | 231.3 |
| QR Payments | 61.9 |
| UPI Lite | 31.3 |
| UPI Autopay | 21.5 |

## Failure analysis
- INC-2026-11 — PSP callback latency increase on CRED (day 1 of 2); see INC-2026-11.

## Recommendations
Stay on the open incident: keep recovery monitoring on CRED and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D28-MON) and any meetings/emails on 19 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D28-MON, RPT-D27-DAILY, INC-2026-11
