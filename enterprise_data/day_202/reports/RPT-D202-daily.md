---
id: RPT-D202-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-25T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 25 Jul 2026)

**Report ID:** RPT-D202-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 25 Jul 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 202 of 206)

## Transaction summary
The rail processed 663.8M UPI transactions on Saturday — a lighter Saturday — down 10.3M on the same day last week. Success held at 99.19% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 663.8  (▼107.8 d/d, ▼10.3 w/w, ▼132.1 m/m)
- **Success Rate:** 99.19%  (▼0.79 d/d, ▼0.79 w/w, ▲0.06 m/m)
- **Settlement Success:** 99.98%  (▲0.4 d/d, ▲0.23 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.25%  (▼0.01 d/d, ▼0.02 w/w, ▼0.3 m/m)
- **Business Declines:** 0.15%  (▼0.09 m/m)
- **Customer Complaints:** 837  (▼3 d/d, ▼26 w/w, ▼1305 m/m)
- **Merchant Complaints:** 83  (▼4 w/w, ▼151 m/m)
- **Fraud Alerts:** 697  (▼2 d/d, ▼7 w/w, ▼463 m/m)
- **Risk Score:** 18  (▼16 m/m)
- **Response Time:** 525 ms  (▲2 d/d, ▼3 w/w, ▼228 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 216.1 | 99.67% |
| HDFC Bank | 71.0 | 99.42% |
| Bank of Baroda | 51.1 | 99.26% |
| Union Bank of India | 44.8 | 99.63% |
| Axis Bank | 40.9 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 317.1 | 99.51% | 198 ms |
| Google Pay | 217.1 | 99.35% | 241 ms |
| Paytm | 52.7 | 99.53% | 201 ms |
| Navi | 24.4 | 99.53% | 304 ms |
| SuperMoney | 12.9 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 245.6 |
| Person to Person | 235.6 |
| QR Payments | 63.1 |
| UPI Lite | 31.9 |
| UPI Autopay | 21.9 |

## Failure analysis
- No incidents open. Technical declines are within the 0.25% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D202-MON) and any meetings/emails on 25 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D202-MON, RPT-D201-DAILY
