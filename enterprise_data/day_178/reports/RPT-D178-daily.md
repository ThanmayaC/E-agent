---
id: RPT-D178-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-12-16T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 16 Dec 2026)

**Report ID:** RPT-D178-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 16 Dec 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 178 of 180)

## Transaction summary
The rail processed 1061.7M UPI transactions on Wednesday — a steady mid-week day — up 25.4M on the same day last week. Success held at 99.98% and settlement at 99.11%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1061.7  (▲8.0 d/d, ▲25.4 w/w, ▲316.8 m/m)
- **Success Rate:** 99.98%  (▲0.57 d/d, ▲0.38 m/m)
- **Settlement Success:** 99.11%  (▼0.56 d/d, ▼0.64 w/w, ▼0.32 m/m)
- **Technical Declines:** 0.23%  (▼0.01 w/w, ▼0.22 m/m)
- **Business Declines:** 0.13%  (▼0.04 w/w, ▼0.07 m/m)
- **Customer Complaints:** 853  (▼133 w/w, ▼1089 m/m)
- **Merchant Complaints:** 84  (▼1 d/d, ▼72 w/w, ▼127 m/m)
- **Fraud Alerts:** 670  (▼6 d/d, ▼24 w/w, ▼381 m/m)
- **Risk Score:** 18  (▼13 m/m)
- **Response Time:** 529 ms  (▲3 d/d, ▼5 w/w, ▼213 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 341.4 | 99.5% |
| HDFC Bank | 117.1 | 99.55% |
| Bank of Baroda | 84.2 | 99.64% |
| Union Bank of India | 73.1 | 99.43% |
| ICICI Bank | 65.5 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 506.5 | 99.14% | 231 ms |
| Google Pay | 346.8 | 99.17% | 316 ms |
| Paytm | 85.7 | 99.06% | 192 ms |
| Navi | 39.1 | 99.17% | 225 ms |
| SuperMoney | 20.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 398.1 |
| Person to Person | 376.9 |
| QR Payments | 100.9 |
| UPI Lite | 51.0 |
| UPI Autopay | 35.0 |

## Failure analysis
- No incidents open. Technical declines are within the 0.23% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D178-MON) and any meetings/emails on 16 Dec.

Refs: upi_kpis_month.xlsx, TEAMS-D178-MON, RPT-D177-DAILY
