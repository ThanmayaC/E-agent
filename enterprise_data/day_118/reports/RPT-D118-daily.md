---
id: RPT-D118-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-02T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 02 May 2026)

**Report ID:** RPT-D118-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 02 May 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 118 of 206)

## Transaction summary
The rail processed 635.0M UPI transactions on Saturday — a lighter Saturday — down 16.3M on the same day last week. Success landed at 99.98% and settlement at 99.67%, held back by live issues on Union Bank of India (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 635.0  (▼92.9 d/d, ▼16.3 w/w, ▼160.9 m/m)
- **Success Rate:** 99.98%  (▲1.38 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.67%  (▲0.99 d/d, ▼0.24 w/w, ▼0.28 m/m)
- **Technical Declines:** 0.35%  (▼0.01 d/d, ▼0.01 w/w, ▼0.2 m/m)
- **Business Declines:** 0.23%  (▼0.04 d/d, ▲0.02 w/w, ▼0.01 m/m)
- **Customer Complaints:** 1,378  (▼100 d/d, ▲91 w/w, ▼764 m/m)
- **Merchant Complaints:** 232  (▼62 d/d, ▲72 w/w, ▼2 m/m)
- **Fraud Alerts:** 866  (▲4 d/d, ▼13 w/w, ▼294 m/m)
- **Risk Score:** 23  (▼1 w/w, ▼11 m/m)
- **Response Time:** 611 ms  (▼10 w/w, ▼142 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 206.7 | 99.67% |
| HDFC Bank | 67.9 | 99.42% |
| Bank of Baroda | 48.9 | 99.26% |
| Union Bank of India | 42.8 | 98.26% |
| Axis Bank | 39.1 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 303.3 | 99.51% | 198 ms |
| Google Pay | 207.7 | 99.35% | 241 ms |
| Paytm | 50.4 | 99.53% | 201 ms |
| Navi | 23.3 | 99.53% | 304 ms |
| SuperMoney | 12.4 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 234.9 |
| Person to Person | 225.4 |
| QR Payments | 60.3 |
| UPI Lite | 30.5 |
| UPI Autopay | 21.0 |

## Failure analysis
- INC-2026-05 — merchant settlement delay on Union Bank of India (day 2 of 3); see RCA-2026-05.

## Recommendations
Stay on the open incident: keep recovery monitoring on Union Bank of India and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D118-MON) and any meetings/emails on 02 May.

Refs: upi_kpis_month.xlsx, TEAMS-D118-MON, RPT-D117-DAILY, INC-2026-05, RCA-2026-05
