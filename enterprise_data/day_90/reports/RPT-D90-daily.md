---
id: RPT-D90-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-04T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 04 Apr 2026)

**Report ID:** RPT-D90-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 04 Apr 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 90 of 206)

## Transaction summary
The rail processed 620.6M UPI transactions on Saturday — a lighter Saturday — down 167.6M on the same day last week. Success held at 99.33% and settlement at 99.6%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 620.6  (▼237.5 d/d, ▼167.6 w/w, ▼175.3 m/m)
- **Success Rate:** 99.33%  (▼0.24 d/d, ▲0.26 w/w, ▲0.2 m/m)
- **Settlement Success:** 99.6%  (▼0.38 d/d, ▼0.38 w/w, ▼0.35 m/m)
- **Technical Declines:** 0.39%  (▼0.05 w/w, ▼0.16 m/m)
- **Business Declines:** 0.19%  (▼0.01 w/w, ▼0.05 m/m)
- **Customer Complaints:** 1,420  (▼3 d/d, ▼114 w/w, ▼722 m/m)
- **Merchant Complaints:** 147  (▼3 d/d, ▼8 w/w, ▼87 m/m)
- **Fraud Alerts:** 928  (▲4 d/d, ▼1 w/w, ▼232 m/m)
- **Risk Score:** 26  (▼8 m/m)
- **Response Time:** 648 ms  (▲6 d/d, ▼13 w/w, ▼105 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 202.0 | 99.67% |
| HDFC Bank | 66.4 | 99.42% |
| Bank of Baroda | 47.8 | 99.26% |
| Union Bank of India | 41.9 | 99.63% |
| Axis Bank | 38.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 296.4 | 99.51% | 198 ms |
| Google Pay | 203.0 | 99.35% | 241 ms |
| Paytm | 49.2 | 99.53% | 201 ms |
| Navi | 22.8 | 99.53% | 304 ms |
| SuperMoney | 12.1 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 229.6 |
| Person to Person | 220.3 |
| QR Payments | 59.0 |
| UPI Lite | 29.8 |
| UPI Autopay | 20.5 |

## Failure analysis
- No incidents open. Technical declines are within the 0.39% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D90-MON) and any meetings/emails on 04 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D90-MON, RPT-D89-DAILY
