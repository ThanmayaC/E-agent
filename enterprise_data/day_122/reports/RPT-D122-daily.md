---
id: RPT-D122-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-21T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 21 Oct 2026)

**Report ID:** RPT-D122-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 21 Oct 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 122 of 180)

## Transaction summary
The rail processed 957.9M UPI transactions on Wednesday — a steady mid-week day — up 19.3M on the same day last week. Success held at 99.98% and settlement at 98.92%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 957.9  (▲25.9 d/d, ▲19.3 w/w, ▲213.0 m/m)
- **Success Rate:** 99.98%  (▲0.22 d/d, ▲0.78 w/w, ▲0.38 m/m)
- **Settlement Success:** 98.92%  (▼0.69 d/d, ▼1.01 w/w, ▼0.51 m/m)
- **Technical Declines:** 0.28%  (▼0.01 d/d, ▼0.01 w/w, ▼0.17 m/m)
- **Business Declines:** 0.15%  (▼0.02 w/w, ▼0.05 m/m)
- **Customer Complaints:** 1,104  (▼1 d/d, ▼126 w/w, ▼838 m/m)
- **Merchant Complaints:** 112  (▼1 d/d, ▼5 w/w, ▼99 m/m)
- **Fraud Alerts:** 771  (▼4 d/d, ▼77 w/w, ▼280 m/m)
- **Risk Score:** 21  (▼5 w/w, ▼10 m/m)
- **Response Time:** 582 ms  (▼11 d/d, ▼13 w/w, ▼160 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 308.0 | 99.5% |
| HDFC Bank | 105.7 | 99.55% |
| Bank of Baroda | 76.0 | 99.64% |
| Union Bank of India | 66.0 | 99.43% |
| ICICI Bank | 59.1 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 457.0 | 99.14% | 231 ms |
| Google Pay | 312.9 | 99.17% | 316 ms |
| Paytm | 77.3 | 99.06% | 192 ms |
| Navi | 35.3 | 99.17% | 225 ms |
| SuperMoney | 18.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 359.2 |
| Person to Person | 340.1 |
| QR Payments | 91.0 |
| UPI Lite | 46.0 |
| UPI Autopay | 31.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.28% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D122-MON) and any meetings/emails on 21 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D122-MON, RPT-D121-DAILY
