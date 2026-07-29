---
id: RPT-D26-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-17T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 17 Jul 2026)

**Report ID:** RPT-D26-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 17 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 26 of 180)

## Transaction summary
The rail processed 782.9M UPI transactions on Friday — a steady mid-week day — up 10.4M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 782.9  (▲3.8 d/d, ▲10.4 w/w, ▲38.0 m/m)
- **Success Rate:** 99.98%  (▲0.67 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.93 d/d, ▲0.35 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.41%  (▼0.01 w/w, ▼0.04 m/m)
- **Business Declines:** 0.19%  (▼0.01 m/m)
- **Customer Complaints:** 1,741  (▲6 d/d, ▼58 w/w, ▼201 m/m)
- **Merchant Complaints:** 184  (▼3 d/d, ▼6 w/w, ▼27 m/m)
- **Fraud Alerts:** 979  (▼15 d/d, ▼34 w/w, ▼72 m/m)
- **Risk Score:** 29  (▼2 m/m)
- **Response Time:** 702 ms  (▲2 d/d, ▼5 w/w, ▼40 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 251.7 | 99.5% |
| HDFC Bank | 86.4 | 99.55% |
| Bank of Baroda | 62.1 | 99.64% |
| Union Bank of India | 53.9 | 99.43% |
| ICICI Bank | 48.3 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 373.5 | 99.14% | 231 ms |
| Google Pay | 255.7 | 99.17% | 316 ms |
| Paytm | 63.2 | 99.06% | 192 ms |
| Navi | 28.9 | 99.17% | 225 ms |
| SuperMoney | 15.3 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 293.6 |
| Person to Person | 277.9 |
| QR Payments | 74.4 |
| UPI Lite | 37.6 |
| UPI Autopay | 25.8 |

## Failure analysis
- No incidents open. Technical declines are within the 0.41% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D26-MON) and any meetings/emails on 17 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D26-MON, RPT-D25-DAILY
