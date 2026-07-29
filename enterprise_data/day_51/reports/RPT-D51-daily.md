---
id: RPT-D51-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-11T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 11 Aug 2026)

**Report ID:** RPT-D51-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 11 Aug 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 51 of 180)

## Transaction summary
The rail processed 807.5M UPI transactions on Tuesday — a steady mid-week day — down 0.9M on the same day last week. Success held at 99.98% and settlement at 98.9%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 807.5  (▲16.8 d/d, ▼0.9 w/w, ▲62.6 m/m)
- **Success Rate:** 99.98%  (▲0.14 d/d, ▲0.2 w/w, ▲0.38 m/m)
- **Settlement Success:** 98.9%  (▼1.08 d/d, ▼0.53 w/w, ▼0.53 m/m)
- **Technical Declines:** 0.37%  (▼0.01 w/w, ▼0.08 m/m)
- **Business Declines:** 0.18%  (▼0.03 w/w, ▼0.02 m/m)
- **Customer Complaints:** 1,553  (▼3 d/d, ▼173 w/w, ▼389 m/m)
- **Merchant Complaints:** 163  (▼84 w/w, ▼48 m/m)
- **Fraud Alerts:** 925  (▼6 d/d, ▼24 w/w, ▼126 m/m)
- **Risk Score:** 27  (▲1 d/d, ▼4 m/m)
- **Response Time:** 664 ms  (▼5 d/d, ▼15 w/w, ▼78 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 259.6 | 99.5% |
| HDFC Bank | 89.1 | 99.55% |
| Bank of Baroda | 64.0 | 99.64% |
| Union Bank of India | 55.6 | 99.43% |
| ICICI Bank | 49.8 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 385.2 | 99.14% | 231 ms |
| Google Pay | 263.8 | 99.17% | 316 ms |
| Paytm | 65.1 | 99.06% | 192 ms |
| Navi | 29.8 | 99.17% | 225 ms |
| SuperMoney | 15.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 302.8 |
| Person to Person | 286.7 |
| QR Payments | 76.7 |
| UPI Lite | 38.8 |
| UPI Autopay | 26.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.37% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D51-MON) and any meetings/emails on 11 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D51-MON, RPT-D50-DAILY
