---
id: RPT-D90-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-19T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 19 Sep 2026)

**Report ID:** RPT-D90-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 19 Sep 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 90 of 180)

## Transaction summary
The rail processed 790.7M UPI transactions on Saturday — a lighter Saturday — down 15.3M on the same day last week. Success held at 99.43% and settlement at 99.76%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 790.7  (▼116.8 d/d, ▼15.3 w/w, ▲45.8 m/m)
- **Success Rate:** 99.43%  (▲0.51 d/d, ▼0.38 w/w, ▼0.17 m/m)
- **Settlement Success:** 99.76%  (▲0.76 d/d, ▼0.22 w/w, ▲0.33 m/m)
- **Technical Declines:** 0.32%  (▼0.01 d/d, ▼0.01 w/w, ▼0.13 m/m)
- **Business Declines:** 0.16%  (▼0.04 m/m)
- **Customer Complaints:** 1,290  (▼19 d/d, ▼43 w/w, ▼652 m/m)
- **Merchant Complaints:** 131  (▼2 d/d, ▼7 w/w, ▼80 m/m)
- **Fraud Alerts:** 843  (▼8 d/d, ▼7 w/w, ▼208 m/m)
- **Risk Score:** 23  (▼1 d/d, ▼1 w/w, ▼8 m/m)
- **Response Time:** 626 ms  (▼2 d/d, ▼5 w/w, ▼116 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 254.2 | 99.5% |
| HDFC Bank | 87.2 | 99.55% |
| Bank of Baroda | 62.7 | 99.64% |
| Union Bank of India | 54.5 | 99.43% |
| ICICI Bank | 48.8 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 377.2 | 99.14% | 231 ms |
| Google Pay | 258.3 | 99.17% | 316 ms |
| Paytm | 63.8 | 99.06% | 192 ms |
| Navi | 29.1 | 99.17% | 225 ms |
| SuperMoney | 15.4 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 296.5 |
| Person to Person | 280.7 |
| QR Payments | 75.1 |
| UPI Lite | 38.0 |
| UPI Autopay | 26.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.32% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D90-MON) and any meetings/emails on 19 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D90-MON, RPT-D89-DAILY
