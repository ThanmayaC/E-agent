---
id: RPT-D92-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-21T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 21 Sep 2026)

**Report ID:** RPT-D92-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 21 Sep 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 92 of 180)

## Transaction summary
The rail processed 851.3M UPI transactions on Monday — the Monday ramp-up after the weekend — up 8.5M on the same day last week. Success held at 99.35% and settlement at 99.81%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 851.3  (▲115.4 d/d, ▲8.5 w/w, ▲106.4 m/m)
- **Success Rate:** 99.35%  (▼0.63 d/d, ▲0.33 w/w, ▼0.25 m/m)
- **Settlement Success:** 99.81%  (▼0.17 d/d, ▲0.26 w/w, ▲0.38 m/m)
- **Technical Declines:** 0.32%  (▼0.11 w/w, ▼0.13 m/m)
- **Business Declines:** 0.16%  (▼0.04 m/m)
- **Customer Complaints:** 1,262  (▼6 d/d, ▼389 w/w, ▼680 m/m)
- **Merchant Complaints:** 132  (▲1 d/d, ▼4 w/w, ▼79 m/m)
- **Fraud Alerts:** 840  (▲2 d/d, ▼14 w/w, ▼211 m/m)
- **Risk Score:** 23  (▼1 w/w, ▼8 m/m)
- **Response Time:** 623 ms  (▲1 d/d, ▼84 w/w, ▼119 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 273.7 | 99.5% |
| HDFC Bank | 93.9 | 99.55% |
| Bank of Baroda | 67.5 | 99.64% |
| Union Bank of India | 58.6 | 99.43% |
| ICICI Bank | 52.5 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 406.1 | 99.14% | 231 ms |
| Google Pay | 278.1 | 99.17% | 316 ms |
| Paytm | 68.7 | 99.06% | 192 ms |
| Navi | 31.4 | 99.17% | 225 ms |
| SuperMoney | 16.6 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 319.2 |
| Person to Person | 302.2 |
| QR Payments | 80.9 |
| UPI Lite | 40.9 |
| UPI Autopay | 28.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.32% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D92-MON) and any meetings/emails on 21 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D92-MON, RPT-D91-DAILY
