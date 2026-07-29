---
id: RPT-D94-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-23T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 23 Sep 2026)

**Report ID:** RPT-D94-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 23 Sep 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 94 of 180)

## Transaction summary
The rail processed 901.4M UPI transactions on Wednesday — a steady mid-week day — up 6.1M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 901.4  (▲6.1 w/w, ▲156.5 m/m)
- **Success Rate:** 99.98%  (▲0.47 d/d, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.71 d/d, ▲0.46 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.32%  (▲0.01 d/d, ▼0.04 w/w, ▼0.13 m/m)
- **Business Declines:** 0.16%  (▼0.04 m/m)
- **Customer Complaints:** 1,251  (▼5 d/d, ▼169 w/w, ▼691 m/m)
- **Merchant Complaints:** 129  (▼2 d/d, ▼5 w/w, ▼82 m/m)
- **Fraud Alerts:** 831  (▼3 d/d, ▼14 w/w, ▼220 m/m)
- **Risk Score:** 23  (▼1 w/w, ▼8 m/m)
- **Response Time:** 622 ms  (▼4 d/d, ▼31 w/w, ▼120 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 289.8 | 99.5% |
| HDFC Bank | 99.4 | 99.55% |
| Bank of Baroda | 71.5 | 99.64% |
| Union Bank of India | 62.1 | 99.43% |
| ICICI Bank | 55.6 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 430.0 | 99.14% | 231 ms |
| Google Pay | 294.4 | 99.17% | 316 ms |
| Paytm | 72.7 | 99.06% | 192 ms |
| Navi | 33.2 | 99.17% | 225 ms |
| SuperMoney | 17.6 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 338.0 |
| Person to Person | 320.0 |
| QR Payments | 85.6 |
| UPI Lite | 43.3 |
| UPI Autopay | 29.7 |

## Failure analysis
- No incidents open. Technical declines are within the 0.32% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D94-MON) and any meetings/emails on 23 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D94-MON, RPT-D93-DAILY
