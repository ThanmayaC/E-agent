---
id: RPT-D99-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-28T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 28 Sep 2026)

**Report ID:** RPT-D99-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 28 Sep 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 99 of 180)

## Transaction summary
The rail processed 1027.6M UPI transactions on Monday — the month-end surge as salary and bill-pay flows land — up 176.3M on the same day last week. Success landed at 99.09% and settlement at 99.98%, held back by live issues on iMobile Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1027.6  (▲299.4 d/d, ▲176.3 w/w, ▲282.7 m/m)
- **Success Rate:** 99.09%  (▼0.75 d/d, ▼0.26 w/w, ▼0.51 m/m)
- **Settlement Success:** 99.98%  (▲1.1 d/d, ▲0.17 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.31%  (▼0.01 w/w, ▼0.14 m/m)
- **Business Declines:** 0.17%  (▲0.01 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,265  (▼44 d/d, ▲3 w/w, ▼677 m/m)
- **Merchant Complaints:** 125  (▼1 d/d, ▼7 w/w, ▼86 m/m)
- **Fraud Alerts:** 849  (▼26 d/d, ▲9 w/w, ▼202 m/m)
- **Risk Score:** 24  (▼2 d/d, ▲1 w/w, ▼7 m/m)
- **Response Time:** 613 ms  (▼10 w/w, ▼129 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 330.4 | 99.5% |
| HDFC Bank | 113.4 | 99.55% |
| Bank of Baroda | 81.5 | 99.64% |
| Union Bank of India | 70.8 | 99.43% |
| ICICI Bank | 63.4 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 490.2 | 99.14% | 231 ms |
| Google Pay | 335.7 | 99.17% | 316 ms |
| Paytm | 82.9 | 99.06% | 192 ms |
| Navi | 37.9 | 99.17% | 225 ms |
| SuperMoney | 20.0 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 385.3 |
| Person to Person | 364.8 |
| QR Payments | 97.6 |
| UPI Lite | 49.3 |
| UPI Autopay | 33.9 |

## Failure analysis
- INC-2026-04 — fraud / risk spike on iMobile Pay (day 5 of 5); see RCA-2026-04.

## Recommendations
Stay on the open incident: keep recovery monitoring on iMobile Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D99-MON) and any meetings/emails on 28 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D99-MON, RPT-D98-DAILY, INC-2026-04, RCA-2026-04
