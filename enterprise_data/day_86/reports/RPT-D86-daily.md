---
id: RPT-D86-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-15T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 15 Sep 2026)

**Report ID:** RPT-D86-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 15 Sep 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 86 of 180)

## Transaction summary
The rail processed 907.9M UPI transactions on Tuesday — a steady mid-week day — up 25.7M on the same day last week. Success landed at 98.63% and settlement at 99.98%, held back by live issues on Axis Mobile (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 907.9  (▲65.1 d/d, ▲25.7 w/w, ▲163.0 m/m)
- **Success Rate:** 98.63%  (▼0.39 d/d, ▼1.35 w/w, ▼0.97 m/m)
- **Settlement Success:** 99.98%  (▲0.43 d/d, ▲0.55 m/m)
- **Technical Declines:** 0.39%  (▼0.04 d/d, ▲0.05 w/w, ▼0.06 m/m)
- **Business Declines:** 0.16%  (▼0.04 m/m)
- **Customer Complaints:** 1,533  (▼118 d/d, ▲183 w/w, ▼409 m/m)
- **Merchant Complaints:** 136  (▼4 w/w, ▼75 m/m)
- **Fraud Alerts:** 847  (▼7 d/d, ▼15 w/w, ▼204 m/m)
- **Risk Score:** 24  (▼7 m/m)
- **Response Time:** 680 ms  (▼27 d/d, ▲49 w/w, ▼62 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 291.9 | 99.5% |
| HDFC Bank | 100.2 | 99.55% |
| Bank of Baroda | 72.0 | 99.64% |
| Union Bank of India | 62.5 | 99.43% |
| ICICI Bank | 56.0 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 433.1 | 99.14% | 231 ms |
| Google Pay | 296.6 | 99.17% | 316 ms |
| Paytm | 73.2 | 99.06% | 192 ms |
| Navi | 33.5 | 99.17% | 225 ms |
| SuperMoney | 17.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 340.5 |
| Person to Person | 322.3 |
| QR Payments | 86.3 |
| UPI Lite | 43.6 |
| UPI Autopay | 30.0 |

## Failure analysis
- INC-2026-14 — PSP callback latency increase on Axis Mobile (day 2 of 5); see RCA-2026-14.

## Recommendations
Stay on the open incident: keep recovery monitoring on Axis Mobile and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D86-MON) and any meetings/emails on 15 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D86-MON, RPT-D85-DAILY, INC-2026-14, RCA-2026-14
