---
id: RPT-D103-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-17T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 17 Apr 2026)

**Report ID:** RPT-D103-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 17 Apr 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 103 of 206)

## Transaction summary
The rail processed 703.2M UPI transactions on Friday — a steady mid-week day — up 0.6M on the same day last week. Success landed at 99.24% and settlement at 99.98%, held back by live issues on Kotak Mahindra Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 703.2  (▲5.3 d/d, ▲0.6 w/w, ▼92.7 m/m)
- **Success Rate:** 99.24%  (▼0.42 d/d, ▲0.22 w/w, ▲0.11 m/m)
- **Settlement Success:** 99.98%  (▲0.94 d/d, ▲0.77 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.37%  (▼0.01 w/w, ▼0.18 m/m)
- **Business Declines:** 0.2%  (▼0.02 d/d, ▲0.01 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,396  (▼44 d/d, ▲36 w/w, ▼746 m/m)
- **Merchant Complaints:** 175  (▼29 d/d, ▲32 w/w, ▼59 m/m)
- **Fraud Alerts:** 888  (▼7 d/d, ▼20 w/w, ▼272 m/m)
- **Risk Score:** 25  (▼9 m/m)
- **Response Time:** 634 ms  (▼5 w/w, ▼119 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 228.9 | 99.67% |
| HDFC Bank | 75.2 | 99.42% |
| Bank of Baroda | 54.1 | 99.26% |
| Union Bank of India | 47.4 | 99.63% |
| Axis Bank | 43.3 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 335.9 | 99.51% | 198 ms |
| Google Pay | 230.0 | 99.35% | 241 ms |
| Paytm | 55.8 | 99.53% | 201 ms |
| Navi | 25.9 | 99.53% | 304 ms |
| SuperMoney | 13.7 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 260.2 |
| Person to Person | 249.6 |
| QR Payments | 66.8 |
| UPI Lite | 33.8 |
| UPI Autopay | 23.2 |

## Failure analysis
- INC-2026-20 — merchant settlement delay on Kotak Mahindra Bank (day 3 of 3); see RCA-2026-20.

## Recommendations
Stay on the open incident: keep recovery monitoring on Kotak Mahindra Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D103-MON) and any meetings/emails on 17 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D103-MON, RPT-D102-DAILY, INC-2026-20, RCA-2026-20
