---
id: RPT-D89-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-18T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 18 Sep 2026)

**Report ID:** RPT-D89-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 18 Sep 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 89 of 180)

## Transaction summary
The rail processed 907.5M UPI transactions on Friday — a steady mid-week day — down 169.1M on the same day last week. Success landed at 98.92% and settlement at 99.0%, held back by live issues on Axis Mobile (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 907.5  (▼1.8 d/d, ▼169.1 w/w, ▲162.6 m/m)
- **Success Rate:** 98.92%  (▼1.06 d/d, ▼0.24 w/w, ▼0.68 m/m)
- **Settlement Success:** 99.0%  (▼0.74 d/d, ▼0.11 w/w, ▼0.43 m/m)
- **Technical Declines:** 0.33%  (▼0.01 d/d, ▼0.12 m/m)
- **Business Declines:** 0.16%  (▼0.04 m/m)
- **Customer Complaints:** 1,309  (▼50 d/d, ▼22 w/w, ▼633 m/m)
- **Merchant Complaints:** 133  (▼6 w/w, ▼78 m/m)
- **Fraud Alerts:** 851  (▲6 d/d, ▼9 w/w, ▼200 m/m)
- **Risk Score:** 24  (▼7 m/m)
- **Response Time:** 628 ms  (▼10 d/d, ▼4 w/w, ▼114 m/m)

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
| Google Pay | 296.4 | 99.17% | 316 ms |
| Paytm | 73.2 | 99.06% | 192 ms |
| Navi | 33.4 | 99.17% | 225 ms |
| SuperMoney | 17.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 340.3 |
| Person to Person | 322.2 |
| QR Payments | 86.2 |
| UPI Lite | 43.6 |
| UPI Autopay | 29.9 |

## Failure analysis
- INC-2026-14 — PSP callback latency increase on Axis Mobile (day 5 of 5); see RCA-2026-14.

## Recommendations
Stay on the open incident: keep recovery monitoring on Axis Mobile and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D89-MON) and any meetings/emails on 18 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D89-MON, RPT-D88-DAILY, INC-2026-14, RCA-2026-14
