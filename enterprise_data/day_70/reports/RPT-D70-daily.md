---
id: RPT-D70-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-15T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 15 Mar 2026)

**Report ID:** RPT-D70-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 15 Mar 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 70 of 206)

## Transaction summary
The rail processed 565.4M UPI transactions on Sunday — a quiet Sunday — down 1.8M on the same day last week. Success held at 98.5% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 565.4  (▼62.4 d/d, ▼1.8 w/w, ▼230.5 m/m)
- **Success Rate:** 98.5%  (▼1.48 d/d, ▼0.07 w/w, ▼0.63 m/m)
- **Settlement Success:** 99.98%  (▲0.35 d/d, ▲0.03 m/m)
- **Technical Declines:** 0.42%  (▼0.01 w/w, ▼0.13 m/m)
- **Business Declines:** 0.2%  (▼0.04 m/m)
- **Customer Complaints:** 1,547  (▼2 d/d, ▼73 w/w, ▼595 m/m)
- **Merchant Complaints:** 164  (▼2 d/d, ▼5 w/w, ▼70 m/m)
- **Fraud Alerts:** 971  (▼7 d/d, ▼8 w/w, ▼189 m/m)
- **Risk Score:** 27  (▼1 d/d, ▼1 w/w, ▼7 m/m)
- **Response Time:** 673 ms  (▲6 d/d, ▼8 w/w, ▼80 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 184.0 | 99.67% |
| HDFC Bank | 60.5 | 99.42% |
| Bank of Baroda | 43.5 | 99.26% |
| Union Bank of India | 38.1 | 99.63% |
| Axis Bank | 34.8 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 270.1 | 99.51% | 198 ms |
| Google Pay | 184.9 | 99.35% | 241 ms |
| Paytm | 44.8 | 99.53% | 201 ms |
| Navi | 20.8 | 99.53% | 304 ms |
| SuperMoney | 11.0 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 209.2 |
| Person to Person | 200.7 |
| QR Payments | 53.7 |
| UPI Lite | 27.1 |
| UPI Autopay | 18.7 |

## Failure analysis
- No incidents open. Technical declines are within the 0.42% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D70-MON) and any meetings/emails on 15 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D70-MON, RPT-D69-DAILY
