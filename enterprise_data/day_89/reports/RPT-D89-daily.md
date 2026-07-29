---
id: RPT-D89-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-03T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 03 Apr 2026)

**Report ID:** RPT-D89-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 03 Apr 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 89 of 206)

## Transaction summary
The rail processed 858.1M UPI transactions on Friday — a campaign-driven high-volume day — up 163.5M on the same day last week. Success held at 99.57% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 858.1  (▲153.4 d/d, ▲163.5 w/w, ▲62.2 m/m)
- **Success Rate:** 99.57%  (▲0.79 d/d, ▼0.41 w/w, ▲0.44 m/m)
- **Settlement Success:** 99.98%  (▲0.34 d/d, ▲0.03 m/m)
- **Technical Declines:** 0.39%  (▼0.01 d/d, ▼0.08 w/w, ▼0.16 m/m)
- **Business Declines:** 0.19%  (▼0.01 w/w, ▼0.05 m/m)
- **Customer Complaints:** 1,423  (▲3 d/d, ▼204 w/w, ▼719 m/m)
- **Merchant Complaints:** 150  (▼1 d/d, ▼5 w/w, ▼84 m/m)
- **Fraud Alerts:** 924  (▲2 d/d, ▼19 w/w, ▼236 m/m)
- **Risk Score:** 26  (▼8 m/m)
- **Response Time:** 642 ms  (▼1 d/d, ▼23 w/w, ▼111 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 279.3 | 99.67% |
| HDFC Bank | 91.7 | 99.42% |
| Bank of Baroda | 66.0 | 99.26% |
| Union Bank of India | 57.9 | 99.63% |
| Axis Bank | 52.9 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 409.9 | 99.51% | 198 ms |
| Google Pay | 280.6 | 99.35% | 241 ms |
| Paytm | 68.1 | 99.53% | 201 ms |
| Navi | 31.5 | 99.53% | 304 ms |
| SuperMoney | 16.7 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 317.5 |
| Person to Person | 304.6 |
| QR Payments | 81.5 |
| UPI Lite | 41.2 |
| UPI Autopay | 28.3 |

## Failure analysis
- No incidents open. Technical declines are within the 0.39% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D89-MON) and any meetings/emails on 03 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D89-MON, RPT-D88-DAILY
