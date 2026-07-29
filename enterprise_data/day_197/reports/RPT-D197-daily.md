---
id: RPT-D197-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-20T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 20 Jul 2026)

**Report ID:** RPT-D197-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 20 Jul 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 197 of 206)

## Transaction summary
The rail processed 730.4M UPI transactions on Monday — the Monday ramp-up after the weekend — up 4.0M on the same day last week. Success held at 99.98% and settlement at 99.96%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 730.4  (▲114.0 d/d, ▲4.0 w/w, ▼65.5 m/m)
- **Success Rate:** 99.98%  (▲0.91 d/d, ▲0.43 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.96%  (▲0.25 d/d, ▲0.28 w/w, ▲0.01 m/m)
- **Technical Declines:** 0.26%  (▼0.01 w/w, ▼0.29 m/m)
- **Business Declines:** 0.15%  (▼0.09 m/m)
- **Customer Complaints:** 846  (▼14 d/d, ▼28 w/w, ▼1296 m/m)
- **Merchant Complaints:** 84  (▼1 d/d, ▼3 w/w, ▼150 m/m)
- **Fraud Alerts:** 710  (▲7 d/d, ▼15 w/w, ▼450 m/m)
- **Risk Score:** 18  (▼1 w/w, ▼16 m/m)
- **Response Time:** 530 ms  (▲3 d/d, ▼6 w/w, ▼223 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 237.7 | 99.67% |
| HDFC Bank | 78.1 | 99.42% |
| Bank of Baroda | 56.2 | 99.26% |
| Union Bank of India | 49.3 | 99.63% |
| Axis Bank | 45.0 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 348.9 | 99.51% | 198 ms |
| Google Pay | 238.9 | 99.35% | 241 ms |
| Paytm | 57.9 | 99.53% | 201 ms |
| Navi | 26.9 | 99.53% | 304 ms |
| SuperMoney | 14.2 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 270.2 |
| Person to Person | 259.3 |
| QR Payments | 69.4 |
| UPI Lite | 35.1 |
| UPI Autopay | 24.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.26% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D197-MON) and any meetings/emails on 20 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D197-MON, RPT-D196-DAILY
