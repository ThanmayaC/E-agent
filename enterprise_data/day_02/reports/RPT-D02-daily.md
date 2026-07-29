---
id: RPT-D02-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-23T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 23 Jun 2026)

**Report ID:** RPT-D02-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 23 Jun 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 2 of 180)

## Transaction summary
The rail processed 772.9M UPI transactions on Tuesday — a steady mid-week day — the first day in the window. Success held at 99.35% and settlement at 99.56%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 772.9  (▲28.0 d/d, ▲28.0 m/m)
- **Success Rate:** 99.35%  (▼0.25 d/d, ▼0.25 m/m)
- **Settlement Success:** 99.56%  (▲0.13 d/d, ▲0.13 m/m)
- **Technical Declines:** 0.45%
- **Business Declines:** 0.2%
- **Customer Complaints:** 1,930  (▼12 d/d, ▼12 m/m)
- **Merchant Complaints:** 207  (▼4 d/d, ▼4 m/m)
- **Fraud Alerts:** 1,052  (▲1 d/d, ▲1 m/m)
- **Risk Score:** 31
- **Response Time:** 735 ms  (▼7 d/d, ▼7 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 248.5 | 99.5% |
| HDFC Bank | 85.3 | 99.55% |
| Bank of Baroda | 61.3 | 99.64% |
| Union Bank of India | 53.2 | 99.43% |
| ICICI Bank | 47.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 368.7 | 99.14% | 231 ms |
| Google Pay | 252.5 | 99.17% | 316 ms |
| Paytm | 62.4 | 99.06% | 192 ms |
| Navi | 28.5 | 99.17% | 225 ms |
| SuperMoney | 15.1 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 289.8 |
| Person to Person | 274.4 |
| QR Payments | 73.4 |
| UPI Lite | 37.1 |
| UPI Autopay | 25.5 |

## Failure analysis
- No incidents open. Technical declines are within the 0.45% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D02-MON) and any meetings/emails on 23 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D02-MON, RPT-D01-DAILY
