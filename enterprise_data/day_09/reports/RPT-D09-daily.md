---
id: RPT-D09-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-30T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 30 Jun 2026)

**Report ID:** RPT-D09-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 30 Jun 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 9 of 180)

## Transaction summary
The rail processed 850.4M UPI transactions on Tuesday — the month-end surge as salary and bill-pay flows land — up 77.5M on the same day last week. Success landed at 99.72% and settlement at 99.98%, held back by live issues on YONO SBI (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 850.4  (▼11.4 d/d, ▲77.5 w/w, ▲105.5 m/m)
- **Success Rate:** 99.72%  (▼0.26 d/d, ▲0.37 w/w, ▲0.12 m/m)
- **Settlement Success:** 99.98%  (▲0.42 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.58%  (▲0.14 d/d, ▲0.13 w/w, ▲0.13 m/m)
- **Business Declines:** 0.2%
- **Customer Complaints:** 2,390  (▲495 d/d, ▲460 w/w, ▲448 m/m)
- **Merchant Complaints:** 200  (▼4 d/d, ▼7 w/w, ▼11 m/m)
- **Fraud Alerts:** 1,023  (▼2 d/d, ▼29 w/w, ▼28 m/m)
- **Risk Score:** 30  (▼1 w/w, ▼1 m/m)
- **Response Time:** 826 ms  (▲107 d/d, ▲91 w/w, ▲84 m/m)

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
- INC-2026-13 — PSP callback latency increase on YONO SBI (day 1 of 4); see RCA-2026-13.

## Recommendations
Stay on the open incident: keep recovery monitoring on YONO SBI and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D09-MON) and any meetings/emails on 30 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D09-MON, RPT-D08-DAILY, INC-2026-13, RCA-2026-13
