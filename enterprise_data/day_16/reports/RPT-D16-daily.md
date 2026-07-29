---
id: RPT-D16-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-20T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 20 Jan 2026)

**Report ID:** RPT-D16-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 20 Jan 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 16 of 206)

## Transaction summary
The rail processed 669.2M UPI transactions on Tuesday — a steady mid-week day — up 14.5M on the same day last week. Success held at 99.36% and settlement at 99.87%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 669.2  (▲26.0 d/d, ▲14.5 w/w, ▼126.7 m/m)
- **Success Rate:** 99.36%  (▲0.58 d/d, ▼0.6 w/w, ▲0.23 m/m)
- **Settlement Success:** 99.87%  (▲0.39 d/d, ▲0.1 w/w, ▼0.08 m/m)
- **Technical Declines:** 0.52%  (▼0.02 w/w, ▼0.03 m/m)
- **Business Declines:** 0.23%  (▼0.01 w/w, ▼0.01 m/m)
- **Customer Complaints:** 2,018  (▼14 d/d, ▼36 w/w, ▼124 m/m)
- **Merchant Complaints:** 219  (▼1 d/d, ▼6 w/w, ▼15 m/m)
- **Fraud Alerts:** 1,111  (▲8 d/d, ▼16 w/w, ▼49 m/m)
- **Risk Score:** 32  (▼1 d/d, ▼1 w/w, ▼2 m/m)
- **Response Time:** 745 ms  (▲4 d/d, ▼3 w/w, ▼8 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 217.8 | 99.67% |
| HDFC Bank | 71.5 | 99.42% |
| Bank of Baroda | 51.5 | 99.26% |
| Union Bank of India | 45.1 | 99.63% |
| Axis Bank | 41.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 319.6 | 99.51% | 198 ms |
| Google Pay | 218.9 | 99.35% | 241 ms |
| Paytm | 53.1 | 99.53% | 201 ms |
| Navi | 24.6 | 99.53% | 304 ms |
| SuperMoney | 13.0 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 247.6 |
| Person to Person | 237.6 |
| QR Payments | 63.6 |
| UPI Lite | 32.1 |
| UPI Autopay | 22.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.52% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D16-MON) and any meetings/emails on 20 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D16-MON, RPT-D15-DAILY
