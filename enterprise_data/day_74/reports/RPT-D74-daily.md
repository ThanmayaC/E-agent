---
id: RPT-D74-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-19T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 19 Mar 2026)

**Report ID:** RPT-D74-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 19 Mar 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 74 of 206)

## Transaction summary
The rail processed 697.1M UPI transactions on Thursday — a steady mid-week day — up 25.2M on the same day last week. Success held at 99.63% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 697.1  (▼7.1 d/d, ▲25.2 w/w, ▼98.8 m/m)
- **Success Rate:** 99.63%  (▼0.35 d/d, ▲0.73 w/w, ▲0.5 m/m)
- **Settlement Success:** 99.98%  (▲1.14 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.41%  (▼0.01 d/d, ▼0.02 w/w, ▼0.14 m/m)
- **Business Declines:** 0.2%  (▼0.04 m/m)
- **Customer Complaints:** 1,515  (▼12 d/d, ▼60 w/w, ▼627 m/m)
- **Merchant Complaints:** 161  (▼1 d/d, ▼5 w/w, ▼73 m/m)
- **Fraud Alerts:** 962  (▼9 d/d, ▼10 w/w, ▼198 m/m)
- **Risk Score:** 27  (▼1 w/w, ▼7 m/m)
- **Response Time:** 658 ms  (▼8 d/d, ▼11 w/w, ▼95 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 226.9 | 99.67% |
| HDFC Bank | 74.5 | 99.42% |
| Bank of Baroda | 53.6 | 99.26% |
| Union Bank of India | 47.0 | 99.63% |
| Axis Bank | 43.0 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 333.0 | 99.51% | 198 ms |
| Google Pay | 228.0 | 99.35% | 241 ms |
| Paytm | 55.3 | 99.53% | 201 ms |
| Navi | 25.6 | 99.53% | 304 ms |
| SuperMoney | 13.6 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 257.9 |
| Person to Person | 247.5 |
| QR Payments | 66.2 |
| UPI Lite | 33.5 |
| UPI Autopay | 23.0 |

## Failure analysis
- No incidents open. Technical declines are within the 0.41% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D74-MON) and any meetings/emails on 19 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D74-MON, RPT-D73-DAILY
