---
id: RPT-D87-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-16T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 16 Sep 2026)

**Report ID:** RPT-D87-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 16 Sep 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 87 of 180)

## Transaction summary
The rail processed 895.3M UPI transactions on Wednesday — a steady mid-week day — up 28.1M on the same day last week. Success landed at 99.98% and settlement at 99.52%, held back by live issues on Axis Mobile (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 895.3  (▼12.6 d/d, ▲28.1 w/w, ▲150.4 m/m)
- **Success Rate:** 99.98%  (▲1.35 d/d, ▲1.06 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.52%  (▼0.46 d/d, ▼0.46 w/w, ▲0.09 m/m)
- **Technical Declines:** 0.36%  (▼0.03 d/d, ▲0.03 w/w, ▼0.09 m/m)
- **Business Declines:** 0.16%  (▼0.04 m/m)
- **Customer Complaints:** 1,420  (▼113 d/d, ▲90 w/w, ▼522 m/m)
- **Merchant Complaints:** 134  (▼2 d/d, ▼5 w/w, ▼77 m/m)
- **Fraud Alerts:** 845  (▼2 d/d, ▼20 w/w, ▼206 m/m)
- **Risk Score:** 24  (▼7 m/m)
- **Response Time:** 653 ms  (▼27 d/d, ▲21 w/w, ▼89 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 287.9 | 99.5% |
| HDFC Bank | 98.8 | 99.55% |
| Bank of Baroda | 71.0 | 99.64% |
| Union Bank of India | 61.7 | 99.43% |
| ICICI Bank | 55.2 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 427.1 | 99.14% | 231 ms |
| Google Pay | 292.4 | 99.17% | 316 ms |
| Paytm | 72.2 | 99.06% | 192 ms |
| Navi | 33.0 | 99.17% | 225 ms |
| SuperMoney | 17.4 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 335.7 |
| Person to Person | 317.8 |
| QR Payments | 85.1 |
| UPI Lite | 43.0 |
| UPI Autopay | 29.5 |

## Failure analysis
- INC-2026-14 — PSP callback latency increase on Axis Mobile (day 3 of 5); see RCA-2026-14.

## Recommendations
Stay on the open incident: keep recovery monitoring on Axis Mobile and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D87-MON) and any meetings/emails on 16 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D87-MON, RPT-D86-DAILY, INC-2026-14, RCA-2026-14
