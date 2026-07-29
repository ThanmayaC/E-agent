---
id: RPT-D14-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-18T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 18 Jan 2026)

**Report ID:** RPT-D14-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 18 Jan 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 14 of 206)

## Transaction summary
The rail processed 539.2M UPI transactions on Sunday — a quiet Sunday — broadly flat against the same day last week. Success held at 99.03% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 539.2  (▼72.1 d/d, ▼256.7 m/m)
- **Success Rate:** 99.03%  (▲0.68 d/d, ▼0.66 w/w, ▼0.1 m/m)
- **Settlement Success:** 99.98%  (▲0.05 d/d, ▲0.75 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.52%  (▼0.01 d/d, ▼0.2 w/w, ▼0.03 m/m)
- **Business Declines:** 0.23%  (▼0.01 w/w, ▼0.01 m/m)
- **Customer Complaints:** 2,041  (▲1 d/d, ▼555 w/w, ▼101 m/m)
- **Merchant Complaints:** 221  (▲2 d/d, ▼92 w/w, ▼13 m/m)
- **Fraud Alerts:** 1,105  (▼18 w/w, ▼55 m/m)
- **Risk Score:** 32  (▼1 d/d, ▼1 w/w, ▼2 m/m)
- **Response Time:** 747 ms  (▲11 d/d, ▼44 w/w, ▼6 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 175.5 | 99.67% |
| HDFC Bank | 57.6 | 99.42% |
| Bank of Baroda | 41.5 | 99.26% |
| Union Bank of India | 36.4 | 99.63% |
| Axis Bank | 33.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 257.6 | 99.51% | 198 ms |
| Google Pay | 176.3 | 99.35% | 241 ms |
| Paytm | 42.8 | 99.53% | 201 ms |
| Navi | 19.8 | 99.53% | 304 ms |
| SuperMoney | 10.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 199.5 |
| Person to Person | 191.4 |
| QR Payments | 51.2 |
| UPI Lite | 25.9 |
| UPI Autopay | 17.8 |

## Failure analysis
- No incidents open. Technical declines are within the 0.52% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D14-MON) and any meetings/emails on 18 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D14-MON, RPT-D13-DAILY
