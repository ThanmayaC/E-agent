---
id: RPT-D73-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-18T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 18 Mar 2026)

**Report ID:** RPT-D73-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 18 Mar 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 73 of 206)

## Transaction summary
The rail processed 704.2M UPI transactions on Wednesday — a steady mid-week day — down 123.6M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 704.2  (▲12.8 d/d, ▼123.6 w/w, ▼91.7 m/m)
- **Success Rate:** 99.98%  (▲0.95 d/d, ▲1.39 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.98%  (▲0.6 d/d, ▲0.97 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.42%  (▼0.01 w/w, ▼0.13 m/m)
- **Business Declines:** 0.2%  (▼0.04 m/m)
- **Customer Complaints:** 1,527  (▼14 d/d, ▼45 w/w, ▼615 m/m)
- **Merchant Complaints:** 162  (▼2 d/d, ▼5 w/w, ▼72 m/m)
- **Fraud Alerts:** 971  (▲17 d/d, ▼10 w/w, ▼189 m/m)
- **Risk Score:** 27  (▼1 w/w, ▼7 m/m)
- **Response Time:** 666 ms  (▲5 d/d, ▼12 w/w, ▼87 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 229.2 | 99.67% |
| HDFC Bank | 75.3 | 99.42% |
| Bank of Baroda | 54.2 | 99.26% |
| Union Bank of India | 47.5 | 99.63% |
| Axis Bank | 43.4 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 336.4 | 99.51% | 198 ms |
| Google Pay | 230.3 | 99.35% | 241 ms |
| Paytm | 55.9 | 99.53% | 201 ms |
| Navi | 25.9 | 99.53% | 304 ms |
| SuperMoney | 13.7 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 260.6 |
| Person to Person | 250.0 |
| QR Payments | 66.9 |
| UPI Lite | 33.8 |
| UPI Autopay | 23.2 |

## Failure analysis
- No incidents open. Technical declines are within the 0.42% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D73-MON) and any meetings/emails on 18 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D73-MON, RPT-D72-DAILY
