---
id: RPT-D45-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-18T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 18 Feb 2026)

**Report ID:** RPT-D45-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 18 Feb 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 45 of 206)

## Transaction summary
The rail processed 683.2M UPI transactions on Wednesday — a steady mid-week day — up 0.5M on the same day last week. Success held at 99.41% and settlement at 99.89%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 683.2  (▼2.6 d/d, ▲0.5 w/w, ▼112.7 m/m)
- **Success Rate:** 99.41%  (▼0.57 d/d, ▲0.17 w/w, ▲0.28 m/m)
- **Settlement Success:** 99.89%  (▼0.09 d/d, ▲0.37 w/w, ▼0.06 m/m)
- **Technical Declines:** 0.47%  (▼0.01 w/w, ▼0.08 m/m)
- **Business Declines:** 0.22%  (▼0.01 w/w, ▼0.02 m/m)
- **Customer Complaints:** 1,761  (▼10 d/d, ▼71 w/w, ▼381 m/m)
- **Merchant Complaints:** 187  (▼6 w/w, ▼47 m/m)
- **Fraud Alerts:** 1,032  (▼1 d/d, ▼26 w/w, ▼128 m/m)
- **Risk Score:** 29  (▼1 d/d, ▼3 w/w, ▼5 m/m)
- **Response Time:** 700 ms  (▲4 d/d, ▼12 w/w, ▼53 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 222.4 | 99.67% |
| HDFC Bank | 73.0 | 99.42% |
| Bank of Baroda | 52.6 | 99.26% |
| Union Bank of India | 46.1 | 99.63% |
| Axis Bank | 42.1 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 326.3 | 99.51% | 198 ms |
| Google Pay | 223.4 | 99.35% | 241 ms |
| Paytm | 54.2 | 99.53% | 201 ms |
| Navi | 25.1 | 99.53% | 304 ms |
| SuperMoney | 13.3 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 252.8 |
| Person to Person | 242.5 |
| QR Payments | 64.9 |
| UPI Lite | 32.8 |
| UPI Autopay | 22.5 |

## Failure analysis
- No incidents open. Technical declines are within the 0.47% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D45-MON) and any meetings/emails on 18 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D45-MON, RPT-D44-DAILY
