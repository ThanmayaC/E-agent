---
id: RPT-D134-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-18T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 18 May 2026)

**Report ID:** RPT-D134-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 18 May 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 134 of 206)

## Transaction summary
The rail processed 693.5M UPI transactions on Monday — the Monday ramp-up after the weekend — up 7.2M on the same day last week. Success held at 98.9% and settlement at 98.97%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 693.5  (▲89.7 d/d, ▲7.2 w/w, ▼102.4 m/m)
- **Success Rate:** 98.9%  (▼1.08 d/d, ▼0.79 w/w, ▼0.23 m/m)
- **Settlement Success:** 98.97%  (▲0.06 w/w, ▼0.98 m/m)
- **Technical Declines:** 0.33%  (▼0.01 w/w, ▼0.22 m/m)
- **Business Declines:** 0.17%  (▼0.01 w/w, ▼0.07 m/m)
- **Customer Complaints:** 1,142  (▼5 d/d, ▼71 w/w, ▼1000 m/m)
- **Merchant Complaints:** 118  (▼1 d/d, ▼19 w/w, ▼116 m/m)
- **Fraud Alerts:** 830  (▲2 d/d, ▼14 w/w, ▼330 m/m)
- **Risk Score:** 22  (▼1 w/w, ▼12 m/m)
- **Response Time:** 597 ms  (▼2 d/d, ▼8 w/w, ▼156 m/m)

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
| Navi | 25.5 | 99.53% | 304 ms |
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
- No incidents open. Technical declines are within the 0.33% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D134-MON) and any meetings/emails on 18 May.

Refs: upi_kpis_month.xlsx, TEAMS-D134-MON, RPT-D133-DAILY
