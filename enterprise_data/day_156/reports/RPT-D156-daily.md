---
id: RPT-D156-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-24T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 24 Nov 2026)

**Report ID:** RPT-D156-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 24 Nov 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 156 of 180)

## Transaction summary
The rail processed 1009.0M UPI transactions on Tuesday — a steady mid-week day — down 6.5M on the same day last week. Success held at 99.2% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1009.0  (▲20.3 d/d, ▼6.5 w/w, ▲264.1 m/m)
- **Success Rate:** 99.2%  (▼0.7 d/d, ▼0.49 w/w, ▼0.4 m/m)
- **Settlement Success:** 99.98%  (▲0.55 m/m)
- **Technical Declines:** 0.25%  (▼0.01 w/w, ▼0.2 m/m)
- **Business Declines:** 0.13%  (▼0.01 d/d, ▼0.04 w/w, ▼0.07 m/m)
- **Customer Complaints:** 943  (▼32 d/d, ▼143 w/w, ▼999 m/m)
- **Merchant Complaints:** 95  (▲1 d/d, ▼3 w/w, ▼116 m/m)
- **Fraud Alerts:** 717  (▼15 d/d, ▼95 w/w, ▼334 m/m)
- **Risk Score:** 19  (▼1 d/d, ▼6 w/w, ▼12 m/m)
- **Response Time:** 549 ms  (▼4 d/d, ▼11 w/w, ▼193 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 324.4 | 99.5% |
| HDFC Bank | 111.3 | 99.55% |
| Bank of Baroda | 80.0 | 99.64% |
| Union Bank of India | 69.5 | 99.43% |
| ICICI Bank | 62.2 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 481.4 | 99.14% | 231 ms |
| Google Pay | 329.6 | 99.17% | 316 ms |
| Paytm | 81.4 | 99.06% | 192 ms |
| Navi | 37.2 | 99.17% | 225 ms |
| SuperMoney | 19.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 378.4 |
| Person to Person | 358.2 |
| QR Payments | 95.9 |
| UPI Lite | 48.4 |
| UPI Autopay | 33.3 |

## Failure analysis
- No incidents open. Technical declines are within the 0.25% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D156-MON) and any meetings/emails on 24 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D156-MON, RPT-D155-DAILY
