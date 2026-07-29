---
id: RPT-D200-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-23T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 23 Jul 2026)

**Report ID:** RPT-D200-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 23 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 200 of 206)

## Transaction summary
The rail processed 747.1M UPI transactions on Thursday — a steady mid-week day — up 0.4M on the same day last week. Success held at 99.31% and settlement at 99.54%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 747.1  (▼9.3 d/d, ▲0.4 w/w, ▼48.8 m/m)
- **Success Rate:** 99.31%  (▼0.67 d/d, ▼0.24 w/w, ▲0.18 m/m)
- **Settlement Success:** 99.54%  (▲0.34 d/d, ▲0.01 w/w, ▼0.41 m/m)
- **Technical Declines:** 0.26%  (▼0.29 m/m)
- **Business Declines:** 0.15%  (▼0.09 m/m)
- **Customer Complaints:** 837  (▼11 d/d, ▼28 w/w, ▼1305 m/m)
- **Merchant Complaints:** 83  (▼1 d/d, ▼4 w/w, ▼151 m/m)
- **Fraud Alerts:** 703  (▼14 w/w, ▼457 m/m)
- **Risk Score:** 18  (▼1 w/w, ▼16 m/m)
- **Response Time:** 525 ms  (▼4 d/d, ▼12 w/w, ▼228 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 243.2 | 99.67% |
| HDFC Bank | 79.9 | 99.42% |
| Bank of Baroda | 57.5 | 99.26% |
| Union Bank of India | 50.4 | 99.63% |
| Axis Bank | 46.0 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 356.9 | 99.51% | 198 ms |
| Google Pay | 244.3 | 99.35% | 241 ms |
| Paytm | 59.3 | 99.53% | 201 ms |
| Navi | 27.5 | 99.53% | 304 ms |
| SuperMoney | 14.6 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 276.4 |
| Person to Person | 265.2 |
| QR Payments | 71.0 |
| UPI Lite | 35.9 |
| UPI Autopay | 24.7 |

## Failure analysis
- No incidents open. Technical declines are within the 0.26% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D200-MON) and any meetings/emails on 23 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D200-MON, RPT-D199-DAILY
