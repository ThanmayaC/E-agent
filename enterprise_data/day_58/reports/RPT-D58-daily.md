---
id: RPT-D58-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-03T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 03 Mar 2026)

**Report ID:** RPT-D58-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 03 Mar 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 58 of 206)

## Transaction summary
The rail processed 696.6M UPI transactions on Tuesday — a steady mid-week day — down 133.4M on the same day last week. Success held at 99.87% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 696.6  (▲28.7 d/d, ▼133.4 w/w, ▼99.3 m/m)
- **Success Rate:** 99.87%  (▲1.27 d/d, ▲0.58 w/w, ▲0.74 m/m)
- **Settlement Success:** 99.98%  (▲1.26 d/d, ▲0.03 m/m)
- **Technical Declines:** 0.44%  (▼0.01 d/d, ▼0.01 w/w, ▼0.11 m/m)
- **Business Declines:** 0.21%  (▼0.1 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,627  (▼25 d/d, ▼429 w/w, ▼515 m/m)
- **Merchant Complaints:** 176  (▼5 w/w, ▼58 m/m)
- **Fraud Alerts:** 1,005  (▲2 d/d, ▼229 w/w, ▼155 m/m)
- **Risk Score:** 28  (▼16 w/w, ▼6 m/m)
- **Response Time:** 689 ms  (▲7 d/d, ▼7 w/w, ▼64 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 226.7 | 99.67% |
| HDFC Bank | 74.5 | 99.42% |
| Bank of Baroda | 53.6 | 99.26% |
| Union Bank of India | 47.0 | 99.63% |
| Axis Bank | 42.9 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 332.7 | 99.51% | 198 ms |
| Google Pay | 227.8 | 99.35% | 241 ms |
| Paytm | 55.3 | 99.53% | 201 ms |
| Navi | 25.6 | 99.53% | 304 ms |
| SuperMoney | 13.6 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 257.7 |
| Person to Person | 247.3 |
| QR Payments | 66.2 |
| UPI Lite | 33.4 |
| UPI Autopay | 23.0 |

## Failure analysis
- No incidents open. Technical declines are within the 0.44% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D58-MON) and any meetings/emails on 03 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D58-MON, RPT-D57-DAILY
