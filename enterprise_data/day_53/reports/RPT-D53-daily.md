---
id: RPT-D53-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-13T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 13 Aug 2026)

**Report ID:** RPT-D53-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 13 Aug 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 53 of 180)

## Transaction summary
The rail processed 831.5M UPI transactions on Thursday — a steady mid-week day — up 3.9M on the same day last week. Success held at 99.34% and settlement at 99.01%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 831.5  (▲0.7 d/d, ▲3.9 w/w, ▲86.6 m/m)
- **Success Rate:** 99.34%  (▼0.64 d/d, ▲0.71 w/w, ▼0.26 m/m)
- **Settlement Success:** 99.01%  (▼0.81 d/d, ▼0.76 w/w, ▼0.42 m/m)
- **Technical Declines:** 0.37%  (▼0.01 w/w, ▼0.08 m/m)
- **Business Declines:** 0.17%  (▼0.01 d/d, ▼0.01 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,519  (▼14 d/d, ▼52 w/w, ▼423 m/m)
- **Merchant Complaints:** 160  (▼2 d/d, ▼7 w/w, ▼51 m/m)
- **Fraud Alerts:** 915  (▼15 d/d, ▼17 w/w, ▼136 m/m)
- **Risk Score:** 26  (▼1 w/w, ▼5 m/m)
- **Response Time:** 672 ms  (▲5 d/d, ▼7 w/w, ▼70 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 267.3 | 99.5% |
| HDFC Bank | 91.7 | 99.55% |
| Bank of Baroda | 65.9 | 99.64% |
| Union Bank of India | 57.3 | 99.43% |
| ICICI Bank | 51.3 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 396.7 | 99.14% | 231 ms |
| Google Pay | 271.6 | 99.17% | 316 ms |
| Paytm | 67.1 | 99.06% | 192 ms |
| Navi | 30.6 | 99.17% | 225 ms |
| SuperMoney | 16.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 311.8 |
| Person to Person | 295.2 |
| QR Payments | 79.0 |
| UPI Lite | 39.9 |
| UPI Autopay | 27.4 |

## Failure analysis
- No incidents open. Technical declines are within the 0.37% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D53-MON) and any meetings/emails on 13 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D53-MON, RPT-D52-DAILY
