---
id: RPT-D45-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-05T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 05 Aug 2026)

**Report ID:** RPT-D45-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 05 Aug 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 45 of 180)

## Transaction summary
The rail processed 817.5M UPI transactions on Wednesday — a steady mid-week day — down 93.2M on the same day last week. Success held at 99.69% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 817.5  (▲9.1 d/d, ▼93.2 w/w, ▲72.6 m/m)
- **Success Rate:** 99.69%  (▼0.09 d/d, ▼0.29 w/w, ▲0.09 m/m)
- **Settlement Success:** 99.98%  (▲0.55 d/d, ▲0.55 m/m)
- **Technical Declines:** 0.38%  (▼0.02 w/w, ▼0.07 m/m)
- **Business Declines:** 0.18%  (▼0.03 d/d, ▼0.03 w/w, ▼0.02 m/m)
- **Customer Complaints:** 1,590  (▼136 d/d, ▼206 w/w, ▼352 m/m)
- **Merchant Complaints:** 169  (▼78 d/d, ▼80 w/w, ▼42 m/m)
- **Fraud Alerts:** 949  (▼16 w/w, ▼102 m/m)
- **Risk Score:** 27  (▼1 w/w, ▼4 m/m)
- **Response Time:** 680 ms  (▲1 d/d, ▼7 w/w, ▼62 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 262.8 | 99.5% |
| HDFC Bank | 90.2 | 99.55% |
| Bank of Baroda | 64.8 | 99.64% |
| Union Bank of India | 56.3 | 99.43% |
| ICICI Bank | 50.4 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 390.0 | 99.14% | 231 ms |
| Google Pay | 267.0 | 99.17% | 316 ms |
| Paytm | 66.0 | 99.06% | 192 ms |
| Navi | 30.1 | 99.17% | 225 ms |
| SuperMoney | 15.9 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 306.6 |
| Person to Person | 290.2 |
| QR Payments | 77.7 |
| UPI Lite | 39.2 |
| UPI Autopay | 27.0 |

## Failure analysis
- No incidents open. Technical declines are within the 0.38% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D45-MON) and any meetings/emails on 05 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D45-MON, RPT-D44-DAILY
