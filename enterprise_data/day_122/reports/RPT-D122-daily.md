---
id: RPT-D122-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-06T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 06 May 2026)

**Report ID:** RPT-D122-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 06 May 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 122 of 206)

## Transaction summary
The rail processed 723.0M UPI transactions on Wednesday — a steady mid-week day — down 58.4M on the same day last week. Success held at 99.98% and settlement at 98.89%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 723.0  (▼1.1 d/d, ▼58.4 w/w, ▼72.9 m/m)
- **Success Rate:** 99.98%  (▲1.15 d/d, ▲0.68 w/w, ▲0.85 m/m)
- **Settlement Success:** 98.89%  (▼1.09 d/d, ▼0.66 w/w, ▼1.06 m/m)
- **Technical Declines:** 0.35%  (▼0.14 w/w, ▼0.2 m/m)
- **Business Declines:** 0.18%  (▼0.06 m/m)
- **Customer Complaints:** 1,203  (▼7 d/d, ▼386 w/w, ▼939 m/m)
- **Merchant Complaints:** 125  (▼2 d/d, ▼58 w/w, ▼109 m/m)
- **Fraud Alerts:** 843  (▼3 d/d, ▼20 w/w, ▼317 m/m)
- **Risk Score:** 23  (▼1 w/w, ▼11 m/m)
- **Response Time:** 613 ms  (▲10 d/d, ▼34 w/w, ▼140 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 235.3 | 99.67% |
| HDFC Bank | 77.3 | 99.42% |
| Bank of Baroda | 55.6 | 99.26% |
| Union Bank of India | 48.8 | 99.63% |
| Axis Bank | 44.5 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 345.3 | 99.51% | 198 ms |
| Google Pay | 236.4 | 99.35% | 241 ms |
| Paytm | 57.3 | 99.53% | 201 ms |
| Navi | 26.6 | 99.53% | 304 ms |
| SuperMoney | 14.1 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 267.5 |
| Person to Person | 256.7 |
| QR Payments | 68.7 |
| UPI Lite | 34.7 |
| UPI Autopay | 23.9 |

## Failure analysis
- No incidents open. Technical declines are within the 0.35% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D122-MON) and any meetings/emails on 06 May.

Refs: upi_kpis_month.xlsx, TEAMS-D122-MON, RPT-D121-DAILY
