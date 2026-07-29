---
id: RPT-D175-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-28T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 28 Jun 2026)

**Report ID:** RPT-D175-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 28 Jun 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 175 of 206)

## Transaction summary
The rail processed 844.6M UPI transactions on Sunday — the month-end surge as salary and bill-pay flows land — up 246.9M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 844.6  (▲183.9 d/d, ▲246.9 w/w, ▲48.7 m/m)
- **Success Rate:** 99.98%  (▲1.02 d/d, ▲0.85 m/m)
- **Settlement Success:** 99.98%  (▲0.31 d/d, ▲0.21 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.28%  (▼0.01 w/w, ▼0.27 m/m)
- **Business Declines:** 0.16%  (▼0.08 m/m)
- **Customer Complaints:** 949  (▲7 d/d, ▼34 w/w, ▼1193 m/m)
- **Merchant Complaints:** 94  (▼1 d/d, ▼5 w/w, ▼140 m/m)
- **Fraud Alerts:** 742  (▲2 d/d, ▼10 w/w, ▼418 m/m)
- **Risk Score:** 20  (▼14 m/m)
- **Response Time:** 555 ms  (▲4 d/d, ▼7 w/w, ▼198 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 274.9 | 99.67% |
| HDFC Bank | 90.3 | 99.42% |
| Bank of Baroda | 65.0 | 99.26% |
| Union Bank of India | 57.0 | 99.63% |
| Axis Bank | 52.0 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 403.4 | 99.51% | 198 ms |
| Google Pay | 276.2 | 99.35% | 241 ms |
| Paytm | 67.0 | 99.53% | 201 ms |
| Navi | 31.1 | 99.53% | 304 ms |
| SuperMoney | 16.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 312.5 |
| Person to Person | 299.8 |
| QR Payments | 80.2 |
| UPI Lite | 40.5 |
| UPI Autopay | 27.9 |

## Failure analysis
- No incidents open. Technical declines are within the 0.28% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D175-MON) and any meetings/emails on 28 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D175-MON, RPT-D174-DAILY
