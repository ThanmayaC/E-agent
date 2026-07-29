---
id: RPT-D156-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-09T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 09 Jun 2026)

**Report ID:** RPT-D156-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 09 Jun 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 156 of 206)

## Transaction summary
The rail processed 735.2M UPI transactions on Tuesday — a steady mid-week day — down 1.1M on the same day last week. Success held at 99.98% and settlement at 99.95%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 735.2  (▲35.3 d/d, ▼1.1 w/w, ▼60.7 m/m)
- **Success Rate:** 99.98%  (▲0.2 d/d, ▲0.25 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.95%  (▲0.44 d/d, ▲0.54 w/w)
- **Technical Declines:** 0.31%  (▲0.01 d/d, ▼0.24 m/m)
- **Business Declines:** 0.16%  (▼0.01 w/w, ▼0.08 m/m)
- **Customer Complaints:** 1,039  (▲3 d/d, ▼22 w/w, ▼1103 m/m)
- **Merchant Complaints:** 105  (▼1 d/d, ▼5 w/w, ▼129 m/m)
- **Fraud Alerts:** 780  (▼18 w/w, ▼380 m/m)
- **Risk Score:** 21  (▼13 m/m)
- **Response Time:** 576 ms  (▲3 d/d, ▼3 w/w, ▼177 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 239.3 | 99.67% |
| HDFC Bank | 78.6 | 99.42% |
| Bank of Baroda | 56.6 | 99.26% |
| Union Bank of India | 49.6 | 99.63% |
| Axis Bank | 45.3 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 351.2 | 99.51% | 198 ms |
| Google Pay | 240.4 | 99.35% | 241 ms |
| Paytm | 58.3 | 99.53% | 201 ms |
| Navi | 27.0 | 99.53% | 304 ms |
| SuperMoney | 14.3 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 272.0 |
| Person to Person | 261.0 |
| QR Payments | 69.8 |
| UPI Lite | 35.3 |
| UPI Autopay | 24.3 |

## Failure analysis
- No incidents open. Technical declines are within the 0.31% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D156-MON) and any meetings/emails on 09 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D156-MON, RPT-D155-DAILY
