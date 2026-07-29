---
id: RPT-D12-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-03T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 03 Jul 2026)

**Report ID:** RPT-D12-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 03 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 12 of 180)

## Transaction summary
The rail processed 777.5M UPI transactions on Friday — a steady mid-week day — up 30.2M on the same day last week. Success landed at 99.89% and settlement at 98.74%, held back by live issues on Paytm, YONO SBI (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 777.5  (▲22.5 d/d, ▲30.2 w/w, ▲32.6 m/m)
- **Success Rate:** 99.89%  (▲1.81 d/d, ▲1.32 w/w, ▲0.29 m/m)
- **Settlement Success:** 98.74%  (▲0.09 d/d, ▼0.54 w/w, ▼0.69 m/m)
- **Technical Declines:** 0.54%  (▼0.09 d/d, ▼0.06 w/w, ▲0.09 m/m)
- **Business Declines:** 0.19%  (▼0.01 w/w, ▼0.01 m/m)
- **Customer Complaints:** 2,259  (▼260 d/d, ▼91 w/w, ▲317 m/m)
- **Merchant Complaints:** 198  (▼2 d/d, ▼87 w/w, ▼13 m/m)
- **Fraud Alerts:** 1,023  (▼9 d/d, ▼17 w/w, ▼28 m/m)
- **Risk Score:** 30  (▼1 m/m)
- **Response Time:** 797 ms  (▼57 d/d, ▲22 w/w, ▲55 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 250.0 | 99.5% |
| HDFC Bank | 85.8 | 99.55% |
| Bank of Baroda | 61.7 | 99.64% |
| Union Bank of India | 53.6 | 99.43% |
| ICICI Bank | 47.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 370.9 | 99.14% | 231 ms |
| Google Pay | 254.0 | 99.17% | 316 ms |
| Paytm | 62.7 | 98.69% | 256 ms |
| Navi | 28.7 | 99.17% | 225 ms |
| SuperMoney | 15.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 291.6 |
| Person to Person | 276.0 |
| QR Payments | 73.9 |
| UPI Lite | 37.3 |
| UPI Autopay | 25.7 |

## Failure analysis
- INC-2026-13 — PSP callback latency increase on YONO SBI (day 4 of 4); see RCA-2026-13.
- INC-2026-16 — PSP callback latency increase on Paytm (day 2 of 4); see RCA-2026-16.

## Recommendations
Stay on the open incidents: keep recovery monitoring on Paytm, YONO SBI and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D12-MON) and any meetings/emails on 03 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D12-MON, RPT-D11-DAILY, INC-2026-13, INC-2026-16, RCA-2026-13, RCA-2026-16
