---
id: RPT-D163-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-12-01T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 01 Dec 2026)

**Report ID:** RPT-D163-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 01 Dec 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 163 of 180)

## Transaction summary
The rail processed 1049.6M UPI transactions on Tuesday — a steady mid-week day — up 40.6M on the same day last week. Success held at 99.98% and settlement at 99.53%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1049.6  (▼208.6 d/d, ▲40.6 w/w, ▲304.7 m/m)
- **Success Rate:** 99.98%  (▲0.78 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.53%  (▼0.45 d/d, ▼0.45 w/w, ▲0.1 m/m)
- **Technical Declines:** 0.24%  (▼0.1 d/d, ▼0.01 w/w, ▼0.21 m/m)
- **Business Declines:** 0.13%  (▼0.07 m/m)
- **Customer Complaints:** 905  (▼244 d/d, ▼38 w/w, ▼1037 m/m)
- **Merchant Complaints:** 91  (▼38 d/d, ▼4 w/w, ▼120 m/m)
- **Fraud Alerts:** 699  (▲2 d/d, ▼18 w/w, ▼352 m/m)
- **Risk Score:** 19  (▼12 m/m)
- **Response Time:** 541 ms  (▼35 d/d, ▼8 w/w, ▼201 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 337.5 | 99.5% |
| HDFC Bank | 115.8 | 99.55% |
| Bank of Baroda | 83.2 | 99.64% |
| Union Bank of India | 72.3 | 99.43% |
| ICICI Bank | 64.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 500.7 | 99.14% | 231 ms |
| Google Pay | 342.8 | 99.17% | 316 ms |
| Paytm | 84.7 | 99.06% | 192 ms |
| Navi | 38.7 | 99.17% | 225 ms |
| SuperMoney | 20.5 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 393.6 |
| Person to Person | 372.6 |
| QR Payments | 99.7 |
| UPI Lite | 50.4 |
| UPI Autopay | 34.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.24% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D163-MON) and any meetings/emails on 01 Dec.

Refs: upi_kpis_month.xlsx, TEAMS-D163-MON, RPT-D162-DAILY
