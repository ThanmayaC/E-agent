---
id: RPT-D153-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-21T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 21 Nov 2026)

**Report ID:** RPT-D153-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 21 Nov 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 153 of 180)

## Transaction summary
The rail processed 905.3M UPI transactions on Saturday — a lighter Saturday — up 30.5M on the same day last week. Success landed at 99.3% and settlement at 99.98%, held back by live issues on HDFC MobileBanking (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 905.3  (▼77.7 d/d, ▲30.5 w/w, ▲160.4 m/m)
- **Success Rate:** 99.3%  (▼0.32 d/d, ▼0.68 w/w, ▼0.3 m/m)
- **Settlement Success:** 99.98%  (▲0.28 d/d, ▲0.55 m/m)
- **Technical Declines:** 0.25%  (▼0.01 w/w, ▼0.2 m/m)
- **Business Declines:** 0.17%  (▼0.03 d/d, ▲0.01 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,066  (▼89 d/d, ▲8 w/w, ▼876 m/m)
- **Merchant Complaints:** 96  (▼50 w/w, ▼115 m/m)
- **Fraud Alerts:** 798  (▼74 d/d, ▲70 w/w, ▼253 m/m)
- **Risk Score:** 25  (▼4 d/d, ▲5 w/w, ▼6 m/m)
- **Response Time:** 558 ms  (▼1 d/d, ▼2 w/w, ▼184 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 291.1 | 99.5% |
| HDFC Bank | 99.9 | 99.55% |
| Bank of Baroda | 71.8 | 99.64% |
| Union Bank of India | 62.4 | 99.43% |
| ICICI Bank | 55.8 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 431.9 | 99.14% | 231 ms |
| Google Pay | 295.7 | 99.17% | 316 ms |
| Paytm | 73.0 | 99.06% | 192 ms |
| Navi | 33.4 | 99.17% | 225 ms |
| SuperMoney | 17.6 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 339.5 |
| Person to Person | 321.4 |
| QR Payments | 86.0 |
| UPI Lite | 43.5 |
| UPI Autopay | 29.9 |

## Failure analysis
- INC-2026-06 — fraud / risk spike on HDFC MobileBanking (day 3 of 5); see RCA-2026-06.

## Recommendations
Stay on the open incident: keep recovery monitoring on HDFC MobileBanking and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D153-MON) and any meetings/emails on 21 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D153-MON, RPT-D152-DAILY, INC-2026-06, RCA-2026-06
