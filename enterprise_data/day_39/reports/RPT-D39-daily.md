---
id: RPT-D39-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-12T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 12 Feb 2026)

**Report ID:** RPT-D39-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 12 Feb 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 39 of 206)

## Transaction summary
The rail processed 684.6M UPI transactions on Thursday — a steady mid-week day — down 0.9M on the same day last week. Success held at 98.96% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 684.6  (▲1.9 d/d, ▼0.9 w/w, ▼111.3 m/m)
- **Success Rate:** 98.96%  (▼0.28 d/d, ▼1.02 w/w, ▼0.17 m/m)
- **Settlement Success:** 99.98%  (▲0.46 d/d, ▲0.03 m/m)
- **Technical Declines:** 0.48%  (▼0.01 w/w, ▼0.07 m/m)
- **Business Declines:** 0.22%  (▼0.01 d/d, ▼0.11 w/w, ▼0.02 m/m)
- **Customer Complaints:** 1,790  (▼42 d/d, ▼462 w/w, ▼352 m/m)
- **Merchant Complaints:** 192  (▼1 d/d, ▼6 w/w, ▼42 m/m)
- **Fraud Alerts:** 1,050  (▼8 d/d, ▼247 w/w, ▼110 m/m)
- **Risk Score:** 30  (▼2 d/d, ▼17 w/w, ▼4 m/m)
- **Response Time:** 710 ms  (▼2 d/d, ▼10 w/w, ▼43 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 222.8 | 99.67% |
| HDFC Bank | 73.2 | 99.42% |
| Bank of Baroda | 52.7 | 99.26% |
| Union Bank of India | 46.2 | 99.63% |
| Axis Bank | 42.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 327.0 | 99.51% | 198 ms |
| Google Pay | 223.9 | 99.35% | 241 ms |
| Paytm | 54.3 | 99.53% | 201 ms |
| Navi | 25.2 | 99.53% | 304 ms |
| SuperMoney | 13.3 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 253.3 |
| Person to Person | 243.0 |
| QR Payments | 65.0 |
| UPI Lite | 32.9 |
| UPI Autopay | 22.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.48% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D39-MON) and any meetings/emails on 12 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D39-MON, RPT-D38-DAILY
