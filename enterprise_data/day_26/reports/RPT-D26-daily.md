---
id: RPT-D26-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-30T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 30 Jan 2026)

**Report ID:** RPT-D26-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 30 Jan 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 26 of 206)

## Transaction summary
The rail processed 739.8M UPI transactions on Friday — the month-end surge as salary and bill-pay flows land — up 84.1M on the same day last week. Success held at 99.76% and settlement at 99.96%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 739.8  (▼4.6 d/d, ▲84.1 w/w, ▼56.1 m/m)
- **Success Rate:** 99.76%  (▼0.17 d/d, ▲1.15 w/w, ▲0.63 m/m)
- **Settlement Success:** 99.96%  (▲0.1 d/d, ▲0.11 w/w, ▲0.01 m/m)
- **Technical Declines:** 0.5%  (▼0.17 w/w, ▼0.05 m/m)
- **Business Declines:** 0.23%  (▼0.01 m/m)
- **Customer Complaints:** 1,927  (▲23 d/d, ▼418 w/w, ▼215 m/m)
- **Merchant Complaints:** 205  (▼4 d/d, ▼8 w/w, ▼29 m/m)
- **Fraud Alerts:** 1,086  (▲13 d/d, ▼5 w/w, ▼74 m/m)
- **Risk Score:** 32  (▼2 m/m)
- **Response Time:** 723 ms  (▲2 d/d, ▼40 w/w, ▼30 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 240.8 | 99.67% |
| HDFC Bank | 79.1 | 99.42% |
| Bank of Baroda | 56.9 | 99.26% |
| Union Bank of India | 49.9 | 99.63% |
| Axis Bank | 45.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 353.4 | 99.51% | 198 ms |
| Google Pay | 241.9 | 99.35% | 241 ms |
| Paytm | 58.7 | 99.53% | 201 ms |
| Navi | 27.2 | 99.53% | 304 ms |
| SuperMoney | 14.4 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 273.7 |
| Person to Person | 262.6 |
| QR Payments | 70.3 |
| UPI Lite | 35.5 |
| UPI Autopay | 24.4 |

## Failure analysis
- No incidents open. Technical declines are within the 0.5% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D26-MON) and any meetings/emails on 30 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D26-MON, RPT-D25-DAILY
