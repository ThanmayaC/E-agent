---
id: RPT-D117-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-01T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 01 May 2026)

**Report ID:** RPT-D117-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 01 May 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 117 of 206)

## Transaction summary
The rail processed 727.9M UPI transactions on Friday — a steady mid-week day — up 24.1M on the same day last week. Success landed at 99.98% and settlement at 98.68%, held back by live issues on Union Bank of India (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 727.9  (▼59.0 d/d, ▲24.1 w/w, ▼68.0 m/m)
- **Success Rate:** 99.98%  (▲0.28 d/d, ▲0.85 m/m)
- **Settlement Success:** 98.68%  (▼1.3 d/d, ▼0.63 w/w, ▼1.27 m/m)
- **Technical Declines:** 0.36%  (▲0.01 d/d, ▼0.19 m/m)
- **Business Declines:** 0.27%  (▲0.09 d/d, ▲0.04 w/w, ▲0.03 m/m)
- **Customer Complaints:** 1,478  (▲225 d/d, ▲191 w/w, ▼664 m/m)
- **Merchant Complaints:** 294  (▲164 d/d, ▲110 w/w, ▲60 m/m)
- **Fraud Alerts:** 862  (▲1 d/d, ▼18 w/w, ▼298 m/m)
- **Risk Score:** 23  (▼1 d/d, ▼1 w/w, ▼11 m/m)
- **Response Time:** 611 ms  (▼5 d/d, ▼9 w/w, ▼142 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 236.9 | 99.67% |
| HDFC Bank | 77.8 | 99.42% |
| Bank of Baroda | 56.0 | 99.26% |
| Union Bank of India | 49.1 | 97.43% |
| Axis Bank | 44.9 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 347.7 | 99.51% | 198 ms |
| Google Pay | 238.0 | 99.35% | 241 ms |
| Paytm | 57.7 | 99.53% | 201 ms |
| Navi | 26.8 | 99.53% | 304 ms |
| SuperMoney | 14.2 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 269.3 |
| Person to Person | 258.4 |
| QR Payments | 69.2 |
| UPI Lite | 34.9 |
| UPI Autopay | 24.0 |

## Failure analysis
- INC-2026-05 — merchant settlement delay on Union Bank of India (day 1 of 3); see RCA-2026-05.

## Recommendations
Stay on the open incident: keep recovery monitoring on Union Bank of India and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D117-MON) and any meetings/emails on 01 May.

Refs: upi_kpis_month.xlsx, TEAMS-D117-MON, RPT-D116-DAILY, INC-2026-05, RCA-2026-05
