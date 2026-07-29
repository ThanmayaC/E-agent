---
id: RPT-D57-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-02T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 02 Mar 2026)

**Report ID:** RPT-D57-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 02 Mar 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 57 of 206)

## Transaction summary
The rail processed 667.9M UPI transactions on Monday — the Monday ramp-up after the weekend — up 10.5M on the same day last week. Success held at 98.6% and settlement at 98.72%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 667.9  (▲100.9 d/d, ▲10.5 w/w, ▼128.0 m/m)
- **Success Rate:** 98.6%  (▲0.2 d/d, ▼0.76 w/w, ▼0.53 m/m)
- **Settlement Success:** 98.72%  (▼0.07 d/d, ▼0.45 w/w, ▼1.23 m/m)
- **Technical Declines:** 0.45%  (▼0.01 w/w, ▼0.1 m/m)
- **Business Declines:** 0.21%  (▼0.06 d/d, ▼0.16 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,652  (▼226 d/d, ▼640 w/w, ▼490 m/m)
- **Merchant Complaints:** 176  (▼2 d/d, ▼7 w/w, ▼58 m/m)
- **Fraud Alerts:** 1,003  (▼128 d/d, ▼355 w/w, ▼157 m/m)
- **Risk Score:** 28  (▼10 d/d, ▼26 w/w, ▼6 m/m)
- **Response Time:** 682 ms  (▼1 d/d, ▼11 w/w, ▼71 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 217.4 | 99.67% |
| HDFC Bank | 71.4 | 99.42% |
| Bank of Baroda | 51.4 | 99.26% |
| Union Bank of India | 45.1 | 99.63% |
| Axis Bank | 41.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 319.0 | 99.51% | 198 ms |
| Google Pay | 218.4 | 99.35% | 241 ms |
| Paytm | 53.0 | 99.53% | 201 ms |
| Navi | 24.6 | 99.53% | 304 ms |
| SuperMoney | 13.0 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 247.1 |
| Person to Person | 237.1 |
| QR Payments | 63.5 |
| UPI Lite | 32.1 |
| UPI Autopay | 22.0 |

## Failure analysis
- No incidents open. Technical declines are within the 0.45% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D57-MON) and any meetings/emails on 02 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D57-MON, RPT-D56-DAILY
