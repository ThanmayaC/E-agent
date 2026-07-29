---
id: RPT-D116-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-30T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 30 Apr 2026)

**Report ID:** RPT-D116-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 30 Apr 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 116 of 206)

## Transaction summary
The rail processed 786.9M UPI transactions on Thursday — the month-end surge as salary and bill-pay flows land — up 77.0M on the same day last week. Success held at 99.7% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 786.9  (▲5.5 d/d, ▲77.0 w/w, ▼9.0 m/m)
- **Success Rate:** 99.7%  (▲0.4 d/d, ▲1.15 w/w, ▲0.57 m/m)
- **Settlement Success:** 99.98%  (▲0.43 d/d, ▲0.03 m/m)
- **Technical Declines:** 0.35%  (▼0.14 d/d, ▼0.02 w/w, ▼0.2 m/m)
- **Business Declines:** 0.18%  (▼0.08 w/w, ▼0.06 m/m)
- **Customer Complaints:** 1,253  (▼336 d/d, ▼30 w/w, ▼889 m/m)
- **Merchant Complaints:** 130  (▼53 d/d, ▼84 w/w, ▼104 m/m)
- **Fraud Alerts:** 861  (▼2 d/d, ▼9 w/w, ▼299 m/m)
- **Risk Score:** 24  (▼10 m/m)
- **Response Time:** 616 ms  (▼31 d/d, ▼10 w/w, ▼137 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 256.1 | 99.67% |
| HDFC Bank | 84.1 | 99.42% |
| Bank of Baroda | 60.6 | 99.26% |
| Union Bank of India | 53.1 | 99.63% |
| Axis Bank | 48.5 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 375.9 | 99.51% | 198 ms |
| Google Pay | 257.3 | 99.35% | 241 ms |
| Paytm | 62.4 | 99.53% | 201 ms |
| Navi | 28.9 | 99.53% | 304 ms |
| SuperMoney | 15.3 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 291.2 |
| Person to Person | 279.3 |
| QR Payments | 74.8 |
| UPI Lite | 37.8 |
| UPI Autopay | 26.0 |

## Failure analysis
- No incidents open. Technical declines are within the 0.35% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D116-MON) and any meetings/emails on 30 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D116-MON, RPT-D115-DAILY
