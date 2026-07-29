---
id: RPT-D79-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-08T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 08 Sep 2026)

**Report ID:** RPT-D79-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 08 Sep 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 79 of 180)

## Transaction summary
The rail processed 882.2M UPI transactions on Tuesday — a steady mid-week day — up 20.4M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 882.2  (▲27.0 d/d, ▲20.4 w/w, ▲137.3 m/m)
- **Success Rate:** 99.98%  (▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.55 m/m)
- **Technical Declines:** 0.34%  (▼0.01 w/w, ▼0.11 m/m)
- **Business Declines:** 0.16%  (▼0.01 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,350  (▼12 d/d, ▼47 w/w, ▼592 m/m)
- **Merchant Complaints:** 140  (▼6 w/w, ▼71 m/m)
- **Fraud Alerts:** 862  (▼25 w/w, ▼189 m/m)
- **Risk Score:** 24  (▼1 w/w, ▼7 m/m)
- **Response Time:** 631 ms  (▼7 d/d, ▼18 w/w, ▼111 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 283.6 | 99.5% |
| HDFC Bank | 97.3 | 99.55% |
| Bank of Baroda | 70.0 | 99.64% |
| Union Bank of India | 60.8 | 99.43% |
| ICICI Bank | 54.4 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 420.9 | 99.14% | 231 ms |
| Google Pay | 288.2 | 99.17% | 316 ms |
| Paytm | 71.2 | 99.06% | 192 ms |
| Navi | 32.5 | 99.17% | 225 ms |
| SuperMoney | 17.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 330.8 |
| Person to Person | 313.2 |
| QR Payments | 83.8 |
| UPI Lite | 42.3 |
| UPI Autopay | 29.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.34% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D79-MON) and any meetings/emails on 08 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D79-MON, RPT-D78-DAILY
