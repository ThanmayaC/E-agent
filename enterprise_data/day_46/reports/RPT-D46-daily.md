---
id: RPT-D46-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-06T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 06 Aug 2026)

**Report ID:** RPT-D46-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 06 Aug 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 46 of 180)

## Transaction summary
The rail processed 827.6M UPI transactions on Thursday — a steady mid-week day — down 77.8M on the same day last week. Success held at 98.63% and settlement at 99.77%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 827.6  (▲10.1 d/d, ▼77.8 w/w, ▲82.7 m/m)
- **Success Rate:** 98.63%  (▼1.06 d/d, ▼0.97 w/w, ▼0.97 m/m)
- **Settlement Success:** 99.77%  (▼0.21 d/d, ▲0.35 w/w, ▲0.34 m/m)
- **Technical Declines:** 0.38%  (▼0.01 w/w, ▼0.07 m/m)
- **Business Declines:** 0.18%  (▼0.02 m/m)
- **Customer Complaints:** 1,571  (▼19 d/d, ▼69 w/w, ▼371 m/m)
- **Merchant Complaints:** 167  (▼2 d/d, ▼7 w/w, ▼44 m/m)
- **Fraud Alerts:** 932  (▼17 d/d, ▼15 w/w, ▼119 m/m)
- **Risk Score:** 27  (▼4 m/m)
- **Response Time:** 679 ms  (▼1 d/d, ▼3 w/w, ▼63 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 266.1 | 99.5% |
| HDFC Bank | 91.3 | 99.55% |
| Bank of Baroda | 65.6 | 99.64% |
| Union Bank of India | 57.0 | 99.43% |
| ICICI Bank | 51.0 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 394.8 | 99.14% | 231 ms |
| Google Pay | 270.3 | 99.17% | 316 ms |
| Paytm | 66.8 | 99.06% | 192 ms |
| Navi | 30.5 | 99.17% | 225 ms |
| SuperMoney | 16.1 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 310.4 |
| Person to Person | 293.8 |
| QR Payments | 78.6 |
| UPI Lite | 39.7 |
| UPI Autopay | 27.3 |

## Failure analysis
- No incidents open. Technical declines are within the 0.38% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D46-MON) and any meetings/emails on 06 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D46-MON, RPT-D45-DAILY
