---
id: RPT-D99-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-13T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 13 Apr 2026)

**Report ID:** RPT-D99-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 13 Apr 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 99 of 206)

## Transaction summary
The rail processed 687.4M UPI transactions on Monday — the Monday ramp-up after the weekend — down 9.1M on the same day last week. Success held at 99.98% and settlement at 99.69%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 687.4  (▲123.6 d/d, ▼9.1 w/w, ▼108.5 m/m)
- **Success Rate:** 99.98%  (▲1.33 d/d, ▲1.81 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.69%  (▲0.09 d/d, ▲0.36 w/w, ▼0.26 m/m)
- **Technical Declines:** 0.38%  (▼0.42 w/w, ▼0.17 m/m)
- **Business Declines:** 0.19%  (▼0.05 m/m)
- **Customer Complaints:** 1,348  (▼7 d/d, ▼1017 w/w, ▼794 m/m)
- **Merchant Complaints:** 141  (▼1 d/d, ▼167 w/w, ▼93 m/m)
- **Fraud Alerts:** 909  (▲7 d/d, ▼6 w/w, ▼251 m/m)
- **Risk Score:** 25  (▼1 w/w, ▼9 m/m)
- **Response Time:** 633 ms  (▼5 d/d, ▼118 w/w, ▼120 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 223.7 | 99.67% |
| HDFC Bank | 73.5 | 99.42% |
| Bank of Baroda | 52.9 | 99.26% |
| Union Bank of India | 46.4 | 99.63% |
| Axis Bank | 42.4 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 328.3 | 99.51% | 198 ms |
| Google Pay | 224.8 | 99.35% | 241 ms |
| Paytm | 54.5 | 99.53% | 201 ms |
| Navi | 25.3 | 99.53% | 304 ms |
| SuperMoney | 13.4 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 254.3 |
| Person to Person | 244.0 |
| QR Payments | 65.3 |
| UPI Lite | 33.0 |
| UPI Autopay | 22.7 |

## Failure analysis
- No incidents open. Technical declines are within the 0.38% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D99-MON) and any meetings/emails on 13 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D99-MON, RPT-D98-DAILY
