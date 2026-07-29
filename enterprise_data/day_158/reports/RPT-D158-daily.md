---
id: RPT-D158-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-26T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 26 Nov 2026)

**Report ID:** RPT-D158-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 26 Nov 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 158 of 180)

## Transaction summary
The rail processed 1025.8M UPI transactions on Thursday — a steady mid-week day — up 32.4M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1025.8  (▲8.0 d/d, ▲32.4 w/w, ▲280.9 m/m)
- **Success Rate:** 99.98%  (▲0.02 d/d, ▲0.06 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.55 m/m)
- **Technical Declines:** 0.25%  (▼0.2 m/m)
- **Business Declines:** 0.13%  (▼0.01 d/d, ▼0.11 w/w, ▼0.07 m/m)
- **Customer Complaints:** 926  (▼9 d/d, ▼362 w/w, ▼1016 m/m)
- **Merchant Complaints:** 93  (▼3 w/w, ▼118 m/m)
- **Fraud Alerts:** 706  (▼7 d/d, ▼263 w/w, ▼345 m/m)
- **Risk Score:** 19  (▼17 w/w, ▼12 m/m)
- **Response Time:** 545 ms  (▼7 d/d, ▼16 w/w, ▼197 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 329.8 | 99.5% |
| HDFC Bank | 113.2 | 99.55% |
| Bank of Baroda | 81.4 | 99.64% |
| Union Bank of India | 70.7 | 99.43% |
| ICICI Bank | 63.2 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 489.4 | 99.14% | 231 ms |
| Google Pay | 335.1 | 99.17% | 316 ms |
| Paytm | 82.8 | 99.06% | 192 ms |
| Navi | 37.8 | 99.17% | 225 ms |
| SuperMoney | 20.0 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 384.7 |
| Person to Person | 364.2 |
| QR Payments | 97.5 |
| UPI Lite | 49.2 |
| UPI Autopay | 33.9 |

## Failure analysis
- No incidents open. Technical declines are within the 0.25% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D158-MON) and any meetings/emails on 26 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D158-MON, RPT-D157-DAILY
