---
id: RPT-D180-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-03T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 03 Jul 2026)

**Report ID:** RPT-D180-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 03 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 180 of 206)

## Transaction summary
The rail processed 746.7M UPI transactions on Friday — a steady mid-week day — down 3.7M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 746.7  (▲16.8 d/d, ▼3.7 w/w, ▼49.2 m/m)
- **Success Rate:** 99.98%  (▲0.54 d/d, ▲0.85 m/m)
- **Settlement Success:** 99.98%  (▲0.03 m/m)
- **Technical Declines:** 0.28%  (▼0.01 w/w, ▼0.27 m/m)
- **Business Declines:** 0.15%  (▼0.01 w/w, ▼0.09 m/m)
- **Customer Complaints:** 921  (▼12 d/d, ▼30 w/w, ▼1221 m/m)
- **Merchant Complaints:** 94  (▼3 w/w, ▼140 m/m)
- **Fraud Alerts:** 737  (▲3 d/d, ▼8 w/w, ▼423 m/m)
- **Risk Score:** 19  (▼1 w/w, ▼15 m/m)
- **Response Time:** 548 ms  (▲4 d/d, ▼4 w/w, ▼205 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 243.1 | 99.67% |
| HDFC Bank | 79.8 | 99.42% |
| Bank of Baroda | 57.5 | 99.26% |
| Union Bank of India | 50.4 | 99.63% |
| Axis Bank | 46.0 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 356.7 | 99.51% | 198 ms |
| Google Pay | 244.2 | 99.35% | 241 ms |
| Paytm | 59.2 | 99.53% | 201 ms |
| Navi | 27.5 | 99.53% | 304 ms |
| SuperMoney | 14.6 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 276.3 |
| Person to Person | 265.1 |
| QR Payments | 70.9 |
| UPI Lite | 35.8 |
| UPI Autopay | 24.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.28% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D180-MON) and any meetings/emails on 03 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D180-MON, RPT-D179-DAILY
