---
id: RPT-D46-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-19T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 19 Feb 2026)

**Report ID:** RPT-D46-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 19 Feb 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 46 of 206)

## Transaction summary
The rail processed 666.7M UPI transactions on Thursday — a steady mid-week day — down 17.9M on the same day last week. Success held at 99.15% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 666.7  (▼16.5 d/d, ▼17.9 w/w, ▼129.2 m/m)
- **Success Rate:** 99.15%  (▼0.26 d/d, ▲0.19 w/w, ▲0.02 m/m)
- **Settlement Success:** 99.98%  (▲0.09 d/d, ▲0.03 m/m)
- **Technical Declines:** 0.46%  (▼0.01 d/d, ▼0.02 w/w, ▼0.09 m/m)
- **Business Declines:** 0.21%  (▼0.01 d/d, ▼0.01 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,729  (▼32 d/d, ▼61 w/w, ▼413 m/m)
- **Merchant Complaints:** 186  (▼1 d/d, ▼6 w/w, ▼48 m/m)
- **Fraud Alerts:** 1,020  (▼12 d/d, ▼30 w/w, ▼140 m/m)
- **Risk Score:** 30  (▲1 d/d, ▼4 m/m)
- **Response Time:** 694 ms  (▼6 d/d, ▼16 w/w, ▼59 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 217.0 | 99.67% |
| HDFC Bank | 71.3 | 99.42% |
| Bank of Baroda | 51.3 | 99.26% |
| Union Bank of India | 45.0 | 99.63% |
| Axis Bank | 41.1 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 318.5 | 99.51% | 198 ms |
| Google Pay | 218.0 | 99.35% | 241 ms |
| Paytm | 52.9 | 99.53% | 201 ms |
| Navi | 24.5 | 99.53% | 304 ms |
| SuperMoney | 13.0 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 246.7 |
| Person to Person | 236.7 |
| QR Payments | 63.3 |
| UPI Lite | 32.0 |
| UPI Autopay | 22.0 |

## Failure analysis
- No incidents open. Technical declines are within the 0.46% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D46-MON) and any meetings/emails on 19 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D46-MON, RPT-D45-DAILY
