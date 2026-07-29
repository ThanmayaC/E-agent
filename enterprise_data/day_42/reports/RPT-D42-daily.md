---
id: RPT-D42-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-02T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 02 Aug 2026)

**Report ID:** RPT-D42-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 02 Aug 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 42 of 180)

## Transaction summary
The rail processed 672.0M UPI transactions on Sunday — a quiet Sunday — up 9.1M on the same day last week. Success held at 99.7% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 672.0  (▼41.6 d/d, ▲9.1 w/w, ▼72.9 m/m)
- **Success Rate:** 99.7%  (▲1.09 d/d, ▲1.18 w/w, ▲0.1 m/m)
- **Settlement Success:** 99.98%  (▲0.37 d/d, ▲0.72 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.38%  (▼0.01 d/d, ▼0.1 w/w, ▼0.07 m/m)
- **Business Declines:** 0.18%  (▼0.02 m/m)
- **Customer Complaints:** 1,593  (▼34 d/d, ▼339 w/w, ▼349 m/m)
- **Merchant Complaints:** 171  (▼1 d/d, ▼5 w/w, ▼40 m/m)
- **Fraud Alerts:** 957  (▲4 d/d, ▼2 w/w, ▼94 m/m)
- **Risk Score:** 27  (▼1 d/d, ▼1 w/w, ▼4 m/m)
- **Response Time:** 679 ms  (▼3 d/d, ▼73 w/w, ▼63 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 216.1 | 99.5% |
| HDFC Bank | 74.1 | 99.55% |
| Bank of Baroda | 53.3 | 99.64% |
| Union Bank of India | 46.3 | 99.43% |
| ICICI Bank | 41.4 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 320.6 | 99.14% | 231 ms |
| Google Pay | 219.5 | 99.17% | 316 ms |
| Paytm | 54.2 | 99.06% | 192 ms |
| Navi | 24.8 | 99.17% | 225 ms |
| SuperMoney | 13.1 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 252.0 |
| Person to Person | 238.6 |
| QR Payments | 63.8 |
| UPI Lite | 32.3 |
| UPI Autopay | 22.2 |

## Failure analysis
- No incidents open. Technical declines are within the 0.38% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D42-MON) and any meetings/emails on 02 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D42-MON, RPT-D41-DAILY
