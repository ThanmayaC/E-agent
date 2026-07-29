---
id: RPT-D192-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-15T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 15 Jul 2026)

**Report ID:** RPT-D192-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 15 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 192 of 206)

## Transaction summary
The rail processed 762.4M UPI transactions on Wednesday — a steady mid-week day — up 19.6M on the same day last week. Success held at 99.54% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 762.4  (▲18.8 d/d, ▲19.6 w/w, ▼33.5 m/m)
- **Success Rate:** 99.54%  (▲0.35 d/d, ▲0.53 w/w, ▲0.41 m/m)
- **Settlement Success:** 99.98%  (▲0.31 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.27%  (▼0.08 w/w, ▼0.28 m/m)
- **Business Declines:** 0.15%  (▼0.09 m/m)
- **Customer Complaints:** 874  (▼195 w/w, ▼1268 m/m)
- **Merchant Complaints:** 88  (▲1 d/d, ▼3 w/w, ▼146 m/m)
- **Fraud Alerts:** 709  (▼4 d/d, ▼20 w/w, ▼451 m/m)
- **Risk Score:** 19  (▼15 m/m)
- **Response Time:** 530 ms  (▼9 d/d, ▼29 w/w, ▼223 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 248.2 | 99.67% |
| HDFC Bank | 81.5 | 99.42% |
| Bank of Baroda | 58.7 | 99.26% |
| Union Bank of India | 51.4 | 99.63% |
| Axis Bank | 47.0 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 364.2 | 99.51% | 198 ms |
| Google Pay | 249.3 | 99.35% | 241 ms |
| Paytm | 60.5 | 99.53% | 201 ms |
| Navi | 28.0 | 99.53% | 304 ms |
| SuperMoney | 14.9 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 282.1 |
| Person to Person | 270.7 |
| QR Payments | 72.4 |
| UPI Lite | 36.6 |
| UPI Autopay | 25.2 |

## Failure analysis
- No incidents open. Technical declines are within the 0.27% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D192-MON) and any meetings/emails on 15 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D192-MON, RPT-D191-DAILY
