---
id: RPT-D165-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-18T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 18 Jun 2026)

**Report ID:** RPT-D165-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 18 Jun 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 165 of 206)

## Transaction summary
The rail processed 737.4M UPI transactions on Thursday — a steady mid-week day — up 1.3M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 737.4  (▼14.0 d/d, ▲1.3 w/w, ▼58.5 m/m)
- **Success Rate:** 99.98%  (▲0.62 d/d, ▲0.15 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.98%  (▲0.28 d/d, ▲0.03 m/m)
- **Technical Declines:** 0.3%  (▼0.25 m/m)
- **Business Declines:** 0.16%  (▼0.08 m/m)
- **Customer Complaints:** 987  (▼9 d/d, ▼30 w/w, ▼1155 m/m)
- **Merchant Complaints:** 100  (▼1 d/d, ▼4 w/w, ▼134 m/m)
- **Fraud Alerts:** 762  (▼6 d/d, ▼11 w/w, ▼398 m/m)
- **Risk Score:** 20  (▼1 w/w, ▼14 m/m)
- **Response Time:** 561 ms  (▲4 d/d, ▼10 w/w, ▼192 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 240.0 | 99.67% |
| HDFC Bank | 78.8 | 99.42% |
| Bank of Baroda | 56.8 | 99.26% |
| Union Bank of India | 49.7 | 99.63% |
| Axis Bank | 45.4 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 352.2 | 99.51% | 198 ms |
| Google Pay | 241.2 | 99.35% | 241 ms |
| Paytm | 58.5 | 99.53% | 201 ms |
| Navi | 27.1 | 99.53% | 304 ms |
| SuperMoney | 14.4 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 272.8 |
| Person to Person | 261.8 |
| QR Payments | 70.1 |
| UPI Lite | 35.4 |
| UPI Autopay | 24.3 |

## Failure analysis
- No incidents open. Technical declines are within the 0.3% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D165-MON) and any meetings/emails on 18 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D165-MON, RPT-D164-DAILY
