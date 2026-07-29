---
id: RPT-D123-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-07T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 07 May 2026)

**Report ID:** RPT-D123-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 07 May 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 123 of 206)

## Transaction summary
The rail processed 700.8M UPI transactions on Thursday — a steady mid-week day — down 86.1M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 700.8  (▼22.2 d/d, ▼86.1 w/w, ▼95.1 m/m)
- **Success Rate:** 99.98%  (▲0.28 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.98%  (▲1.09 d/d, ▲0.03 m/m)
- **Technical Declines:** 0.34%  (▼0.01 d/d, ▼0.01 w/w, ▼0.21 m/m)
- **Business Declines:** 0.18%  (▼0.06 m/m)
- **Customer Complaints:** 1,201  (▼2 d/d, ▼52 w/w, ▼941 m/m)
- **Merchant Complaints:** 126  (▲1 d/d, ▼4 w/w, ▼108 m/m)
- **Fraud Alerts:** 842  (▼1 d/d, ▼19 w/w, ▼318 m/m)
- **Risk Score:** 23  (▼1 w/w, ▼11 m/m)
- **Response Time:** 603 ms  (▼10 d/d, ▼13 w/w, ▼150 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 228.1 | 99.67% |
| HDFC Bank | 74.9 | 99.42% |
| Bank of Baroda | 53.9 | 99.26% |
| Union Bank of India | 47.3 | 99.63% |
| Axis Bank | 43.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 334.7 | 99.51% | 198 ms |
| Google Pay | 229.2 | 99.35% | 241 ms |
| Paytm | 55.6 | 99.53% | 201 ms |
| Navi | 25.8 | 99.53% | 304 ms |
| SuperMoney | 13.7 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 259.3 |
| Person to Person | 248.8 |
| QR Payments | 66.6 |
| UPI Lite | 33.6 |
| UPI Autopay | 23.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.34% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D123-MON) and any meetings/emails on 07 May.

Refs: upi_kpis_month.xlsx, TEAMS-D123-MON, RPT-D122-DAILY
