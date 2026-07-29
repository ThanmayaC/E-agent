---
id: RPT-D157-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-10T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 10 Jun 2026)

**Report ID:** RPT-D157-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 10 Jun 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 157 of 206)

## Transaction summary
The rail processed 918.6M UPI transactions on Wednesday — a campaign-driven high-volume day — up 178.4M on the same day last week. Success held at 99.63% and settlement at 99.16%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 918.6  (▲183.4 d/d, ▲178.4 w/w, ▲122.7 m/m)
- **Success Rate:** 99.63%  (▼0.35 d/d, ▲0.22 w/w, ▲0.5 m/m)
- **Settlement Success:** 99.16%  (▼0.79 d/d, ▲0.22 w/w, ▼0.79 m/m)
- **Technical Declines:** 0.31%  (▼0.24 m/m)
- **Business Declines:** 0.16%  (▼0.01 w/w, ▼0.08 m/m)
- **Customer Complaints:** 1,038  (▼1 d/d, ▼32 w/w, ▼1104 m/m)
- **Merchant Complaints:** 105  (▼4 w/w, ▼129 m/m)
- **Fraud Alerts:** 780  (▼13 w/w, ▼380 m/m)
- **Risk Score:** 21  (▼13 m/m)
- **Response Time:** 566 ms  (▼10 d/d, ▼6 w/w, ▼187 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 299.0 | 99.67% |
| HDFC Bank | 98.2 | 99.42% |
| Bank of Baroda | 70.7 | 99.26% |
| Union Bank of India | 62.0 | 99.63% |
| Axis Bank | 56.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 438.8 | 99.51% | 198 ms |
| Google Pay | 300.4 | 99.35% | 241 ms |
| Paytm | 72.9 | 99.53% | 201 ms |
| Navi | 33.8 | 99.53% | 304 ms |
| SuperMoney | 17.9 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 339.9 |
| Person to Person | 326.1 |
| QR Payments | 87.3 |
| UPI Lite | 44.1 |
| UPI Autopay | 30.3 |

## Failure analysis
- No incidents open. Technical declines are within the 0.31% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D157-MON) and any meetings/emails on 10 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D157-MON, RPT-D156-DAILY
