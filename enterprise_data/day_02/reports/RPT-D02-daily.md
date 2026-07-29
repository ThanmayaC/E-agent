---
id: RPT-D02-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-06T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 06 Jan 2026)

**Report ID:** RPT-D02-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 06 Jan 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 2 of 206)

## Transaction summary
The rail processed 651.8M UPI transactions on Tuesday — a steady mid-week day — the first day in the window. Success held at 99.72% and settlement at 99.45%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 651.8  (▼144.1 d/d, ▼144.1 m/m)
- **Success Rate:** 99.72%  (▲0.59 d/d, ▲0.59 m/m)
- **Settlement Success:** 99.45%  (▼0.5 d/d, ▼0.5 m/m)
- **Technical Declines:** 0.55%
- **Business Declines:** 0.24%
- **Customer Complaints:** 2,123  (▼19 d/d, ▼19 m/m)
- **Merchant Complaints:** 235  (▲1 d/d, ▲1 m/m)
- **Fraud Alerts:** 1,149  (▼11 d/d, ▼11 m/m)
- **Risk Score:** 34
- **Response Time:** 763 ms  (▲10 d/d, ▲10 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 212.2 | 99.67% |
| HDFC Bank | 69.7 | 99.42% |
| Bank of Baroda | 50.2 | 99.26% |
| Union Bank of India | 44.0 | 99.63% |
| Axis Bank | 40.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 311.3 | 99.51% | 198 ms |
| Google Pay | 213.2 | 99.35% | 241 ms |
| Paytm | 51.7 | 99.53% | 201 ms |
| Navi | 24.0 | 99.53% | 304 ms |
| SuperMoney | 12.7 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 241.2 |
| Person to Person | 231.4 |
| QR Payments | 61.9 |
| UPI Lite | 31.3 |
| UPI Autopay | 21.5 |

## Failure analysis
- No incidents open. Technical declines are within the 0.55% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D02-MON) and any meetings/emails on 06 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D02-MON, RPT-D01-DAILY
