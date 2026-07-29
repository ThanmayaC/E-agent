---
id: RPT-D137-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-05T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 05 Nov 2026)

**Report ID:** RPT-D137-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 05 Nov 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 137 of 180)

## Transaction summary
The rail processed 986.9M UPI transactions on Thursday — a steady mid-week day — down 101.9M on the same day last week. Success held at 99.05% and settlement at 99.63%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 986.9  (▲37.9 d/d, ▼101.9 w/w, ▲242.0 m/m)
- **Success Rate:** 99.05%  (▼0.53 d/d, ▼0.6 w/w, ▼0.55 m/m)
- **Settlement Success:** 99.63%  (▼0.17 d/d, ▼0.35 w/w, ▲0.2 m/m)
- **Technical Declines:** 0.27%  (▼0.02 w/w, ▼0.18 m/m)
- **Business Declines:** 0.14%  (▼0.03 d/d, ▼0.04 w/w, ▼0.06 m/m)
- **Customer Complaints:** 1,021  (▼90 d/d, ▼102 w/w, ▼921 m/m)
- **Merchant Complaints:** 104  (▼50 d/d, ▼53 w/w, ▼107 m/m)
- **Fraud Alerts:** 745  (▲1 d/d, ▼15 w/w, ▼306 m/m)
- **Risk Score:** 20  (▼1 w/w, ▼11 m/m)
- **Response Time:** 573 ms  (▼9 w/w, ▼169 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 317.3 | 99.5% |
| HDFC Bank | 108.9 | 99.55% |
| Bank of Baroda | 78.3 | 99.64% |
| Union Bank of India | 68.0 | 99.43% |
| ICICI Bank | 60.8 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 470.8 | 99.14% | 231 ms |
| Google Pay | 322.4 | 99.17% | 316 ms |
| Paytm | 79.6 | 99.06% | 192 ms |
| Navi | 36.4 | 99.17% | 225 ms |
| SuperMoney | 19.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 370.1 |
| Person to Person | 350.3 |
| QR Payments | 93.8 |
| UPI Lite | 47.4 |
| UPI Autopay | 32.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.27% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D137-MON) and any meetings/emails on 05 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D137-MON, RPT-D136-DAILY
