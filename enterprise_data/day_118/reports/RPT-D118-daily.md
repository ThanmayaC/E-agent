---
id: RPT-D118-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-17T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 17 Oct 2026)

**Report ID:** RPT-D118-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 17 Oct 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 118 of 180)

## Transaction summary
The rail processed 850.4M UPI transactions on Saturday — a lighter Saturday — up 1.7M on the same day last week. Success landed at 99.98% and settlement at 98.99%, held back by live issues on CRED (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 850.4  (▼85.7 d/d, ▲1.7 w/w, ▲105.5 m/m)
- **Success Rate:** 99.98%  (▲0.73 d/d, ▲0.77 w/w, ▲0.38 m/m)
- **Settlement Success:** 98.99%  (▼0.84 d/d, ▼0.31 w/w, ▼0.44 m/m)
- **Technical Declines:** 0.35%  (▼0.04 d/d, ▲0.05 w/w, ▼0.1 m/m)
- **Business Declines:** 0.15%  (▼0.05 m/m)
- **Customer Complaints:** 1,317  (▼142 d/d, ▲162 w/w, ▼625 m/m)
- **Merchant Complaints:** 115  (▲1 d/d, ▼4 w/w, ▼96 m/m)
- **Fraud Alerts:** 779  (▼11 d/d, ▼16 w/w, ▼272 m/m)
- **Risk Score:** 21  (▼2 d/d, ▼1 w/w, ▼10 m/m)
- **Response Time:** 637 ms  (▼38 d/d, ▲37 w/w, ▼105 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 273.4 | 99.5% |
| HDFC Bank | 93.8 | 99.55% |
| Bank of Baroda | 67.4 | 99.64% |
| Union Bank of India | 58.6 | 99.43% |
| ICICI Bank | 52.4 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 405.7 | 99.14% | 231 ms |
| Google Pay | 277.8 | 99.17% | 316 ms |
| Paytm | 68.6 | 99.06% | 192 ms |
| Navi | 31.3 | 99.17% | 225 ms |
| SuperMoney | 16.6 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 318.9 |
| Person to Person | 301.9 |
| QR Payments | 80.8 |
| UPI Lite | 40.8 |
| UPI Autopay | 28.1 |

## Failure analysis
- INC-2026-08 — PSP callback latency increase on CRED (day 2 of 4); see RCA-2026-08.

## Recommendations
Stay on the open incident: keep recovery monitoring on CRED and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D118-MON) and any meetings/emails on 17 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D118-MON, RPT-D117-DAILY, INC-2026-08, RCA-2026-08
