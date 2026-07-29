---
id: RPT-D142-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-10T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 10 Nov 2026)

**Report ID:** RPT-D142-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 10 Nov 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 142 of 180)

## Transaction summary
The rail processed 994.1M UPI transactions on Tuesday — a steady mid-week day — up 9.1M on the same day last week. Success landed at 99.0% and settlement at 99.98%, held back by live issues on BHIM (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 994.1  (▲43.7 d/d, ▲9.1 w/w, ▲249.2 m/m)
- **Success Rate:** 99.0%  (▼0.76 d/d, ▼0.21 w/w, ▼0.6 m/m)
- **Settlement Success:** 99.98%  (▲0.55 m/m)
- **Technical Declines:** 0.28%  (▼0.01 d/d, ▲0.01 w/w, ▼0.17 m/m)
- **Business Declines:** 0.14%  (▼0.05 w/w, ▼0.06 m/m)
- **Customer Complaints:** 1,047  (▼50 d/d, ▼123 w/w, ▼895 m/m)
- **Merchant Complaints:** 101  (▼1 d/d, ▼86 w/w, ▼110 m/m)
- **Fraud Alerts:** 743  (▲2 d/d, ▼16 w/w, ▼308 m/m)
- **Risk Score:** 20  (▼11 m/m)
- **Response Time:** 577 ms  (▼12 d/d, ▲1 w/w, ▼165 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 319.6 | 99.5% |
| HDFC Bank | 109.7 | 99.55% |
| Bank of Baroda | 78.8 | 99.64% |
| Union Bank of India | 68.5 | 99.43% |
| ICICI Bank | 61.3 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 474.3 | 99.14% | 231 ms |
| Google Pay | 324.7 | 99.17% | 316 ms |
| Paytm | 80.2 | 99.06% | 192 ms |
| Navi | 36.6 | 99.17% | 225 ms |
| SuperMoney | 19.4 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 372.8 |
| Person to Person | 352.9 |
| QR Payments | 94.4 |
| UPI Lite | 47.7 |
| UPI Autopay | 32.8 |

## Failure analysis
- INC-2026-25 — PSP callback latency increase on BHIM (day 4 of 5); see RCA-2026-25.

## Recommendations
Stay on the open incident: keep recovery monitoring on BHIM and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D142-MON) and any meetings/emails on 10 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D142-MON, RPT-D141-DAILY, INC-2026-25, RCA-2026-25
