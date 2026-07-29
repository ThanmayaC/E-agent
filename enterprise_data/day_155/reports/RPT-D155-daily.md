---
id: RPT-D155-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-23T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 23 Nov 2026)

**Report ID:** RPT-D155-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 23 Nov 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 155 of 180)

## Transaction summary
The rail processed 988.7M UPI transactions on Monday — the Monday ramp-up after the weekend — up 37.3M on the same day last week. Success landed at 99.9% and settlement at 99.98%, held back by live issues on HDFC MobileBanking (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 988.7  (▲146.6 d/d, ▲37.3 w/w, ▲243.8 m/m)
- **Success Rate:** 99.9%  (▼0.08 d/d, ▲0.4 w/w, ▲0.3 m/m)
- **Settlement Success:** 99.98%  (▲0.89 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.25%  (▼0.01 w/w, ▼0.2 m/m)
- **Business Declines:** 0.14%  (▼0.01 d/d, ▼0.07 w/w, ▼0.06 m/m)
- **Customer Complaints:** 975  (▼26 d/d, ▼226 w/w, ▼967 m/m)
- **Merchant Complaints:** 94  (▼1 d/d, ▼17 w/w, ▼117 m/m)
- **Fraud Alerts:** 732  (▼21 d/d, ▼146 w/w, ▼319 m/m)
- **Risk Score:** 20  (▼2 d/d, ▼10 w/w, ▼11 m/m)
- **Response Time:** 553 ms  (▲2 d/d, ▼9 w/w, ▼189 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 317.9 | 99.5% |
| HDFC Bank | 109.1 | 99.55% |
| Bank of Baroda | 78.4 | 99.64% |
| Union Bank of India | 68.1 | 99.43% |
| ICICI Bank | 61.0 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 471.7 | 99.14% | 231 ms |
| Google Pay | 322.9 | 99.17% | 316 ms |
| Paytm | 79.8 | 99.06% | 192 ms |
| Navi | 36.4 | 99.17% | 225 ms |
| SuperMoney | 19.3 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 370.8 |
| Person to Person | 351.0 |
| QR Payments | 93.9 |
| UPI Lite | 47.5 |
| UPI Autopay | 32.6 |

## Failure analysis
- INC-2026-06 — fraud / risk spike on HDFC MobileBanking (day 5 of 5); see RCA-2026-06.

## Recommendations
Stay on the open incident: keep recovery monitoring on HDFC MobileBanking and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D155-MON) and any meetings/emails on 23 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D155-MON, RPT-D154-DAILY, INC-2026-06, RCA-2026-06
