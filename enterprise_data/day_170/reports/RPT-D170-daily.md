---
id: RPT-D170-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-23T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 23 Jun 2026)

**Report ID:** RPT-D170-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 23 Jun 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 170 of 206)

## Transaction summary
The rail processed 743.7M UPI transactions on Tuesday — a steady mid-week day — up 22.2M on the same day last week. Success held at 98.95% and settlement at 99.76%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 743.7  (▲11.2 d/d, ▲22.2 w/w, ▼52.2 m/m)
- **Success Rate:** 98.95%  (▼1.03 d/d, ▼0.32 w/w, ▼0.18 m/m)
- **Settlement Success:** 99.76%  (▲0.34 d/d, ▲0.76 w/w, ▼0.19 m/m)
- **Technical Declines:** 0.29%  (▼0.01 w/w, ▼0.26 m/m)
- **Business Declines:** 0.16%  (▼0.08 m/m)
- **Customer Complaints:** 970  (▲2 d/d, ▼29 w/w, ▼1172 m/m)
- **Merchant Complaints:** 98  (▼4 w/w, ▼136 m/m)
- **Fraud Alerts:** 757  (▼6 d/d, ▼5 w/w, ▼403 m/m)
- **Risk Score:** 20  (▼1 w/w, ▼14 m/m)
- **Response Time:** 555 ms  (▼4 d/d, ▼9 w/w, ▼198 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 242.1 | 99.67% |
| HDFC Bank | 79.5 | 99.42% |
| Bank of Baroda | 57.2 | 99.26% |
| Union Bank of India | 50.2 | 99.63% |
| Axis Bank | 45.8 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 355.2 | 99.51% | 198 ms |
| Google Pay | 243.2 | 99.35% | 241 ms |
| Paytm | 59.0 | 99.53% | 201 ms |
| Navi | 27.3 | 99.53% | 304 ms |
| SuperMoney | 14.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 275.2 |
| Person to Person | 264.0 |
| QR Payments | 70.7 |
| UPI Lite | 35.7 |
| UPI Autopay | 24.5 |

## Failure analysis
- No incidents open. Technical declines are within the 0.29% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D170-MON) and any meetings/emails on 23 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D170-MON, RPT-D169-DAILY
