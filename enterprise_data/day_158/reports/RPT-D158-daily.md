---
id: RPT-D158-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-11T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 11 Jun 2026)

**Report ID:** RPT-D158-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 11 Jun 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 158 of 206)

## Transaction summary
The rail processed 736.1M UPI transactions on Thursday — a steady mid-week day — down 9.7M on the same day last week. Success held at 99.83% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 736.1  (▼182.5 d/d, ▼9.7 w/w, ▼59.8 m/m)
- **Success Rate:** 99.83%  (▲0.2 d/d, ▲0.62 w/w, ▲0.7 m/m)
- **Settlement Success:** 99.98%  (▲0.82 d/d, ▲0.48 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.3%  (▼0.01 d/d, ▼0.33 w/w, ▼0.25 m/m)
- **Business Declines:** 0.16%  (▼0.08 m/m)
- **Customer Complaints:** 1,017  (▼21 d/d, ▼778 w/w, ▼1125 m/m)
- **Merchant Complaints:** 104  (▼1 d/d, ▼122 w/w, ▼130 m/m)
- **Fraud Alerts:** 773  (▼7 d/d, ▼14 w/w, ▼387 m/m)
- **Risk Score:** 21  (▼13 m/m)
- **Response Time:** 571 ms  (▲5 d/d, ▼91 w/w, ▼182 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 239.6 | 99.67% |
| HDFC Bank | 78.7 | 99.42% |
| Bank of Baroda | 56.7 | 99.26% |
| Union Bank of India | 49.7 | 99.63% |
| Axis Bank | 45.4 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 351.6 | 99.51% | 198 ms |
| Google Pay | 240.7 | 99.35% | 241 ms |
| Paytm | 58.4 | 99.53% | 201 ms |
| Navi | 27.1 | 99.53% | 304 ms |
| SuperMoney | 14.4 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 272.4 |
| Person to Person | 261.3 |
| QR Payments | 69.9 |
| UPI Lite | 35.3 |
| UPI Autopay | 24.3 |

## Failure analysis
- No incidents open. Technical declines are within the 0.3% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D158-MON) and any meetings/emails on 11 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D158-MON, RPT-D157-DAILY
