---
id: RPT-D50-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-10T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 10 Aug 2026)

**Report ID:** RPT-D50-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 10 Aug 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 50 of 180)

## Transaction summary
The rail processed 790.7M UPI transactions on Monday — the Monday ramp-up after the weekend — up 14.8M on the same day last week. Success held at 99.84% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 790.7  (▲126.6 d/d, ▲14.8 w/w, ▲45.8 m/m)
- **Success Rate:** 99.84%  (▼0.14 d/d, ▲1.11 w/w, ▲0.24 m/m)
- **Settlement Success:** 99.98%  (▲0.31 d/d, ▲0.19 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.37%  (▼0.01 d/d, ▼0.02 w/w, ▼0.08 m/m)
- **Business Declines:** 0.18%  (▼0.05 w/w, ▼0.02 m/m)
- **Customer Complaints:** 1,556  (▼1 d/d, ▼240 w/w, ▼386 m/m)
- **Merchant Complaints:** 163  (▼139 w/w, ▼48 m/m)
- **Fraud Alerts:** 931  (▲2 d/d, ▼7 w/w, ▼120 m/m)
- **Risk Score:** 26  (▼1 d/d, ▼1 w/w, ▼5 m/m)
- **Response Time:** 669 ms  (▲1 d/d, ▼7 w/w, ▼73 m/m)

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
- No incidents open. Technical declines are within the 0.37% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D50-MON) and any meetings/emails on 10 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D50-MON, RPT-D49-DAILY
