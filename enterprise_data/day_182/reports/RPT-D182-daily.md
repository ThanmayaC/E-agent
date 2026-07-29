---
id: RPT-D182-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-05T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 05 Jul 2026)

**Report ID:** RPT-D182-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 05 Jul 2026  ·  **Day archetype:** Sunday (quiet) · maintenance window
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 182 of 206)

## Transaction summary
The rail processed 620.7M UPI transactions on Sunday — a quiet Sunday with a scheduled maintenance window — down 223.9M on the same day last week. Success held at 99.8% and settlement at 99.63%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 620.7  (▼52.5 d/d, ▼223.9 w/w, ▼175.2 m/m)
- **Success Rate:** 99.8%  (▼0.18 d/d, ▼0.18 w/w, ▲0.67 m/m)
- **Settlement Success:** 99.63%  (▼0.35 d/d, ▼0.35 w/w, ▼0.32 m/m)
- **Technical Declines:** 0.27%  (▼0.01 d/d, ▼0.01 w/w, ▼0.28 m/m)
- **Business Declines:** 0.15%  (▼0.01 w/w, ▼0.09 m/m)
- **Customer Complaints:** 912  (▼7 d/d, ▼37 w/w, ▼1230 m/m)
- **Merchant Complaints:** 92  (▼2 w/w, ▼142 m/m)
- **Fraud Alerts:** 731  (▼3 d/d, ▼11 w/w, ▼429 m/m)
- **Risk Score:** 19  (▼1 w/w, ▼15 m/m)
- **Response Time:** 548 ms  (▲8 d/d, ▼7 w/w, ▼205 m/m)

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
| PhonePe | 296.5 | 99.51% | 198 ms |
| Google Pay | 203.0 | 99.35% | 241 ms |
| Paytm | 49.2 | 99.53% | 201 ms |
| Navi | 22.8 | 99.53% | 304 ms |
| SuperMoney | 12.1 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 229.7 |
| Person to Person | 220.3 |
| QR Payments | 59.0 |
| UPI Lite | 29.8 |
| UPI Autopay | 20.5 |

## Failure analysis
- No incidents open. Technical declines are within the 0.27% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D182-MON) and any meetings/emails on 05 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D182-MON, RPT-D181-DAILY
