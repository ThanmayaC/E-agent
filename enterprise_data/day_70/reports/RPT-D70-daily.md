---
id: RPT-D70-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-30T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 30 Aug 2026)

**Report ID:** RPT-D70-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 30 Aug 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 70 of 180)

## Transaction summary
The rail processed 941.2M UPI transactions on Sunday — the month-end surge as salary and bill-pay flows land — up 247.2M on the same day last week. Success landed at 99.92% and settlement at 99.31%, held back by live issues on BHIM (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 941.2  (▼10.9 d/d, ▲247.2 w/w, ▲196.3 m/m)
- **Success Rate:** 99.92%  (▲0.42 d/d, ▲0.54 w/w, ▲0.32 m/m)
- **Settlement Success:** 99.31%  (▲0.21 d/d, ▲0.46 w/w, ▼0.12 m/m)
- **Technical Declines:** 0.46%  (▲0.11 d/d, ▲0.05 w/w, ▲0.01 m/m)
- **Business Declines:** 0.17%  (▼0.03 m/m)
- **Customer Complaints:** 1,779  (▲368 d/d, ▲162 w/w, ▼163 m/m)
- **Merchant Complaints:** 147  (▼1 d/d, ▼6 w/w, ▼64 m/m)
- **Fraud Alerts:** 886  (▲7 d/d, ▼22 w/w, ▼165 m/m)
- **Risk Score:** 25  (▼1 w/w, ▼6 m/m)
- **Response Time:** 733 ms  (▲88 d/d, ▲60 w/w, ▼9 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 302.6 | 99.5% |
| HDFC Bank | 103.8 | 99.55% |
| Bank of Baroda | 74.6 | 99.64% |
| Union Bank of India | 64.8 | 99.43% |
| ICICI Bank | 58.0 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 449.0 | 99.14% | 231 ms |
| Google Pay | 307.4 | 99.17% | 316 ms |
| Paytm | 75.9 | 99.06% | 192 ms |
| Navi | 34.7 | 99.17% | 225 ms |
| SuperMoney | 18.3 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 353.0 |
| Person to Person | 334.1 |
| QR Payments | 89.4 |
| UPI Lite | 45.2 |
| UPI Autopay | 31.1 |

## Failure analysis
- INC-2026-23 — PSP callback latency increase on BHIM (day 1 of 2); see INC-2026-23.

## Recommendations
Stay on the open incident: keep recovery monitoring on BHIM and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D70-MON) and any meetings/emails on 30 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D70-MON, RPT-D69-DAILY, INC-2026-23
