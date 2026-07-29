---
id: RPT-D157-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-25T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 25 Nov 2026)

**Report ID:** RPT-D157-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 25 Nov 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 157 of 180)

## Transaction summary
The rail processed 1017.8M UPI transactions on Wednesday — a steady mid-week day — up 20.4M on the same day last week. Success held at 99.96% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1017.8  (▲8.8 d/d, ▲20.4 w/w, ▲272.9 m/m)
- **Success Rate:** 99.96%  (▲0.76 d/d, ▼0.02 w/w, ▲0.36 m/m)
- **Settlement Success:** 99.98%  (▲0.55 m/m)
- **Technical Declines:** 0.25%  (▼0.2 m/m)
- **Business Declines:** 0.14%  (▲0.01 d/d, ▼0.06 m/m)
- **Customer Complaints:** 935  (▼8 d/d, ▼24 w/w, ▼1007 m/m)
- **Merchant Complaints:** 93  (▼2 d/d, ▼4 w/w, ▼118 m/m)
- **Fraud Alerts:** 713  (▼4 d/d, ▼15 w/w, ▼338 m/m)
- **Risk Score:** 19  (▼12 m/m)
- **Response Time:** 552 ms  (▲3 d/d, ▼7 w/w, ▼190 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 327.2 | 99.5% |
| HDFC Bank | 112.3 | 99.55% |
| Bank of Baroda | 80.7 | 99.64% |
| Union Bank of India | 70.1 | 99.43% |
| ICICI Bank | 62.8 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 485.6 | 99.14% | 231 ms |
| Google Pay | 332.4 | 99.17% | 316 ms |
| Paytm | 82.1 | 99.06% | 192 ms |
| Navi | 37.5 | 99.17% | 225 ms |
| SuperMoney | 19.8 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 381.7 |
| Person to Person | 361.3 |
| QR Payments | 96.7 |
| UPI Lite | 48.9 |
| UPI Autopay | 33.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.25% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D157-MON) and any meetings/emails on 25 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D157-MON, RPT-D156-DAILY
