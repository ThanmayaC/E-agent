---
id: RPT-D11-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-02T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 02 Jul 2026)

**Report ID:** RPT-D11-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 02 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 11 of 180)

## Transaction summary
The rail processed 755.0M UPI transactions on Thursday — a steady mid-week day — down 176.5M on the same day last week. Success landed at 98.08% and settlement at 98.65%, held back by live issues on Paytm, YONO SBI (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 755.0  (▼193.5 d/d, ▼176.5 w/w, ▲10.1 m/m)
- **Success Rate:** 98.08%  (▼0.32 d/d, ▼1.27 w/w, ▼1.52 m/m)
- **Settlement Success:** 98.65%  (▼0.84 d/d, ▼0.41 w/w, ▼0.78 m/m)
- **Technical Declines:** 0.63%  (▲0.1 d/d, ▼0.11 w/w, ▲0.18 m/m)
- **Business Declines:** 0.19%  (▼0.01 d/d, ▼0.01 w/w, ▼0.01 m/m)
- **Customer Complaints:** 2,519  (▲323 d/d, ▼236 w/w, ▲577 m/m)
- **Merchant Complaints:** 200  (▲1 d/d, ▼149 w/w, ▼11 m/m)
- **Fraud Alerts:** 1,032  (▲14 d/d, ▼4 w/w, ▼19 m/m)
- **Risk Score:** 30  (▼1 m/m)
- **Response Time:** 854 ms  (▲75 d/d, ▲53 w/w, ▲112 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 242.8 | 99.5% |
| HDFC Bank | 83.3 | 99.55% |
| Bank of Baroda | 59.9 | 99.64% |
| Union Bank of India | 52.0 | 99.43% |
| ICICI Bank | 46.6 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 360.2 | 99.14% | 231 ms |
| Google Pay | 246.6 | 99.17% | 316 ms |
| Paytm | 60.9 | 98.46% | 295 ms |
| Navi | 27.8 | 99.17% | 225 ms |
| SuperMoney | 14.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 283.1 |
| Person to Person | 268.0 |
| QR Payments | 71.7 |
| UPI Lite | 36.2 |
| UPI Autopay | 24.9 |

## Failure analysis
- INC-2026-13 — PSP callback latency increase on YONO SBI (day 3 of 4); see RCA-2026-13.
- INC-2026-16 — PSP callback latency increase on Paytm (day 1 of 4); see RCA-2026-16.

## Recommendations
Stay on the open incidents: keep recovery monitoring on Paytm, YONO SBI and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D11-MON) and any meetings/emails on 02 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D11-MON, RPT-D10-DAILY, INC-2026-13, INC-2026-16, RCA-2026-13, RCA-2026-16
