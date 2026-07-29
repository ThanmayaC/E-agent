---
id: RPT-D06-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-27T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 27 Jun 2026)

**Report ID:** RPT-D06-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 27 Jun 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 6 of 180)

## Transaction summary
The rail processed 665.9M UPI transactions on Saturday — a lighter Saturday — the first day in the window. Success landed at 99.98% and settlement at 99.98%, held back by live issues on Union Bank of India (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 665.9  (▼81.4 d/d, ▼79.0 m/m)
- **Success Rate:** 99.98%  (▲1.41 d/d, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.7 d/d, ▲0.55 m/m)
- **Technical Declines:** 0.52%  (▼0.08 d/d, ▲0.07 m/m)
- **Business Declines:** 0.2%
- **Customer Complaints:** 2,135  (▼215 d/d, ▲193 m/m)
- **Merchant Complaints:** 240  (▼45 d/d, ▲29 m/m)
- **Fraud Alerts:** 1,027  (▼13 d/d, ▼24 m/m)
- **Risk Score:** 30  (▼1 m/m)
- **Response Time:** 750 ms  (▼25 d/d, ▲8 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 214.1 | 99.5% |
| HDFC Bank | 73.5 | 99.55% |
| Bank of Baroda | 52.8 | 99.64% |
| Union Bank of India | 45.9 | 99.08% |
| ICICI Bank | 41.1 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 317.7 | 99.14% | 231 ms |
| Google Pay | 217.5 | 99.17% | 316 ms |
| Paytm | 53.7 | 99.06% | 192 ms |
| Navi | 24.5 | 99.17% | 225 ms |
| SuperMoney | 13.0 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 249.7 |
| Person to Person | 236.4 |
| QR Payments | 63.3 |
| UPI Lite | 32.0 |
| UPI Autopay | 22.0 |

## Failure analysis
- INC-2026-01 — bank timeout / 5xx spike on Union Bank of India (day 4 of 4); see RCA-2026-01.

## Recommendations
Stay on the open incident: keep recovery monitoring on Union Bank of India and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D06-MON) and any meetings/emails on 27 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D06-MON, RPT-D05-DAILY, INC-2026-01, RCA-2026-01
