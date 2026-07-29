---
id: RPT-D174-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-27T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 27 Jun 2026)

**Report ID:** RPT-D174-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 27 Jun 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 174 of 206)

## Transaction summary
The rail processed 660.7M UPI transactions on Saturday — a lighter Saturday — down 3.0M on the same day last week. Success held at 98.96% and settlement at 99.67%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 660.7  (▼89.7 d/d, ▼3.0 w/w, ▼135.2 m/m)
- **Success Rate:** 98.96%  (▼1.02 d/d, ▼1.02 w/w, ▼0.17 m/m)
- **Settlement Success:** 99.67%  (▼0.31 d/d, ▲0.39 w/w, ▼0.28 m/m)
- **Technical Declines:** 0.28%  (▼0.01 d/d, ▼0.01 w/w, ▼0.27 m/m)
- **Business Declines:** 0.16%  (▼0.08 m/m)
- **Customer Complaints:** 942  (▼9 d/d, ▼39 w/w, ▼1200 m/m)
- **Merchant Complaints:** 95  (▼2 d/d, ▼4 w/w, ▼139 m/m)
- **Fraud Alerts:** 740  (▼5 d/d, ▼21 w/w, ▼420 m/m)
- **Risk Score:** 20  (▼14 m/m)
- **Response Time:** 551 ms  (▼1 d/d, ▼11 w/w, ▼202 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 215.1 | 99.67% |
| HDFC Bank | 70.6 | 99.42% |
| Bank of Baroda | 50.8 | 99.26% |
| Union Bank of India | 44.6 | 99.63% |
| Axis Bank | 40.7 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 315.6 | 99.51% | 198 ms |
| Google Pay | 216.1 | 99.35% | 241 ms |
| Paytm | 52.4 | 99.53% | 201 ms |
| Navi | 24.3 | 99.53% | 304 ms |
| SuperMoney | 12.9 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 244.5 |
| Person to Person | 234.5 |
| QR Payments | 62.8 |
| UPI Lite | 31.7 |
| UPI Autopay | 21.8 |

## Failure analysis
- No incidents open. Technical declines are within the 0.28% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D174-MON) and any meetings/emails on 27 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D174-MON, RPT-D173-DAILY
