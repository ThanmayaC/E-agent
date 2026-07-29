---
id: RPT-D205-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-28T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 28 Jul 2026)

**Report ID:** RPT-D205-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 28 Jul 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 205 of 206)

## Transaction summary
The rail processed 926.3M UPI transactions on Tuesday — a campaign-driven high-volume day — up 157.6M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 926.3  (▲176.4 d/d, ▲157.6 w/w, ▲130.4 m/m)
- **Success Rate:** 99.98%  (▲0.58 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.98%  (▲0.03 m/m)
- **Technical Declines:** 0.25%  (▼0.01 d/d, ▼0.01 w/w, ▼0.3 m/m)
- **Business Declines:** 0.14%  (▼0.01 d/d, ▼0.01 w/w, ▼0.1 m/m)
- **Customer Complaints:** 827  (▼6 d/d, ▼19 w/w, ▼1315 m/m)
- **Merchant Complaints:** 82  (▼3 w/w, ▼152 m/m)
- **Fraud Alerts:** 687  (▼11 d/d, ▼11 w/w, ▼473 m/m)
- **Risk Score:** 18  (▼16 m/m)
- **Response Time:** 523 ms  (▲1 d/d, ▼4 w/w, ▼230 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 301.5 | 99.67% |
| HDFC Bank | 99.0 | 99.42% |
| Bank of Baroda | 71.3 | 99.26% |
| Union Bank of India | 62.5 | 99.63% |
| Axis Bank | 57.1 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 442.5 | 99.51% | 198 ms |
| Google Pay | 302.9 | 99.35% | 241 ms |
| Paytm | 73.5 | 99.53% | 201 ms |
| Navi | 34.1 | 99.53% | 304 ms |
| SuperMoney | 18.1 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 342.7 |
| Person to Person | 328.8 |
| QR Payments | 88.0 |
| UPI Lite | 44.5 |
| UPI Autopay | 30.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.25% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D205-MON) and any meetings/emails on 28 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D205-MON, RPT-D204-DAILY
