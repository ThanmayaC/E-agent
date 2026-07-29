---
id: RPT-D95-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-24T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 24 Sep 2026)

**Report ID:** RPT-D95-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 24 Sep 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 95 of 180)

## Transaction summary
The rail processed 907.6M UPI transactions on Thursday — a steady mid-week day — down 1.7M on the same day last week. Success landed at 99.71% and settlement at 98.96%, held back by live issues on iMobile Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 907.6  (▲6.2 d/d, ▼1.7 w/w, ▲162.7 m/m)
- **Success Rate:** 99.71%  (▼0.27 d/d, ▼0.27 w/w, ▲0.11 m/m)
- **Settlement Success:** 98.96%  (▼1.02 d/d, ▼0.78 w/w, ▼0.47 m/m)
- **Technical Declines:** 0.32%  (▼0.02 w/w, ▼0.13 m/m)
- **Business Declines:** 0.28%  (▲0.12 d/d, ▲0.12 w/w, ▲0.08 m/m)
- **Customer Complaints:** 1,693  (▲442 d/d, ▲334 w/w, ▼249 m/m)
- **Merchant Complaints:** 130  (▲1 d/d, ▼3 w/w, ▼81 m/m)
- **Fraud Alerts:** 1,103  (▲272 d/d, ▲258 w/w, ▲52 m/m)
- **Risk Score:** 43  (▲20 d/d, ▲19 w/w, ▲12 m/m)
- **Response Time:** 619 ms  (▼3 d/d, ▼19 w/w, ▼123 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 291.8 | 99.5% |
| HDFC Bank | 100.1 | 99.55% |
| Bank of Baroda | 72.0 | 99.64% |
| Union Bank of India | 62.5 | 99.43% |
| ICICI Bank | 56.0 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 433.0 | 99.14% | 231 ms |
| Google Pay | 296.5 | 99.17% | 316 ms |
| Paytm | 73.2 | 99.06% | 192 ms |
| Navi | 33.4 | 99.17% | 225 ms |
| SuperMoney | 17.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 340.4 |
| Person to Person | 322.2 |
| QR Payments | 86.2 |
| UPI Lite | 43.6 |
| UPI Autopay | 30.0 |

## Failure analysis
- INC-2026-04 — fraud / risk spike on iMobile Pay (day 1 of 5); see RCA-2026-04.

## Recommendations
Stay on the open incident: keep recovery monitoring on iMobile Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D95-MON) and any meetings/emails on 24 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D95-MON, RPT-D94-DAILY, INC-2026-04, RCA-2026-04
