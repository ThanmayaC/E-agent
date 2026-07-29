---
id: RPT-D18-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-09T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 09 Jul 2026)

**Report ID:** RPT-D18-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 09 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 18 of 180)

## Transaction summary
The rail processed 779.8M UPI transactions on Thursday — a steady mid-week day — up 24.8M on the same day last week. Success held at 98.8% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 779.8  (▲13.1 d/d, ▲24.8 w/w, ▲34.9 m/m)
- **Success Rate:** 98.8%  (▼1.18 d/d, ▲0.72 w/w, ▼0.8 m/m)
- **Settlement Success:** 99.98%  (▲1.33 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.42%  (▼0.01 d/d, ▼0.21 w/w, ▼0.03 m/m)
- **Business Declines:** 0.19%  (▼0.05 d/d, ▼0.01 m/m)
- **Customer Complaints:** 1,804  (▼238 d/d, ▼715 w/w, ▼138 m/m)
- **Merchant Complaints:** 193  (▼1 d/d, ▼7 w/w, ▼18 m/m)
- **Fraud Alerts:** 1,002  (▼134 d/d, ▼30 w/w, ▼49 m/m)
- **Risk Score:** 29  (▼9 d/d, ▼1 w/w, ▼2 m/m)
- **Response Time:** 710 ms  (▼9 d/d, ▼144 w/w, ▼32 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 250.7 | 99.5% |
| HDFC Bank | 86.0 | 99.55% |
| Bank of Baroda | 61.8 | 99.64% |
| Union Bank of India | 53.7 | 99.43% |
| ICICI Bank | 48.1 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 372.0 | 99.14% | 231 ms |
| Google Pay | 254.7 | 99.17% | 316 ms |
| Paytm | 62.9 | 99.06% | 192 ms |
| Navi | 28.7 | 99.17% | 225 ms |
| SuperMoney | 15.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 292.4 |
| Person to Person | 276.8 |
| QR Payments | 74.1 |
| UPI Lite | 37.4 |
| UPI Autopay | 25.7 |

## Failure analysis
- No incidents open. Technical declines are within the 0.42% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D18-MON) and any meetings/emails on 09 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D18-MON, RPT-D17-DAILY
