---
id: RPT-D61-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-21T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 21 Aug 2026)

**Report ID:** RPT-D61-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 21 Aug 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 61 of 180)

## Transaction summary
The rail processed 1033.3M UPI transactions on Friday — a campaign-driven high-volume day — up 37.4M on the same day last week. Success landed at 98.93% and settlement at 99.98%, held back by live issues on Collect Requests (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1033.3  (▲204.4 d/d, ▲37.4 w/w, ▲288.4 m/m)
- **Success Rate:** 98.93%  (▼0.87 d/d, ▼1.05 w/w, ▼0.67 m/m)
- **Settlement Success:** 99.98%  (▲0.99 d/d, ▲0.55 m/m)
- **Technical Declines:** 0.53%  (▲0.17 d/d, ▲0.17 w/w, ▲0.08 m/m)
- **Business Declines:** 0.17%  (▼0.02 d/d, ▼0.03 m/m)
- **Customer Complaints:** 1,898  (▲385 d/d, ▲373 w/w, ▼44 m/m)
- **Merchant Complaints:** 155  (▼30 d/d, ▼5 w/w, ▼56 m/m)
- **Fraud Alerts:** 900  (▼29 w/w, ▼151 m/m)
- **Risk Score:** 26  (▼5 m/m)
- **Response Time:** 698 ms  (▲41 d/d, ▲32 w/w, ▼44 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 332.2 | 99.5% |
| HDFC Bank | 114.0 | 99.55% |
| Bank of Baroda | 81.9 | 99.64% |
| Union Bank of India | 71.2 | 99.43% |
| ICICI Bank | 63.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 493.0 | 99.14% | 231 ms |
| Google Pay | 337.5 | 99.17% | 316 ms |
| Paytm | 83.4 | 99.06% | 192 ms |
| Navi | 38.1 | 99.17% | 225 ms |
| SuperMoney | 20.1 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 387.5 |
| Person to Person | 366.8 |
| QR Payments | 98.2 |
| UPI Lite | 49.6 |
| UPI Autopay | 34.1 |

## Failure analysis
- INC-2026-28 — feature-level degradation on Collect Requests (day 1 of 3); see RCA-2026-28.

## Recommendations
Stay on the open incident: keep recovery monitoring on Collect Requests and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D61-MON) and any meetings/emails on 21 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D61-MON, RPT-D60-DAILY, INC-2026-28, RCA-2026-28
