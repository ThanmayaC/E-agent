---
id: RPT-D98-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-27T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 27 Sep 2026)

**Report ID:** RPT-D98-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 27 Sep 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 98 of 180)

## Transaction summary
The rail processed 728.2M UPI transactions on Sunday — a quiet Sunday — down 7.7M on the same day last week. Success landed at 99.84% and settlement at 98.88%, held back by live issues on iMobile Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 728.2  (▼88.8 d/d, ▼7.7 w/w, ▼16.7 m/m)
- **Success Rate:** 99.84%  (▼0.14 d/d, ▼0.14 w/w, ▲0.24 m/m)
- **Settlement Success:** 98.88%  (▼0.07 d/d, ▼1.1 w/w, ▼0.55 m/m)
- **Technical Declines:** 0.31%  (▼0.01 w/w, ▼0.14 m/m)
- **Business Declines:** 0.17%  (▼0.03 d/d, ▲0.01 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,309  (▼90 d/d, ▲41 w/w, ▼633 m/m)
- **Merchant Complaints:** 126  (▼2 d/d, ▼5 w/w, ▼85 m/m)
- **Fraud Alerts:** 875  (▼47 d/d, ▲37 w/w, ▼176 m/m)
- **Risk Score:** 26  (▼3 d/d, ▲3 w/w, ▼5 m/m)
- **Response Time:** 613 ms  (▼9 w/w, ▼129 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 234.1 | 99.5% |
| HDFC Bank | 80.3 | 99.55% |
| Bank of Baroda | 57.8 | 99.64% |
| Union Bank of India | 50.2 | 99.43% |
| ICICI Bank | 44.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 347.4 | 99.14% | 231 ms |
| Google Pay | 237.9 | 99.17% | 316 ms |
| Paytm | 58.7 | 99.06% | 192 ms |
| Navi | 26.8 | 99.17% | 225 ms |
| SuperMoney | 14.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 273.1 |
| Person to Person | 258.5 |
| QR Payments | 69.2 |
| UPI Lite | 35.0 |
| UPI Autopay | 24.0 |

## Failure analysis
- INC-2026-04 — fraud / risk spike on iMobile Pay (day 4 of 5); see RCA-2026-04.

## Recommendations
Stay on the open incident: keep recovery monitoring on iMobile Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D98-MON) and any meetings/emails on 27 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D98-MON, RPT-D97-DAILY, INC-2026-04, RCA-2026-04
