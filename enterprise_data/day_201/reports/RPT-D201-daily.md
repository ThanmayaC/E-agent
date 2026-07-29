---
id: RPT-D201-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-24T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 24 Jul 2026)

**Report ID:** RPT-D201-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 24 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 201 of 206)

## Transaction summary
The rail processed 771.6M UPI transactions on Friday — a steady mid-week day — up 10.5M on the same day last week. Success held at 99.98% and settlement at 99.58%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 771.6  (▲24.5 d/d, ▲10.5 w/w, ▼24.3 m/m)
- **Success Rate:** 99.98%  (▲0.67 d/d, ▲0.06 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.58%  (▲0.04 d/d, ▼0.35 w/w, ▼0.37 m/m)
- **Technical Declines:** 0.26%  (▼0.29 m/m)
- **Business Declines:** 0.15%  (▼0.09 m/m)
- **Customer Complaints:** 840  (▲3 d/d, ▼27 w/w, ▼1302 m/m)
- **Merchant Complaints:** 83  (▼4 w/w, ▼151 m/m)
- **Fraud Alerts:** 699  (▼4 d/d, ▼14 w/w, ▼461 m/m)
- **Risk Score:** 18  (▼1 w/w, ▼16 m/m)
- **Response Time:** 523 ms  (▼2 d/d, ▼13 w/w, ▼230 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 251.2 | 99.67% |
| HDFC Bank | 82.5 | 99.42% |
| Bank of Baroda | 59.4 | 99.26% |
| Union Bank of India | 52.1 | 99.63% |
| Axis Bank | 47.5 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 368.6 | 99.51% | 198 ms |
| Google Pay | 252.3 | 99.35% | 241 ms |
| Paytm | 61.2 | 99.53% | 201 ms |
| Navi | 28.4 | 99.53% | 304 ms |
| SuperMoney | 15.0 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 285.5 |
| Person to Person | 273.9 |
| QR Payments | 73.3 |
| UPI Lite | 37.0 |
| UPI Autopay | 25.5 |

## Failure analysis
- No incidents open. Technical declines are within the 0.26% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D201-MON) and any meetings/emails on 24 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D201-MON, RPT-D200-DAILY
