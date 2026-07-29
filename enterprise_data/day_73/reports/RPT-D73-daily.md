---
id: RPT-D73-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-02T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 02 Sep 2026)

**Report ID:** RPT-D73-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 02 Sep 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 73 of 180)

## Transaction summary
The rail processed 854.7M UPI transactions on Wednesday — a steady mid-week day — down 15.4M on the same day last week. Success held at 99.98% and settlement at 98.92%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 854.7  (▼7.1 d/d, ▼15.4 w/w, ▲109.8 m/m)
- **Success Rate:** 99.98%  (▲0.06 w/w, ▲0.38 m/m)
- **Settlement Success:** 98.92%  (▼1.06 d/d, ▼1.06 w/w, ▼0.51 m/m)
- **Technical Declines:** 0.34%  (▼0.01 d/d, ▼0.01 w/w, ▼0.11 m/m)
- **Business Declines:** 0.17%  (▼0.04 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,402  (▲5 d/d, ▼46 w/w, ▼540 m/m)
- **Merchant Complaints:** 143  (▼3 d/d, ▼62 w/w, ▼68 m/m)
- **Fraud Alerts:** 878  (▼9 d/d, ▼19 w/w, ▼173 m/m)
- **Risk Score:** 25  (▼6 m/m)
- **Response Time:** 638 ms  (▼11 d/d, ▼9 w/w, ▼104 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 274.8 | 99.5% |
| HDFC Bank | 94.3 | 99.55% |
| Bank of Baroda | 67.8 | 99.64% |
| Union Bank of India | 58.9 | 99.43% |
| ICICI Bank | 52.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 407.8 | 99.14% | 231 ms |
| Google Pay | 279.2 | 99.17% | 316 ms |
| Paytm | 69.0 | 99.06% | 192 ms |
| Navi | 31.5 | 99.17% | 225 ms |
| SuperMoney | 16.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 320.5 |
| Person to Person | 303.4 |
| QR Payments | 81.2 |
| UPI Lite | 41.0 |
| UPI Autopay | 28.2 |

## Failure analysis
- No incidents open. Technical declines are within the 0.34% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D73-MON) and any meetings/emails on 02 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D73-MON, RPT-D72-DAILY
