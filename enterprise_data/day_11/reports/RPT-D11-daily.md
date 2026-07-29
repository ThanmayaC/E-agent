---
id: RPT-D11-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-15T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 15 Jan 2026)

**Report ID:** RPT-D11-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 15 Jan 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 11 of 206)

## Transaction summary
The rail processed 654.0M UPI transactions on Thursday — a steady mid-week day — up 10.9M on the same day last week. Success held at 98.99% and settlement at 99.6%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 654.0  (▼25.0 d/d, ▲10.9 w/w, ▼141.9 m/m)
- **Success Rate:** 98.99%  (▲0.73 d/d, ▼0.99 w/w, ▼0.14 m/m)
- **Settlement Success:** 99.6%  (▲0.75 d/d, ▼0.38 w/w, ▼0.35 m/m)
- **Technical Declines:** 0.53%  (▼0.02 w/w, ▼0.02 m/m)
- **Business Declines:** 0.24%
- **Customer Complaints:** 2,058  (▼21 d/d, ▼73 w/w, ▼84 m/m)
- **Merchant Complaints:** 223  (▼2 d/d, ▼8 w/w, ▼11 m/m)
- **Fraud Alerts:** 1,129  (▲15 d/d, ▼6 w/w, ▼31 m/m)
- **Risk Score:** 33  (▼1 w/w, ▼1 m/m)
- **Response Time:** 742 ms  (▼7 d/d, ▼8 w/w, ▼11 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 212.9 | 99.67% |
| HDFC Bank | 69.9 | 99.42% |
| Bank of Baroda | 50.3 | 99.26% |
| Union Bank of India | 44.1 | 99.63% |
| Axis Bank | 40.3 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 312.4 | 99.51% | 198 ms |
| Google Pay | 213.9 | 99.35% | 241 ms |
| Paytm | 51.9 | 99.53% | 201 ms |
| Navi | 24.0 | 99.53% | 304 ms |
| SuperMoney | 12.8 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 242.0 |
| Person to Person | 232.2 |
| QR Payments | 62.1 |
| UPI Lite | 31.4 |
| UPI Autopay | 21.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.53% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D11-MON) and any meetings/emails on 15 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D11-MON, RPT-D10-DAILY
