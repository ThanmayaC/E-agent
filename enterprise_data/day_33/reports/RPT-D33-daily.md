---
id: RPT-D33-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-24T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 24 Jul 2026)

**Report ID:** RPT-D33-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 24 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 33 of 180)

## Transaction summary
The rail processed 815.2M UPI transactions on Friday — a steady mid-week day — up 32.3M on the same day last week. Success held at 99.43% and settlement at 98.83%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 815.2  (▲33.6 d/d, ▲32.3 w/w, ▲70.3 m/m)
- **Success Rate:** 99.43%  (▼0.05 d/d, ▼0.55 w/w, ▼0.17 m/m)
- **Settlement Success:** 98.83%  (▼1.15 d/d, ▼1.15 w/w, ▼0.6 m/m)
- **Technical Declines:** 0.4%  (▼0.01 w/w, ▼0.05 m/m)
- **Business Declines:** 0.18%  (▼0.01 d/d, ▼0.01 w/w, ▼0.02 m/m)
- **Customer Complaints:** 1,682  (▼59 w/w, ▼260 m/m)
- **Merchant Complaints:** 178  (▼1 d/d, ▼6 w/w, ▼33 m/m)
- **Fraud Alerts:** 969  (▼11 d/d, ▼10 w/w, ▼82 m/m)
- **Risk Score:** 28  (▼1 w/w, ▼3 m/m)
- **Response Time:** 696 ms  (▲9 d/d, ▼6 w/w, ▼46 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 262.1 | 99.5% |
| HDFC Bank | 89.9 | 99.55% |
| Bank of Baroda | 64.7 | 99.64% |
| Union Bank of India | 56.2 | 99.43% |
| ICICI Bank | 50.3 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 388.9 | 99.14% | 231 ms |
| Google Pay | 266.3 | 99.17% | 316 ms |
| Paytm | 65.8 | 99.06% | 192 ms |
| Navi | 30.0 | 99.17% | 225 ms |
| SuperMoney | 15.9 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 305.7 |
| Person to Person | 289.4 |
| QR Payments | 77.4 |
| UPI Lite | 39.1 |
| UPI Autopay | 26.9 |

## Failure analysis
- No incidents open. Technical declines are within the 0.4% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D33-MON) and any meetings/emails on 24 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D33-MON, RPT-D32-DAILY
