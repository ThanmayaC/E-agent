---
id: RPT-D177-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-12-15T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 15 Dec 2026)

**Report ID:** RPT-D177-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 15 Dec 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 177 of 180)

## Transaction summary
The rail processed 1053.7M UPI transactions on Tuesday — a steady mid-week day — up 3.7M on the same day last week. Success held at 99.41% and settlement at 99.67%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1053.7  (▲43.0 d/d, ▲3.7 w/w, ▲308.8 m/m)
- **Success Rate:** 99.41%  (▼0.21 d/d, ▼0.57 w/w, ▼0.19 m/m)
- **Settlement Success:** 99.67%  (▼0.05 d/d, ▲0.17 w/w, ▲0.24 m/m)
- **Technical Declines:** 0.23%  (▼0.01 w/w, ▼0.22 m/m)
- **Business Declines:** 0.13%  (▼0.07 m/m)
- **Customer Complaints:** 853  (▲2 d/d, ▼46 w/w, ▼1089 m/m)
- **Merchant Complaints:** 85  (▼3 w/w, ▼126 m/m)
- **Fraud Alerts:** 676  (▼9 d/d, ▼11 w/w, ▼375 m/m)
- **Risk Score:** 18  (▼13 m/m)
- **Response Time:** 526 ms  (▼19 w/w, ▼216 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 338.8 | 99.5% |
| HDFC Bank | 116.2 | 99.55% |
| Bank of Baroda | 83.6 | 99.64% |
| Union Bank of India | 72.6 | 99.43% |
| ICICI Bank | 65.0 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 502.7 | 99.14% | 231 ms |
| Google Pay | 344.2 | 99.17% | 316 ms |
| Paytm | 85.0 | 99.06% | 192 ms |
| Navi | 38.8 | 99.17% | 225 ms |
| SuperMoney | 20.5 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 395.1 |
| Person to Person | 374.1 |
| QR Payments | 100.1 |
| UPI Lite | 50.6 |
| UPI Autopay | 34.8 |

## Failure analysis
- No incidents open. Technical declines are within the 0.23% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D177-MON) and any meetings/emails on 15 Dec.

Refs: upi_kpis_month.xlsx, TEAMS-D177-MON, RPT-D176-DAILY
