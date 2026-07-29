---
id: RPT-D29-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-20T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 20 Jul 2026)

**Report ID:** RPT-D29-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 20 Jul 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 29 of 180)

## Transaction summary
The rail processed 974.2M UPI transactions on Monday — a campaign-driven high-volume day — up 208.9M on the same day last week. Success landed at 99.91% and settlement at 99.98%, held back by live issues on CRED (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 974.2  (▲322.6 d/d, ▲208.9 w/w, ▲229.3 m/m)
- **Success Rate:** 99.91%  (▲0.87 d/d, ▲0.9 w/w, ▲0.31 m/m)
- **Settlement Success:** 99.98%  (▲1.0 d/d, ▲1.28 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.49%  (▼0.05 d/d, ▲0.08 w/w, ▲0.04 m/m)
- **Business Declines:** 0.19%  (▼0.01 m/m)
- **Customer Complaints:** 1,985  (▼188 d/d, ▲204 w/w, ▲43 m/m)
- **Merchant Complaints:** 181  (▼6 w/w, ▼30 m/m)
- **Fraud Alerts:** 970  (▼8 d/d, ▼25 w/w, ▼81 m/m)
- **Risk Score:** 29  (▼2 m/m)
- **Response Time:** 759 ms  (▼29 d/d, ▲49 w/w, ▲17 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 313.2 | 99.5% |
| HDFC Bank | 107.5 | 99.55% |
| Bank of Baroda | 77.3 | 99.64% |
| Union Bank of India | 67.1 | 99.43% |
| ICICI Bank | 60.1 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 464.8 | 99.14% | 231 ms |
| Google Pay | 318.2 | 99.17% | 316 ms |
| Paytm | 78.6 | 99.06% | 192 ms |
| Navi | 35.9 | 99.17% | 225 ms |
| SuperMoney | 19.0 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 365.3 |
| Person to Person | 345.8 |
| QR Payments | 92.5 |
| UPI Lite | 46.8 |
| UPI Autopay | 32.1 |

## Failure analysis
- INC-2026-11 — PSP callback latency increase on CRED (day 2 of 2); see INC-2026-11.

## Recommendations
Stay on the open incident: keep recovery monitoring on CRED and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D29-MON) and any meetings/emails on 20 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D29-MON, RPT-D28-DAILY, INC-2026-11
