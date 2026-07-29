---
id: RPT-D96-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-10T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 10 Apr 2026)

**Report ID:** RPT-D96-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 10 Apr 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 96 of 206)

## Transaction summary
The rail processed 702.6M UPI transactions on Friday — a steady mid-week day — down 155.5M on the same day last week. Success held at 99.02% and settlement at 99.21%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 702.6  (▼2.3 d/d, ▼155.5 w/w, ▼93.3 m/m)
- **Success Rate:** 99.02%  (▲0.45 d/d, ▼0.55 w/w, ▼0.11 m/m)
- **Settlement Success:** 99.21%  (▼0.77 d/d, ▼0.77 w/w, ▼0.74 m/m)
- **Technical Declines:** 0.38%  (▼0.07 d/d, ▼0.01 w/w, ▼0.17 m/m)
- **Business Declines:** 0.19%  (▼0.05 m/m)
- **Customer Complaints:** 1,360  (▼178 d/d, ▼63 w/w, ▼782 m/m)
- **Merchant Complaints:** 143  (▼27 d/d, ▼7 w/w, ▼91 m/m)
- **Fraud Alerts:** 908  (▲3 d/d, ▼16 w/w, ▼252 m/m)
- **Risk Score:** 25  (▼1 w/w, ▼9 m/m)
- **Response Time:** 639 ms  (▼11 d/d, ▼3 w/w, ▼114 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 228.7 | 99.67% |
| HDFC Bank | 75.1 | 99.42% |
| Bank of Baroda | 54.1 | 99.26% |
| Union Bank of India | 47.4 | 99.63% |
| Axis Bank | 43.3 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 335.6 | 99.51% | 198 ms |
| Google Pay | 229.8 | 99.35% | 241 ms |
| Paytm | 55.7 | 99.53% | 201 ms |
| Navi | 25.8 | 99.53% | 304 ms |
| SuperMoney | 13.7 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 260.0 |
| Person to Person | 249.4 |
| QR Payments | 66.7 |
| UPI Lite | 33.7 |
| UPI Autopay | 23.2 |

## Failure analysis
- No incidents open. Technical declines are within the 0.38% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D96-MON) and any meetings/emails on 10 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D96-MON, RPT-D95-DAILY
