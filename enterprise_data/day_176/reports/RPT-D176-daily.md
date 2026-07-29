---
id: RPT-D176-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-12-14T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 14 Dec 2026)

**Report ID:** RPT-D176-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 14 Dec 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 176 of 180)

## Transaction summary
The rail processed 1010.7M UPI transactions on Monday — the Monday ramp-up after the weekend — down 8.4M on the same day last week. Success held at 99.62% and settlement at 99.72%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1010.7  (▲139.7 d/d, ▼8.4 w/w, ▲265.8 m/m)
- **Success Rate:** 99.62%  (▼0.36 d/d, ▼0.36 w/w, ▲0.02 m/m)
- **Settlement Success:** 99.72%  (▲0.36 d/d, ▲0.38 w/w, ▲0.29 m/m)
- **Technical Declines:** 0.23%  (▼0.03 w/w, ▼0.22 m/m)
- **Business Declines:** 0.13%  (▼0.07 m/m)
- **Customer Complaints:** 851  (▼11 d/d, ▼65 w/w, ▼1091 m/m)
- **Merchant Complaints:** 85  (▼3 w/w, ▼126 m/m)
- **Fraud Alerts:** 685  (▲8 d/d, ▼3 w/w, ▼366 m/m)
- **Risk Score:** 18  (▼13 m/m)
- **Response Time:** 526 ms  (▼9 d/d, ▼16 w/w, ▼216 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 325.0 | 99.5% |
| HDFC Bank | 111.5 | 99.55% |
| Bank of Baroda | 80.2 | 99.64% |
| Union Bank of India | 69.6 | 99.43% |
| ICICI Bank | 62.3 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 482.2 | 99.14% | 231 ms |
| Google Pay | 330.1 | 99.17% | 316 ms |
| Paytm | 81.5 | 99.06% | 192 ms |
| Navi | 37.2 | 99.17% | 225 ms |
| SuperMoney | 19.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 379.0 |
| Person to Person | 358.8 |
| QR Payments | 96.0 |
| UPI Lite | 48.5 |
| UPI Autopay | 33.4 |

## Failure analysis
- No incidents open. Technical declines are within the 0.23% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D176-MON) and any meetings/emails on 14 Dec.

Refs: upi_kpis_month.xlsx, TEAMS-D176-MON, RPT-D175-DAILY
