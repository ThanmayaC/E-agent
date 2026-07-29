---
id: RPT-D152-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-20T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 20 Nov 2026)

**Report ID:** RPT-D152-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 20 Nov 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 152 of 180)

## Transaction summary
The rail processed 983.0M UPI transactions on Friday — a steady mid-week day — down 27.1M on the same day last week. Success landed at 99.62% and settlement at 99.7%, held back by live issues on HDFC MobileBanking (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 983.0  (▼10.4 d/d, ▼27.1 w/w, ▲238.1 m/m)
- **Success Rate:** 99.62%  (▼0.3 d/d, ▼0.17 w/w, ▲0.02 m/m)
- **Settlement Success:** 99.7%  (▼0.28 d/d, ▼0.08 w/w, ▲0.27 m/m)
- **Technical Declines:** 0.25%  (▼0.01 w/w, ▼0.2 m/m)
- **Business Declines:** 0.2%  (▼0.04 d/d, ▲0.02 w/w)
- **Customer Complaints:** 1,155  (▼133 d/d, ▲50 w/w, ▼787 m/m)
- **Merchant Complaints:** 96  (▼82 w/w, ▼115 m/m)
- **Fraud Alerts:** 872  (▼97 d/d, ▲144 w/w, ▼179 m/m)
- **Risk Score:** 29  (▼7 d/d, ▲9 w/w, ▼2 m/m)
- **Response Time:** 559 ms  (▼2 d/d, ▲1 w/w, ▼183 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 316.1 | 99.5% |
| HDFC Bank | 108.4 | 99.55% |
| Bank of Baroda | 78.0 | 99.64% |
| Union Bank of India | 67.7 | 99.43% |
| ICICI Bank | 60.6 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 469.0 | 99.14% | 231 ms |
| Google Pay | 321.1 | 99.17% | 316 ms |
| Paytm | 79.3 | 99.06% | 192 ms |
| Navi | 36.2 | 99.17% | 225 ms |
| SuperMoney | 19.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 368.6 |
| Person to Person | 349.0 |
| QR Payments | 93.4 |
| UPI Lite | 47.2 |
| UPI Autopay | 32.4 |

## Failure analysis
- INC-2026-06 — fraud / risk spike on HDFC MobileBanking (day 2 of 5); see RCA-2026-06.

## Recommendations
Stay on the open incident: keep recovery monitoring on HDFC MobileBanking and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D152-MON) and any meetings/emails on 20 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D152-MON, RPT-D151-DAILY, INC-2026-06, RCA-2026-06
