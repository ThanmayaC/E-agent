---
id: RPT-D41-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-01T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 01 Aug 2026)

**Report ID:** RPT-D41-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 01 Aug 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 41 of 180)

## Transaction summary
The rail processed 713.6M UPI transactions on Saturday — a lighter Saturday — down 3.7M on the same day last week. Success held at 98.61% and settlement at 99.61%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 713.6  (▼179.7 d/d, ▼3.7 w/w, ▼31.3 m/m)
- **Success Rate:** 98.61%  (▼1.37 d/d, ▼0.56 w/w, ▼0.99 m/m)
- **Settlement Success:** 99.61%  (▼0.37 d/d, ▲0.65 w/w, ▲0.18 m/m)
- **Technical Declines:** 0.39%  (▼0.13 w/w, ▼0.06 m/m)
- **Business Declines:** 0.18%  (▼0.02 m/m)
- **Customer Complaints:** 1,627  (▲7 d/d, ▼482 w/w, ▼315 m/m)
- **Merchant Complaints:** 172  (▼1 d/d, ▼6 w/w, ▼39 m/m)
- **Fraud Alerts:** 953  (▲1 d/d, ▼23 w/w, ▼98 m/m)
- **Risk Score:** 28  (▲1 d/d, ▼3 m/m)
- **Response Time:** 682 ms  (▲3 d/d, ▼100 w/w, ▼60 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 229.4 | 99.5% |
| HDFC Bank | 78.7 | 99.55% |
| Bank of Baroda | 56.6 | 99.64% |
| Union Bank of India | 49.2 | 99.43% |
| ICICI Bank | 44.0 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 340.4 | 99.14% | 231 ms |
| Google Pay | 233.1 | 99.17% | 316 ms |
| Paytm | 57.6 | 99.06% | 192 ms |
| Navi | 26.3 | 99.17% | 225 ms |
| SuperMoney | 13.9 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 267.6 |
| Person to Person | 253.3 |
| QR Payments | 67.8 |
| UPI Lite | 34.3 |
| UPI Autopay | 23.5 |

## Failure analysis
- No incidents open. Technical declines are within the 0.39% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D41-MON) and any meetings/emails on 01 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D41-MON, RPT-D40-DAILY
