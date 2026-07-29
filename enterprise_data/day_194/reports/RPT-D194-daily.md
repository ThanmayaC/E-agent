---
id: RPT-D194-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-17T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 17 Jul 2026)

**Report ID:** RPT-D194-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 17 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 194 of 206)

## Transaction summary
The rail processed 761.1M UPI transactions on Friday — a steady mid-week day — up 10.8M on the same day last week. Success held at 99.92% and settlement at 99.93%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 761.1  (▲14.4 d/d, ▲10.8 w/w, ▼34.8 m/m)
- **Success Rate:** 99.92%  (▲0.37 d/d, ▲0.29 w/w, ▲0.79 m/m)
- **Settlement Success:** 99.93%  (▲0.4 d/d, ▲0.62 w/w, ▼0.02 m/m)
- **Technical Declines:** 0.26%  (▼0.03 w/w, ▼0.29 m/m)
- **Business Declines:** 0.15%  (▼0.09 m/m)
- **Customer Complaints:** 867  (▲2 d/d, ▼74 w/w, ▼1275 m/m)
- **Merchant Complaints:** 87  (▼2 w/w, ▼147 m/m)
- **Fraud Alerts:** 713  (▼4 d/d, ▼17 w/w, ▼447 m/m)
- **Risk Score:** 19  (▼15 m/m)
- **Response Time:** 536 ms  (▼1 d/d, ▼8 w/w, ▼217 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 247.7 | 99.67% |
| HDFC Bank | 81.4 | 99.42% |
| Bank of Baroda | 58.6 | 99.26% |
| Union Bank of India | 51.3 | 99.63% |
| Axis Bank | 46.9 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 363.5 | 99.51% | 198 ms |
| Google Pay | 248.9 | 99.35% | 241 ms |
| Paytm | 60.4 | 99.53% | 201 ms |
| Navi | 28.0 | 99.53% | 304 ms |
| SuperMoney | 14.8 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 281.6 |
| Person to Person | 270.2 |
| QR Payments | 72.3 |
| UPI Lite | 36.5 |
| UPI Autopay | 25.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.26% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D194-MON) and any meetings/emails on 17 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D194-MON, RPT-D193-DAILY
