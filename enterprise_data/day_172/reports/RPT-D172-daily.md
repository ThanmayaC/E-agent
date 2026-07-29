---
id: RPT-D172-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-25T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 25 Jun 2026)

**Report ID:** RPT-D172-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 25 Jun 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 172 of 206)

## Transaction summary
The rail processed 892.3M UPI transactions on Thursday — a campaign-driven high-volume day — up 154.9M on the same day last week. Success held at 98.89% and settlement at 98.99%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 892.3  (▲166.0 d/d, ▲154.9 w/w, ▲96.4 m/m)
- **Success Rate:** 98.89%  (▼1.09 d/d, ▼1.09 w/w, ▼0.24 m/m)
- **Settlement Success:** 98.99%  (▼0.99 d/d, ▼0.99 w/w, ▼0.96 m/m)
- **Technical Declines:** 0.29%  (▼0.01 w/w, ▼0.26 m/m)
- **Business Declines:** 0.16%  (▼0.08 m/m)
- **Customer Complaints:** 953  (▼17 d/d, ▼34 w/w, ▼1189 m/m)
- **Merchant Complaints:** 97  (▼1 d/d, ▼3 w/w, ▼137 m/m)
- **Fraud Alerts:** 756  (▲9 d/d, ▼6 w/w, ▼404 m/m)
- **Risk Score:** 20  (▼14 m/m)
- **Response Time:** 556 ms  (▼2 d/d, ▼5 w/w, ▼197 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 290.4 | 99.67% |
| HDFC Bank | 95.4 | 99.42% |
| Bank of Baroda | 68.7 | 99.26% |
| Union Bank of India | 60.2 | 99.63% |
| Axis Bank | 55.0 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 426.2 | 99.51% | 198 ms |
| Google Pay | 291.8 | 99.35% | 241 ms |
| Paytm | 70.8 | 99.53% | 201 ms |
| Navi | 32.8 | 99.53% | 304 ms |
| SuperMoney | 17.4 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 330.2 |
| Person to Person | 316.8 |
| QR Payments | 84.8 |
| UPI Lite | 42.8 |
| UPI Autopay | 29.4 |

## Failure analysis
- No incidents open. Technical declines are within the 0.29% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D172-MON) and any meetings/emails on 25 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D172-MON, RPT-D171-DAILY
