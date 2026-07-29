---
id: RPT-D175-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-12-13T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 13 Dec 2026)

**Report ID:** RPT-D175-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 13 Dec 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 175 of 180)

## Transaction summary
The rail processed 871.0M UPI transactions on Sunday — a quiet Sunday — up 12.5M on the same day last week. Success held at 99.98% and settlement at 99.36%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 871.0  (▼58.9 d/d, ▲12.5 w/w, ▲126.1 m/m)
- **Success Rate:** 99.98%  (▲0.38 m/m)
- **Settlement Success:** 99.36%  (▲0.13 d/d, ▼0.62 w/w, ▼0.07 m/m)
- **Technical Declines:** 0.23%  (▼0.01 d/d, ▼0.05 w/w, ▼0.22 m/m)
- **Business Declines:** 0.13%  (▼0.01 d/d, ▼0.07 m/m)
- **Customer Complaints:** 862  (▼8 d/d, ▼112 w/w, ▼1080 m/m)
- **Merchant Complaints:** 85  (▼12 d/d, ▼4 w/w, ▼126 m/m)
- **Fraud Alerts:** 677  (▼14 w/w, ▼374 m/m)
- **Risk Score:** 18  (▼13 m/m)
- **Response Time:** 535 ms  (▲5 d/d, ▼21 w/w, ▼207 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 280.0 | 99.5% |
| HDFC Bank | 96.1 | 99.55% |
| Bank of Baroda | 69.1 | 99.64% |
| Union Bank of India | 60.0 | 99.43% |
| ICICI Bank | 53.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 415.5 | 99.14% | 231 ms |
| Google Pay | 284.5 | 99.17% | 316 ms |
| Paytm | 70.3 | 99.06% | 192 ms |
| Navi | 32.1 | 99.17% | 225 ms |
| SuperMoney | 17.0 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 326.6 |
| Person to Person | 309.2 |
| QR Payments | 82.7 |
| UPI Lite | 41.8 |
| UPI Autopay | 28.7 |

## Failure analysis
- No incidents open. Technical declines are within the 0.23% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D175-MON) and any meetings/emails on 13 Dec.

Refs: upi_kpis_month.xlsx, TEAMS-D175-MON, RPT-D174-DAILY
