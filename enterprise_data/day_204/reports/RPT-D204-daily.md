---
id: RPT-D204-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-27T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 27 Jul 2026)

**Report ID:** RPT-D204-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 27 Jul 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 204 of 206)

## Transaction summary
The rail processed 749.9M UPI transactions on Monday — the Monday ramp-up after the weekend — up 19.5M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 749.9  (▲128.5 d/d, ▲19.5 w/w, ▼46.0 m/m)
- **Success Rate:** 99.98%  (▲0.7 d/d, ▲0.85 m/m)
- **Settlement Success:** 99.98%  (▲0.02 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.26%  (▲0.01 d/d, ▼0.29 m/m)
- **Business Declines:** 0.15%  (▼0.09 m/m)
- **Customer Complaints:** 833  (▲5 d/d, ▼13 w/w, ▼1309 m/m)
- **Merchant Complaints:** 82  (▼2 w/w, ▼152 m/m)
- **Fraud Alerts:** 698  (▼12 w/w, ▼462 m/m)
- **Risk Score:** 18  (▼16 m/m)
- **Response Time:** 522 ms  (▲2 d/d, ▼8 w/w, ▼231 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 244.1 | 99.67% |
| HDFC Bank | 80.2 | 99.42% |
| Bank of Baroda | 57.7 | 99.26% |
| Union Bank of India | 50.6 | 99.63% |
| Axis Bank | 46.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 358.2 | 99.51% | 198 ms |
| Google Pay | 245.2 | 99.35% | 241 ms |
| Paytm | 59.5 | 99.53% | 201 ms |
| Navi | 27.6 | 99.53% | 304 ms |
| SuperMoney | 14.6 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 277.5 |
| Person to Person | 266.2 |
| QR Payments | 71.2 |
| UPI Lite | 36.0 |
| UPI Autopay | 24.7 |

## Failure analysis
- No incidents open. Technical declines are within the 0.26% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D204-MON) and any meetings/emails on 27 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D204-MON, RPT-D203-DAILY
