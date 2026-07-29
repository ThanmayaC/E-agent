---
id: RPT-D88-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-17T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 17 Sep 2026)

**Report ID:** RPT-D88-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 17 Sep 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 88 of 180)

## Transaction summary
The rail processed 909.3M UPI transactions on Thursday — a steady mid-week day — up 38.0M on the same day last week. Success landed at 99.98% and settlement at 99.74%, held back by live issues on Axis Mobile (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 909.3  (▲14.0 d/d, ▲38.0 w/w, ▲164.4 m/m)
- **Success Rate:** 99.98%  (▲0.64 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.74%  (▲0.22 d/d, ▲0.85 w/w, ▲0.31 m/m)
- **Technical Declines:** 0.34%  (▼0.02 d/d, ▲0.01 w/w, ▼0.11 m/m)
- **Business Declines:** 0.16%  (▼0.04 m/m)
- **Customer Complaints:** 1,359  (▼61 d/d, ▲25 w/w, ▼583 m/m)
- **Merchant Complaints:** 133  (▼1 d/d, ▼5 w/w, ▼78 m/m)
- **Fraud Alerts:** 845  (▼11 w/w, ▼206 m/m)
- **Risk Score:** 24  (▼7 m/m)
- **Response Time:** 638 ms  (▼15 d/d, ▼104 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 292.4 | 99.5% |
| HDFC Bank | 100.3 | 99.55% |
| Bank of Baroda | 72.1 | 99.64% |
| Union Bank of India | 62.6 | 99.43% |
| ICICI Bank | 56.1 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 433.8 | 99.14% | 231 ms |
| Google Pay | 297.0 | 99.17% | 316 ms |
| Paytm | 73.4 | 99.06% | 192 ms |
| Navi | 33.5 | 99.17% | 225 ms |
| SuperMoney | 17.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 341.0 |
| Person to Person | 322.8 |
| QR Payments | 86.4 |
| UPI Lite | 43.6 |
| UPI Autopay | 30.0 |

## Failure analysis
- INC-2026-14 — PSP callback latency increase on Axis Mobile (day 4 of 5); see RCA-2026-14.

## Recommendations
Stay on the open incident: keep recovery monitoring on Axis Mobile and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D88-MON) and any meetings/emails on 17 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D88-MON, RPT-D87-DAILY, INC-2026-14, RCA-2026-14
