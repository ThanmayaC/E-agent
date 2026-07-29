---
id: RPT-D159-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-27T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 27 Nov 2026)

**Report ID:** RPT-D159-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 27 Nov 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 159 of 180)

## Transaction summary
The rail processed 1001.0M UPI transactions on Friday — a steady mid-week day — up 18.0M on the same day last week. Success held at 99.28% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1001.0  (▼24.8 d/d, ▲18.0 w/w, ▲256.1 m/m)
- **Success Rate:** 99.28%  (▼0.7 d/d, ▼0.34 w/w, ▼0.32 m/m)
- **Settlement Success:** 99.98%  (▲0.28 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.24%  (▼0.01 d/d, ▼0.01 w/w, ▼0.21 m/m)
- **Business Declines:** 0.14%  (▲0.01 d/d, ▼0.06 w/w, ▼0.06 m/m)
- **Customer Complaints:** 926  (▼229 w/w, ▼1016 m/m)
- **Merchant Complaints:** 93  (▼3 w/w, ▼118 m/m)
- **Fraud Alerts:** 712  (▲6 d/d, ▼160 w/w, ▼339 m/m)
- **Risk Score:** 19  (▼10 w/w, ▼12 m/m)
- **Response Time:** 543 ms  (▼2 d/d, ▼16 w/w, ▼199 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 321.8 | 99.5% |
| HDFC Bank | 110.4 | 99.55% |
| Bank of Baroda | 79.4 | 99.64% |
| Union Bank of India | 69.0 | 99.43% |
| ICICI Bank | 61.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 477.6 | 99.14% | 231 ms |
| Google Pay | 327.0 | 99.17% | 316 ms |
| Paytm | 80.8 | 99.06% | 192 ms |
| Navi | 36.9 | 99.17% | 225 ms |
| SuperMoney | 19.5 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 375.4 |
| Person to Person | 355.4 |
| QR Payments | 95.1 |
| UPI Lite | 48.0 |
| UPI Autopay | 33.0 |

## Failure analysis
- No incidents open. Technical declines are within the 0.24% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D159-MON) and any meetings/emails on 27 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D159-MON, RPT-D158-DAILY
