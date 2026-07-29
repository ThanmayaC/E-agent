---
id: RPT-D179-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-12-17T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 17 Dec 2026)

**Report ID:** RPT-D179-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 17 Dec 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 179 of 180)

## Transaction summary
The rail processed 1290.1M UPI transactions on Thursday — a campaign-driven high-volume day — up 237.4M on the same day last week. Success held at 99.5% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1290.1  (▲228.4 d/d, ▲237.4 w/w, ▲545.2 m/m)
- **Success Rate:** 99.5%  (▼0.48 d/d, ▼0.48 w/w, ▼0.1 m/m)
- **Settlement Success:** 99.98%  (▲0.87 d/d, ▲0.43 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.23%  (▼0.22 m/m)
- **Business Declines:** 0.13%  (▼0.02 w/w, ▼0.07 m/m)
- **Customer Complaints:** 850  (▼3 d/d, ▼77 w/w, ▼1092 m/m)
- **Merchant Complaints:** 84  (▼45 w/w, ▼127 m/m)
- **Fraud Alerts:** 672  (▲2 d/d, ▼20 w/w, ▼379 m/m)
- **Risk Score:** 18  (▼13 m/m)
- **Response Time:** 532 ms  (▲3 d/d, ▼3 w/w, ▼210 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 414.8 | 99.5% |
| HDFC Bank | 142.3 | 99.55% |
| Bank of Baroda | 102.3 | 99.64% |
| Union Bank of India | 88.9 | 99.43% |
| ICICI Bank | 79.5 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 615.5 | 99.14% | 231 ms |
| Google Pay | 421.4 | 99.17% | 316 ms |
| Paytm | 104.1 | 99.06% | 192 ms |
| Navi | 47.5 | 99.17% | 225 ms |
| SuperMoney | 25.1 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 483.8 |
| Person to Person | 458.0 |
| QR Payments | 122.6 |
| UPI Lite | 61.9 |
| UPI Autopay | 42.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.23% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D179-MON) and any meetings/emails on 17 Dec.

Refs: upi_kpis_month.xlsx, TEAMS-D179-MON, RPT-D178-DAILY
