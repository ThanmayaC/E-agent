---
id: RPT-D150-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-18T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 18 Nov 2026)

**Report ID:** RPT-D150-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 18 Nov 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 150 of 180)

## Transaction summary
The rail processed 997.4M UPI transactions on Wednesday — a steady mid-week day — down 3.5M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 997.4  (▼18.1 d/d, ▼3.5 w/w, ▲252.5 m/m)
- **Success Rate:** 99.98%  (▲0.29 d/d, ▲0.24 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.55 m/m)
- **Technical Declines:** 0.25%  (▼0.01 d/d, ▼0.02 w/w, ▼0.2 m/m)
- **Business Declines:** 0.14%  (▼0.03 d/d, ▼0.06 m/m)
- **Customer Complaints:** 959  (▼127 d/d, ▼48 w/w, ▼983 m/m)
- **Merchant Complaints:** 97  (▼1 d/d, ▼4 w/w, ▼114 m/m)
- **Fraud Alerts:** 728  (▼84 d/d, ▼4 w/w, ▼323 m/m)
- **Risk Score:** 19  (▼6 d/d, ▼1 w/w, ▼12 m/m)
- **Response Time:** 559 ms  (▼1 d/d, ▼15 w/w, ▼183 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 320.7 | 99.5% |
| HDFC Bank | 110.0 | 99.55% |
| Bank of Baroda | 79.1 | 99.64% |
| Union Bank of India | 68.7 | 99.43% |
| ICICI Bank | 61.5 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 475.8 | 99.14% | 231 ms |
| Google Pay | 325.8 | 99.17% | 316 ms |
| Paytm | 80.5 | 99.06% | 192 ms |
| Navi | 36.8 | 99.17% | 225 ms |
| SuperMoney | 19.4 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 374.0 |
| Person to Person | 354.1 |
| QR Payments | 94.8 |
| UPI Lite | 47.9 |
| UPI Autopay | 32.9 |

## Failure analysis
- No incidents open. Technical declines are within the 0.25% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D150-MON) and any meetings/emails on 18 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D150-MON, RPT-D149-DAILY
