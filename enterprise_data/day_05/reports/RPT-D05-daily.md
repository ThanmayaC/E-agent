---
id: RPT-D05-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-26T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 26 Jun 2026)

**Report ID:** RPT-D05-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 26 Jun 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 5 of 180)

## Transaction summary
The rail processed 747.3M UPI transactions on Friday — a steady mid-week day — the first day in the window. Success landed at 98.57% and settlement at 99.28%, held back by live issues on Union Bank of India (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 747.3  (▼184.2 d/d, ▲2.4 m/m)
- **Success Rate:** 98.57%  (▼0.78 d/d, ▼1.03 m/m)
- **Settlement Success:** 99.28%  (▲0.22 d/d, ▼0.15 m/m)
- **Technical Declines:** 0.6%  (▼0.14 d/d, ▲0.15 m/m)
- **Business Declines:** 0.2%
- **Customer Complaints:** 2,350  (▼405 d/d, ▲408 m/m)
- **Merchant Complaints:** 285  (▼64 d/d, ▲74 m/m)
- **Fraud Alerts:** 1,040  (▲4 d/d, ▼11 m/m)
- **Risk Score:** 30  (▼1 m/m)
- **Response Time:** 775 ms  (▼26 d/d, ▲33 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 240.3 | 99.5% |
| HDFC Bank | 82.4 | 99.55% |
| Bank of Baroda | 59.3 | 99.64% |
| Union Bank of India | 51.5 | 98.69% |
| ICICI Bank | 46.1 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 356.5 | 99.14% | 231 ms |
| Google Pay | 244.1 | 99.17% | 316 ms |
| Paytm | 60.3 | 99.06% | 192 ms |
| Navi | 27.5 | 99.17% | 225 ms |
| SuperMoney | 14.6 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 280.2 |
| Person to Person | 265.3 |
| QR Payments | 71.0 |
| UPI Lite | 35.9 |
| UPI Autopay | 24.7 |

## Failure analysis
- INC-2026-01 — bank timeout / 5xx spike on Union Bank of India (day 3 of 4); see RCA-2026-01.

## Recommendations
Stay on the open incident: keep recovery monitoring on Union Bank of India and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D05-MON) and any meetings/emails on 26 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D05-MON, RPT-D04-DAILY, INC-2026-01, RCA-2026-01
