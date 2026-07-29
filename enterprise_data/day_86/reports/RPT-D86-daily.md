---
id: RPT-D86-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-31T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 31 Mar 2026)

**Report ID:** RPT-D86-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 31 Mar 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 86 of 206)

## Transaction summary
The rail processed 787.5M UPI transactions on Tuesday — the month-end surge as salary and bill-pay flows land — up 93.8M on the same day last week. Success held at 98.67% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 787.5  (▲11.0 d/d, ▲93.8 w/w, ▼8.4 m/m)
- **Success Rate:** 98.67%  (▲0.12 d/d, ▼0.51 w/w, ▼0.46 m/m)
- **Settlement Success:** 99.98%  (▲0.08 d/d, ▲0.57 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.39%  (▼0.01 d/d, ▼0.1 w/w, ▼0.16 m/m)
- **Business Declines:** 0.19%  (▼0.01 w/w, ▼0.05 m/m)
- **Customer Complaints:** 1,435  (▼25 d/d, ▼290 w/w, ▼707 m/m)
- **Merchant Complaints:** 152  (▲1 d/d, ▼5 w/w, ▼82 m/m)
- **Fraud Alerts:** 939  (▲5 d/d, ▼10 w/w, ▼221 m/m)
- **Risk Score:** 26  (▼1 w/w, ▼8 m/m)
- **Response Time:** 655 ms  (▼2 d/d, ▼55 w/w, ▼98 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 256.3 | 99.67% |
| HDFC Bank | 84.2 | 99.42% |
| Bank of Baroda | 60.6 | 99.26% |
| Union Bank of India | 53.1 | 99.63% |
| Axis Bank | 48.5 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 376.2 | 99.51% | 198 ms |
| Google Pay | 257.5 | 99.35% | 241 ms |
| Paytm | 62.5 | 99.53% | 201 ms |
| Navi | 29.0 | 99.53% | 304 ms |
| SuperMoney | 15.4 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 291.4 |
| Person to Person | 279.6 |
| QR Payments | 74.8 |
| UPI Lite | 37.8 |
| UPI Autopay | 26.0 |

## Failure analysis
- No incidents open. Technical declines are within the 0.39% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D86-MON) and any meetings/emails on 31 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D86-MON, RPT-D85-DAILY
