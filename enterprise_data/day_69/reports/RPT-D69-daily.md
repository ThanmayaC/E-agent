---
id: RPT-D69-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-14T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 14 Mar 2026)

**Report ID:** RPT-D69-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 14 Mar 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 69 of 206)

## Transaction summary
The rail processed 627.8M UPI transactions on Saturday — a lighter Saturday — up 1.3M on the same day last week. Success held at 99.98% and settlement at 99.63%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 627.8  (▼56.6 d/d, ▲1.3 w/w, ▼168.1 m/m)
- **Success Rate:** 99.98%  (▲0.01 d/d, ▲0.09 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.63%  (▲0.81 d/d, ▲1.36 w/w, ▼0.32 m/m)
- **Technical Declines:** 0.42%  (▼0.01 d/d, ▼0.01 w/w, ▼0.13 m/m)
- **Business Declines:** 0.2%  (▼0.04 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,549  (▼11 d/d, ▼195 w/w, ▼593 m/m)
- **Merchant Complaints:** 166  (▲1 d/d, ▼87 w/w, ▼68 m/m)
- **Fraud Alerts:** 978  (▲14 d/d, ▼13 w/w, ▼182 m/m)
- **Risk Score:** 28  (▼6 m/m)
- **Response Time:** 667 ms  (▲2 d/d, ▼7 w/w, ▼86 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 204.3 | 99.67% |
| HDFC Bank | 67.1 | 99.42% |
| Bank of Baroda | 48.3 | 99.26% |
| Union Bank of India | 42.4 | 99.63% |
| Axis Bank | 38.7 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 299.9 | 99.51% | 198 ms |
| Google Pay | 205.3 | 99.35% | 241 ms |
| Paytm | 49.8 | 99.53% | 201 ms |
| Navi | 23.1 | 99.53% | 304 ms |
| SuperMoney | 12.2 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 232.3 |
| Person to Person | 222.9 |
| QR Payments | 59.6 |
| UPI Lite | 30.1 |
| UPI Autopay | 20.7 |

## Failure analysis
- No incidents open. Technical declines are within the 0.42% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D69-MON) and any meetings/emails on 14 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D69-MON, RPT-D68-DAILY
