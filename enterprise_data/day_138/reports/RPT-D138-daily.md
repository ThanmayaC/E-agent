---
id: RPT-D138-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-06T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 06 Nov 2026)

**Report ID:** RPT-D138-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 06 Nov 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 138 of 180)

## Transaction summary
The rail processed 1198.6M UPI transactions on Friday — a campaign-driven high-volume day — up 108.7M on the same day last week. Success held at 99.89% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1198.6  (▲211.7 d/d, ▲108.7 w/w, ▲453.7 m/m)
- **Success Rate:** 99.89%  (▲0.84 d/d, ▲1.41 w/w, ▲0.29 m/m)
- **Settlement Success:** 99.98%  (▲0.35 d/d, ▲0.34 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.27%  (▼0.17 w/w, ▼0.18 m/m)
- **Business Declines:** 0.14%  (▼0.02 w/w, ▼0.06 m/m)
- **Customer Complaints:** 1,025  (▲4 d/d, ▼478 w/w, ▼917 m/m)
- **Merchant Complaints:** 102  (▼2 d/d, ▼99 w/w, ▼109 m/m)
- **Fraud Alerts:** 747  (▲2 d/d, ▼18 w/w, ▼304 m/m)
- **Risk Score:** 20  (▼1 w/w, ▼11 m/m)
- **Response Time:** 570 ms  (▼3 d/d, ▼61 w/w, ▼172 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 385.4 | 99.5% |
| HDFC Bank | 132.2 | 99.55% |
| Bank of Baroda | 95.1 | 99.64% |
| Union Bank of India | 82.6 | 99.43% |
| ICICI Bank | 73.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 571.8 | 99.14% | 231 ms |
| Google Pay | 391.5 | 99.17% | 316 ms |
| Paytm | 96.7 | 99.06% | 192 ms |
| Navi | 44.2 | 99.17% | 225 ms |
| SuperMoney | 23.4 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 449.5 |
| Person to Person | 425.5 |
| QR Payments | 113.9 |
| UPI Lite | 57.5 |
| UPI Autopay | 39.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.27% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D138-MON) and any meetings/emails on 06 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D138-MON, RPT-D137-DAILY
