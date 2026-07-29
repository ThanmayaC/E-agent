---
id: RPT-D17-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-08T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 08 Jul 2026)

**Report ID:** RPT-D17-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 08 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 17 of 180)

## Transaction summary
The rail processed 766.7M UPI transactions on Wednesday — a steady mid-week day — down 181.8M on the same day last week. Success landed at 99.98% and settlement at 99.98%, held back by live issues on YONO SBI (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 766.7  (▲6.4 d/d, ▼181.8 w/w, ▲21.8 m/m)
- **Success Rate:** 99.98%  (▲1.5 d/d, ▲1.58 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.51 d/d, ▲0.49 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.43%  (▲0.01 d/d, ▼0.1 w/w, ▼0.02 m/m)
- **Business Declines:** 0.24%  (▼0.04 d/d, ▲0.04 w/w, ▲0.04 m/m)
- **Customer Complaints:** 2,042  (▼160 d/d, ▼154 w/w, ▲100 m/m)
- **Merchant Complaints:** 194  (▼1 d/d, ▼5 w/w, ▼17 m/m)
- **Fraud Alerts:** 1,136  (▼77 d/d, ▲118 w/w, ▲85 m/m)
- **Risk Score:** 38  (▼7 d/d, ▲8 w/w, ▲7 m/m)
- **Response Time:** 719 ms  (▲8 d/d, ▼60 w/w, ▼23 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 246.5 | 99.5% |
| HDFC Bank | 84.6 | 99.55% |
| Bank of Baroda | 60.8 | 99.64% |
| Union Bank of India | 52.8 | 99.43% |
| ICICI Bank | 47.3 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 365.8 | 99.14% | 231 ms |
| Google Pay | 250.4 | 99.17% | 316 ms |
| Paytm | 61.9 | 99.06% | 192 ms |
| Navi | 28.3 | 99.17% | 225 ms |
| SuperMoney | 14.9 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 287.5 |
| Person to Person | 272.2 |
| QR Payments | 72.8 |
| UPI Lite | 36.8 |
| UPI Autopay | 25.3 |

## Failure analysis
- INC-2026-09 — fraud / risk spike on YONO SBI (day 3 of 3); see RCA-2026-09.

## Recommendations
Stay on the open incident: keep recovery monitoring on YONO SBI and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D17-MON) and any meetings/emails on 08 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D17-MON, RPT-D16-DAILY, INC-2026-09, RCA-2026-09
