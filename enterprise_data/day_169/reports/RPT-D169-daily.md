---
id: RPT-D169-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-22T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 22 Jun 2026)

**Report ID:** RPT-D169-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 22 Jun 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 169 of 206)

## Transaction summary
The rail processed 732.5M UPI transactions on Monday — the Monday ramp-up after the weekend — up 3.3M on the same day last week. Success held at 99.98% and settlement at 99.42%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 732.5  (▲134.8 d/d, ▲3.3 w/w, ▼63.4 m/m)
- **Success Rate:** 99.98%  (▲0.7 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.42%  (▼0.35 d/d, ▼0.56 w/w, ▼0.53 m/m)
- **Technical Declines:** 0.29%  (▼0.01 w/w, ▼0.26 m/m)
- **Business Declines:** 0.16%  (▼0.08 m/m)
- **Customer Complaints:** 968  (▼15 d/d, ▼40 w/w, ▼1174 m/m)
- **Merchant Complaints:** 98  (▼1 d/d, ▼4 w/w, ▼136 m/m)
- **Fraud Alerts:** 763  (▲11 d/d, ▼8 w/w, ▼397 m/m)
- **Risk Score:** 20  (▼14 m/m)
- **Response Time:** 559 ms  (▼3 d/d, ▼8 w/w, ▼194 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 238.4 | 99.67% |
| HDFC Bank | 78.3 | 99.42% |
| Bank of Baroda | 56.4 | 99.26% |
| Union Bank of India | 49.4 | 99.63% |
| Axis Bank | 45.1 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 349.9 | 99.51% | 198 ms |
| Google Pay | 239.6 | 99.35% | 241 ms |
| Paytm | 58.1 | 99.53% | 201 ms |
| Navi | 26.9 | 99.53% | 304 ms |
| SuperMoney | 14.3 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 271.0 |
| Person to Person | 260.0 |
| QR Payments | 69.6 |
| UPI Lite | 35.2 |
| UPI Autopay | 24.2 |

## Failure analysis
- No incidents open. Technical declines are within the 0.29% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D169-MON) and any meetings/emails on 22 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D169-MON, RPT-D168-DAILY
