---
id: RPT-D64-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-09T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 09 Mar 2026)

**Report ID:** RPT-D64-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 09 Mar 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 64 of 206)

## Transaction summary
The rail processed 848.7M UPI transactions on Monday — a campaign-driven high-volume day — up 180.8M on the same day last week. Success held at 99.8% and settlement at 98.76%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 848.7  (▲281.5 d/d, ▲180.8 w/w, ▲52.8 m/m)
- **Success Rate:** 99.8%  (▲1.23 d/d, ▲1.2 w/w, ▲0.67 m/m)
- **Settlement Success:** 98.76%  (▼1.22 d/d, ▲0.04 w/w, ▼1.19 m/m)
- **Technical Declines:** 0.43%  (▼0.02 w/w, ▼0.12 m/m)
- **Business Declines:** 0.2%  (▼0.01 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,589  (▼31 d/d, ▼63 w/w, ▼553 m/m)
- **Merchant Complaints:** 168  (▼1 d/d, ▼8 w/w, ▼66 m/m)
- **Fraud Alerts:** 982  (▲3 d/d, ▼21 w/w, ▼178 m/m)
- **Risk Score:** 28  (▼6 m/m)
- **Response Time:** 681 ms  (▼1 w/w, ▼72 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 276.3 | 99.67% |
| HDFC Bank | 90.7 | 99.42% |
| Bank of Baroda | 65.3 | 99.26% |
| Union Bank of India | 57.3 | 99.63% |
| Axis Bank | 52.3 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 405.4 | 99.51% | 198 ms |
| Google Pay | 277.6 | 99.35% | 241 ms |
| Paytm | 67.3 | 99.53% | 201 ms |
| Navi | 31.2 | 99.53% | 304 ms |
| SuperMoney | 16.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 314.0 |
| Person to Person | 301.3 |
| QR Payments | 80.6 |
| UPI Lite | 40.7 |
| UPI Autopay | 28.0 |

## Failure analysis
- No incidents open. Technical declines are within the 0.43% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D64-MON) and any meetings/emails on 09 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D64-MON, RPT-D63-DAILY
