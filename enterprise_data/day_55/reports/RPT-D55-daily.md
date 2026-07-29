---
id: RPT-D55-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-15T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 15 Aug 2026)

**Report ID:** RPT-D55-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 15 Aug 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 55 of 180)

## Transaction summary
The rail processed 745.6M UPI transactions on Saturday — a lighter Saturday — down 9.0M on the same day last week. Success held at 99.69% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 745.6  (▼250.3 d/d, ▼9.0 w/w, ▲0.7 m/m)
- **Success Rate:** 99.69%  (▼0.29 d/d, ▼0.29 w/w, ▲0.09 m/m)
- **Settlement Success:** 99.98%  (▲0.07 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.37%  (▲0.01 d/d, ▼0.08 m/m)
- **Business Declines:** 0.18%  (▲0.01 d/d, ▼0.02 m/m)
- **Customer Complaints:** 1,513  (▼12 d/d, ▼49 w/w, ▼429 m/m)
- **Merchant Complaints:** 159  (▼1 d/d, ▼6 w/w, ▼52 m/m)
- **Fraud Alerts:** 917  (▼12 d/d, ▼12 w/w, ▼134 m/m)
- **Risk Score:** 26  (▼1 w/w, ▼5 m/m)
- **Response Time:** 667 ms  (▲1 d/d, ▼11 w/w, ▼75 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 239.7 | 99.5% |
| HDFC Bank | 82.3 | 99.55% |
| Bank of Baroda | 59.1 | 99.64% |
| Union Bank of India | 51.4 | 99.43% |
| ICICI Bank | 46.0 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 355.7 | 99.14% | 231 ms |
| Google Pay | 243.5 | 99.17% | 316 ms |
| Paytm | 60.2 | 99.06% | 192 ms |
| Navi | 27.5 | 99.17% | 225 ms |
| SuperMoney | 14.5 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 279.6 |
| Person to Person | 264.7 |
| QR Payments | 70.8 |
| UPI Lite | 35.8 |
| UPI Autopay | 24.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.37% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D55-MON) and any meetings/emails on 15 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D55-MON, RPT-D54-DAILY
