---
id: RPT-D106-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-20T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 20 Apr 2026)

**Report ID:** RPT-D106-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 20 Apr 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 106 of 206)

## Transaction summary
The rail processed 694.2M UPI transactions on Monday — the Monday ramp-up after the weekend — up 6.8M on the same day last week. Success held at 99.98% and settlement at 99.75%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 694.2  (▲104.6 d/d, ▲6.8 w/w, ▼101.7 m/m)
- **Success Rate:** 99.98%  (▲0.57 d/d, ▲0.85 m/m)
- **Settlement Success:** 99.75%  (▲0.97 d/d, ▲0.06 w/w, ▼0.2 m/m)
- **Technical Declines:** 0.37%  (▼0.01 w/w, ▼0.18 m/m)
- **Business Declines:** 0.19%  (▲0.01 d/d, ▼0.05 m/m)
- **Customer Complaints:** 1,314  (▲9 d/d, ▼34 w/w, ▼828 m/m)
- **Merchant Complaints:** 137  (▼1 d/d, ▼4 w/w, ▼97 m/m)
- **Fraud Alerts:** 884  (▼8 d/d, ▼25 w/w, ▼276 m/m)
- **Risk Score:** 24  (▼1 w/w, ▼10 m/m)
- **Response Time:** 625 ms  (▼8 w/w, ▼128 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 226.0 | 99.67% |
| HDFC Bank | 74.2 | 99.42% |
| Bank of Baroda | 53.4 | 99.26% |
| Union Bank of India | 46.8 | 99.63% |
| Axis Bank | 42.8 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 331.6 | 99.51% | 198 ms |
| Google Pay | 227.0 | 99.35% | 241 ms |
| Paytm | 55.1 | 99.53% | 201 ms |
| Navi | 25.5 | 99.53% | 304 ms |
| SuperMoney | 13.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 256.9 |
| Person to Person | 246.4 |
| QR Payments | 65.9 |
| UPI Lite | 33.3 |
| UPI Autopay | 22.9 |

## Failure analysis
- No incidents open. Technical declines are within the 0.37% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D106-MON) and any meetings/emails on 20 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D106-MON, RPT-D105-DAILY
