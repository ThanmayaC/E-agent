---
id: RPT-D177-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-30T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 30 Jun 2026)

**Report ID:** RPT-D177-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 30 Jun 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 177 of 206)

## Transaction summary
The rail processed 831.5M UPI transactions on Tuesday — the month-end surge as salary and bill-pay flows land — up 87.8M on the same day last week. Success held at 99.62% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 831.5  (▲87.8 w/w, ▲35.6 m/m)
- **Success Rate:** 99.62%  (▲0.07 d/d, ▲0.67 w/w, ▲0.49 m/m)
- **Settlement Success:** 99.98%  (▲0.83 d/d, ▲0.22 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.28%  (▼0.01 d/d, ▼0.01 w/w, ▼0.27 m/m)
- **Business Declines:** 0.16%  (▼0.08 m/m)
- **Customer Complaints:** 931  (▼17 d/d, ▼39 w/w, ▼1211 m/m)
- **Merchant Complaints:** 93  (▼1 d/d, ▼5 w/w, ▼141 m/m)
- **Fraud Alerts:** 742  (▲3 d/d, ▼15 w/w, ▼418 m/m)
- **Risk Score:** 20  (▲1 d/d, ▼14 m/m)
- **Response Time:** 549 ms  (▼6 w/w, ▼204 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 270.7 | 99.67% |
| HDFC Bank | 88.9 | 99.42% |
| Bank of Baroda | 64.0 | 99.26% |
| Union Bank of India | 56.1 | 99.63% |
| Axis Bank | 51.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 397.2 | 99.51% | 198 ms |
| Google Pay | 271.9 | 99.35% | 241 ms |
| Paytm | 66.0 | 99.53% | 201 ms |
| Navi | 30.6 | 99.53% | 304 ms |
| SuperMoney | 16.2 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 307.7 |
| Person to Person | 295.2 |
| QR Payments | 79.0 |
| UPI Lite | 39.9 |
| UPI Autopay | 27.4 |

## Failure analysis
- No incidents open. Technical declines are within the 0.28% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D177-MON) and any meetings/emails on 30 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D177-MON, RPT-D176-DAILY
