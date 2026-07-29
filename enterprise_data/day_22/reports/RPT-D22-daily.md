---
id: RPT-D22-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-13T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 13 Jul 2026)

**Report ID:** RPT-D22-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 13 Jul 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 22 of 180)

## Transaction summary
The rail processed 765.3M UPI transactions on Monday — the Monday ramp-up after the weekend — up 21.4M on the same day last week. Success held at 99.01% and settlement at 98.7%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 765.3  (▲130.4 d/d, ▲21.4 w/w, ▲20.4 m/m)
- **Success Rate:** 99.01%  (▲0.07 d/d, ▼0.56 w/w, ▼0.59 m/m)
- **Settlement Success:** 98.7%  (▼1.28 d/d, ▼0.77 w/w, ▼0.73 m/m)
- **Technical Declines:** 0.41%  (▼0.02 w/w, ▼0.04 m/m)
- **Business Declines:** 0.19%  (▼0.15 w/w, ▼0.01 m/m)
- **Customer Complaints:** 1,781  (▼10 d/d, ▼703 w/w, ▼161 m/m)
- **Merchant Complaints:** 187  (▼2 d/d, ▼9 w/w, ▼24 m/m)
- **Fraud Alerts:** 995  (▲4 d/d, ▼353 w/w, ▼56 m/m)
- **Risk Score:** 29  (▼26 w/w, ▼2 m/m)
- **Response Time:** 710 ms  (▼4 d/d, ▼13 w/w, ▼32 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 246.1 | 99.5% |
| HDFC Bank | 84.4 | 99.55% |
| Bank of Baroda | 60.7 | 99.64% |
| Union Bank of India | 52.7 | 99.43% |
| ICICI Bank | 47.2 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 365.1 | 99.14% | 231 ms |
| Google Pay | 250.0 | 99.17% | 316 ms |
| Paytm | 61.7 | 99.06% | 192 ms |
| Navi | 28.2 | 99.17% | 225 ms |
| SuperMoney | 14.9 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 287.0 |
| Person to Person | 271.7 |
| QR Payments | 72.7 |
| UPI Lite | 36.7 |
| UPI Autopay | 25.3 |

## Failure analysis
- No incidents open. Technical declines are within the 0.41% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D22-MON) and any meetings/emails on 13 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D22-MON, RPT-D21-DAILY
