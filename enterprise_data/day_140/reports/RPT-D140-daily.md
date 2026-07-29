---
id: RPT-D140-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-08T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 08 Nov 2026)

**Report ID:** RPT-D140-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 08 Nov 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 140 of 180)

## Transaction summary
The rail processed 804.1M UPI transactions on Sunday — a quiet Sunday — up 19.1M on the same day last week. Success landed at 99.32% and settlement at 99.04%, held back by live issues on BHIM (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 804.1  (▼86.1 d/d, ▲19.1 w/w, ▲59.2 m/m)
- **Success Rate:** 99.32%  (▼0.33 d/d, ▲0.14 w/w, ▼0.28 m/m)
- **Settlement Success:** 99.04%  (▼0.58 d/d, ▼0.22 w/w, ▼0.39 m/m)
- **Technical Declines:** 0.32%  (▼0.03 d/d, ▲0.05 w/w, ▼0.13 m/m)
- **Business Declines:** 0.14%  (▼0.01 w/w, ▼0.06 m/m)
- **Customer Complaints:** 1,173  (▼107 d/d, ▲136 w/w, ▼769 m/m)
- **Merchant Complaints:** 103  (▼8 w/w, ▼108 m/m)
- **Fraud Alerts:** 742  (▼3 d/d, ▼20 w/w, ▼309 m/m)
- **Risk Score:** 20  (▼1 w/w, ▼11 m/m)
- **Response Time:** 614 ms  (▼28 d/d, ▲36 w/w, ▼128 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 258.5 | 99.5% |
| HDFC Bank | 88.7 | 99.55% |
| Bank of Baroda | 63.8 | 99.64% |
| Union Bank of India | 55.4 | 99.43% |
| ICICI Bank | 49.6 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 383.6 | 99.14% | 231 ms |
| Google Pay | 262.6 | 99.17% | 316 ms |
| Paytm | 64.9 | 99.06% | 192 ms |
| Navi | 29.6 | 99.17% | 225 ms |
| SuperMoney | 15.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 301.5 |
| Person to Person | 285.5 |
| QR Payments | 76.4 |
| UPI Lite | 38.6 |
| UPI Autopay | 26.5 |

## Failure analysis
- INC-2026-25 — PSP callback latency increase on BHIM (day 2 of 5); see RCA-2026-25.

## Recommendations
Stay on the open incident: keep recovery monitoring on BHIM and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D140-MON) and any meetings/emails on 08 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D140-MON, RPT-D139-DAILY, INC-2026-25, RCA-2026-25
