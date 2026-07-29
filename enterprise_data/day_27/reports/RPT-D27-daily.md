---
id: RPT-D27-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-18T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 18 Jul 2026)

**Report ID:** RPT-D27-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 18 Jul 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 27 of 180)

## Transaction summary
The rail processed 716.6M UPI transactions on Saturday — a lighter Saturday — up 10.8M on the same day last week. Success held at 99.8% and settlement at 99.06%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 716.6  (▼66.3 d/d, ▲10.8 w/w, ▼28.3 m/m)
- **Success Rate:** 99.8%  (▼0.18 d/d, ▲0.86 w/w, ▲0.2 m/m)
- **Settlement Success:** 99.06%  (▼0.92 d/d, ▼0.92 w/w, ▼0.37 m/m)
- **Technical Declines:** 0.41%  (▼0.01 w/w, ▼0.04 m/m)
- **Business Declines:** 0.19%  (▼0.01 m/m)
- **Customer Complaints:** 1,739  (▼2 d/d, ▼32 w/w, ▼203 m/m)
- **Merchant Complaints:** 182  (▼2 d/d, ▼7 w/w, ▼29 m/m)
- **Fraud Alerts:** 980  (▲1 d/d, ▼12 w/w, ▼71 m/m)
- **Risk Score:** 29  (▼2 m/m)
- **Response Time:** 706 ms  (▲4 d/d, ▼7 w/w, ▼36 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 230.4 | 99.5% |
| HDFC Bank | 79.1 | 99.55% |
| Bank of Baroda | 56.8 | 99.64% |
| Union Bank of India | 49.4 | 99.43% |
| ICICI Bank | 44.2 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 341.9 | 99.14% | 231 ms |
| Google Pay | 234.1 | 99.17% | 316 ms |
| Paytm | 57.8 | 99.06% | 192 ms |
| Navi | 26.4 | 99.17% | 225 ms |
| SuperMoney | 14.0 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 268.7 |
| Person to Person | 254.4 |
| QR Payments | 68.1 |
| UPI Lite | 34.4 |
| UPI Autopay | 23.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.41% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D27-MON) and any meetings/emails on 18 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D27-MON, RPT-D26-DAILY
