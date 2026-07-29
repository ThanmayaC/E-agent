---
id: RPT-D30-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-21T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 21 Jul 2026)

**Report ID:** RPT-D30-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 21 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 30 of 180)

## Transaction summary
The rail processed 789.8M UPI transactions on Tuesday — a steady mid-week day — up 13.2M on the same day last week. Success held at 99.98% and settlement at 99.87%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 789.8  (▼184.4 d/d, ▲13.2 w/w, ▲44.9 m/m)
- **Success Rate:** 99.98%  (▲0.07 d/d, ▲0.38 m/m)
- **Settlement Success:** 99.87%  (▼0.11 d/d, ▼0.11 w/w, ▲0.44 m/m)
- **Technical Declines:** 0.4%  (▼0.09 d/d, ▼0.01 w/w, ▼0.05 m/m)
- **Business Declines:** 0.18%  (▼0.01 d/d, ▼0.01 w/w, ▼0.02 m/m)
- **Customer Complaints:** 1,700  (▼285 d/d, ▼74 w/w, ▼242 m/m)
- **Merchant Complaints:** 182  (▲1 d/d, ▼6 w/w, ▼29 m/m)
- **Fraud Alerts:** 976  (▲6 d/d, ▼12 w/w, ▼75 m/m)
- **Risk Score:** 29  (▼2 m/m)
- **Response Time:** 694 ms  (▼65 d/d, ▼12 w/w, ▼48 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 253.9 | 99.5% |
| HDFC Bank | 87.1 | 99.55% |
| Bank of Baroda | 62.6 | 99.64% |
| Union Bank of India | 54.4 | 99.43% |
| ICICI Bank | 48.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 376.8 | 99.14% | 231 ms |
| Google Pay | 258.0 | 99.17% | 316 ms |
| Paytm | 63.7 | 99.06% | 192 ms |
| Navi | 29.1 | 99.17% | 225 ms |
| SuperMoney | 15.4 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 296.2 |
| Person to Person | 280.4 |
| QR Payments | 75.0 |
| UPI Lite | 37.9 |
| UPI Autopay | 26.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.4% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D30-MON) and any meetings/emails on 21 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D30-MON, RPT-D29-DAILY
