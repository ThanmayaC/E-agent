---
id: RPT-D189-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-12T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 12 Jul 2026)

**Report ID:** RPT-D189-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 12 Jul 2026  ·  **Day archetype:** Sunday (quiet) · maintenance window
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 189 of 206)

## Transaction summary
The rail processed 615.9M UPI transactions on Sunday — a quiet Sunday with a scheduled maintenance window — down 4.8M on the same day last week. Success held at 99.98% and settlement at 99.52%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 615.9  (▼44.1 d/d, ▼4.8 w/w, ▼180.0 m/m)
- **Success Rate:** 99.98%  (▲0.18 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.52%  (▼0.46 d/d, ▼0.11 w/w, ▼0.43 m/m)
- **Technical Declines:** 0.27%  (▼0.01 d/d, ▼0.28 m/m)
- **Business Declines:** 0.15%  (▼0.09 m/m)
- **Customer Complaints:** 883  (▼29 d/d, ▼29 w/w, ▼1259 m/m)
- **Merchant Complaints:** 89  (▼3 w/w, ▼145 m/m)
- **Fraud Alerts:** 727  (▼4 w/w, ▼433 m/m)
- **Risk Score:** 19  (▼15 m/m)
- **Response Time:** 537 ms  (▼1 d/d, ▼11 w/w, ▼216 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 200.5 | 99.67% |
| HDFC Bank | 65.8 | 99.42% |
| Bank of Baroda | 47.4 | 99.26% |
| Union Bank of India | 41.5 | 99.63% |
| Axis Bank | 37.9 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 294.2 | 99.51% | 198 ms |
| Google Pay | 201.4 | 99.35% | 241 ms |
| Paytm | 48.9 | 99.53% | 201 ms |
| Navi | 22.6 | 99.53% | 304 ms |
| SuperMoney | 12.0 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 227.9 |
| Person to Person | 218.6 |
| QR Payments | 58.5 |
| UPI Lite | 29.6 |
| UPI Autopay | 20.3 |

## Failure analysis
- No incidents open. Technical declines are within the 0.27% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D189-MON) and any meetings/emails on 12 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D189-MON, RPT-D188-DAILY
