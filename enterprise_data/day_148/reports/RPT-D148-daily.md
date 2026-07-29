---
id: RPT-D148-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-01T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 01 Jun 2026)

**Report ID:** RPT-D148-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 01 Jun 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 148 of 206)

## Transaction summary
The rail processed 700.1M UPI transactions on Monday — the Monday ramp-up after the weekend — down 4.4M on the same day last week. Success landed at 99.5% and settlement at 99.74%, held back by live issues on BHIM, MetroRide, QuickBite (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 700.1  (▼124.8 d/d, ▼4.4 w/w, ▼95.8 m/m)
- **Success Rate:** 99.5%  (▲0.3 d/d, ▲0.48 w/w, ▲0.37 m/m)
- **Settlement Success:** 99.74%  (▼0.24 d/d, ▲0.39 w/w, ▼0.21 m/m)
- **Technical Declines:** 0.32%  (▼0.01 d/d, ▼0.23 m/m)
- **Business Declines:** 0.21%  (▼0.03 d/d, ▼0.04 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,097  (▼36 d/d, ▼260 w/w, ▼1045 m/m)
- **Merchant Complaints:** 152  (▼26 d/d, ▲38 w/w, ▼82 m/m)
- **Fraud Alerts:** 791  (▼12 d/d, ▼193 w/w, ▼369 m/m)
- **Risk Score:** 21  (▼12 w/w, ▼13 m/m)
- **Response Time:** 590 ms  (▲4 d/d, ▲5 w/w, ▼163 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 227.9 | 99.67% |
| HDFC Bank | 74.9 | 99.42% |
| Bank of Baroda | 53.9 | 99.26% |
| Union Bank of India | 47.2 | 99.63% |
| Axis Bank | 43.1 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 334.4 | 99.51% | 198 ms |
| Google Pay | 229.0 | 99.35% | 241 ms |
| Paytm | 55.5 | 99.53% | 201 ms |
| Navi | 25.7 | 99.53% | 304 ms |
| SuperMoney | 13.7 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 259.0 |
| Person to Person | 248.5 |
| QR Payments | 66.5 |
| UPI Lite | 33.6 |
| UPI Autopay | 23.1 |

## Failure analysis
- INC-2026-14 — PSP callback latency increase on BHIM (day 5 of 5); see RCA-2026-14.
- INC-2026-07 — merchant decline-rate spike on MetroRide, QuickBite (day 2 of 2); see INC-2026-07.

## Recommendations
Stay on the open incidents: keep recovery monitoring on BHIM, MetroRide, QuickBite and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D148-MON) and any meetings/emails on 01 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D148-MON, RPT-D147-DAILY, INC-2026-14, INC-2026-07, RCA-2026-14
