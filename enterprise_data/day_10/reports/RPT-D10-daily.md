---
id: RPT-D10-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-01T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 01 Jul 2026)

**Report ID:** RPT-D10-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 01 Jul 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 10 of 180)

## Transaction summary
The rail processed 948.5M UPI transactions on Wednesday — a campaign-driven high-volume day — up 181.1M on the same day last week. Success landed at 98.4% and settlement at 99.49%, held back by live issues on YONO SBI (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 948.5  (▲98.1 d/d, ▲181.1 w/w, ▲203.6 m/m)
- **Success Rate:** 98.4%  (▼1.32 d/d, ▲1.01 w/w, ▼1.2 m/m)
- **Settlement Success:** 99.49%  (▼0.49 d/d, ▲0.44 w/w, ▲0.06 m/m)
- **Technical Declines:** 0.53%  (▼0.05 d/d, ▼0.39 w/w, ▲0.08 m/m)
- **Business Declines:** 0.2%
- **Customer Complaints:** 2,196  (▼194 d/d, ▼1090 w/w, ▲254 m/m)
- **Merchant Complaints:** 199  (▼1 d/d, ▼235 w/w, ▼12 m/m)
- **Fraud Alerts:** 1,018  (▼5 d/d, ▼33 w/w, ▼33 m/m)
- **Risk Score:** 30  (▼1 w/w, ▼1 m/m)
- **Response Time:** 779 ms  (▼47 d/d, ▼68 w/w, ▲37 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 305.0 | 99.5% |
| HDFC Bank | 104.6 | 99.55% |
| Bank of Baroda | 75.2 | 99.64% |
| Union Bank of India | 65.3 | 99.43% |
| ICICI Bank | 58.5 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 452.5 | 99.14% | 231 ms |
| Google Pay | 309.8 | 99.17% | 316 ms |
| Paytm | 76.5 | 99.06% | 192 ms |
| Navi | 35.0 | 99.17% | 225 ms |
| SuperMoney | 18.5 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 355.7 |
| Person to Person | 336.7 |
| QR Payments | 90.1 |
| UPI Lite | 45.5 |
| UPI Autopay | 31.3 |

## Failure analysis
- INC-2026-13 — PSP callback latency increase on YONO SBI (day 2 of 4); see RCA-2026-13.

## Recommendations
Stay on the open incident: keep recovery monitoring on YONO SBI and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D10-MON) and any meetings/emails on 01 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D10-MON, RPT-D09-DAILY, INC-2026-13, RCA-2026-13
