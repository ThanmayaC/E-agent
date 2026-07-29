---
id: RPT-D82-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-11T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 11 Sep 2026)

**Report ID:** RPT-D82-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 11 Sep 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 82 of 180)

## Transaction summary
The rail processed 1076.6M UPI transactions on Friday — a campaign-driven high-volume day — up 209.3M on the same day last week. Success held at 99.16% and settlement at 99.11%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1076.6  (▲205.3 d/d, ▲209.3 w/w, ▲331.7 m/m)
- **Success Rate:** 99.16%  (▼0.18 d/d, ▼0.19 w/w, ▼0.44 m/m)
- **Settlement Success:** 99.11%  (▲0.22 d/d, ▼0.28 w/w, ▼0.32 m/m)
- **Technical Declines:** 0.33%  (▼0.01 w/w, ▼0.12 m/m)
- **Business Declines:** 0.16%  (▼0.01 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,331  (▼3 d/d, ▼52 w/w, ▼611 m/m)
- **Merchant Complaints:** 139  (▲1 d/d, ▼5 w/w, ▼72 m/m)
- **Fraud Alerts:** 860  (▲4 d/d, ▼8 w/w, ▼191 m/m)
- **Risk Score:** 24  (▼7 m/m)
- **Response Time:** 632 ms  (▼6 d/d, ▼8 w/w, ▼110 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 346.2 | 99.5% |
| HDFC Bank | 118.8 | 99.55% |
| Bank of Baroda | 85.4 | 99.64% |
| Union Bank of India | 74.2 | 99.43% |
| ICICI Bank | 66.4 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 513.6 | 99.14% | 231 ms |
| Google Pay | 351.7 | 99.17% | 316 ms |
| Paytm | 86.9 | 99.06% | 192 ms |
| Navi | 39.7 | 99.17% | 225 ms |
| SuperMoney | 21.0 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 403.7 |
| Person to Person | 382.2 |
| QR Payments | 102.3 |
| UPI Lite | 51.7 |
| UPI Autopay | 35.5 |

## Failure analysis
- No incidents open. Technical declines are within the 0.33% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D82-MON) and any meetings/emails on 11 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D82-MON, RPT-D81-DAILY
