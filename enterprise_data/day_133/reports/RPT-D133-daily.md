---
id: RPT-D133-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-17T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 17 May 2026)

**Report ID:** RPT-D133-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 17 May 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 133 of 206)

## Transaction summary
The rail processed 603.8M UPI transactions on Sunday — a quiet Sunday — up 17.1M on the same day last week. Success held at 99.98% and settlement at 98.97%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 603.8  (▼39.8 d/d, ▲17.1 w/w, ▼192.1 m/m)
- **Success Rate:** 99.98%  (▲0.39 w/w, ▲0.85 m/m)
- **Settlement Success:** 98.97%  (▼1.01 d/d, ▲0.16 w/w, ▼0.98 m/m)
- **Technical Declines:** 0.33%  (▼0.01 d/d, ▼0.01 w/w, ▼0.22 m/m)
- **Business Declines:** 0.17%  (▼0.01 d/d, ▼0.03 w/w, ▼0.07 m/m)
- **Customer Complaints:** 1,147  (▼2 d/d, ▼83 w/w, ▼995 m/m)
- **Merchant Complaints:** 119  (▼5 d/d, ▼37 w/w, ▼115 m/m)
- **Fraud Alerts:** 828  (▲4 d/d, ▼15 w/w, ▼332 m/m)
- **Risk Score:** 22  (▼1 w/w, ▼12 m/m)
- **Response Time:** 599 ms  (▼2 d/d, ▼10 w/w, ▼154 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 196.5 | 99.67% |
| HDFC Bank | 64.6 | 99.42% |
| Bank of Baroda | 46.5 | 99.26% |
| Union Bank of India | 40.7 | 99.63% |
| Axis Bank | 37.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 288.4 | 99.51% | 198 ms |
| Google Pay | 197.5 | 99.35% | 241 ms |
| Paytm | 47.9 | 99.53% | 201 ms |
| Navi | 22.2 | 99.53% | 304 ms |
| SuperMoney | 11.8 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 223.4 |
| Person to Person | 214.3 |
| QR Payments | 57.4 |
| UPI Lite | 29.0 |
| UPI Autopay | 19.9 |

## Failure analysis
- No incidents open. Technical declines are within the 0.33% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D133-MON) and any meetings/emails on 17 May.

Refs: upi_kpis_month.xlsx, TEAMS-D133-MON, RPT-D132-DAILY
