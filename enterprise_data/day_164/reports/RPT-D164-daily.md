---
id: RPT-D164-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-12-02T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 02 Dec 2026)

**Report ID:** RPT-D164-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 02 Dec 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 164 of 180)

## Transaction summary
The rail processed 1034.5M UPI transactions on Wednesday — a steady mid-week day — up 16.7M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1034.5  (▼15.1 d/d, ▲16.7 w/w, ▲289.6 m/m)
- **Success Rate:** 99.98%  (▲0.02 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.45 d/d, ▲0.55 m/m)
- **Technical Declines:** 0.24%  (▼0.01 w/w, ▼0.21 m/m)
- **Business Declines:** 0.13%  (▼0.01 w/w, ▼0.07 m/m)
- **Customer Complaints:** 899  (▼6 d/d, ▼36 w/w, ▼1043 m/m)
- **Merchant Complaints:** 90  (▼1 d/d, ▼3 w/w, ▼121 m/m)
- **Fraud Alerts:** 698  (▼1 d/d, ▼15 w/w, ▼353 m/m)
- **Risk Score:** 19  (▼12 m/m)
- **Response Time:** 541 ms  (▼11 w/w, ▼201 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 332.6 | 99.5% |
| HDFC Bank | 114.1 | 99.55% |
| Bank of Baroda | 82.0 | 99.64% |
| Union Bank of India | 71.3 | 99.43% |
| ICICI Bank | 63.8 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 493.5 | 99.14% | 231 ms |
| Google Pay | 337.9 | 99.17% | 316 ms |
| Paytm | 83.5 | 99.06% | 192 ms |
| Navi | 38.1 | 99.17% | 225 ms |
| SuperMoney | 20.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 387.9 |
| Person to Person | 367.2 |
| QR Payments | 98.3 |
| UPI Lite | 49.7 |
| UPI Autopay | 34.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.24% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D164-MON) and any meetings/emails on 02 Dec.

Refs: upi_kpis_month.xlsx, TEAMS-D164-MON, RPT-D163-DAILY
