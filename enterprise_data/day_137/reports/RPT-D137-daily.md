---
id: RPT-D137-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-21T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 21 May 2026)

**Report ID:** RPT-D137-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 21 May 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 137 of 206)

## Transaction summary
The rail processed 729.0M UPI transactions on Thursday — a steady mid-week day — up 5.8M on the same day last week. Success held at 99.18% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 729.0  (▼139.0 d/d, ▲5.8 w/w, ▼66.9 m/m)
- **Success Rate:** 99.18%  (▼0.02 w/w, ▲0.05 m/m)
- **Settlement Success:** 99.98%  (▲0.03 m/m)
- **Technical Declines:** 0.33%  (▼0.01 w/w, ▼0.22 m/m)
- **Business Declines:** 0.17%  (▼0.03 w/w, ▼0.07 m/m)
- **Customer Complaints:** 1,127  (▼7 d/d, ▼39 w/w, ▼1015 m/m)
- **Merchant Complaints:** 115  (▼1 d/d, ▼30 w/w, ▼119 m/m)
- **Fraud Alerts:** 821  (▼7 d/d, ▼13 w/w, ▼339 m/m)
- **Risk Score:** 22  (▼1 w/w, ▼12 m/m)
- **Response Time:** 594 ms  (▲6 d/d, ▼1 w/w, ▼159 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 237.3 | 99.67% |
| HDFC Bank | 77.9 | 99.42% |
| Bank of Baroda | 56.1 | 99.26% |
| Union Bank of India | 49.2 | 99.63% |
| Axis Bank | 44.9 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 348.2 | 99.51% | 198 ms |
| Google Pay | 238.4 | 99.35% | 241 ms |
| Paytm | 57.8 | 99.53% | 201 ms |
| Navi | 26.8 | 99.53% | 304 ms |
| SuperMoney | 14.2 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 269.7 |
| Person to Person | 258.8 |
| QR Payments | 69.3 |
| UPI Lite | 35.0 |
| UPI Autopay | 24.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.33% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D137-MON) and any meetings/emails on 21 May.

Refs: upi_kpis_month.xlsx, TEAMS-D137-MON, RPT-D136-DAILY
