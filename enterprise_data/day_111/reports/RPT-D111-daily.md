---
id: RPT-D111-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-10T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 10 Oct 2026)

**Report ID:** RPT-D111-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 10 Oct 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 111 of 180)

## Transaction summary
The rail processed 848.7M UPI transactions on Saturday — a lighter Saturday — up 27.2M on the same day last week. Success held at 99.21% and settlement at 99.3%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 848.7  (▼53.2 d/d, ▲27.2 w/w, ▲103.8 m/m)
- **Success Rate:** 99.21%  (▼0.2 d/d, ▼0.63 w/w, ▼0.39 m/m)
- **Settlement Success:** 99.3%  (▼0.68 d/d, ▲0.36 w/w, ▼0.13 m/m)
- **Technical Declines:** 0.3%  (▼0.15 m/m)
- **Business Declines:** 0.15%  (▼0.01 w/w, ▼0.05 m/m)
- **Customer Complaints:** 1,155  (▼14 d/d, ▼59 w/w, ▼787 m/m)
- **Merchant Complaints:** 119  (▼12 w/w, ▼92 m/m)
- **Fraud Alerts:** 795  (▼11 d/d, ▼15 w/w, ▼256 m/m)
- **Risk Score:** 22  (▼9 m/m)
- **Response Time:** 600 ms  (▼1 d/d, ▼13 w/w, ▼142 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 272.9 | 99.5% |
| HDFC Bank | 93.6 | 99.55% |
| Bank of Baroda | 67.3 | 99.64% |
| Union Bank of India | 58.5 | 99.43% |
| ICICI Bank | 52.3 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 404.9 | 99.14% | 231 ms |
| Google Pay | 277.2 | 99.17% | 316 ms |
| Paytm | 68.5 | 99.06% | 192 ms |
| Navi | 31.3 | 99.17% | 225 ms |
| SuperMoney | 16.5 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 318.3 |
| Person to Person | 301.3 |
| QR Payments | 80.6 |
| UPI Lite | 40.7 |
| UPI Autopay | 28.0 |

## Failure analysis
- No incidents open. Technical declines are within the 0.3% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D111-MON) and any meetings/emails on 10 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D111-MON, RPT-D110-DAILY
