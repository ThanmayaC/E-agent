---
id: RPT-D106-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-05T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 05 Oct 2026)

**Report ID:** RPT-D106-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 05 Oct 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 106 of 180)

## Transaction summary
The rail processed 1117.0M UPI transactions on Monday — a campaign-driven high-volume day — up 89.4M on the same day last week. Success held at 99.21% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1117.0  (▲369.2 d/d, ▲89.4 w/w, ▲372.1 m/m)
- **Success Rate:** 99.21%  (▼0.23 d/d, ▲0.12 w/w, ▼0.39 m/m)
- **Settlement Success:** 99.98%  (▲0.77 d/d, ▲0.55 m/m)
- **Technical Declines:** 0.3%  (▼0.01 w/w, ▼0.15 m/m)
- **Business Declines:** 0.15%  (▼0.01 d/d, ▼0.02 w/w, ▼0.05 m/m)
- **Customer Complaints:** 1,178  (▼13 d/d, ▼87 w/w, ▼764 m/m)
- **Merchant Complaints:** 121  (▼2 d/d, ▼4 w/w, ▼90 m/m)
- **Fraud Alerts:** 810  (▼4 d/d, ▼39 w/w, ▼241 m/m)
- **Risk Score:** 22  (▼2 w/w, ▼9 m/m)
- **Response Time:** 605 ms  (▲3 d/d, ▼8 w/w, ▼137 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 359.1 | 99.5% |
| HDFC Bank | 123.2 | 99.55% |
| Bank of Baroda | 88.6 | 99.64% |
| Union Bank of India | 76.9 | 99.43% |
| ICICI Bank | 68.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 532.9 | 99.14% | 231 ms |
| Google Pay | 364.9 | 99.17% | 316 ms |
| Paytm | 90.1 | 99.06% | 192 ms |
| Navi | 41.2 | 99.17% | 225 ms |
| SuperMoney | 21.8 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 418.9 |
| Person to Person | 396.5 |
| QR Payments | 106.1 |
| UPI Lite | 53.6 |
| UPI Autopay | 36.9 |

## Failure analysis
- No incidents open. Technical declines are within the 0.3% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D106-MON) and any meetings/emails on 05 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D106-MON, RPT-D105-DAILY
