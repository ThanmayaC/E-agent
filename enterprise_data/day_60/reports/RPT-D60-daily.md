---
id: RPT-D60-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-05T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 05 Mar 2026)

**Report ID:** RPT-D60-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 05 Mar 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 60 of 206)

## Transaction summary
The rail processed 693.5M UPI transactions on Thursday — a steady mid-week day — up 9.3M on the same day last week. Success landed at 98.25% and settlement at 99.98%, held back by live issues on Navi (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 693.5  (▲17.8 d/d, ▲9.3 w/w, ▼102.4 m/m)
- **Success Rate:** 98.25%  (▼1.59 d/d, ▼1.4 w/w, ▼0.88 m/m)
- **Settlement Success:** 99.98%  (▲0.6 d/d, ▲0.76 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.44%  (▼0.11 w/w, ▼0.11 m/m)
- **Business Declines:** 0.31%  (▼0.06 d/d, ▲0.1 w/w, ▲0.07 m/m)
- **Customer Complaints:** 1,967  (▼234 d/d, ▲2 w/w, ▼175 m/m)
- **Merchant Complaints:** 172  (▼2 d/d, ▼9 w/w, ▼62 m/m)
- **Fraud Alerts:** 1,213  (▼112 d/d, ▲197 w/w, ▲53 m/m)
- **Risk Score:** 43  (▼10 d/d, ▲14 w/w, ▲9 m/m)
- **Response Time:** 687 ms  (▼2 d/d, ▼59 w/w, ▼66 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 225.7 | 99.67% |
| HDFC Bank | 74.1 | 99.42% |
| Bank of Baroda | 53.4 | 99.26% |
| Union Bank of India | 46.8 | 99.63% |
| Axis Bank | 42.7 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 331.3 | 99.51% | 198 ms |
| Google Pay | 226.8 | 99.35% | 241 ms |
| Paytm | 55.0 | 99.53% | 201 ms |
| Navi | 25.5 | 98.91% | 605 ms |
| SuperMoney | 13.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 256.6 |
| Person to Person | 246.2 |
| QR Payments | 65.9 |
| UPI Lite | 33.3 |
| UPI Autopay | 22.9 |

## Failure analysis
- INC-2026-03 — fraud / risk spike on Navi (day 2 of 3); see RCA-2026-03.

## Recommendations
Stay on the open incident: keep recovery monitoring on Navi and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D60-MON) and any meetings/emails on 05 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D60-MON, RPT-D59-DAILY, INC-2026-03, RCA-2026-03
