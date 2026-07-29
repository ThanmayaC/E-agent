---
id: RPT-D162-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-15T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 15 Jun 2026)

**Report ID:** RPT-D162-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 15 Jun 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 162 of 206)

## Transaction summary
The rail processed 729.2M UPI transactions on Monday — the Monday ramp-up after the weekend — up 29.3M on the same day last week. Success held at 99.28% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 729.2  (▲121.1 d/d, ▲29.3 w/w, ▼66.7 m/m)
- **Success Rate:** 99.28%  (▼0.7 d/d, ▼0.5 w/w, ▲0.15 m/m)
- **Settlement Success:** 99.98%  (▲0.47 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.3%  (▼0.25 m/m)
- **Business Declines:** 0.16%  (▼0.08 m/m)
- **Customer Complaints:** 1,008  (▲7 d/d, ▼28 w/w, ▼1134 m/m)
- **Merchant Complaints:** 102  (▼1 d/d, ▼4 w/w, ▼132 m/m)
- **Fraud Alerts:** 771  (▲3 d/d, ▼9 w/w, ▼389 m/m)
- **Risk Score:** 20  (▼1 d/d, ▼1 w/w, ▼14 m/m)
- **Response Time:** 567 ms  (▼2 d/d, ▼6 w/w, ▼186 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 237.4 | 99.67% |
| HDFC Bank | 78.0 | 99.42% |
| Bank of Baroda | 56.1 | 99.26% |
| Union Bank of India | 49.2 | 99.63% |
| Axis Bank | 44.9 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 348.3 | 99.51% | 198 ms |
| Google Pay | 238.5 | 99.35% | 241 ms |
| Paytm | 57.8 | 99.53% | 201 ms |
| Navi | 26.8 | 99.53% | 304 ms |
| SuperMoney | 14.2 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 269.8 |
| Person to Person | 258.9 |
| QR Payments | 69.3 |
| UPI Lite | 35.0 |
| UPI Autopay | 24.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.3% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D162-MON) and any meetings/emails on 15 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D162-MON, RPT-D161-DAILY
