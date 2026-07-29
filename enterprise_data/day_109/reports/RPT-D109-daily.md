---
id: RPT-D109-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-08T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 08 Oct 2026)

**Report ID:** RPT-D109-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 08 Oct 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 109 of 180)

## Transaction summary
The rail processed 914.2M UPI transactions on Thursday — a steady mid-week day — down 12.0M on the same day last week. Success held at 99.44% and settlement at 99.18%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 914.2  (▼15.2 d/d, ▼12.0 w/w, ▲169.3 m/m)
- **Success Rate:** 99.44%  (▼0.54 d/d, ▼0.54 w/w, ▼0.16 m/m)
- **Settlement Success:** 99.18%  (▼0.8 d/d, ▲0.37 w/w, ▼0.25 m/m)
- **Technical Declines:** 0.3%  (▼0.01 w/w, ▼0.15 m/m)
- **Business Declines:** 0.15%  (▼0.02 w/w, ▼0.05 m/m)
- **Customer Complaints:** 1,164  (▼17 d/d, ▼95 w/w, ▼778 m/m)
- **Merchant Complaints:** 121  (▼38 w/w, ▼90 m/m)
- **Fraud Alerts:** 809  (▲8 d/d, ▼5 w/w, ▼242 m/m)
- **Risk Score:** 22  (▼1 w/w, ▼9 m/m)
- **Response Time:** 604 ms  (▲1 d/d, ▼6 w/w, ▼138 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 293.9 | 99.5% |
| HDFC Bank | 100.9 | 99.55% |
| Bank of Baroda | 72.5 | 99.64% |
| Union Bank of India | 63.0 | 99.43% |
| ICICI Bank | 56.4 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 436.1 | 99.14% | 231 ms |
| Google Pay | 298.6 | 99.17% | 316 ms |
| Paytm | 73.8 | 99.06% | 192 ms |
| Navi | 33.7 | 99.17% | 225 ms |
| SuperMoney | 17.8 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 342.8 |
| Person to Person | 324.5 |
| QR Payments | 86.8 |
| UPI Lite | 43.9 |
| UPI Autopay | 30.2 |

## Failure analysis
- No incidents open. Technical declines are within the 0.3% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D109-MON) and any meetings/emails on 08 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D109-MON, RPT-D108-DAILY
