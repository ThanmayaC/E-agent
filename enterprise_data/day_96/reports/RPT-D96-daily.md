---
id: RPT-D96-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-25T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 25 Sep 2026)

**Report ID:** RPT-D96-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 25 Sep 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 96 of 180)

## Transaction summary
The rail processed 890.0M UPI transactions on Friday — a steady mid-week day — down 17.5M on the same day last week. Success landed at 98.83% and settlement at 99.92%, held back by live issues on iMobile Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 890.0  (▼17.6 d/d, ▼17.5 w/w, ▲145.1 m/m)
- **Success Rate:** 98.83%  (▼0.88 d/d, ▼0.09 w/w, ▼0.77 m/m)
- **Settlement Success:** 99.92%  (▲0.96 d/d, ▲0.92 w/w, ▲0.49 m/m)
- **Technical Declines:** 0.31%  (▼0.01 d/d, ▼0.02 w/w, ▼0.14 m/m)
- **Business Declines:** 0.23%  (▼0.05 d/d, ▲0.07 w/w, ▲0.03 m/m)
- **Customer Complaints:** 1,509  (▼184 d/d, ▲200 w/w, ▼433 m/m)
- **Merchant Complaints:** 129  (▼1 d/d, ▼4 w/w, ▼82 m/m)
- **Fraud Alerts:** 998  (▼105 d/d, ▲147 w/w, ▼53 m/m)
- **Risk Score:** 35  (▼8 d/d, ▲11 w/w, ▲4 m/m)
- **Response Time:** 612 ms  (▼7 d/d, ▼16 w/w, ▼130 m/m)

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
| PhonePe | 424.6 | 99.14% | 231 ms |
| Google Pay | 290.7 | 99.17% | 316 ms |
| Paytm | 71.8 | 99.06% | 192 ms |
| Navi | 32.8 | 99.17% | 225 ms |
| SuperMoney | 17.3 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 333.8 |
| Person to Person | 315.9 |
| QR Payments | 84.5 |
| UPI Lite | 42.7 |
| UPI Autopay | 29.4 |

## Failure analysis
- INC-2026-04 — fraud / risk spike on iMobile Pay (day 2 of 5); see RCA-2026-04.

## Recommendations
Stay on the open incident: keep recovery monitoring on iMobile Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D96-MON) and any meetings/emails on 25 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D96-MON, RPT-D95-DAILY, INC-2026-04, RCA-2026-04
