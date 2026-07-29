---
id: RPT-D120-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-04T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 04 May 2026)

**Report ID:** RPT-D120-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 04 May 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 120 of 206)

## Transaction summary
The rail processed 683.1M UPI transactions on Monday — the Monday ramp-up after the weekend — down 3.6M on the same day last week. Success held at 99.94% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 683.1  (▲98.4 d/d, ▼3.6 w/w, ▼112.8 m/m)
- **Success Rate:** 99.94%  (▼0.04 d/d, ▲0.45 w/w, ▲0.81 m/m)
- **Settlement Success:** 99.98%  (▲1.28 d/d, ▲0.55 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.35%  (▼0.01 w/w, ▼0.2 m/m)
- **Business Declines:** 0.18%  (▼0.03 d/d, ▼0.06 m/m)
- **Customer Complaints:** 1,231  (▼73 d/d, ▼43 w/w, ▼911 m/m)
- **Merchant Complaints:** 127  (▼56 d/d, ▼5 w/w, ▼107 m/m)
- **Fraud Alerts:** 858  (▲8 d/d, ▼12 w/w, ▼302 m/m)
- **Risk Score:** 24  (▲1 d/d, ▼10 m/m)
- **Response Time:** 607 ms  (▼10 d/d, ▼5 w/w, ▼146 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 222.3 | 99.67% |
| HDFC Bank | 73.0 | 99.42% |
| Bank of Baroda | 52.6 | 99.26% |
| Union Bank of India | 46.1 | 99.63% |
| Axis Bank | 42.1 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 326.3 | 99.51% | 198 ms |
| Google Pay | 223.4 | 99.35% | 241 ms |
| Paytm | 54.2 | 99.53% | 201 ms |
| Navi | 25.1 | 99.53% | 304 ms |
| SuperMoney | 13.3 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 252.7 |
| Person to Person | 242.5 |
| QR Payments | 64.9 |
| UPI Lite | 32.8 |
| UPI Autopay | 22.5 |

## Failure analysis
- No incidents open. Technical declines are within the 0.35% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D120-MON) and any meetings/emails on 04 May.

Refs: upi_kpis_month.xlsx, TEAMS-D120-MON, RPT-D119-DAILY
