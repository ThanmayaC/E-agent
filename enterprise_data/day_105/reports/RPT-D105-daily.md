---
id: RPT-D105-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-19T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 19 Apr 2026)

**Report ID:** RPT-D105-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 19 Apr 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 105 of 206)

## Transaction summary
The rail processed 589.6M UPI transactions on Sunday — a quiet Sunday — up 25.8M on the same day last week. Success held at 99.41% and settlement at 98.78%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 589.6  (▼50.8 d/d, ▲25.8 w/w, ▼206.3 m/m)
- **Success Rate:** 99.41%  (▲0.27 d/d, ▲0.76 w/w, ▲0.28 m/m)
- **Settlement Success:** 98.78%  (▼0.47 d/d, ▼0.82 w/w, ▼1.17 m/m)
- **Technical Declines:** 0.37%  (▼0.01 w/w, ▼0.18 m/m)
- **Business Declines:** 0.18%  (▼0.01 d/d, ▼0.01 w/w, ▼0.06 m/m)
- **Customer Complaints:** 1,305  (▼15 d/d, ▼50 w/w, ▼837 m/m)
- **Merchant Complaints:** 138  (▼4 w/w, ▼96 m/m)
- **Fraud Alerts:** 892  (▲4 d/d, ▼10 w/w, ▼268 m/m)
- **Risk Score:** 24  (▼1 d/d, ▼1 w/w, ▼10 m/m)
- **Response Time:** 625 ms  (▼4 d/d, ▼13 w/w, ▼128 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 191.9 | 99.67% |
| HDFC Bank | 63.0 | 99.42% |
| Bank of Baroda | 45.4 | 99.26% |
| Union Bank of India | 39.8 | 99.63% |
| Axis Bank | 36.3 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 281.6 | 99.51% | 198 ms |
| Google Pay | 192.8 | 99.35% | 241 ms |
| Paytm | 46.8 | 99.53% | 201 ms |
| Navi | 21.7 | 99.53% | 304 ms |
| SuperMoney | 11.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 218.2 |
| Person to Person | 209.3 |
| QR Payments | 56.0 |
| UPI Lite | 28.3 |
| UPI Autopay | 19.5 |

## Failure analysis
- No incidents open. Technical declines are within the 0.37% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D105-MON) and any meetings/emails on 19 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D105-MON, RPT-D104-DAILY
