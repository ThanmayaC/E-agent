---
id: RPT-D176-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-29T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 29 Jun 2026)

**Report ID:** RPT-D176-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 29 Jun 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 176 of 206)

## Transaction summary
The rail processed 831.5M UPI transactions on Monday — the month-end surge as salary and bill-pay flows land — up 99.0M on the same day last week. Success held at 99.55% and settlement at 99.15%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 831.5  (▼13.1 d/d, ▲99.0 w/w, ▲35.6 m/m)
- **Success Rate:** 99.55%  (▼0.43 d/d, ▼0.43 w/w, ▲0.42 m/m)
- **Settlement Success:** 99.15%  (▼0.83 d/d, ▼0.27 w/w, ▼0.8 m/m)
- **Technical Declines:** 0.29%  (▲0.01 d/d, ▼0.26 m/m)
- **Business Declines:** 0.16%  (▼0.08 m/m)
- **Customer Complaints:** 948  (▼1 d/d, ▼20 w/w, ▼1194 m/m)
- **Merchant Complaints:** 94  (▼4 w/w, ▼140 m/m)
- **Fraud Alerts:** 739  (▼3 d/d, ▼24 w/w, ▼421 m/m)
- **Risk Score:** 19  (▼1 d/d, ▼1 w/w, ▼15 m/m)
- **Response Time:** 549 ms  (▼6 d/d, ▼10 w/w, ▼204 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 270.7 | 99.67% |
| HDFC Bank | 88.9 | 99.42% |
| Bank of Baroda | 64.0 | 99.26% |
| Union Bank of India | 56.1 | 99.63% |
| Axis Bank | 51.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 397.2 | 99.51% | 198 ms |
| Google Pay | 271.9 | 99.35% | 241 ms |
| Paytm | 66.0 | 99.53% | 201 ms |
| Navi | 30.6 | 99.53% | 304 ms |
| SuperMoney | 16.2 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 307.7 |
| Person to Person | 295.2 |
| QR Payments | 79.0 |
| UPI Lite | 39.9 |
| UPI Autopay | 27.4 |

## Failure analysis
- No incidents open. Technical declines are within the 0.29% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D176-MON) and any meetings/emails on 29 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D176-MON, RPT-D175-DAILY
