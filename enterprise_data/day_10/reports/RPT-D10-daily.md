---
id: RPT-D10-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-14T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 14 Jan 2026)

**Report ID:** RPT-D10-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 14 Jan 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 10 of 206)

## Transaction summary
The rail processed 679.0M UPI transactions on Wednesday — a steady mid-week day — up 19.9M on the same day last week. Success held at 98.26% and settlement at 98.85%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 679.0  (▲24.3 d/d, ▲19.9 w/w, ▼116.9 m/m)
- **Success Rate:** 98.26%  (▼1.7 d/d, ▼1.47 w/w, ▼0.87 m/m)
- **Settlement Success:** 98.85%  (▼0.92 d/d, ▼0.45 w/w, ▼1.1 m/m)
- **Technical Declines:** 0.53%  (▼0.01 d/d, ▼0.02 w/w, ▼0.02 m/m)
- **Business Declines:** 0.24%
- **Customer Complaints:** 2,079  (▲25 d/d, ▼47 w/w, ▼63 m/m)
- **Merchant Complaints:** 225  (▼10 w/w, ▼9 m/m)
- **Fraud Alerts:** 1,114  (▼13 d/d, ▼28 w/w, ▼46 m/m)
- **Risk Score:** 33  (▼1 w/w, ▼1 m/m)
- **Response Time:** 749 ms  (▲1 d/d, ▼3 w/w, ▼4 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 221.0 | 99.67% |
| HDFC Bank | 72.6 | 99.42% |
| Bank of Baroda | 52.3 | 99.26% |
| Union Bank of India | 45.8 | 99.63% |
| Axis Bank | 41.8 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 324.3 | 99.51% | 198 ms |
| Google Pay | 222.1 | 99.35% | 241 ms |
| Paytm | 53.9 | 99.53% | 201 ms |
| Navi | 25.0 | 99.53% | 304 ms |
| SuperMoney | 13.2 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 251.2 |
| Person to Person | 241.0 |
| QR Payments | 64.5 |
| UPI Lite | 32.6 |
| UPI Autopay | 22.4 |

## Failure analysis
- No incidents open. Technical declines are within the 0.53% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D10-MON) and any meetings/emails on 14 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D10-MON, RPT-D09-DAILY
