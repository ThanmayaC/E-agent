---
id: RPT-D97-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-11T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 11 Apr 2026)

**Report ID:** RPT-D97-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 11 Apr 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 97 of 206)

## Transaction summary
The rail processed 640.7M UPI transactions on Saturday — a lighter Saturday — up 20.1M on the same day last week. Success held at 99.86% and settlement at 99.38%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 640.7  (▼61.9 d/d, ▲20.1 w/w, ▼155.2 m/m)
- **Success Rate:** 99.86%  (▲0.84 d/d, ▲0.53 w/w, ▲0.73 m/m)
- **Settlement Success:** 99.38%  (▲0.17 d/d, ▼0.22 w/w, ▼0.57 m/m)
- **Technical Declines:** 0.38%  (▼0.01 w/w, ▼0.17 m/m)
- **Business Declines:** 0.19%  (▼0.05 m/m)
- **Customer Complaints:** 1,376  (▲16 d/d, ▼44 w/w, ▼766 m/m)
- **Merchant Complaints:** 143  (▼4 w/w, ▼91 m/m)
- **Fraud Alerts:** 913  (▲5 d/d, ▼15 w/w, ▼247 m/m)
- **Risk Score:** 25  (▼1 w/w, ▼9 m/m)
- **Response Time:** 633 ms  (▼6 d/d, ▼15 w/w, ▼120 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 208.5 | 99.67% |
| HDFC Bank | 68.5 | 99.42% |
| Bank of Baroda | 49.3 | 99.26% |
| Union Bank of India | 43.2 | 99.63% |
| Axis Bank | 39.5 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 306.0 | 99.51% | 198 ms |
| Google Pay | 209.5 | 99.35% | 241 ms |
| Paytm | 50.8 | 99.53% | 201 ms |
| Navi | 23.6 | 99.53% | 304 ms |
| SuperMoney | 12.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 237.1 |
| Person to Person | 227.4 |
| QR Payments | 60.9 |
| UPI Lite | 30.8 |
| UPI Autopay | 21.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.38% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D97-MON) and any meetings/emails on 11 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D97-MON, RPT-D96-DAILY
